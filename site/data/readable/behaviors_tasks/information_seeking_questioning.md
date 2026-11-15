# Information-seeking questioning
**Type:** Behavioral indicator  
**Supporting papers:** 17  
**Also known as:** Symptom inquiry, Question asking, Follow-up question generation, Open-ended question asking, Open-ended questioning, Question selection, Seeking information  

## State of the Field

**Space of definitions.** Across papers, the prevailing usage treats this behavior as asking follow-up, clarifying, or probing questions when the initial context is incomplete. Most definitions describe generating questions to elicit missing symptoms, history, diagnostic details, user parameters, or other information needed before making a diagnosis, giving an answer, or proceeding with an action. A common clinical framing describes it as selective or sequential inquiry to accumulate evidence, while a smaller line of work frames it more generally as asking questions to reduce uncertainty or improve confidence in a decision.

**Variants.** Papers study several variants of this behavior. The most common are clinical follow-up questioning and symptom inquiry, where a model probes for additional patient information; other work studies open-ended questioning that seeks descriptive answers rather than yes or no replies, question asking in interactive tasks such as hidden-object or city-guessing games, question selection from a candidate set as the next informative query, and clarification or confirmation seeking before tool use or action. Across these variants, the shared element is eliciting additional information from an interlocutor or latent target.

**Space of elicitation and scores.** No measurement instrument is linked to this behavior in the papers.

**What it is taken as evidence of.** No construct is linked to this behavior in the papers.

## Sources

**Symptom inquiry** (1 paper: [DDO: Dual-Decision Optimization for LLM-Based Medical Consultation via Multi-Agent Collaboration](https://aclanthology.org/2025.emnlp-main.1340.pdf))
> Engaging in a sequential decision-making process to selectively ask about additional symptoms to accumulate diagnostic evidence.

**Information-seeking questioning** (1 paper: [3MDBench: Medical Multimodal Multi-agent Dialogue Benchmark](https://aclanthology.org/2025.emnlp-main.1353.pdf))
> Asking follow-up questions to elicit missing symptoms, history, or other diagnostic details from the patient.

**Question asking** (2 papers: [MediQ: Question-Asking LLMs and a Benchmark for Reliable Interactive Clinical Reasoning](https://proceedings.neurips.cc/paper_files/paper/2024/file/32b80425554e081204e5988ab1c97e9a-Paper-Conference.pdf), [LMRL Gym: Benchmarks for Multi-Turn Reinforcement Learning with Language Models](https://raw.githubusercontent.com/mlresearch/v267/main/assets/abdulhai25a/abdulhai25a.pdf))
> Generating follow-up inquiries to gather additional patient information when initial context is insufficient.

**Follow-up question generation** (2 papers: [BIRD: A Trustworthy Bayesian Inference Framework for Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/19452e14fe6e0a8ac00410f1eebcbded-Paper-Conference.pdf), [Position: Uncertainty Quantification Needs Reassessment for Large Language Model Agents](https://raw.githubusercontent.com/mlresearch/v267/main/assets/kirchhof25b/kirchhof25b.pdf))
> The observable act of generating questions to acquire additional information needed to improve confidence in a decision.

**Open-ended question asking** (1 paper: [GuessingGame: Measuring the Informativeness of Open-Ended Questions in Large Language Models](https://aclanthology.org/2025.emnlp-main.876.pdf))
> Posing free-form questions that elicit descriptive answers, rather than binary yes/no responses, to gather richer information about a hidden object.

**Open-ended questioning** (1 paper: [Position: Medical Large Language Model Benchmarks Should Prioritize Construct Validity](https://raw.githubusercontent.com/mlresearch/v267/main/assets/alaa25a/alaa25a.pdf))
> The behavior of asking questions that encourage detailed, narrative responses rather than simple yes/no answers.

**Question selection** (1 paper: [Adaptive Elicitation of Latent Information Using Natural Language](https://raw.githubusercontent.com/mlresearch/v267/main/assets/wang25ff/wang25ff.pdf))
> The observable act of choosing a natural language question from a candidate set to ask next, based on prior interactions with a latent entity.

**Seeking information** (1 paper: [CONFETTI: Conversational Function-Calling Evaluation Through Turn-Level Interactions](https://aclanthology.org/2025.acl-long.394.pdf))
> Producing responses that ask the user for clarification, missing parameters, or confirmation before proceeding with an action.
