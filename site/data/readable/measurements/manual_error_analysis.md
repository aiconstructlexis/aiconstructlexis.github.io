# Manual error analysis
**Type:** Measurement instrument  
**Supporting papers:** 5  
**Also known as:** Manual error annotation  

## State of the Field

**What it is.** Across papers, the prevailing usage is a human evaluation protocol in which annotators manually inspect model outputs or rationales against predefined error categories. Definitions range from native English speakers assessing rationale mistakes such as context, word-sense, and pun pair errors, to manual error annotation that counts errors in generated instructions across categories such as incorrect assembly operations or order. Other descriptions emphasize fine-grained taxonomies of linguistic and non-linguistic errors, or manual analysis of incorrect generations.

**What it is claimed to measure.** Papers use it to measure one construct, linguistic quality, and two behavioral indicators, calculation error and reasoning error. One paper uses manual annotation to investigate inconsistencies and linguistic quality, while another reports that in-depth human analysis identified common error types including calculation error and reasoning error. The reported measurement claims therefore center on this small set: linguistic quality, calculation error, and reasoning error.

**Space of uses.** Papers position it "beyond standard metrics" or as "in-depth" manual analysis of incorrect generations. One use describes "a set of questions to determine the presence of each category of mistake," while another counts errors in generated text across predefined categories. No other measurement instrument is linked to it.

## Sources

**Manual error analysis** (3 papers: [Pun Unintended: LLMs and the Illusion of Humor Understanding](https://aclanthology.org/2025.emnlp-main.1419.pdf), [Differentially Private Learning Needs Better Model Initialization and Self-Distillation](https://aclanthology.org/2025.naacl-long.455.pdf), [I Don't Know: Explicit Modeling of Uncertainty with an [IDK] Token](https://proceedings.neurips.cc/paper_files/paper/2024/file/14c018d2e72c521605b0567029ef0efb-Paper-Conference.pdf))
> Human evaluation protocol in which native English speakers assess model-generated rationales for specific error types, including context, word-sense, and pun pair errors.

**Manual error annotation** (1 paper: [Evaluating Spatiotemporal Consistency in Automatically Generated Sewing Instructions](https://aclanthology.org/2025.emnlp-main.934.pdf))
> A procedure where human annotators manually identify and count errors in model-generated text according to a predefined set of categories, such as incorrect assembly operations or order.

## Relationships

### → Manual error analysis
- **Linguistic quality** (construct): *measured_by*, 1 paper
  > To investigate the impact of DPSGD and distillation on inconsistencies and linguistic quality, we manually annotated 50 outputs each from the XSum, MRPC, and Pubmed test sets. (Section 5.4)
  - [Differentially Private Learning Needs Better Model Initialization and Self-Distillation](https://aclanthology.org/2025.naacl-long.455.pdf)
- **Reasoning error** (behavioral indicator): *measured_by*, 1 paper
  > we conduct an in-depth human analysis of the error cases made by GPT-4o, Qwen2-VL-7B, and Llama 3.2-Vision 11B... Through in-depth analysis, we have identified the following ﬁve common error types that current MLLMs are likely to make: (1) Reasoning Error... (Section 4)
  - [Are Multimodal LLMs Robust Against Adversarial Perturbations? RoMMath: A Systematic Evaluation on Multimodal Math Reasoning](https://aclanthology.org/2025.naacl-long.582.pdf)
- **Calculation error** (behavioral indicator): *measured_by*, 1 paper
  > we conduct an in-depth human analysis of the error cases... Through in-depth analysis, we have identified the following ﬁve common error types that current MLLMs are likely to make: ... (5) Calculation Error... (Section 4)
  - [Are Multimodal LLMs Robust Against Adversarial Perturbations? RoMMath: A Systematic Evaluation on Multimodal Math Reasoning](https://aclanthology.org/2025.naacl-long.582.pdf)
