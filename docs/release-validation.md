# README Pro 0.1.0 release validation

Validated October 31, 2026 with Codex CLI 0.159.0. These checks cover the portable plugin and Codex installation. They do not establish OpenAI publisher verification, portal scans, approval, or official publication.

## Packaging and presentation

- Root manifest passed the official Agent Plugins 1.0.0 JSON schema.
- Skill Creator validation passed for the unchanged skill instructions.
- Unit tests passed for exact archive inventory, reproducible builds, invalid listing metadata, and escaping icon paths.
- The extracted archive passed metadata, skill/reference, icon, license, and byte-equality checks. Two independent builds produced identical archive bytes.
- The final 1024 × 1024 PNG is below 5 MiB. Its silhouette was inspected at 128, 48, and 24 pixels on light and dark backgrounds. It was generated with built-in ImageGen and resized to the required square dimensions.
- The updated README was rendered locally and inspected, with no page overflow. This was a local Markdown preview, not GitHub's exact renderer.
- Local Markdown links/fragments and image references resolved. The skill text and its references remain unchanged from the standalone release.

## Installed-plugin checks

A fresh temporary Codex state registered the local marketplace and installed `readme-pro@eni-akin` version 0.1.0. The CLI reported it installed and enabled. No compatibility manifest was required. The package contains exactly one skill and all three reference documents.

The final six-case pass loaded that isolated profile's enabled plugin configuration. Each session read the installed skill and its applicable bundled references. Fixtures used synthetic data. Source execution used Python 3.12.14 where relevant.

| Case | Observed result |
| --- | --- |
| CLI without README | Created a repository-backed README; verified sample output `5`, help, whitespace/Unicode behavior, empty input, missing arguments/files, and invalid UTF-8 |
| Library | Created source-installation and public API documentation; installed into an isolated Python environment and verified examples outside the source directory |
| Targeted quick-start edit | Verified live startup and expected JSON on both documented ports; assertions confirmed every byte outside Quick start remained unchanged |
| Stale application README | Corrected setup, unsupported features, and configuration; verified both GET routes plus 404/501 behavior; attribution preserved |
| Educational ML evaluation | Reproduced `accuracy=0.75 n=4`, demonstrated the negation failure, and explained synthetic data and unsupported claims |
| Review without edits | Identified incorrect routes, ignored flags, and unsupported auth, license, readiness, and throughput claims; exercised live health/404 behavior; before/after file hashes matched |

An initial network-restricted attempt could not connect to Codex. It was stopped before rerunning with approved network access. A preliminary source-focused run reported its unavailable build/socket checks; the final pass used the enabled isolated configuration, available Python runtime, and local-network access. All six final sessions completed successfully.

## Public GitHub acceptance

After the package/catalog push, a second fresh Codex state successfully ran:

```sh
codex plugin marketplace add eni-akin/readme_pro
codex plugin add readme-pro@eni-akin
```

The CLI reported version 0.1.0 installed and enabled from the Git-backed marketplace. The installed manifest, icon, skill, and all three references matched the checked source bytes. Exactly one skill was present. All four listing URLs were fetched without authentication and served the expected public project, issue tracker, privacy, and terms content.

## Release artifact

File: `readme-pro-0.1.0.zip`

SHA-256:

```text
5144d4c3d6ba6aa139902641b88f92e7743241b91a01e5d438c4fa0978b4415e
```

The ZIP includes only one plugin directory containing the portable manifest, MIT license, PNG icon, and complete skill directory. It excludes the marketplace catalog, project instructions, source-control files, development scripts, test fixtures, dependencies, and authentication state.

## Limits

Generated fixture READMEs received source checks, not individual rendered previews. Declared runtime ranges, other operating systems, the application's alternate PORT example, large real-world repositories, and other agent products were not comprehensively tested. Official directory access, publisher identity, saved-draft metadata, portal scans, policy attestations, review, and publication require separate verification in the OpenAI portal.
