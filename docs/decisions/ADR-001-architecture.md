# ADR-001

# Project Architecture

Status

Accepted

---

## Context

The backend is expected to grow into a modular platform composed of multiple bounded contexts such as:

- Auth
- Academy
- Players
- Coaches
- Teams
- Training
- Payments
- Notifications

The architecture must support long-term scalability while keeping modules independent.

---

## Decision

The project adopts:

- Domain-Driven Design (DDD)
- Clean Architecture
- CQRS
- SOLID principles

Each module is responsible for its own:

- Domain
- Application
- Infrastructure
- Presentation

Shared technical concerns belong to Core.

---

## Consequences

Benefits

- High cohesion.
- Low coupling.
- Independent modules.
- Better testing.
- Easier maintenance.

Trade-offs

- More folders.
- More abstraction.
- Higher initial complexity.