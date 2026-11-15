# Positional bias
**Type:** Construct  
**Supporting papers:** 43  
**Also known as:** Positional Bias, Ordering bias, Position bias, Middle bias, Order bias, Thought shifting  

## State of the Field

**Space of definitions.** Across papers, positional bias is most commonly treated as order- or location-sensitive behavior: model outputs, attention, retrieval, or evaluations change because information appears at a particular place in the context or comparison rather than because the content differs. This dominant framing is described as under-attention to the middle, degradation for later tokens, easier memorization or retrieval from earlier training positions, or stronger influence from demonstrations that appear later and closer to the query. Smaller lines of work define it more narrowly as a systematic evaluation error in pairwise comparison, or as option-order bias in multiple-choice and Likert settings, where one side or answer position is favored regardless of quality. Definitions differ mainly in where position enters, long context, training documents, demonstrations, or answer ordering, though they share the idea that presentation location changes behavior.

**Space of facets.** Papers use several near-synonymous labels for related order effects: position bias, ordering bias, and order bias all refer to output changes driven by presentation order, and one paper explicitly equates positional bias with permutation bias. Within long-context work, lost-in-the-middle and middle bias are treated as manifestations of uneven positional sensitivity, with middle bias described as attention concentrated on a few middle tokens and as distinct from sink or recency effects. Another strand introduces thought shifting as a reasoning-level manifestation, where positional bias alters the reasoning trajectory, and one paper contrasts reducing lost-in-the-middle with replacing it by recency bias.

**Space of measurement.** Operationalization spans 3 linked measurement instruments and 7 behavioral indicators. The named instruments are Chatbot Arena, where weak LLM judges were observed to prefer the first response, MMLU, used in experiments on removing positional bias, and PoSum-Bench, a benchmark for positional bias in conversational summarization; the linked indicators include Lost-in-the-middle and Multiple-choice question answering. Across these setups, authors make the construct concrete by shuffling option or response order, or by moving relevant content across the context window, and then checking whether selections, preferences, retrieval success, or summarization behavior change. These operationalizations largely follow the broad definitions of position-sensitive behavior, though pairwise judge preference and option-order tests reflect the narrower evaluation and multiple-choice framings.

**Links.** Several papers claim causal relationships from positional bias to long-context understanding and long-context reasoning, to knowledge extraction ability, and to task performance or evaluation properties. One paper reports that faithfulness correlates with it through a U-shaped pattern, where beginnings and ends are handled more faithfully than the middle. Papers also relate it to selection bias. Overall, the literature links it to 9 constructs and 7 behavioral indicators.

## Sources

**Positional bias** (7 papers: [Exploring the Role of Large Language Models in Prompt Encoding for Diffusion Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/d68c1d10957c8d21ed9dea209533c5a4-Paper-Conference.pdf), [Revisiting In-context Learning Inference Circuit in Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/22d4f952efa13970f0b1ffb22170d416-Paper-Conference.pdf), [On Positional Bias of Faithfulness for Long-form Summarization](https://aclanthology.org/2025.naacl-long.442.pdf), [Where is the answer? An empirical study of positional bias for parametric knowledge extraction in language model](https://aclanthology.org/2025.naacl-long.58.pdf), [Positional Overload: Positional Debiasing and Context Window Extension for Large Language Models using Set Encoding](https://aclanthology.org/2025.acl-long.197.pdf), [Aligning with Logic: Measuring, Evaluating and Improving Logical Preference Consistency in Large Language Models](https://raw.githubusercontent.com/mlresearch/v267/main/assets/liu25u/liu25u.pdf), [Break the Checkbox: Challenging Closed-Style Evaluations of Cultural Alignment in LLMs](https://aclanthology.org/2025.emnlp-main.2.pdf))
> An intrinsic property of decoder-only models where the ability to comprehend and represent information degrades for tokens appearing later in a sequence, due to the causal attention mechanism.

**Positional Bias** (1 paper: [RevisEval: Improving LLM-as-a-Judge via Response-Adapted References](https://proceedings.iclr.cc/paper_files/paper/2025/file/f7ed2318cec3540ca267c3ede12d82fe-Paper-Conference.pdf))
> A systematic error where evaluation outcomes depend on the order of presentation rather than content quality.

**Ordering bias** (1 paper: [ReCogLab: a framework testing relational reasoning & cognitive hypotheses on LLMs](https://proceedings.iclr.cc/paper_files/paper/2025/file/6fc46679a7ba2ec82183cf01b80e5133-Paper-Conference.pdf))
> A tendency for performance to vary depending on the presentation order of premises or statements.

**Position bias** (4 papers: [Follow My Instruction and Spill the Beans: Scalable Data Extraction from Retrieval-Augmented Generation Systems](https://proceedings.iclr.cc/paper_files/paper/2025/file/79cafa874121a3435d8a54f454b646b4-Paper-Conference.pdf), [Generating Complex Question Decompositions in the Face of Distribution Shifts](https://aclanthology.org/2025.naacl-long.55.pdf), [Tuning LLM Judge Design Decisions for 1/1000 of the Cost](https://raw.githubusercontent.com/mlresearch/v267/main/assets/salinas25a/salinas25a.pdf), [POSITION BIAS MITIGATES POSITION BIAS: Mitigate Position Bias Through Inter-Position Knowledge Distillation](https://aclanthology.org/2025.emnlp-main.78.pdf))
> A model's latent tendency to give disproportionate weight to information based on its position within the context window, such as favoring content at the beginning or end.

**Middle bias** (1 paper: [ParallelComp: Parallel Long-Context Compressor for Length Extrapolation](https://raw.githubusercontent.com/mlresearch/v267/main/assets/xiong25b/xiong25b.pdf))
> The latent tendency of the model to focus disproportionately on a subset of tokens located in the middle of the input sequence, forming a non-uniform attention pattern distinct from sink or recency effects.

**Order bias** (1 paper: [A Comprehensive Literary Chinese Reading Comprehension Dataset with an Evidence Curation Based Solution](https://aclanthology.org/2025.emnlp-main.177.pdf))
> The tendency of a model to favor certain answer positions (e.g., A, B, C, D) regardless of content, indicating a vulnerability to the presentation order of options rather than genuine comprehension.

**Thought shifting** (1 paper: [POSITION BIAS MITIGATES POSITION BIAS: Mitigate Position Bias Through Inter-Position Knowledge Distillation](https://aclanthology.org/2025.emnlp-main.78.pdf))
> The deviation in a model's reasoning chain due to the position of relevant documents, resulting in incorrect or suboptimal reasoning paths in multi-hop tasks.

## Relationships

### Positional bias →
- **Long-context understanding** (construct): *causes*, 2 papers
  > "they tend to favor content at certain positions ... which harms complex reasoning (Chen et al., 2024b), long-context understanding (Liu et al., 2024) and model-based evaluation"
  - [Eliminating Position Bias of Language Models: A Mechanistic Approach](https://proceedings.iclr.cc/paper_files/paper/2025/file/e389b15166cf98966ba058965a8c17e3-Paper-Conference.pdf)
  - [POSITION BIAS MITIGATES POSITION BIAS: Mitigate Position Bias Through Inter-Position Knowledge Distillation](https://aclanthology.org/2025.emnlp-main.78.pdf)
- **Robustness** (construct): *causes*, 1 paper
  > "This bias often leads to unexpected model failures and hurts performance, robustness, and reliability across various applications."
  - [Eliminating Position Bias of Language Models: A Mechanistic Approach](https://proceedings.iclr.cc/paper_files/paper/2025/file/e389b15166cf98966ba058965a8c17e3-Paper-Conference.pdf)
- **Reliability** (construct): *causes*, 1 paper
  > "This bias often leads to unexpected model failures and hurts performance, robustness, and reliability across various applications."
  - [Eliminating Position Bias of Language Models: A Mechanistic Approach](https://proceedings.iclr.cc/paper_files/paper/2025/file/e389b15166cf98966ba058965a8c17e3-Paper-Conference.pdf)
- **Knowledge extraction ability** (construct): *causes*, 1 paper
  > LMs suffer from positional bias in the training data, i.e. they struggle to answer questions about the information described in the middle or at the end of the training document. (Abstract)
  - [Where is the answer? An empirical study of positional bias for parametric knowledge extraction in language model](https://aclanthology.org/2025.naacl-long.58.pdf)
- **Boolean question answering** (behavioral indicator): *causes*, 1 paper
  > We further find that the positional bias can hurt models’ performance even for questions answerable with Yes/No. (Section 1)
  - [Where is the answer? An empirical study of positional bias for parametric knowledge extraction in language model](https://aclanthology.org/2025.naacl-long.58.pdf)
- **MMLU** (measurement instrument): *measured_by*, 1 paper
  > Our experiments with the MMLU dataset (Hendrycks et al., 2020) show that set encoding offers a guaranteed and efficient way to remove positional bias without requiring multiple model runs or complex debiasing techniques. (Section 1)
  - [Positional Overload: Positional Debiasing and Context Window Extension for Large Language Models using Set Encoding](https://aclanthology.org/2025.acl-long.197.pdf)
- **Chatbot Arena** (measurement instrument): *measured_by*, 1 paper
  > We observed positional bias in some weak LLM judges on Chatbot Arena where the first response was consistently preferred, similar to (Zheng et al., 2023).
  - [SkillAggregation: Reference-free LLM-Dependent Aggregation](https://aclanthology.org/2025.acl-long.756.pdf)
- **PoSum-Bench** (measurement instrument): *measured_by*, 1 paper
  > To address this issue, we introduce PoSum-Bench, a comprehensive benchmark for evaluating positional bias in conversational summarization, featuring diverse English and French conversational datasets spanning formal meetings, casual conversations, and customer service interactions. (Abstract)
  - [PoSum-Bench: Benchmarking Position Bias in LLM-based Conversational Summarization](https://aclanthology.org/2025.emnlp-main.404.pdf)
- **Long-context reasoning** (construct): *causes*, 1 paper
  > PB poses significant obstacles in information-rich settings, such as retrieval-augmented generation (Fang et al., 2025; Dong et al., 2025b), long-context reasoning (Li et al., 2024a; Kuratov et al., 2024), and LLM-as-a-judge (Wang et al., 2024b; Li et al., 2024c). (Section 1)
  - [POSITION BIAS MITIGATES POSITION BIAS: Mitigate Position Bias Through Inter-Position Knowledge Distillation](https://aclanthology.org/2025.emnlp-main.78.pdf)

### → Positional bias
- **Faithfulness** (construct): *correlates*, 1 paper
  > Analyzing LLM-generated summaries across six datasets, we find a "U-shaped" trend in faithfulness, where LLMs faithfully summarize the beginning and end of documents but neglect middle content.
  - [On Positional Bias of Faithfulness for Long-form Summarization](https://aclanthology.org/2025.naacl-long.442.pdf)

### Associated with
- **Multiple-choice question answering** (behavioral indicator), 2 papers
  > Pezeshkpour et al., 2023 identify inherent ‘positional bias’ in the MCQ setting, where LLMs prefer to select options in specific positions as answers (Section 2)
  - [Order-Independence Without Fine Tuning](https://proceedings.neurips.cc/paper_files/paper/2024/file/85529bc995777a74072ef63c05bedd30-Paper-Conference.pdf)
  - [Positional Overload: Positional Debiasing and Context Window Extension for Large Language Models using Set Encoding](https://aclanthology.org/2025.acl-long.197.pdf)
- **Pairwise comparison** (behavioral indicator), 2 papers
  > Positional bias (Wang et al., 2024a; Zheng et al., 2023; Wu & Aji, 2023; Chen et al., 2024) occurs when human or LLM evaluators tend to favor one side in a pairwise comparison, regardless of answer quality. (Section 4.5)
  - [RevisEval: Improving LLM-as-a-Judge via Response-Adapted References](https://proceedings.iclr.cc/paper_files/paper/2025/file/f7ed2318cec3540ca267c3ede12d82fe-Paper-Conference.pdf)
  - [Eliminating Position Bias of Language Models: A Mechanistic Approach](https://proceedings.iclr.cc/paper_files/paper/2025/file/e389b15166cf98966ba058965a8c17e3-Paper-Conference.pdf)
- **Lost-in-the-middle** (behavioral indicator), 2 papers
  > “We observed significant positional bias in LMMs, reminiscent of the ‘lost-in-the-middle’ pathology found in NLP tasks”
  - [Visual Haystacks: A Vision-Centric Needle-In-A-Haystack Benchmark](https://proceedings.iclr.cc/paper_files/paper/2025/file/a264726ebd222124514a32bf0143b83d-Paper-Conference.pdf)
  - [On the Emergence of Position Bias in Transformers](https://raw.githubusercontent.com/mlresearch/v267/main/assets/wu25ad/wu25ad.pdf)
- **Selection bias** (construct), 2 papers
  > Our findings show that selection bias, driven by both token identity and positional preferences, intensifies with increasing task difficulty, particularly when MCQ options are fine-grained. (Conclusion)
  - [Benchmarking and Mitigating MCQA Selection Bias of Large Vision-Language Models](https://aclanthology.org/2025.emnlp-main.1703.pdf)
  - [Large Language Models Are Not Robust Multiple Choice Selectors](https://proceedings.iclr.cc/paper_files/paper/2024/file/54dd9e0cff6d9214e20d97eb2a3bae49-Paper-Conference.pdf)
- **Recency bias** (construct), 1 paper
  > “This approach may appear to improve faithfulness, but it ultimately replaces one positional bias, i.e., lost-in-the-middle, with another, i.e., recency bias.”
  - [On Positional Bias of Faithfulness for Long-form Summarization](https://aclanthology.org/2025.naacl-long.442.pdf)
- **Preference consistency** (construct), 1 paper
  > Moreover, GPT-3.5-Turbo shows a markedly lower preference consistency than GPT-4-Turbo, indicating that its evaluations are primarily driven by position bias rather than comparing output qualities. (Section 4.3)
  - [Investigating Non-Transitivity in LLM-as-a-Judge](https://raw.githubusercontent.com/mlresearch/v267/main/assets/xu25w/xu25w.pdf)
- **Word sense disambiguation** (behavioral indicator), 1 paper
  > This pattern highlights a potential limitation in some LLMs: rather than evaluating definitions purely on semantic appropriateness, they may rely on superficial heuristics such as positional order, which may compromise their reliability and generalization in unbiased WSD tasks (Section 3.2).
  - [Do Large Language Models Understand Word Senses?](https://aclanthology.org/2025.emnlp-main.1720.pdf)
- **Multi-document question answering** (behavioral indicator), 1 paper
  > We select four tasks that pose position bias: ... retrieval-augmented question-answering (Liu et al., 2024) that asks LMs to answer questions based on retrieved documents
  - [Eliminating Position Bias of Language Models: A Mechanistic Approach](https://proceedings.iclr.cc/paper_files/paper/2025/file/e389b15166cf98966ba058965a8c17e3-Paper-Conference.pdf)
- **Synthetic recall** (behavioral indicator), 1 paper
  > In retrieval tasks, PB predominantly manifests as token-shifting... (Section 1)
  - [POSITION BIAS MITIGATES POSITION BIAS: Mitigate Position Bias Through Inter-Position Knowledge Distillation](https://aclanthology.org/2025.emnlp-main.78.pdf)
