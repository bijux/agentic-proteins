#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
# Copyright © 2025 Bijan Mousavi

"""Documentation consistency gate."""

from __future__ import annotations

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DOCS_DIR = ROOT / "docs"
SRC_DIR = ROOT / "src" / "agentic_proteins"

MODULE_RE = re.compile(r"agentic_proteins\.[A-Za-z0-9_\.]+")
SRC_PATH_RE = re.compile(r"src/agentic_proteins/[A-Za-z0-9_\-/\.]+")
MKDOCS_RE = re.compile(r"([A-Za-z0-9_./-]+\.md)")
REQUIRED_MODULE_DOCS = {
    "agents": "concepts/agent.md",
    "contracts": "architecture/architecture.md",
    "core": "architecture/architecture.md",
    "design_loop": "execution/design-loop.md",
    "domain": "evaluation/selection.md",
    "execution": "execution/execution-model.md",
    "interfaces": "cli/cli.md",
    "memory": "architecture/architecture.md",
    "providers": "architecture/architecture.md",
    "registry": "architecture/architecture.md",
    "report": "evaluation/selection.md",
    "runtime": "architecture/architecture.md",
    "state": "artifact/provenance.md",
    "tools": "execution/execution-model.md",
    "validation": "architecture/architecture.md",
}
FUTURE_WORDS = re.compile(
    r"\b(will|planned|future|soon|upcoming|later|tbd)\b", re.IGNORECASE
)


def _module_index() -> set[str]:
    modules: set[str] = {"agentic_proteins"}
    for path in SRC_DIR.rglob("*.py"):
        rel = path.relative_to(SRC_DIR)
        parts = list(rel.parts)
        if parts[-1] == "__init__.py":
            parts = parts[:-1]
        else:
            parts[-1] = parts[-1][:-3]
        if not parts:
            continue
        modules.add("agentic_proteins." + ".".join(parts))
    return modules


def _path_exists(path_str: str) -> bool:
    return (ROOT / path_str).exists()


def main() -> int:
    if not DOCS_DIR.exists():
        print("docs/ missing")
        return 1

    mkdocs_path = ROOT / "mkdocs.yml"
    nav_refs: set[Path] = set()
    if mkdocs_path.exists():
        mkdocs_text = mkdocs_path.read_text()
        for entry in MKDOCS_RE.findall(mkdocs_text):
            nav_refs.add(Path(entry))

    modules = _module_index()
    failures: list[str] = []

    if mkdocs_path.exists():
        for ref in sorted(nav_refs):
            if ref.parts and ref.parts[0] == "docs":
                failures.append(f"nav_ref_outside_docs: {ref}")
                continue
            if not (DOCS_DIR / ref).exists():
                failures.append(f"missing_nav_ref: {ref}")

    for path in DOCS_DIR.rglob("*"):
        if path.is_dir() and path.name == "artifacts":
            failures.append(f"forbidden_docs_dir: {path.relative_to(DOCS_DIR)}")
        if path.is_dir():
            md_files = [p.name for p in path.glob("*.md")]
            if path != DOCS_DIR and md_files == ["index.md"]:
                failures.append(
                    f"index_only_dir: {path.relative_to(DOCS_DIR)}"
                )

    for module, doc_path in REQUIRED_MODULE_DOCS.items():
        if not (DOCS_DIR / doc_path).exists():
            failures.append(f"missing_module_doc: {module} -> {doc_path}")

    for doc in sorted(DOCS_DIR.rglob("*.md")):
        rel = doc.relative_to(DOCS_DIR)
        if rel.name != rel.name.lower():
            failures.append(f"non_lowercase_doc: {rel}")
        if rel not in nav_refs:
            failures.append(f"orphan_doc: {rel}")
        text = doc.read_text()
        if len(text.strip().splitlines()) < 4:
            failures.append(f"empty_doc: {rel}")
        rel_from_root = doc.relative_to(ROOT)
        normalized = re.sub(r"\bPLANNED\b", "PLAN_STATE", text)
        if FUTURE_WORDS.search(normalized):
            failures.append(f"future_language: {rel_from_root}")

        module_refs = MODULE_RE.findall(text)
        if not module_refs:
            failures.append(f"missing_module_ref: {rel_from_root}")

        for ref in module_refs:
            ref = ref.rstrip(".,);:")
            if ref in modules:
                continue
            if any(mod.startswith(ref + ".") for mod in modules):
                continue
            failures.append(f"unknown_module_ref: {ref} in {rel_from_root}")

        for path_ref in SRC_PATH_RE.findall(text):
            if not _path_exists(path_ref):
                failures.append(f"missing_path_ref: {path_ref} in {rel_from_root}")

    if failures:
        for failure in failures:
            print(failure)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
