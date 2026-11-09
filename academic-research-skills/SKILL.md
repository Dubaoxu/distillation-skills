---
name: academic-research-skills
description: "Manage academic research, literature synthesis, paper planning and writing, citation checks, peer review, and revision in one workflow. Use for review or empirical papers, single-stage manuscript tasks, or a full research-to-paper project, including Zotero literature and Obsidian notes."
metadata:
  version: "4.0.0"
  task_type: open-ended
  data_access_level: verified_only
---

# 学术研究与论文写作

One skill handles research, writing, integrity checks, review, revision, and
cross-session continuation. Select internal modes from the user's request;
never require them to invoke or install another research skill.
Follow the user's language, discipline, requested deliverable, and scope.

## Intake and routing

Read available drafts, research notes, review comments, and project configuration
before asking questions. If present, read `research-project.yaml` and the existing
Material Passport. Reuse recorded choices and inspect current artifacts to resolve
stale state. Ask only for missing information that affects the requested work:
paper type, research question, target venue/audience, materials, or output format.

Select the smallest mode that completes the request:

| User intent | Internal mode | Start with |
|---|---|---|
| Explore a question, search or synthesize literature, fact-check | `research` | Research question and source corpus |
| Plan an outline, draft/revise a section, write a paper, format or audit citations | `write` | Existing evidence, configuration, outline or draft |
| Critique a manuscript, check methodology, verify revisions | `review` | The supplied manuscript and any review history |
| Complete the research-to-paper process | `pipeline` | Latest evidenced stage; start at research only if needed |
| Continue a saved project | `resume` | Passport, latest artifacts, unresolved issues and next action |

For mixed requests, chain only the needed stages in this same skill. Supplying a
draft does not automatically request an entire pipeline. A request for review
does not authorize rewriting the manuscript. Reviewer comments plus a request to
revise select `write` revision mode; a request to check the revision selects
`review` verification mode.

## Paper type and connected materials

Read [the portable research workflow](shared/references/portable_research_workflow.md)
when using project configuration, Zotero, Obsidian, or switching runtimes. It
defines paths, library/export handling, corpus-fragment merging, and paper types.

- **Review paper:** choose narrative, systematic, or scoping from the user's
  intention. Narrative synthesis needs explicit scope and counter-evidence;
  systematic/scoping work needs recorded searches, screening decisions, and
  extraction. Do not invent screening counts or label an incomplete search
  systematic. Meta-analysis requires suitable extracted data and methods.
- **Empirical or methods paper:** draft around actual design, datasets, code,
  baselines, experiments, and results. Missing experiments stay pending. Separate
  proposed methods from implemented and validated behavior.
- **Zotero:** use connected capabilities when available, otherwise the supported
  offline export adapter. Preserve citation keys and item identities.
- **Obsidian:** use the chosen vault/project layout and preserve user annotations.
  Notes, abstracts, metadata, and acquired original texts are different evidence
  levels; an imported note does not verify the paper's claims.

## Shared execution and evidence rules

1. Build an evidence map before synthesizing or drafting substantive claims.
   Verify bibliographic identity separately from claim support. Keep original
   text page/section anchors where available; record missing access and uncertainty.
2. Preserve source keys across notes, corpus, manuscript, and bibliography. Review
   corpus rejections and resolve identity conflicts before citing. Adapter fragments
   must not replace the full passport.
3. Reuse existing valid material. Do not fabricate references, data, experiments,
   statistics, ethical approvals, source reads, or tool execution.
4. Match the requested scope and authorization. Confirm consequential choices not
   already settled; existing user authorization can cover routine stage transitions.
   User instructions govern autonomy if older internal protocols demand repeated
   confirmations. Failed integrity checks remain failures regardless of autonomy.
5. Internal agent files describe roles. Use host-supported tools and sequential
   roles when suitable. Do not claim independent or paper-blind review without
   the actual isolated calls required by that mode. Disclose unavailable isolation
   and offer a supported narrower review.
6. Bound revision: use the established two review/revision rounds unless the user
   requests more. Report residual issues explicitly. Critical evidence/integrity
   defects cannot be converted into an unconditional pass by calling them limitations.

## Research, writing, and review

Read only the internal workflow needed for the selected mode and follow its links
for detailed role instructions, templates, and contracts:

| Mode | Internal reference | Use |
|---|---|---|
| `research` | [Research workflow](deep-research/WORKFLOW.md) | Scoping, search, verification, synthesis, research reports; quick, literature, fact-check, Socratic and systematic-review options |
| `write` | [Writing workflow](academic-paper/WORKFLOW.md) | Configuration, structure, evidence-backed argument, drafting, abstract, citations, formatting and revision |
| `review` | [Review workflow](academic-paper-reviewer/WORKFLOW.md) | Methodology/domain/argument critique, editorial synthesis and revision verification |
| `pipeline`, `resume` | [Stage/state protocol](academic-pipeline/WORKFLOW.md) | State transitions, integrity gates, passport and finalization; load other references only as the next stage needs them |

These are internal documents, not four skills. Their historical names and
version numbers identify retained protocols. Interpret old cross-skill dispatch
as a mode transition inside this skill, not a separate invocation. This entrypoint
governs scope, routing, runtime adaptation, and authorization when older text
conflicts. Retained evidence, verification, and isolation requirements still apply.

Full workflow: scope → search and verify → synthesize → outline and draft →
integrity check → review → revise and verify responses → final integrity check →
requested output. At each transition retain the artifact version, decisions,
unresolved issues, and next action. A review or citation check can enter midway.

For systematic work, preserve search/screening/extraction lineage through writing
and review; do not reroute it into generic empirical reporting. For empirical
work, require the actual results supporting conclusions rather than borrowing
claims from related papers.

## Paths, persistence, and delivery

This `SKILL.md` directory is the source root. Resolve `shared/` and `scripts/`
against it; resolve each internal document's local `agents/`, `references/`,
`templates/`, and `examples/` against that document's parent directory. References
with a module prefix resolve from the root. Do not rely on the shell's current
directory, Claude-only commands, hooks, or a missing `.claude/CLAUDE.md`.

Use the existing Material Passport contracts under `shared/` and the stage/state
protocol for complete projects. `research-project.yaml` is configuration, not a
replacement passport. A small standalone task does not require creating a full
project or running all stages. Update only relevant project artifacts.

Deliver the requested artifact and briefly report source/evidence coverage,
checks actually run, unresolved issues, and where work can resume. Distinguish
simulated review from journal acceptance and an incomplete draft from a verified
final manuscript. Keep process records proportional to the user's requested work.

For project-local installation and paper-type initialization, use
`scripts/setup_research.py`; installation exposes only `academic-research-skills`
in the selected host. See the portable workflow for commands.
