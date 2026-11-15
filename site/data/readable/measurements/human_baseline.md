# Human baseline
**Type:** Measurement instrument  
**Supporting papers:** 30  
**Also known as:** Human performance evaluation, Human performance study, Human-baseline study, Human experiment, Human CAI study, Human expert forecasts, Professional Nutritionist Study, Expert user study, Human validation study, Offline human survey, Human baseline evaluation, Human performance comparison, Human-level baseline, Human performance validation, Human benchmark  

## State of the Field

**What it is.** Across papers, the prevailing usage is not a single standardized benchmark but a family of human performance reference protocols. Most commonly, humans attempt the same benchmark tasks as models or agents so papers can establish a baseline for performance, success rate, efficiency, time, or accuracy. Some papers define it more narrowly as independent annotators manually synchronizing multilingual tables, a linguist creating vowel prediction baselines, native speakers or untrained annotators labeling benchmark subsets, an offline clue-by-clue survey with guesses and "buzz" decisions, or humans acting as LLM agents to estimate an upper bound. Several versions are run on subsets rather than full benchmarks, including 100 table-updating pairs, 75 abstracts, 1000 questions, and 35-40 held-out questions.

**What it is claimed to measure.** Papers do not formally link this instrument to any constructs or behavioral indicators. Instead, they use it to measure human task performance for comparison with model outputs, variously reporting success rate and efficiency, performance, time and accuracy, argument classification performance, answerability on document questions, or expert forecasting accuracy. Rather than being tied to a recurring construct, the papers frame it as a benchmark-specific reference for how people perform the task at hand.

**Space of uses.** It is linked to two other instruments, OSWorld and Bongard Problems, and papers describe it as related to those benchmarks. The dominant positioning is as a comparison point for humans versus models or agents, but some papers use it as an upper-bound reference, to contextualize LLM scores, or to verify that benchmark items are answerable by people. In the OSWorld link, a paper reports that the human performance study showed its examples were more time-consuming and challenging than prior work, while the Bongard Problems link appears in a participant-based human performance evaluation.

**Concerns raised.** The clearest limitation papers state is practical scope. One study says its human baseline covered only 100 randomly selected table-updating pairs "due to cost and time constraints," and several other papers also run human baselines on selected subsets of items rather than full benchmarks.

## Sources

**Human baseline** (2 papers: [Leveraging LLM For Synchronizing Information Across Multilingual Tables](https://aclanthology.org/2025.naacl-long.329.pdf), [Tonguescape: Exploring Language Models Understanding of Vowel Articulation](https://aclanthology.org/2025.naacl-long.627.pdf))
> A human performance benchmark for information updating, derived from independent annotators manually synchronizing tables, used to compare model outputs on a subset of 100 examples.

**Human performance evaluation** (4 papers: [VideoWebArena: Evaluating Long Context Multimodal Agents with Video Understanding Web Tasks](https://proceedings.iclr.cc/paper_files/paper/2025/file/5b555804d495321df2e3208cc27f4fbc-Paper-Conference.pdf), [Windows Agent Arena: Evaluating Multi-Modal OS Agents at Scale](https://raw.githubusercontent.com/mlresearch/v267/main/assets/bonatti25a/bonatti25a.pdf), [GuessingGame: Measuring the Informativeness of Open-Ended Questions in Large Language Models](https://aclanthology.org/2025.emnlp-main.876.pdf), [SciEvent: Benchmarking Multi-domain Scientific Event Extraction](https://aclanthology.org/2025.emnlp-main.871.pdf))
> A protocol where human participants attempt tasks from the benchmark to establish a baseline for success rates and efficiency, with evaluation conducted by a third party.

**Human performance study** (1 paper: [OSWorld: Benchmarking Multimodal Agents for Open-Ended Tasks in Real Computer Environments](https://proceedings.neurips.cc/paper_files/paper/2024/file/5d413e48f84dc61244b6be550f1cd8f5-Paper-Datasets_and_Benchmarks_Track.pdf))
> An evaluation protocol where human participants (computer science students) perform the benchmark tasks to establish a baseline for performance, time, and accuracy.

**Human experiment** (1 paper: [Probing LLM World Models: Enhancing Guesstimation with Wisdom of Crowds Decoding](https://aclanthology.org/2025.emnlp-main.234.pdf))
> A study conducted with human participants to establish a baseline for Wisdom of Crowds effects in guesstimation tasks and to compare human performance with that of LLMs.

**Human CAI study** (1 paper: [Can LLMs Help You at Work? A Sandbox for Evaluating LLM Agents in Enterprise Environments](https://aclanthology.org/2025.emnlp-main.466.pdf))
> A human evaluation in which human participants acted as LLM agents to complete EnterpriseBench tasks, used to measure upper-bound performance and compare against model agents.

**Human expert forecasts** (1 paper: [Position: LLM Social Simulations Are a Promising Research Method](https://raw.githubusercontent.com/mlresearch/v267/main/assets/anthis25a/anthis25a.pdf))
> An evaluation protocol where human experts predict research outcomes, used as a performance baseline to compare against LLM simulation accuracy.

**Professional Nutritionist Study** (1 paper: [NutriBench: A Dataset for Evaluating Large Language Models in Nutrition Estimation from Meal Descriptions](https://proceedings.iclr.cc/paper_files/paper/2025/file/ef3a57e4f26b640e6f90d78cbb011feb-Paper-Conference.pdf))
> A human evaluation procedure where professional nutritionists provide carbohydrate estimates for a subset of meal descriptions to compare against LLM performance.

**Expert user study** (1 paper: [Automated Hypothesis Validation with Agentic Sequential Falsifications](https://raw.githubusercontent.com/mlresearch/v267/main/assets/huang25n/huang25n.pdf))
> A human evaluation protocol where domain experts, such as computational biologists, perform a task like hypothesis validation, and their performance and process are compared against an automated system.

**Human validation study** (1 paper: [MOSAIC: Modeling Social AI for Content Dissemination and Regulation in Multi-Agent Simulations](https://aclanthology.org/2025.emnlp-main.325.pdf))
> A user study with 204 participants recruited via Prolific, comparing human and agent engagement behaviors on curated social media snapshots containing factual and false news articles.

**Offline human survey** (1 paper: [GRACE: A Granular Benchmark for Evaluating Model Calibration against Human Calibration](https://aclanthology.org/2025.acl-long.962.pdf))
> A data collection procedure where human participants view a sequence of clues for held-out questions and submit a guess after each clue, also indicating whether they would choose to 'buzz' at that point.

**Human baseline evaluation** (2 papers: [Can LLMs Solve Molecule Puzzles? A Multimodal Benchmark for Molecular Structure Elucidation](https://proceedings.neurips.cc/paper_files/paper/2024/file/f2b9e8e7a36d43ddfd3d55113d56b1e0-Paper-Datasets_and_Benchmarks_Track.pdf), [SciFIBench: Benchmarking Large Multimodal Models for Scientific Figure Interpretation](https://proceedings.neurips.cc/paper_files/paper/2024/file/217bb44ab14621754db8a392163e6b07-Paper-Datasets_and_Benchmarks_Track.pdf))
> An evaluation protocol where human experts (six Ph.D. candidates in chemistry) solve puzzles from the MolPuzzle benchmark to establish a performance baseline for comparison with LLMs.

**Human performance comparison** (1 paper: [NYU CTF Bench: A Scalable Open-Source Benchmark Dataset for Evaluating LLMs in Offensive Security](https://proceedings.neurips.cc/paper_files/paper/2024/file/69d97a6493fbf016fff0a751f253ad18-Paper-Datasets_and_Benchmarks_Track.pdf))
> An evaluation protocol comparing LLM scores on CTF challenges against scores achieved by human participants in the same competitions.

**Human-level baseline** (1 paper: [Optimus-1: Hybrid Multimodal Memory Empowered Agents Excel in Long-Horizon Tasks](https://proceedings.neurips.cc/paper_files/paper/2024/file/5949a8750a110ce1f0631b1776c500a2-Paper-Conference.pdf))
> An evaluation protocol where 10 human volunteers perform the benchmark tasks to establish a performance reference point.

**Human performance validation** (1 paper: [WildDoc: How Far Are We from Achieving Comprehensive and Robust Document Understanding in the Wild?](https://aclanthology.org/2025.emnlp-main.1172.pdf))
> An evaluation protocol to verify dataset answerability by measuring human accuracy on a randomly selected subset of questions and corresponding document images.

**Human benchmark** (1 paper: [TVQACML: Benchmarking Text-Centric Visual Question Answering in Multilingual Chinese Minority Languages](https://aclanthology.org/2025.emnlp-main.705.pdf))
> A native-speaker human evaluation using five annotators per language to provide reference performance for the benchmark.

## Relationships

### Associated with
- **OSWorld** (measurement instrument), 1 paper
  > The human performance study indicates that task examples from OSWORLD are more time-consuming and challenging compared to those in prior work. (Section 3.2)
  - [OSWorld: Benchmarking Multimodal Agents for Open-Ended Tasks in Real Computer Environments](https://proceedings.neurips.cc/paper_files/paper/2024/file/5d413e48f84dc61244b6be550f1cd8f5-Paper-Datasets_and_Benchmarks_Track.pdf)
- **Bongard Problems** (measurement instrument), 1 paper
  > “For evaluating human performances on BPs, 30 participants were recruited among Prolific users”
  - [Bongard in Wonderland: Visual Puzzles that Still Make AI Go Mad?](https://raw.githubusercontent.com/mlresearch/v267/main/assets/wust25a/wust25a.pdf)
