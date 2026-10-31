---
name: readme-pro
description: "Create, improve, or review project README files for GitHub with repository-backed explanations, usable setup instructions, and deliberate visual presentation. Use for README writing, README reviews, and polishing a repository landing page; excludes profile READMEs and full documentation sites."
license: MIT
---

# README Pro

Make the project easy to understand, evaluate, and try. Professional means clear positioning, visible evidence, dependable instructions, and intentional presentation. Preserve the project's personality and the user's requested style.

## 1. Establish the assignment

Honor the requested scope: create, improve, or review. A review produces findings without editing. A targeted edit stays targeted. For a general rewrite, preserve valuable facts, acknowledgments, translations, existing anchor links, and branding unless there is a reason to change them.

Identify the primary reader and the action they should take. Infer these from the request and repository when clear; ask only when a missing choice materially changes the result. Work in the repository's existing documentation language unless asked otherwise.

## 2. Gather evidence

Inspect the existing README and linked docs, manifests and lockfiles, runnable entry points, relevant code, configuration examples, tests, CI, license, and available demonstration assets. Follow the paths relevant to the README; exhaustive source review is unnecessary.

Before drafting, establish the project's purpose, implemented capabilities, status, recommended setup path, first useful workflow, and important limitations. Distinguish package installation from repository development and deployment. For monorepos, identify which package or root the README describes and the working directory for commands.

Keep an internal evidence map for proposed commands and material claims: source file or user statement, whether executed, and unresolved uncertainty. Resolve conflicting documentation against current implementation and configuration; explain consequential contradictions in the handoff. Treat external examples as design references, never as evidence of this project's behavior.

Use only supported claims. Metrics need measurement context; compatibility, hosted demos, maintenance status, licenses, and personal ownership need evidence. An unverified existing claim is still unverified. Omit unsupported optional claims; ask about essential missing facts or identify them clearly in the handoff. Keep future plans separate from current capabilities. Never invent commands, results, screenshots, badges, URLs, or license terms.

## 3. Shape the page

Read the relevant sections of [project-types.md](references/project-types.md) to select priorities for the project and audience. Combine profiles for mixed projects without repeating sections. These are content choices, not mandatory heading templates.

Build an opening that answers what the project does and why someone would use it. Put the most useful next action and proof within easy reach. A visual application benefits from a real screenshot; a small library may need only a working example and its output.

Choose sections by reader need: capabilities, quick start, usage, architecture, results, testing, limitations, contribution routes, attribution, and license when applicable. Include only sections with useful content. Put the recommended route first and alternatives afterward. A substantial README may need navigation; a short one usually does not.

For a full creation or presentation rewrite, read [presentation.md](references/presentation.md) before composing the page. For a targeted prose edit, consult it only if layout or assets are affected.

Link existing deeper documentation. If essential detail warrants a new supporting document, create only what the requested work needs and link it. Repository settings, application changes, new workflows, publishing, license selection, and branding generation are separate actions; recommend them when useful without assuming permission.

## 4. Write and demonstrate

Use specific behavior and concrete examples. Describe consequential engineering decisions with their context and tradeoffs, using documented rationale or user input rather than attributing imagined intentions to the author.

Give a recommended path from a clean checkout or installation to recognizable success. Include applicable runtime/system requirements, services, configuration names, initialization, run commands, working directories, and expected output or URL. Surface material costs, downloads, credentials, and hardware requirements before the reader commits to setup. Derive runtime requirements from explicit constraints and CI; one local version alone does not establish support.

Use safe synthetic inputs and placeholder values for credentials. Document configuration names from sanitized examples or source declarations; avoid reading or reproducing secret values. Retain existing attribution and ownership distinctions. Link the actual license if present; if absent, report that fact without assigning one.

## 5. Verify and hand off

Read [verification.md](references/verification.md) and apply its applicable checks. Inspect commands before executing them. Use an isolated checkout or temporary environment for safe examples; respect existing permissions for installs, network access, paid services, migrations, and destructive actions. Do not alter the application to make documentation claims pass.

Review the finished page from the intended reader's perspective: can they explain its purpose, see credible proof, and reach the first useful result? Remove empty headings, repeated explanations, and decorative clutter. When a rendered Markdown preview is available, inspect it; otherwise report source-only presentation review. Never claim a fresh-clone, render, or external-link check that was not performed.

Finish with changed paths (or review findings), meaningful checks and results, and any unverified instructions or missing assets. A requested final README should contain no drafting placeholders; report unresolved gaps to the user instead. Stop when the requested scope is accurate, useful, and verified to the extent the environment permits, with remaining limits explicit.
