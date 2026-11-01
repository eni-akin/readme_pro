# README Pro 0.1.1 release validation

Validated November 1, 2026 with Codex CLI 0.159.0. The supplied Sparkle Page logo update was confirmed merged into `main` at `0fad26c` before release preparation.

## Changes and checks

- The README uses the supplied violet-and-gold primary symbol. The plugin listing and composer use the supplied white-on-violet app icon, rendered at 1024 × 1024 pixels. SVG masters are retained in the repository.
- Both existing packaging unit tests passed, covering exact archive inventory, reproducible output, invalid metadata, and escaping icon paths.
- The release builder validated metadata, PNG dimensions/size, skill/reference files, and license consistency; checked ZIP inventory and CRC; then extracted and validated byte equality against the source.
- The skill instructions, references, package builder, and tests are unchanged from 0.1.0. The six behavioral cases were not repeated for this branding-only change; see the [0.1.0 record](release-validation.md) for that evidence.
- An isolated Codex profile with 0.1.0 installed from the public GitHub marketplace ran `codex plugin marketplace upgrade eni-akin --json`. It reported the selected marketplace upgraded with no errors. `codex plugin list --marketplace eni-akin --json` then reported version 0.1.1 installed and enabled.
- The logo branch's visual checks covered the README render and symbols on light and dark backgrounds at practical sizes. Source SVGs matched the supplied kit. Those visual checks were not repeated during release preparation because the artwork is unchanged.

## Artifact

File: `readme-pro-0.1.1.zip`

SHA-256:

```text
70d62706f763acaec3912abe0629f43e8cff4bf88bebf9e67e87a0d62d6e75de
```

The plugin ZIP contains the manifest, MIT license, PNG icon, and complete skill directory. SVG masters and documentation are available in the repository and GitHub's source archives. The published 0.1.0 assets and checksums are preserved.

## Limits

The explicit upgrade command was verified; automatic-update timing was not measured. Other clients and operating systems were not tested for this release. Official OpenAI directory submission remains deferred: this GitHub release does not constitute an OpenAI directory submission, approval, or publication.
