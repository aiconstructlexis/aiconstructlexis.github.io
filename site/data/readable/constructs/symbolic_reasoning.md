# Symbolic reasoning
**Type:** Construct  
**Supporting papers:** 36  
**Also known as:** Symbolic computing, Symbol processing  

## State of the Field

**Space of definitions.** Across the papers, the prevailing usage frames symbolic reasoning as a latent ability to manipulate abstract symbols, discrete patterns, or formal expressions according to explicit rules in order to reach correct outputs on rule-governed or logic-based problems. Some definitions make the reference standard explicit by grounding symbolic problems in natural formal systems, with examples including mathematics, first-order logic, planning languages, date calculations, navigation, and transformations such as deletion, reordering, swapping, or concatenating letters. Smaller lines of work recast the same area as symbolic computing, meaning rigorous exact operations via code generation, or as symbol processing, meaning operation on abstract variables that remain invariant to their specific values through mechanisms such as indirection. Taken together, the definitions vary mainly along two axes: latent ability versus reasoning approach or emergent mechanism, and broad rule-based problem solving versus narrower transformation tasks.

**Space of facets.** Papers usually place symbolic reasoning as one category within broader reasoning taxonomies, most often alongside arithmetic and commonsense reasoning, and sometimes alongside math, logical reasoning, language understanding, world knowledge, reading comprehension, and coding. Some authors say a problem is symbolic when it can be grounded in a natural formal system, while others carve out recurring subdomains such as date understanding, navigation, logical deduction, and rule application on remapped tokens independent of domain knowledge. Neighboring labels are not fully interchangeable: neuro-symbolic reasoning is described as combining learning abilities with symbolic systems for explicit knowledge representation and logical reasoning, symbolic computing via code generation emphasizes exact operations and tool use, and one paper contrasts symbolic reasoning with broader semantic understanding by describing SQL-based symbolic reasoning as strong on computations but poor on noisy or unstructured inputs.

**Space of measurement.** Papers operationalize the construct with six linked measurement instruments, all benchmark or dataset based, and with four linked behavioral indicators. The most frequently linked instruments are Coin Flip, Last letter concatenation, BIG-Bench Hard, and AQuA-RAT, with two other instruments; the most frequently linked behavioral indicator is Chain of thought, with three others. These operationalizations make the construct concrete through tasks such as determining a coin's final face after a sequence of flips, concatenating the last letters of words, and handling symbolic multiple-choice expressions not explicitly defined in the query. This measurement space largely matches the dominant definitions because it centers rule application, symbolic transformation, and multi-step logical deduction on structured inputs.

**Links.** Several papers claim a causal relationship from Chain of thought to symbolic reasoning, reporting that symbolic reasoning is among the categories that benefited the most or derive substantial benefit from CoT. One paper claims a causal relationship from symbolic reasoning to Abstract reasoning, arguing that emergent reasoning depends on symbolic mechanisms, and another claims a causal relationship from symbolic reasoning to Mathematical problem solving, where rising equation complexity makes symbolic reasoning a limiting factor. Separate papers relate Autoformalization to enhanced capabilities for symbolic reasoning and relate Code generation to symbolic reasoning through symbolic computing via code generation; no correlational links are reported.

## Sources

**Symbolic reasoning** (14 papers: [Escape Sky-high Cost: Early-stopping Self-Consistency for Multi-step Reasoning](https://proceedings.iclr.cc/paper_files/paper/2024/file/3fe2a777282299ecb4f9e7ebb531f0ab-Paper-Conference.pdf), [Large Language Model Cascades with Mixture of Thought Representations for Cost-Efficient Reasoning](https://proceedings.iclr.cc/paper_files/paper/2024/file/5de11e930c1bbfda5d4fc9d2b0924032-Paper-Conference.pdf), [Mastering Symbolic Operations: Augmenting Language Models with Compiled Neural Networks](https://proceedings.iclr.cc/paper_files/paper/2024/file/72679d76c80e079c70fe5977d21ed1e4-Paper-Conference.pdf), [Chain-of-Thought Reasoning Without Prompting](https://proceedings.neurips.cc/paper_files/paper/2024/file/7a8e7fd295aa04eac4b470ae27f8785c-Paper-Conference.pdf), [To CoT or not to CoT? Chain-of-thought helps mainly on math and symbolic reasoning](https://proceedings.iclr.cc/paper_files/paper/2025/file/ead542f13a38179d1b55b88610f959a1-Paper-Conference.pdf), [Large Language Models Are Cross-Lingual Knowledge-Free Reasoners](https://aclanthology.org/2025.naacl-long.72.pdf), [PORT: Preference Optimization on Reasoning Traces](https://aclanthology.org/2025.naacl-long.549.pdf), [Towards Rationality in Language and Multimodal Agents: A Survey](https://aclanthology.org/2025.naacl-long.186.pdf), [Self-Harmonized Chain of Thought](https://aclanthology.org/2025.naacl-long.53.pdf), [H-STAR: LLM-driven Hybrid SQL-Text Adaptive Reasoning on Tables](https://aclanthology.org/2025.naacl-long.445.pdf), [Can LLMs Help Uncover Insights about LLMs? A Large-Scale, Evolving Literature Analysis of Frontier LLMs](https://aclanthology.org/2025.acl-long.998.pdf), [Parameters vs FLOPs: Scaling Laws for Optimal Sparsity for Mixture-of-Experts Language Models](https://raw.githubusercontent.com/mlresearch/v267/main/assets/abnar25a/abnar25a.pdf), [Predicate-Guided Generation for Mathematical Reasoning](https://aclanthology.org/2025.emnlp-main.462.pdf), [Benchmarking Abstract and Reasoning Abilities Through A Theoretical Perspective](https://raw.githubusercontent.com/mlresearch/v267/main/assets/ma25u/ma25u.pdf))
> The latent ability to manipulate symbols or discrete patterns according to formal rules to reach a correct answer.

**Symbolic computing** (1 paper: [CodeSteer: Symbolic-Augmented Language Models via Code/Text Guidance](https://raw.githubusercontent.com/mlresearch/v267/main/assets/chen25x/chen25x.pdf))
> The model's ability to perform rigorous, exact operations through programmatic solutions, such as computation, symbolic manipulation, and algorithmic processing.

**Symbol processing** (1 paper: [Emergent Symbolic Mechanisms Support Abstract Reasoning in Large Language Models](https://raw.githubusercontent.com/mlresearch/v267/main/assets/yang25c/yang25c.pdf))
> An emergent cognitive capacity to operate on abstract variables (symbols) that are invariant to the specific values they are associated with, using mechanisms like indirection.

## Relationships

### Symbolic reasoning →
- **Coin Flip** (measurement instrument): *measured_by*, 6 papers
  > For symbolic reasoning, we use Last Letter Concatenation and Coin Flip from Wei et al. (2022).
  - [Escape Sky-high Cost: Early-stopping Self-Consistency for Multi-step Reasoning](https://proceedings.iclr.cc/paper_files/paper/2024/file/3fe2a777282299ecb4f9e7ebb531f0ab-Paper-Conference.pdf)
  - [Calibrating Reasoning in Language Models with Internal Consistency](https://proceedings.neurips.cc/paper_files/paper/2024/file/d037fd021c9aace128b8ce25001cdb6c-Paper-Conference.pdf)
  - [CodePlan: Unlocking Reasoning Potential in Large Language Models by Scaling Code-form Planning](https://proceedings.iclr.cc/paper_files/paper/2025/file/c362b360765ed90ae4bd9c6764837e0e-Paper-Conference.pdf)
  - [Self-Harmonized Chain of Thought](https://aclanthology.org/2025.naacl-long.53.pdf)
  - [Large Language Models Are Cross-Lingual Knowledge-Free Reasoners](https://aclanthology.org/2025.naacl-long.72.pdf)
  - [Rethinking Chain-of-Thought from the Perspective of Self-Training](https://raw.githubusercontent.com/mlresearch/v267/main/assets/wu25al/wu25al.pdf)
- **Last letter concatenation** (measurement instrument): *measured_by*, 5 papers
  > For symbolic reasoning, we use Last Letter Concatenation and Coin Flip from Wei et al. (2022).
  - [Escape Sky-high Cost: Early-stopping Self-Consistency for Multi-step Reasoning](https://proceedings.iclr.cc/paper_files/paper/2024/file/3fe2a777282299ecb4f9e7ebb531f0ab-Paper-Conference.pdf)
  - [CodePlan: Unlocking Reasoning Potential in Large Language Models by Scaling Code-form Planning](https://proceedings.iclr.cc/paper_files/paper/2025/file/c362b360765ed90ae4bd9c6764837e0e-Paper-Conference.pdf)
  - [Don't Take Things Out of Context: Attention Intervention for Enhancing Chain-of-Thought Reasoning in Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/9eaeccb40e16ba5ae4e25e9fdb2fea19-Paper-Conference.pdf)
  - [Forking Paths in Neural Text Generation](https://proceedings.iclr.cc/paper_files/paper/2025/file/2b6a8ca3d06ffa2e044bff8c723863ff-Paper-Conference.pdf)
  - [Rethinking Chain-of-Thought from the Perspective of Self-Training](https://raw.githubusercontent.com/mlresearch/v267/main/assets/wu25al/wu25al.pdf)
- **BIG-Bench Hard** (measurement instrument): *measured_by*, 3 papers
  > Additionally, we investigate symbolic reasoning tasks from Big-Bench-Hard (bench authors, 2023; Suzgun et al., 2022). (Section 3)
  - [Chain-of-Thought Reasoning Without Prompting](https://proceedings.neurips.cc/paper_files/paper/2024/file/7a8e7fd295aa04eac4b470ae27f8785c-Paper-Conference.pdf)
  - [CodePlan: Unlocking Reasoning Potential in Large Language Models by Scaling Code-form Planning](https://proceedings.iclr.cc/paper_files/paper/2025/file/c362b360765ed90ae4bd9c6764837e0e-Paper-Conference.pdf)
  - [Beyond Output Matching: Bidirectional Alignment for Enhanced In-Context Learning](https://aclanthology.org/2025.acl-long.1573.pdf)
- **Abstract reasoning** (construct): *causes*, 1 paper
  > These results point toward a resolution of the longstanding debate between symbolic and neural network approaches, suggesting that emergent reasoning in neural networks depends on the emergence of symbolic mechanisms. (Abstract)
  - [Emergent Symbolic Mechanisms Support Abstract Reasoning in Large Language Models](https://raw.githubusercontent.com/mlresearch/v267/main/assets/yang25c/yang25c.pdf)
- **Mathematical problem solving** (behavioral indicator): *causes*, 1 paper
  > Finally, as equation complexity increases, symbolic reasoning itself becomes a limiting factor.
  - [Can Vision-Language Models Solve Visual Math Equations?](https://aclanthology.org/2025.emnlp-main.547.pdf)
- **Date Understanding** (measurement instrument): *measured_by*, 1 paper
  > Symbolic Reasoning. We select four datasets from BigBench (Srivastava et al., 2022) for testing, including Date Understanding, Penguin, Colored Objects and Logical Deduction. (Section 4.1)
  - [Dynamic Collaboration of Multi-Language Models based on Minimal Complete Semantic Units](https://aclanthology.org/2025.emnlp-main.651.pdf)
- **BIG-Bench Logical Deduction** (measurement instrument): *measured_by*, 1 paper
  > Symbolic Reasoning. We select four datasets from BigBench (Srivastava et al., 2022) for testing, including Date Understanding, Penguin, Colored Objects and Logical Deduction. (Section 4.1)
  - [Dynamic Collaboration of Multi-Language Models based on Minimal Complete Semantic Units](https://aclanthology.org/2025.emnlp-main.651.pdf)
- **AQuA-RAT** (measurement instrument): *measured_by*, 1 paper
  > AQuA involves multiple-choice symbolic reasoning with expressions not explicitly defined in the query. (Section 4)
  - [FLARE: Faithful Logic-Aided Reasoning and Exploration](https://aclanthology.org/2025.emnlp-main.1193.pdf)

### → Symbolic reasoning
- **Chain of thought** (behavioral indicator): *causes*, 2 papers
  > The three categories which benefited the most from CoT are symbolic reasoning, math, and logical reasoning, with average improvements of 14.2, 12.3, 6.9, respectively. (Section 3)
  - [To CoT or not to CoT? Chain-of-thought helps mainly on math and symbolic reasoning](https://proceedings.iclr.cc/paper_files/paper/2025/file/ead542f13a38179d1b55b88610f959a1-Paper-Conference.pdf)
  - [Can LLMs Help Uncover Insights about LLMs? A Large-Scale, Evolving Literature Analysis of Frontier LLMs](https://aclanthology.org/2025.acl-long.998.pdf)

### Associated with
- **Autoformalization** (behavioral indicator), 1 paper
  > To address this, we propose using auto-formalization agents equipped with enhanced capabilities for symbolic reasoning.
  - [Position: Trustworthy AI Agents Require the Integration of Large Language Models and Formal Methods](https://raw.githubusercontent.com/mlresearch/v267/main/assets/zhang25ds/zhang25ds.pdf)
- **Code generation** (behavioral indicator), 1 paper
  > “symbolic computing via code generation is adept at handling rigorous operations”
  - [CodeSteer: Symbolic-Augmented Language Models via Code/Text Guidance](https://raw.githubusercontent.com/mlresearch/v267/main/assets/chen25x/chen25x.pdf)
