# Research Project Structure Template

This repository is a reusable skeleton for empirical research projects. `README.md` is the structure reference for the repository: it documents root files, directory purposes, and naming conventions.

## Required Root Files

- `AGENTS.md`: AI-facing project brief and operating rules for tools that read `AGENTS.md`.
- `CLAUDE.md`: mirrored AI-facing project brief and operating rules for tools that read `CLAUDE.md`.
- `PROJECT_REPORT.md`: research-progress summary covering theory, model, empirical package, and current status.
- `MEASURES.md`: variable and measure registry, with sources and operationalization notes.
- `README.md`: repository structure reference and naming guide.

## Directory Purposes

- `compliance/`: IRB, consent, preregistration, DMP, and related governance materials.
- `literature/`: literature review source files, summaries, and reading notes.
- `logs/`: dated project logs and the daily log template.
- `meetings/`: meeting notes and the meeting template.
- `presentation/`: conference, workshop, PDW, and internal presentation assets.
- `scripts/`: helper scripts for maintaining AI docs and repository structure.
- `studies/`: study-level packages for active empirical work.
- `studies/archive/`: archived pilots, dropped studies, and mixed legacy materials.
- `submission/`: submission logs, journal-specific requirements, revision rounds, and reusable submission templates.
- `writing/`: manuscript drafts and reusable writing templates.

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
|   |-- other/
|   |   `-- .gitkeep
|   `-- preregistration/
|       `-- .gitkeep
|-- literature/
|-- logs/
|   |-- .gitkeep
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
|   |-- study-01-field/
|   |   |-- README.md
|   |   |-- design/
|   |   |-- materials/
|   |   |-- data/
|   |   |   |-- analysis-notes/
|   |   |   |-- cleaned-data/
|   |   |   |-- final-analysis-data/
|   |   |   `-- raw-data/
|   |   |-- analysis/
|   |   `-- outputs/
|   `-- study-02-experiment/
|       |-- README.md
|       |-- design/
|       |-- materials/
|       |-- data/
|       |   |-- analysis-notes/
|       |   |-- cleaned-data/
|       |   |-- final-analysis-data/
|       |   `-- raw-data/
|       |-- analysis/
|       `-- outputs/
|-- submission/
|   |-- journal-specific/
|   |   `-- [journal-name]/
|   |       |-- guidelines.md
|   |       |-- format-template/
|   |       `-- checklist.md
|   |-- revision-rounds/
|   |   |-- r1/
|   |   |-- r2/
|   |   `-- r3/
|   |-- shared-templates/
|   |   |-- cover-letter-template.md
|   |   |-- response-letter-template.md
|   |   |-- submission-guideline-JAP.md
|   |   `-- title-page-template.md
|   `-- SUBMISSION_LOG.md
`-- writing/
    |-- drafts/
    |   `-- .gitkeep
    `-- templates/
        `-- .gitkeep
```
<!-- END DIRECTORY TREE -->
