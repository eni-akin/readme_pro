# Release and OpenAI submission

README Pro has two distribution channels: the GitHub-backed Codex marketplace and the shared OpenAI directory. A GitHub release does not create or update an official listing.

## Build and check

Use Python 3.9 or newer. From the repository root:

```sh
python3 -m pip install -r requirements-dev.txt
python3 -m unittest discover -s tests -v
python3 scripts/package_release.py
```

The builder uses `plugin.json` as the version source. It includes only the manifest, license, icon, and skill directory, rejects unexpected metadata or escaping asset paths, checks the archive inventory, and validates extracted files. The output ZIP and checksum are in ignored `dist/`. If that version already exists, use a fresh output directory with `--output-dir /absolute/path/to/output`; do not overwrite published release artifacts.

Inspect the ZIP itself before uploading. Do not add marketplace catalogs, Git history, dependency directories, authentication files, `.app.json`, app bindings, or unrelated project instructions. The portable package has no MCP configuration or executable runtime.

## Test the installed plugin

Register and install in temporary Codex state rather than changing the maintainer's normal configuration. Test the six cases in [evaluation.md](evaluation.md) through the installed skill and verify its references resolve from the installed directory. Record the Codex version, actual results, and unavailable checks in [validation.md](validation.md). Compare review-only input hashes and content outside a targeted section.

After pushing the catalog, verify these same commands from GitHub in fresh test state:

```sh
codex plugin marketplace add eni-akin/readme_pro
codex plugin add readme-pro@eni-akin
```

Check the installed version and skill inventory, then begin a new chat to exercise the skill. Keep examples and fixture repositories free of private data. Never copy account credentials into a release or test evidence.

## GitHub release

Commit the validated package and documentation, push, then publish a matching version tag and GitHub release with the ZIP, checksum, release notes, and tested Codex version. Record the source commit in the release notes. Verify downloads against the published SHA-256 file.

## Official OpenAI directory

Publisher: Eniola Akinpelumi. Initial release: 0.1.0, free, English, Developer Tools, without publisher-imposed country restrictions. The directory is shared with ChatGPT, with Codex as this project's tested workflow.

1. Open [OpenAI Plugins](https://platform.openai.com/plugins), select the owning organization/project, confirm submission permissions, and complete individual developer verification. Keep verification documents outside the repository.
2. Upload the validated skills-only ZIP. Inspect the saved publisher, version, exactly one skill, icon, descriptions, starter prompts, public URLs, and country availability. Upload creates a draft, not a public listing.
3. Resolve required metadata checks and skill scans for that version. Skills-only packages need no MCP cases, demo recording, or reviewer credentials. The publisher must personally review and complete policy attestations.
4. Submit the selected draft for review. Record the actual state and address reviewer feedback with a complete corrected ZIP. Do not claim approval while review is pending.
5. Once approved, publish that exact version, verify the public listing URL and name search, install it from the directory, and check its skill inventory and main workflow. Only then add the official listing link to the README.

If the portal reports an access or eligibility restriction, record its actual message and resolve it with the organization owner or OpenAI. Do not create duplicate private plugins or add a server to bypass an eligibility check. No publisher identity, scans, attestations, review, or publication is established merely by a successful local build.

Follow the current [submission guide](https://developers.openai.com/plugins/deploy/submission) and [submission error reference](https://developers.openai.com/plugins/deploy/submission-errors). Four listing URLs are supplied for helpful public information; current rules make them optional for skills-only ZIP submissions. Review the package's privacy and terms pages before submitting.

## Updates

Increment the semantic version, update release notes, rerun affected checks, and publish matching GitHub artifacts. To update the official listing, upload a complete new ZIP to the existing plugin, resolve its checks/review, and publish the approved package version. Changes pushed to GitHub do not update the official directory automatically. Never replace a previously published archive under the same version.
