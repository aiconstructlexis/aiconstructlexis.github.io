# OpinionQA
**Type:** Measurement instrument  
**Supporting papers:** 8  
**Also known as:** OpinionsQA  

## State of the Field

**What it is.** Across the papers, the prevailing usage treats OpinionQA as a survey-based benchmark or dataset built from Pew Research's American Trends Panel, using public opinion questions and demographic-group response distributions to compare model outputs with those of U.S. respondents. Definitions often describe it as multiple-choice survey or QA data covering topics such as science, politics, health, and personal relationships, and some specify versions such as a subsampled train/test split or a U.S. opinions subset labeled OQA or OpinionQA W27. A smaller line of work refers to "OpinionsQA" as persona data used in prior work to learn persona embeddings and soft prompts.

**What it is claimed to measure.** Papers use OpinionQA to measure 2 constructs and no behavioral indicators. The linked constructs are Personalization and Pluralistic alignment, both through measured_by relations: personalization work describes it as a dataset proposed to measure the steerability of LLMs for specific users or social groups, while pluralistic-alignment work places it among datasets for quantifying distributional alignment. These claims therefore span more than one construct, although the dominant descriptive framing presents the benchmark as evaluating how model response distributions match demographic or public opinion distributions.

**Space of uses.** Several papers use OpinionQA as part of a multi-dataset evaluation rather than alone. It appears alongside GlobalOpinionQA in work on personalization and on distributional alignment, alongside Value Kaleidoscope in one evaluation, and within a three-dataset setup that also includes NYT Book Opinions. Another paper cites it as source persona data in prior work on learning persona embeddings and designing soft prompts for steering model behavior.

## Sources

**OpinionQA** (6 papers: [Few-shot Personalization of LLMs with Mis-aligned Responses](https://aclanthology.org/2025.naacl-long.598.pdf), [Benchmarking Distributional Alignment of Large Language Models](https://aclanthology.org/2025.naacl-long.2.pdf), [Uncertainty Quantification for LLM-Based Survey Simulations](https://raw.githubusercontent.com/mlresearch/v267/main/assets/huang25am/huang25am.pdf), [Exploring Chain-of-Thought Reasoning for Steerable Pluralistic Alignment](https://aclanthology.org/2025.emnlp-main.1301.pdf), [Reward Model Perspectives: Whose Opinions Do Reward Models Reward?](https://aclanthology.org/2025.emnlp-main.754.pdf), [Value Profiles for Encoding Human Variation](https://aclanthology.org/2025.emnlp-main.106.pdf))
> A survey-based benchmark using PEW public opinion questions and demographic-group response distributions to evaluate distributional alignment.

**OpinionsQA** (1 paper: [Evaluating the Prompt Steerability of Large Language Models](https://aclanthology.org/2025.naacl-long.400.pdf))
> A persona dataset used in prior work to learn persona embeddings and design soft-prompts for steering model behavior.

## Relationships

### → OpinionQA
- **Personalization** (construct): *measured_by*, 1 paper
  > For the experiments, we first use two multiple-choice QA datasets proposed to measure the steerability of LLMs for specific users (or social groups): OpinionQA (Santurkar et al., 2023) and GlobalOpinionQA (Durmus et al., 2023). (Section 4.1)
  - [Few-shot Personalization of LLMs with Mis-aligned Responses](https://aclanthology.org/2025.naacl-long.598.pdf)
- **Pluralistic alignment** (construct): *measured_by*, 1 paper
  > In this section, we describe three datasets for quantifying distributional alignment – OpinionQA (Santurkar et al., 2023), GlobalOpinionQA (Durmus et al., 2024), and a new non-political subjective opinion dataset, NYT Book Opinions.
  - [Benchmarking Distributional Alignment of Large Language Models](https://aclanthology.org/2025.naacl-long.2.pdf)
