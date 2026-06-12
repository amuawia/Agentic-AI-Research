Source for Prompt (User Message)
Define below
Prompt (User Message)
{{ $('When chat message received').item.json.chatInput }}
 
Require Specific Output Format

Enable Fallback Model

Options
System Message
You are an AI assistant.

Return ONLY valid JSON.

Keep the answer concise and structured.
Do not exceed 250 words.
The "answer" field must be a plain text string, not an object or array.

{
  "task_id": "1",
  "answer": "...",
  "execution_summary": "...",
  "confidence": 0.0
}
