# LLM-as-a-judge
**Type:** Measurement instrument  
**Supporting papers:** 544  
**Also known as:** LLM-as-judge, LLM-as-a-Judge, Autonomous evaluator, GPT-Judge, LLM judgment, GPT-4 preference evaluation, GPT-4o Based Evaluation, GPT-4o-based evaluation, GPT-4V-aided evaluation, GPT-Evaluation, LLM-based evaluator, Llama-3 70B judge, Llama-3-70B judge, LLM Judge, LLM judge, GPT-based metric, GPT-4 Rating, Automatic evaluation with GPT-4, Success detector, GPT-Eval, ChatGPT Evaluation, External LLM evaluation, GPT-assisted choice evaluation, Automatic evaluation of explanations, LLM grader, Model of Interestingness, Mixture of judges, Oracle-LLM-as-a-judge, LLM-based evaluation pipeline, GPT-4 judge evaluation, GPT-4 Judge Evaluation, LLM-as-judge evaluation, GPT-4 judge, GPT-4 Judge, LLM-as-Judge, GPT-4 comparison, ChatGPT-based evaluator, LLM evaluator, Ref-GPT4, Arena-Hard Judge, Vanilla judge, GPT-4 scoring, LLM-Eval, Judge model evaluation, Judge function, GPT-4o-mini judge, GPT4o-mini judge, Model-based parsers, Claude 3 Opus Harmful-Yet-Helpful Score, GPT-4o scoring, Automated evaluation, GPT4Score, Claude 3-as-a-Judge, GPT-4 utility judge, GPT-4o Judge, LLM-as-Judge (LAJ), GPT Score, GPT-4 eval, GPT-4 assisted evaluation, GPT-4 evaluation, GPT-4 pairwise evaluation, LLM-based auto-evaluation, GPT-4o Score, LMExaminer, GPT-4o evaluation protocol, Model-based verifier, Procedural LLM-based grading, GPT-4 judgment, GPT-4 based evaluation, GPT-4-based evaluation, GPT-4o evaluation, GPT-4o assisted evaluation, LLM-as-judge relevance assessment, MLLM-as-a-Judge, LLMs as Judges, Model-as-Judge, Large-scale pairwise comparison, GPT Judge, GPT-4o judge, Comparative evaluation, Gemini 1.0 Ultra evaluation, Agents-as-an-Evaluator, GPT-4o-based judge, Knowledge Capability, GPT score, Preference-Similarity, GPT-4 based autograder, GPT-4V evaluation, GPT-4-based evaluator, Ensemble-as-Judges, GPT-4o automated judge, LLM judge evaluation, LLM Evaluator, LLM-based grading, GPT4-as-a-judge, Claude-3.5-Sonnet Evaluation, Claude Sonnet API evaluation, GPT-based evaluation, Model-as-judge evaluation, GPT-4 complexity estimation, LLM-based Judge, LLM-Judge, Generative-Judge, LLM-as-Prompt-Judge, Oracle judge model, GPT-4 as a judge, GPT-4 preference analysis, GPT-ranking, LLM-as-a-judge evaluation, Google Gemini evaluation pipeline, DeepSeek R1 evaluation, ERNIE Bot 4.0 evaluation, VLM-as-a-Judge, LLM-assisted evaluation, Bias Judge, NLI Judge, LLM Judge Scores, LM judge evaluation, LLM self-judge, GPT-4o Judgements, GPT-4o-mini Evaluator, LLM-as-judge evaluator, MLLM-as-a-judge, GPT-4o model-based assessment, GPT-4o-based evaluation framework, GPT-eval, LLM-as-Evaluator, LLM-as-a-Meta-Judge, LLM-based Simulated Evaluation, LLM-based alignment evaluation, RAG-AS-A-JUDGE, GPT-4o judge evaluation, GPT-4.1 mini re-evaluation, CUA-as-a-Judge, LLM Judger, OpenAI-o3 evaluation, LLM-based story evaluator, Dic-Judge, GPT-as-a-Judge, LLM-based judge, LLM-based Behavior Classification, LLM-based safety moderator, Automated LLM-based evaluation framework, LM-as-a-judge, LLM-based Classical Poetry Metric, GPT-4-as-a-judge, LLM evaluation, GPT-4 multidimensional score, GPT-4 rating, GPT-4V based evaluation, GPT-4 Evaluation, GPT-4 win rate, GPT-4–judged pairwise comparisons, Pairwise evaluation, LLM-based zero-shot annotation, LLM-CoT, ChatbotArena (Arena-Hard) prompt, LLM-powered evaluation, LLM-based evaluation, Model-Based Evaluation, GPT-based assessment, GPT evaluation, Llama3-based metric, Model-based evaluation, GPT-4V judge, GPT-4 evaluator, ChatGPT-based evaluation, GPT-3.5-turbo evaluation, GPT-4-based preference test, GPT-4 evaluation protocol, GPT-3.5-based evaluation, GPT-4 ranking, GPT-4 Grader, Claude 3 Opus Grader, GPT-4 feedback, GPT-4o-mini labeling, GPT-4o-based metric, GPT-4-based Likert evaluation, Judge LLM evaluation, LLM-as-a-judge framework, LLM-as-judge framework, GPT-4o as a judge, GPT-4o-as-Judge, Autorater evaluation, Model arena evaluation, GPT-4o evaluator, LLMs-as-Judges, GPT-4V-based evaluation  

## State of the Field

**What it is.** Across papers, the prevailing usage is an evaluation protocol in which one language model, usually a separate or stronger model, judges another model's outputs. Most definitions describe pairwise comparisons, numeric scoring, binary correctness or harmfulness judgments, or rubric-based classification over open-ended responses, sometimes with references, full dialogue history, source documents, or images as context. A smaller line of work extends the same pattern to VLM or MLLM judges, autonomous evaluators, prompt judges, meta-judges, and ensemble or mixture-of-judges setups, and some papers distinguish prompting styles such as a Vanilla judge or an Arena-Hard judge.

**What it is claimed to measure.** Papers use it to measure 53 constructs and 33 behavioral indicators, so the claims spread across many targets rather than converging on one construct. The most common construct-level uses are helpfulness, harmlessness, factuality, and text generation quality, and the most frequent behavioral use is text generation, with the remaining links spanning 49 other constructs and 32 other behavioral indicators.

**Space of uses.** Most papers position it as a scalable proxy for human annotation when outputs are open-ended or hard to score with exact-match, BLEU, or ROUGE, and many use it alongside human checks, rule-based metrics, or benchmark-specific measures. Across papers, it is linked to 11 measurement instruments: most often Human evaluation, WildBench, EHRNoteQA, Expert evaluation, and FLASK, with six other instruments linked as well. In recorded relationships, papers report that it correlates with Human evaluation and Expert evaluation, and is related to WildBench, EHRNoteQA, and FLASK; some papers use it as the main metric, while others treat it as an auxiliary validation step.

**Concerns raised.** A recurring concern is validity and robustness. Some papers say LLM-as-a-judge results can be difficult to interpret and may not align with human judgments, others describe LLM graders as non-determinant and highly dependent on prompts, and several note positional bias or judge-specific bias, leading to order swapping, ensembles, or multiple judges to reduce it. Additional concerns include extra API or inference cost, possible overfitting to the judge, data and model bias in agent-based evaluator variants, and task mismatch, for example claims that general LLM-as-a-judge setups may miss numerical accuracy or table topic coverage.

## Sources

**LLM-as-judge** (23 papers: [OmniJARVIS: Unified Vision-Language-Action Tokenization Enables Open-World Instruction Following Agents](https://proceedings.neurips.cc/paper_files/paper/2024/file/85f1225db986e629289f402c46eff1a4-Paper-Conference.pdf), [Spread Preference Annotation: Direct Preference Judgment for Efficient LLM Alignment](https://proceedings.iclr.cc/paper_files/paper/2025/file/342e5fc02b86dec9b24e41b22968e539-Paper-Conference.pdf), [Generating Complex Question Decompositions in the Face of Distribution Shifts](https://aclanthology.org/2025.naacl-long.55.pdf), [Contrastive Perplexity for Controlled Generation: An Application in Detoxifying Large Language Models](https://aclanthology.org/2025.acl-long.125.pdf), [Correlated Errors in Large Language Models](https://raw.githubusercontent.com/mlresearch/v267/main/assets/kim25e/kim25e.pdf), [AIR: Complex Instruction Generation via Automatic Iterative Refinement](https://aclanthology.org/2025.emnlp-main.1628.pdf), [DIWALI - Diversity and Inclusivity aWare cuLture specific Items for India: Dataset and Assessment of LLMs for Cultural Text Adaptation in Indian Context](https://aclanthology.org/2025.emnlp-main.1706.pdf), [DischargeSim: A Simulation Benchmark for Educational Doctor–Patient Communication at Discharge](https://aclanthology.org/2025.emnlp-main.546.pdf), [GraphAgent: Agentic Graph Language Assistant](https://aclanthology.org/2025.emnlp-main.1339.pdf), [Hallucination Detection in LLMs Using Spectral Features of Attention Maps](https://aclanthology.org/2025.emnlp-main.1239.pdf), [HypER: Literature-grounded Hypothesis Generation and Distillation with Provenance](https://aclanthology.org/2025.emnlp-main.1292.pdf), [Making VLMs More Robot-Friendly: Self-Critical Distillation of Low-Level Procedural Reasoning](https://aclanthology.org/2025.emnlp-main.1658.pdf), [NileChat: Towards Linguistically Diverse and Culturally Aware LLMs for Local Communities](https://aclanthology.org/2025.emnlp-main.556.pdf), [R-TOFU: Unlearning in Large Reasoning Models](https://aclanthology.org/2025.emnlp-main.265.pdf), [SEPS: A Separability Measure for Robust Unlearning in LLMs](https://aclanthology.org/2025.emnlp-main.283.pdf), [Sparse Neurons Carry Strong Signals of Question Ambiguity in LLMs](https://aclanthology.org/2025.emnlp-main.813.pdf), [TactfulToM: Do LLMs have the Theory of Mind ability to understand White Lies?](https://aclanthology.org/2025.emnlp-main.1272.pdf), [The Illusion of Progress: Re-evaluating Hallucination Detection in LLMs](https://aclanthology.org/2025.emnlp-main.1761.pdf), [ThinkSLM: Towards Reasoning in Small Language Models](https://aclanthology.org/2025.emnlp-main.1659.pdf), [Threading the Needle: Reweaving Chain-of-Thought Reasoning to Explain Human Label Variation](https://aclanthology.org/2025.emnlp-main.1682.pdf), [Tuning Less, Prompting More: In-Context Preference Learning Pipeline for Natural Language Transformation](https://aclanthology.org/2025.emnlp-main.737.pdf), [WebMMU: A Benchmark for Multimodal Multilingual Website Understanding and Code Generation](https://aclanthology.org/2025.emnlp-main.1276.pdf), [XLQA: A Benchmark for Locale-Aware Multilingual Open-Domain Question Answering](https://aclanthology.org/2025.emnlp-main.1466.pdf))
> An evaluation protocol where a large language model is used to assess the quality and accuracy of another model's outputs, particularly for open-ended tasks like question answering.

**LLM-as-a-judge** (70 papers: [IaC-Eval: A Code Generation Benchmark for Cloud Infrastructure-as-Code Programs](https://proceedings.neurips.cc/paper_files/paper/2024/file/f26b29298ae8acd94bd7e839688e329b-Paper-Datasets_and_Benchmarks_Track.pdf), [LongGenBench: Benchmarking Long-Form Generation in Long Context LLMs](https://proceedings.iclr.cc/paper_files/paper/2025/file/141304a37d59ec7f116f3535f1b74bde-Paper-Conference.pdf), [GuideLLM: Exploring LLM-Guided Conversation with Applications in Autobiography Interviewing](https://aclanthology.org/2025.naacl-long.287.pdf), [Is a Peeled Apple Still Red? Evaluating LLMs' Ability for Conceptual Combination with Property Type](https://aclanthology.org/2025.naacl-long.456.pdf), [Fine-Tuning Large Language Models with Sequential Instructions](https://aclanthology.org/2025.naacl-long.288.pdf), [Do RAG Systems Cover What Matters? Evaluating and Optimizing Responses with Sub-Question Coverage](https://aclanthology.org/2025.naacl-long.301.pdf), [Large Language Models for Persian-English Idiom Translation](https://aclanthology.org/2025.naacl-long.405.pdf), [ProMQA: Question Answering Dataset for Multimodal Procedural Activity Understanding](https://aclanthology.org/2025.naacl-long.579.pdf), [FisherSFT: Data-Efficient Supervised Fine-Tuning of Language Models Using Information Gain](https://raw.githubusercontent.com/mlresearch/v267/main/assets/deb25a/deb25a.pdf), [A Good Plan is Hard to Find: Aligning Models with Preferences is Misaligned with What Helps Users](https://aclanthology.org/2025.emnlp-main.585.pdf), [Are LLMs Better than Reported? Detecting Label Errors and Mitigating Their Effect on Model Performance](https://aclanthology.org/2025.emnlp-main.1360.pdf), [CAVE : Detecting and Explaining Commonsense Anomalies in Visual Environments](https://aclanthology.org/2025.emnlp-main.1379.pdf), [Calibrating Verbal Uncertainty as a Linear Feature to Reduce Hallucinations](https://aclanthology.org/2025.emnlp-main.187.pdf), [Can Large Language Models be Effective Online Opinion Miners?](https://aclanthology.org/2025.emnlp-main.1178.pdf), [CodeArena: Evaluating and Aligning CodeLLMs on Human Preference](https://aclanthology.org/2025.emnlp-main.489.pdf), [Creativity in LLM-based Multi-Agent Systems: A Survey](https://aclanthology.org/2025.emnlp-main.1403.pdf), [Date Fragments: A Hidden Bottleneck of Tokenization for Temporal Reasoning](https://aclanthology.org/2025.emnlp-main.159.pdf), [DeepResearcher: Scaling Deep Research via Reinforcement Learning in Real-world Environments](https://aclanthology.org/2025.emnlp-main.22.pdf), [Disambiguation in Conversational Question Answering in the Era of LLMs and Agents: A Survey](https://aclanthology.org/2025.emnlp-main.482.pdf), [Do RAG Systems Really Suffer From Positional Bias?](https://aclanthology.org/2025.emnlp-main.1422.pdf), [Dyve: Thinking Fast and Slow for Dynamic Process Verification](https://aclanthology.org/2025.emnlp-main.1136.pdf), [Efficient Context Selection for Long-Context QA: No Tuning, No Iteration, Just Adaptive-k](https://aclanthology.org/2025.emnlp-main.1017.pdf), [Evaluating Robustness of Large Audio Language Models to Audio Injection: An Empirical Study](https://aclanthology.org/2025.emnlp-main.1303.pdf), [FB-Bench: A Fine-Grained Multi-Task Benchmark for Evaluating LLMs' Responsiveness to Human Feedback](https://aclanthology.org/2025.emnlp-main.471.pdf), [Feature Extraction and Steering for Enhanced Chain-of-Thought Reasoning in Language Models](https://aclanthology.org/2025.emnlp-main.552.pdf), [FinTrust: A Comprehensive Benchmark of Trustworthiness Evaluation in Finance Domain](https://aclanthology.org/2025.emnlp-main.512.pdf), [Flaw or Artifact? Rethinking Prompt Sensitivity in Evaluating LLMs](https://aclanthology.org/2025.emnlp-main.1006.pdf), [From General Reward to Targeted Reward: Improving Open-ended Long-context Generation Models](https://aclanthology.org/2025.emnlp-main.260.pdf), [How Does DPO Reduce Toxicity? A Mechanistic Neuron-Level Analysis](https://aclanthology.org/2025.emnlp-main.1501.pdf), [How to Protect Yourself from 5G Radiation? Investigating LLM Responses to Implicit Misinformation](https://aclanthology.org/2025.emnlp-main.1468.pdf), [Igniting Creative Writing in Small Language Models: LLM-as-a-Judge versus Multi-Agent Refined Rewards](https://aclanthology.org/2025.emnlp-main.868.pdf), [IntentionFrame: A Semi-Structured, Multi-Aspect Framework for Fine-Grained Conversational Intention Understanding](https://aclanthology.org/2025.emnlp-main.1427.pdf), [Investigating Pedagogical Teacher and Student LLM Agents: Genetic Adaptation Meets Retrieval-Augmented Generation Across Learning Styles](https://aclanthology.org/2025.emnlp-main.675.pdf), [LeTS: Learning to Think-and-Search via Process-and-Outcome Reward Hybridization](https://aclanthology.org/2025.emnlp-main.257.pdf), [Learning from Diverse Reasoning Paths with Routing and Collaboration](https://aclanthology.org/2025.emnlp-main.141.pdf), [Liaozhai through the Looking-Glass: On Paratextual Explicitation of Culture-Bound Terms in Machine Translation](https://aclanthology.org/2025.emnlp-main.1744.pdf), [LiteraryQA: Towards Effective Evaluation of Long-document Narrative QA](https://aclanthology.org/2025.emnlp-main.1729.pdf), [Measuring Chain of Thought Faithfulness by Unlearning Reasoning Steps](https://aclanthology.org/2025.emnlp-main.504.pdf), [MemeArena: Automating Context-Aware Unbiased Evaluation of Harmfulness Understanding for Multimodal Large Language Models](https://aclanthology.org/2025.emnlp-main.890.pdf), [Memory-QA: Answering Recall Questions Based on Multimodal Memories](https://aclanthology.org/2025.emnlp-main.1234.pdf), [MetaFaith: Faithful Natural Language Uncertainty Expression in LLMs](https://aclanthology.org/2025.emnlp-main.1505.pdf), [Multi-perspective Analysis of Large Language Model Domain Specialization: An Experiment in Accounting Audit Procedures Generation](https://aclanthology.org/2025.emnlp-main.891.pdf), [MultiMed-ST: Large-scale Many-to-many Multilingual Medical Speech Translation](https://aclanthology.org/2025.emnlp-main.599.pdf), [NOVER: Incentive Training for Language Models via Verifier-Free Reinforcement Learning](https://aclanthology.org/2025.emnlp-main.378.pdf), [NitiBench: Benchmarking LLM Frameworks on Thai Legal Question Answering Capabilities](https://aclanthology.org/2025.emnlp-main.1739.pdf), [On LLM-Based Scientific Inductive Reasoning Beyond Equations](https://aclanthology.org/2025.emnlp-main.476.pdf), [PLLuM-Align: Polish Preference Dataset for Large Language Model Alignment](https://aclanthology.org/2025.emnlp-main.1219.pdf), [Please Translate Again: Two Simple Experiments on Whether Human-Like Reasoning Helps Translation](https://aclanthology.org/2025.emnlp-main.1031.pdf), [Pluralistic Alignment for Healthcare: A Role-Driven Framework](https://aclanthology.org/2025.emnlp-main.1596.pdf), [Proactive Assistant Dialogue Generation from Streaming Egocentric Videos](https://aclanthology.org/2025.emnlp-main.605.pdf), [R-CHAR: A Metacognition-Driven Framework for Role-Playing in Large Language Models](https://aclanthology.org/2025.emnlp-main.1372.pdf), [RAED: Retrieval-Augmented Entity Description Generation for Emerging Entity Linking and Disambiguation](https://aclanthology.org/2025.emnlp-main.1746.pdf), [Recursive Training Loops in LLMs: How training data properties modulate distribution shift in generated data?](https://aclanthology.org/2025.emnlp-main.1643.pdf), [Rethinking Text-based Protein Understanding: Retrieval or LLM?](https://aclanthology.org/2025.emnlp-main.1211.pdf), [ReviewRL: Towards Automated Scientific Review with RL](https://aclanthology.org/2025.emnlp-main.857.pdf), [SATBench: Benchmarking LLMs' Logical Reasoning via Automated Puzzle Generation from SAT Formulas](https://aclanthology.org/2025.emnlp-main.1716.pdf), [SHARP: Steering Hallucination in LVLMs via Representation Engineering](https://aclanthology.org/2025.emnlp-main.725.pdf), [Sketch-of-Thought: Efficient LLM Reasoning with Adaptive Cognitive-Inspired Sketching](https://aclanthology.org/2025.emnlp-main.1236.pdf), [SmartBench: Is Your LLM Truly a Good Chinese Smartphone Assistant?](https://aclanthology.org/2025.emnlp-main.194.pdf), [Summarizing Speech: A Comprehensive Survey](https://aclanthology.org/2025.emnlp-main.1388.pdf), [Synthetic Socratic Debates: Examining Persona Effects on Moral Decision and Persuasion Dynamics](https://aclanthology.org/2025.emnlp-main.831.pdf), [T2R-BENCH: A Benchmark for Real World Table-to-Report Task](https://aclanthology.org/2025.emnlp-main.1141.pdf), [TP-RAG: Benchmarking Retrieval-Augmented Large Language Model Agents for Spatiotemporal-Aware Travel Planning](https://aclanthology.org/2025.emnlp-main.626.pdf), [TableEval: A Real-World Benchmark for Complex, Multilingual, and Multi-Structured Table Question Answering](https://aclanthology.org/2025.emnlp-main.363.pdf), [TaxoAlign: Scholarly Taxonomy Generation Using Language Models](https://aclanthology.org/2025.emnlp-main.1536.pdf), [Think, Verbalize, then Speak: Bridging Complex Thoughts and Comprehensible Speech](https://aclanthology.org/2025.emnlp-main.726.pdf), [TounsiBench: Benchmarking Large Language Models for Tunisian Arabic](https://aclanthology.org/2025.emnlp-main.1756.pdf), [Translationese-index: Using Likelihood Ratios for Graded and Generalizable Measurement of Translationese](https://aclanthology.org/2025.emnlp-main.633.pdf), [User Feedback in Human-LLM Dialogues: A Lens to Understand Users But Noisy as a Learning Signal](https://aclanthology.org/2025.emnlp-main.133.pdf), [WangchanThaiInstruct: An instruction-following Dataset for Culture-Aware, Multitask, and Multi-domain Evaluation in Thai](https://aclanthology.org/2025.emnlp-main.175.pdf))
> An evaluation protocol in which a language model is used as the judge to assess whether generated solutions are correct.

**LLM-as-a-Judge** (5 papers: [HonestLLM: Toward an Honest and Helpful Large Language Model](https://proceedings.neurips.cc/paper_files/paper/2024/file/0d99a8c048befb6dd6e17d7684adacac-Paper-Conference.pdf), [Generative Verifiers: Reward Modeling as Next-Token Prediction](https://proceedings.iclr.cc/paper_files/paper/2025/file/214308a2d5e3f83ef9ad2739e1cbc46d-Paper-Conference.pdf), [CAMIEval: Enhancing NLG Evaluation through Multidimensional Comparative Instruction-Following Analysis](https://aclanthology.org/2025.naacl-long.438.pdf), [ITALIC: An Italian Culture-Aware Natural Language Benchmark](https://aclanthology.org/2025.naacl-long.68.pdf), [Tree-of-Evolution: Tree-Structured Instruction Evolution for Code Generation in Large Language Models](https://aclanthology.org/2025.acl-long.14.pdf))
> An evaluation methodology where a large language model is used to judge and score the quality of another model's responses based on a predefined set of criteria.

**Autonomous evaluator** (1 paper: [DigiRL: Training In-The-Wild Device-Control Agents with Autonomous Reinforcement Learning](https://proceedings.neurips.cc/paper_files/paper/2024/file/1704ddd0bb89f159dfe609b32c889995-Paper-Conference.pdf))
> A Gemini 1.5 Pro-based evaluation procedure that judges whether a screenshot indicates task completion and assigns success or failure to trajectories.

**GPT-Judge** (2 papers: [ERBench: An Entity-Relationship based Automatically Verifiable Hallucination Benchmark for Large Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/5ef9853a6cdea40ae3e301a6d8dc32b5-Paper-Datasets_and_Benchmarks_Track.pdf), [Layer-Level Self-Exposure and Patch: Affirmative Token Mitigation for Jailbreak Attack Defense](https://aclanthology.org/2025.naacl-long.623.pdf))
> A GPT-4-based judgment protocol used to compare whether two rationales refer to the same entity with the same properties.

**LLM judgment** (1 paper: [Automating Dataset Updates Towards Reliable and Timely Evaluation of Large Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/1e89c12621c0315373f20f0aeabe5dbe-Paper-Datasets_and_Benchmarks_Track.pdf))
> An evaluation procedure in which an LLM scores a candidate answer against a reference answer on accuracy, coherence, and factuality.

**GPT-based metric** (1 paper: [VoxDialogue: Can Spoken Dialogue Systems Understand Information Beyond Words?](https://proceedings.iclr.cc/paper_files/paper/2025/file/011df158529ddceb5f2f7a65f2732a5a-Paper-Conference.pdf))
> A qualitative evaluation protocol that uses a large language model (GPT) to assess the quality of generated dialogue responses based on a 5-point scale of contextual relevance and attribute accuracy.

**GPT-4 preference evaluation** (1 paper: [SCOPE: A Self-supervised Framework for Improving Faithfulness in Conditional Text Generation](https://proceedings.iclr.cc/paper_files/paper/2025/file/05d6b5b6901fb57d2c287e1d3ce6d63c-Paper-Conference.pdf))
> A pairwise preference evaluation protocol using GPT-4 as a proxy for human judgment to assess the relative faithfulness of two generated texts against a common input.

**GPT-4 Rating** (1 paper: [DRESSing Up LLM: Efficient Stylized Question-Answering via Style Subspace Editing](https://proceedings.iclr.cc/paper_files/paper/2025/file/09425891e393e64b0535194a81ba15b7-Paper-Conference.pdf))
> An evaluation protocol using GPT-4 to rate stylized responses comprehensively on a scale of 0 to 10, serving as a surrogate for human evaluation.

**LLM-based evaluator** (2 papers: [Agents' Room: Narrative Generation through Multi-step Collaboration](https://proceedings.iclr.cc/paper_files/paper/2025/file/0fbc8a83d93dd8021a4dd8d2d34138eb-Paper-Conference.pdf), [UDA: A Benchmark Suite for Retrieval Augmented Generation in Real-World Document Analysis](https://proceedings.neurips.cc/paper_files/paper/2024/file/7c06759d1a8567f087b02e8589454917-Paper-Datasets_and_Benchmarks_Track.pdf))
> An automated evaluation procedure that uses a large language model to perform side-by-side comparisons of system-generated stories based on prompts targeting specific quality dimensions.

**GPT-4V-aided evaluation** (1 paper: [Self-Correcting Decoding with Generative Feedback for Mitigating Hallucinations in Large Vision-Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/109cf25cbc36037deecdbeabfa199956-Paper-Conference.pdf))
> An evaluation protocol where a powerful vision-language model (GPT-4V) is used to assess the quality, accuracy, and detailedness of responses generated by other models.

**LLM-based evaluation** (18 papers: [MedTrinity-25M: A Large-scale Multimodal Dataset with Multigranular Annotations for Medicine](https://proceedings.iclr.cc/paper_files/paper/2025/file/11c483499c285f30daf832c17dc752bd-Paper-Conference.pdf), [Semantic-Eval : A Semantic Comprehension Evaluation Framework for Large Language Models Generation without Training](https://aclanthology.org/2025.acl-long.477.pdf), [A Multilingual, Culture-First Approach to Addressing Misgendering in LLM Applications](https://aclanthology.org/2025.emnlp-main.1587.pdf), [Argument Summarization and its Evaluation in the Era of Large Language Models](https://aclanthology.org/2025.emnlp-main.1797.pdf), [Beyond Static Testbeds: An Interaction-Centric Agent Simulation Platform for Dynamic Recommender Systems](https://aclanthology.org/2025.emnlp-main.956.pdf), [Beyond Task-Oriented and Chitchat Dialogues: Proactive and Transition-Aware Conversational Agents](https://aclanthology.org/2025.emnlp-main.672.pdf), [C3: A Bilingual Benchmark for Spoken Dialogue Models Exploring Challenges in Complex Conversations](https://aclanthology.org/2025.emnlp-main.1160.pdf), [Certified Mitigation of Worst-Case LLM Copyright Infringement](https://aclanthology.org/2025.emnlp-main.1784.pdf), [KCS: Diversify Multi-hop Question Generation with Knowledge Composition Sampling](https://aclanthology.org/2025.emnlp-main.1181.pdf), [NormGenesis: Multicultural Dialogue Generation via Exemplar-Guided Social Norm Modeling and Violation Recovery](https://aclanthology.org/2025.emnlp-main.1715.pdf), [On the Role of Model Prior in Real-World Inductive Reasoning](https://aclanthology.org/2025.emnlp-main.534.pdf), [QUIDS: Query Intent Description for Exploratory Search via Dual Space Modeling](https://aclanthology.org/2025.emnlp-main.1680.pdf), [Teaching Your Models to Understand Code via Focal Preference Alignment](https://aclanthology.org/2025.emnlp-main.707.pdf), [Towards AI-Assisted Psychotherapy: Emotion-Guided Generative Interventions](https://aclanthology.org/2025.emnlp-main.1664.pdf), [Transferable Direct Prompt Injection via Activation-Guided MCMC Sampling](https://aclanthology.org/2025.emnlp-main.102.pdf), [Uncovering Argumentative Flow: A Question-Focus Discourse Structuring Framework](https://aclanthology.org/2025.emnlp-main.416.pdf), [VisFinEval: A Scenario-Driven Chinese Multimodal Benchmark for Holistic Financial Understanding](https://aclanthology.org/2025.emnlp-main.1229.pdf), [ANAH-v2: Scaling Analytical Hallucination Annotation of Large Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/6e4cdfdd909ea4e34bfc85a12774cba0-Paper-Conference.pdf))
> A quality assessment protocol where a large language model, such as GPT-4V, is used to score the factual and diagnostic accuracy of generated medical descriptions.

**GPT-Evaluation** (1 paper: [Visual Agents as Fast and Slow Thinkers](https://proceedings.iclr.cc/paper_files/paper/2025/file/14fb70b97c70d5cc5445cd2d5bf818db-Paper-Conference.pdf))
> An evaluation protocol where GPT-4 is used to score model performance by comparing its generated answers to ground truth answers.

**GPT-4o Based Evaluation** (1 paper: [Magnetic Preference Optimization: Achieving Last-iterate Convergence for Language Model Alignment](https://proceedings.iclr.cc/paper_files/paper/2025/file/5833b4daf5b076dd1cdb362b163dff0c-Paper-Conference.pdf))
> A human-like evaluation procedure where the GPT-4o model is used to compare and rate the quality of responses from two different models on safety-related prompts.

**Llama-3-70B judge** (1 paper: [Jailbreaking Leading Safety-Aligned LLMs with Simple Adaptive Attacks](https://proceedings.iclr.cc/paper_files/paper/2025/file/63fa7efdd3bcf944a4bd6e0ff6a50041-Paper-Conference.pdf))
> An evaluation protocol that uses the Llama-3-70B model as a judge to assess the success of jailbreak attacks.

**LLM Judge** (1 paper: [Proactive Privacy Amnesia for Large Language Models: Safeguarding PII with Negligible Impact on Model Utility](https://proceedings.iclr.cc/paper_files/paper/2025/file/8c234d9c7e738a793947e0282c36eb95-Paper-Conference.pdf))
> An evaluation protocol that uses a powerful LLM, such as GPT-4o, to assess and score the quality of another model's generated content.

**GPT-4o-based evaluation** (5 papers: [Improving Instruction-Following in Language Models through Activation Steering](https://proceedings.iclr.cc/paper_files/paper/2025/file/8c3262a4c965ba9888f120d4f9e13478-Paper-Conference.pdf), [MME-CoT: Benchmarking Chain-of-Thought in Large Multimodal Models for Reasoning Quality, Robustness, and Efficiency](https://raw.githubusercontent.com/mlresearch/v267/main/assets/jiang25n/jiang25n.pdf), [Is Translation All You Need? A Study on Solving Multilingual Tasks with Large Language Models](https://aclanthology.org/2025.naacl-long.485.pdf), [K-COMP: Retrieval-Augmented Medical Domain Question Answering With Knowledge-Injected Compressor](https://aclanthology.org/2025.naacl-long.351.pdf), [LLMs as Meta-Reviewers' Assistants: A Case Study](https://aclanthology.org/2025.naacl-long.395.pdf))
> A GPT-4o-based human-like judging procedure in which GPT-4o generates yes/no questions about response quality and then answers them with rationales to score base-query responses.

**LLM judge** (2 papers: [On Speeding Up Language Model Evaluation](https://proceedings.iclr.cc/paper_files/paper/2025/file/a38cfba4c717e5a37b200294615e546e-Paper-Conference.pdf), [In Prospect and Retrospect: Reflective Memory Management for Long-term Personalized Dialogue Agents](https://aclanthology.org/2025.acl-long.413.pdf))
> A specific application of LLM-based scoring where a powerful LLM acts as an automated judge to evaluate model outputs.

**Llama-3 70B judge** (1 paper: [Does Refusal Training in LLMs Generalize to the Past Tense?](https://proceedings.iclr.cc/paper_files/paper/2025/file/d432fbe4877ee1a6a51632a18e69784f-Paper-Conference.pdf))
> A Llama-3 70B-based semantic judge used to evaluate whether responses satisfy the jailbreak criterion.

**LLM-based evaluation pipeline** (1 paper: [Dynamic-SUPERB Phase-2: A Collaboratively Expanding Benchmark for Measuring the Capabilities of Spoken Language Models with 180 Tasks](https://proceedings.iclr.cc/paper_files/paper/2025/file/ce1a7774429d5c06cc744ff4260a8e9f-Paper-Conference.pdf))
> An automated evaluation procedure that uses GPT-4o or LLaMA3.1-8b-Instruct to judge classification outputs and post-process regression outputs into task-compatible formats.

**External LLM evaluation** (1 paper: [Mechanistic Permutability: Match Features Across Layers](https://proceedings.iclr.cc/paper_files/paper/2025/file/d1422213c9f2bdd5178b77d166fba86a-Paper-Conference.pdf))
> A large-language-model-based semantic judgment procedure that labels matched feature descriptions as SAME, MAYBE, or DIFFERENT.

**GPT-assisted choice evaluation** (1 paper: [A-Bench: Are LMMs Masters at Evaluating AI-generated Images?](https://proceedings.iclr.cc/paper_files/paper/2025/file/d355518527578ce26b80da96e9fc2750-Paper-Conference.pdf))
> A technique used to automatically validate the correctness of LMM responses to multiple-choice questions by using a GPT model to handle variations in answer formatting.

**Success detector** (1 paper: [OMNI-EPIC: Open-endedness via Models of human Notions of Interestingness with Environments Programmed in Code](https://proceedings.iclr.cc/paper_files/paper/2025/file/d40d7cbe7210f8a13ea0149eeae9c6de-Paper-Conference.pdf))
> An LLM- or VLM-based procedure that checks whether an agent has successfully completed a generated task.

**Model of Interestingness** (1 paper: [OMNI-EPIC: Open-endedness via Models of human Notions of Interestingness with Environments Programmed in Code](https://proceedings.iclr.cc/paper_files/paper/2025/file/d40d7cbe7210f8a13ea0149eeae9c6de-Paper-Conference.pdf))
> An LLM-based evaluation procedure that judges whether a newly generated task is interesting relative to similar archived tasks.

**Automatic evaluation of explanations** (1 paper: [NL-Eye: Abductive NLI For Images](https://proceedings.iclr.cc/paper_files/paper/2025/file/d5aed68fde8e934d0ae4aadb57acc6c0-Paper-Conference.pdf))
> A reference-based evaluation procedure where a large language model acts as a judge to determine if a model-generated explanation aligns with a set of human-written gold reference explanations.

**LLM grader** (1 paper: [Rethinking and Improving Autoformalization: Towards a Faithful Metric and a Dependency Retrieval-based Approach](https://proceedings.iclr.cc/paper_files/paper/2025/file/d630537fc4402cfa3ebbc7450a0cac91-Paper-Conference.pdf))
> An LLM-based judging procedure that prompts a language model to determine equivalence between predicted and ground-truth formal statements.

**ChatGPT Evaluation** (2 papers: [Backdooring Vision-Language Models with Out-Of-Distribution Data](https://proceedings.iclr.cc/paper_files/paper/2025/file/da37068018f8f7185720b83ea6f48377-Paper-Conference.pdf), [Learnability Matters: Active Learning for Video Captioning](https://proceedings.neurips.cc/paper_files/paper/2024/file/43069caa6776eac8bca4bfd74d4a476d-Paper-Conference.pdf))
> An evaluation protocol that uses ChatGPT to provide judgments on the conceptual consistency of model outputs, serving as an automated proxy for human assessment.

**GPT-Eval** (1 paper: [Benchmarking Vision Language Model Unlearning via Fictitious Facial Identity Dataset](https://proceedings.iclr.cc/paper_files/paper/2025/file/dafb7f4ced9ac559e077fc611d6e96e5-Paper-Conference.pdf))
> An evaluation protocol that uses a large language model (GPT-4o mini) as a judge to score model outputs based on semantic criteria such as correctness, helpfulness, and relevance.

**Automatic evaluation with GPT-4** (1 paper: [Context Steering: Controllable Personalization at Inference Time](https://proceedings.iclr.cc/paper_files/paper/2025/file/db178cd03313e23cffb8937e93f0d464-Paper-Conference.pdf))
> An evaluation procedure that uses GPT-4 to rate or compare the outputs of other language models based on criteria like helpfulness and relevance.

**Mixture of judges** (1 paper: [Is Your Video Language Model a Reliable Judge?](https://proceedings.iclr.cc/paper_files/paper/2025/file/dc4f891373d19087d1ddda33e81e00e4-Paper-Conference.pdf))
> A reliability-gated evaluation procedure that selects a subset of VLM judges based on per-dimension reliability scores before producing a final assessment.

**Oracle-LLM-as-a-judge** (1 paper: [Measuring And Improving Persuasiveness Of Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/e0e956681b04ac126679e8c7dd706b2e-Paper-Conference.pdf))
> An automated evaluation protocol that uses a specially trained LLM (the "Oracle") to rate or compare the persuasive quality of generated content, serving as a proxy for human judgment.

**GPT-4 judge** (2 papers: [FairMT-Bench: Benchmarking Fairness for Multi-turn Dialogue in Conversational LLMs](https://proceedings.iclr.cc/paper_files/paper/2025/file/00d80722b756de0166523a87805dd00f-Paper-Conference.pdf), [MULTIVOX: A Benchmark for Evaluating Voice Assistants for Multimodal Interactions](https://aclanthology.org/2025.emnlp-main.1447.pdf))
> An LLM-as-judge evaluation procedure in which GPT-4 scores model generations using the full dialogue history and the original biased statement.

**GPT-4 judge evaluation** (1 paper: [The Belief State Transformer](https://proceedings.iclr.cc/paper_files/paper/2025/file/01b3dea1871f7cea1e0e6be1f2f085bc-Paper-Conference.pdf))
> An evaluation protocol where GPT-4 is used as a proxy for a human judge to compare and analyze stories generated by different models based on factors like grammar, flow, cohesiveness, and creativity.

**LLM-as-Judge** (3 papers: [Unlearning or Obfuscating? Jogging the Memory of Unlearned LLMs via Benign Relearning](https://proceedings.iclr.cc/paper_files/paper/2025/file/18fd48d9cbbf9a20e434c9d3db6973c5-Paper-Conference.pdf), [Afrispeech-Dialog: A Benchmark Dataset for Spontaneous English Conversations in Healthcare and Beyond](https://aclanthology.org/2025.naacl-long.426.pdf), [MCQG-SRefine: Multiple Choice Question Generation and Evaluation with Iterative Self-Critique, Correction, and Comparison Feedback](https://aclanthology.org/2025.naacl-long.538.pdf))
> A judge-model evaluation procedure that scores whether generated answers are relevant or appropriate for a query in the unlearning setting.

**GPT-4 Judge** (1 paper: [BadRobot: Jailbreaking Embodied LLM Agents in the Physical World](https://proceedings.iclr.cc/paper_files/paper/2025/file/5b2fa23e4ef0f7ac6c4f01d7998e6237-Paper-Conference.pdf))
> An evaluation protocol that uses the GPT-4 model to automatically assess and score the harmfulness of an embodied agent's linguistic and action outputs on a scale from 1 to 5.

**GPT-4 Judge Evaluation** (1 paper: [Unbounded: A Generative Infinite Game of Character Life Simulation](https://proceedings.iclr.cc/paper_files/paper/2025/file/da2411768acb844b255bb6770e5a71c7-Paper-Conference.pdf))
> An evaluation protocol where the GPT-4 model is used as an automated judge to score and compare the responses of two other models on criteria such as state update accuracy, environment relevance, story coherence, and instruction following.

**LLM-as-judge evaluation** (10 papers: [FormalAlign: Automated Alignment Evaluation for Autoformalization](https://proceedings.iclr.cc/paper_files/paper/2025/file/fceedf8c9c0ff51f41b9fe0294ef0070-Paper-Conference.pdf), [SimRAG: Self-Improving Retrieval-Augmented Generation for Adapting Large Language Models to Specialized Domains](https://aclanthology.org/2025.naacl-long.575.pdf), [When2Call: When (not) to Call Tools](https://aclanthology.org/2025.naacl-long.174.pdf), [Principled Content Selection to Generate Diverse and Personalized Multi-Document Summaries](https://aclanthology.org/2025.acl-long.1445.pdf), [SK-VQA: Synthetic Knowledge Generation at Scale for Training Context-Augmented Multimodal LLMs](https://raw.githubusercontent.com/mlresearch/v267/main/assets/su25a/su25a.pdf), [Fann or Flop: A Multigenre, Multiera Benchmark for Arabic Poetry Understanding in LLMs](https://aclanthology.org/2025.emnlp-main.1023.pdf), [SafeScientist: Enhancing AI Scientist Safety for Risk-Aware Scientific Discovery](https://aclanthology.org/2025.emnlp-main.116.pdf), [TableRAG: A Retrieval Augmented Generation Framework for Heterogeneous Document Reasoning](https://aclanthology.org/2025.emnlp-main.710.pdf), [Taming Text-to-Image Synthesis for Novices: User-centric Prompt Generation via Multi-turn Guidance](https://aclanthology.org/2025.emnlp-main.444.pdf), [VC4VG: Optimizing Video Captions for Text-to-Video Generation](https://aclanthology.org/2025.emnlp-main.59.pdf))
> A procedure where a large language model is used as a judge to evaluate the alignment between informal and formal mathematical statements.

**LLM evaluator** (1 paper: [Param$\Delta$ for Direct Mixing: Post-Train Large Language Model At Zero Cost](https://proceedings.iclr.cc/paper_files/paper/2025/file/78bca5cc621a0846cb1f8265e1927a2a-Paper-Conference.pdf))
> An evaluation protocol where a separate large language model is used to assess the quality or correctness of another model's outputs, often guided by a specific prompt and context.

**GPT-4 comparison** (1 paper: [TIS-DPO: Token-level Importance Sampling for Direct Preference Optimization With Estimated Weights](https://proceedings.iclr.cc/paper_files/paper/2025/file/7fb9f39075a5202472676a7531568212-Paper-Conference.pdf))
> A human-like pairwise comparison procedure in which GPT-4 compares outputs and determines win-rate.

**GPT-4 scoring** (2 papers: [IDA-VLM: Towards Movie Understanding via ID-Aware Large Vision-Language Model](https://proceedings.iclr.cc/paper_files/paper/2025/file/82dcb6da1b408d59d15f68afdebf1489-Paper-Conference.pdf), [SNS-Bench: Defining, Building, and Assessing Capabilities of Large Language Models in Social Networking Services](https://raw.githubusercontent.com/mlresearch/v267/main/assets/guo25o/guo25o.pdf))
> A human-readable scoring procedure in which GPT-4 rates open-ended question-answering and caption outputs against reference answers.

**ChatGPT-based evaluator** (1 paper: [From Exploration to Mastery: Enabling LLMs to Master Tools via Self-Driven Interactions](https://proceedings.iclr.cc/paper_files/paper/2025/file/8c22e5e918198702765ecff4b20d0a90-Paper-Conference.pdf))
> An automated evaluation procedure that uses a large language model (ChatGPT) to conduct pairwise comparisons of model outputs to determine a winner.

**Ref-GPT4** (1 paper: [Federated Residual Low-Rank Adaption of Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/906c860f1b7515a8ffec02dcdac74048-Paper-Conference.pdf))
> A benchmark in which GPT-4 rates generated responses for open-ended evaluation.

**Arena-Hard Judge** (1 paper: [JudgeBench: A Benchmark for Evaluating LLM-Based Judges](https://proceedings.iclr.cc/paper_files/paper/2025/file/9e720fce64f91114c49cfd640d821da3-Paper-Conference.pdf))
> A prompting method for LLM-based judges where the model is instructed to first generate its own reference answer before analyzing and judging the provided response pair.

**Vanilla judge** (1 paper: [JudgeBench: A Benchmark for Evaluating LLM-Based Judges](https://proceedings.iclr.cc/paper_files/paper/2025/file/9e720fce64f91114c49cfd640d821da3-Paper-Conference.pdf))
> A simple prompting method for LLM-based judges, adapted from AlpacaFarm, that directly asks the LLM to indicate its preferred response without requiring an explanation.

**Judge function** (1 paper: [EFFICIENT JAILBREAK ATTACK SEQUENCES ON LARGE LANGUAGE MODELS VIA MULTI-ARMED BANDIT-BASED CONTEXT SWITCHING](https://proceedings.iclr.cc/paper_files/paper/2025/file/52724c4ea3634f610b0ef0245ce5bd20-Paper-Conference.pdf))
> An automated evaluation procedure using a separate LLM (Llama-3.1-8B-Instruct) to assess a target model's response and assign a binary reward indicating whether the content is harmful (1) or benign (0).

**GPT-4o scoring** (2 papers: [Anyprefer: An Agentic Framework for Preference Data Synthesis](https://proceedings.iclr.cc/paper_files/paper/2025/file/56fbf5a2109a6c17372209c9fa698857-Paper-Conference.pdf), [On Understanding Attention-Based In-Context Learning for Categorical Data](https://raw.githubusercontent.com/mlresearch/v267/main/assets/wang25u/wang25u.pdf))
> A GPT-4o-based evaluation procedure that scores sampled preference data on a 1-to-10 scale for quality assessment.

**GPT-4o-mini judge** (1 paper: [Weak-to-Strong Preference Optimization: Stealing Reward from Weak Aligned Model](https://proceedings.iclr.cc/paper_files/paper/2025/file/5beb3a846137dd6524f2da17c97d9426-Paper-Conference.pdf))
> A judge-model evaluation procedure in which GPT-4o-mini is used to score or compare dialogue outputs.

**LLM-Eval** (1 paper: [Provence: efficient and robust context pruning for retrieval-augmented generation](https://proceedings.iclr.cc/paper_files/paper/2025/file/5e956fef0946dc1e39760f94b78045fe-Paper-Conference.pdf))
> An LLM-based evaluation procedure used to judge answer quality for generated responses in the RAG setting.

**Judge model evaluation** (1 paper: [Functional Homotopy: Smoothing Discrete Optimization via Continuous Parameters for LLM Jailbreak Attacks](https://proceedings.iclr.cc/paper_files/paper/2025/file/5ed212957dbe503283c577a94202cb8c-Paper-Conference.pdf))
> An evaluation procedure where a separate large language model (Llama-2 13B) is used to automatically assess whether a model's response to a prompt constitutes a successful jailbreak.

**GPT4o-mini judge** (1 paper: [PaCA: Partial Connection Adaptation for Efficient Fine-Tuning](https://proceedings.iclr.cc/paper_files/paper/2025/file/6b4fd4a4607f57fe65b5e276bdb17ed1-Paper-Conference.pdf))
> An evaluation protocol using the GPT4o-mini model to score or judge model outputs on benchmark tasks.

**Model-based parsers** (1 paper: [MixEval-X: Any-to-any Evaluations from Real-world Data Mixture](https://proceedings.iclr.cc/paper_files/paper/2025/file/6de2e84b8da47bb2eb5e2ac96c63d2b0-Paper-Conference.pdf))
> A grading procedure that uses language models to score responses against problem statements and reference answers.

**Claude 3 Opus Harmful-Yet-Helpful Score** (1 paper: [Failures to Find Transferable Image Jailbreaks Between Vision-Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/6e3daaeca6be8579573f69082b2dd58b-Paper-Conference.pdf))
> An evaluation procedure where the Claude 3 Opus model is prompted to assess and score the degree to which a VLM's generated output is both harmful and helpful.

**GPT4Score** (1 paper: [SeCom: On Memory Construction and Retrieval for Personalized Conversational Agents](https://proceedings.iclr.cc/paper_files/paper/2025/file/e56f394bbd4f0ec81393d767caa5a31b-Paper-Conference.pdf))
> An evaluation procedure where the GPT-4 model is prompted to assign an integer quality rating, from 0 (poor) to 100 (excellent), to a generated response.

**GPT Score** (1 paper: [DeepRTL: Bridging Verilog Understanding and Generation with a Unified Representation Model](https://proceedings.iclr.cc/paper_files/paper/2025/file/e9750610639c3e7a849cff746bf60dbd-Paper-Conference.pdf))
> An evaluation procedure that uses GPT-4 to quantify the semantic coherence between a generated description and a ground truth description by assigning a similarity score from 0 to 1.

**Automated evaluation** (1 paper: [Century: A Framework and Dataset for Evaluating Historical Contextualisation of Sensitive Images](https://proceedings.iclr.cc/paper_files/paper/2025/file/efc549c2d22edf2f244b7013387c6251-Paper-Conference.pdf))
> An evaluation protocol that uses foundation models as 'labellers' to produce ratings for the accuracy, thoroughness, and objectivity of responses generated by other target models.

**GPT-4o Judge** (1 paper: [ScienceAgentBench: Toward Rigorous Assessment of Language Agents for Data-Driven Scientific Discovery](https://proceedings.iclr.cc/paper_files/paper/2025/file/f12b4df26344f3be803c06b555252efe-Paper-Conference.pdf))
> A judge-based evaluation procedure using GPT-4o to compare a program-produced figure with the ground truth and rate figure quality.

**GPT-4 utility judge** (1 paper: [Language Models are Advanced Anonymizers](https://proceedings.iclr.cc/paper_files/paper/2025/file/f478b2e8ad9ff0756bf5b79fb31c330f-Paper-Conference.pdf))
> An automated evaluation protocol that uses the GPT-4 model to score the utility of anonymized text based on its readability and similarity in meaning to the original.

**LLM-as-Judge (LAJ)** (1 paper: [DELIFT: Data Efficient Language model Instruction Fine-Tuning](https://proceedings.iclr.cc/paper_files/paper/2025/file/f9d446812a6fdc05453f4093e54831e8-Paper-Conference.pdf))
> An evaluation protocol where a large language model is used to score the outputs of another model on a numeric scale based on criteria like correctness, clarity, and instruction adherence.

**Claude 3-as-a-Judge** (1 paper: [SeRA: Self-Reviewing and Alignment of LLMs using Implicit Reward Margins](https://proceedings.iclr.cc/paper_files/paper/2025/file/fdcf2565ea86530d65b3622c06d90841-Paper-Conference.pdf))
> A judge-based evaluation procedure in which Claude 3 compares model outputs or assigns ratings to assess response quality.

**GPT-4 evaluation** (16 papers: [Your Weak LLM is Secretly a Strong Teacher for Alignment](https://proceedings.iclr.cc/paper_files/paper/2025/file/332b4fbe322e11a71fa39d91c664d8fa-Paper-Conference.pdf), [Multimodal Cognitive Reframing Therapy via Multi-hop Psychotherapeutic Reasoning](https://aclanthology.org/2025.naacl-long.250.pdf), [PicPersona-TOD : A Dataset for Personalizing Utterance Style in Task-Oriented Dialogue with Image Persona](https://aclanthology.org/2025.naacl-long.403.pdf), [From Distributional to Overton Pluralism: Investigating Large Language Model Alignment](https://aclanthology.org/2025.naacl-long.346.pdf), [Instantly Learning Preference Alignment via In-context DPO](https://aclanthology.org/2025.naacl-long.8.pdf), [A Logical Fallacy-Informed Framework for Argument Generation](https://aclanthology.org/2025.naacl-long.374.pdf), [ToolFlow: Boosting LLM Tool-Calling Through Natural and Coherent Dialogue Synthesis](https://aclanthology.org/2025.naacl-long.214.pdf), [AdvisorQA: Towards Helpful and Harmless Advice-seeking Question Answering with Collective Intelligence](https://aclanthology.org/2025.naacl-long.333.pdf), [LLMs Can Simulate Standardized Patients via Agent Coevolution](https://aclanthology.org/2025.acl-long.846.pdf), [Adversaries Can Misuse Combinations of Safe Models](https://raw.githubusercontent.com/mlresearch/v267/main/assets/jones25a/jones25a.pdf), [Aligner: Efficient Alignment by Learning to Correct](https://proceedings.neurips.cc/paper_files/paper/2024/file/a51a74b2d71387dc71cc29181b5519bb-Paper-Conference.pdf), [Aligning Large Language Models with Representation Editing: A Control Perspective](https://proceedings.neurips.cc/paper_files/paper/2024/file/41bba7b0f5c81e789a20bb16a370aeeb-Paper-Conference.pdf), [EHRNoteQA: An LLM Benchmark for Real-World Clinical Practice Using Discharge Summaries](https://proceedings.neurips.cc/paper_files/paper/2024/file/e15c4afff22f12c4986c1fcb4e941e03-Paper-Datasets_and_Benchmarks_Track.pdf), [LoFiT: Localized Fine-tuning on LLM Representations](https://proceedings.neurips.cc/paper_files/paper/2024/file/122ea6470232ee5e79a2649243348005-Paper-Conference.pdf), [Preference Alignment with Flow Matching](https://proceedings.neurips.cc/paper_files/paper/2024/file/3df874367ce2c43891aab1ab23ae6959-Paper-Conference.pdf), [RoleAgent: Building, Interacting, and Benchmarking High-quality Role-Playing Agents from Scripts](https://proceedings.neurips.cc/paper_files/paper/2024/file/5875aca1ef70285a35940afbbce0f9fb-Paper-Datasets_and_Benchmarks_Track.pdf))
> An evaluation protocol that uses the GPT-4 model as a proxy for human judgment to assess and compare the quality of responses generated by other models.

**GPT-4 eval** (1 paper: [Aligning Language Models with Demonstrated Feedback](https://proceedings.iclr.cc/paper_files/paper/2025/file/349a45f211fb1b3850da1ccd829e869e-Paper-Conference.pdf))
> An automatic evaluation protocol where GPT-4 is prompted to select which of two generated texts more closely matches the style of a reference text, with results averaged over swapped orders to mitigate bias.

**GPT-4o Score** (1 paper: [ChartMimic: Evaluating LMM's Cross-Modal Reasoning Capability via Chart-to-Code Generation](https://proceedings.iclr.cc/paper_files/paper/2025/file/42806406dd99e30c3796bc98b2670fa2-Paper-Conference.pdf))
> An evaluation procedure that uses the GPT-4o model to assess the high-level visual similarity between a generated chart and a ground-truth chart, producing a score from 0 to 100.

**GPT-4 pairwise evaluation** (1 paper: [MA-RLHF: Reinforcement Learning from Human Feedback with Macro Actions](https://proceedings.iclr.cc/paper_files/paper/2025/file/429d69979c22b06d6baa65caf3ab1e10-Paper-Conference.pdf))
> A human-like pairwise judgment procedure in which GPT-4 compares two responses and selects a winner based on task-specific criteria.

**GPT-4 assisted evaluation** (1 paper: [Intervening Anchor Token: Decoding Strategy in Alleviating Hallucinations for MLLMs](https://proceedings.iclr.cc/paper_files/paper/2025/file/4537e2172096d966228d68c428392894-Paper-Conference.pdf))
> A human-in-the-loop style evaluation procedure in which GPT-4 judges hallucinations in generated image descriptions sentence by sentence against detailed ground truth.

**LLM-based auto-evaluation** (1 paper: [FaithEval: Can Your Language Model Stay Faithful to Context, Even If "The Moon is Made of Marshmallows"](https://proceedings.iclr.cc/paper_files/paper/2025/file/48404cd9ce03946c6b7177691f3267a1-Paper-Conference.pdf))
> A validation procedure where an LLM judge is used to automatically verify the quality of a generated context by checking if a specific answer is both valid and uniquely supported by that context.

**LMExaminer** (1 paper: [Benchmarking LLMs' Judgments with No Gold Standard](https://proceedings.iclr.cc/paper_files/paper/2025/file/a9b0e4e205bdf232da9f74bfb9469539-Paper-Conference.pdf))
> An evaluation protocol where a large language model (e.g., GPT-4o) is used as an oracle to directly score the quality of another model's generated text.

**GPT-4o evaluation protocol** (1 paper: [Amulet: ReAlignment During Test Time for Personalized Preference Adaptation of LLMs](https://proceedings.iclr.cc/paper_files/paper/2025/file/b7c43d4a79dede363a2d061c6158e5a5-Paper-Conference.pdf))
> An evaluation procedure where GPT-4o acts as a discriminator to compare pairs of model responses based on user preferences, categorizing outcomes as win, lose, or tie.

**Model-based verifier** (1 paper: [SysBench: Can LLMs Follow System Message?](https://proceedings.iclr.cc/paper_files/paper/2025/file/b917f916e7eed84ffe8f5e63492b2be8-Paper-Conference.pdf))
> An evaluation protocol that uses an advanced LLM (like GPT-4o) as a judge to automatically assess whether a model's response satisfies the constraints defined in a system message, guided by a manually created checklist.

**GPT-4 judgment** (1 paper: [PAD: Personalized Alignment of LLMs at Decoding-time](https://proceedings.iclr.cc/paper_files/paper/2025/file/196c8da9209b1977408d8771c4e7ee56-Paper-Conference.pdf))
> An evaluation procedure leveraging GPT-4 to conduct judgments towards certain personalized preferences and report comparative win rates.

**Procedural LLM-based grading** (1 paper: [HARDMath: A Benchmark Dataset for Challenging Problems in Applied Mathematics](https://proceedings.iclr.cc/paper_files/paper/2025/file/23d64d26abb5a0e9f2014cfcc700f82a-Paper-Conference.pdf))
> An evaluation protocol that uses an LLM (e.g., GPT-4o) as a grader to assess the correctness of intermediate steps in a model's solution procedure, based on a provided answer key and rubric.

**GPT-4 based evaluation** (3 papers: [Collab: Controlled Decoding using Mixture of Agents for LLM Alignment](https://proceedings.iclr.cc/paper_files/paper/2025/file/2e79dce47c5bbe738dff9c05ace8a037-Paper-Conference.pdf), [InfoPO: On Mutual Information Maximization for Large Language Model Alignment](https://aclanthology.org/2025.naacl-long.585.pdf), [Transfer Q-star : Principled Decoding for LLM Alignment](https://proceedings.neurips.cc/paper_files/paper/2024/file/b8700a8a005032fe869c741b0a75274b-Paper-Conference.pdf))
> An evaluation protocol where the GPT-4 model is used as a surrogate for human judgment to rate and compare model-generated responses based on criteria like relevance, accuracy, and helpfulness.

**GPT-4-based evaluation** (2 papers: [MMWorld: Towards Multi-discipline Multi-faceted World Model Evaluation in Videos](https://proceedings.iclr.cc/paper_files/paper/2025/file/4364fef031fdf7bfd9d1c9c56b287084-Paper-Conference.pdf), [SparseLoRA: Accelerating LLM Fine-Tuning with Contextual Sparsity](https://raw.githubusercontent.com/mlresearch/v267/main/assets/khaki25a/khaki25a.pdf))
> An evaluation protocol where a large language model (GPT-4) is used as a judge to determine if a model's generated answer is correct.

**GPT-4o evaluation** (2 papers: [A Distributional Approach to Uncertainty-Aware Preference Alignment Using Offline Demonstrations](https://proceedings.iclr.cc/paper_files/paper/2025/file/084cf2b3d73abafa1705336a0e9ebb1c-Paper-Conference.pdf), [ReLearn: Unlearning via Learning for Large Language Models](https://aclanthology.org/2025.acl-long.297.pdf))
> An automated evaluation procedure using GPT-4o to assess model safety and quality on test samples.

**GPT-4o assisted evaluation** (3 papers: [MLLM can see? Dynamic Correction Decoding for Hallucination Mitigation](https://proceedings.iclr.cc/paper_files/paper/2025/file/24079b91da7257cb78805262996152b8-Paper-Conference.pdf), [SHARE: Shared Memory-Aware Open-Domain Long-Term Dialogue Dataset Constructed from Movie Script](https://aclanthology.org/2025.acl-long.704.pdf), [Mitigating Hallucinations in Vision-Language Models through Image-Guided Head Suppression](https://aclanthology.org/2025.emnlp-main.631.pdf))
> An open-ended evaluation protocol where the GPT-4o model is used to assess and score model-generated image descriptions based on criteria such as accuracy, detailedness, and coherence.

**LLM-as-judge relevance assessment** (1 paper: [From Models to Microtheories: Distilling a Model's Topical Knowledge for Grounded Question-Answering](https://proceedings.iclr.cc/paper_files/paper/2025/file/77d52754ff6b2de5a5d96ee921b6b3cd-Paper-Conference.pdf))
> An automatic evaluation protocol that uses an LLM as a judge to score the relevance of a fact to a question on a 0-5 scale, based on an existing rubric.

**MLLM-as-a-Judge** (1 paper: [Interleaved Scene Graphs for Interleaved Text-and-Image Generation Assessment](https://proceedings.iclr.cc/paper_files/paper/2025/file/b9e0ceee9751ae8b5c6603c029e4ca42-Paper-Conference.pdf))
> A human-aligned evaluation protocol in which a multimodal large language model judges the overall quality of generated responses, sometimes using golden answers and chain-of-thought prompting.

**LLMs as Judges** (1 paper: [Beyond Dialogue: A Profile-Dialogue Alignment Framework Towards General Role-Playing Language Model](https://aclanthology.org/2025.acl-long.586.pdf))
> An automated evaluation protocol where large language models assess dialogue quality across multiple dimensions using standardized prompts, serving as objective and scalable judges.

**Model-as-Judge** (1 paper: [MAmmoTH-VL: Eliciting Multimodal Reasoning with Instruction Tuning at Scale](https://aclanthology.org/2025.acl-long.680.pdf))
> Automated evaluation method using a large model to assess the logical consistency and quality of question-answer pairs against visual inputs, used for filtering hallucinated content.

**GPT Judge** (1 paper: [AGD: Adversarial Game Defense Against Jailbreak Attacks in Large Language Models](https://aclanthology.org/2025.acl-long.851.pdf))
> An evaluation protocol (Qi et al., 2023) that uses GPT-4 to assess the harmfulness of model responses by assigning a rating on a 1-to-5 scale.

**Large-scale pairwise comparison** (1 paper: [It's Not Bragging If You Can Back It Up: Can LLMs Understand Braggings?](https://aclanthology.org/2025.acl-long.858.pdf))
> An automated evaluation method where a powerful LLM (GPT-4) acts as a judge to compare an LLM-generated explanation against a human-written gold standard and select the better one.

**GPT-4o judge** (1 paper: [LLMs know their vulnerabilities: Uncover Safety Gaps through Natural Distribution Shifts](https://aclanthology.org/2025.acl-long.1207.pdf))
> A robust evaluation method using GPT-4o to assess whether model outputs are harmful, leveraging its strong reasoning and content moderation capabilities as a proxy for human judgment.

**Gemini 1.0 Ultra evaluation** (1 paper: [Design Considerations in Offline Preference-based RL](https://raw.githubusercontent.com/mlresearch/v267/main/assets/agarwal25a/agarwal25a.pdf))
> An evaluation protocol where a prompted Gemini 1.0 Ultra model is used to compare the quality and conciseness of generated summaries against a baseline policy.

**Preference-Similarity** (1 paper: [Aligning LLMs by Predicting Preferences from User Writing Samples](https://raw.githubusercontent.com/mlresearch/v267/main/assets/aroca-ouellette25a/aroca-ouellette25a.pdf))
> An LLM-as-a-Judge protocol that measures preference quality by prompting an LLM to rate the similarity between an inferred preference description and a true preference description on a 5-point Likert scale.

**Comparative evaluation** (1 paper: [Autoformulation of Mathematical Optimization Models Using LLMs](https://raw.githubusercontent.com/mlresearch/v267/main/assets/astorga25a/astorga25a.pdf))
> LLM-based evaluation method where candidate formulations are scored relative to baseline models to produce a consistent reward signal for correctness.

**GPT-4o-based judge** (1 paper: [Emergent Misalignment: Narrow finetuning can produce broadly misaligned LLMs](https://raw.githubusercontent.com/mlresearch/v267/main/assets/betley25a/betley25a.pdf))
> A GPT-4o-based automated evaluation procedure that scores responses for alignment with human values and coherence, and classifies responses as misaligned under specified thresholds.

**Knowledge Capability** (1 paper: [SEFE: Superficial and Essential Forgetting Eliminator for Multimodal Continual Instruction Tuning](https://raw.githubusercontent.com/mlresearch/v267/main/assets/chen25n/chen25n.pdf))
> Evaluation component in CoIN that uses a large language model (Qwen1.5-32B) to assess the factual correctness of model answers, particularly useful when answers are in non-standard formats.

**Agents-as-an-Evaluator** (1 paper: [Unbiased Evaluation of Large Language Models from a Causal Perspective](https://raw.githubusercontent.com/mlresearch/v267/main/assets/chen25bi/chen25bi.pdf))
> An LLM-based evaluation paradigm where language models generate and rephrase evaluation questions and criteria, potentially introducing data and model bias.

**GPT score** (1 paper: [De-mark: Watermark Removal in Large Language Models](https://raw.githubusercontent.com/mlresearch/v267/main/assets/chen25bq/chen25bq.pdf))
> An evaluation procedure that uses a separate, powerful language model (such as gpt-3.5-turbo-0125) to assess the quality of text generated by another model.

**Ensemble-as-Judges** (1 paper: [From Crowdsourced Data to High-quality Benchmarks: Arena-Hard and Benchbuilder Pipeline](https://raw.githubusercontent.com/mlresearch/v267/main/assets/li25h/li25h.pdf))
> Evaluation method that aggregates judgments from multiple LLM judges (e.g., GPT-4-Turbo and Gemini-1.5-Pro) to reduce individual model biases and improve alignment with human preferences.

**GPT-4 based autograder** (1 paper: [Eliciting Language Model Behaviors with Investigator Agents](https://raw.githubusercontent.com/mlresearch/v267/main/assets/li25i/li25i.pdf))
> A specific LLM-as-judge implementation that uses GPT-4 to automatically evaluate the success of attacks in generating harmful behaviors.

**GPT-4-based evaluator** (1 paper: [Test-Time Preference Optimization: On-the-Fly Alignment via Iterative Textual Feedback](https://raw.githubusercontent.com/mlresearch/v267/main/assets/li25ac/li25ac.pdf))
> An evaluation protocol that uses GPT-4 to perform pairwise comparisons and determine a win-rate between the outputs of different models on a given set of prompts.

**GPT-4o automated judge** (1 paper: [One Example Shown, Many Concepts Known! Counterexample-Driven Conceptual Reasoning in Mathematical LLMs](https://raw.githubusercontent.com/mlresearch/v267/main/assets/li25ax/li25ax.pdf))
> An evaluation framework using GPT-4o to automatically assess whether model-generated examples align with reference examples in logical structure, problem decomposition, and goal relevance.

**GPT-4V evaluation** (1 paper: [What If We Recaption Billions of Web Images with LLaMA-3?](https://raw.githubusercontent.com/mlresearch/v267/main/assets/li25ch/li25ch.pdf))
> Human-like evaluation using GPT-4V to rate caption quality and alignment with images on a 1–5 scale based on fluency and correctness.

**LLM Evaluator** (1 paper: [Bootstrapping Self-Improvement of Language Model Programs for Zero-Shot Schema Matching](https://raw.githubusercontent.com/mlresearch/v267/main/assets/seedat25a/seedat25a.pdf))
> A validation method that uses a separate language model to score the relevance of schema matches on a numerical scale, guiding a zero-shot optimization process.

**GPT4-as-a-judge** (1 paper: [Reliable and Efficient Amortized Model-based Evaluation](https://raw.githubusercontent.com/mlresearch/v267/main/assets/truong25c/truong25c.pdf))
> An evaluation procedure where a high-performance language model (GPT-4) is used to dichotomously grade the responses of other models.

**LLM-based grading** (1 paper: [Generalized Interpolating Discrete Diffusion](https://raw.githubusercontent.com/mlresearch/v267/main/assets/von-rutte25a/von-rutte25a.pdf))
> An evaluation protocol where a large language model (GPT-4o in this paper) is used to rate the quality of generated samples on several qualitative dimensions like clarity and factuality.

**LLM judge evaluation** (3 papers: [CollabLLM: From Passive Responders to Active Collaborators](https://raw.githubusercontent.com/mlresearch/v267/main/assets/wu25i/wu25i.pdf), [FaST: Feature-aware Sampling and Tuning for Personalized Preference Alignment with Limited Data](https://aclanthology.org/2025.emnlp-main.475.pdf), [From Problem-Solving to Teaching Problem-Solving: Aligning LLMs with Pedagogy using Reinforcement Learning](https://aclanthology.org/2025.emnlp-main.15.pdf))
> Automated assessment using LLMs (e.g., Claude-3.5-Sonnet) to score interactivity and task success on a 0–1 scale based on conversation quality.

**GPT-based evaluation** (4 papers: [FlipAttack: Jailbreak LLMs via Flipping](https://raw.githubusercontent.com/mlresearch/v267/main/assets/liu25z/liu25z.pdf), [MMRC: A Large-Scale Benchmark for Understanding Multimodal Large Language Model in Real-World Conversation](https://aclanthology.org/2025.acl-long.1096.pdf), [$E^3$: Exploring Embodied Emotion Through A Large-Scale Egocentric Video Dataset](https://proceedings.neurips.cc/paper_files/paper/2024/file/d611d5c0251d9680f869c5d2c46c6fcd-Paper-Datasets_and_Benchmarks_Track.pdf), [Cracking the Code of Juxtaposition: Can AI Models Understand the Humorous Contradictions](https://proceedings.neurips.cc/paper_files/paper/2024/file/540a6eefb60428c8547a27253f9a2a59-Paper-Conference.pdf))
> Evaluation method using a strong LLM (e.g., GPT-4) to score model responses on rejection status, completion of harmful request, and illegal/unsafe output.

**Claude Sonnet API evaluation** (1 paper: [Progressively Label Enhancement for Large Language Model Alignment](https://raw.githubusercontent.com/mlresearch/v267/main/assets/liu25cg/liu25cg.pdf))
> An API-based pairwise evaluation procedure using Claude Sonnet to judge which of two model responses is better, with position swapping to reduce bias.

**Claude-3.5-Sonnet Evaluation** (1 paper: [The Energy Loss Phenomenon in RLHF: A New Perspective on Mitigating Reward Hacking](https://raw.githubusercontent.com/mlresearch/v267/main/assets/miao25c/miao25c.pdf))
> An evaluation protocol where the Claude-3.5-Sonnet model is used as an automated judge to assess the quality of model responses.

**Model-as-judge evaluation** (1 paper: [Understanding the Logic of Direct Preference Alignment through Logic](https://raw.githubusercontent.com/mlresearch/v267/main/assets/richardson25a/richardson25a.pdf))
> Human evaluation protocol adapted from Hong et al. (2024) where a large language model acts as a judge to compare outputs from models trained with different losses.

**LLM-Judge** (1 paper: [Optimizing Adaptive Attacks against Watermarks for Language Models](https://raw.githubusercontent.com/mlresearch/v267/main/assets/diaa25a/diaa25a.pdf))
> An automated evaluation metric that uses a large language model to assess the quality of paraphrased text relative to the original, providing a score based on semantic fidelity and fluency.

**GPT-4 complexity estimation** (1 paper: [Understanding Complexity in VideoQA via Visual Program Generation](https://raw.githubusercontent.com/mlresearch/v267/main/assets/eyzaguirre25a/eyzaguirre25a.pdf))
> Prompt-based evaluation using GPT-4 to estimate question complexity on a Likert scale, serving as a text-based baseline for comparison.

**LLM-based Judge** (1 paper: [Dialogue Without Limits: Constant-Sized KV Caches for Extended Response in LLMs](https://raw.githubusercontent.com/mlresearch/v267/main/assets/ghadia25a/ghadia25a.pdf))
> Evaluation protocol using a large language model (Mistral-Large-123B) to score generated responses across multiple quality criteria, aggregating them into a final performance metric.

**Generative-Judge** (1 paper: [Cannot See the Forest for the Trees: Invoking Heuristics and Biases to Elicit Irrational Choices of LLMs](https://raw.githubusercontent.com/mlresearch/v267/main/assets/yang25s/yang25s.pdf))
> Automated evaluation method using a strong LLM (e.g., GPT-4-turbo) to judge whether model outputs contain harmful content and thus count as successful jailbreaks.

**LLM-as-Prompt-Judge** (1 paper: [R.I.P.: Better Models by Survival of the Fittest Prompts](https://raw.githubusercontent.com/mlresearch/v267/main/assets/yu25u/yu25u.pdf))
> An evaluation protocol where a powerful language model is used to assess the quality of input prompts on a binary or pointwise scale.

**Oracle judge model** (1 paper: [Preference learning made easy: Everything should be understood through win rate](https://raw.githubusercontent.com/mlresearch/v267/main/assets/zhang25bm/zhang25bm.pdf))
> A trained model used to estimate the true preference probability p(ℓ= 1 | x, y0, y1) by relabeling preference annotations, serving as a proxy for human judgment in evaluating win rate.

**GPT-4 preference analysis** (1 paper: [Controlled Text Generation via Language Model Arithmetic](https://proceedings.iclr.cc/paper_files/paper/2024/file/96aad3299d18497e2bea4fc20b949b81-Paper-Conference.pdf))
> A human-like comparative evaluation procedure in which GPT-4 chooses the best response in terms of toxicity and relevance.

**GPT-4 as a judge** (2 papers: [Compressing LLMs: The Truth is Rarely Pure and Never Simple](https://proceedings.iclr.cc/paper_files/paper/2024/file/9f09f316a3eaf59d9ced5ffaefe97e0f-Paper-Conference.pdf), [ComPO: Community Preferences for Language Model Personalization](https://aclanthology.org/2025.naacl-long.419.pdf))
> An evaluation protocol where the GPT-4 model is prompted to rate and compare the quality of answers generated by other models on a numeric scale.

**GPT-ranking** (1 paper: [Hybrid LLM: Cost-Efficient and Quality-Aware Query Routing](https://proceedings.iclr.cc/paper_files/paper/2024/file/b47d93c99fa22ac0b377578af0a1f63a-Paper-Conference.pdf))
> An evaluation method that uses a large language model, such as GPT-4, to provide relative quality rankings between pairs of generated text outputs.

**LLM-as-a-judge evaluation** (2 papers: [Frictional Agent Alignment Framework: Slow Down and Don't Break Things](https://aclanthology.org/2025.acl-long.542.pdf), [WizardArena: Post-training Large Language Models via Simulated Offline Chatbot Arena](https://proceedings.neurips.cc/paper_files/paper/2024/file/ca4aa9acc097e0f606af55bf986cb031-Paper-Conference.pdf))
> Evaluation method using GPT-4o as a judge to score and compare model-generated friction interventions across seven dimensions including thought-provoking, actionability, and relevance.

**Google Gemini evaluation pipeline** (1 paper: [Towards Controllable Speech Synthesis in the Era of Large Language Models: A Systematic Survey](https://aclanthology.org/2025.emnlp-main.40.pdf))
> A model-based evaluation pipeline using Google Gemini to assess synthesized speech on dimensions such as instruction following, naturalness, and expressiveness.

**DeepSeek R1 evaluation** (1 paper: [Theorem-Validated Reverse Chain-of-Thought Problem Generation for Geometric Reasoning](https://aclanthology.org/2025.emnlp-main.38.pdf))
> An evaluation protocol where the DeepSeek R1 model is used to quantitatively assess model outputs on qualitative criteria such as logical consistency and clarity.

**ERNIE Bot 4.0 evaluation** (1 paper: [Theorem-Validated Reverse Chain-of-Thought Problem Generation for Geometric Reasoning](https://aclanthology.org/2025.emnlp-main.38.pdf))
> An evaluation protocol where the ERNIE Bot 4.0 model is used to automatically score the correctness of model predictions against ground truth answers.

**VLM-as-a-Judge** (1 paper: [EQA-RM: A Generative Embodied Reward Model with Test-time Scaling](https://aclanthology.org/2025.emnlp-main.48.pdf))
> A prompting-based evaluation procedure in which vision-language models are used offline to judge EQA responses.

**LLM-assisted evaluation** (1 paper: [MovieCORE: COgnitive REasoning in Movies](https://aclanthology.org/2025.emnlp-main.66.pdf))
> An evaluation scheme where an LLM (GPT-4o-mini) is prompted to score model-generated answers on a scale from 0 to 5 across multiple criteria, including depth, comprehensiveness, coherence, and evidence.

**Bias Judge** (1 paper: [CoBia: Constructed Conversations Can Trigger Otherwise Concealed Societal Biases in LLMs](https://aclanthology.org/2025.emnlp-main.84.pdf))
> An LLM-as-a-judge system that assesses whether a model's response agrees with a biased opinion, considering both direct and implicit bias while excluding explicit rejections of bias.

**NLI Judge** (1 paper: [CoBia: Constructed Conversations Can Trigger Otherwise Concealed Societal Biases in LLMs](https://aclanthology.org/2025.emnlp-main.84.pdf))
> A natural language inference-based evaluation method that classifies the logical relationship between a biased opinion and the model's output as enforces, agrees, neutral, or negates, used to assess bias in model responses.

**LLM Judge Scores** (1 paper: [Alignment Quality Index (AQI) : Beyond Refusals: AQI as an Intrinsic Alignment Diagnostic via Latent Geometry, Cluster Divergence, and Layer wise Pooled Representations](https://aclanthology.org/2025.emnlp-main.145.pdf))
> Model preference comparison scores derived from human-aligned rubrics, used to evaluate the behavioral alignment of model outputs based on comparative judgments.

**LM judge evaluation** (1 paper: [reWordBench: Benchmarking and Improving the Robustness of Reward Models with Transformed Inputs](https://aclanthology.org/2025.emnlp-main.167.pdf))
> An automatic evaluation protocol where a state-of-the-art language model is prompted to judge which of two model-generated responses is preferred, with the results aggregated into a win rate.

**LLM self-judge** (1 paper: [Are Generative Models Underconfident? Better Quality Estimation with Boosted Model Probability](https://aclanthology.org/2025.emnlp-main.166.pdf))
> A method where a large language model is prompted to assign a quality score to its own output, requiring an additional inference step.

**GPT-4o Judgements** (1 paper: [MultiAgentESC: A LLM-based Multi-Agent Collaboration Framework for Emotional Support Conversation](https://aclanthology.org/2025.emnlp-main.232.pdf))
> An evaluation procedure using the GPT-4o model to score the performance of different methods on five aspects: Fluency, Identification, Comforting, Suggestion, and Overall.

**GPT-4o-mini Evaluator** (1 paper: [DMDTEval: An Evaluation and Analysis of LLMs on Disambiguation in Multi-domain Translation](https://aclanthology.org/2025.emnlp-main.309.pdf))
> An evaluation procedure that uses the GPT-4o-mini model with a specific prompt to assess the disambiguation capability of other LLMs.

**LLM-as-judge evaluator** (1 paper: [Keep Security! Benchmarking Security Policy Preservation in Large Language Model Contexts Against Indirect Attacks in Question Answering](https://aclanthology.org/2025.emnlp-main.345.pdf))
> An automated evaluation method using an LLM (GPT-4.1) to judge whether model outputs leak confidential information or faithfully include non-confidential content, based on predefined policy targets and discussion summaries.

**MLLM-as-a-judge** (1 paper: [ViLBench: A Suite for Vision-Language Process Reward Modeling](https://aclanthology.org/2025.emnlp-main.344.pdf))
> An evaluation paradigm where a Vision Large Language Model is used as an automated judge to score or critique the outputs of other models.

**GPT-4o model-based assessment** (1 paper: [ViDoRAG: Visual Document Retrieval-Augmented Generation via Dynamic Iterative Reasoning Agents](https://aclanthology.org/2025.emnlp-main.464.pdf))
> An evaluation protocol using GPT-4o to score model responses on a 1–5 scale by comparing them to reference answers, with scores ≥4 considered correct.

**GPT-4o-based evaluation framework** (1 paper: [Plan Dynamically, Express Rhetorically: A Debate-Driven Rhetorical Framework for Argumentative Writing](https://aclanthology.org/2025.emnlp-main.483.pdf))
> A GPT-4o-based automatic evaluation procedure that scores generated essays along multiple qualitative dimensions using detailed feedback before scoring.

**GPT-eval** (1 paper: [CIFLEX: Contextual Instruction Flow for Sub-task Execution in Multi-Turn Interactions with a Single On-Device LLM](https://aclanthology.org/2025.emnlp-main.533.pdf))
> An evaluation protocol that uses a large language model (GPT) to assess the quality of generated text on dimensions like coherence and correctness.

**LLM-as-Evaluator** (1 paper: [Long-Form Information Alignment Evaluation Beyond Atomic Facts](https://aclanthology.org/2025.emnlp-main.558.pdf))
> A general evaluation methodology where a large language model is prompted to directly score or assess the quality of a generated text based on given criteria.

**LLM-as-a-Meta-Judge** (1 paper: [Meta-Rewarding Language Models: Self-Improving Alignment with LLM-as-a-Meta-Judge](https://aclanthology.org/2025.emnlp-main.583.pdf))
> A prompting-based evaluation procedure in which an LLM compares two judgments and selects the more accurate one according to a rubric.

**LLM-based Simulated Evaluation** (1 paper: [AskToAct: Enhancing LLMs Tool Use via Self-Correcting Clarification](https://aclanthology.org/2025.emnlp-main.682.pdf))
> An automated evaluation framework where an LLM simulates user behavior to systematically assess a model's performance in handling unspecified queries.

**LLM-based alignment evaluation** (1 paper: [TreeReview: A Dynamic Tree of Questions Framework for Deep and Efficient LLM-based Scientific Peer Review](https://aclanthology.org/2025.emnlp-main.790.pdf))
> An automatic evaluation procedure where an LLM (Gemini-2.5-Pro) performs a many-to-many matching between generated and reference feedback comments to assess alignment.

**RAG-AS-A-JUDGE** (1 paper: [Med-PRM: Medical Reasoning Models with Stepwise, Guideline-verified Process Rewards](https://aclanthology.org/2025.emnlp-main.837.pdf))
> An evaluation procedure where a large language model, conditioned on retrieved documents, performs binary classification on each step of a reasoning trace to determine its correctness.

**GPT-4o judge evaluation** (1 paper: [3DS: Medical Domain Adaptation of LLMs via Decomposed Difficulty-based Data Selection](https://aclanthology.org/2025.emnlp-main.983.pdf))
> Pair-wise comparison using GPT-4o as an automated judge to assess model outputs on coherence, relevance, and quality in open-ended tasks.

**GPT-4.1 mini re-evaluation** (1 paper: [Table-R1: Inference-Time Scaling for Table Reasoning Tasks](https://aclanthology.org/2025.emnlp-main.1040.pdf))
> An automated evaluation procedure where responses marked as incorrect by exact match are re-evaluated by the GPT-4.1 mini model to account for formatting variations or semantic equivalence.

**CUA-as-a-Judge** (1 paper: [FlashAdventure: A Benchmark for GUI Agents Solving Full Story Arcs in Diverse Adventure Games](https://aclanthology.org/2025.emnlp-main.1192.pdf))
> Automated gameplay evaluator implemented using Claude-3.7-Sonnet that verifies milestone completion by interacting with the game environment as an oracle.

**LLM Judger** (1 paper: [Video2Roleplay: A Multimodal Dataset and Framework for Video-Guided Role-playing Agents](https://aclanthology.org/2025.emnlp-main.1209.pdf))
> An automated evaluation method using large language models (e.g., GPT-4o) to score model responses across multiple role-playing metrics, with temperature set to 0.0 and multiple rounds averaged.

**OpenAI-o3 evaluation** (1 paper: [Code Execution as Grounded Supervision for LLM Reasoning](https://aclanthology.org/2025.emnlp-main.1260.pdf))
> An evaluation procedure where a strong reasoning model (OpenAI-o3) is used to identify errors within the intermediate steps of a generated reasoning process.

**LLM-based story evaluator** (1 paper: [Beyond Outlining: Heterogeneous Recursive Planning for Adaptive Long-form Writing with Language Models](https://aclanthology.org/2025.emnlp-main.1254.pdf))
> An evaluation protocol where an LLM (Gemini 2.0-Flash) performs pairwise comparisons of generated stories to determine superiority across dimensions like plot, creativity, and language use.

**Dic-Judge** (1 paper: [Reasoning-to-Defend: Safety-Aware Reasoning Can Defend Large Language Models from Jailbreaking](https://aclanthology.org/2025.emnlp-main.1493.pdf))
> An automated judge used to classify model responses into categories like 'Full Refusal' or 'Full Compliance' for over-refusal analysis.

**GPT-as-a-Judge** (1 paper: [SCRIBE: Structured Chain Reasoning for Interactive Behaviour Explanations using Tool Calling](https://aclanthology.org/2025.emnlp-main.1490.pdf))
> Automated evaluation protocol using GPT-4.1 as a judge to assess model responses on criteria including relevance, actionability, tool relevance, spelling and grammar, and correctness, based on a structured rubric and chain-of-thought prompting.

**LLM-based judge** (1 paper: [Where Confabulation Lives: Latent Feature Discovery in LLMs](https://aclanthology.org/2025.emnlp-main.1515.pdf))
> A few-shot prompted language-model judge used to label open-ended generations as containing invented information or as refusals/confessions of ignorance.

**LLM-based Behavior Classification** (1 paper: [Implicit Behavioral Alignment of Language Agents in High-Stakes Crowd Simulations](https://aclanthology.org/2025.emnlp-main.1562.pdf))
> A procedure using gpt-4.1 as a deterministic classifier to map agent state-action trajectories into discrete behavior labels via chain-of-thought prompting.

**LLM-based safety moderator** (1 paper: [Are Vision-Language Models Safe in the Wild? A Meme-Based Benchmark Study](https://aclanthology.org/2025.emnlp-main.1555.pdf))
> Automated evaluation using LLMs (e.g., GPT-4o, GPT-4o-mini) to classify model responses along safety dimensions such as harmfulness, refusal, and task completion.

**Automated LLM-based evaluation framework** (1 paper: [Text2Vis: A Challenging and Diverse Benchmark for Generating Multimodal Visualizations from Text](https://aclanthology.org/2025.emnlp-main.1622.pdf))
> A scalable evaluation pipeline that uses an LLM judge (e.g., GPT-4o) to systematically assess answer correctness, code execution success, visualization readability, and chart accuracy without human annotation.

**LM-as-a-judge** (1 paper: [CARE: Multilingual Human Preference Learning for Cultural Awareness](https://aclanthology.org/2025.emnlp-main.1669.pdf))
> An evaluation protocol in which GPT-4o is prompted to generate a rationale and assign a 1–10 score to model responses relative to human references.

**LLM-based Classical Poetry Metric** (1 paper: [Benchmarking LLMs for Translating Classical Chinese Poetry: Evaluating Adequacy, Fluency, and Elegance](https://aclanthology.org/2025.emnlp-main.1678.pdf))
> An evaluation procedure using an LLM (GPT-4) with a 1-5 scoring prompt to assess the quality of poetry translations across three dimensions: Beauty of Sound (BS), Beauty of Form (BF), and Beauty of Meaning (BM).

**GPT-4-as-a-judge** (2 papers: [Turning Logic Against Itself: Probing Model Defenses Through Contrastive Questions](https://aclanthology.org/2025.emnlp-main.1762.pdf), [WONDERBREAD: A Benchmark for Evaluating Multimodal Foundation Models on Business Process Management Tasks](https://proceedings.neurips.cc/paper_files/paper/2024/file/d1fa821312040303b089ae529dbf81a6-Paper-Datasets_and_Benchmarks_Track.pdf))
> A judge-model evaluation procedure using GPT-4 to label model responses as harmful or not harmful for jailbreak assessment.

**LLM evaluation** (2 papers: [Evaluating Small Language Models for News Summarization: Implications and Factors Influencing Performance](https://aclanthology.org/2025.naacl-long.253.pdf), [An LLM-Based Approach for Insight Generation in Data Analysis](https://aclanthology.org/2025.naacl-long.24.pdf))
> Automated assessment using an LLM as a judge to evaluate insightfulness via pairwise comparisons or correctness via claim validation, calibrated against human judgments.

**GPT-4 multidimensional score** (1 paper: [On the Power of Decision Trees in Auto-Regressive Language Modeling](https://proceedings.neurips.cc/paper_files/paper/2024/file/72176f95680c3fb27a0966f36d5d0c53-Paper-Conference.pdf))
> A GPT-4-based evaluation procedure that grades story completions along multiple qualitative dimensions.

**GPT-4 rating** (1 paper: [Uncovering Safety Risks of Large Language Models through Concept Activation Vector](https://proceedings.neurips.cc/paper_files/paper/2024/file/d3a230d716e65afab578a8eb31a8d25f-Paper-Conference.pdf))
> An automated evaluation protocol where the GPT-4 model is used as a judge to assess the quality and safety of other models' responses based on predefined criteria.

**GPT-4V based evaluation** (1 paper: [Make-it-Real: Unleashing Large Multimodal Model for Painting 3D Objects with Realistic Materials](https://proceedings.neurips.cc/paper_files/paper/2024/file/b3b55c366d641c07180c40e4f978f311-Paper-Conference.pdf))
> An evaluation protocol where GPT-4V is prompted to act as an expert to compare the photorealism of 3D objects before and after material refinement, providing a preference and a justification.

**GPT-4 win rate** (1 paper: [Language Model Detectors Are Easily Optimized Against](https://proceedings.iclr.cc/paper_files/paper/2024/file/1f9f07df0992ce21698d800eaa891bd8-Paper-Conference.pdf))
> A human-or-model preference evaluation in which GPT-4 chooses which of two generations is more fluently and coherently written.

**GPT-4 Evaluation** (3 papers: [Amortizing intractable inference in large language models](https://proceedings.iclr.cc/paper_files/paper/2024/file/bc667ac84ef58f2b5022da97a465cbab-Paper-Conference.pdf), [Multilingual Jailbreak Challenges in Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/6b396f766a50e0853a5164e68048540c-Paper-Conference.pdf), [The False Promise of Imitating Proprietary Language Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/4db16435e3a5a2ef3fc39b8f0d12498d-Paper-Conference.pdf))
> Automated evaluation using GPT-4 to perform blind pairwise comparisons between model outputs, simulating human judgment on quality.

**GPT-4–judged pairwise comparisons** (1 paper: [JI2S: Joint Influence-Aware Instruction Data Selection for Efficient Fine-Tuning](https://aclanthology.org/2025.emnlp-main.26.pdf))
> Human-like evaluation where GPT-4 compares model outputs in a pairwise fashion across test sets to determine relative quality.

**Pairwise evaluation** (1 paper: [Fooling the LVLM Judges: Visual Biases in LVLM-Based Evaluation](https://aclanthology.org/2025.emnlp-main.1182.pdf))
> A comparative evaluation procedure in which an LVLM judge selects which of two images better aligns with a given textual prompt, with order reversed to control position bias.

**LLM-based zero-shot annotation** (1 paper: [Understanding the Thinking Process of Reasoning Models: A Perspective from Schoenfeld's Episode Theory](https://aclanthology.org/2025.emnlp-main.922.pdf))
> Automated evaluation method using large language models (e.g., GPT-4.1, Gemini-2.0) in zero-shot or few-shot settings with prompting techniques to replicate human episode labeling.

**LLM-CoT** (1 paper: [Optimizing Adaptive Attacks against Watermarks for Language Models](https://raw.githubusercontent.com/mlresearch/v267/main/assets/diaa25a/diaa25a.pdf))
> An LLM-based chain-of-thought judging procedure used to assess paraphrase quality.

**ChatbotArena (Arena-Hard) prompt** (1 paper: [Diverging Preferences: When do Annotators Disagree and do Models Know?](https://raw.githubusercontent.com/mlresearch/v267/main/assets/zhang25bx/zhang25bx.pdf))
> A specific prompting template from the ChatbotArena project used to conduct LLM-as-Judge evaluations.

**LLM-powered evaluation** (1 paper: [A Dual-Mind Framework for Strategic and Expressive Negotiation Agent](https://aclanthology.org/2025.acl-long.1161.pdf))
> An evaluation methodology where a Large Language Model is used to assess the quality of generated text based on predefined criteria, serving as an alternative to human annotators.

**Model-Based Evaluation** (1 paper: [MaXIFE: Multilingual and Cross-lingual Instruction Following Evaluation](https://aclanthology.org/2025.acl-long.698.pdf))
> Evaluation using a large language model (Claude-3.5 Sonnet) to assess instruction adherence in categories requiring semantic or subjective judgment, such as style, tone, and language switching.

**GPT-based assessment** (1 paper: [Bone Soups: A Seek-and-Soup Model Merging Approach for Controllable Multi-Objective Generation](https://aclanthology.org/2025.acl-long.1322.pdf))
> An evaluation procedure that uses a large generative model, such as GPT-4, as an automated evaluator to assess the quality of another model's output in realistic scenarios.

**GPT evaluation** (1 paper: [PopAlign: Diversifying Contrasting Patterns for a More Comprehensive Alignment](https://aclanthology.org/2025.acl-long.1403.pdf))
> An evaluation protocol that uses a powerful proprietary model, such as GPT-4, as an automated judge to compare and rate the quality of outputs from other models.

**Llama3-based metric** (1 paper: [Adapting Sentence-level Automatic Metrics for Document-level Simplification Evaluation](https://aclanthology.org/2025.naacl-long.327.pdf))
> Evaluation method using Llama3-8B-Instruct to score simplifications on meaning preservation, fluency, and simplicity via prompt-based judgment.

**Model-based evaluation** (1 paper: [ResearchAgent: Iterative Research Idea Generation over Scientific Literature with Large Language Models](https://aclanthology.org/2025.naacl-long.342.pdf))
> An automatic evaluation procedure where an LLM (GPT-4) is used to judge the quality of generated research ideas based on predefined criteria, using both Likert scale ratings and pairwise comparisons.

**GPT-4V judge** (1 paper: [Aligning Vision Models with Human Aesthetics in Retrieval: Benchmarks and Algorithms](https://proceedings.neurips.cc/paper_files/paper/2024/file/9d3faa41886997cfc2128b930077fa49-Paper-Conference.pdf))
> An evaluation protocol that uses the GPT-4V model to compare the outputs of two retrieval systems and determine which one performs better based on criteria like accuracy and aesthetics, often employing an order-consistency strategy to mitigate bias.

**GPT-4 evaluator** (3 papers: [AGILE: A Novel Reinforcement Learning Framework of LLM Agents](https://proceedings.neurips.cc/paper_files/paper/2024/file/097c514162ea7126d40671d23e12f51b-Paper-Conference.pdf), [DHA: Learning Decoupled-Head Attention from Transformer Checkpoints via Adaptive Heads Fusion](https://proceedings.neurips.cc/paper_files/paper/2024/file/518a75257f37b32f711082dff33c2ffc-Paper-Conference.pdf), [Mars: Situated Inductive Reasoning in an Open-World Environment](https://proceedings.neurips.cc/paper_files/paper/2024/file/1fb6d0b52f5e41b11392841a66dbfe7d-Paper-Datasets_and_Benchmarks_Track.pdf))
> A procedure using GPT-4 to measure the precision of predicted rules and the recall of ground truth rules in natural language.

**ChatGPT-based evaluation** (1 paper: [Visual CoT: Advancing Multi-Modal Language Models with a Comprehensive Dataset and Benchmark for Chain-of-Thought Reasoning](https://proceedings.neurips.cc/paper_files/paper/2024/file/0ff38d72a2e0aa6dbe42de83a17b2223-Paper-Datasets_and_Benchmarks_Track.pdf))
> An evaluation protocol where model-generated answers are scored for accuracy on a numerical scale from 0 to 1 by the ChatGPT model.

**GPT-3.5-turbo evaluation** (1 paper: [Shadowcast: Stealthy Data Poisoning Attacks Against Vision-Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/6a2e30664b9647f97d7b9275358d083c-Paper-Conference.pdf))
> An automated evaluation procedure that uses the GPT-3.5-turbo model to assess whether a VLM's response aligns with a predefined destination concept, used to measure the success rate of persuasion attacks.

**GPT-4-based preference test** (1 paper: [Paralinguistics-Aware Speech-Empowered Large Language Models for Natural Conversation](https://proceedings.neurips.cc/paper_files/paper/2024/file/ecfa5340fd896e5314bc5e132b5dd5ca-Paper-Conference.pdf))
> An automated evaluation protocol where the GPT-4 model is used as a judge to compare and select the preferred response between two models based on transcribed text.

**GPT-4 evaluation protocol** (1 paper: [SpatialRGPT: Grounded Spatial Reasoning in Vision-Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/f38cb4cf9a5eaa92b3cfa481832719c6-Paper-Conference.pdf))
> A GPT-4-based judging procedure used to score qualitative spatial answers and normalize quantitative answers into common units for evaluation.

**GPT-3.5-based evaluation** (1 paper: [MMBench-Video: A Long-Form Multi-Shot Benchmark for Holistic Video Understanding](https://proceedings.neurips.cc/paper_files/paper/2024/file/a2326c9715a516c91174132e0170073a-Paper-Datasets_and_Benchmarks_Track.pdf))
> An automated evaluation protocol using the GPT-3.5 model to score open-ended answers, which the paper critiques for being less accurate and less aligned with human preferences.

**GPT-4 ranking** (1 paper: [Voila-A: Aligning Vision-Language Models with User's Gaze Attention](https://proceedings.neurips.cc/paper_files/paper/2024/file/03738e5f26967582eeb3b57eef82f1f0-Paper-Conference.pdf))
> A pairwise evaluation procedure using GPT-4 to compare two candidate answers and judge which response is better.

**GPT-4 Grader** (1 paper: [Can Models Learn Skill Composition from Examples?](https://proceedings.neurips.cc/paper_files/paper/2024/file/b99fd30559b520cc97447ba905040677-Paper-Conference.pdf))
> A measurement protocol using GPT-4 as the automated grader model to evaluate generated text pieces based on specific criteria within the SKILL-MIX evaluation.

**Claude 3 Opus Grader** (1 paper: [Can Models Learn Skill Composition from Examples?](https://proceedings.neurips.cc/paper_files/paper/2024/file/b99fd30559b520cc97447ba905040677-Paper-Conference.pdf))
> A measurement protocol using Claude 3 Opus as the automated grader model to verify SKILL-MIX evaluation results and eliminate potential bias from GPT-4 grading.

**GPT-4 feedback** (1 paper: [Adversarial Moment-Matching Distillation of Large Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/cbae8efcc23a0cb6d15a20f245514020-Paper-Conference.pdf))
> An evaluation protocol where the GPT-4 model is used to provide qualitative feedback or scores on the outputs of the model being tested.

**GPT-4o-mini labeling** (1 paper: [Goal-Conditioned DPO: Prioritizing Safety in Misaligned Instructions](https://aclanthology.org/2025.naacl-long.369.pdf))
> Evaluation protocol using GPT-4o-mini to classify model responses as good, bad, or unclear based on predefined criteria.

**GPT-4o-based metric** (1 paper: [On Positional Bias of Faithfulness for Long-form Summarization](https://aclanthology.org/2025.naacl-long.442.pdf))
> An LLM-based faithfulness evaluation method using GPT-4o to judge whether a summary is entailed by the source documents, capable of processing full context or aggregated document chunks.

**GPT-4-based Likert evaluation** (1 paper: [MAMM-Refine: A Recipe for Improving Faithfulness in Generation with Multi-Agent Collaboration](https://aclanthology.org/2025.naacl-long.498.pdf))
> A human-like evaluation protocol using GPT-4 to rate the quality of model outputs on a Likert scale, used here to assess faithfulness in refinement.

**Judge LLM evaluation** (1 paper: [Anecdoctoring: Automated Red-Teaming Across Language and Place](https://aclanthology.org/2025.emnlp-main.964.pdf))
> A human-validated automated evaluation protocol using GPT-4o as a judge model to score model outputs on a 5-point harm scale, where scores of 4 or 5 indicate policy violations.

**LLM-as-a-judge framework** (2 papers: [Deriving Strategic Market Insights with Large Language Models: A Benchmark for Forward Counterfactual Generation](https://aclanthology.org/2025.emnlp-main.575.pdf), [EduAdapt: A Question Answer Benchmark Dataset for Evaluating Grade-Level Adaptability in LLMs](https://aclanthology.org/2025.emnlp-main.1736.pdf))
> An automated evaluation method using GPT-4o to assess whether generated counterfactuals meet criteria for forward-compatibility and directionality based on structured prompts.

**LLM-as-judge framework** (1 paper: [EGOILLUSION: Benchmarking Hallucinations in Egocentric Video Understanding](https://aclanthology.org/2025.emnlp-main.1446.pdf))
> A two-step evaluation procedure using an LLM to judge whether open-ended responses implicitly assume object presence and to assess factual correctness.

**GPT-4o as a judge** (1 paper: [AFRIDOC-MT: Document-level MT Corpus for African Languages](https://aclanthology.org/2025.emnlp-main.1413.pdf))
> An evaluation protocol where GPT-4o is used to assess the quality of translated documents based on criteria such as fluency, content errors, and cohesion.

**GPT-4o-as-Judge** (1 paper: [EIFBENCH: Extremely Complex Instruction Following Benchmark for Large Language Models](https://aclanthology.org/2025.emnlp-main.1059.pdf))
> Human evaluation protocol using GPT-4o as an automated judge to assess constraint adherence in model outputs via binary compliance scoring.

**Autorater evaluation** (1 paper: [Unstructured Evidence Attribution for Long Context Query Focused Summarization](https://aclanthology.org/2025.emnlp-main.95.pdf))
> Automated evaluation using an LLM-based rater (DeepSeek-V3) to score relevance and consistency of evidence and summaries by prompting with source text, target text, and query.

**Model arena evaluation** (1 paper: [A Symbolic Adversarial Learning Framework for Evolving Fake News Generation and Detection](https://aclanthology.org/2025.emnlp-main.619.pdf))
> An evaluation method where LLMs act as judges to compare and assess the perceived credibility of different model-generated texts.

**GPT-4o evaluator** (1 paper: [MoLoRAG: Bootstrapping Document Understanding via Multi-modal Logic-aware Retrieval](https://aclanthology.org/2025.emnlp-main.708.pdf))
> An evaluation procedure in which GPT-4o judges whether generated answers match ground-truth answers for long-sentence or multiple-choice document QA items.

**LLMs-as-Judges** (1 paper: [Position: LLMs Can be Good Tutors in English Education](https://aclanthology.org/2025.emnlp-main.885.pdf))
> An automated evaluation protocol where a large language model is used to assess the quality of another model's output, reducing the need for human annotation.

**GPT-4V-based evaluation** (1 paper: [I2EBench: A Comprehensive Benchmark for Instruction-based Image Editing](https://proceedings.neurips.cc/paper_files/paper/2024/file/48fecef47b19fe501d27d338b6d52582-Paper-Conference.pdf))
> An automated evaluation procedure that uses the GPT-4V model to make judgments about the quality of edited images for high-level dimensions like counting, object removal, and background replacement.

## Relationships

### LLM-as-a-judge →
- **Omni-Judge** (measurement instrument): *correlates*, 1 paper
  > Our Omni-Judge provides achieves over 91% consistency with GPT-4o
  - [Omni-MATH: A Universal Olympiad Level Mathematic Benchmark for Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/f9e1e8b56c7e363985ebeb0e9dd1a85c-Paper-Conference.pdf)

### → LLM-as-a-judge
- **Helpfulness** (construct): *measured_by*, 19 papers
  > the three rounds of Safe RLHF significantly improved the Elo scores in both helpfulness and harmlessness, as evaluated by both GPT-4 and human evaluators.
  - [Safe RLHF: Safe Reinforcement Learning from Human Feedback](https://proceedings.iclr.cc/paper_files/paper/2024/file/dd1577afd396928ed64216f3f1fd5556-Paper-Conference.pdf)
  - [Compressing LLMs: The Truth is Rarely Pure and Never Simple](https://proceedings.iclr.cc/paper_files/paper/2024/file/9f09f316a3eaf59d9ced5ffaefe97e0f-Paper-Conference.pdf)
  - [An Emulator for Fine-tuning Large Language Models using Small Language Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/389e161125965c0f0ba50420fee45774-Paper-Conference.pdf)
  - [ARGS: Alignment as Reward-Guided Search](https://proceedings.iclr.cc/paper_files/paper/2024/file/4d1344317478ad99ff5f4e414aeab689-Paper-Conference.pdf)
  - [Stepwise Alignment for Constrained Language Model Policy Optimization](https://proceedings.neurips.cc/paper_files/paper/2024/file/bcfcf7232cb74e1ef82d751880ff835b-Paper-Conference.pdf)
  - [Aligning Large Language Models with Representation Editing: A Control Perspective](https://proceedings.neurips.cc/paper_files/paper/2024/file/41bba7b0f5c81e789a20bb16a370aeeb-Paper-Conference.pdf)
  - [MedJourney: Benchmark and Evaluation of Large Language Models over Patient Clinical Journey](https://proceedings.neurips.cc/paper_files/paper/2024/file/9f80af32390984cb709cdeb014d0df41-Paper-Datasets_and_Benchmarks_Track.pdf)
  - [DACO: Towards Application-Driven and Comprehensive Data Analysis via Code Generation](https://proceedings.neurips.cc/paper_files/paper/2024/file/a4cb1444fb05839d0113d2773da88a49-Paper-Datasets_and_Benchmarks_Track.pdf)
  - [Aligner: Efficient Alignment by Learning to Correct](https://proceedings.neurips.cc/paper_files/paper/2024/file/a51a74b2d71387dc71cc29181b5519bb-Paper-Conference.pdf)
  - [Collab: Controlled Decoding using Mixture of Agents for LLM Alignment](https://proceedings.iclr.cc/paper_files/paper/2025/file/2e79dce47c5bbe738dff9c05ace8a037-Paper-Conference.pdf)
  - [GenARM: Reward Guided Generation with Autoregressive Reward Model for Test-Time Alignment](https://proceedings.iclr.cc/paper_files/paper/2025/file/b7a55b1fa8f2500299e1af3562a1191d-Paper-Conference.pdf)
  - [LLaMA-Omni: Seamless Speech Interaction with Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/90d1fc07f46e31387978b88e7e057a31-Paper-Conference.pdf)
  - [MACPO: Weak-to-Strong Alignment via Multi-Agent Contrastive Preference Optimization](https://proceedings.iclr.cc/paper_files/paper/2025/file/9ddd47ee8d0b9543925a8db3e9d879b3-Paper-Conference.pdf)
  - [DPL: Diverse Preference Learning Without A Reference Model](https://aclanthology.org/2025.naacl-long.190.pdf)
  - [AdvisorQA: Towards Helpful and Harmless Advice-seeking Question Answering with Collective Intelligence](https://aclanthology.org/2025.naacl-long.333.pdf)
  - [From Distributional to Overton Pluralism: Investigating Large Language Model Alignment](https://aclanthology.org/2025.naacl-long.346.pdf)
  - [On the Role of Model Prior in Real-World Inductive Reasoning](https://aclanthology.org/2025.emnlp-main.534.pdf)
  - [Data to Defense: The Role of Curation in Aligning Large Language Models Against Safety Compromise](https://aclanthology.org/2025.emnlp-main.647.pdf)
  - [SPIRIT: Patching Speech Language Models against Jailbreak Attacks](https://aclanthology.org/2025.emnlp-main.734.pdf)
- **Harmlessness** (construct): *measured_by*, 12 papers
  > the three rounds of Safe RLHF significantly improved the Elo scores in both helpfulness and harmlessness, as evaluated by both GPT-4 and human evaluators.
  - [Safe RLHF: Safe Reinforcement Learning from Human Feedback](https://proceedings.iclr.cc/paper_files/paper/2024/file/dd1577afd396928ed64216f3f1fd5556-Paper-Conference.pdf)
  - [An Emulator for Fine-tuning Large Language Models using Small Language Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/389e161125965c0f0ba50420fee45774-Paper-Conference.pdf)
  - [ARGS: Alignment as Reward-Guided Search](https://proceedings.iclr.cc/paper_files/paper/2024/file/4d1344317478ad99ff5f4e414aeab689-Paper-Conference.pdf)
  - [RAIN: Your Language Models Can Align Themselves without Finetuning](https://proceedings.iclr.cc/paper_files/paper/2024/file/5a4699b3d0bf7ba934fe10cdba5a8a32-Paper-Conference.pdf)
  - [Stepwise Alignment for Constrained Language Model Policy Optimization](https://proceedings.neurips.cc/paper_files/paper/2024/file/bcfcf7232cb74e1ef82d751880ff835b-Paper-Conference.pdf)
  - [Aligning Large Language Models with Representation Editing: A Control Perspective](https://proceedings.neurips.cc/paper_files/paper/2024/file/41bba7b0f5c81e789a20bb16a370aeeb-Paper-Conference.pdf)
  - [Aligner: Efficient Alignment by Learning to Correct](https://proceedings.neurips.cc/paper_files/paper/2024/file/a51a74b2d71387dc71cc29181b5519bb-Paper-Conference.pdf)
  - [Collab: Controlled Decoding using Mixture of Agents for LLM Alignment](https://proceedings.iclr.cc/paper_files/paper/2025/file/2e79dce47c5bbe738dff9c05ace8a037-Paper-Conference.pdf)
  - [GenARM: Reward Guided Generation with Autoregressive Reward Model for Test-Time Alignment](https://proceedings.iclr.cc/paper_files/paper/2025/file/b7a55b1fa8f2500299e1af3562a1191d-Paper-Conference.pdf)
  - [MACPO: Weak-to-Strong Alignment via Multi-Agent Contrastive Preference Optimization](https://proceedings.iclr.cc/paper_files/paper/2025/file/9ddd47ee8d0b9543925a8db3e9d879b3-Paper-Conference.pdf)
  - [AGD: Adversarial Game Defense Against Jailbreak Attacks in Large Language Models](https://aclanthology.org/2025.acl-long.851.pdf)
  - [Weak-to-Strong Jailbreaking on Large Language Models](https://raw.githubusercontent.com/mlresearch/v267/main/assets/zhao25aa/zhao25aa.pdf)
- **Human evaluation** (measurement instrument): *correlates*, 10 papers
  > experiments demonstrate that LLM-based metrics show a higher correlation with human evaluation compared to traditional metrics. (Abstract)
  - [SD-Eval: A Benchmark Dataset for Spoken Dialogue Understanding Beyond Words](https://proceedings.neurips.cc/paper_files/paper/2024/file/681fe4ec554beabdc9c84a1780cd5a8a-Paper-Datasets_and_Benchmarks_Track.pdf)
  - [Omni-MATH: A Universal Olympiad Level Mathematic Benchmark for Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/f9e1e8b56c7e363985ebeb0e9dd1a85c-Paper-Conference.pdf)
  - [ChartMimic: Evaluating LMM's Cross-Modal Reasoning Capability via Chart-to-Code Generation](https://proceedings.iclr.cc/paper_files/paper/2025/file/42806406dd99e30c3796bc98b2670fa2-Paper-Conference.pdf)
  - [MMWorld: Towards Multi-discipline Multi-faceted World Model Evaluation in Videos](https://proceedings.iclr.cc/paper_files/paper/2025/file/4364fef031fdf7bfd9d1c9c56b287084-Paper-Conference.pdf)
  - [Truth Knows No Language: Evaluating Truthfulness Beyond English](https://aclanthology.org/2025.acl-long.1507.pdf)
  - [Palm: A Culturally Inclusive and Linguistically Diverse Dataset for Arabic LLMs](https://aclanthology.org/2025.acl-long.1579.pdf)
  - [CKnowEdit: A New Chinese Knowledge Editing Dataset for Linguistics, Facts, and Logic Error Correction in LLMs](https://aclanthology.org/2025.acl-long.430.pdf)
  - [Memorization or Reasoning? Exploring the Idiom Understanding of LLMs](https://aclanthology.org/2025.emnlp-main.1099.pdf)
  - [AccessEval: Benchmarking Disability Bias in Large Language Models](https://aclanthology.org/2025.emnlp-main.1653.pdf)
  - [The Illusion of Progress: Re-evaluating Hallucination Detection in LLMs](https://aclanthology.org/2025.emnlp-main.1761.pdf)
- **Factuality** (construct): *measured_by*, 9 papers
  > Using GPT-4 as a judge, we find that FactTune-MC and FactTune-EC can improve both factuality and fluency compared to the SFT model (examples in Appendix Table 8). (Section 4.2)
  - [Fine-Tuning Language Models for Factuality](https://proceedings.iclr.cc/paper_files/paper/2024/file/c361ae924c23cafca6033610d25dbc65-Paper-Conference.pdf)
  - [An Emulator for Fine-tuning Large Language Models using Small Language Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/389e161125965c0f0ba50420fee45774-Paper-Conference.pdf)
  - [Chunk-Distilled Language Modeling](https://proceedings.iclr.cc/paper_files/paper/2025/file/0d4d9fc36c783fcd31af2fda532e6c33-Paper-Conference.pdf)
  - [Identifying Reliable Evaluation Metrics for Scientific Text Revision](https://aclanthology.org/2025.acl-long.335.pdf)
  - [SK-VQA: Synthetic Knowledge Generation at Scale for Training Context-Augmented Multimodal LLMs](https://raw.githubusercontent.com/mlresearch/v267/main/assets/su25a/su25a.pdf)
  - [Generalized Interpolating Discrete Diffusion](https://raw.githubusercontent.com/mlresearch/v267/main/assets/von-rutte25a/von-rutte25a.pdf)
  - [SCRIBE: Structured Chain Reasoning for Interactive Behaviour Explanations using Tool Calling](https://aclanthology.org/2025.emnlp-main.1490.pdf)
  - [TounsiBench: Benchmarking Large Language Models for Tunisian Arabic](https://aclanthology.org/2025.emnlp-main.1756.pdf)
  - [The Illusion of Progress: Re-evaluating Hallucination Detection in LLMs](https://aclanthology.org/2025.emnlp-main.1761.pdf)
- **Text generation** (behavioral indicator): *measured_by*, 8 papers
  > As we generate open-ended text from our off-the-shelf models OTSi and our mLLaVA variants for Object Identification, we evaluate this particular task using an LLM-as-a-Judge, specifically Prometheus-2-8x7B (Kim et al., 2024). (Section 4.2)
  - [See It from My Perspective: How Language Affects Cultural Bias in Image Understanding](https://proceedings.iclr.cc/paper_files/paper/2025/file/8c0fabe372177d2aded596be2d3b4544-Paper-Conference.pdf)
  - [Proactive Privacy Amnesia for Large Language Models: Safeguarding PII with Negligible Impact on Model Utility](https://proceedings.iclr.cc/paper_files/paper/2025/file/8c234d9c7e738a793947e0282c36eb95-Paper-Conference.pdf)
  - [Federated Residual Low-Rank Adaption of Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/906c860f1b7515a8ffec02dcdac74048-Paper-Conference.pdf)
  - [Differentially Private Steering for Large Language Model Alignment](https://proceedings.iclr.cc/paper_files/paper/2025/file/45326c2df19fee16fc1ebc44941fea8e-Paper-Conference.pdf)
  - [HaDeMiF: Hallucination Detection and Mitigation in Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/c98987c5ec4f30920d7190dc699e3daf-Paper-Conference.pdf)
  - [Personality Alignment of Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/25203d1cc8c58381eab578f4fcf9c4f8-Paper-Conference.pdf)
  - [Fine-Tuning Large Language Models with Sequential Instructions](https://aclanthology.org/2025.naacl-long.288.pdf)
  - [FisherSFT: Data-Efficient Supervised Fine-Tuning of Language Models Using Information Gain](https://raw.githubusercontent.com/mlresearch/v267/main/assets/deb25a/deb25a.pdf)
- **Text generation quality** (construct): *measured_by*, 7 papers
  > These newly designed criteria leverage human judges or GPT-4 to better evaluate response quality. (Section 3.1)
  - [Uncovering Safety Risks of Large Language Models through Concept Activation Vector](https://proceedings.neurips.cc/paper_files/paper/2024/file/d3a230d716e65afab578a8eb31a8d25f-Paper-Conference.pdf)
  - [To Code or Not To Code? Exploring Impact of Code in Pre-training](https://proceedings.iclr.cc/paper_files/paper/2025/file/c513d1786f85531fac7050947736265f-Paper-Conference.pdf)
  - [LongWriter: Unleashing 10,000+ Word Generation from Long Context LLMs](https://proceedings.iclr.cc/paper_files/paper/2025/file/59f278de1619bdb6b53fd04e8e0976e0-Paper-Conference.pdf)
  - [Improving Instruction-Following in Language Models through Activation Steering](https://proceedings.iclr.cc/paper_files/paper/2025/file/8c3262a4c965ba9888f120d4f9e13478-Paper-Conference.pdf)
  - [Evaluating Language Models as Synthetic Data Generators](https://aclanthology.org/2025.acl-long.320.pdf)
  - [RAPID: Long-Context Inference with Retrieval-Augmented Speculative Decoding](https://raw.githubusercontent.com/mlresearch/v267/main/assets/chen25s/chen25s.pdf)
  - [SparseLoRA: Accelerating LLM Fine-Tuning with Contextual Sparsity](https://raw.githubusercontent.com/mlresearch/v267/main/assets/khaki25a/khaki25a.pdf)
- **Hallucination** (behavioral indicator): *measured_by*, 7 papers
  > To measure hallucination on the realistic tasks, we use GPT-4 as an evaluator (OpenAI, 2023), following Yue et al. (2023); Gao et al. (2023a). (Section 3.2)
  - [Teaching Language Models to Hallucinate Less with Synthetic Tasks](https://proceedings.iclr.cc/paper_files/paper/2024/file/e4cd50120b6d7e8daff1749d6bbaa889-Paper-Conference.pdf)
  - [Intervening Anchor Token: Decoding Strategy in Alleviating Hallucinations for MLLMs](https://proceedings.iclr.cc/paper_files/paper/2025/file/4537e2172096d966228d68c428392894-Paper-Conference.pdf)
  - [Robust Multimodal Large Language Models Against Modality Conflict](https://raw.githubusercontent.com/mlresearch/v267/main/assets/zhang25dq/zhang25dq.pdf)
  - [Unveiling the Response of Large Vision-Language Models to Visually Absent Tokens](https://aclanthology.org/2025.emnlp-main.1092.pdf)
  - [Hallucination Detection in LLMs Using Spectral Features of Attention Maps](https://aclanthology.org/2025.emnlp-main.1239.pdf)
  - [Mitigating Hallucinations in Vision-Language Models through Image-Guided Head Suppression](https://aclanthology.org/2025.emnlp-main.631.pdf)
  - [An LLM-Based Approach for Insight Generation in Data Analysis](https://aclanthology.org/2025.naacl-long.24.pdf)
- **Fluency** (construct): *measured_by*, 5 papers
  > Using GPT-4 as a judge, we find that FactTune-MC and FactTune-EC can improve both factuality and fluency compared to the SFT model (examples in Appendix Table 8). (Section 4.2)
  - [Fine-Tuning Language Models for Factuality](https://proceedings.iclr.cc/paper_files/paper/2024/file/c361ae924c23cafca6033610d25dbc65-Paper-Conference.pdf)
  - [MA-RLHF: Reinforcement Learning from Human Feedback with Macro Actions](https://proceedings.iclr.cc/paper_files/paper/2025/file/429d69979c22b06d6baa65caf3ab1e10-Paper-Conference.pdf)
  - [Adapting Sentence-level Automatic Metrics for Document-level Simplification Evaluation](https://aclanthology.org/2025.naacl-long.327.pdf)
  - [Fann or Flop: A Multigenre, Multiera Benchmark for Arabic Poetry Understanding in LLMs](https://aclanthology.org/2025.emnlp-main.1023.pdf)
  - [DIWALI - Diversity and Inclusivity aWare cuLture specific Items for India: Dataset and Assessment of LLMs for Cultural Text Adaptation in Indian Context](https://aclanthology.org/2025.emnlp-main.1706.pdf)
- **Relevance** (construct): *measured_by*, 5 papers
  > We prompt GPT-4 to rate responses from various decoding strategies on relevance, accuracy, and insightfulness, scoring them from 1 to 10. (Table 2)
  - [Transfer Q-star : Principled Decoding for LLM Alignment](https://proceedings.neurips.cc/paper_files/paper/2024/file/b8700a8a005032fe869c741b0a75274b-Paper-Conference.pdf)
  - [Collab: Controlled Decoding using Mixture of Agents for LLM Alignment](https://proceedings.iclr.cc/paper_files/paper/2025/file/2e79dce47c5bbe738dff9c05ace8a037-Paper-Conference.pdf)
  - [CaLMQA: Exploring culturally specific long-form question answering across 23 languages](https://aclanthology.org/2025.acl-long.578.pdf)
  - [Multi-perspective Analysis of Large Language Model Domain Specialization: An Experiment in Accounting Audit Procedures Generation](https://aclanthology.org/2025.emnlp-main.891.pdf)
  - [TounsiBench: Benchmarking Large Language Models for Tunisian Arabic](https://aclanthology.org/2025.emnlp-main.1756.pdf)
- **Harmful content generation** (behavioral indicator): *measured_by*, 5 papers
  > To measure jailbreak success, we computed: (i) Cross-Entropy (Eqn. 1) and (ii) Claude 3 Opus Harmful-Yet-Helpful Score by prompting Claude 3 Opus to assess how helpful-yet-harmful sampled outputs are.
  - [Failures to Find Transferable Image Jailbreaks Between Vision-Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/6e3daaeca6be8579573f69082b2dd58b-Paper-Conference.pdf)
  - [EFFICIENT JAILBREAK ATTACK SEQUENCES ON LARGE LANGUAGE MODELS VIA MULTI-ARMED BANDIT-BASED CONTEXT SWITCHING](https://proceedings.iclr.cc/paper_files/paper/2025/file/52724c4ea3634f610b0ef0245ce5bd20-Paper-Conference.pdf)
  - [Safety Alignment Should be Made More Than Just a Few Tokens Deep](https://proceedings.iclr.cc/paper_files/paper/2025/file/88be023075a5a3ff3dc3b5d26623fa22-Paper-Conference.pdf)
  - [FlipAttack: Jailbreak LLMs via Flipping](https://raw.githubusercontent.com/mlresearch/v267/main/assets/liu25z/liu25z.pdf)
  - [Visual Contextual Attack: Jailbreaking MLLMs with Image-Driven Context Injection](https://aclanthology.org/2025.emnlp-main.487.pdf)
- **Faithfulness** (construct): *measured_by*, 4 papers
  > In this work, we evaluate primarily our models using recent NLI-related metrics (Zha et al., 2023; Dušek & Kasner, 2020), and LLM-as-a-judge, focusing on faithfulness (Chiang & Lee, 2023; Gilardi et al., 2023). (Section 2)
  - [SCOPE: A Self-supervised Framework for Improving Faithfulness in Conditional Text Generation](https://proceedings.iclr.cc/paper_files/paper/2025/file/05d6b5b6901fb57d2c287e1d3ce6d63c-Paper-Conference.pdf)
  - [SARA: Salience-Aware Reinforced Adaptive Decoding for Large Language Models in Abstractive Summarization](https://aclanthology.org/2025.acl-long.1236.pdf)
  - [Fann or Flop: A Multigenre, Multiera Benchmark for Arabic Poetry Understanding in LLMs](https://aclanthology.org/2025.emnlp-main.1023.pdf)
  - [Keep Security! Benchmarking Security Policy Preservation in Large Language Model Contexts Against Indirect Attacks in Question Answering](https://aclanthology.org/2025.emnlp-main.345.pdf)
- **Jailbreaking** (behavioral indicator): *measured_by*, 4 papers
  > We use GPT-4 as the semantic judge (see Table 8 for the prompt) in line with the criteria established by Chao et al. (2023), where a jailbreak is considered successful only if it achieves a 10/10 jailbreak score from GPT-4.
  - [Jailbreaking Leading Safety-Aligned LLMs with Simple Adaptive Attacks](https://proceedings.iclr.cc/paper_files/paper/2025/file/63fa7efdd3bcf944a4bd6e0ff6a50041-Paper-Conference.pdf)
  - [Does Refusal Training in LLMs Generalize to the Past Tense?](https://proceedings.iclr.cc/paper_files/paper/2025/file/d432fbe4877ee1a6a51632a18e69784f-Paper-Conference.pdf)
  - [Jailbreaking as a Reward Misspecification Problem](https://proceedings.iclr.cc/paper_files/paper/2025/file/cf00c2fdf92882989b1fc0e3094a2abf-Paper-Conference.pdf)
  - [Diversity Helps Jailbreak Large Language Models](https://aclanthology.org/2025.naacl-long.238.pdf)
- **Instruction following** (behavioral indicator): *measured_by*, 3 papers
  > Vicuna QA (Chiang et al., 2023) uses GPT-4 to evaluate the abilities of open-ended chatbots to follow instructions.
  - [DoLa: Decoding by Contrasting Layers Improves Factuality in Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/edc36117f795ca52a0cbf6a7b3882859-Paper-Conference.pdf)
  - [Listen, Think, and Understand](https://proceedings.iclr.cc/paper_files/paper/2024/file/510d0935b543a29d686f93fa52d1c288-Paper-Conference.pdf)
  - [DELIFT: Data Efficient Language model Instruction Fine-Tuning](https://proceedings.iclr.cc/paper_files/paper/2025/file/f9d446812a6fdc05453f4093e54831e8-Paper-Conference.pdf)
- **Question answering** (behavioral indicator): *measured_by*, 3 papers
  > Question Answering. For questions about workflow demonstrations, the model generates a natural language answer, assessing its understanding of workflow semantics. We use GPT-4 to compare the generated answer to a reference answer for evaluation. (Section 4.2)
  - [WONDERBREAD: A Benchmark for Evaluating Multimodal Foundation Models on Business Process Management Tasks](https://proceedings.neurips.cc/paper_files/paper/2024/file/d1fa821312040303b089ae529dbf81a6-Paper-Datasets_and_Benchmarks_Track.pdf)
  - [UDA: A Benchmark Suite for Retrieval Augmented Generation in Real-World Document Analysis](https://proceedings.neurips.cc/paper_files/paper/2024/file/7c06759d1a8567f087b02e8589454917-Paper-Datasets_and_Benchmarks_Track.pdf)
  - [Provence: efficient and robust context pruning for retrieval-augmented generation](https://proceedings.iclr.cc/paper_files/paper/2025/file/5e956fef0946dc1e39760f94b78045fe-Paper-Conference.pdf)
- **Truthfulness** (construct): *measured_by*, 3 papers
  > We prompt GPT-4 to evaluate the informativeness (Info) and truthfulness (True) of model responses given the question and the gold labels. (Section 6).
  - [LoFiT: Localized Fine-tuning on LLM Representations](https://proceedings.neurips.cc/paper_files/paper/2024/file/122ea6470232ee5e79a2649243348005-Paper-Conference.pdf)
  - [Truth Knows No Language: Evaluating Truthfulness Beyond English](https://aclanthology.org/2025.acl-long.1507.pdf)
  - [TruthFlow: Truthful LLM Generation via Representation Flow Correction](https://raw.githubusercontent.com/mlresearch/v267/main/assets/wang25i/wang25i.pdf)
- **Insightfulness** (construct): *measured_by*, 3 papers
  > We prompt GPT-4 to rate responses from various decoding strategies on relevance, accuracy, and insightfulness, scoring them from 1 to 10. (Table 2)
  - [Transfer Q-star : Principled Decoding for LLM Alignment](https://proceedings.neurips.cc/paper_files/paper/2024/file/b8700a8a005032fe869c741b0a75274b-Paper-Conference.pdf)
  - [Collab: Controlled Decoding using Mixture of Agents for LLM Alignment](https://proceedings.iclr.cc/paper_files/paper/2025/file/2e79dce47c5bbe738dff9c05ace8a037-Paper-Conference.pdf)
  - [An LLM-Based Approach for Insight Generation in Data Analysis](https://aclanthology.org/2025.naacl-long.24.pdf)
- **Naturalness** (construct): *measured_by*, 3 papers
  > When evaluating the likelihood of the activity sequences, GPT-4o is instructed to take the following criteria into account: Naturalness: How well the activity aligns with the person’s innate abilities, habits, and environment.
  - [Simulating Human-like Daily Activities with Desire-driven Autonomy](https://proceedings.iclr.cc/paper_files/paper/2025/file/513cb685f67550dbd133b81a7a24249f-Paper-Conference.pdf)
  - [ToolFlow: Boosting LLM Tool-Calling Through Natural and Coherent Dialogue Synthesis](https://aclanthology.org/2025.naacl-long.214.pdf)
  - [Towards Controllable Speech Synthesis in the Era of Large Language Models: A Systematic Survey](https://aclanthology.org/2025.emnlp-main.40.pdf)
- **Personalization** (construct): *measured_by*, 3 papers
  > “We further explore whether we can employ language models to automate the evaluation... we ask GPT-4 to rate the responses based on their helpfulness and relevance to users’ preferences.”
  - [Context Steering: Controllable Personalization at Inference Time](https://proceedings.iclr.cc/paper_files/paper/2025/file/db178cd03313e23cffb8937e93f0d464-Paper-Conference.pdf)
  - [Personal Travel Solver: A Preference-Driven LLM-Solver System for Travel Planning](https://aclanthology.org/2025.acl-long.1339.pdf)
  - [Aligning LLMs by Predicting Preferences from User Writing Samples](https://raw.githubusercontent.com/mlresearch/v267/main/assets/aroca-ouellette25a/aroca-ouellette25a.pdf)
- **Interpretability and explainability** (construct): *measured_by*, 3 papers
  > We utilize a large multimodal model (GPT-4o) as the ‘judge’ to assign entailment scores given a constructed rule. ... This observation validates the interpretability of the reasoning paths in the concept tree. (Section 4.6)
  - [COCO-Tree: Compositional Hierarchical Concept Trees for Enhanced Reasoning in Vision-Language Models](https://aclanthology.org/2025.emnlp-main.135.pdf)
  - [Judge and Improve: Towards a Better Reasoning of Knowledge Graphs with Large Language Models](https://aclanthology.org/2025.emnlp-main.269.pdf)
  - [WISE: Weak-Supervision-Guided Step-by-Step Explanations for Multimodal LLMs in Image Classification](https://aclanthology.org/2025.emnlp-main.741.pdf)
- **Instruction following ability** (construct): *measured_by*, 2 papers
  > To evaluate system message following, similar to (Jiang et al., 2023; Zheng et al., 2023; Wen et al., 2024), we use advanced LLMs as verifier, and ensure evaluation accuracy through manually annotated evaluation checklists and well-designed evaluation prompts. (Section 1)
  - [SysBench: Can LLMs Follow System Message?](https://proceedings.iclr.cc/paper_files/paper/2025/file/b917f916e7eed84ffe8f5e63492b2be8-Paper-Conference.pdf)
  - [Identifying Reliable Evaluation Metrics for Scientific Text Revision](https://aclanthology.org/2025.acl-long.335.pdf)
- **Safety** (construct): *measured_by*, 2 papers
  > We use GPT-4 [1] to measure the helpfulness and harmlessness (i.e., safety) of the responses generated by the LM policies.
  - [Stepwise Alignment for Constrained Language Model Policy Optimization](https://proceedings.neurips.cc/paper_files/paper/2024/file/bcfcf7232cb74e1ef82d751880ff835b-Paper-Conference.pdf)
  - [DPL: Diverse Preference Learning Without A Reference Model](https://aclanthology.org/2025.naacl-long.190.pdf)
- **Coherence** (construct): *measured_by*, 2 papers
  > By the prompts, the LLM judge must consider (a) the response’s naturalness, coherence, engagingness and groundedness. (Section 4.3)
  - [SD-Eval: A Benchmark Dataset for Spoken Dialogue Understanding Beyond Words](https://proceedings.neurips.cc/paper_files/paper/2024/file/681fe4ec554beabdc9c84a1780cd5a8a-Paper-Datasets_and_Benchmarks_Track.pdf)
  - [Simulating Human-like Daily Activities with Desire-driven Autonomy](https://proceedings.iclr.cc/paper_files/paper/2025/file/513cb685f67550dbd133b81a7a24249f-Paper-Conference.pdf)
- **Chain of thought** (behavioral indicator): *measured_by*, 2 papers
  > For evaluating intermediate reasoning steps, we randomly select 200 samples and use a strong reasoning model, OpenAI-o3, to identify any errors within the reasoning process (Section 3.3).
  - [Code Execution as Grounded Supervision for LLM Reasoning](https://aclanthology.org/2025.emnlp-main.1260.pdf)
  - [SATBench: Benchmarking LLMs' Logical Reasoning via Automated Puzzle Generation from SAT Formulas](https://aclanthology.org/2025.emnlp-main.1716.pdf)
- **Object hallucination** (behavioral indicator): *measured_by*, 2 papers
  > "we evaluate LURE on six open-source LVLMs and found it outperforms the previous best approach in both general object hallucination evaluation metrics, GPT, and human evaluations" (Abstract); "In addition to human evaluation, inspired from (Zheng et al., 2023), we also prompt GPT-3.5 to compare different descriptions. In this GPT evaluation" (Section 4.1)
  - [Analyzing and Mitigating Object Hallucination in Large Vision-Language Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/fc625e831361cfcc82cb74224fdc66cb-Paper-Conference.pdf)
  - [Mitigating Object Hallucination in Large Vision-Language Models via Image-Grounded Guidance](https://raw.githubusercontent.com/mlresearch/v267/main/assets/zhao25j/zhao25j.pdf)
- **Text summarization** (behavioral indicator): *measured_by*, 2 papers
  > For the dialogue generation and summarization tasks, we use GPT-4 for zero-shot pairwise evaluation, which is consistent with human judgments (see prompts in Appendix C.2.1). (Section 5.1)
  - [Cal-DPO: Calibrated Direct Preference Optimization for Language Model Alignment](https://proceedings.neurips.cc/paper_files/paper/2024/file/cf8b2205e39f81726a8d828ecbe00ad0-Paper-Conference.pdf)
  - [TIS-DPO: Token-level Importance Sampling for Direct Preference Optimization With Estimated Weights](https://proceedings.iclr.cc/paper_files/paper/2025/file/7fb9f39075a5202472676a7531568212-Paper-Conference.pdf)
- **Image captioning** (behavioral indicator): *measured_by*, 2 papers
  > For literal description and contradiction, we report BERT score (recall), BLEURT (BLT), and GPT evaluation score. (Table 2)
  - [Cracking the Code of Juxtaposition: Can AI Models Understand the Humorous Contradictions](https://proceedings.neurips.cc/paper_files/paper/2024/file/540a6eefb60428c8547a27253f9a2a59-Paper-Conference.pdf)
  - [Do You Keep an Eye on What I Ask? Mitigating Multimodal Hallucination via Attention-Guided Ensemble Decoding](https://proceedings.iclr.cc/paper_files/paper/2025/file/637b275a6e65924719198188fc939632-Paper-Conference.pdf)
- **Accuracy** (construct): *measured_by*, 2 papers
  > We prompt GPT-4 to rate responses from various decoding strategies on relevance, accuracy, and insightfulness, scoring them from 1 to 10. (Table 2)
  - [Transfer Q-star : Principled Decoding for LLM Alignment](https://proceedings.neurips.cc/paper_files/paper/2024/file/b8700a8a005032fe869c741b0a75274b-Paper-Conference.pdf)
  - [Collab: Controlled Decoding using Mixture of Agents for LLM Alignment](https://proceedings.iclr.cc/paper_files/paper/2025/file/2e79dce47c5bbe738dff9c05ace8a037-Paper-Conference.pdf)
- **Linguistic quality** (construct): *measured_by*, 2 papers
  > Linguistic Quality: The response logical. The model correctly understands the medical task, and the expressions smooth and natural. (Section 4.2.4, The Prompt for GPT-4 to Rate the Performance of QA Tasks)
  - [MedJourney: Benchmark and Evaluation of Large Language Models over Patient Clinical Journey](https://proceedings.neurips.cc/paper_files/paper/2024/file/9f80af32390984cb709cdeb014d0df41-Paper-Datasets_and_Benchmarks_Track.pdf)
  - [Generalized Interpolating Discrete Diffusion](https://raw.githubusercontent.com/mlresearch/v267/main/assets/von-rutte25a/von-rutte25a.pdf)
- **Generalization** (construct): *measured_by*, 2 papers
  > “We focus on the GPT-4 evaluation since the reward model will not be accurate for the OOD data.”
  - [Aligning Large Language Models with Representation Editing: A Control Perspective](https://proceedings.neurips.cc/paper_files/paper/2024/file/41bba7b0f5c81e789a20bb16a370aeeb-Paper-Conference.pdf)
  - [PAD: Personalized Alignment of LLMs at Decoding-time](https://proceedings.iclr.cc/paper_files/paper/2025/file/196c8da9209b1977408d8771c4e7ee56-Paper-Conference.pdf)
- **Toxicity** (construct): *measured_by*, 2 papers
  > We evaluate Toxicity and Hallucination using GPT-4o OpenAI (2023) and Claude-3.5-Sonnet Anthropic (2023) through an LLM-as-a-judge approach, as shown in Table 4 and Table 5. (Section 4.7)
  - [PALMBENCH: A COMPREHENSIVE BENCHMARK OF COMPRESSED LARGE LANGUAGE MODELS ON MOBILE PLATFORMS](https://proceedings.iclr.cc/paper_files/paper/2025/file/a647405740b28a61311ac9cff28772e5-Paper-Conference.pdf)
  - [Controlling Language and Diffusion Models by Transporting Activations](https://proceedings.iclr.cc/paper_files/paper/2025/file/df4f6e43446b1ee29c5a33d32c279f83-Paper-Conference.pdf)
- **Narrative coherence** (construct): *measured_by*, 2 papers
  > In addition, we develop a LLM-based evaluator (Liusie et al., 2023; Liu et al., 2024; Zheng et al., 2024; Bohnet et al., 2024) to perform side-by-side comparisons of system output. We design prompts targeting the same dimensions of story quality adopted in our human evaluation (Section 6.2).
  - [Agents' Room: Narrative Generation through Multi-step Collaboration](https://proceedings.iclr.cc/paper_files/paper/2025/file/0fbc8a83d93dd8021a4dd8d2d34138eb-Paper-Conference.pdf)
  - [Unbounded: A Generative Infinite Game of Character Life Simulation](https://proceedings.iclr.cc/paper_files/paper/2025/file/da2411768acb844b255bb6770e5a71c7-Paper-Conference.pdf)
- **Tool use** (behavioral indicator): *measured_by*, 2 papers
  > Win Rate (Win%), which evaluates effectiveness through pairwise comparisons by a ChatGPT-based evaluator, capturing nuanced performance differences not reflected by rule-based metrics. (Section 3.1)
  - [From Exploration to Mastery: Enabling LLMs to Master Tools via Self-Driven Interactions](https://proceedings.iclr.cc/paper_files/paper/2025/file/8c22e5e918198702765ecff4b20d0a90-Paper-Conference.pdf)
  - [CIFLEX: Contextual Instruction Flow for Sub-task Execution in Multi-Turn Interactions with a Single On-Device LLM](https://aclanthology.org/2025.emnlp-main.533.pdf)
- **Informativeness** (construct): *measured_by*, 2 papers
  > We also train several judge models for informativeness following the same procedure as for truthfulness. (Section 3.2.4)
  - [Truth Knows No Language: Evaluating Truthfulness Beyond English](https://aclanthology.org/2025.acl-long.1507.pdf)
  - [TruthFlow: Truthful LLM Generation via Representation Flow Correction](https://raw.githubusercontent.com/mlresearch/v267/main/assets/wang25i/wang25i.pdf)
- **Personalized response generation** (behavioral indicator): *measured_by*, 2 papers
  > PAChat achieves the best results across all metrics, demonstrating significant improvements in personalized response generation and particularly winning favor with both GPT and human judges. (Section 5.3.1)
  - [PACHAT: Persona-Aware Speech Assistant for Multi-party Dialogue](https://aclanthology.org/2025.emnlp-main.1492.pdf)
  - [FaST: Feature-aware Sampling and Tuning for Personalized Preference Alignment with Limited Data](https://aclanthology.org/2025.emnlp-main.475.pdf)
- **Creativity** (construct): *measured_by*, 1 paper
  > we do LLM-based grading of samples before and after self-correction in terms of clarity, grammaticality, factuality, writing style, and creativity. (Sec. 5.4)
  - [Generalized Interpolating Discrete Diffusion](https://raw.githubusercontent.com/mlresearch/v267/main/assets/von-rutte25a/von-rutte25a.pdf)
- **Logical consistency** (construct): *measured_by*, 1 paper
  > We use DeepSeek R1 and ERNIE Bot 4.0 to quantitatively evaluate model outputs before and after training, focusing on logical consistency, clarity, and lack of ambiguity (Section 5)
  - [Theorem-Validated Reverse Chain-of-Thought Problem Generation for Geometric Reasoning](https://aclanthology.org/2025.emnlp-main.38.pdf)
- **Adequacy** (construct): *measured_by*, 1 paper
  > we propose an automatic evaluation metric based on GPT-4, which better assesses translation quality in terms of adequacy, fluency, and elegance, overcoming the limitations of traditional metrics. (Abstract)
  - [Benchmarking LLMs for Translating Classical Chinese Poetry: Evaluating Adequacy, Fluency, and Elegance](https://aclanthology.org/2025.emnlp-main.1678.pdf)
- **Knowledge graph completion** (behavioral indicator): *measured_by*, 1 paper
  > We conduct comprehensive experiments on two UrbanKGC tasks in two metropolises (New York City and Chicago) using both human evaluation and GPT-4-based self-evaluation. (Section 1)
  - [UrbanKGent: A Unified Large Language Model Agent Framework for Urban Knowledge Graph Construction](https://proceedings.neurips.cc/paper_files/paper/2024/file/decd42d78c42cea59c95c7c3d40d5e0f-Paper-Conference.pdf)
- **Dialogue generation** (behavioral indicator): *measured_by*, 1 paper
  > For the dialogue generation and summarization tasks, we use GPT-4 for zero-shot pairwise evaluation, which is consistent with human judgments (see prompts in Appendix C.2.1). (Section 5.1)
  - [Cal-DPO: Calibrated Direct Preference Optimization for Language Model Alignment](https://proceedings.neurips.cc/paper_files/paper/2024/file/cf8b2205e39f81726a8d828ecbe00ad0-Paper-Conference.pdf)
- **Counting** (behavioral indicator): *measured_by*, 1 paper
  > To assess this dimension, we query GPT-4V about the number of target objects in the image and compare its response with the human-annotated answer. (Sec. 3.1.1)
  - [I2EBench: A Comprehensive Benchmark for Instruction-based Image Editing](https://proceedings.neurips.cc/paper_files/paper/2024/file/48fecef47b19fe501d27d338b6d52582-Paper-Conference.pdf)
- **Image editing** (behavioral indicator): *measured_by*, 1 paper
  > To evaluate this dimension, we inquire whether GPT-4V identifies the presence of the target object in the image. (Sec. 3.1.1)
  - [I2EBench: A Comprehensive Benchmark for Instruction-based Image Editing](https://proceedings.neurips.cc/paper_files/paper/2024/file/48fecef47b19fe501d27d338b6d52582-Paper-Conference.pdf)
- **3D question answering** (behavioral indicator): *measured_by*, 1 paper
  > "we employ both human evaluators and GPT-4 to ascertain answer accuracy"
  - [MMScan: A Multi-Modal 3D Scene Dataset with Hierarchical Grounded Language Annotations](https://proceedings.neurips.cc/paper_files/paper/2024/file/5aed0d900297bd5593afc14ff452d4a8-Paper-Datasets_and_Benchmarks_Track.pdf)
- **Explanation quality** (construct): *measured_by*, 1 paper
  > Explanation quality, which denotes the correctness and policy adherence of the guardrail explanations. Specifically, we consider both GPT-4o as a judge (Zheng et al., 2023) and human evaluators... (Section 5.1)
  - [SafeWatch: An Efficient Safety-Policy Following Video Guardrail Model with Transparent Explanations](https://proceedings.iclr.cc/paper_files/paper/2025/file/beac6bfb7eac3d651307c16ac747df01-Paper-Conference.pdf)
- **Stereotyping** (construct): *measured_by*, 1 paper
  > Particularly, for the bias type of Stereotyping, we use GPT-4 to assess the stereotypical degree of LLM-generated outputs regarding any specific social group.
  - [CEB: Compositional Evaluation Benchmark for Fairness in Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/38e491559eb9e4cf31b8cd3a4e222436-Paper-Conference.pdf)
- **Multi-turn dialogue** (behavioral indicator): *measured_by*, 1 paper
  > To assess free-form questions and multiple-round conversations, we utilize the LLM-as-a-Judge methodology, which assigns a similarity score ranging from 1 to 5 between MLLM’s response and a predefined golden answer... (Section 3.1)
  - [GUI-World: A Video Benchmark and Dataset for Multimodal GUI-oriented Understanding](https://proceedings.iclr.cc/paper_files/paper/2025/file/3926df1a00c9abf056df7bcf253d026a-Paper-Conference.pdf)
- **Visual question answering** (behavioral indicator): *measured_by*, 1 paper
  > For VQA, we use a pretrained LLM to determine whether the prediction has semantically equivalent to the ground-truth while for captioning, we use GPT-3.5 to score the quality of the generated caption on a scale of score 1-10 (details in appendix). (Section 2.2)
  - [VL-ICL Bench: The Devil in the Details of Multimodal In-Context Learning](https://proceedings.iclr.cc/paper_files/paper/2025/file/f8a2070082ad05b4deeff4ffb4312a6f-Paper-Conference.pdf)
- **Robustness** (construct): *measured_by*, 1 paper
  > GPT-4 comparison for robustness (Figure 5 caption).
  - [Uncertainty and Influence aware Reward Model Refinement for Reinforcement Learning from Human Feedback](https://proceedings.iclr.cc/paper_files/paper/2025/file/fd7259e22add6de6df8ff0ccc902a34d-Paper-Conference.pdf)
- **Plausibility** (construct): *measured_by*, 1 paper
  > When evaluating the likelihood of the activity sequences, GPT-4o is instructed to take the following criteria into account: ... Plausibility: How reasonable, likely, or believable a sequence of actions is, given the circumstances, context, and known behavior patterns.
  - [Simulating Human-like Daily Activities with Desire-driven Autonomy](https://proceedings.iclr.cc/paper_files/paper/2025/file/513cb685f67550dbd133b81a7a24249f-Paper-Conference.pdf)
- **Text-image alignment** (construct): *measured_by*, 1 paper
  > Building on previous work (An et al., 2023; Liu et al., 2024d), we enhance the process by employing MLLM-as-a-Judge with golden answers and the "Analyze-then-Judge" Chain-of-Thought (CoT) (Wei et al., 2022). This allows for a more human-aligned evaluation, assessing generation quality, text-image alignment, and helpfulness to yield a comprehensive score.
  - [Interleaved Scene Graphs for Interleaved Text-and-Image Generation Assessment](https://proceedings.iclr.cc/paper_files/paper/2025/file/b9e0ceee9751ae8b5c6603c029e4ca42-Paper-Conference.pdf)
- **Video question answering** (behavioral indicator): *measured_by*, 1 paper
  > The second method involves models freely generating answers, which are then evaluated by GPT-4. Given the question, correct answer, and model’s prediction, GPT-4 returns a True or False judgment.
  - [MMWorld: Towards Multi-discipline Multi-faceted World Model Evaluation in Videos](https://proceedings.iclr.cc/paper_files/paper/2025/file/4364fef031fdf7bfd9d1c9c56b287084-Paper-Conference.pdf)
- **Video captioning** (behavioral indicator): *measured_by*, 1 paper
  > "For question-answering and caption generation tasks... GPT-4 is used to score the results."
  - [IDA-VLM: Towards Movie Understanding via ID-Aware Large Vision-Language Model](https://proceedings.iclr.cc/paper_files/paper/2025/file/82dcb6da1b408d59d15f68afdebf1489-Paper-Conference.pdf)
- **Expert evaluation** (measurement instrument): *correlates*, 1 paper
  > employ a combination of expert human evaluation and LLM-as-a-Judge (using GPT-4-turbo-2024-04-09)... has a higher correlation (≈0.97%) to expert human evaluations
  - [Visual Description Grounding Reduces Hallucinations and Boosts Reasoning in LVLMs](https://proceedings.iclr.cc/paper_files/paper/2025/file/a6805b5564bd8d813a81c4b5a97e5ca6-Paper-Conference.pdf)
- **Honesty** (construct): *measured_by*, 1 paper
  > “we conduct a one-shot ‘first-past-the-post’ (FPP)-style assessment with GPT-4o as the judge ... for quality ratings on a Likert scale between 1 to 5 ... including overall performance, honesty, helpfulness, truthfulness, and safety”
  - [DPL: Diverse Preference Learning Without A Reference Model](https://aclanthology.org/2025.naacl-long.190.pdf)
- **Argument quality** (construct): *measured_by*, 1 paper
  > For the win-rate, we prompt GPT-4 to decide which argument is superior, or if both are equally good. (Section 5.2)
  - [A Logical Fallacy-Informed Framework for Argument Generation](https://aclanthology.org/2025.naacl-long.374.pdf)
- **Semantic preservation** (construct): *measured_by*, 1 paper
  > “We use Llama3-8B-Instruct ... to evaluate the generated simplified text along three dimensions: meaning preservation, fluency, and simplicity.”
  - [Adapting Sentence-level Automatic Metrics for Document-level Simplification Evaluation](https://aclanthology.org/2025.naacl-long.327.pdf)
- **Simplicity** (construct): *measured_by*, 1 paper
  > “We use Llama3-8B-Instruct ... to evaluate the generated simplified text along three dimensions: meaning preservation, fluency, and simplicity.”
  - [Adapting Sentence-level Automatic Metrics for Document-level Simplification Evaluation](https://aclanthology.org/2025.naacl-long.327.pdf)
- **Idea generation** (behavioral indicator): *measured_by*, 1 paper
  > LLM-as-a-Judge idea evaluation (Table 4) evidences higher quality ideas when generations are grounded with MIR (Section 6.4)
  - [MIR: Methodology Inspiration Retrieval for Scientific Research Problems](https://aclanthology.org/2025.acl-long.1390.pdf)
- **Engagement** (construct): *measured_by*, 1 paper
  > We use GPT-4o to evaluate Engagingness, Humanness, and Memorability. (Section 4.1)
  - [Flexibly Utilize Memory for Long-Term Conversation via a Fragment-then-Compose Framework](https://aclanthology.org/2025.emnlp-main.1069.pdf)
- **Clarity** (construct): *measured_by*, 1 paper
  > we do LLM-based grading of samples before and after self-correction in terms of clarity, grammaticality, factuality, writing style, and creativity. (Sec. 5.4)
  - [Generalized Interpolating Discrete Diffusion](https://raw.githubusercontent.com/mlresearch/v267/main/assets/von-rutte25a/von-rutte25a.pdf)
- **Multimodal alignment** (construct): *measured_by*, 1 paper
  > GPT-4V (Achiam et al., 2023b), which assesses the fluency and alignment of captions with the given images.
  - [What If We Recaption Billions of Web Images with LLaMA-3?](https://raw.githubusercontent.com/mlresearch/v267/main/assets/li25ch/li25ch.pdf)
- **Image generation** (behavioral indicator): *measured_by*, 1 paper
  > following the GPT-4V metric introduced in Section 4.2, we randomly select a subset of 3,000 our generated images for GPT-4V evaluation.
  - [What If We Recaption Billions of Web Images with LLaMA-3?](https://raw.githubusercontent.com/mlresearch/v267/main/assets/li25ch/li25ch.pdf)
- **Reasoning quality** (construct): *measured_by*, 1 paper
  > For recall, we prompt GPT-4o to match each key step annotation in the prediction. For precision, GPT-4o is instructed to split the prediction into steps and determine the correctness of all the image caption and logical inference steps. (Figure 4)
  - [MME-CoT: Benchmarking Chain-of-Thought in Large Multimodal Models for Reasoning Quality, Robustness, and Efficiency](https://raw.githubusercontent.com/mlresearch/v267/main/assets/jiang25n/jiang25n.pdf)
- **Long-form text generation** (behavioral indicator): *measured_by*, 1 paper
  > the evaluation metrics of instruction-following tasks, especially those that require long-form generations (e.g., LLM-judge (Dubois et al., 2023) and code generation benchmarks (Chen et al., 2021)).
  - [NICE Data Selection for Instruction Tuning in LLMs with Non-differentiable Evaluation Metric](https://raw.githubusercontent.com/mlresearch/v267/main/assets/wang25bm/wang25bm.pdf)
- **Controllability** (construct): *measured_by*, 1 paper
  > For the latter, we use an LLM judge to rate steered outputs on three relevant axes (see §3.3).
  - [AxBench: Steering LLMs? Even Simple Baselines Outperform Sparse Autoencoders](https://raw.githubusercontent.com/mlresearch/v267/main/assets/wu25a/wu25a.pdf)
- **Interactivity** (construct): *measured_by*, 1 paper
  > Interactivity (ITR), which evaluates engagement levels using an LLM judge (Claude-3.5-Sonnet), with scores rescaled to an upper bound of 1.
  - [CollabLLM: From Passive Responders to Active Collaborators](https://raw.githubusercontent.com/mlresearch/v267/main/assets/wu25i/wu25i.pdf)
- **Reward hacking** (behavioral indicator): *measured_by*, 1 paper
  > "we use AI feedback to identify hacking samples following Miao et al. (2024). Speciﬁcally, we ﬁrst outline common hacking behaviors ... and then use GPT-4 to evaluate responses based on these criteria"
  - [The Energy Loss Phenomenon in RLHF: A New Perspective on Mitigating Reward Hacking](https://raw.githubusercontent.com/mlresearch/v267/main/assets/miao25c/miao25c.pdf)
- **Trend analysis** (behavioral indicator): *measured_by*, 1 paper
  > GPT-4o rates the generated trend descriptions on a scale of 1 to 5 (with 5 being the highest) by comparing each output to ground truth and providing explanatory feedback.
  - [SensorLLM: Aligning Large Language Models with Motion Sensors for Human Activity Recognition](https://aclanthology.org/2025.emnlp-main.19.pdf)
- **Verbal uncertainty** (construct): *measured_by*, 1 paper
  > We follow recent work in expression decisiveness quantification and employ "LLM-as-a-Judge" to measure VU (Yona et al., 2024; Zheng et al., 2023). (Section 2.2)
  - [Calibrating Verbal Uncertainty as a Linear Feature to Reduce Hallucinations](https://aclanthology.org/2025.emnlp-main.187.pdf)
- **Disambiguation ability** (construct): *measured_by*, 1 paper
  > Therefore, we design a prompt to evaluate the disambiguation capability of LLMs using GPT-4o-mini7. (Section 2.4)
  - [DMDTEval: An Evaluation and Analysis of LLMs on Disambiguation in Multi-domain Translation](https://aclanthology.org/2025.emnlp-main.309.pdf)
- **Novelty** (construct): *measured_by*, 1 paper
  > In addition to assessing the effectiveness of hypotheses in downstream task usage, we also evaluate their helpfulness (Liu et al., 2024) and novelty (Liu et al., 2024; Si et al., 2024) through LLM-based metrics. (Section 4.2)
  - [On the Role of Model Prior in Real-World Inductive Reasoning](https://aclanthology.org/2025.emnlp-main.534.pdf)
- **Textual aesthetics** (construct): *measured_by*, 1 paper
  > we employ the 'LLM-as-a-judge' framework to approximate human preferences for text aesthetics.
  - [Textual Aesthetics in Large Language Models](https://aclanthology.org/2025.emnlp-main.696.pdf)
- **Comprehensiveness** (construct): *measured_by*, 1 paper
  > The evaluation framework uses multi-perspective criteria by LLM-as-a-judge, such as comprehensiveness, specificity, and relevance. (Section 1)
  - [Multi-perspective Analysis of Large Language Model Domain Specialization: An Experiment in Accounting Audit Procedures Generation](https://aclanthology.org/2025.emnlp-main.891.pdf)
- **Specificity** (construct): *measured_by*, 1 paper
  > The evaluation framework uses multi-perspective criteria by LLM-as-a-judge, such as comprehensiveness, specificity, and relevance. (Section 1)
  - [Multi-perspective Analysis of Large Language Model Domain Specialization: An Experiment in Accounting Audit Procedures Generation](https://aclanthology.org/2025.emnlp-main.891.pdf)
- **Reasoning** (construct): *measured_by*, 1 paper
  > Reasoning-based skills are assessed using a GPT-4o mini, assigning a score from 0 to 10.
  - [InfiniBench: A Benchmark for Large Multi-Modal Models in Long-Form Movies and TV Shows](https://aclanthology.org/2025.emnlp-main.984.pdf)
- **Prompt sensitivity** (construct): *measured_by*, 1 paper
  > To rigorously assess whether LLMs truly suffer from prompt sensitivity, we revisit this issue using a more robust evaluation strategy: LLMs as judges.
  - [Flaw or Artifact? Rethinking Prompt Sensitivity in Evaluating LLMs](https://aclanthology.org/2025.emnlp-main.1006.pdf)
- **Machine translation** (behavioral indicator): *measured_by*, 1 paper
  > Table 2 shows that large language models effectively evaluate classical Chinese poetry translation... (Section 7.1)
  - [Benchmarking LLMs for Translating Classical Chinese Poetry: Evaluating Adequacy, Fluency, and Elegance](https://aclanthology.org/2025.emnlp-main.1678.pdf)
- **Persuasiveness** (construct): *measured_by*, 1 paper
  > Essays are evaluated across five dimensions: ... (4) Persuasiveness... we adopt a GPT-4o-based evaluation framework for more consistent, human-aligned assessments. (Section 4.2)
  - [Plan Dynamically, Express Rhetorically: A Debate-Driven Rhetorical Framework for Argumentative Writing](https://aclanthology.org/2025.emnlp-main.483.pdf)
- **Abstention** (behavioral indicator): *measured_by*, 1 paper
  > A pretrained LLM-as-judge labels responses as either abstention (clarification or refusal) or direct answer... (Section 4.1)
  - [Sparse Neurons Carry Strong Signals of Question Ambiguity in LLMs](https://aclanthology.org/2025.emnlp-main.813.pdf)
- **Direct answering** (behavioral indicator): *measured_by*, 1 paper
  > A pretrained LLM-as-judge labels responses as either abstention (clarification or refusal) or direct answer... (Section 4.1)
  - [Sparse Neurons Carry Strong Signals of Question Ambiguity in LLMs](https://aclanthology.org/2025.emnlp-main.813.pdf)
- **Coverage** (construct): *measured_by*, 1 paper
  > We address coverage by instructing an LLM to count the number of reference summaries covered by a set of candidate summaries. (Section 3.5)
  - [Argument Summarization and its Evaluation in the Era of Large Language Models](https://aclanthology.org/2025.emnlp-main.1797.pdf)
- **Redundancy** (construct): *measured_by*, 1 paper
  > To assess redundancy, we instruct an LLM to count the number of unique main statements within a set of candidate summaries. (Section 3.5)
  - [Argument Summarization and its Evaluation in the Era of Large Language Models](https://aclanthology.org/2025.emnlp-main.1797.pdf)
- **Cultural text adaptation** (behavioral indicator): *measured_by*, 1 paper
  > To measure the cultural competence of LLMs on a cultural text adaptation task, we evaluate the adaptations using the CSIs created, LLM as Judge, and human evaluations from diverse socio-demographic region. (Abstract)
  - [DIWALI - Diversity and Inclusivity aWare cuLture specific Items for India: Dataset and Assessment of LLMs for Cultural Text Adaptation in Indian Context](https://aclanthology.org/2025.emnlp-main.1706.pdf)
- **Definition generation** (behavioral indicator): *measured_by*, 1 paper
  > we employ a Large Language Model (LLM) as a judge (LLM-as-a-Judge) (Gu et al., 2024) to provide qualitative insights into the quality of generated descriptions (Section 5.4).
  - [RAED: Retrieval-Augmented Entity Description Generation for Emerging Entity Linking and Disambiguation](https://aclanthology.org/2025.emnlp-main.1746.pdf)
- **Knowledge** (construct): *measured_by*, 1 paper
  > “Knowledge Capability (KC), which leverages Qwen1.5-32B (Bai et al., 2023a) to evaluate the correctness of knowledge presented in answers.”
  - [SEFE: Superficial and Essential Forgetting Eliminator for Multimodal Continual Instruction Tuning](https://raw.githubusercontent.com/mlresearch/v267/main/assets/chen25n/chen25n.pdf)

### Associated with
- **WildBench** (measurement instrument), 2 papers
  > We use the public dataset from Wildbench (Lin et al., 2024) to obtain our LLM-based evaluation. (Section 4.2)
  - [Polyrating: A Cost-Effective and Bias-Aware Rating System for LLM Evaluation](https://proceedings.iclr.cc/paper_files/paper/2025/file/d06537b4b38ccf008a54559d2c56fa23-Paper-Conference.pdf)
  - [Diverging Preferences: When do Annotators Disagree and do Models Know?](https://raw.githubusercontent.com/mlresearch/v267/main/assets/zhang25bx/zhang25bx.pdf)
- **MT-Bench** (measurement instrument), 1 paper
  > MT Bench (Zheng et al., 2023) with 160 open-ended questions using LLM-as-a-judge (Section 5)
  - [RouteLLM: Learning to Route LLMs from Preference Data](https://proceedings.iclr.cc/paper_files/paper/2025/file/5503a7c69d48a2f86fc00b3dc09de686-Paper-Conference.pdf)
- **Pairwise comparison** (behavioral indicator), 1 paper
  > We explore two typical LLM-as-a-judge methods: Pairwise comparison (Section 2.1)
  - [Varying Shades of Wrong: Aligning LLMs with Wrong Answers Only](https://proceedings.iclr.cc/paper_files/paper/2025/file/1aa1fde3661b23ba9b043082069fd144-Paper-Conference.pdf)
- **Prompt robustness** (construct), 1 paper
  > When we adopt LLM-as-a-Judge evaluations, we observe a substantial reduction in performance variance and a consistently higher correlation in model rankings across prompts. Our findings suggest that modern LLMs are more robust to prompt templates than previously believed...
  - [Flaw or Artifact? Rethinking Prompt Sensitivity in Evaluating LLMs](https://aclanthology.org/2025.emnlp-main.1006.pdf)
- **FLASK** (measurement instrument), 1 paper
  > “FLASK (Fine-grained Language Model Evaluation based on Alignment SKill Sets), a fine-grained evaluation protocol for both human-based and model-based evaluation”
  - [FLASK: Fine-grained Language Model Evaluation based on Alignment Skill Sets](https://proceedings.iclr.cc/paper_files/paper/2024/file/f41b4a6b202adcd8e150a9d4f124d8f6-Paper-Conference.pdf)
- **EHRNoteQA** (measurement instrument), 1 paper
  > “For open-ended QA, we use GPT-4 to evaluate the model outputs instead of using traditional methods such BLEU or ROUGE-L”
  - [EHRNoteQA: An LLM Benchmark for Real-World Clinical Practice Using Discharge Summaries](https://proceedings.neurips.cc/paper_files/paper/2024/file/e15c4afff22f12c4986c1fcb4e941e03-Paper-Datasets_and_Benchmarks_Track.pdf)
- **Preference prediction** (behavioral indicator), 1 paper
  > "using an LLM’s predictions to approximate human preferences between them, a technique often referred to as LLM-as-judge"
  - [Spread Preference Annotation: Direct Preference Judgment for Efficient LLM Alignment](https://proceedings.iclr.cc/paper_files/paper/2025/file/342e5fc02b86dec9b24e41b22968e539-Paper-Conference.pdf)
- **FaithEval** (measurement instrument), 1 paper
  > “we validate the quality of the new context by using a separate LLM judge to verify whether the new answer is valid given the context”
  - [FaithEval: Can Your Language Model Stay Faithful to Context, Even If "The Moon is Made of Marshmallows"](https://proceedings.iclr.cc/paper_files/paper/2025/file/48404cd9ce03946c6b7177691f3267a1-Paper-Conference.pdf)
- **LLMBar** (measurement instrument), 1 paper
  > "We evaluate CAMIEVAL on two benchmarks, LLMBar (Zeng et al., 2023) and InstruSum (Liu et al., 2023c), which respectively represent pairwise evaluation of instruction-following and pointwise scoring of instruction controllable summarization."
  - [CAMIEval: Enhancing NLG Evaluation through Multidimensional Comparative Instruction-Following Analysis](https://aclanthology.org/2025.naacl-long.438.pdf)
- **Evaluation bias** (construct), 1 paper
  > “Agents-as-an-Evaluator exhibit two biases: data bias and model bias.”
  - [Unbiased Evaluation of Large Language Models from a Causal Perspective](https://raw.githubusercontent.com/mlresearch/v267/main/assets/chen25bi/chen25bi.pdf)
- **MUCAR** (measurement instrument), 1 paper
  > “MUCAR is the first benchmark to comprehensively address visual ambiguity, contextual ambiguity, and multilinguality, while integrating both human and GPT-based evaluation.”
  - [MUCAR: Benchmarking Multilingual Cross-Modal Ambiguity Resolution for Multimodal Large Language Models](https://aclanthology.org/2025.emnlp-main.760.pdf)
- **ResumeBench-Mix** (measurement instrument), 1 paper
  > "we employ widely used common metrics for machine generated text ... as well as using a LLM-as-a-judge way to validate the dataset with 20% of samples in Resumebench-Mix"
  - [Beyond Human Labels: A Multi-Linguistic Auto-Generated Benchmark for Evaluating Large Language Models on Resume Parsing](https://aclanthology.org/2025.emnlp-main.1626.pdf)
