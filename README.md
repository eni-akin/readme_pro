# README Pro

An agent skill that turns a repository into a clear, credible, and polished project README.

README Pro helps a coding agent inspect what the project actually does, choose a structure for its readers, show useful proof, and document a path to the first working result. It supports creating a README, improving an existing one, and reviewing one without edits.

[Install](#install) · [Use it](#use-it) · [Examples](examples/before-after.md) · [Skill instructions](skills/readme-pro/SKILL.md)

## What it brings to the page

- A specific explanation of the project and its value.
- Examples, screenshots, demos, or results that demonstrate real behavior.
- Setup and usage instructions checked against repository files and, when feasible, execution.
- Content priorities for applications, CLIs, libraries, APIs, AI/ML, data analysis, educational projects, and monorepos.
- Consistent formatting, useful navigation, accessible assets, and relevant badges.
- Honest limitations and a clear account of anything the agent could not verify.

The skill adapts the layout to the project and audience. It preserves useful existing content, attribution, and the project's voice. It never treats missing evidence as permission to invent a feature or result.

## Install

### Codex

Clone [this repository](https://github.com/eni-akin/readme_pro), then copy `skills/readme-pro/` into your personal skills directory. Current [Codex documentation](https://learn.chatgpt.com/docs/build-skills) lists `~/.agents/skills/` for user skills and `.agents/skills/` for repository skills. Keep `references/` and `agents/` alongside `SKILL.md`.

For example, on macOS/Linux, from this repository's root:

```sh
mkdir -p ~/.agents/skills
cp -R skills/readme-pro ~/.agents/skills/
```

The installed entry point should be `~/.agents/skills/readme-pro/SKILL.md`. Check for an existing installation before copying so you can preserve local customizations. Codex detects skill changes automatically; restart it if the skill does not appear. If your environment uses another configured skill location, use that location instead.

### Other skill-capable agents

The core is plain Markdown with `name` and `description` frontmatter and relative reference files. Copy the whole `skills/readme-pro/` directory into the skill location documented by your agent. `agents/openai.yaml` supplies Codex-specific UI metadata. Other agents' discovery paths and invocation syntax vary; compatibility must be tested in the chosen agent.

No API key, external service, or runtime package is required by the skill itself. The target project's own setup may have additional requirements.

## Use it

In Codex:

```text
Use $readme-pro to create a README for this repository.
```

```text
Use $readme-pro to improve this README for developers evaluating the library.
Preserve our existing branding and contribution links.
```

```text
Use $readme-pro to review README.md without editing files.
Focus on setup accuracy and unsupported claims.
```

```text
Use $readme-pro to improve only the quick start. Leave the rest of the README as it is.
```

You can specify the reader, documentation language, tone, or files in scope. Otherwise the agent infers sensible choices from the repository. Codex can also select the skill automatically for matching README requests.

## What to expect

The agent inspects relevant source, manifests, examples, tests, documentation, and assets. It selects content for the project type, writes within your requested scope, then checks facts, commands, links, and presentation. Its handoff identifies changed files, verification results, and remaining gaps.

Some checks depend on the host environment. Without a renderer, browser, credentials, or required hardware, the agent should state that limitation. It should ask for an essential missing fact, omit an unsupported optional claim, or suggest a useful missing capture. A README request does not authorize publishing, changing repository settings, or altering application behavior.

## Package layout

```text
skills/readme-pro/
├── SKILL.md
├── LICENSE
├── agents/openai.yaml
└── references/
    ├── project-types.md
    ├── presentation.md
    └── verification.md
```

The entry point contains the workflow. References supply project-specific priorities, presentation decisions, and verification criteria. There are no required scripts or bundled visual templates.

## Development and contributions

See [the evaluation guide](docs/evaluation.md) for realistic acceptance cases. Improvements should address observed output problems, keep the entry point concise, and put conditional detail in the relevant reference. Include the request, minimal repository context, observed failure, and evidence that a proposed change fixes it. Remove secrets before sharing fixtures or outputs.

This repository contains the skill source; packaging does not itself establish that every agent or project has been tested. See [validation results](docs/validation.md) for the checks actually performed.

## Design references

The editorial direction draws on the [README research supplied by the author](https://chatgpt.com/share/6ae4f7ff-53bc-83e8-9a7d-798f5d06c1f0): help readers understand, evaluate, and try the project. The guidance is adapted into decisions rather than copied into a universal template. See [reference notes](docs/references.md) for further examples.

## License

[MIT](LICENSE) — copyright 2026 Eniola Akinpelumi.
