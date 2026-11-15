# DecodingTrust
**Type:** Measurement instrument  
**Supporting papers:** 8  
**Also known as:** Decoding Trust  

## State of the Field

**What it is.** Across the surveyed work, the prevailing usage treats DecodingTrust as a benchmark dataset for evaluating LLM trustworthiness, and often safety, with several papers describing it as covering multiple perspectives. Some papers narrow that broad framing to particular components, especially a stereotypes partition, described in one study as 48 statements for race groups black and white, and a privacy dataset centered on the Enron email extraction task. A smaller framing presents it as a public leaderboard that integrates large amounts of new test data to evaluate and rank safety and trustworthiness, and another describes it through red-teaming prompts or instructions.

**What it is claimed to measure.** Papers link DecodingTrust to 2 constructs and 1 behavioral indicator. Most definitions frame it as measuring Trustworthiness, while other papers use it to measure Stereotyping and Privacy leakage, with the privacy use tied to the Enron email extraction task and data leakage. The measurement claims therefore span both a broad construct and more specific targets, rather than converging on only one use.

**Space of uses.** No measurement instrument is linked to it through formal relationships. In practice, papers position it both as a broad benchmark for trustworthiness and as a source of specific evaluation slices, and they mention it alongside TrustLLM, CrowS-Pairs, AdvBench, SafetyPrompt, and Enkrypt AI. These pairings vary by use, including stereotype evaluation with CrowS-Pairs, comparison to TrustLLM as another broad trustworthiness benchmark, grouping with AdvBench and SafetyPrompt as collections of red-teaming instructions, and mention with Enkrypt AI as a leaderboard using large amounts of new test data.

**Concerns raised.** One paper raises a concern about its testing format, describing DecodingTrust as using static templates that do not account for the dynamic nature of red-teaming algorithms, which that paper says limits effectiveness.

## Sources

**Decoding Trust** (1 paper: [Certifying Counterfactual Bias in LLMs](https://proceedings.iclr.cc/paper_files/paper/2025/file/1c6decac1477fbcc2cbf12d314ce0133-Paper-Conference.pdf))
> A benchmark dataset used to evaluate LLM properties, including stereotype bias against demographic groups, here using the stereotypes partition.

**DecodingTrust** (6 papers: [IterGen: Iterative Semantic-aware Structured LLM Generation with Backtracking](https://proceedings.iclr.cc/paper_files/paper/2025/file/3d3a9e085540c65dd3e5731361f9320e-Paper-Conference.pdf), [Raising the Bar: Investigating the Values of Large Language Models via Generative Evolving Testing](https://raw.githubusercontent.com/mlresearch/v267/main/assets/jiang25l/jiang25l.pdf), [ALI-Agent: Assessing LLMs' Alignment with Human Values via Agent-based Evaluation](https://proceedings.neurips.cc/paper_files/paper/2024/file/b35c38f70065ac6c694089ca93a015bb-Paper-Conference.pdf), [Enhancing Multiple Dimensions of Trustworthiness in LLMs via Sparse Activation Control](https://proceedings.neurips.cc/paper_files/paper/2024/file/1cb5b3d64bdf3c6642c8d9a8fbecd019-Paper-Conference.pdf), [Jailbreaking Large Language Models Against Moderation Guardrails via Cipher Characters](https://proceedings.neurips.cc/paper_files/paper/2024/file/6d56bc83ae9a4fafdce050bb36f04174-Paper-Conference.pdf), [SG-Bench: Evaluating LLM Safety Generalization Across Diverse Tasks and Prompt Types](https://proceedings.neurips.cc/paper_files/paper/2024/file/de7b99107c53e60257c727dc73daf1d1-Paper-Datasets_and_Benchmarks_Track.pdf))
> A benchmark dataset designed to evaluate the trustworthiness of LLMs, including tasks related to privacy, such as the Enron email extraction task used to assess data leakage.

## Relationships

### → DecodingTrust
- **Trustworthiness** (construct): *measured_by*, 1 paper
  > DecodingTrust (Wang et al. [2023]) was among the first to aim for a comprehensive assessment of trustworthiness in GPT models from several perspectives. (Section 2.1)
  - [Enhancing Multiple Dimensions of Trustworthiness in LLMs via Sparse Activation Control](https://proceedings.neurips.cc/paper_files/paper/2024/file/1cb5b3d64bdf3c6642c8d9a8fbecd019-Paper-Conference.pdf)
- **Privacy leakage** (behavioral indicator): *measured_by*, 1 paper
  > We use the DecodingTrust (Wang et al., 2024) privacy dataset, focusing on the Enron email extraction task. (Section 4.2)
  - [IterGen: Iterative Semantic-aware Structured LLM Generation with Backtracking](https://proceedings.iclr.cc/paper_files/paper/2025/file/3d3a9e085540c65dd3e5731361f9320e-Paper-Conference.pdf)
- **Stereotyping** (construct): *measured_by*, 1 paper
  > To verify ALI-Agent’s effectiveness as a general evaluation framework, we conduct experiments on six datasets from three distinct aspects of human values: stereotypes (DecodingTrust [11], CrowS-Pairs [2])...
  - [ALI-Agent: Assessing LLMs' Alignment with Human Values via Agent-based Evaluation](https://proceedings.neurips.cc/paper_files/paper/2024/file/b35c38f70065ac6c694089ca93a015bb-Paper-Conference.pdf)
