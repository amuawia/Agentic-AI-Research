# Study 002 Related Work References

## Purpose of This File

This document is a working reference inventory for the Study 002 manuscript. It supports the development of the Related Work section and is not itself part of the final manuscript.

The references are grouped according to the thematic structure defined in `related_work_sources.md`.

Before final submission, each entry should be checked for:

* DOI
* final venue
* publisher formatting
* BibTeX accuracy
* citation style required by the selected venue

---

# Core Citation Set Used in the Revised Related Work

The rewritten Related Work section emphasizes the following citation groups:

- Foundation-model evaluation and benchmarking: HELM, MMLU, BIG-bench, SWE-bench, AgentBench.
- Evaluation validity and judging: MT-Bench, Chatbot Arena, AlpacaEval / evaluator-debiasing work.
- Agentic systems and workflow architecture: autonomous-agent surveys, augmented language models, Toolformer, Generative Agents.
- Multi-stage reasoning and review: Chain-of-Thought, self-consistency, ReAct, Tree of Thoughts, Reflexion, Self-Refine, and critical self-correction surveys.
- Cross-provider context: GPT, Gemini, and Claude technical/model reports, interpreted cautiously as time-bounded background rather than ranking evidence.
- Operational efficiency: transformer inference efficiency, efficient LLM surveys, and compute/resource-cost literature.
- Study-specific continuity: Study 001 as the single-provider predecessor and Study 002 as the controlled cross-provider extension.

This citation set supports the paper's public-safe positioning as a controlled exploratory operational benchmark rather than a permanent provider ranking or definitive human-quality assessment.

---

# 1. Foundation Model Evaluation and Benchmarking

## REF01

Liang, P., Bommasani, R., Lee, T., Tsipras, D., Soylu, D., Yasunaga, M., Zhang, Y., Narayanan, D., Wu, Y., Kumar, A., et al. (2023).
**Holistic Evaluation of Language Models.**
Transactions on Machine Learning Research.

Use in Study 002:
Supports holistic, multi-metric evaluation of language models and the need for transparent benchmark design.

Status: Must cite.

---

## REF02

Hendrycks, D., Burns, C., Basart, S., Zou, A., Mazeika, M., Song, D., and Steinhardt, J. (2021).
**Measuring Massive Multitask Language Understanding.**
International Conference on Learning Representations.

Use in Study 002:
Supports multi-domain evaluation of knowledge and reasoning capabilities.

Status: Must cite.

---

## REF03

Srivastava, A., Rastogi, A., Rao, A., Shoeb, A. A. M., Abid, A., Fisch, A., Brown, A. R., Santoro, A., Gupta, A., Garriga-Alonso, A., et al. (2022).
**Beyond the Imitation Game: Quantifying and Extrapolating the Capabilities of Language Models.**
arXiv preprint arXiv:2206.04615.

Use in Study 002:
Supports broad benchmark construction across diverse language-model capabilities.

Status: Must cite.

---

## REF04

Jimenez, C. E., Yang, J., Wettig, A., Yao, S., Pei, K., Press, O., and Narasimhan, K. (2024).
**SWE-bench: Can Language Models Resolve Real-World GitHub Issues?**
International Conference on Learning Representations.

Use in Study 002:
Supports realistic coding-task evaluation and software-engineering benchmark design.

Status: Must cite.

---

## REF05

Zheng, L., Chiang, W.-L., Sheng, Y., Zhuang, S., Wu, Z., Zhuang, Y., Lin, Z., Li, Z., Li, D., Xing, E. P., Zhang, H., Gonzalez, J. E., and Stoica, I. (2023).
**Judging LLM-as-a-Judge with MT-Bench and Chatbot Arena.**
arXiv preprint arXiv:2306.05685.

Use in Study 002:
Supports scalable LLM evaluation using MT-Bench and LLM-as-judge methods, while also highlighting evaluation bias concerns.

Status: Must cite.

---

## REF06

Chiang, W.-L., Zheng, L., Sheng, Y., Angelopoulos, A. N., Li, T., Li, D., Zhang, H., Zhu, B., Jordan, M. I., Gonzalez, J. E., and Stoica, I. (2024).
**Chatbot Arena: An Open Platform for Evaluating LLMs by Human Preference.**
Proceedings of Machine Learning Research.

Use in Study 002:
Supports human-preference-based evaluation and comparative model ranking.

Status: Strongly recommended.

---

## REF07

Dubois, Y., Galambosi, B., Liang, P., and Hashimoto, T. B. (2024).
**Length-Controlled AlpacaEval: A Simple Way to Debias Automatic Evaluators.**
arXiv preprint arXiv:2404.04475.

Use in Study 002:
Supports discussion of automated evaluation limitations and evaluator bias.

Status: Recommended.

---

## REF08

Li, J., Wang, S., Zhang, M., Li, W., Lai, Y., Kang, X., Ma, W., and Liu, Y. (2024).
**AgentBoard: An Analytical Evaluation Board of Multi-turn LLM Agents.**
arXiv preprint.

Use in Study 002:
Supports agent evaluation beyond single-turn model benchmarking.

Status: Verify bibliographic details before final use.

---

## REF09

Liu, X., Yu, H., Zhang, H., Xu, Y., Lei, X., Lai, H., Gu, Y., Ding, H., Men, K., Yang, K., et al. (2024).
**AgentBench: Evaluating LLMs as Agents.**
International Conference on Learning Representations.

Use in Study 002:
Supports evaluation of LLMs as autonomous agents across multiple environments.

Status: Must cite.

---

# 2. Agentic AI and Workflow Architectures

## REF10

Wang, L., Ma, C., Feng, X., Zhang, Z., Yang, H., Zhang, J., Chen, Z., Tang, J., Chen, X., Lin, Y., Zhao, W. X., Wei, Z., and Wen, J.-R. (2024).
**A Survey on Large Language Model Based Autonomous Agents.**
Frontiers of Computer Science.

Use in Study 002:
Provides a broad foundation for LLM-based autonomous agent systems.

Status: Must cite.

---

## REF11

Xi, Z., Chen, W., Guo, X., He, W., Ding, Y., Hong, B., Zhang, M., Wang, J., Jin, S., Zhou, E., et al. (2023).
**The Rise and Potential of Large Language Model Based Agents: A Survey.**
arXiv preprint arXiv:2309.07864.

Use in Study 002:
Supports the emergence of LLM agents as a distinct research area.

Status: Strongly recommended.

---

## REF12

Yehudai, A., Eden, L., Li, A., Uziel, G., Zhao, Y., Bar-Haim, R., Cohan, A., and Shmueli-Scheuer, M. (2025).
**Survey on Evaluation of LLM-based Agents.**
arXiv preprint arXiv:2503.16416.

Use in Study 002:
Supports agent-evaluation challenges and the need for systematic evaluation methods.

Status: Strongly recommended.

---

## REF13

Luo, J., Zhang, W., Yuan, Y., Zhao, Y., Yang, J., Gu, Y., Wu, B., Chen, B., Qiao, Z., Long, Q., et al. (2025).
**Large Language Model Agent: A Survey on Methodology, Applications and Challenges.**
arXiv preprint arXiv:2503.21460.

Use in Study 002:
Supports methodology-centered taxonomies of LLM agents.

Status: Recommended.

---

## REF14

Mialon, G., Dessì, R., Lomeli, M., Nalmpantis, C., Pasunuru, R., Raileanu, R., Rozière, B., Schick, T., Dwivedi-Yu, J., Celikyilmaz, A., Grave, E., LeCun, Y., and Scialom, T. (2023).
**Augmented Language Models: A Survey.**
Transactions on Machine Learning Research.

Use in Study 002:
Supports the concept of augmenting language models with reasoning, tools, and external modules.

Status: Must cite.

---

## REF15

Schick, T., Dwivedi-Yu, J., Dessì, R., Raileanu, R., Lomeli, M., Hambro, E., Zettlemoyer, L., Cancedda, N., and Scialom, T. (2023).
**Toolformer: Language Models Can Teach Themselves to Use Tools.**
Advances in Neural Information Processing Systems.

Use in Study 002:
Supports tool-use and external-action paradigms in LLM systems.

Status: Recommended.

---

## REF16

Park, J. S., O'Brien, J. C., Cai, C. J., Morris, M. R., Liang, P., and Bernstein, M. S. (2023).
**Generative Agents: Interactive Simulacra of Human Behavior.**
ACM Symposium on User Interface Software and Technology.

Use in Study 002:
Supports agent architectures incorporating memory, reflection, and planning.

Status: Recommended.

---

# 3. Multi-Stage Reasoning, Reflection, and Review

## REF17

Wei, J., Wang, X., Schuurmans, D., Bosma, M., Ichter, B., Xia, F., Chi, E., Le, Q. V., and Zhou, D. (2022).
**Chain-of-Thought Prompting Elicits Reasoning in Large Language Models.**
Advances in Neural Information Processing Systems.

Use in Study 002:
Supports structured intermediate reasoning as a mechanism for improving complex-task performance.

Status: Must cite.

---

## REF18

Wang, X., Wei, J., Schuurmans, D., Le, Q. V., Chi, E. H., Narang, S., Chowdhery, A., and Zhou, D. (2023).
**Self-Consistency Improves Chain of Thought Reasoning in Language Models.**
International Conference on Learning Representations.

Use in Study 002:
Supports reasoning-path diversity and self-consistency as performance-enhancing mechanisms.

Status: Strongly recommended.

---

## REF19

Yao, S., Zhao, J., Yu, D., Du, N., Shafran, I., Narasimhan, K., and Cao, Y. (2023).
**ReAct: Synergizing Reasoning and Acting in Language Models.**
International Conference on Learning Representations.

Use in Study 002:
Supports combined reasoning-action workflows.

Status: Must cite.

---

## REF20

Shinn, N., Cassano, F., Berman, E., Gopinath, A., Narasimhan, K., and Yao, S. (2023).
**Reflexion: Language Agents with Verbal Reinforcement Learning.**
Advances in Neural Information Processing Systems.

Use in Study 002:
Supports reflection and feedback-based improvement in language agents.

Status: Must cite.

---

## REF21

Yao, S., Yu, D., Zhao, J., Shafran, I., Griffiths, T. L., Cao, Y., and Narasimhan, K. (2023).
**Tree of Thoughts: Deliberate Problem Solving with Large Language Models.**
arXiv preprint arXiv:2305.10601.

Use in Study 002:
Supports deliberate multi-path reasoning and self-evaluation.

Status: Must cite.

---

## REF22

Madaan, A., Tandon, N., Gupta, P., Hallinan, S., Gao, L., Wiegreffe, S., Alon, U., Dziri, N., Prabhumoye, S., Yang, Y., et al. (2023).
**Self-Refine: Iterative Refinement with Self-Feedback.**
Advances in Neural Information Processing Systems.

Use in Study 002:
Supports reviewer-style refinement and iterative output improvement.

Status: Must cite.

---

## REF23

Du, Y., Li, S., Torralba, A., Tenenbaum, J. B., and Mordatch, I. (2024).
**Improving Factuality and Reasoning in Language Models through Multiagent Debate.**
International Conference on Machine Learning.

Use in Study 002:
Supports multi-agent interaction as a mechanism for improving reasoning and factuality.

Status: Recommended.

---

## REF24

Kamoi, R., Goyal, T., Rodriguez, J. D., Durrett, G., and Doddapaneni, S. (2024).
**When Can LLMs Actually Correct Their Own Mistakes? A Critical Survey of Self-Correction of LLMs.**
Transactions of the Association for Computational Linguistics.

Use in Study 002:
Supports cautious interpretation of reviewer and self-correction mechanisms.

Status: Strongly recommended.

---

## REF25

Renze, M., and Guven, E. (2024).
**Self-Reflection in LLM Agents: Effects on Problem-Solving Performance.**
arXiv preprint arXiv:2405.06682.

Use in Study 002:
Supports analysis of self-reflection and problem-solving improvements across models.

Status: Recommended.

---

# 4. Multi-Agent Frameworks and Agent Environments

## REF26

Wu, Q., Bansal, G., Zhang, J., Wu, Y., Li, B., Zhu, E., Jiang, L., Zhang, X., Zhang, S., Liu, J., Awadallah, A. H., White, R. W., Burger, D., and Wang, C. (2023).
**AutoGen: Enabling Next-Gen LLM Applications via Multi-Agent Conversation.**
arXiv preprint arXiv:2308.08155.

Use in Study 002:
Supports multi-agent orchestration and workflow-driven LLM applications.

Status: Must cite.

---

## REF27

Zhou, S., Xu, F., Zhu, H., Zhou, X., Lo, R., Sridhar, A., Cheng, X., Ou, T., Bisk, Y., Fried, D., Alon, U., and Neubig, G. (2024).
**WebArena: A Realistic Web Environment for Building Autonomous Agents.**
International Conference on Learning Representations.

Use in Study 002:
Supports realistic environment-based evaluation of autonomous agents.

Status: Strongly recommended.

---

## REF28

Xie, T., Zhang, D., Chen, J., Li, X., Zhao, S., Cao, R., Hua, T. J., Cheng, Z., Shin, D., Lei, F., Liu, Y., Xu, Y., Zhou, S., Savarese, S., Xiong, C., Zhong, V., and Yu, T. (2024).
**OSWorld: Benchmarking Multimodal Agents for Open-Ended Tasks in Real Computer Environments.**
Advances in Neural Information Processing Systems.

Use in Study 002:
Supports realistic agent evaluation in computer-use environments.

Status: Recommended.

---

## REF29

Yang, J., Jimenez, C. E., Wettig, A., Lieret, K., Yao, S., Narasimhan, K., and Press, O. (2024).
**SWE-agent: Agent-Computer Interfaces Enable Automated Software Engineering.**
Advances in Neural Information Processing Systems.

Use in Study 002:
Supports agent-interface design and automated software-engineering evaluation.

Status: Recommended.

---

# 5. Cross-Provider and Comparative Model Evaluation

## REF30

OpenAI. (2023).
**GPT-4 Technical Report.**
arXiv preprint arXiv:2303.08774.

Use in Study 002:
Provides context for OpenAI foundation-model capabilities and evaluation reporting.

Status: Recommended background.

---

## REF31

Anil, R., Dai, A. M., Firat, O., Johnson, M., Lepikhin, D., Passos, A., Shakeri, S., Taropa, E., Bailey, P., Chen, Z., et al. (2023).
**PaLM 2 Technical Report.**
arXiv preprint arXiv:2305.10403.

Use in Study 002:
Provides context for Google foundation-model development and evaluation practices.

Status: Recommended background.

---

## REF32

Team Gemini, Google. (2023).
**Gemini: A Family of Highly Capable Multimodal Models.**
arXiv preprint arXiv:2312.11805.

Use in Study 002:
Provides context for Gemini model-family capabilities.

Status: Recommended background.

---

## REF33

Anthropic. (2024).
**The Claude 3 Model Family: Opus, Sonnet, Haiku.**
Technical report / model card.

Use in Study 002:
Provides context for Anthropic model-family design and evaluation.

Status: Verify final source format before use.

---

## REF34

Dubois, Y., Li, X., Taori, R., Zhang, T., Gulrajani, I., Ba, J., Guestrin, C., Liang, P., and Hashimoto, T. B. (2023).
**AlpacaFarm: A Simulation Framework for Methods that Learn from Human Feedback.**
Advances in Neural Information Processing Systems.

Use in Study 002:
Supports model comparison and preference-based evaluation methods.

Status: Recommended.

---

## REF35

Bubeck, S., Chandrasekaran, V., Eldan, R., Gehrke, J., Horvitz, E., Kamar, E., Lee, P., Lee, Y. T., Li, Y., Lundberg, S., et al. (2023).
**Sparks of Artificial General Intelligence: Early Experiments with GPT-4.**
arXiv preprint arXiv:2303.12712.

Use in Study 002:
Provides early evaluation context for advanced foundation-model capabilities.

Status: Optional; use cautiously because it is model-specific and interpretive.

---

# 6. Operational Trade-Offs, Efficiency, and Deployment Considerations

## REF36

Patterson, D., Gonzalez, J., Le, Q., Liang, C., Munguia, L.-M., Rothchild, D., So, D., Texier, M., and Dean, J. (2021).
**Carbon Emissions and Large Neural Network Training.**
arXiv preprint arXiv:2104.10350.

Use in Study 002:
Supports broader discussion of computational cost and environmental considerations.

Status: Optional.

---

## REF37

Strubell, E., Ganesh, A., and McCallum, A. (2019).
**Energy and Policy Considerations for Deep Learning in NLP.**
Association for Computational Linguistics.

Use in Study 002:
Supports cost and resource-efficiency discussion.

Status: Optional foundational reference.

---

## REF38

Pope, R., Douglas, S., Chowdhery, A., Devlin, J., Bradbury, J., Heek, J., Xiao, K., Agrawal, S., and Dean, J. (2023).
**Efficiently Scaling Transformer Inference.**
Proceedings of Machine Learning and Systems.

Use in Study 002:
Supports inference efficiency and operational performance considerations.

Status: Recommended.

---

## REF39

Xu, L., Xie, H., Qin, S.-Z. J., Tao, X., and Wang, F. L. (2024).
**Parameter-Efficient Fine-Tuning Methods for Pretrained Language Models: A Critical Review and Assessment.**
arXiv / survey source.

Use in Study 002:
Optional context for resource-efficient adaptation, although not directly about workflows.

Status: Optional; verify venue before final use.

---

## REF40

Wan, Z., Wang, X., Liu, C., Alam, S., Zheng, Y., Liu, J., Qu, Z., Yan, S., Zhu, Y., Zhang, Q., Chowdhury, M., and Zhang, M. (2023).
**Efficient Large Language Models: A Survey.**
arXiv preprint.

Use in Study 002:
Supports discussion of LLM efficiency and resource-aware deployment.

Status: Recommended; verify final venue before final use.

---

# 7. Study-Specific and Prior Work

## REF41

Ali, M. (2026).
**Evaluating Multi-Agent Workflow Architectures for Enterprise AI Tasks: A Comparative Study Using Gemini and n8n.**
Zenodo. DOI: 10.5281/zenodo.20606084.

Use in Study 002:
Primary prior work. Establishes Study 001 and motivates Study 002 as a controlled cross-provider extension.

Status: Must cite.

---

## REF42

Ali, M. (2026).
**Agentic-AI-Research Repository.**
GitHub repository.

Use in Study 002:
Supports reproducibility package, datasets, scripts, workflow versions, and research traceability.

Status: Cite in reproducibility section if journal permits software/repository citations.

---

# Summary by Theme

| Theme                                           | References |
| ----------------------------------------------- | ---------: |
| Foundation Model Evaluation and Benchmarking    |          9 |
| Agentic AI and Workflow Architectures           |          7 |
| Multi-Stage Reasoning, Reflection, and Review   |          9 |
| Multi-Agent Frameworks and Agent Environments   |          4 |
| Cross-Provider and Comparative Model Evaluation |          6 |
| Operational Trade-Offs and Efficiency           |          5 |
| Study-Specific Prior Work                       |          2 |
| Total                                           |         42 |

---

# Notes for Final Manuscript

1. Use approximately 30–40 of these references in the final Related Work section.
2. Keep 40–50 total references in the full manuscript after adding methodology/statistics references.
3. Verify all BibTeX entries before submission.
4. Prefer peer-reviewed versions when available.
5. Use arXiv versions only when no formal venue version exists or when the work is widely recognized and highly relevant.
6. Avoid overloading the Related Work section with provider technical reports unless they directly support model-context statements.
7. Study 001 should be cited explicitly when positioning Study 002 as a controlled cross-provider extension.
