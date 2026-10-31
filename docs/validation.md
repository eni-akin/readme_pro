# Validation record

For the plugin package and installed-plugin checks, see [0.1.0 release validation](release-validation.md). The original record below covers standalone skill authoring.

Validated on October 31, 2026. This records observed checks for the initial package, not a guarantee across all projects or agents.

## Package checks

- Initialized with Skill Creator's bundled initializer and validated with its `quick_validate.py`.
- Parsed Markdown, checked local file links and heading fragments, and checked Codex UI metadata and invocation settings.
- All nine Markdown documents parsed successfully; all 11 local links/fragments outside illustrative code blocks resolved.
- Rendered the distribution README and before/after examples locally, inspected full-page browser captures, and checked for page overflow. The preview used Python Markdown and GitHub-like styling, not GitHub's own rendering service.
- Preserved the repository's existing MIT license, including its copyright holder.
- Included the same license inside the installable skill folder so its terms accompany standalone copies.
- Checked installation guidance against [official skill documentation](https://learn.chatgpt.com/docs/build-skills). It documents `~/.agents/skills/` for user discovery and `.agents/skills/` for repository discovery.
- Opened the linked GitHub formatting guidance and six primary project references. The repository's own public URL could not be fetched by the web tool; its URL was confirmed from the local Git remote. The shared research conversation was read during planning, not fetched again during package validation.

## Independent forward tests

Two evaluating agents applied the skill to isolated synthetic repositories. The package author inspected their generated READMEs and execution reports.

| Case | Observed result |
| --- | --- |
| CLI without README | Documented actual syntax, sample output, input preservation, and error behavior; example printed `5` |
| Small library | Documented local source installation and public API; offline build/install and import produced `Hello World!` |
| Targeted quick-start edit | Corrected startup and success check; health request succeeded on an alternate port; assertions confirmed all content outside Quick start was unchanged |
| App with stale README | Replaced nonexistent npm/login/editing claims with actual Python setup and read-only workflow; page, JSON endpoint, and 404 checked; credits preserved |
| Educational ML evaluation | Reproduced `accuracy=0.75 n=4`; documented synthetic data, metric, absent split/baseline, and an observed negation failure |
| Review without edits | Identified unsupported authentication, route, flag, license, throughput, and readiness claims; SHA256 hashes confirmed both input files were unchanged |

No blocking instruction defect was observed in these cases. The package was revised during creation to correct the installation location before final validation.

## Limits

The library build used existing build tooling offline; a normal network-dependent isolated install was not exercised. One fixture's default port was occupied, so its alternate port was used. Synthetic tests do not establish real-world scale, GPU reproduction, all project profiles, or compatibility with other agents. Public GitHub publishing and an actual installed-skill discovery session are separate from these package tests.
