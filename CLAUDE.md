# Project AI Brief

## Rules

- At the start of each session, load:
  - `README.md`
  - `PROJECT_REPORT.md`
  - `MEASURES.md`
  - the two most recent meeting notes in `meetings/`

- Each time this file is loaded at the start of a session, run `python3 scripts/update_readme_structure.py` before relying on the folder structure documented in `README.md`.

- Keep `AGENTS.md` and `CLAUDE.md` identical at all times.

- If either `AGENTS.md` or `CLAUDE.md` is edited, run `python3 scripts/sync_ai_docs.py` immediately.

- Use these naming conventions unless the project explicitly defines a stricter one:
  - Analysis scripts: `YYYY-MM-DD_study{N}_{analysis-type}_v{NN}.{ext}`
    - Example: `2026-03-11_study2_mediation-analysis_v01.R`
  - Draft files: `YYYY-MM-DD_{journal-name}_draft_v{NN}.{ext}`
    - Example: `2026-03-11_JCR_draft_v03.docx`
  - Meeting notes: `YYYY-MM-DD_meeting_{attendee-initials}.{ext}`
    - Example: `2026-03-11_meeting_YY-TL-GT.md`
  - Log files: `YYYY-MM-DD.{ext}`
    - Example: `2026-03-11.md`
  
- Update `PROJECT_REPORT.md` when important literature, theory structure, conceptual model, hypotheses, empirical package, analysis method, project stage, or next steps change.

- Update `MEASURES.md` when variables, measures, source citations, coding rules, aggregation rules, or sample/wave usage change.

  ——————

## Project Information

### Project Identity

- Project status: choose one from idea / literature review / data collection / data cleaning / analysis / writing / submission / revise and resubmit / accepted / published
- Last updated: 

### Research Question

- Primary research question:
- Core theoretical lens:

### Empirical Package

- Sample(s):
- Data source(s):
- Main variables:

### Collaborators

| Name | Role | Institution | Email | ORCID | Google Scholar |
|---|---|---|---|---|---|
| Your name | PI / author | University | name@university.edu | 0000-0000-0000-0000 | https://scholar.google.com/ |
