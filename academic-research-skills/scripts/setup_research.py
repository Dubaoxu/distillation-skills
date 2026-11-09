#!/usr/bin/env python3
"""Create a portable ARS project or project-local skill entrypoints.

No global settings, MCP registrations, or source libraries are modified.
Requires PyYAML (already in requirements-dev.txt).
"""
from __future__ import annotations

import argparse
import json
from pathlib import Path
import sys

import yaml

SUITE = Path(__file__).resolve().parents[1]
SKILL_NAME = "academic-research-skills"


def write_new_files(files: dict[Path, str]) -> list[Path]:
    # Preflight the complete operation before creating any files.
    for path in files:
        if path.exists() or path.is_symlink():
            raise ValueError(f"refusing to replace existing path: {path}")
        for parent in path.parents:
            if parent.exists() and not parent.is_dir():
                raise ValueError(f"parent is not a directory: {parent}")
    for path, text in files.items():
        path.parent.mkdir(parents=True, exist_ok=True)
        with path.open("x", encoding="utf-8", newline="\n") as stream:
            stream.write(text)
    return list(files)


def init_project(directory: Path, paper_type: str, review_kind: str | None,
                 title: str, vault: Path | None = None) -> list[Path]:
    if paper_type not in {"review", "empirical"}:
        raise ValueError("paper_type must be review or empirical")
    if paper_type == "empirical" and review_kind is not None:
        raise ValueError("--review-kind is only valid for review papers")
    if review_kind is not None and review_kind not in {"narrative", "systematic", "scoping"}:
        raise ValueError("unknown review kind")
    kind = (review_kind or "narrative") if paper_type == "review" else None
    root = directory.resolve()
    config = {
        "schema_version": 1,
        "title": title,
        "paper_type": paper_type,
        "review_kind": kind,
        "language": "zh-CN",
        "stage": "intake",
        "obsidian_vault": str(vault.resolve()) if vault else None,
        "zotero": {"mode": "auto", "collection": None, "export_file": None},
        "artifacts": {"corpus": "sources/corpus.yaml", "passport": "passport.yaml",
                      "draft": "manuscript/draft.md", "review": "reviews/review.md"},
    }
    # Adapter outputs are corpus fragments, not complete pipeline passports.
    # Leave passport creation to the state tracker after intake.
    files = {
        root / "research-project.yaml": yaml.safe_dump(config, allow_unicode=True, sort_keys=False),
        root / "sources/README.md": "# Sources\n\nStore scoped exports and adapter corpus fragments here. Imported metadata is not verified full-text evidence.\n",
        root / "notes/research-log.md": f"# {title}\n\n## Decisions\n\n## Open questions\n\n## Next action\n\nComplete intake and select the literature corpus.\n",
        root / "manuscript/draft.md": f"# {title}\n\nDraft pending evidence and outline.\n",
        root / "reviews/README.md": "# Reviews\n\nKeep review reports and revision responses here.\n",
    }
    return write_new_files(files)


def install_entrypoints(project: Path, target: str) -> list[Path]:
    if target not in {"codex", "claude", "both"}:
        raise ValueError("unknown target")
    folders = {"codex": ".agents", "claude": ".claude"}
    selected = folders if target == "both" else {target: folders[target]}
    files = {}
    for folder in selected.values():
        for legacy in ("deep-research", "academic-paper", "academic-paper-reviewer", "academic-pipeline"):
            old_entry = project.resolve() / folder / "skills" / legacy / "SKILL.md"
            if old_entry.exists():
                raise ValueError(f"legacy skill entrypoint present; migrate it before single-skill installation: {old_entry}")
        source = SUITE / "SKILL.md"
        text = source.read_text(encoding="utf-8")
        metadata = yaml.safe_load(text.split("---", 2)[1])
        wrapper = (
            "---\nname: " + SKILL_NAME + "\ndescription: "
            + json.dumps(metadata["description"], ensure_ascii=False)
            + "\n---\n\nRead and follow the unified source skill at:\n\n"
            + f"`{source.as_posix()}`\n\n"
            + "Resolve all internal modules, references, and scripts against the source root:\n\n"
            + f"`{SUITE.as_posix()}`\n\n"
            + "Research, writing, review, and orchestration are internal modes of this single skill. "
            + "Do not discover or install the former four skills separately.\n"
        )
        files[project.resolve() / folder / "skills" / SKILL_NAME / "SKILL.md"] = wrapper
    return write_new_files(files)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    commands = parser.add_subparsers(dest="command", required=True)
    init = commands.add_parser("init", help="create a new research project")
    init.add_argument("--directory", type=Path, required=True)
    init.add_argument("--paper-type", choices=("review", "empirical"), required=True)
    init.add_argument("--review-kind", choices=("narrative", "systematic", "scoping"))
    init.add_argument("--title", required=True)
    init.add_argument("--vault", type=Path)
    install = commands.add_parser("install", help="create project-local entrypoints; keep this source checkout in place")
    install.add_argument("--project", type=Path, required=True)
    install.add_argument("--target", choices=("codex", "claude", "both"), required=True)
    args = parser.parse_args()
    try:
        if args.command == "init":
            paths = init_project(args.directory, args.paper_type, args.review_kind, args.title, args.vault)
        else:
            paths = install_entrypoints(args.project, args.target)
    except (OSError, ValueError, yaml.YAMLError) as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        return 1
    for path in paths:
        print(path)
    return 0


if __name__ == "__main__":
    sys.exit(main())
