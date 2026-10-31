# Choose content for the reader

Read the audience guidance and only the relevant project profiles. Section order follows the reader's next decision, not this file's order.

## Audience

| Reader | Prioritize |
| --- | --- |
| Adopter | Problem solved, compatibility, installation, first useful example |
| Engineer evaluating implementation | Working proof, setup, components, tests, consequential tradeoffs |
| Portfolio evaluator | Immediate description and result, accurate ownership, engineering decisions |
| Contributor | Development setup, checks, existing contribution and support routes |
| Researcher | Main result, evaluation context, data provenance, reproduction path |

Give skimmers enough information to understand the project before installation. Let deeper readers follow precise links.

## Application: frontend or full stack

Lead with the main workflow, an actual screenshot, and an existing demo if available. Explain the relationship between a hosted service and self-hosted code. Setup may require frontend/backend processes, external services, migrations, seed data, and environment variables. Show how to access the running app and complete one safe workflow.

Document browser support, responsiveness, accessibility decisions, authentication, and data handling when they materially affect use and are supported by evidence. Describe consequential missing functionality honestly. Request missing screenshots or give a concrete capture suggestion in the handoff; a fabricated interface is not project evidence.

## CLI

Put a useful command and representative output early. Explain installation separately from running source, shell/platform requirements, input and output paths, and relevant exit/error behavior. Show one common workflow before advanced flags. Use the actual help and tests to verify syntax. State overwrite, deletion, remote submission, or other significant effects before examples that perform them.

## Library or package

Lead with the task the package makes easier, installation, and a minimal import/use/result example. Verify public exports and the package name, and distinguish published-package behavior from unreleased source. Link broader API docs and examples rather than copying the full reference. Include runtime support and important interoperability limits only when established.

## API or backend service

Show a representative request and response with authentication placeholders and the correct base URL. Include required services, database initialization/migrations, sample data if available, startup, and a success check. Link endpoint documentation. Explain relevant validation, permission, rate, and resource limits based on implementation. Use synthetic data and safe endpoints in examples.

## AI/ML or research

Explain whether the project trains, fine-tunes, performs inference, or calls an external provider. Connect main results to the actual dataset/split, metric definition, sample size, baseline, configuration, and code/model version where known. Distinguish examples from measured evaluation; missing evidence means qualifying or removing the claim.

Separate lightweight inference/demo setup from full reproduction. Document model/data access, provenance and reuse constraints, downloads, hardware/memory, runtime, costs, seeds, and reproducibility limits where known. Link evaluation scripts, notebooks, model cards, or papers that exist. Explain meaningful failure cases and data handling. Never convert a toy score into a general performance claim.

## Data analysis

Lead with the question, main findings, and readable figures. Give data provenance, access requirements, cleaning steps, relevant variable definitions, and a path to reproduce outputs. Distinguish descriptive findings from supported causal claims. Keep sensitive or restricted datasets out of public examples.

## Educational implementation

State the concept and deliberate simplifications, provide a small example with known output, and identify tests or comparisons against known results. Credit tutorials and upstream work, and distinguish the author's additions. Describe limits relative to operational use without diminishing the learning value.

## Multi-service system or monorepo

Clarify repository scope, component responsibilities, and which path newcomers should run first. A compact architecture diagram helps when it explains actual data/request flow. Include only essential services and startup order in the root quick start; route component-specific instructions to existing package docs. Verify relative links from each document's directory.
