# Resume authoring

For any resume or CV creation, tailoring, rewriting, formatting, or saved edit, follow `skills/resume/SKILL.md` relative to this file. Use the `resumes-lol` MCP and always Jake's Resume template. Apply this even when a document, PDF, or specialist career skill is also involved. Read-only reviews may inspect local files without remote edits.

## Ponytail

Use Ponytail `full` for coding work in this project: solve the complete task with the smallest clear change.

Before editing, read the affected code and account for callers, tests, fixtures, configuration, and exports. Check for compatibility, data-loss, privacy, and security risks.

Prefer, in order: no change, an existing project pattern, the standard library or platform, an installed dependency, then the minimum new code. Preserve existing validation and error handling. Add one focused test or assertion for new non-trivial logic; trivial changes need none. Mark intentional limits as `shortcut: <limit>, <when to upgrade>`.

Do not trade away validation at trust boundaries, data-loss protection, security, accessibility, required hardware calibration, or explicit requirements. End each handoff with what was skipped or unchecked and any remaining risk.

## Agent skills

### Issue tracker

Issues are tracked as local Markdown files under `.scratch/`. See `docs/agents/issue-tracker.md`.

### Triage labels

Triage uses the five default canonical labels. See `docs/agents/triage-labels.md`.

### Domain docs

Domain documentation uses a single-context layout. See `docs/agents/domain.md`.
