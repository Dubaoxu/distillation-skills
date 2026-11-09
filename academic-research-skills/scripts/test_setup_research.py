"""Behavioral checks for project creation and project-local skill discovery."""
from pathlib import Path
import importlib.util

import pytest
import yaml

SCRIPT = Path(__file__).with_name("setup_research.py")
spec = importlib.util.spec_from_file_location("setup_research", SCRIPT)
setup = importlib.util.module_from_spec(spec)
spec.loader.exec_module(setup)

layout_spec = importlib.util.spec_from_file_location("spec_consistency", SCRIPT.with_name("check_spec_consistency.py"))
layout = importlib.util.module_from_spec(layout_spec)
layout_spec.loader.exec_module(layout)


@pytest.mark.parametrize("kind", ["narrative", "systematic", "scoping"])
def test_review_configuration_and_artifacts(tmp_path, kind):
    root = tmp_path / "论文 空格"
    setup.init_project(root, "review", kind, "中文综述", tmp_path)
    config = yaml.safe_load((root / "research-project.yaml").read_text(encoding="utf-8"))
    assert config["review_kind"] == kind
    assert config["obsidian_vault"] == str(tmp_path.resolve())
    assert (root / config["artifacts"]["draft"]).is_file()
    assert not (root / config["artifacts"]["passport"]).exists()


def test_empirical_does_not_select_a_review(tmp_path):
    setup.init_project(tmp_path, "empirical", None, "Methods")
    config = yaml.safe_load((tmp_path / "research-project.yaml").read_text())
    assert config["paper_type"] == "empirical"
    assert config["review_kind"] is None


def test_invalid_combination_writes_nothing(tmp_path):
    with pytest.raises(ValueError):
        setup.init_project(tmp_path, "empirical", "systematic", "Title")
    assert list(tmp_path.iterdir()) == []


def test_project_collision_preserves_files_and_does_not_partially_init(tmp_path):
    draft = tmp_path / "manuscript/draft.md"
    draft.parent.mkdir()
    draft.write_text("User draft")
    with pytest.raises(ValueError):
        setup.init_project(tmp_path, "empirical", None, "Title")
    assert draft.read_text() == "User draft"
    assert not (tmp_path / "research-project.yaml").exists()


def test_both_runtime_entrypoints_resolve_sources(tmp_path):
    paths = setup.install_entrypoints(tmp_path, "both")
    assert len(paths) == 2
    for path in paths:
        text = path.read_text(encoding="utf-8")
        metadata = yaml.safe_load(text.split("---", 2)[1])
        assert metadata["name"] == setup.SKILL_NAME
        assert (setup.SUITE / "SKILL.md").is_file()
        assert str(setup.SUITE.as_posix()) in text
    for folder in (".agents", ".claude"):
        assert [p.name for p in (tmp_path / folder / "skills").iterdir()] == [setup.SKILL_NAME]
    assert not (tmp_path / "AGENTS.md").exists()


def test_install_collision_preflights_all_targets(tmp_path):
    existing = tmp_path / ".claude/skills/academic-research-skills/SKILL.md"
    existing.parent.mkdir(parents=True)
    existing.write_text("User skill")
    with pytest.raises(ValueError):
        setup.install_entrypoints(tmp_path, "both")
    assert existing.read_text() == "User skill"
    assert not (tmp_path / ".agents").exists()


def test_suite_has_only_one_discoverable_manifest():
    assert list(setup.SUITE.rglob("SKILL.md")) == [setup.SUITE / "SKILL.md"]


def test_install_does_not_add_fifth_skill_to_legacy_install(tmp_path):
    old = tmp_path / ".claude/skills/deep-research/SKILL.md"
    old.parent.mkdir(parents=True)
    old.write_text("User-owned legacy entry")
    with pytest.raises(ValueError, match="legacy skill entrypoint"):
        setup.install_entrypoints(tmp_path, "both")
    assert not (tmp_path / ".agents").exists()
    assert old.read_text() == "User-owned legacy entry"


def test_layout_validator_accepts_unified_source():
    assert layout.check_unified_layout(setup.SUITE) == []


def test_layout_validator_rejects_missing_module_and_extra_manifest(tmp_path):
    (tmp_path / "SKILL.md").write_text(
        "---\nname: academic-research-skills\n---\n[missing](missing.md)\n",
        encoding="utf-8",
    )
    extra = tmp_path / "extra/SKILL.md"
    extra.parent.mkdir()
    extra.write_text("---\nname: extra\n---\nExtra")
    errors = layout.check_unified_layout(tmp_path)
    assert any("exactly one" in error for error in errors)
    assert any("missing.md" in error for error in errors)
    assert any("missing retained workflow" in error for error in errors)
