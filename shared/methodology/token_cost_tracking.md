# Token and Cost Tracking Methodology

## Version

Current Version: V1.4.3

## Purpose

This document describes the token estimation and cost estimation methodology used in Study 002.

## Token Estimation Method

Actual provider-reported token usage is not currently collected through workflow execution.

Therefore, token usage is estimated using character counts.

Formula:

estimated_tokens = round(character_count / 4)

The estimation is applied consistently across all providers and workflow architectures.

## Workflow Coverage

### Basic Agent

Token estimation includes:

* System prompt
* User prompt
* Final model output

LLM Calls: 1

### Planner–Executor

Token estimation includes:

Planner Call

* Planner system prompt
* User prompt
* Planner output

Executor Call

* Executor system prompt
* Planner output
* Executor output

LLM Calls: 2

### Planner–Executor–Reviewer

Token estimation includes:

Planner Call

* Planner system prompt
* User prompt
* Planner output

Executor Call

* Executor system prompt
* Planner output
* Executor output

Reviewer Call

* Reviewer prompt
* Executor output
* Reviewer output

LLM Calls: 3

## Cost Estimation

Estimated cost is calculated using:

estimated_input_tokens
estimated_output_tokens

and provider-specific public API pricing.

## Version History

### V1.4.2

Token estimation considered only final workflow outputs.

### V1.4.3

Token estimation includes all LLM calls and intermediate outputs across workflow stages.

This version is the official methodology for Study 002 provider comparison experiments.
