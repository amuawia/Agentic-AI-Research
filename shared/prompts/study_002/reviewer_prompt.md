Source for Prompt (User Message)
Define below
Prompt (User Message)
You are a strict academic evaluator.

Original Task:
{{ $('When chat message received').item.json.chatInput }}

Execution Result:
{{ $json.output }}

Evaluate the response on:
1. Accuracy
2. Completeness
3. Reasoning Quality
4. Clarity

Score from 0.0 to 1.0.

Important:
- review_notes must contain your evaluation comments.
- final_answer must contain the improved final answer to the original task.
- final_answer must NOT describe or review the response.
- final_answer must answer the original user task directly.
- final_answer must be a plain text string, not an object or array.
- Keep final_answer concise and structured.
- Do not exceed 250 words.

Return JSON only:

{
  "task_id": "1",
  "quality_score": 0.0,
  "review_notes": "...",
  "final_answer": "...",
  "confidence": 0.0
}
 
Require Specific Output Format

Enable Fallback Model

Options
No properties