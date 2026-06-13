# Scoring Rubric

## Purpose

This rubric defines the evaluation methodology used to assess task outputs generated during Study 002.

The rubric is applied consistently across all providers and workflow architectures.

---

# Quality Score

Quality Score measures the overall usefulness and correctness of the generated response.

Range:

0.0 to 1.0

---

## Evaluation Criteria

### 1. Accuracy

The factual correctness of the response.

Questions:

* Is the information correct?
* Are there factual errors?
* Are calculations correct?

---

### 2. Completeness

The extent to which the response addresses the task requirements.

Questions:

* Were all requirements addressed?
* Were important elements omitted?

---

### 3. Reasoning Quality

The quality of analysis and logical thinking.

Questions:

* Is the reasoning coherent?
* Are conclusions supported?

---

### 4. Clarity

The readability and structure of the response.

Questions:

* Is the response understandable?
* Is the structure logical?

---

# Quality Score Scale

| Score | Interpretation                                                            |
| ----- | ------------------------------------------------------------------------- |
| 1.0   | Excellent. Fully correct, complete, well-reasoned, and clearly presented. |
| 0.9   | Very strong response with only minor weaknesses.                          |
| 0.8   | Good response with limited issues.                                        |
| 0.7   | Generally acceptable but contains noticeable weaknesses.                  |
| 0.6   | Partially successful response. Significant improvements needed.           |
| 0.5   | Mixed quality. Major limitations present.                                 |
| 0.4   | Weak response with substantial issues.                                    |
| 0.3   | Poor response. Limited usefulness.                                        |
| 0.2   | Mostly incorrect or incomplete.                                           |
| 0.1   | Extremely poor response.                                                  |
| 0.0   | Failed response or unusable output.                                       |

---

# Confidence Score

Confidence Score represents the model's self-reported confidence.

Range:

0.0 to 1.0

Confidence is not treated as a direct measure of answer quality.

Confidence is analyzed separately from Quality Score.

---

# Evaluation Procedure

## Step 1

Review the original task.

## Step 2

Review the generated answer.

## Step 3

Evaluate:

* Accuracy
* Completeness
* Reasoning Quality
* Clarity

## Step 4

Assign a Quality Score between 0.0 and 1.0.

## Step 5

Record the model-reported Confidence Score.

---

# Missing or Invalid Outputs

If output parsing fails:

Quality Score:

0.0

Confidence Score:

0.0

API Status:

Failure

---

# Reviewer Consistency

The same evaluation criteria must be applied throughout the entire study.

The scoring rubric must not be modified after official data collection begins.

Any future changes require a new rubric version.

---

# Version Control

Current Version:

Rubric V1.0

Status:

Frozen for Study 002

Effective Workflow Version:

V1.4.3
