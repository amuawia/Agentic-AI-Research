# Datasets

This directory contains all datasets used and generated during Study 002.

## Structure

```text
datasets/
├── README.md
├── task_bank/
├── pilot/
├── openai/
├── gemini/
├── claude/
└── merged/
```

## task_bank

Contains the official task set used throughout the study.

Example:

```text
task_bank_v1.csv
```

The same task bank must be used for all providers and workflow architectures.

---

## pilot

Contains pilot and validation runs performed before official data collection.

Pilot data is not included in the final statistical analysis.

Example:

```text
Agentic_AI_Experiments_Pilot_OpenAI_V1.4.2.xlsx
```

---

## openai

Contains official OpenAI experimental results.

Expected content:

```text
Agentic_AI_Experiments_OpenAI_V1.0.xlsx
```

---

## gemini

Contains official Google Gemini experimental results.

Expected content:

```text
Agentic_AI_Experiments_Gemini_V1.0.xlsx
```

---

## claude

Contains official Anthropic Claude experimental results.

Expected content:

```text
Agentic_AI_Experiments_Claude_V1.0.xlsx
```

---

## merged

Contains merged datasets used for cross-provider analysis.

Expected content:

```text
Agentic_AI_Experiments_Master_V1.0.xlsx
```

---

## Data Collection Rules

1. Use identical tasks across all providers.
2. Use identical workflow architectures.
3. Maintain consistent prompts whenever possible.
4. Record all experimental metrics.
5. Preserve raw outputs for reproducibility.

## Reproducibility

All datasets should remain versioned and traceable to the workflows used to generate them.
