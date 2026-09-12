#!/usr/bin/env python3
"""Validate the structural and safety invariants of an M365 tenant catalog."""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path
from typing import Any

try:
    import yaml
except ImportError:  # pragma: no cover - dependency error is user-facing
    yaml = None


SECRET_KEY = re.compile(
    r"(^|_)(password|passwd|secret|token|private_key|client_secret|recovery_code)s?($|_)",
    re.IGNORECASE,
)
SAFE_CREDENTIAL_POLICY_KEYS = {
    "change_temporary_password",
    "require_password_change",
    "password_change_required",
}
PROFILE_SECTIONS = {
    "identity",
    "licenses",
    "groups",
    "exchange",
    "collaboration",
    "intune",
    "power_automate",
    "first_sign_in",
}


def load_catalog(path: Path) -> Any:
    if yaml is None:
        raise RuntimeError(
            "PyYAML is required. Install scripts/requirements.txt in an isolated environment."
        )
    with path.open("r", encoding="utf-8") as handle:
        return yaml.safe_load(handle)


def walk_for_secrets(value: Any, location: str, errors: list[str]) -> None:
    if isinstance(value, dict):
        for key, child in value.items():
            child_location = f"{location}.{key}" if location else str(key)
            is_safe_policy = (
                str(key).lower() in SAFE_CREDENTIAL_POLICY_KEYS
                and isinstance(child, bool)
            )
            if SECRET_KEY.search(str(key)) and not is_safe_policy:
                errors.append(f"secret-bearing key is forbidden: {child_location}")
            walk_for_secrets(child, child_location, errors)
    elif isinstance(value, list):
        for index, child in enumerate(value):
            walk_for_secrets(child, f"{location}[{index}]", errors)


def validate_profiles(profiles: Any, errors: list[str], warnings: list[str]) -> None:
    if not isinstance(profiles, dict) or not profiles:
        errors.append("profiles must be a non-empty mapping")
        return

    for name, profile in profiles.items():
        prefix = f"profiles.{name}"
        if not isinstance(name, str) or not re.fullmatch(r"[a-z0-9][a-z0-9-]*", name):
            errors.append(f"invalid profile name: {name!r}")
        if not isinstance(profile, dict):
            errors.append(f"{prefix} must be a mapping")
            continue
        extends = profile.get("extends", [])
        if isinstance(extends, str):
            extends = [extends]
        if not isinstance(extends, list) or not all(isinstance(item, str) for item in extends):
            errors.append(f"{prefix}.extends must be a list of profile names")
            extends = []
        for parent in extends:
            if parent not in profiles:
                errors.append(f"{prefix}.extends references unknown profile {parent!r}")
        if not PROFILE_SECTIONS.intersection(profile):
            warnings.append(f"{prefix} has no entitlement or identity sections")

    visiting: set[str] = set()
    visited: set[str] = set()

    def visit(name: str, trail: list[str]) -> None:
        if name in visiting:
            errors.append("profile inheritance cycle: " + " -> ".join(trail + [name]))
            return
        if name in visited:
            return
        visiting.add(name)
        profile = profiles.get(name, {})
        parents = profile.get("extends", []) if isinstance(profile, dict) else []
        if isinstance(parents, str):
            parents = [parents]
        if isinstance(parents, list):
            for parent in parents:
                if isinstance(parent, str) and parent in profiles:
                    visit(parent, trail + [name])
        visiting.remove(name)
        visited.add(name)

    for profile_name in profiles:
        visit(profile_name, [])


def validate_catalog(data: Any) -> tuple[list[str], list[str]]:
    errors: list[str] = []
    warnings: list[str] = []

    if not isinstance(data, dict):
        return ["catalog root must be a mapping"], warnings
    if data.get("schema_version") != 1:
        errors.append("schema_version must be 1")

    tenant = data.get("tenant")
    if not isinstance(tenant, dict):
        errors.append("tenant must be a mapping")
    else:
        domain = tenant.get("primary_domain")
        if not isinstance(domain, str) or "." not in domain:
            errors.append("tenant.primary_domain must be a domain name")
        if not tenant.get("display_name"):
            warnings.append("tenant.display_name is missing")

    validate_profiles(data.get("profiles"), errors, warnings)
    walk_for_secrets(data, "", errors)
    return errors, warnings


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("catalog", type=Path)
    args = parser.parse_args()

    try:
        data = load_catalog(args.catalog)
    except (OSError, RuntimeError, ValueError) as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        return 2

    errors, warnings = validate_catalog(data)
    for warning in warnings:
        print(f"WARNING: {warning}")
    for error in errors:
        print(f"ERROR: {error}", file=sys.stderr)

    if errors:
        print(f"Catalog invalid: {len(errors)} error(s), {len(warnings)} warning(s)")
        return 1
    print(f"Catalog valid: {len(warnings)} warning(s)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
