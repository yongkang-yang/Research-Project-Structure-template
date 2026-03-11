# Research Project Structure Template

This repository is a reusable skeleton for empirical research projects. `README.md` is the structure reference for the repository: it documents root files, directory purposes, and naming conventions.

## Required Root Files

- `AGENTS.md`: AI-facing project brief and operating rules for tools that read `AGENTS.md`.
- `CLAUDE.md`: mirrored AI-facing project brief and operating rules for tools that read `CLAUDE.md`.
- `PROJECT_REPORT.md`: research-progress summary covering theory, model, empirical package, and current status.
- `MEASURES.md`: variable and measure registry, with sources and operationalization notes.
- `README.md`: repository structure reference and naming guide.

## Directory Tree

This block is the only auto-generated section in `README.md`.
Its update position is fixed between the `BEGIN DIRECTORY TREE` and `END DIRECTORY TREE` markers.

<!-- BEGIN DIRECTORY TREE -->
```text
.
|-- compliance/
|   |-- consent/
|   |   `-- .gitkeep
|   |-- dmp/
|   |   `-- .gitkeep
|   |-- irb/
|   |   `-- .gitkeep
|   `-- other/
|       `-- .gitkeep
|-- data/
|   |-- analysis-notes/
|   |   |-- .gitkeep
|   |   `-- analysis_note_template.md
|   |-- cleaned-data/
|   |   `-- .gitkeep
|   |-- data-analysis/
|   |   `-- .gitkeep
|   |-- final-analysis-data/
|   |   `-- .gitkeep
|   |-- osf-public-data/
|   |   `-- .gitkeep
|   `-- raw-data/
|       `-- .gitkeep
|-- literature/
|-- meetings/
|   |-- .gitkeep
|   `-- meeting_template.md
|-- presentation/
|   |-- conferences/
|   |   `-- .gitkeep
|   |-- internal/
|   |   `-- .gitkeep
|   |-- pdws/
|   |   `-- .gitkeep
|   `-- workshops/
|       `-- .gitkeep
|-- scripts/
|   |-- sync_ai_docs.py
|   `-- update_readme_structure.py
|-- submission/
|   |-- journal-placeholder/
|   |   `-- r1-revise-resubmit/
|   `-- shared-templates/
|       |-- cover-letter-template.md
|       |-- response-letter-template.md
|       |-- submission-guideline-JAP.md
|       `-- title-page-template.md
`-- writing/
    |-- drafts/
    |   `-- .gitkeep
    `-- templates/
        `-- .gitkeep
```
<!-- END DIRECTORY TREE -->

## Root File Descriptions

### `AGENTS.md`

- project-understanding scaffold for AI tools that read `AGENTS.md`
- includes project identity, research question, theory/model structure, empirical package, collaborator information, compliance status, file index, and AI rules

### `CLAUDE.md`

- mirrored version of `AGENTS.md` for AI tools that read `CLAUDE.md`

### `PROJECT_REPORT.md`

- project snapshot
- research question and objective
- important literature
- theory structure
- conceptual model
- empirical package
- analysis method
- current status
- recent updates
- open tasks
- risks and issues
- decisions log
- next actions

### `MEASURES.md`

- variable or construct name
- source or citation
- measure type
- operational definition
- coding or aggregation rule
- sample or wave usage
- analysis file reference when relevant

For original scale items or question wording, use `/home/ykyan/clawd/memory/scales_and_measures.md`.

## Public/Private Reminder

If this repository is public, do not commit restricted raw data, signed consent forms, protected IRB documents, or identifying information that should remain private.
