# Paper Writing Agent

[中文版](README.zh-CN.md)

A **general-purpose** Claude Code skill for academic paper writing — from raw research materials to submission-ready manuscript with journal recommendations. Works across any academic domain.

## Overview

`paper-writing-agent` is a **coordination layer** that bridges three components into a unified writing pipeline:

| Component | Role |
|-----------|------|
| **User Materials** | All documents provided by the user — drafts, notes, data, references, domain knowledge |
| **academic-paper** (v3.1.2) | 12-agent paper writing pipeline — 10 modes, 6 structural types (IMRaD/review/theoretical/case study/policy brief/conference), 5 citation formats (APA/Chicago/IEEE/MLA/GB/T 7714) |
| **academic-paper-reviewer** (v1.9.1) | 7-agent multi-perspective review — EIC + 3 peer reviewers + Devil's Advocate, 0–100 scoring rubric |

The agent's value is **systematic coordination**: before dispatching to the general-purpose writing/review pipelines, it performs material analysis, literature matching, citation graph construction, and research gap analysis — producing more precise, better-structured outputs in any domain.

## Pipeline (8 Phases)

```
Phase 0: Domain ID   →  Auto-detect field, subfield, methodology type from user materials
Phase 1: Analysis    →  Extract core claims, innovations, methods, assumptions
Phase 2: Literature  →  Local-first search → Google Scholar / arXiv / Semantic Scholar
Phase 3: Graph       →  Citation relationship graph (extends/contrasts/subsumes/disagrees)
Phase 4: Gaps        →  Solved / partially-solved / unsolved problems
Phase 5: Brief       →  Writing brief → delegate to academic-paper for drafting
Phase 6: Review      →  Delegate to academic-paper-reviewer (5 independent reviews)
Phase 7: Revise      →  Revision loop (max 3 rounds, bounded iteration)
Phase 8: Finalize    →  Format output (LaTeX/DOCX/PDF) + journal recommendations
```

**Stop conditions**: score ≥80 (Accept) / 3 review rounds reached / 2 consecutive rounds with <5pt improvement / user terminates.

## File Structure

```
paper-writing-agent/
├── SKILL.md                     # Skill definition (8-phase pipeline)
├── README.md                    # This file (EN)
├── README.zh-CN.md              # Chinese version
├── references/                  # Research materials
│   ├── citation_graph.md        # Citation relationship graph
│   ├── journal_recommendations.md # Journal recommendations
│   ├── literature_map.md        # Literature coverage map
│   ├── material_analysis.md     # Raw material analysis
│   ├── research_gaps.md         # Identified research gaps
│   ├── writing_brief.md         # Writing brief for academic-paper
│   └── review_round2.md         # Second-round review report
├── need/                        # Missing-data annotations
└── older/                       # Version archive (v0.1, v0.2, ...)
```

> **Note:** This skill depends on [academic-research-skills](../academic-research-skills/) (v3.9.2), which should be installed alongside it.

## When to Use

- Systematically writing papers from multiple documents, drafts, and notes
- Managing the full write-review-revise lifecycle
- Building precise citation graphs and literature alignment
- Version-managed, traceable iterative writing workflow
- Getting simulated peer review before real submission
- Matching papers to the most suitable journals based on content

## When NOT to Use

- Research-only (no writing needed) → use `deep-research` directly
- Reviewing an existing paper → use `academic-paper-reviewer` directly
- Full end-to-end pipeline with integrity checks → use `academic-pipeline`
- Quick short article / blog post → use `academic-paper` directly

## Delegation Model

```
paper-writing-agent (coordinator)
    │
    ├── Phase 0–4: Local analysis (user-material-driven)
    ├── Phase 5:    ──delegate──→ academic-paper (12-agent writing)
    ├── Phase 6:    ──delegate──→ academic-paper-reviewer (7-agent review)
    ├── Phase 7:    ──delegate──→ academic-paper (revision mode)
    └── Phase 8:    ──delegate──→ academic-paper (format-convert) + journal recs
```

## Core Principles

1. **Evidence-driven** — Every claim backed by literature or data. Missing evidence → tagged in `need/`, never fabricated.
2. **User-materials-first** — All analysis starts from user-provided materials. Web search fills gaps only.
3. **Delegate expertise** — Writing to `academic-paper`, review to `academic-paper-reviewer`. No reinvention.
4. **Version traceable** — Every revision produces a new version; old versions preserved in `older/`.
5. **Bounded iteration** — Max 3 external review rounds. After round 3, surface unresolved issues for user decision.
6. **Domain-adaptive** — Phase 0 automatically identifies the field from user materials. No hardcoded domain assumptions.

## Journal Recommendation

Recommends journals based on five dimensions:

| Dimension | What's Evaluated |
|-----------|-----------------|
| Topic match | Is the paper within the journal's scope? |
| Method preference | Does the journal favor theoretical depth or empirical results? |
| Innovation tier | Incremental → Q3; significant breakthrough → Q2; field-defining → Q1 |
| Citation origin | Where are the paper's core references published? → prioritize those |
| Field conventions | What are the recognized top venues in this domain? |

## Setup

1. Clone the full `distillation-skills` repository:
   ```bash
   git clone <repo-url> ~/.claude/skills/distillation-skills
   ```

2. The skill auto-loads when Claude Code detects the skill directory. Ensure both `paper-writing-agent/` and `academic-research-skills/` are under the same parent directory.

3. Place any domain reference materials you have in the working directory — the agent auto-detects and uses them in Phase 0.

## Dependencies

This skill requires [academic-research-skills v3.9.2](../academic-research-skills/) (installed at the parent level), which provides:
- `deep-research` (v2.9.4) — 13-agent research team
- `academic-paper` (v3.1.2) — 12-agent writing pipeline
- `academic-paper-reviewer` (v1.9.1) — Multi-perspective review
- `academic-pipeline` (v3.9.2) — Full pipeline orchestrator

## License

See [SKILL.md](SKILL.md) frontmatter. Inherits from the parent project.

## Author

Cheng-I Wu ([@Imbad0202](https://github.com/Imbad0202))
