# ADR-004

# Continuous Integration

Status

Accepted

---

## Context

Every push must validate the project automatically.

---

## Decision

GitHub Actions is the official Continuous Integration platform.

Every Push and Pull Request executes:

```
task verify-full
```

The workflow is intentionally minimal.

Future stages such as Docker build, deployment and coverage will extend the pipeline without changing its entry point.

---

## Consequences

Benefits

- Automatic validation.
- Reproducible builds.
- Healthy repository.
- Easy future expansion.