# Repetitive generation
**Type:** Behavioral indicator  
**Supporting papers:** 21  
**Also known as:** Repetitive text generation, Repetition, Parroting, Meaningless repetition, Content repetition, Token repetition, Duplication, Text repetition, Oscillatory hallucination  

## State of the Field

**Space of definitions.** Across papers, the prevailing usage is as a generation failure in which outputs repeat tokens, words, phrases, sentences, utterances, or ideas. Most descriptions treat the repeated material as unnecessary or meaningless, either as repetition that affects meaning, adds no new information, or lowers readability, conciseness, coherence, or response diversity. A smaller line of work narrows it to outputs that devolve into unproductive loops on hard tasks, repeated list items within a single response, or repetition of the same prompted token many times.

**Variants.** Variants span general and long-form text generation, reasoning failures described as unproductive generation loops, multi-turn social dialogue, query-focused and book-length summarization, code generation, and translation. The most common labels are repetitive generation, repetition, and repetitive text generation, while smaller labels include parroting for repeated actions in dialogue and oscillatory hallucination for repeated token sequences in translation. Other formulations focus on duplicate summary spans, duplicate code fragments such as repeated assertions or comments, single-token repetition tasks, and repeated character sequences in no-space content.

**Space of elicitation and scores.** Papers connect it to 1 measurement instrument, Human evaluation. This appears as guideline-based human scoring that assesses repetition alongside fluency, coherence, compatibility, and hallucination, and some evaluation prompts ask directly whether a response repeats itself, including repeated list items.

**What it is taken as evidence of.** No construct is linked to it, so papers do not present a shared view of which construct it reflects. Instead, individual papers report it as related to Style transfer and Reward hacking, and one paper claims a causal relationship from Repetitive generation to Training data regurgitation, stating that repeated tokens could confuse models and create a vulnerability for leakage attacks.

## Sources

**Repetition** (3 papers: [Segment-Level Diffusion: A Framework for Controllable Long-Form Generation with Diffusion Language Models](https://aclanthology.org/2025.acl-long.210.pdf), [MuTIS: Enhancing Reasoning Efficiency through Multi Turn Intervention Sampling in Reinforcement Learning](https://aclanthology.org/2025.emnlp-main.690.pdf), [DETQUS: Decomposition-Enhanced Transformers for QUery-focused Summarization](https://aclanthology.org/2025.naacl-long.138.pdf))
> An observable failure mode where the model generates repetitive tokens, phrases, or entire utterances that degrade the quality and meaning of the text.

**Repetitive text generation** (2 papers: [ReLearn: Unlearning via Learning for Large Language Models](https://aclanthology.org/2025.acl-long.297.pdf), [Branch-GAN: Improving Text Generation with (not so) Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/02a92b52670752daf17b53f04f1ab405-Paper-Conference.pdf))
> An observable failure mode where the model produces outputs consisting of repeating words or phrases.

**Parroting** (1 paper: [SOTOPIA-Ω: Dynamic Strategy Injection Learning and Social Instruction Following Evaluation for Social Agents](https://aclanthology.org/2025.acl-long.1203.pdf))
> Repeating similar or nearly identical actions across multiple turns in a dialogue, resulting in low response diversity despite potential goal achievement.

**Repetitive generation** (4 papers: [Sparse Activation Editing for Reliable Instruction Following in Narratives](https://aclanthology.org/2025.emnlp-main.1311.pdf), [A Closer Look at Machine Unlearning for Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/7b7db41ea66d624587f211aa15c07e45-Paper-Conference.pdf), [Human Feedback is not Gold Standard](https://proceedings.iclr.cc/paper_files/paper/2024/file/f719b8ca81221f380836e573d479c223-Paper-Conference.pdf), [Tailoring Self-Rationalizers with Multi-Reward Distillation](https://proceedings.iclr.cc/paper_files/paper/2024/file/b5e5753b0a0e440a6d8dc7e143617cec-Paper-Conference.pdf))
> Producing overly repetitive text as a failure mode after excessive editing strength.

**Meaningless repetition** (1 paper: [Weights-Rotated Preference Optimization for Large Language Models](https://aclanthology.org/2025.emnlp-main.1329.pdf))
> The observable pattern of repeating phrases, sentences, or ideas without adding new information, often as a result of reward hacking in preference optimization.

**Content repetition** (1 paper: [Rethinking Repetition Problems of LLMs in Code Generation](https://aclanthology.org/2025.acl-long.48.pdf))
> The observable repetition of identical or nearly identical tokens, expressions, or comments in the generated code, such as repeated assertions or print statements.

**Token repetition** (1 paper: [Interpreting the Repeated Token Phenomenon in Large Language Models](https://raw.githubusercontent.com/mlresearch/v267/main/assets/yona25a/yona25a.pdf))
> Producing the same input token repeatedly when prompted with a repetition task.

**Duplication** (1 paper: [BooookScore: A systematic exploration of book-length summarization in the era of LLMs](https://proceedings.iclr.cc/paper_files/paper/2024/file/f7b77476d89d5fb58aeb77691d2f40f5-Paper-Conference.pdf))
> Repeating the same or very similar information multiple times within the summary, reducing conciseness and coherence.

**Text repetition** (1 paper: [RAP: A Metric for Balancing Repetition and Performance in Open-Source Large Language Models](https://aclanthology.org/2025.naacl-long.69.pdf))
> Generating repeated word sequences or repeated character sequences within no-space content.

**Oscillatory hallucination** (1 paper: [Mitigating Hallucinated Translations in Large Language Models with Hallucination-focused Preference Optimization](https://aclanthology.org/2025.naacl-long.175.pdf))
> A repetitive output pattern in translation where a sequence of tokens is excessively repeated, indicating a form of degenerate generation.

## Relationships

### Repetitive generation →
- **Human evaluation** (measurement instrument): *measured_by*, 1 paper
  > To address this, we extend human evaluation guidelines from Clark et al. (2023), assessing repetition, fluency, coherence, compatibility (ROCStories/DialogSum), and hallucination (DeliData): (Section 4.2)
  - [Segment-Level Diffusion: A Framework for Controllable Long-Form Generation with Diffusion Language Models](https://aclanthology.org/2025.acl-long.210.pdf)
- **Training data regurgitation** (behavioral indicator): *causes*, 1 paper
  > Nasr et al. (2023) first observed that repeated tokens could confuse models, creating a vulnerability exploitable for training data leakage attacks. (Section 5)
  - [Interpreting the Repeated Token Phenomenon in Large Language Models](https://raw.githubusercontent.com/mlresearch/v267/main/assets/yona25a/yona25a.pdf)

### Associated with
- **Style transfer** (behavioral indicator), 1 paper
  > First, we observe repetitions and hallucinations in some transferred texts. (Limitations)
  - [Style Transfer with Multi-iteration Preference Optimization](https://aclanthology.org/2025.naacl-long.135.pdf)
- **Reward hacking** (behavioral indicator), 1 paper
  > We observed that with enough training compute, the model started to show signs of reward hacking, where it increased the lengths of its CoTs on hard questions using repetition rather than learning to solve them. (Section 4.6)
  - [Demystifying Long Chain-of-Thought Reasoning](https://raw.githubusercontent.com/mlresearch/v267/main/assets/yang25ae/yang25ae.pdf)
