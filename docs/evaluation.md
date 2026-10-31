# Evaluate README Pro

Package validation checks metadata and structure. Behavioral testing checks whether the skill actually improves the reader's experience. Run these cases again after material instruction changes, using isolated temporary repositories and the current skill.

## Method

Give the evaluating agent the skill path, the user request, and raw repository files. Keep scoring criteria separate from the prompt so the agent must make its own editorial choices. Inspect the generated artifact, execution evidence, and handoff. Record concrete failures; revise only the responsible guidance and rerun affected cases.

Use small self-contained fixtures, synthetic values, and no live external mutations. Review-only tests should compare file hashes before and after. Execute documented examples when safe. Mark unavailable renderers, network access, and dependencies as unchecked rather than passed.

## Cases

| Case | Example request | Evidence to evaluate |
| --- | --- | --- |
| CLI, absent README | Create a README for this tool | Actual help/flags, file effects, first task and output, no invented package install |
| Web app, stale README | Improve this README for evaluators | Implemented workflow vs planned features, correct scripts/config, real or explicitly missing assets, preserved attribution |
| Library | Document installation and a minimal example | Published vs source distinction, public exports, correct result and compatibility constraints |
| AI/ML project | Make the README credible for researchers | Dataset/metric context, reproduction command, resource limits, no invented evaluation or production claims |
| Misleading README, review only | Review without editing | Evidence-backed findings, unsupported claims identified, byte-for-byte unchanged input files |
| Targeted edit | Improve only the quick start | Correct setup instructions, no unrelated heading/branding/content changes |

## Acceptance

The page explains purpose quickly, shows credible project-specific evidence, and gives a supported next action. Commands and factual claims trace to project sources or execution. Applicable prerequisites and consequential limits are visible. Links and assets resolve, prose is scannable, attribution survives, and no unnecessary template sections appear. The handoff accurately distinguishes performed checks from unverified work.

Reject outputs that invent features, metrics, screenshots, licensing, ownership, or URLs; hide essential setup gaps; silently edit on review; expand a targeted request; or describe source inspection as successful execution.
