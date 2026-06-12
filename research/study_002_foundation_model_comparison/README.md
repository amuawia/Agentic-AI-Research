# Study 002: Foundation Model Comparison

## Overview

This study extends the findings of Study 001 by evaluating multi-agent AI workflow architectures across multiple foundation model providers.

The goal is to assess how workflow design and model selection influence answer quality, confidence, execution cost, latency, and overall effectiveness across enterprise AI tasks.

## Research Objective

To compare the performance of three workflow architectures across multiple foundation model providers using a consistent experimental design.

### Workflow Architectures

* Basic Agent
* Planner–Executor
* Planner–Executor–Reviewer

### Foundation Model Providers

* OpenAI
* Google Gemini
* Anthropic Claude

## Research Questions

### RQ1

How does workflow architecture affect task performance?

### RQ2

How do different foundation model providers perform under identical workflow architectures?

### RQ3

What are the trade-offs between quality, confidence, latency, token consumption, and cost?

### RQ4

Does the Planner–Executor–Reviewer architecture consistently improve answer quality compared to simpler architectures?

## Experimental Design

### Tasks

The study uses a fixed task bank covering:

* Knowledge Tasks
* Reasoning Tasks
* Coding Tasks

### Difficulty Levels

* Easy
* Medium
* Hard

### Evaluation Metrics

* Quality Score
* Confidence Score
* Execution Duration
* Token Consumption
* Estimated Cost
* Workflow Complexity

## Repository Structure

```text
datasets/
workflows/
analysis/
figures/
results/
manuscript/
```

## Status

In Progress

## Planned Publication

Peer-reviewed journal or conference submission.

## Related Study

Study 001:

Evaluating Multi-Agent Workflow Architectures for Enterprise AI Tasks: A Comparative Study Using Gemini and n8n

DOI: 10.5281/zenodo.20606084
