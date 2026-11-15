# SAFE
**Type:** Measurement instrument  
**Supporting papers:** 3  

## State of the Field

**What it is.** Across the surveyed work, SAFE is most commonly presented as Search-Augmented Factuality Evaluator, an LLM-based search procedure, sometimes framed as an investigative agent, that uses iterative Google Search queries to assess whether generated facts are supported by external evidence. In Long-form factuality in large language models, it is described more specifically as splitting a long-form response into individual facts, checking relevance, searching the web, and labeling each fact as supported, not supported, or irrelevant; other definitions use the broader formulation of asking whether search results support a fact.

**What it is claimed to measure.** Papers link SAFE to 3 behavioral indicators and no constructs. The prevailing measurement claim centers on Hallucination: one paper uses SAFE to quantify LLM hallucinations, and related evidence says it enables direct measurement of hallucination. The other linked indicators, Fact checking and Search query generation, are reported as related to SAFE rather than as additional things it measures, so the explicit measurement claims converge on hallucination.

**Space of uses.** Papers use SAFE as an evaluation procedure for long-form responses and as a public metric for quantifying hallucination. The clearest paired use is alongside FActScore, where one study states that it quantifies LLM hallucinations with "two public metrics: FActScore and SAFE"; elsewhere SAFE is positioned as a multi-step procedure that breaks responses into facts, sends Google Search queries, and determines whether each fact is supported by the search results.

## Sources

**SAFE** (2 papers: [Can Knowledge Graphs Make Large Language Models More Trustworthy? An Empirical Study Over Open-ended Question Answering](https://aclanthology.org/2025.acl-long.622.pdf), [Long-form factuality in large language models](https://proceedings.neurips.cc/paper_files/paper/2024/file/937ae0e83eb08d2cb8627fe1def8c751-Paper-Conference.pdf))
> Language model-based investigative agent that uses iterative Google Search queries to assess whether generated facts are supported by external evidence.

## Relationships

### → SAFE
- **Hallucination** (behavioral indicator): *measured_by*, 1 paper
  > it enables direct measurement of hallucination using metrics such as FActScore (Min et al., 2023) and SAFE (Wei et al., 2024) (Section 1)
  - [Can Knowledge Graphs Make Large Language Models More Trustworthy? An Empirical Study Over Open-ended Question Answering](https://aclanthology.org/2025.acl-long.622.pdf)

### Associated with
- **Search query generation** (behavioral indicator), 1 paper
  > SAFE utilizes an LLM to... comprising sending search queries to Google Search...
  - [Long-form factuality in large language models](https://proceedings.neurips.cc/paper_files/paper/2024/file/937ae0e83eb08d2cb8627fe1def8c751-Paper-Conference.pdf)
- **Fact checking** (behavioral indicator), 1 paper
  > ...and determining whether a fact is supported by the search results.
  - [Long-form factuality in large language models](https://proceedings.neurips.cc/paper_files/paper/2024/file/937ae0e83eb08d2cb8627fe1def8c751-Paper-Conference.pdf)
