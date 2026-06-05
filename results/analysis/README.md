# Analysis Dataset

This folder contains the cleaned analysis files for the main_001 experiment.

## Files

### main_001_checkpoint_90runs.csv
Raw exported experiment results after completing all main_001 runs.

Contains:
- 9 pilot runs
- 90 main_001 runs
- Total: 99 runs

### tasks.csv
Final research task list used in the experiment.

Contains:
- 30 tasks
- Categories: Knowledge, Reasoning, Coding
- Difficulty levels: easy, medium, hard

### main_001_analysis_dataset.xlsx
Cleaned dataset prepared for analysis.

Processing steps:
1. Removed pilot_001 rows.
2. Kept only main_001 rows.
3. Matched each run to the task list using the prompt text.
4. Added task metadata:
   - real_task_id
   - category
   - difficulty
   - expected_output

Expected final size:
- 90 rows
- 30 tasks
- 3 workflows per task

## Notes

The original task_id column in the raw results should not be used for analysis because it was fixed as 1 during workflow execution. Use real_task_id from the merged task metadata instead.