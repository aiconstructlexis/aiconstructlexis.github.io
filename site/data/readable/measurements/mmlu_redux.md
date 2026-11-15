# MMLU-Redux
**Type:** Measurement instrument  
**Supporting papers:** 10  
**Also known as:** MMLU-redux  

## State of the Field

**What it is.** Most papers describe MMLU-Redux as a zero-shot or revised variant of MMLU used as an evaluation benchmark for general knowledge, language understanding, and reasoning. Several descriptions present it as multiple-choice or closed-form question answering across a wide range of subjects, with one definition placing those subjects from elementary to professional level. Papers differ on its scope: some describe a manually re-annotated subset of 3,000 questions across 30 subjects, while others describe 5,700 manually re-annotated questions across all 57 subjects, with corrections to ground truth answers and question clarity.

**What it is claimed to measure.** Papers use MMLU-Redux to measure 3 constructs and 1 behavioral indicator. The prevailing link is to Reasoning: papers call it a logical reasoning or reasoning benchmark and use it to verify reasoning abilities or performance after editing. Smaller lines of work use it to measure Mathematical reasoning and Robustness, and one paper reports that it can also measure Error detection. The reported uses therefore span several targets rather than centering on only one, though Reasoning is the most common framing.

**Space of uses.** Papers typically position MMLU-Redux as an evaluation benchmark within broader suites of logical reasoning or multiple-choice test sets. Usage descriptions show zero-shot prompting and zero-shot chain-of-thought prompting, including one case using the ZeroEval prompting framework to elicit chain-of-thought reasoning; another paper lists it alongside ARC-Challenge and CommonsenseQA. Papers do not directly link it to another measurement instrument in the recorded relations, and they use it for checks such as reasoning performance, robustness under choice-order swapping, and model behavior before and after editing.

**Concerns raised.** Some authors describe MMLU-Redux as manually re-annotated to correct errors in ground truth answers and question clarity, which is the main benchmark-level issue stated in the papers.

## Sources

**MMLU-redux** (1 paper: [As Simple as Fine-tuning: LLM Alignment via Bidirectional Negative Feedback Loss](https://proceedings.iclr.cc/paper_files/paper/2025/file/4bc4e9ecd5ae4a75048dc216a770cba1-Paper-Conference.pdf))
> A benchmark used to evaluate a model's language understanding and knowledge across a wide range of subjects.

**MMLU-Redux** (5 papers: [Magpie: Alignment Data Synthesis from Scratch by Prompting Aligned LLMs with Nothing](https://proceedings.iclr.cc/paper_files/paper/2025/file/be06e3802e9411381feece79b4d960c1-Paper-Conference.pdf), [The Good, The Bad, and The Greedy: Evaluation of LLMs Should Not Ignore Non-Determinism](https://aclanthology.org/2025.naacl-long.211.pdf), [Are We Done with MMLU?](https://aclanthology.org/2025.naacl-long.262.pdf), [Mitigating Selection Bias with Node Pruning and Auxiliary Options](https://aclanthology.org/2025.acl-long.259.pdf), [Advancing Oversight Reasoning across Languages for Audit Sycophantic Behaviour via X-Agent](https://aclanthology.org/2025.emnlp-main.654.pdf))
> MMLU-Redux, a zero-shot variant of MMLU used as an evaluation benchmark for general knowledge and reasoning.

## Relationships

### → MMLU-Redux
- **Reasoning** (construct): *measured_by*, 2 papers
  > Furthermore, we also evaluate all the models on four logical reasoning benchmarks to verify the impact of these alignment methods on model’s reasoning abilities, including: MMLU-redux (Gema et al., 2024) (Language)...
  - [As Simple as Fine-tuning: LLM Alignment via Bidirectional Negative Feedback Loss](https://proceedings.iclr.cc/paper_files/paper/2025/file/4bc4e9ecd5ae4a75048dc216a770cba1-Paper-Conference.pdf)
  - [Representation Shattering in Transformers: A Synthetic Study with Knowledge Editing](https://raw.githubusercontent.com/mlresearch/v267/main/assets/nishi25a/nishi25a.pdf)
- **Error detection** (behavioral indicator): *measured_by*, 1 paper
  > "MMLU-Redux can also be used as a strong benchmark for automatic error detection in NLP datasets"
  - [Are We Done with MMLU?](https://aclanthology.org/2025.naacl-long.262.pdf)
- **Robustness** (construct): *measured_by*, 1 paper
  > To assess the robustness of QuaSAR as an ICL strategy, we evaluated two different phenomena: (i) the order swapping of choices in MMLU-Redux... (Section 4.4)
  - [Improving Chain-of-Thought Reasoning via Quasi-Symbolic Abstractions](https://aclanthology.org/2025.acl-long.843.pdf)
- **Mathematical reasoning** (construct): *measured_by*, 1 paper
  > We select a total of seven datasets, including... MMLU-Redux (Gema et al. 2024); focusing on various mathematics subjects... (Section 3)
  - [CoMAT: Chain of Mathematically Annotated Thought Improves Mathematical Reasoning](https://aclanthology.org/2025.emnlp-main.1024.pdf)
