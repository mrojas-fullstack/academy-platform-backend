# ADR-003

# Quality Gates

Status

Accepted

---

## Context

Code quality must be validated before changes reach the repository.

---

## Decision

Two quality gate levels are defined.

Developer

```
task verify
```

Runs:

- Ruff
- Ruff Format
- MyPy

Continuous Integration

```
task verify-full
```

Runs:

- Ruff
- Ruff Format
- MyPy
- Compile
- Pytest

---

## Consequences

Benefits

- Fast local feedback.
- Strong CI validation.
- Consistent workflow.