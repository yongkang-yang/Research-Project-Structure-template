# Project AI Brief

## Rules

- At the start of each session, load:
  - `README.md`
  - `PROJECT_REPORT.md`
  - `MEASURES.md`
  - the two most recent notes in `logs`

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
  
- Update `PROJECT_REPORT.md` when important literature, theory structure, conceptual model, hypotheses, empirical package, analysis method, project stage, or next steps change. Only update content within the existing placeholder items `[to be filled]`; do not add or remove any sections.

- Update `MEASURES.md` when variables, measures, source citations, coding rules, aggregation rules, or sample/wave usage change.
- update `Logs` when the conversation is complete. 

## Custom Rules

Do not modify the rules above. Add all new project-specific rules below this line.

