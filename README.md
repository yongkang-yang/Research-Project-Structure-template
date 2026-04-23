# Research Project Structure Template

This repository is a reusable skeleton for empirical research projects. `README.md` is the structure reference for the repository: it documents root files, directory purposes, and naming conventions.

## Required Root Files

- `AGENTS.md`: AI-facing project brief and operating rules for tools that read `AGENTS.md`.
- `CLAUDE.md`: mirrored AI-facing project brief and operating rules for tools that read `CLAUDE.md`.
- `PROJECT_REPORT.md`: research-progress summary covering project status, active theory decisions, empirical package, and current status.
- `MEASURES.md`: variable and measure registry, with sources and operationalization notes.
- `README.md`: repository structure reference and naming guide.

## Directory Purposes

- `compliance/`: IRB, consent, preregistration, DMP, and related governance materials.
- `literature/`: literature review source files, synthesis documents, and reading notes. Keep the main literature synthesis in `literature/LITERATURE_REVIEW.md`.
- `logs/`: dated project logs and the daily log template.
- `meetings/`: meeting notes and the meeting template.
- `presentation/`: conference, workshop, PDW, and internal presentation assets.
- `scripts/`: helper scripts for maintaining AI docs and repository structure.
- `studies/`: study-level packages for active empirical work.
- `studies/archive/`: archived pilots, dropped studies, and mixed legacy materials.
- `submission/`: submission logs, journal-specific requirements, revision rounds, and reusable submission templates.
- `writing/`: manuscript drafts and reusable writing templates.

## Working Rules

- Keep `PROJECT_REPORT.md` lean. It should summarize only the literature decisions that currently affect theory, hypotheses, design, or next steps.
- Put detailed literature extraction, synthesis, contradictions, and reading queues in `literature/LITERATURE_REVIEW.md`.
- If literature notes become paper-specific and long, create files under `literature/notes/` and keep `literature/LITERATURE_REVIEW.md` as the synthesis layer.

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
|-- literature/
|   `-- LITERATURE_REVIEW.md
|-- logs/
|   `-- daily_log_template.md
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
|   |-- check_project_health.py
|   |-- sync_ai_docs.py
|   `-- update_readme_structure.py
|-- studies/
|   |-- archive/
|   |   `-- README.md
|   |-- study-01-field/
|   |   |-- data/
|   |   `-- README.md
|   `-- study-02-experiment/
|       |-- data/
|       `-- README.md
|-- submission/
|   |-- journal-placeholder/
|   |   `-- r1-revise-resubmit/
|   |-- shared-templates/
|   |   |-- cover-letter-template.md
|   |   |-- response-letter-template.md
|   |   |-- submission-guideline-JAP.md
|   |   `-- title-page-template.md
|   `-- SUBMISSION_LOG.md
|-- writing/
|   |-- drafts/
|   |   `-- .gitkeep
|   `-- templates/
|       `-- .gitkeep
`-- Migration Playbook.md
```
<!-- END DIRECTORY TREE -->
