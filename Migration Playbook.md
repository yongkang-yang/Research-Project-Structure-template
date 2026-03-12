# Migration Playbook

Use this playbook，if you already have:

- old folders
- legacy filenames
- mixed study materials
- existing drafts, data files, and outputs

- migrating an existing empirical research repository into the `Research-Project-Structure-template` format

## Objective

The default principle is:

- structure first
- study mapping second
- cleanup last

## Workflow

Copy the template skeleton first, infer the study map from manuscript and submission materials, build `studies/` packages before moving study files, preserve filenames, archive ambiguity, and delete only empty legacy folders at the end.



## How To Infer The Study Structure

Before moving study files, read the most reliable project-defining documents.

Recommended order:

1. latest manuscript draft
2. latest submission draft or conference paper
3. project report or theory memo
4. study design files
5. result summaries and output files

Use those materials to answer:

- how many active studies exist?
- which studies are pilots or dropped?
- which studies are merged, renumbered, or still evolving?
- which study labels are final versus temporary?

If there is study-number ambiguity, stabilize the conceptual package first and postpone renumbering.



## How To Move Files Safely

Move files in three passes.

### Pass 1: obvious project-level materials

Examples:

- IRB and consent files -> `compliance/`
- literature folders -> `literature/`
- manuscript drafts -> `writing/`
- slides -> `presentation/`

### Pass 2: obvious active study materials

Examples:

- study-labeled raw data
- study-labeled result files
- study-specific design documents

### Pass 3: ambiguous or mixed materials

If a file is useful but not confidently placeable, move it to:

- `studies/archive/legacy-mixed-materials/`

This is better than forcing a wrong assignment.

## File Naming Rule During Migration

Default rule:

- preserve original filenames during migration

Why:

- filenames often preserve provenance
- manuscript references may still use the old names
- duplicate checking is easier before renaming

Rename only after the structure is stable.

## How To Handle Pilots And Dropped Studies

Keep them out of active `studies/`.

Use:

- `studies/archive/pilots/`
- `studies/archive/dropped-studies/`
- `studies/archive/legacy-mixed-materials/`

This keeps active study packages clean and reduces AI-context noise.

## How To Handle `.gitkeep`

Use `.gitkeep` only to preserve intentionally empty folders in git.

Rules:

- if a new folder is empty and should exist in the template, keep `.gitkeep`
- if a migrated folder now contains real files, delete `.gitkeep`
- do not leave `.gitkeep` in populated folders unless there is a specific reason

In short:

- empty folder -> `.gitkeep` is fine
- populated folder -> remove `.gitkeep`

## Rules That Prevent Migration Errors

1. Never delete a legacy folder until its contents have been moved and checked.
2. Never assume old top-level folder names reflect the current study logic.
3. If two files may be duplicates, compare them before deleting either one.
4. If a file is ambiguous, archive it instead of guessing.
5. Update the root docs after major migration rounds.
6. Keep `AGENTS.md` and `CLAUDE.md` identical.



## Validation Checklist

Before considering the migration complete, confirm:

- `AGENTS.md` and `CLAUDE.md` are identical
- `README.md` matches the real folder structure
- each active study has a package under `studies/`
- pilots and dropped studies are archived, not mixed into active studies
- ambiguous leftovers are explicitly archived
- empty legacy folders are deleted
- `.gitkeep` is removed from folders that now contain real files
- `PROJECT_REPORT.md` matches the current empirical package
- `MEASURES.md` matches the current construct usage

For new repositories built from scratch, also confirm:

- new files are being added directly into the correct study or project-level folder
- the root directory is not becoming a storage area for drafts and exports
- empty scaffold folders still needed by the template retain `.gitkeep`



