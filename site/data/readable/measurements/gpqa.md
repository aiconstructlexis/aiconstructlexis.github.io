# GPQA
**Type:** Measurement instrument  
**Supporting papers:** 92  

## State of the Field

**What it is.** Across papers, GPQA is most commonly described as a graduate-level, "Google-proof" question-answering benchmark or multiple-choice QA dataset built from expert-written scientific questions. The prevailing description places its content in biology, physics, and chemistry, often as 448 questions written by domain experts or PhD-level experts to test deep reasoning and domain expertise; a smaller set of descriptions broadens this to "various scientific subjects" or "various disciplines."

**What it is claimed to measure.** Papers link GPQA to 9 constructs and 4 behavioral indicators. The dominant claim is that it measures Reasoning, with additional recurring uses for General ability, Generalization, Chain-of-thought reasoning, and Natural language understanding; taken together, papers use it for a range of targets rather than only one. Behavioral-indicator links are present as well, but are fewer and spread across 4 indicators.

**Space of uses.** Papers do not explicitly relate GPQA to another named measurement instrument. In practice, they usually place it inside larger benchmark suites, often alongside MMLU, BBH, GSM8K, ARC-C, and MT-Bench, depending on whether the evaluation is framed as reasoning, general capabilities, or out-of-domain testing. It is often run in zero-shot or few-shot settings, and one paper reports converting it to binary choices; another uses it as a controlled contamination test set.

**Concerns raised.** A contamination-related concern appears in one paper, which treats GPQA as an uncontaminated dataset in a controlled contamination experiment because it was released in 2023, beyond the target models' knowledge cutoff.

## Sources

**GPQA** (17 papers: [CURIE: Evaluating LLMs on Multitask Scientific Long-Context Understanding and Reasoning](https://proceedings.iclr.cc/paper_files/paper/2025/file/1ae4999aefb509d75d8608e07280922c-Paper-Conference.pdf), [Advancing MoE Efficiency: A Collaboration-Constrained Routing (C2R) Strategy for Better Expert Parallelism Design](https://aclanthology.org/2025.naacl-long.347.pdf), [S2-MAD: Breaking the Token Barrier to Enhance Multi-Agent Debate Efficiency](https://aclanthology.org/2025.naacl-long.475.pdf), [Information-Guided Identification of Training Data Imprint in (Proprietary) Large Language Models](https://aclanthology.org/2025.naacl-long.99.pdf), [Auto-Arena: Automating LLM Evaluations with Agent Peer Battles and Committee Discussions](https://aclanthology.org/2025.acl-long.223.pdf), [MAPLE: Many-Shot Adaptive Pseudo-Labeling for In-Context Learning](https://raw.githubusercontent.com/mlresearch/v267/main/assets/chen25bo/chen25bo.pdf), [Efficient Model Development through Fine-tuning Transfer](https://aclanthology.org/2025.emnlp-main.131.pdf), [Cal-DPO: Calibrated Direct Preference Optimization for Language Model Alignment](https://proceedings.neurips.cc/paper_files/paper/2024/file/cf8b2205e39f81726a8d828ecbe00ad0-Paper-Conference.pdf), [Enhancing Reasoning Capabilities of LLMs via Principled Synthetic Logic Corpus](https://proceedings.neurips.cc/paper_files/paper/2024/file/8678da90126aa58326b2fc0254b33a8c-Paper-Conference.pdf), [MAmmoTH2: Scaling Instructions from the Web](https://proceedings.neurips.cc/paper_files/paper/2024/file/a4ca07aa108036f80cbb5b82285fd4b1-Paper-Conference.pdf), [Many-Shot In-Context Learning](https://proceedings.neurips.cc/paper_files/paper/2024/file/8cb564df771e9eacbfe9d72bd46a24a9-Paper-Conference.pdf), [NYU CTF Bench: A Scalable Open-Source Benchmark Dataset for Evaluating LLMs in Offensive Security](https://proceedings.neurips.cc/paper_files/paper/2024/file/69d97a6493fbf016fff0a751f253ad18-Paper-Datasets_and_Benchmarks_Track.pdf), [On scalable oversight with weak LLMs judging strong LLMs](https://proceedings.neurips.cc/paper_files/paper/2024/file/899511e37a8e01e1bd6f6f1d377cc250-Paper-Conference.pdf), [Safetywashing: Do AI Safety Benchmarks Actually Measure Safety Progress?](https://proceedings.neurips.cc/paper_files/paper/2024/file/7ebcdd0de471c027e67a11959c666d74-Paper-Datasets_and_Benchmarks_Track.pdf), [SciInstruct: a Self-Reflective Instruction Annotated Dataset for Training Scientific Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/02ee6b7295f720407b56c457b34c54d5-Paper-Datasets_and_Benchmarks_Track.pdf), [Synthesize, Partition, then Adapt: Eliciting Diverse Samples from Foundation Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/6e2861dabad3fe21a71914ccfbfff976-Paper-Conference.pdf), [UltraMedical: Building Specialized Generalists in Biomedicine](https://proceedings.neurips.cc/paper_files/paper/2024/file/2dfc26ce9039f00eee4aba0c54931e46-Paper-Datasets_and_Benchmarks_Track.pdf))
> A benchmark of graduate-level questions in biology, physics, and chemistry, used for comparison to evaluate scientific domain expertise.

## Relationships

### → GPQA
- **Reasoning** (construct): *measured_by*, 7 papers
  > To rigorously assess the capabilities of models in reasoning abilities across different domains, we utilize several widely used datasets, GSM8K [Cobbe et al., 2021], MATH [Hendrycks et al., 2021b], TheoremQA [Chen et al., 2023b], BIG-Bench Hard (BBH) [Suzgun et al., 2022], ARC-C [Clark et al., 2018], GPQA [Rein et al., 2023], MMLU-STEM [Hendrycks et al., 2021a]. (Section 3.2)
  - [MAmmoTH2: Scaling Instructions from the Web](https://proceedings.neurips.cc/paper_files/paper/2024/file/a4ca07aa108036f80cbb5b82285fd4b1-Paper-Conference.pdf)
  - [Rethinking the Role of Prompting Strategies in LLM Test-Time Scaling: A Perspective of Probability Theory](https://aclanthology.org/2025.acl-long.1356.pdf)
  - [Reward-Guided Speculative Decoding for Efficient LLM Reasoning](https://raw.githubusercontent.com/mlresearch/v267/main/assets/liao25f/liao25f.pdf)
  - [Speculative Prefill: Turbocharging TTFT with Lightweight and Training-Free Token Importance Estimation](https://raw.githubusercontent.com/mlresearch/v267/main/assets/liu25g/liu25g.pdf)
  - [Efficient Model Development through Fine-tuning Transfer](https://aclanthology.org/2025.emnlp-main.131.pdf)
  - [ORPP: Self-Optimizing Role-playing Prompts to Enhance Language Model Capabilities](https://aclanthology.org/2025.emnlp-main.1453.pdf)
  - [Long Chain-of-Thought Fine-tuning via Understanding-to-Reasoning Transition](https://aclanthology.org/2025.emnlp-main.1751.pdf)
- **Generalization** (construct): *measured_by*, 3 papers
  > Additionally, we evaluate the model’s generalization performance across six out-of-domain tasks, including MT-Bench (Zheng et al., 2024), ARC-Challenge (25-shot) (Clark et al., 2018), GSM8K (8-shot) (Cobbe et al., 2021), HellaSwag (8-shot) (Zellers et al., 2019), GPQA (0-shot) (Rein et al., 2023), and MMLU (0-shot) (Hendrycks et al., 2020).
  - [Montessori-Instruct: Generate Influential Training Data Tailored for Student Learning](https://proceedings.iclr.cc/paper_files/paper/2025/file/ba1d33849b963efc6b5d3082ad68f480-Paper-Conference.pdf)
  - [MAS-GPT: Training LLMs to Build LLM-based Multi-Agent Systems](https://raw.githubusercontent.com/mlresearch/v267/main/assets/ye25g/ye25g.pdf)
  - [T1: Advancing Language Model Reasoning through Reinforcement Learning and Inference Scaling](https://raw.githubusercontent.com/mlresearch/v267/main/assets/hou25e/hou25e.pdf)
- **General ability** (construct): *measured_by*, 3 papers
  > We evaluated the general capabilities of the models on benchmarks related to general-domain chat (MT-Bench [83] and Alpaca-Eval [37]), general MCQs (MMLU [34] and GPQA [54]), and mathematical tasks (MATH [22] and GSM8k [12]). (Section 4.1)
  - [UltraMedical: Building Specialized Generalists in Biomedicine](https://proceedings.neurips.cc/paper_files/paper/2024/file/2dfc26ce9039f00eee4aba0c54931e46-Paper-Datasets_and_Benchmarks_Track.pdf)
  - [The Tug of War Within: Mitigating the Fairness-Privacy Conflicts in Large Language Models](https://aclanthology.org/2025.acl-long.590.pdf)
  - [MUSE: MCTS-Driven Red Teaming Framework for Enhanced Multi-Turn Dialogue Safety in Large Language Models](https://aclanthology.org/2025.emnlp-main.1080.pdf)
- **Question answering** (behavioral indicator): *measured_by*, 2 papers
  > question-answering [GPQA, 51] (Introduction).
  - [Many-Shot In-Context Learning](https://proceedings.neurips.cc/paper_files/paper/2024/file/8cb564df771e9eacbfe9d72bd46a24a9-Paper-Conference.pdf)
  - [Diffusion-based Neural Network Weights Generation](https://proceedings.iclr.cc/paper_files/paper/2025/file/f74d79573d71078848973009d0e99bdb-Paper-Conference.pdf)
- **Multiple-choice question answering** (behavioral indicator): *measured_by*, 2 papers
  > To assess the impact of DRAG on retrieval-augmented multiple-choice question answering (MCQA), we conduct extensive experiments across four benchmark datasets: ARC-C, MedMCQA, GPQA, and MMLU
  - [DRAG: Distilling RAG for SLMs from LLMs to Transfer Knowledge and Mitigate Hallucination via Evidence and Graph-based Distillation](https://aclanthology.org/2025.acl-long.358.pdf)
  - [MAPLE: Many-Shot Adaptive Pseudo-Labeling for In-Context Learning](https://raw.githubusercontent.com/mlresearch/v267/main/assets/chen25bo/chen25bo.pdf)
- **Natural language understanding** (construct): *measured_by*, 2 papers
  > To demonstrate the effectiveness of SPA in the natural language understanding domain, we evaluate its performance on several diverse tasks, including Big-Bench Hard (BBH) (Suzgun et al., 2022), GPQA (Rein et al., 2023), MMLU (Hendrycks et al., 2020), and WinoGrande (Sakaguchi et al., 2019).
  - [Synthesize, Partition, then Adapt: Eliciting Diverse Samples from Foundation Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/6e2861dabad3fe21a71914ccfbfff976-Paper-Conference.pdf)
  - [Samba: Simple Hybrid State Space Models for Efficient Unlimited Context Language Modeling](https://proceedings.iclr.cc/paper_files/paper/2025/file/84a7fc24ed52e8eff514c33e8ac76ea3-Paper-Conference.pdf)
- **Chain-of-thought reasoning** (construct): *measured_by*, 2 papers
  > For instance, models frequently demonstrate high performance on standardized test-style questions yet struggle when faced with complex planning or multi-step reasoning challenges, a limitation highlighted by specialized benchmarks like PlanBench (Valmeekam et al., 2022), GPQA (Rein et al., 2023), and HLE (Phan et al., 2025). (Section 2.4)
  - [In Benchmarks We Trust ... Or Not?](https://aclanthology.org/2025.emnlp-main.1208.pdf)
  - [Stepwise Informativeness Search for Improving LLM Reasoning](https://aclanthology.org/2025.emnlp-main.1285.pdf)
- **Tool use** (behavioral indicator): *measured_by*, 1 paper
  > GPQA (Rein et al., 2023) evaluates agents’ ability for coordinated tool use when solving challenging graduate-level problems. (§4.4)
  - [OpenHands: An Open Platform for AI Software Developers as Generalist Agents](https://proceedings.iclr.cc/paper_files/paper/2025/file/a4b6ad6b48850c0c331d1259fc66a69c-Paper-Conference.pdf)
- **Contextual understanding** (construct): *measured_by*, 1 paper
  > For evaluation, we selected eight general-purpose benchmarks to assess context awareness, including MMLU (5-shot) (Hendrycks et al., 2020), MMLU-PRO (5-shot) (Wang et al., 2024), GPQA (0-shot) (Rein et al., 2023), BBH (3-shot) (Srivastava et al., 2023), WinoGrande (5-shot) (Sakaguchi et al., 2019), GSM8k (8-shot) (Cobbe et al., 2021), MATH (4-shot) (Lightman et al., 2023), and DROP (3-shot) (Dua et al., 2019). (Section 6)
  - [HoPE: A Novel Positional Encoding Without Long-Term Decay for Enhanced Context Awareness and Extrapolation](https://aclanthology.org/2025.acl-long.1123.pdf)
- **Iterative refinement** (behavioral indicator): *measured_by*, 1 paper
  > In solution optimization, we assess performance on the Google-proof Question Answering (GPQA) benchmark (Rein et al., 2023)... (Section 4)
  - [Revolve: Optimizing AI Systems by Tracking Response Evolution in Textual Optimization](https://raw.githubusercontent.com/mlresearch/v267/main/assets/zhang25aj/zhang25aj.pdf)
- **Logical reasoning** (construct): *measured_by*, 1 paper
  > For logical reasoning, we evaluate the PrOntoQA (Saparov & He, 2022) dataset for logical deduction in a 5-shot setting and the GPQA (Rein et al., 2023) dataset for graduate-level multiple-choice questions in a 0-shot setting (Section 4).
  - [Policy Guided Tree Search for Enhanced LLM Reasoning](https://raw.githubusercontent.com/mlresearch/v267/main/assets/li25bv/li25bv.pdf)
- **Task generalization** (construct): *measured_by*, 1 paper
  > "To explore the efficacy of our general purpose ARCHON architectures, we evaluate them on three previously unseen tasks: GPQA (Rein et al., 2024), MMLU (Hendrycks et al., 2021), and MMLU Pro (Wang et al., 2024b)."
  - [An Architecture Search Framework for Inference-Time Techniques](https://raw.githubusercontent.com/mlresearch/v267/main/assets/saad-falcon25a/saad-falcon25a.pdf)
- **Commonsense reasoning** (construct): *measured_by*, 1 paper
  > we assess model capabilities in... commonsense reasoning on Hellaswag (Zellers et al., 2019) and GPQA (Rein et al., 2024). (Section 4.1)
  - [Middo: Model-Informed Dynamic Data Optimization for Enhanced LLM Fine-Tuning via Closed-Loop Learning](https://aclanthology.org/2025.emnlp-main.350.pdf)
