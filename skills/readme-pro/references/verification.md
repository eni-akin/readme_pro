# Verification before delivery

Use checks proportional to the requested edit. A wording change does not require installing the project. A new quick start needs stronger evidence. Record performed checks separately from suggestions and blocked checks.

## Facts and integrity

- Trace material capability, status, compatibility, ownership, license, and metric claims to implementation, authoritative project files, or explicit user statements.
- Compare advertised commands against manifests, public exports, help, examples, and tests as applicable. Check names, flags, working directories, configuration names, and startup order.
- Ensure existing user work, useful warnings, attribution, and necessary links survive the edit.
- Use placeholders for secrets and synthetic example data. Check changed prose, URLs, logs, and images for exposed private data.

## First result

When safe and feasible, run the documented minimal path in a clean temporary checkout/environment, including one useful operation and its expected outcome. Inspect scripts first. A successful command in an already prepared environment does not establish a fresh-clone setup.

If execution needs unavailable hardware, credentials, downloads, paid services, or permission, verify the available sources and state exactly what remains untested. Do not invent expected output; use actual output, existing fixtures, or clearly identified illustrative output. Numerical results need enough context to be interpreted and, when claimed reproducible, an actual reproduction route.

## Links and presentation

- Resolve every added or changed relative file/image path from the document's directory and check heading fragments.
- Check external links when network access is available; distinguish a responding URL from a tested demo or authenticated service. Otherwise report them as unverified.
- Check heading nesting, code fences, table readability, navigation, badge targets, and image alt text.
- Inspect a GitHub-compatible rendered preview when available, including images at normal reading width and theme-sensitive graphics in light/dark views. Report source-only review when rendering is unavailable.
- Remove scaffold text, empty headings, broken placeholders, duplicated material, and unsupported promotional claims. Credential placeholders inside instructions are intentional and should remain clearly labeled.

## Reader acceptance

The opening explains the purpose and intended use. Evidence demonstrates something the project actually does. The recommended path identifies prerequisites and a recognizable success state. Important limits and attribution are accurate. Deeper material has useful links. The page feels like this project rather than a generic checklist.

Finish with the actual verification results and unresolved limits. For review-only requests, prioritize actionable findings with locations and evidence; keep the repository unchanged.
