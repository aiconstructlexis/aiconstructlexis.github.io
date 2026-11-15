# MATH-500
**Type:** Measurement instrument  
**Supporting papers:** 88  
**Also known as:** MATH500  

## State of the Field

**What it is.** Most commonly, papers treat MATH-500, also written MATH500, as a 500-question subset or test set from the MATH benchmark, often described as selected from the original 5,000-question MATH test set. Some authors simply describe it as a mathematical reasoning benchmark containing 500 challenging math problems, while others specify that it is a representative, highly challenging 10% subset. Where papers give more detail on content, they describe high school competition math across seven subjects, with AoPS-based difficulty levels from 1 to 5.

**What it is claimed to measure.** Papers link it to three constructs and one behavioral indicator. The prevailing usage is to measure Mathematical reasoning, with closely related uses for broader Reasoning; papers also use it to measure Mathematical problem solving, and a smaller line of work reports it as measuring Verification ability. Overall, the reported measurement claims are concentrated on math-focused reasoning constructs rather than spread across many different targets.

**Space of uses.** Most papers use it within broader evaluation suites rather than alone, most often alongside GSM8K, and often with AIME or GPQA; some also pair it with MMLU. At the instrument level, papers link it only to MATH, explicitly describing it as the MATH500 subset or a subset of the MATH test set. Authors commonly position it as a standard benchmark for comparing methods, while some use it as a subset chosen "due to the computation cost" or as a check that a method "does not degrade reasoning ability."

## Sources

**MATH-500** (4 papers: [HARDMath: A Benchmark Dataset for Challenging Problems in Applied Mathematics](https://proceedings.iclr.cc/paper_files/paper/2025/file/23d64d26abb5a0e9f2014cfcc700f82a-Paper-Conference.pdf), [Revisiting the Test-Time Scaling of o1-like Models: Do they Truly Possess Test-Time Scaling Capabilities?](https://aclanthology.org/2025.acl-long.232.pdf), [Forest-of-Thought: Scaling Test-Time Compute for Enhancing LLM Reasoning](https://raw.githubusercontent.com/mlresearch/v267/main/assets/bi25a/bi25a.pdf), [TokenSkip: Controllable Chain-of-Thought Compression in LLMs](https://aclanthology.org/2025.emnlp-main.165.pdf))
> A subset of the MATH benchmark used for evaluating model performance.

**MATH500** (7 papers: [An Efficient and Precise Training Data Construction Framework for Process-supervised Reward Model in Mathematical Reasoning](https://aclanthology.org/2025.acl-long.216.pdf), [Do NOT Think That Much for 2+3=? On the Overthinking of Long Reasoning Models](https://raw.githubusercontent.com/mlresearch/v267/main/assets/chen25bx/chen25bx.pdf), [From Problem-Solving to Teaching Problem-Solving: Aligning LLMs with Pedagogy using Reinforcement Learning](https://aclanthology.org/2025.emnlp-main.15.pdf), [LLaMA-Berry: Pairwise Optimization for Olympiad-level Mathematical Reasoning via O1-like Monte Carlo Tree Search](https://aclanthology.org/2025.naacl-long.375.pdf), [DART-Math: Difficulty-Aware Rejection Tuning for Mathematical Problem-Solving](https://proceedings.neurips.cc/paper_files/paper/2024/file/0ef1afa0daa888d695dcd5e9513bafa3-Paper-Conference.pdf), [Easy-to-Hard Generalization: Scalable Alignment Beyond Human Supervision](https://proceedings.neurips.cc/paper_files/paper/2024/file/5b6346a05a537d4cdb2f50323452a9fe-Paper-Conference.pdf), [ReST-MCTS*: LLM Self-Training via Process Reward Guided Tree Search](https://proceedings.neurips.cc/paper_files/paper/2024/file/76ec4dc30e9faaf0e4b6093eaa377218-Paper-Conference.pdf))
> A test set of 500 representative questions selected from the original 5,000-question MATH test set, used for evaluating PRM supervision performance.

## Relationships

### → MATH-500
- **Mathematical reasoning** (construct): *measured_by*, 22 papers
  > We analyze the performance of fine-tuned models of various sizes given different inference FLOPs on mathematical reasoning benchmarks (e.g., GSM8K test set (Cobbe et al., 2021) and MATH500 test set (Hendrycks et al., 2021b; Lightman et al., 2024)).
  - [Inference Scaling Laws: An Empirical Analysis of Compute-Optimal Inference for LLM Problem-Solving](https://proceedings.iclr.cc/paper_files/paper/2025/file/8c3caae2f725c8e2a55ecd600563d172-Paper-Conference.pdf)
  - [Enhancing Mathematical Reasoning in LLMs by Stepwise Correction](https://aclanthology.org/2025.acl-long.1048.pdf)
  - [S2R: Teaching LLMs to Self-verify and Self-correct via Reinforcement Learning](https://aclanthology.org/2025.acl-long.1104.pdf)
  - [YuLan-Mini: Pushing the Limits of Open Data-efficient Language Model](https://aclanthology.org/2025.acl-long.268.pdf)
  - [Satori: Reinforcement Learning with Chain-of-Action-Thought Enhances LLM Reasoning via Autoregressive Search](https://raw.githubusercontent.com/mlresearch/v267/main/assets/shen25o/shen25o.pdf)
  - [AdaptiveStep: Automatically Dividing Reasoning Step through Model Confidence](https://raw.githubusercontent.com/mlresearch/v267/main/assets/liu25aq/liu25aq.pdf)
  - [Controlling Large Language Model with Latent Action](https://raw.githubusercontent.com/mlresearch/v267/main/assets/jia25e/jia25e.pdf)
  - [Test-Time Preference Optimization: On-the-Fly Alignment via Iterative Textual Feedback](https://raw.githubusercontent.com/mlresearch/v267/main/assets/li25ac/li25ac.pdf)
  - [Improving Rationality in the Reasoning Process of Language Models through Self-playing Game](https://raw.githubusercontent.com/mlresearch/v267/main/assets/wang25bb/wang25bb.pdf)
  - [Policy Guided Tree Search for Enhanced LLM Reasoning](https://raw.githubusercontent.com/mlresearch/v267/main/assets/li25bv/li25bv.pdf)
  - [rStar-Math: Small LLMs Can Master Math Reasoning with Self-Evolved Deep Thinking](https://raw.githubusercontent.com/mlresearch/v267/main/assets/guan25f/guan25f.pdf)
  - [FANS: Formal Answer Selection for LLM Natural Language Math Reasoning Using Lean4](https://aclanthology.org/2025.emnlp-main.158.pdf)
  - [Large Language Models Have Intrinsic Meta-Cognition, but Need a Good Lens](https://aclanthology.org/2025.emnlp-main.171.pdf)
  - [An Empirical Study of LLM Reasoning Ability Under Strict Output Length Constraint](https://aclanthology.org/2025.emnlp-main.389.pdf)
  - [Feature Extraction and Steering for Enhanced Chain-of-Thought Reasoning in Language Models](https://aclanthology.org/2025.emnlp-main.552.pdf)
  - [START: Self-taught Reasoner with Tools](https://aclanthology.org/2025.emnlp-main.683.pdf)
  - [Let's Reason Formally: Natural-Formal Hybrid Reasoning Enhances LLM's Math Capability](https://aclanthology.org/2025.emnlp-main.850.pdf)
  - [ThinkEdit: Interpretable Weight Editing to Mitigate Overly Short Thinking in Reasoning Models](https://aclanthology.org/2025.emnlp-main.861.pdf)
  - [CoMAT: Chain of Mathematically Annotated Thought Improves Mathematical Reasoning](https://aclanthology.org/2025.emnlp-main.1024.pdf)
  - [The Emperor's New Reasoning: Format Imitation Overshadows Genuine Mathematical Understanding in SFT](https://aclanthology.org/2025.emnlp-main.1067.pdf)
  - [Learning Like Humans: Advancing LLM Reasoning Capabilities via Adaptive Difficulty Curriculum Learning and Expert-Guided Self-Reformulation](https://aclanthology.org/2025.emnlp-main.336.pdf)
  - [Agentic-R1: Distilled Dual-Strategy Reasoning](https://aclanthology.org/2025.emnlp-main.604.pdf)
- **Reasoning** (construct): *measured_by*, 9 papers
  > We evaluate across 6 reasoning benchmarks used in the original papers of the above prompting strategies, including GSM8K (Cobbe et al., 2021), GSM-Hard (Gao et al., 2023), MATH-500 (Hendrycks et al., 2021b; Lightman et al., 2024), MMLU-high-school-biology, chemistry and physics (Hendrycks et al., 2021a). (Section 2.3)
  - [Rethinking the Role of Prompting Strategies in LLM Test-Time Scaling: A Perspective of Probability Theory](https://aclanthology.org/2025.acl-long.1356.pdf)
  - [Demystifying Long Chain-of-Thought Reasoning](https://raw.githubusercontent.com/mlresearch/v267/main/assets/yang25ae/yang25ae.pdf)
  - [Reward-Guided Speculative Decoding for Efficient LLM Reasoning](https://raw.githubusercontent.com/mlresearch/v267/main/assets/liao25f/liao25f.pdf)
  - [Enhancing Reasoning Abilities of Small LLMs with Cognitive Alignment](https://aclanthology.org/2025.emnlp-main.377.pdf)
  - [An Empirical Study of LLM Reasoning Ability Under Strict Output Length Constraint](https://aclanthology.org/2025.emnlp-main.389.pdf)
  - [Step-level Verifier-guided Hybrid Test-Time Scaling for Large Language Models](https://aclanthology.org/2025.emnlp-main.931.pdf)
  - [Reasoning Model Unlearning: Forgetting Traces, Not Just Answers, While Preserving Reasoning Skills](https://aclanthology.org/2025.emnlp-main.220.pdf)
  - [The Impact of Language Mixing on Bilingual LLM Reasoning](https://aclanthology.org/2025.emnlp-main.1654.pdf)
  - [Long Chain-of-Thought Fine-tuning via Understanding-to-Reasoning Transition](https://aclanthology.org/2025.emnlp-main.1751.pdf)
- **Mathematical problem solving** (behavioral indicator): *measured_by*, 8 papers
  > This evaluation includes benchmarks in: ... 3) Specific math domain tasks like MATH500 (Lightman et al., 2023). (Section 4.3)
  - [OpenPRM: Building Open-domain Process-based Reward Models with Preference Trees](https://proceedings.iclr.cc/paper_files/paper/2025/file/c919a2b5ec1de69f2629f9119676e336-Paper-Conference.pdf)
  - [Inference Scaling Laws: An Empirical Analysis of Compute-Optimal Inference for LLM Problem-Solving](https://proceedings.iclr.cc/paper_files/paper/2025/file/8c3caae2f725c8e2a55ecd600563d172-Paper-Conference.pdf)
  - [Reinforce LLM Reasoning through Multi-Agent Reflection](https://raw.githubusercontent.com/mlresearch/v267/main/assets/yuan25l/yuan25l.pdf)
  - [Do NOT Think That Much for 2+3=? On the Overthinking of Long Reasoning Models](https://raw.githubusercontent.com/mlresearch/v267/main/assets/chen25bx/chen25bx.pdf)
  - [AdaptThink: Reasoning Models Can Learn When to Think](https://aclanthology.org/2025.emnlp-main.184.pdf)
  - [ConCISE: Confidence-guided Compression in Step-by-step Efficient Reasoning](https://aclanthology.org/2025.emnlp-main.405.pdf)
  - [Search-o1: Agentic Search-Enhanced Large Reasoning Models](https://aclanthology.org/2025.emnlp-main.276.pdf)
  - [R-PRM: Reasoning-Driven Process Reward Modeling](https://aclanthology.org/2025.emnlp-main.679.pdf)
- **Verification ability** (construct): *measured_by*, 1 paper
  > “For example, when verifying solutions sampled from the Llama-3-70B-Instruct model, PQM improves the accuracy from 39.8% to 51.4%, a direct 11.6% improvement on the challenging MATH500 benchmark”
  - [Process Reward Model with Q-value Rankings](https://proceedings.iclr.cc/paper_files/paper/2025/file/26494b66ae1114d314673e25b4967288-Paper-Conference.pdf)

### Associated with
- **MATH** (measurement instrument), 1 paper
  > For evaluation, we use the MATH500 subset of the test set (Lightman et al., 2023). (Section 2.2)
  - [Warm Up Before You Train: Unlocking General Reasoning in Resource-Constrained Settings](https://aclanthology.org/2025.emnlp-main.727.pdf)
