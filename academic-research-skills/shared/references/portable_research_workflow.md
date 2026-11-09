# Portable research workflow: Zotero, Obsidian, Claude Code, and Codex

Read this reference when using an external library, an Obsidian vault,
`research-project.yaml`, or a runtime other than Claude Code. It supplements the
existing research, writing, review, and passport contracts; it does not replace
their evidence or integrity gates.

## Project intake and paper type

Read the project's `research-project.yaml` if present. Paths in `artifacts` and
`zotero.export_file` are relative to that configuration file, not the shell's
working directory. This file is a project configuration sidecar, **not** a new
Material Passport schema. Keep stage state in the existing passport and update
the sidecar stage label when it changes. On disagreement, inspect the latest
artifacts and passport before resuming; do not trust a stale stage label.

Use explicit user choices first. Ask for paper type only if it is missing and
would change the work. Select the applicable branch:

| Project choice | Research and writing | Review focus |
|---|---|---|
| `review` + `narrative` | Scope/themes, documented search coverage, literature matrix, critical synthesis; `deep-research lit-review` then `academic-paper lit-review` or `full` | Coverage, contradictory findings, synthesis beyond summaries, justified scope |
| `review` + `systematic` | `deep-research systematic-review`, then `academic-paper full`; retain search dates/strings, deduplication, inclusion decisions, extraction and bias records | Search reproducibility, selection accounting, extraction fidelity and justified synthesis |
| `review` + `scoping` | Map concepts and evidence types; adapt a documented search/screen/extraction plan to the scoping question and reporting guidance | Scope, search transparency, charting, evidence gaps; do not force effect pooling |
| `empirical` | `deep-research` for background, then `academic-paper full` using actual methods, datasets, code, and results | Design, baselines, ablations when relevant, leakage, statistics, reproducibility and limits |

For systematic reviews, do not describe an opportunistic library search as a
completed systematic search or invent screening counts. For empirical papers,
missing experiments remain pending; help with plans, methods, or explicitly
marked incomplete sections. A methods contribution without collected results
must not be described as experimentally validated. Evidence hierarchies depend
on the discipline; clinical trial rankings are not universal engineering rubrics.

## Zotero input

`zotero.mode: auto` means choose among capabilities actually available in this
session; it does not promise an installed server or automatic background sync.

1. Prefer a connected Zotero MCP tool or the host's Zotero integration for scoped
   collection/item search. Discover its current tools; do not assume server names,
   ports, auth, or a vendor-specific tool name. Ask which collection if unclear.
2. Without a live integration, use a user-selected **Better BibTeX JSON** export.
   Run `scripts/adapters/zotero.py --input EXPORT --passport FRAGMENT
   --rejection-log REJECTIONS`, then run
   `scripts/check_literature_corpus_schema.py --passport FRAGMENT
   --rejection-log REJECTIONS`. Paths are relative to the ARS suite root here.
   Install `requirements-dev.txt` first. Better CSL JSON is a different format.
3. Preserve both Zotero item identity and the exported citation key. A Zotero item
   key is not a BibTeX key. Never silently rename keys already used in a draft.
4. Adapter output contains `literature_corpus` only. Import that field into the
   existing passport through the state tracker; do not overwrite a full passport
   with an adapter fragment. Keep an original fragment and rejection log.
5. Imported metadata, abstracts, and personal notes are separate evidence levels.
   Do not mark an original source acquired or verified merely because its record
   exists. Obtain the relevant original text when checking substantive claims;
   save page/section anchors and verification status using existing contracts.

The shipped adapter is an offline importer. Live MCP reads use the connected
integration, not that script. If all items are rejected, diagnose the export
format/required fields before continuing. Existing citekey conflicts across
sources require an explicit mapping or deduplication decision, not suffixing and
assuming manuscript citations still match. Do not modify the Zotero database,
enable services, install plugins, or import records merely to read a corpus.

## Obsidian workspace

Confirm the selected vault and project subdirectory from configuration or user
input. Do not infer that every directory of Markdown files is the intended vault.
Use ordinary UTF-8 Markdown and YAML so no community plugin is required.

- Ingest only the selected literature-note directory with
  `scripts/adapters/obsidian.py`, using separate fragment/rejection outputs and
  the same schema validator. Convention A uses `citekey`, `title`, `authors`,
  `year`, with optional `doi`, `venue`, and `tags`; see the adapter README.
- A note body is `user_notes`, not the paper's original text. Wikilinks are literal
  until actually resolved. Do not claim linked notes were read without reading them.
- Keep literature notes, project decisions, manuscript drafts, and review responses
  distinct. Link drafts and reviews using stable project-relative Markdown links.
  Reuse the user's existing layout when supplied.
- Export new literature notes with the same frontmatter convention. Record source
  pointer, read status, claim anchors, and personal interpretation distinctly in
  the body. Preserve existing notes and user annotations; show proposed conflicting
  changes instead of replacing them. Do not change `.obsidian` settings.

## Runtime adaptation

The unified root `SKILL.md` and referenced files are the workflow source of truth. Read
relative `agents/`, `references/`, `templates/` from the source skill directory;
read `shared/`, `scripts/`, and sibling skill paths from the suite root. Do not
depend on the current working directory or an absent `.claude/CLAUDE.md`.
For routing, use `shared/references/intent_clarification_protocol.md` directly.

Claude Code plugin commands and hooks apply only when installed and supported.
In Codex or another host, invoke the skill by its available entrypoint or natural
language, use that host's tools, and run relevant validators explicitly. Do not
claim hooks, dispatch, or checks ran if they did not.

Agent files define roles. Use separate agents/calls only where available,
permitted, and required by the invoked mode. Sequential role passes can support
ordinary work but are not independent blind review. If a mode requires fresh,
paper-blind calls and the host cannot supply that isolation, record the limitation
and offer a supported narrower mode; do not label a same-context review compliant.

On a host switch, read the existing passport and recorded artifact paths, verify
the latest draft/review versions, preserve unresolved issues, and continue at the
requested stage. Preserve the existing confirmation policy unless the user has
explicitly authorized a different level of autonomy. Integrity failures remain
unresolved issues regardless of runtime.

## First use

From the suite root (Python 3.10+):

```sh
python -m pip install -r requirements-dev.txt
python scripts/setup_research.py install --project /path/to/work --target both
python scripts/setup_research.py init --directory /path/to/work/my-paper --paper-type review --review-kind systematic --title "My review"
```

`install` creates small project-local entrypoints in `.agents/skills` (Codex) and
`.claude/skills` (Claude Code), with only `academic-research-skills` in each host,
pointing to this source checkout. The former four names are internal workflows,
not separately installed skills. Keep it in place;
rerun installation in a new location if it moves. Existing entrypoints are never
overwritten. `init` creates configuration and Markdown starting files, not a
completed passport or verified research. For empirical work use
`--paper-type empirical` without `--review-kind`. Optionally pass `--vault PATH`;
that records a location but does not scan or change the vault. Windows paths with
spaces or Chinese characters should be quoted.

Start with: "Use academic-research-skills in pipeline mode. Read my-paper/research-project.yaml, use the
selected Zotero collection/export and Obsidian notes, and continue from the
available evidence." A paper type is independent of execution mode (`full`,
`plan`, etc.). Choosing a type does not force a new full pipeline on a single-stage
request. No live Zotero connection or manuscript quality is guaranteed by setup.
