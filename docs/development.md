# Development Guide

## Overview

This document describes the development workflow used by **Academy Platform Backend**.

The objective is to guarantee a consistent codebase through automated validation, formatting, static analysis and testing.

---

# Development Environment

## Requirements

- Python 3.13+
- uv
- Task
- Git
- Pre-Commit

---

# Install Dependencies

```bash
uv sync --all-groups
```

---

# Install Git Hooks

```bash
uv run pre-commit install
```

This command only needs to be executed once after cloning the repository.

---

# Development Workflow

The expected workflow is:

```
Develop
    ↓
task lint
    ↓
task format
    ↓
Commit
    ↓
Pre-Commit
    ↓
Push
    ↓
GitHub Actions
```

---

# Task Commands

## Install dependencies

```bash
task install
```

---

## Run the application

```bash
task run
```

---

## Format the project

```bash
task format
```

---

## Fix lint issues

```bash
task lint
```

---

## Static type checking

```bash
task typecheck
```

---

## Compile source code

```bash
task compile
```

---

## Run tests

```bash
task test
```

---

## Local quality gates

```bash
task verify
```

This command executes:

- Ruff
- Ruff Format
- MyPy

This command is automatically executed before every commit.

---

## Full quality gates

```bash
task verify-full
```

This command executes:

- Ruff
- Ruff Format
- MyPy
- Compile
- Pytest

This command is executed by GitHub Actions.

---

# Code Quality

The project uses the following tools:

| Tool | Purpose |
|------|----------|
| Ruff | Linting |
| Ruff Format | Formatting |
| MyPy | Static type checking |
| Pytest | Testing |
| Task | Task runner |
| Pre-Commit | Local Git validation |
| GitHub Actions | Continuous Integration |

---

# Development Rules

## 1.

Never execute Python tools directly.

Always use:

```bash
task ...
```

instead of:

```bash
pytest

mypy

ruff
```

---

## 2.

All commits must pass:

```bash
task verify
```

---

## 3.

All pushes must pass:

```bash
task verify-full
```

---

## 4.

No code should be merged if GitHub Actions fails.

---

# Continuous Integration

Every push and pull request automatically executes:

```
task verify-full
```

The repository should always remain in a healthy state.

---

# Architecture Principles

The project follows:

- Domain-Driven Design (DDD)
- Clean Architecture
- SOLID
- CQRS
- Repository Pattern
- Unit of Work
- Domain Events

---

# Dependency Management

The official dependency manager is:

```
uv
```

All Python tools must be executed through `uv`.

---

# Project Philosophy

The goal is not only to produce working software.

The goal is to maintain a clean, consistent and scalable codebase over time.

Every change should improve the architecture instead of increasing technical debt.