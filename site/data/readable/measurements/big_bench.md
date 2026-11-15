# BIG-bench
**Type:** Measurement instrument  
**Supporting papers:** 42  
**Also known as:** BIG-BENCH, BIG-Bench, Big-Bench, Big-bench, BigBench  

## State of the Field

**What it is.** Across these papers, the prevailing usage treats BIG-bench as a large, collaborative evaluation suite, usually described as Beyond the Imitation Game, with 204 or over 200 diverse tasks for probing the capabilities and limitations of language models. Definitions vary in emphasis: some highlight reasoning and comprehension tasks, others say it covers both traditional NLP tasks and novel problems, and several papers use narrower slices such as BIG-BENCH LITE, the BBII subset, the verb tense subset, or single tasks such as Date Understanding and Sudoku.

**What it is claimed to measure.** Papers link BIG-bench to 6 constructs and 4 behavioral indicators, so its reported measurement role spans multiple targets. The construct links are measured_by claims, with papers using it to measure Calibration, Emergent abilities, Logical reasoning, and Social bias, plus 2 other constructs. Behavioral uses are also reported, including Multi-digit multiplication, plus 3 other indicators, and one of those behavioral links is only related rather than measured by the benchmark.

**Space of uses.** Most commonly, papers position BIG-bench as a broad benchmark or as a source of subtasks for targeted evaluations. Papers use it alongside MMLU, and some place it beside HELM, the instruction induction benchmark, or CrowS-Pairs. Papers also link it to one other instrument, Date Understanding, which one study uses as a testbed drawn from BIG-bench; elsewhere the benchmark is used as a seed dataset for updated evaluations or as a source of reasoning tasks.

**Concerns raised.** Direct concerns are sparse. One paper groups BIG-Bench with other knowledge-based and logic-based benchmarks as failing to capture nuanced human preferences.

## Sources

**BIG-Bench** (12 papers: [Large Language Models as Analogical Reasoners](https://proceedings.iclr.cc/paper_files/paper/2024/file/4990dad2c1696224de42573d0222554a-Paper-Conference.pdf), [AutoBencher: Towards Declarative Benchmark Construction](https://proceedings.iclr.cc/paper_files/paper/2025/file/eb216114f3eaad22506fd1bc7bbff0ca-Paper-Conference.pdf), [Interpret and Improve In-Context Learning via the Lens of Input-Label Mappings](https://aclanthology.org/2025.acl-long.196.pdf), [Automating Dataset Updates Towards Reliable and Timely Evaluation of Large Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/1e89c12621c0315373f20f0aeabe5dbe-Paper-Datasets_and_Benchmarks_Track.pdf), [Buffer of Thoughts: Thought-Augmented Reasoning with Large Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/cde328b7bf6358f5ebb91fe9c539745e-Paper-Conference.pdf), [Cross-Care: Assessing the Healthcare Implications of Pre-training Data on Language Model Bias](https://proceedings.neurips.cc/paper_files/paper/2024/file/2a617efee5815f12b405d40569dea0a5-Paper-Datasets_and_Benchmarks_Track.pdf), [Diffusion of Thought: Chain-of-Thought Reasoning in Diffusion Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/be30024e7fa2c29cac7a6dafcbb8571f-Paper-Conference.pdf), [Enhancing LLM Reasoning via Vision-Augmented Prompting](https://proceedings.neurips.cc/paper_files/paper/2024/file/328c922d068dd4ccb23cec5c64e6c7fc-Paper-Conference.pdf), [GameTraversalBenchmark: Evaluating Planning Abilities Of Large Language Models Through Traversing 2D Game Maps](https://proceedings.neurips.cc/paper_files/paper/2024/file/3852c8254bc6d904c09db9921157f59b-Paper-Datasets_and_Benchmarks_Track.pdf), [Preference Learning Algorithms Do Not Learn Preference Rankings](https://proceedings.neurips.cc/paper_files/paper/2024/file/b8ce770a6b25e603fbff4a37f9e31edc-Paper-Conference.pdf), [Symbolic Regression with a Learned Concept Library](https://proceedings.neurips.cc/paper_files/paper/2024/file/4ec3ddc465c6d650c9c419fb91f1c00a-Paper-Conference.pdf), [WizardArena: Post-training Large Language Models via Simulated Offline Chatbot Arena](https://proceedings.neurips.cc/paper_files/paper/2024/file/ca4aa9acc097e0f606af55bf986cb031-Paper-Conference.pdf))
> Comprehensive evaluation suite containing diverse reasoning tasks such as logical deduction, temporal sequences, and formal fallacies, designed to test a wide range of cognitive abilities in language models.

**BigBench** (6 papers: [Predicting Emergent Abilities with Infinite Resolution Evaluation](https://proceedings.iclr.cc/paper_files/paper/2024/file/4e6d14709eae0cbc49a1d19d87fb8b21-Paper-Conference.pdf), [Divide and Translate: Compositional First-Order Logic Translation and Verification for Complex Logical Reasoning](https://proceedings.iclr.cc/paper_files/paper/2025/file/3e592c571de69a43d7a870ea89c7e33a-Paper-Conference.pdf), [Position: Societal Impacts Research Requires Benchmarks for Creative Composition Tasks](https://raw.githubusercontent.com/mlresearch/v267/main/assets/shen25r/shen25r.pdf), [Arena-lite: Efficient and Reliable Large Language Model Evaluation via Tournament-Based Direct Comparisons](https://aclanthology.org/2025.emnlp-main.360.pdf), [No Free Delivery Service: Epistemic limits of passive data collection in complex social systems](https://proceedings.neurips.cc/paper_files/paper/2024/file/b97fc02c9e536d68300d82be05c23aa2-Paper-Conference.pdf), [Observational Scaling Laws and the Predictability of Langauge Model Performance](https://proceedings.neurips.cc/paper_files/paper/2024/file/1cded4f97cf5f01a284c574110b7e3b9-Paper-Conference.pdf))
> A diverse evaluation suite for large language models that includes a wide range of challenging tasks, used here to study in-context learning and emergent abilities.

**BIG-BENCH** (1 paper: [Evaluating the Zero-shot Robustness of Instruction-tuned Language Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/d3221cdb27e49d9c1cd35ad254feccfe-Paper-Conference.pdf))
> Beyond the Imitation Game benchmark, a collaboratively built benchmark of 204 diverse tasks from various domains; the paper uses the BIG-BENCH LITE subset focusing on QA, classification, and translation tasks.

**Big-Bench** (1 paper: [Large Language Models as Tool Makers](https://proceedings.iclr.cc/paper_files/paper/2024/file/ed91353f700d113e5d848c7e04a858b0-Paper-Conference.pdf))
> A benchmark suite containing a wide range of challenging tasks designed to measure the capabilities of large language models, including reasoning and comprehension.

**BIG-bench** (3 papers: [PiCO: Peer Review in LLMs based on Consistency Optimization](https://proceedings.iclr.cc/paper_files/paper/2025/file/39e9c5913c970e3e49c2df629daff636-Paper-Conference.pdf), [Hyperband-based Bayesian Optimization for Black-box Prompt Selection](https://raw.githubusercontent.com/mlresearch/v267/main/assets/schneider25b/schneider25b.pdf), [Steering Language Models in Multi-Token Generation: A Case Study on Tense and Aspect](https://aclanthology.org/2025.emnlp-main.435.pdf))
> Beyond the Imitation Game benchmark (BIG-bench) is a collaborative benchmark comprising 204 diverse tasks designed to probe the capabilities and limitations of large language models.

**Big-bench** (1 paper: [Is Your Model Really A Good Math Reasoner? Evaluating Mathematical Reasoning with Checklist](https://proceedings.iclr.cc/paper_files/paper/2025/file/54d2d38a56a74387d5916ee40e462295-Paper-Conference.pdf))
> A large, collaborative benchmark suite for language models, from which the 'date understanding' task is used as a testbed for commonsense reasoning.

## Relationships

### → BIG-bench
- **Word sorting** (behavioral indicator): *measured_by*, 1 paper
  > We further evaluate on various reasoning tasks in BIG-Bench (Srivastava et al., 2022; Suzgun et al., 2022): word sorting, logical deduction five objects, temporal sequences, reasoning about colored objects, and formal fallacies. (Section 5.1)
  - [Large Language Models as Analogical Reasoners](https://proceedings.iclr.cc/paper_files/paper/2024/file/4990dad2c1696224de42573d0222554a-Paper-Conference.pdf)
- **Logical reasoning** (construct): *measured_by*, 1 paper
  > "We further evaluate on various reasoning tasks in BIG-Bench (Srivastava et al., 2022; Suzgun et al., 2022): word sorting, logical deduction five objects, temporal sequences, reasoning about colored objects, and formal fallacies."
  - [Large Language Models as Analogical Reasoners](https://proceedings.iclr.cc/paper_files/paper/2024/file/4990dad2c1696224de42573d0222554a-Paper-Conference.pdf)
- **Temporal reasoning** (construct): *measured_by*, 1 paper
  > "We further evaluate on various reasoning tasks in BIG-Bench (Srivastava et al., 2022; Suzgun et al., 2022): word sorting, logical deduction five objects, temporal sequences, reasoning about colored objects, and formal fallacies."
  - [Large Language Models as Analogical Reasoners](https://proceedings.iclr.cc/paper_files/paper/2024/file/4990dad2c1696224de42573d0222554a-Paper-Conference.pdf)
- **Social bias** (construct): *measured_by*, 1 paper
  > Probability-based bias evaluations such as CrowS-Pairs [22] and tasks in the BIG-bench benchmarking suite [48] compare the probabilities of stereotype-related tokens conditional on the presence of identity-related tokens. (Section 2.2)
  - [Cross-Care: Assessing the Healthcare Implications of Pre-training Data on Language Model Bias](https://proceedings.neurips.cc/paper_files/paper/2024/file/2a617efee5815f12b405d40569dea0a5-Paper-Datasets_and_Benchmarks_Track.pdf)
- **Table question answering** (behavioral indicator): *measured_by*, 1 paper
  > Three reasoning tasks directly obtained from the BIG-Bench suite [50]: ... Penguins—where the task is to answer questions about penguins' attributes based on a given table
  - [Buffer of Thoughts: Thought-Augmented Reasoning with Large Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/cde328b7bf6358f5ebb91fe9c539745e-Paper-Conference.pdf)
- **Stability** (construct): *measured_by*, 1 paper
  > "Extensive experiments on updated MMLU and BIG-Bench demonstrate the stability of the proposed strategies"
  - [Automating Dataset Updates Towards Reliable and Timely Evaluation of Large Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/1e89c12621c0315373f20f0aeabe5dbe-Paper-Datasets_and_Benchmarks_Track.pdf)
- **Calibration** (construct): *measured_by*, 1 paper
  > Table 2 shows the performance of the posthoc calibrators on MMLU and BigBench datasets.
  - [QA-Calibration of Language Model Confidence Scores](https://proceedings.iclr.cc/paper_files/paper/2025/file/cd96cb9a239c37b39dbf34f3f5a4c56f-Paper-Conference.pdf)
- **Emergent abilities** (construct): *measured_by*, 1 paper
  > Fig. 4 shows U-shaped and inverted-U scaling on 6 datasets exhibiting emergent abilities... Except for MMLU, the other 5 tasks are from Big-Bench.
  - [U-shaped and Inverted-U Scaling behind Emergent Abilities of Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/f696200311b445af686c3ebd87ade1d7-Paper-Conference.pdf)
- **Multi-digit multiplication** (behavioral indicator): *measured_by*, 1 paper
  > "we first consider the multi-digit multiplication task from the BIG-bench benchmark"
  - [Seq-VCR: Preventing Collapse in Intermediate Transformer Representations for Enhanced Reasoning](https://proceedings.iclr.cc/paper_files/paper/2025/file/b577c062bd4f894b7e05fab6440373ed-Paper-Conference.pdf)

### Associated with
- **Object counting** (behavioral indicator), 1 paper
  > Adapted from BIG-bench (Bench authors, 2023), this task tests object classification and counting. (Section 4.3)
  - [A Causal Lens for Evaluating Faithfulness Metrics](https://aclanthology.org/2025.emnlp-main.1496.pdf)
- **Date Understanding** (measurement instrument), 1 paper
  > "We choose the date understanding task in Big-bench (bench authors, 2023) as testbed since it is wildly used to measure commonsense reasoning ability"
  - [Is Your Model Really A Good Math Reasoner? Evaluating Mathematical Reasoning with Checklist](https://proceedings.iclr.cc/paper_files/paper/2025/file/54d2d38a56a74387d5916ee40e462295-Paper-Conference.pdf)
