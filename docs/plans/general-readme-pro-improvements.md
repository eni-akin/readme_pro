# General README Pro improvements and next research plan

Prepared November 1, 2026. This branch updates the base generator's instructions; it does not introduce a fixed README template. The changes apply to future generation and relevant presentation edits. Review-only and targeted-edit boundaries remain in force.

## Evidence and decision

The evidence is the [17-repository catalog](../research/2026-11-01-trending-readme-catalog.md), especially its [layout comparisons](../research/2026-11-01-trending-readme-catalog.md#comparing-layout-decisions), [upkeep observations](../research/2026-11-01-trending-readme-catalog.md#observed-upkeep-problems), and [implications](../research/2026-11-01-trending-readme-catalog.md#implications-for-readme-pro). Exact studied versions are in the [source register](../research/2026-11-01-trending-readme-sources.json).

This is a dated, AI-heavy convenience sample. Trending membership establishes neither good design nor causation. The additions below are editorial hypotheses grounded in observed patterns and tradeoffs. Their effect on generated pages still needs behavioral testing.

The strongest general addition is a deliberate opening: identify the product, explain its task, expose a supported next action, and place useful evidence nearby. Centering, badges, tables, and media are choices within that opening. Their usefulness depends on the project and reader.

## Extracted elements and changes now

| Reusable element | Research basis | Decision for the base generator |
| --- | --- | --- |
| Compact centered identity | Claude-mem, Lightpanda, and Hyprland use prominent branded openings; their density differs | Add explicit guidance to consider a centered existing logo/name with a short description and actions. Keep long prose and instructions left aligned. Preserve an established treatment when it works; text-led openings remain valid. |
| A visible primary action | Hex prioritizes downloads; Hyprland routes to task docs; OpenMausBot distinguishes binaries from source setup | Add a clear hierarchy among Download, Try, Quick start, and Docs. Select existing destinations for the intended reader. |
| Useful badges | The sample mixes technical status, release/license information, community access, and popularity | Expand the badge guidance with question-to-source choices. Add only badges backed by the actual workflow, release, package, terms, report, or support destination. |
| Evidence close to a decision | Lightpanda leads with comparisons, AiSOC with a demonstration, Kornia with suitability qualifications | Explain where to place proof according to the question it answers. Existing rules still require measurement context and genuine assets. |
| Navigation matched to depth | Claude-mem uses jump links and a docs directory; Ziwei has contents; Hyprland delegates to its wiki | Distinguish compact task links, a contents list, and a descriptive documentation directory. A short page can omit all three. |
| Tables for repeatable choices | Hex's download matrix, Ziwei's release/schema tables, and Public APIs' repeated fields | Add a decision rule for tables versus lists: comparable fields suit tables; exploratory topics and long descriptions suit sections or bullets. |
| Optional depth through disclosure | Lightpanda collapses an integration example; Kornia shows how collapsing changes emphasis | Add labeled details blocks as an option for advanced material. Keep the recommended first-use route expanded and costly prerequisites visible. |
| Narrow-screen rhythm | Four mobile captures showed badge/link wrapping and taller stacked introductions | Extend rendered checks to a narrow viewport, focusing on wrapping, tables, and the distance to the main task. Theme checks already exist. |
| Compact language and community routes | Claude-mem and Kronos expose translation choices; Ziwei serves its domain language | Preserve existing translations and commitments while keeping the main route discoverable. Link only available translations. |
| Consistency across surfaces | Counts, versions, inventories, and older collapsed content drifted in several examples | Add explicit checks across opening claims, tables, badges, images, linked docs, and collapsed sections. Distinguish differing scope/date from proven errors. |
| Scope based on the reader's job | Hex and Handy have different depths despite a similar utility category | Clarify the assignment step: decide whether the reader downloads, tries, integrates, evaluates, reproduces, adapts, or browses before choosing depth/order. |

These changes live in [SKILL.md](../../skills/readme-pro/SKILL.md), [presentation.md](../../skills/readme-pro/references/presentation.md), and [verification.md](../../skills/readme-pro/references/verification.md). They reuse the existing instruction layout. [Evaluation guidance](../evaluation.md#research-derived-contrasts) points to the next stage below.

### Badge choices in practice

| Reader question | Candidate when supported | Required source |
| --- | --- | --- |
| Are the relevant checks passing? | Build/test status | This repository's applicable workflow and branch/results |
| What can I install or download? | Release/package version | The actual release page or package registry entry |
| What reuse terms apply? | License | The actual license and material scope |
| Where can I learn or get help? | Documentation/community | An existing maintained destination |
| What test coverage is reported? | Coverage | A real report with the relevant scope |
| Is my runtime/platform supported? | Runtime/platform indicator | Declared support constraints or relevant CI evidence |

A badge is optional even when its source exists. A small number of relevant badges is more useful than repeating every repository property. Stars, download counts, and trend rank can convey activity, but cannot substitute for technical evidence. No universal badge count or automatic popularity row is added.

### Existing strengths retained

The base already requires repository evidence, a first useful result, genuine assets and alt text, qualified metrics, existing attribution, language preservation, and useful deeper links. It already permits centered introductions and rejects badge clutter. Those principles are retained rather than duplicated into a new checklist.

This pass leaves project-type profiles unchanged. Dataset releases, workflow kits, and learning catalogs are promising missing cases, but need focused evaluation before expanding that reference. It also leaves package identity, invocation metadata, version 0.1.1, logos, the distribution README, and published release artifacts unchanged. There is no new runtime dependency or template asset.

### Elements not promoted to defaults

Large sponsor strips, star-history charts, trending badges, long translation strips, repeated commercial calls to action, extensive news feeds, mandatory screenshots, and identical heading sequences are not general defaults. They can serve an established project, but the sample does not show that adding them improves every README. Existing sponsorship, credits, and user-selected personality still deserve preservation.

## Next-stage plan

Recommendation: turn the research into comparative behavioral evaluations before adding more generator rules. The research describes variation; the next useful question is whether README Pro makes appropriate choices when given different evidence and reader needs.

### Stage 1 — Define fixtures and the baseline

Start from the existing [six-case evaluation method](../evaluation.md). Pin the baseline skill to research commit `7d6412b229d804346bf6a31da4f89f6e81257055` and the candidate to the final commit of this branch. Extract each skill into an isolated temporary location. Keep source fixtures identical between runs and record hashes, prompts, skill commit, agent/client version, available tools, and execution permissions.

Create small original fixtures from the contrasts below, using synthetic data and local assets. Use the external projects only as design references; do not run their software or copy their logos, prose, claims, or screenshots. Supply enough raw evidence to make an editorial decision without instructing the author which layout to choose. Keep assessment criteria separate from generation prompts.

Deliverable: a fixture inventory, fixed prompts, evidence inventory, and assessment rubric. Completion: every expected factual assertion has a source and every case has a reader task and an observable success condition. Store maintainable fixtures under `tests/fixtures/` only when implementing this stage; save run artifacts separately from installable skill files.

### Stage 2 — Compare generated pages

Run the original six regression cases plus these eight contrasting fixtures against both baseline and candidate. One run of 14 cases for each version produces 28 initial artifacts. This is a bounded qualitative comparison, not a statistical estimate of reliability. Repeat cases when a failure or ambiguous result needs confirmation and record those repetitions.

| Contrast | Fixture A | Fixture B | Decision to assess |
| --- | --- | --- | --- |
| Utility scope, inspired by Hex/Handy | Focused binary download page with existing releases | Similar utility with meaningful platform troubleshooting and help docs | Does the first stay compact while the second provides selective routes into support? |
| Evidence, inspired by Lightpanda/FreeToken | Infrastructure tool with a qualified local benchmark | Research engine with mechanisms and a paper but no measured comparison | Does the first expose benchmark context while the second avoids invented performance evidence? |
| Browsing, inspired by Public APIs/AI Engineering Hub | Lookup catalog with repeated decision fields | Learning collection with difficulty and prerequisite progression | Does the index support lookup versus learning without forcing the same table or install section? |
| Deployment, inspired by OpenBot/AiSOC | Adaptable template with deployment boundaries | Demonstrable service with operational limitations and a smoke check | Do readers see scope, prerequisites, and the relevant safe first action? |

Distribute these evidence variations across the fixtures: existing centered branding; an effective text-led opening; verified badge sources; missing badge sources; an absent screenshot; a stale headline count; older collapsed content; and a separate translation. Variation should reveal unsupported additions and over-normalization, not demand a particular visual style.

Deliverable: baseline/candidate READMEs, performed command results, source references, and concise findings for all cases. Completion: both versions have an artifact and assessment for every case, with failures separated from unavailable checks.

### Stage 3 — Inspect behavior and presentation

Assess each artifact without telling the reviewer which version produced it where practical. Evaluate the main reader task, factual support, action visibility, useful proof, selective depth/navigation, and maintenance consistency. Record concrete observations, for example whether a download route precedes contributor setup or a stale count is corrected from the inventory. Avoid scoring by heading count, source length, badge count, or centering alone.

Render the affected outputs in a GitHub-compatible preview at desktop and narrow widths; 1440 × 1200 and 390 × 844 provide continuity with the catalog. Inspect theme-sensitive artwork against light and dark backgrounds. Check wrapped action/badge rows, table readability, image meaning, expanded first-use instructions, and the main route after media stacks. Document the renderer and differences from GitHub itself. A source inspection cannot stand in for an unavailable render.

Run the documented minimal workflow where safe. Compare hashes for review-only cases and diffs outside the requested section for targeted edits. Evaluate accuracy independently of visual preference.

Deliverable: an assessment table and relevant render captures. Completion: every case has pass/fail/unchecked evidence for applicable criteria. Fabricated features, URLs, badges, results, or licenses; hidden essential prerequisites; changed review inputs; or edits outside a targeted request block acceptance. Improved appearance does not offset these failures.

### Stage 4 — Refine only demonstrated gaps

Compare candidate outcomes with baseline. Retain changes that improve routes or presentation without factual or scope regressions. Narrow or remove guidance that causes gratuitous centering, badge additions, tall openings, or unnecessary handbook sections. If the new reader jobs fail, extend only the responsible project-type guidance, then rerun affected cases and the preservation regressions.

Potential additions after evidence supports them are a dataset release profile, a template/workflow-kit profile, a lookup-versus-learning distinction, and a compact gateway profile. Existing AI/data/application guidance may already be sufficient; evaluation should settle that before adding text.

Deliverable: a small follow-up diff with a dated validation record linking observed outcomes to each retained change. Completion: every hard failure is resolved or the responsible candidate change is reverted; every unchecked condition remains explicit. If the candidate shows no improvement, retain only useful evaluation assets and simplify the instructions.

### Stage 5 — Prepare a release after validation

Once the behavior is acceptable, choose the next version and follow [releasing.md](../releasing.md): package tests, isolated install, current-skill reference resolution, six installed-workflow regressions plus affected new cases, and artifact verification. Record the tested client/version and exact candidate commit. Use a fresh build directory and preserve published archives.

Deliverable: a release-ready change with validation evidence and release notes explaining user-visible behavior. Merge and release publication are later actions; this request authorizes the improvement branch push and the plan. Official directory onboarding remains deferred.

### Potential outcomes and decision points

| Observed outcome | Next action | Expected benefit |
| --- | --- | --- |
| Candidate improves task routing and stays accurate | Retain the guidance and prepare a validated release | More deliberate openings with project-specific depth |
| Candidate makes more attractive but taller or less usable openings | Narrow the centering/badge guidance and retest | Preserve visual clarity without delaying useful action |
| New reader jobs expose a profile gap | Add the smallest missing profile and evaluate it | Better dataset, template, catalog, or docs-gateway handling |
| No observable improvement over baseline | Remove ineffective additions; keep reusable fixtures | Avoid instruction growth without demonstrated value |
| Results depend on environment or reviewer preference | Record uncertainty and test the disputed behavior again | A bounded decision instead of an unsupported quality claim |

The intended outcome is a generator that chooses different useful pages from different evidence, with repeatable evaluations to protect those choices. This work cannot establish increased stars, adoption, accessibility conformance, or universal readability from the trending sample.

## Status and verification boundaries

The instruction changes, extracted-element decisions, evaluation pointer, and this plan are implemented in this branch. Stages 1–5 are planned work; no new behavioral evaluation results, generated-page render results, installed-plugin checks, or release are claimed here. Static skill/package checks for this branch are reported in the completion handoff. Historical validation records remain historical.

Checks performed for this change:

- Skill Creator's `quick_validate.py` passed for `skills/readme-pro`.
- Both existing package tests passed, covering reproducible archive construction, inventory, invalid metadata, and escaping icon rejection. Their archives were built only in temporary directories.
- All 17 local file/heading links across the six changed Markdown files resolved; fenced blocks were balanced.
- `git diff --check` passed.

These checks establish structural/package integrity, not improved generation behavior. The existing development requirement, PyYAML, was installed in a temporary environment; no project dependency was added.
