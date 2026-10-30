# Domain Docs

How engineering skills consume this repo's domain documentation.

## Before exploring, read these

- `GLOSSARY.md` at the repository root
- `docs/adr/` entries relevant to the area being changed

If these paths do not exist, proceed silently. Domain-modeling skills create them only when they are needed.

## File structure

This is a single-context repository:

```
/
├── GLOSSARY.md
├── docs/adr/
└── src/
```

## Use the glossary's vocabulary

Use terms defined in `GLOSSARY.md` in issues, proposals, tests, and implementation. Reconsider unfamiliar synonyms or note genuine terminology gaps for domain modeling.

## Flag ADR conflicts

Explicitly surface any proposed change that contradicts an existing ADR rather than silently overriding it.
