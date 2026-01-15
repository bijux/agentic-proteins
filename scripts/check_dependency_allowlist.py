# SPDX-License-Identifier: Apache-2.0
# Copyright © 2025 Bijan Mousavi

from __future__ import annotations

from pathlib import Path
import re
import sys
import tomllib


def _normalize(dep: str) -> str:
    match = re.match(r"([A-Za-z0-9_.-]+)", dep.strip())
    return match.group(1).lower() if match else dep.strip().lower()


def main() -> int:
    pyproject = Path("pyproject.toml")
    allowlist_path = Path("docs/security/dependencies.md")
    if not pyproject.exists():
        print("pyproject.toml missing.", file=sys.stderr)
        return 1
    if not allowlist_path.exists():
        print("Allowlist missing: docs/security/dependencies.md", file=sys.stderr)
        return 1
    data = tomllib.loads(pyproject.read_text())
    deps = data.get("project", {}).get("dependencies", [])
    required = {_normalize(dep) for dep in deps}
    allowlist = set()
    for line in allowlist_path.read_text().splitlines():
        stripped = line.strip()
        if stripped.startswith("- "):
            allowlist.add(stripped[2:].strip().lower())
    missing = sorted(required - allowlist)
    if missing:
        print("Dependencies missing from allowlist:", file=sys.stderr)
        for item in missing:
            print(f"- {item}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
