# ADR-002

# Development Tooling

Status

Accepted

---

## Context

The project requires a unified development workflow across all environments.

---

## Decision

The official development tools are:

- uv
- Ruff
- Ruff Format
- MyPy
- Pytest
- Task
- Pre-Commit

All Python commands must be executed through:

```
uv run
```

Task is the official task runner.

---

## Consequences

Benefits

- Consistent environments.
- Reproducible executions.
- Simplified onboarding.
- Single source of truth.