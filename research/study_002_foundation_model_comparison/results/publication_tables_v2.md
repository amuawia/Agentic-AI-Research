# Study 002 Publication Tables v2

Public-safe generated tables for manuscript drafting. `quality_score` is interpreted as an operational workflow-generated quality proxy, not an independent human judgment.

## Table 1. Provider × workflow descriptive summary

- OpenAI / basic_agent: N=30; mean quality=0.940; SD=0.030; mean cost=$0.0055; duration=8.333s; tokens=448.0
- OpenAI / planner_executor: N=30; mean quality=0.939; SD=0.026; mean cost=$0.0107; duration=15.047s; tokens=1047.0
- OpenAI / planner_executor_reviewer: N=30; mean quality=0.895; SD=0.031; mean cost=$0.0206; duration=26.613s; tokens=2265.3
- Google / basic_agent: N=30; mean quality=0.903; SD=0.246; mean cost=$0.0027; duration=11.560s; tokens=360.6
- Google / planner_executor: N=30; mean quality=0.993; SD=0.022; mean cost=$0.0072; duration=22.547s; tokens=1085.4
- Google / planner_executor_reviewer: N=30; mean quality=0.732; SD=0.314; mean cost=$0.0144; duration=47.280s; tokens=2434.4
- Anthropic / basic_agent: N=30; mean quality=0.874; SD=0.170; mean cost=$0.0065; duration=9.897s; tokens=510.7
- Anthropic / planner_executor: N=30; mean quality=0.901; SD=0.102; mean cost=$0.0109; duration=15.613s; tokens=1045.5
- Anthropic / planner_executor_reviewer: N=30; mean quality=0.841; SD=0.132; mean cost=$0.0210; duration=25.620s; tokens=2262.8

## Table 2. Task-category summary

- Knowledge: N=90; mean quality=0.919; SD=0.092; mean confidence=0.943
- Reasoning: N=90; mean quality=0.900; SD=0.145; mean confidence=0.941
- Coding: N=90; mean quality=0.853; SD=0.233; mean confidence=0.907

## Table 3. Difficulty-annotation summary

Difficulty was a secondary annotation layer and was not the primary task-bank balancing criterion.

- easy: N=63; mean quality=0.884; SD=0.207; mean confidence=0.937
- medium: N=99; mean quality=0.900; SD=0.141; mean confidence=0.933
- hard: N=108; mean quality=0.886; SD=0.169; mean confidence=0.924

## Table 4. Top 10 operational-efficiency configurations

- 1. Google / gemini-2.5-pro / basic_agent: balanced efficiency index=0.805; mean quality=0.903; mean cost=$0.0027
- 2. OpenAI / GPT-5.5 / basic_agent: balanced efficiency index=0.669; mean quality=0.940; mean cost=$0.0055
- 3. Anthropic / Claude Sonnet 4.6 / basic_agent: balanced efficiency index=0.531; mean quality=0.874; mean cost=$0.0065
- 4. Google / gemini-2.5-pro / planner_executor: balanced efficiency index=0.360; mean quality=0.993; mean cost=$0.0072
- 5. OpenAI / GPT-5.5 / planner_executor: balanced efficiency index=0.329; mean quality=0.939; mean cost=$0.0107
- 6. Anthropic / Claude Sonnet 4.6 / planner_executor: balanced efficiency index=0.310; mean quality=0.901; mean cost=$0.0109
- 7. OpenAI / GPT-5.5 / planner_executor_reviewer: balanced efficiency index=0.159; mean quality=0.895; mean cost=$0.0206
- 8. Anthropic / Claude Sonnet 4.6 / planner_executor_reviewer: balanced efficiency index=0.149; mean quality=0.841; mean cost=$0.0210
- 9. Google / gemini-2.5-pro / planner_executor_reviewer: balanced efficiency index=0.125; mean quality=0.732; mean cost=$0.0144
