# Privacy leakage
**Type:** Behavioral indicator  
**Supporting papers:** 22  
**Also known as:** Sensitive information exposure, System prompt extraction, Fragment inference, Data stealing, Sensitive information leakage, Image-text pair leakage, Good faith disclosure, PII leakage, Information leakage, Training data extraction, PII extraction, Specific PII leakage, Full request leakage, Semantic sensitive information generation, Private information leakage, Prompt extraction, System prompt leakage  

## State of the Field

**Space of definitions.** Across papers, the prevailing usage treats privacy leakage as observable disclosure or reproduction of sensitive, private, confidential, or personally identifiable information in model outputs. Most formulations count leakage when the model reveals material that should have been withheld, including memorized training examples, PII, confidential system instructions, or contextually prohibited information, often after adversarial prompts or prompt injection, though some papers also study disclosure under simple natural questions or a "good faith" assumption that data may be shared because someone asked. Definitions differ mainly in what is leaked and where it appears, ranging from inferred training fragments and prompt or access-code disclosure to summaries, reasoning traces, final answers, full user requests, and paired image-text outputs.

**Variants.** Papers examine several settings for this behavior. Recurring variants include extraction of memorized training examples or PII, prompt or system-prompt leakage, agent attacks that steal emails, payment methods, specific PII fields, or full user requests, leakage in reasoning traces as well as final answers, and multimodal exposure of paired images and text. Other formulations include fragment-level inference from a few known public fragments, PII carried into summaries, security-policy violations in question answering, and sensitive information generation from simple natural questions; related work also connects agent-side leakage to action grounding and leakage from reasoning models to chain of thought.

**Space of elicitation and scores.** Papers measure this behavior with 5 instruments. The most recurrent is Membership inference attack, used to evaluate or audit privacy leakage through membership leakage of a canary dataset; papers also use DecodingTrust, InjecAgent, MUSE, and Mind2Web, spanning an Enron email extraction privacy dataset, an agent red-teaming framework that tests data stealing attacks, a machine unlearning benchmark that includes "no privacy leakage," and realistic website action steps involving diverse PII categories.

**What it is taken as evidence of.** Across construct links, papers attach this behavior to 2 constructs, most often Memorization and also Privacy preservation. Several papers claim a causal relationship from Memorization to Privacy leakage, citing verbatim training-data memorization and stating that "memorized private information is vulnerable to data extraction"; a separate paper reports that Privacy leakage is related to Privacy preservation by evaluating privacy "in terms of awareness and leakage." These construct links are not framed the same way, since one is causal and the other is recorded as related.

## Sources

**Fragment inference** (1 paper: [Fragments to Facts: Partial-Information Fragment Inference from LLMs](https://raw.githubusercontent.com/mlresearch/v267/main/assets/rosenblatt25a/rosenblatt25a.pdf))
> The observable act of using a small set of known text fragments from a training sample to infer additional, unknown fragments from the same sample by querying a model.

**System prompt extraction** (1 paper: [The Illusion of Role Separation: Hidden Shortcuts in LLM Role Learning (and How to Fix Them)](https://raw.githubusercontent.com/mlresearch/v267/main/assets/wang25ap/wang25ap.pdf))
> An observable attack behavior where the model is manipulated into revealing its confidential system instructions or prompts.

**Sensitive information exposure** (1 paper: [AdvAgent: Controllable Blackbox Red-teaming on Web Agents](https://raw.githubusercontent.com/mlresearch/v267/main/assets/xu25m/xu25m.pdf))
> Revealing sensitive information as a result of malicious prompt injection or adversarial manipulation.

**Data stealing** (1 paper: [UDora: A Unified Red Teaming Framework against LLM Agents by Dynamically Hijacking Their Own Reasoning](https://raw.githubusercontent.com/mlresearch/v267/main/assets/zhang25cl/zhang25cl.pdf))
> The malicious act of accessing and exfiltrating sensitive or private information, such as emails or payment methods.

**Sensitive information leakage** (1 paper: [Reasoning Model Unlearning: Forgetting Traces, Not Just Answers, While Preserving Reasoning Skills](https://aclanthology.org/2025.emnlp-main.220.pdf))
> The unintended disclosure of hazardous or private knowledge in either final answers or reasoning traces, despite unlearning attempts.

**Privacy leakage** (1 paper: [Interpretation Meets Safety: A Survey on Interpretation Methods and Tools for Improving LLM Safety](https://aclanthology.org/2025.emnlp-main.1091.pdf))
> The observable reproduction of sensitive or personally identifiable information from training data in model outputs.

**Image-text pair leakage** (1 paper: [Beyond Text: Unveiling Privacy Vulnerabilities in Multi-modal Retrieval-Augmented Generation](https://aclanthology.org/2025.emnlp-main.1259.pdf))
> The simultaneous exposure of both a private image and its associated text (e.g., a medical image with its diagnostic caption) from a database.

**Good faith disclosure** (1 paper: [Leaky Thoughts: Large Reasoning Models Are Not Private Thinkers](https://aclanthology.org/2025.emnlp-main.1347.pdf))
> An observable behavior where a model discloses private information under the naive assumption that any request for data is trustworthy and made in good faith.

**PII leakage** (1 paper: [How Private are Language Models in Abstractive Summarization?](https://aclanthology.org/2025.emnlp-main.1531.pdf))
> The observable phenomenon where a model includes personally identifiable information from the source document—such as names, ages, locations, or gender—in its generated summary.

**Information leakage** (1 paper: [Keep Security! Benchmarking Security Policy Preservation in Large Language Model Contexts Against Indirect Attacks in Question Answering](https://aclanthology.org/2025.emnlp-main.345.pdf))
> The observable output behavior in which an LLM discloses confidential information that is explicitly prohibited by a user-defined security policy in the context.

**Training data extraction** (1 paper: [Retracing the Past: LLMs Emit Training Data When They Get Lost](https://aclanthology.org/2025.emnlp-main.1789.pdf))
> The model reveals memorized training examples in response to adversarial prompts.

**PII extraction** (1 paper: [Proactive Privacy Amnesia for Large Language Models: Safeguarding PII with Negligible Impact on Model Utility](https://proceedings.iclr.cc/paper_files/paper/2025/file/8c234d9c7e738a793947e0282c36eb95-Paper-Conference.pdf))
> The observable act of a model generating personally identifiable information, such as phone numbers or physical addresses, in response to prompts.

**Specific PII leakage** (1 paper: [EIA: ENVIRONMENTAL INJECTION ATTACK ON GENERALIST WEB AGENTS FOR PRIVACY LEAKAGE](https://proceedings.iclr.cc/paper_files/paper/2025/file/a73474c359ed523e6cd3174ed29a4d56-Paper-Conference.pdf))
> Causing the agent to enter a user’s specific sensitive field value into an injected malicious element instead of the intended target field.

**Full request leakage** (1 paper: [EIA: ENVIRONMENTAL INJECTION ATTACK ON GENERALIST WEB AGENTS FOR PRIVACY LEAKAGE](https://proceedings.iclr.cc/paper_files/paper/2025/file/a73474c359ed523e6cd3174ed29a4d56-Paper-Conference.pdf))
> Causing the agent to reveal the entire task request, including sensitive details beyond a single PII field.

**Semantic sensitive information generation** (1 paper: [A Benchmark for Semantic Sensitive Information in LLMs Outputs](https://proceedings.iclr.cc/paper_files/paper/2025/file/994a53df880f1ec64fd5cbf1bba4a8af-Paper-Conference.pdf))
> The observable act of an LLM producing text that contains semantic sensitive information, particularly in response to simple, non-adversarial prompts.

**Private information leakage** (1 paper: [Can LLMs Keep a Secret? Testing Privacy Implications of Language Models via Contextual Integrity Theory](https://proceedings.iclr.cc/paper_files/paper/2024/file/08305d8b2ddab98932c163ea73df065f-Paper-Conference.pdf))
> The observable act of disclosing sensitive or private information in a context where it should be withheld.

**Prompt extraction** (1 paper: [Tensor Trust: Interpretable Prompt Injection Attacks from an Online Game](https://proceedings.iclr.cc/paper_files/paper/2024/file/519c51529c3544b3430bd8b17d400365-Paper-Conference.pdf))
> The observable behavior where an LLM outputs all or part of its system prompt or access code in response to adversarial input.

**System prompt leakage** (1 paper: [Gandalf the Red: Adaptive Security for LLMs](https://raw.githubusercontent.com/mlresearch/v267/main/assets/pfister25a/pfister25a.pdf))
> An observable attack outcome where the LLM is manipulated into revealing its confidential system prompt or initial instructions.

## Relationships

### Privacy leakage →
- **Membership inference attack** (measurement instrument): *measured_by*, 2 papers
  > we develop the first Membership Inference Attack (MIA) for evaluating and auditing the empirical privacy for the problem of LLM steering via activation editing
  - [Differentially Private Steering for Large Language Model Alignment](https://proceedings.iclr.cc/paper_files/paper/2025/file/45326c2df19fee16fc1ebc44941fea8e-Paper-Conference.pdf)
  - [Privacy Auditing of Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/e76814a0012a46ade4f997591e86f972-Paper-Conference.pdf)
- **Mind2Web** (measurement instrument): *measured_by*, 1 paper
  > We collect 177 action steps that involve diverse PII categories on realistic websites from the Mind2Web dataset, and conduct experiments using one of the most capable generalist web agent frameworks to date. (Abstract)
  - [EIA: ENVIRONMENTAL INJECTION ATTACK ON GENERALIST WEB AGENTS FOR PRIVACY LEAKAGE](https://proceedings.iclr.cc/paper_files/paper/2025/file/a73474c359ed523e6cd3174ed29a4d56-Paper-Conference.pdf)
- **DecodingTrust** (measurement instrument): *measured_by*, 1 paper
  > We use the DecodingTrust (Wang et al., 2024) privacy dataset, focusing on the Enron email extraction task. (Section 4.2)
  - [IterGen: Iterative Semantic-aware Structured LLM Generation with Backtracking](https://proceedings.iclr.cc/paper_files/paper/2025/file/3d3a9e085540c65dd3e5731361f9320e-Paper-Conference.pdf)
- **MUSE** (measurement instrument): *measured_by*, 1 paper
  > We address this issue by proposing MUSE, a comprehensive machine unlearning evaluation benchmark that enumerates six diverse desirable properties for unlearned models: (1) no verbatim memorization, (2) no knowledge memorization, (3) no privacy leakage, (4) utility preservation on data not intended for removal, (5) scalability with respect to the size of removal requests, and (6) sustainability over sequential unlearning requests. (Section 1)
  - [MUSE: Machine Unlearning Six-Way Evaluation for Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/4556f5398bd2c61bd7500e306b4e560a-Paper-Conference.pdf)
- **InjecAgent** (measurement instrument): *measured_by*, 1 paper
  > It tests two types of attacks: direct harm attacks ... and data stealing attacks
  - [UDora: A Unified Red Teaming Framework against LLM Agents by Dynamically Hijacking Their Own Reasoning](https://raw.githubusercontent.com/mlresearch/v267/main/assets/zhang25cl/zhang25cl.pdf)

### → Privacy leakage
- **Memorization** (construct): *causes*, 3 papers
  > there is also growing concern around the privacy risks of their deployment (McCallum, 2023; Bloomberg, 2023; Politico, 2023), because they can memorize some of their training data verbatim
  - [Privacy Auditing of Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/e76814a0012a46ade4f997591e86f972-Paper-Conference.pdf)
  - [Min-K%++: Improved Baseline for Pre-Training Data Detection from Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/a2e3b4132ab2e0b7a21e6e75da7f91a9-Paper-Conference.pdf)
  - [Merger-as-a-Stealer: Stealing Targeted PII from Aligned LLMs with Model Merging](https://aclanthology.org/2025.emnlp-main.295.pdf)

### Associated with
- **Privacy preservation** (construct), 1 paper
  > "we evaluate privacy in terms of awareness and leakage"
  - [MultiTrust: A Comprehensive Benchmark Towards Trustworthy Multimodal Large Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/586640cda3db2dc77349013dcefee456-Paper-Datasets_and_Benchmarks_Track.pdf)
- **Action grounding** (behavioral indicator), 1 paper
  > EIA with the MI strategy can attack the action grounding stage of SeeAct and leak users' specific PII
  - [EIA: ENVIRONMENTAL INJECTION ATTACK ON GENERALIST WEB AGENTS FOR PRIVACY LEAKAGE](https://proceedings.iclr.cc/paper_files/paper/2025/file/a73474c359ed523e6cd3174ed29a4d56-Paper-Conference.pdf)
- **Chain of thought** (behavioral indicator), 1 paper
  > it has been shown in (Jiang et al., 2025; Wu et al., 2025) that reasoning traces can carry more sensitive information than final answers (Section 2)
  - [Reasoning Model Unlearning: Forgetting Traces, Not Just Answers, While Preserving Reasoning Skills](https://aclanthology.org/2025.emnlp-main.220.pdf)
