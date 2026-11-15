# Textual reasoning
**Type:** Behavioral indicator  
**Supporting papers:** 3  
**Also known as:** Verbal reasoning, Natural language reasoning  

## State of the Field

**Space of definitions.** Across definitions, the dominant framing is solving or answering reasoning problems in natural language. Papers describe it as drawing inferences or making judgments from text-based premises, answering directly in natural language rather than executable code, and handling verbal reasoning problems without relying primarily on mathematical calculation.

**Variants.** Other names include verbal reasoning and natural language reasoning. Papers study it as direct natural-language answering instead of code execution, and also in multimodal settings. They relate it to natural language inference and other language-task families, while a separate paper claims a causal relationship from textual reasoning to code debugging.

**Space of elicitation and scores.** Only one measurement instrument is linked to it: AlpacaEval. A paper uses AlpacaEval to assess pure text reasoning ability, and no other instrument is linked to it in the papers.

**What it is taken as evidence of.** Rather than treating it as evidence of one construct, papers relate this behavior to five constructs: visual understanding, chain-of-thought reasoning, mathematical reasoning, natural language understanding, and planning. The reported connections are mixed in wording, with one paper saying it excels in natural language understanding, another saying it struggles with quantitative reasoning, and another discussing difficulty handling visual understanding with textual reasoning simultaneously.

## Sources

**Verbal reasoning** (1 paper: [Conformal Language Model Reasoning with Coherent Factuality](https://proceedings.iclr.cc/paper_files/paper/2025/file/679fcceef65c3d855aa885bd024542c1-Paper-Conference.pdf))
> The observable task of solving reasoning problems expressed in natural language without relying primarily on mathematical calculation.

**Natural language reasoning** (1 paper: [Montessori-Instruct: Generate Influential Training Data Tailored for Student Learning](https://proceedings.iclr.cc/paper_files/paper/2025/file/ba1d33849b963efc6b5d3082ad68f480-Paper-Conference.pdf))
> Drawing inferences or making judgments from text-based premises in benchmark tasks.

**Textual reasoning** (1 paper: [Steering Large Language Models between Code Execution and Textual Reasoning](https://proceedings.iclr.cc/paper_files/paper/2025/file/f763f7c9a6599e14b07add5937d8189c-Paper-Conference.pdf))
> Answering a problem directly in natural language without relying on executable code.

## Relationships

### Textual reasoning →
- **AlpacaEval** (measurement instrument): *measured_by*, 1 paper
  > To assess the model’s pure text reasoning ability, we use AlpacaEval (Li et al., 2023a). (Section 4.2)
  - [UnifiedVisual: A Framework for Constructing Unified Vision-Language Datasets](https://aclanthology.org/2025.emnlp-main.1572.pdf)
- **Code debugging** (behavioral indicator): *causes*, 1 paper
  > Our findings highlight the potential of natural language reasoning to advance automated code debugging and address complex programming challenges. (Abstract)
  - [NL-Debugging: Exploiting Natural Language as an Intermediate Representation for Code Debugging](https://aclanthology.org/2025.emnlp-main.80.pdf)

### Associated with
- **Visual understanding** (construct), 2 papers
  > This indicates that VLMs are capable of textual reasoning. This finding suggests that the reasoning challenge does not mainly lie in the VLM’s textual components but in the visual ones. (Page 8)
  - [NL-Eye: Abductive NLI For Images](https://proceedings.iclr.cc/paper_files/paper/2025/file/d5aed68fde8e934d0ae4aadb57acc6c0-Paper-Conference.pdf)
  - [ProReason: Multi-Modal Proactive Reasoning with Decoupled Eyesight and Wisdom](https://aclanthology.org/2025.emnlp-main.1614.pdf)
- **Chain-of-thought reasoning** (construct), 1 paper
  > Natural Language Reasoning: we prompt LLMs to perform multi-step reasoning via natural language, and select the following publicly avaibable datasets: GSM8k [34] contains grade school math problems to test the basic arithmetic and reasoning ability. (Appendix C)
  - [JiuZhang3.0: Efficiently Improving Mathematical Reasoning by Training Small Data Synthesis Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/0356216f73660e15670510f5e42b5fa6-Paper-Conference.pdf)
- **Natural language inference** (behavioral indicator), 1 paper
  > Natural language reasoning suite consists of 11 benchmarks that involve natural language based reasoning such as Question Answering, natural language inference (NLI), sentence completion, co-reference resolution, and general intelligence.
  - [To Code or Not To Code? Exploring Impact of Code in Pre-training](https://proceedings.iclr.cc/paper_files/paper/2025/file/c513d1786f85531fac7050947736265f-Paper-Conference.pdf)
- **Sentence completion** (behavioral indicator), 1 paper
  > Natural language reasoning suite consists of 11 benchmarks that involve natural language based reasoning such as Question Answering, natural language inference (NLI), sentence completion, co-reference resolution, and general intelligence.
  - [To Code or Not To Code? Exploring Impact of Code in Pre-training](https://proceedings.iclr.cc/paper_files/paper/2025/file/c513d1786f85531fac7050947736265f-Paper-Conference.pdf)
- **Coreference resolution** (behavioral indicator), 1 paper
  > Natural language reasoning suite consists of 11 benchmarks that involve natural language based reasoning such as Question Answering, natural language inference (NLI), sentence completion, co-reference resolution, and general intelligence.
  - [To Code or Not To Code? Exploring Impact of Code in Pre-training](https://proceedings.iclr.cc/paper_files/paper/2025/file/c513d1786f85531fac7050947736265f-Paper-Conference.pdf)
- **Planning** (construct), 1 paper
  > Text is suitable for semantic analysis and commonsense reasoning, but is not the best format for precise computation and planning, symbolic manipulation, and algorithmic processing and optimization (Kambhampati et al., 2024b; Chen et al., 2024a). (Section 1)
  - [Steering Large Language Models between Code Execution and Textual Reasoning](https://proceedings.iclr.cc/paper_files/paper/2025/file/f763f7c9a6599e14b07add5937d8189c-Paper-Conference.pdf)
- **Mathematical reasoning** (construct), 1 paper
  > Textual reasoning ... struggles with quantitative reasoning.
  - [H-STAR: LLM-driven Hybrid SQL-Text Adaptive Reasoning on Tables](https://aclanthology.org/2025.naacl-long.445.pdf)
- **Test output prediction** (behavioral indicator), 1 paper
  > Finally, we introduce a new task that is designed to study natural language reasoning and test generation.
  - [LiveCodeBench: Holistic and Contamination Free Evaluation of Large Language Models for Code](https://proceedings.iclr.cc/paper_files/paper/2025/file/94074dd5a072d28ff75a76dabed43767-Paper-Conference.pdf)
- **Natural language understanding** (construct), 1 paper
  > Textual reasoning excels in natural language understanding
  - [H-STAR: LLM-driven Hybrid SQL-Text Adaptive Reasoning on Tables](https://aclanthology.org/2025.naacl-long.445.pdf)
