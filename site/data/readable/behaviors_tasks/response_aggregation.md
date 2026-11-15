# Response aggregation
**Type:** Behavioral indicator  
**Supporting papers:** 7  
**Also known as:** Answer aggregation, Response fusion, Response synthesis  

## State of the Field

**Space of definitions.** Across the definitions, the prevailing usage treats it as combining multiple candidate answers or responses into one final output. Most descriptions emphasize a final answer that is more reliable, higher-quality, coherent, or refined, whether the inputs come from multiple sources, reasoning paths, or selected experts. Some papers make the success criterion more explicit by describing selection of the most reliable or most plausible response, while others add conflict detection, weighted fusion, or iterative synthesis and refinement.

**Variants.** Papers use several near-synonymous labels, including answer aggregation, response fusion, response aggregation, and response synthesis. The settings vary from multi-path aggregation over answers from sub-questions and the original question, to fusing proposed responses given an instruction prompt, to synthesizing outputs from selected experts through semantic conflict detection and weighted information fusion. A smaller variant frames it as a two-stage knowledge graph-guided response integration process for logical consistency, and another describes iterative synthesis and refinement across candidate responses.

**Space of elicitation and scores.** No measurement instrument is linked to it. Instead, the papers describe modules or prompts that carry it out, such as an aggregator that fuses two candidates and selects the most plausible final answer, or a fuser that takes an instruction prompt and proposed responses to generate one or more fused responses.

**What it is taken as evidence of.** At the construct level, it is linked only to Text generation quality. One paper claims a causal relationship from Response aggregation to Text generation quality, describing aggregators as models that synthesize responses into a single, high-quality output. Separately, one paper reports that it is related to Response ranking, where responses are ranked and the best ones are fused into a single higher quality output.

## Sources

**Answer aggregation** (1 paper: [RTQA : Recursive Thinking for Complex Temporal Knowledge Graph Question Answering with Large Language Models](https://aclanthology.org/2025.emnlp-main.499.pdf))
> The process of combining answers derived from multiple sources or reasoning paths to produce a single, more reliable final answer.

**Response fusion** (1 paper: [An Architecture Search Framework for Inference-Time Techniques](https://raw.githubusercontent.com/mlresearch/v267/main/assets/saad-falcon25a/saad-falcon25a.pdf))
> The act of combining multiple candidate responses into a single, higher-quality output using an LLM.

**Response aggregation** (1 paper: [KABB: Knowledge-Aware Bayesian Bandits for Dynamic Expert Coordination in Multi-Agent Systems](https://raw.githubusercontent.com/mlresearch/v267/main/assets/zhang25aa/zhang25aa.pdf))
> The process of synthesizing outputs from multiple selected experts into a single coherent final response, including conflict detection and weighted fusion.

**Response synthesis** (1 paper: [Mixture-of-Agents Enhances Large Language Model Capabilities](https://proceedings.iclr.cc/paper_files/paper/2025/file/5434be94e82c54327bb9dcaf7fca52b6-Paper-Conference.pdf))
> Combining multiple candidate responses into a single refined answer.

## Relationships

### Response aggregation →
- **Text generation quality** (construct): *causes*, 1 paper
  > "Aggregators are models proficient in synthesizing responses from other models into a single, high-quality output."
  - [Mixture-of-Agents Enhances Large Language Model Capabilities](https://proceedings.iclr.cc/paper_files/paper/2025/file/5434be94e82c54327bb9dcaf7fca52b6-Paper-Conference.pdf)

### Associated with
- **Response ranking** (behavioral indicator), 1 paper
  > "their responses are ranked, and the best ones are fused into a single, higher quality output"
  - [An Architecture Search Framework for Inference-Time Techniques](https://raw.githubusercontent.com/mlresearch/v267/main/assets/saad-falcon25a/saad-falcon25a.pdf)
