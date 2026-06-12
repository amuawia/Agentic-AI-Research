# Study 002 Prompt Set

## Overview

This directory contains the official prompt set used in:

Study 002: Foundation Model Comparison

The prompt set is shared across all evaluated providers to ensure methodological consistency and fair comparison.

Providers:

* OpenAI GPT
* Google Gemini
* Anthropic Claude

Workflow Architectures:

* Basic Agent
* Planner–Executor
* Planner–Executor–Reviewer

---

## Prompt Set Information

Prompt Set Version: 1.0

Status: Frozen

Effective Date: 2026-06-12

---

## Purpose

The purpose of this prompt set is to standardize task execution across all providers and workflow architectures.

No provider-specific prompt modifications should be introduced during official data collection.

Any modification to the prompts must result in a new Prompt Set Version.

---

## Files

### Basic Agent

```text
basic_agent.md
```

### Planner–Executor

```text
planner_prompt.md
executor_prompt.md
```

### Planner–Executor–Reviewer

```text
planner_prompt.md
executor_prompt.md
reviewer_prompt.md
```

---

## Change Control

Prompt Set Version 1.0 is the official prompt configuration used for Study 002.

Any future modifications must be documented in:

```text
shared/prompts/prompt_history.md
```

and assigned a new version number.

Examples:

* Prompt Set Version 1.1
* Prompt Set Version 2.0

---

## Reproducibility

Maintaining a frozen prompt set is essential to ensure reproducibility and comparability across:

* Providers
* Workflow Architectures
* Experimental Runs

All official Study 002 results should reference:

Prompt Set Version: 1.0
Status: Frozen
