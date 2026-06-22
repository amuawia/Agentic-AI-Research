# Study 002 Task-Blocked Robustness Analysis

This public-safe summary reports a task-blocked fixed-effect robustness analysis. Because each of the 30 benchmark tasks was executed under every provider × workflow condition, task identity was included as a blocking factor.

Model form: `outcome ~ task block + provider + workflow + provider × workflow`.

`quality_score` remains an operational workflow-generated proxy rather than an independent human judgment.

## Task-blocked tests

- quality_score / provider_main_given_workflow_task: F(2, 236) = 3.496, p = 0.032, partial eta squared = 0.029
- quality_score / workflow_main_given_provider_task: F(2, 236) = 15.727, p = <0.001, partial eta squared = 0.118
- quality_score / provider_workflow_interaction_given_task_main_effects: F(4, 232) = 5.522, p = <0.001, partial eta squared = 0.087
- confidence / provider_main_given_workflow_task: F(2, 236) = 13.256, p = <0.001, partial eta squared = 0.101
- confidence / workflow_main_given_provider_task: F(2, 236) = 3.935, p = 0.021, partial eta squared = 0.032
- confidence / provider_workflow_interaction_given_task_main_effects: F(4, 232) = 2.242, p = 0.065, partial eta squared = 0.037

## Interpretation

The task-blocked analysis preserves the main Study 002 conclusion that provider and workflow should be evaluated jointly. It also reinforces the need for cautious wording: effects on `quality_score` are effects on an operational proxy whose construction differs between reviewer and non-reviewer workflows.

## Output files

- `analysis/statistical_outputs/task_blocked_analysis.xlsx`
- `results/task_blocked_analysis_summary.md`
