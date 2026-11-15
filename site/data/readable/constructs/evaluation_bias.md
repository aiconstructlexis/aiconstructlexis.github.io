# Evaluation bias
**Type:** Construct  
**Supporting papers:** 9  
**Also known as:** Judge bias, Affinity bias, Bias in feedback, Implicit bias  

## State of the Field

**Space of definitions.** Across these papers, the dominant framing treats evaluation bias as systematic distortion in model-based judging or assessment: a model acting as a reviewer or judge may unfairly favor or disfavor responses, and one formulation defines judge bias as the expected difference between a judge's proxy score and the ground-truth score. A parallel framing defines it more broadly as systematic deviation in estimated model capability caused by flaws in the evaluation protocol. Smaller lines of work use narrower variants, including self-favoring bias, affinity bias toward models whose predictions are functionally similar to the judge's own, bias in human or AI-generated feedback, and implicit preferences that lead judges to prioritize some criteria over explicit instructions.

**Space of facets.** Papers break the construct down in several ways. One account decomposes evaluation bias into original, independent, and related terms, while another describes bias in feedback through presentation-related, social-related, content-related, and cognitive-related biases. Across judge-centered work, affinity bias, self-favoring bias, and implicit bias appear as named variants, so related labels are used both for overall evaluation error and for specific preference patterns inside judges.

**Space of measurement.** Operationalization is narrow in named instruments: papers link evaluation bias to 1 measurement instrument, LLM-as-a-judge, and no behavioral indicators. The operationalizations described in the papers are mostly analytical: one study uses preference gap (PG) to evaluate bias, another defines judge bias as the expected difference between proxy and ground-truth scores, and another defines evaluation bias as the difference between expected estimated capability and true capability. These choices largely match the prevailing definitions that cast the construct as systematic deviation or unfair favoring in judging.

**Links.** Papers only relate evaluation bias to LLM-as-a-judge. One paper states that "Agents-as-an-Evaluator exhibit two biases: data bias and model bias," placing the construct within LLM-based evaluation setups. No causal or correlational links are reported, and no other construct links are reported.

## Sources

**Evaluation bias** (2 papers: [PiCO: Peer Review in LLMs based on Consistency Optimization](https://proceedings.iclr.cc/paper_files/paper/2025/file/39e9c5913c970e3e49c2df629daff636-Paper-Conference.pdf), [Unbiased Evaluation of Large Language Models from a Causal Perspective](https://raw.githubusercontent.com/mlresearch/v267/main/assets/chen25bi/chen25bi.pdf))
> A systematic tendency for a model, when acting as a reviewer, to unfairly favor or disfavor certain models' responses, including a self-favoring bias.

**Judge bias** (1 paper: [Limits to scalable evaluation at the frontier: LLM as judge won’t beat twice the data](https://proceedings.iclr.cc/paper_files/paper/2025/file/4264ee4376776907c0b87ed70b959585-Paper-Conference.pdf))
> The systematic error introduced when using a model as a judge, defined as the expected difference between the judge's proxy score and the ground-truth score.

**Affinity bias** (1 paper: [Great Models Think Alike and this Undermines AI Oversight](https://raw.githubusercontent.com/mlresearch/v267/main/assets/goel25b/goel25b.pdf))
> The tendency of an LLM judge to assign higher scores to models whose predictions are functionally similar to its own, independent of actual performance.

**Bias in feedback** (1 paper: [Position: Challenges and Future Directions of Data-Centric AI Alignment](https://raw.githubusercontent.com/mlresearch/v267/main/assets/yeh25b/yeh25b.pdf))
> Systematic distortions in human or AI-generated feedback that favor certain perspectives, demographics, or values due to non-representative data or model limitations.

**Implicit bias** (1 paper: [Style Outweighs Substance: Failure Modes of LLM Judges in Alignment Benchmarking](https://proceedings.iclr.cc/paper_files/paper/2025/file/1eb36d07ebb13be16ddbda679a95018b-Paper-Conference.pdf))
> An LLM-judge's internal, unstated preference for certain criteria over others, which influences its decisions independently of or in violation of explicit instructions.

## Relationships

### Associated with
- **LLM-as-a-judge** (measurement instrument), 1 paper
  > “Agents-as-an-Evaluator exhibit two biases: data bias and model bias.”
  - [Unbiased Evaluation of Large Language Models from a Causal Perspective](https://raw.githubusercontent.com/mlresearch/v267/main/assets/chen25bi/chen25bi.pdf)
