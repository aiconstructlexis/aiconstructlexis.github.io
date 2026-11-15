# Time-series feature extraction ability
**Type:** Construct  
**Supporting papers:** 4  
**Also known as:** Feature extraction  

## State of the Field

**Space of definitions.** The only explicit definition treats this as the model's ability to identify and use relevant patterns from time-series data for reasoning. In that framing, the relevant patterns include pictorial, time-aware, cross-dimension, and frequency-domain features, and the accompanying discussion says that "most of these planned features are difficult to extract from numerical time series" while "visualization empowers feature extraction" (A Picture is Worth A Thousand Numbers: Enabling LLMs Reason about Time Series via Visualization).

**Space of facets.** Systematization is limited and centers on the feature types named in the definition: pictorial, time-aware, cross-dimension, and frequency-domain. The same framing places the construct alongside accurate reasoning and contrasts harder extraction from numerical time series with extraction supported by visualization, but no other subtypes, synonymies, or broader hierarchies are explicitly specified.

**Space of measurement.** No measurement instrument is linked to this construct, and no behavioral indicator is linked to it. Accordingly, papers do not operationalize it here through a named benchmark, human evaluation, LLM-as-a-judge setup, probe, or analysis; instead, they discuss it through claims about the difficulty of extracting features from numerical time series and the claim that visualization empowers feature extraction.

**Links.** One construct link is recorded: A Decision-Language Model (DLM) for Dynamic Restless Multi-Armed Bandit Tasks in Public Health claims a causal relationship from Logical reasoning to Time-series feature extraction ability. Its evidence is the statement about "analyzing the precision and recall of finding relevant features through the usage of world knowledge and logical reasoning."

## Sources

**Feature extraction** (1 paper: [A Picture is Worth A Thousand Numbers: Enabling LLMs Reason about Time Series via Visualization](https://aclanthology.org/2025.naacl-long.383.pdf))
> The model's ability to identify and utilize relevant patterns from time-series data, such as pictorial, time-aware, cross-dimension, or frequency-domain features, which are critical for accurate reasoning.

## Relationships

### → Time-series feature extraction ability
- **Logical reasoning** (construct): *causes*, 1 paper
  > analyzing the precision and recall of finding relevant features through the usage of world knowledge and logical reasoning (Section 4.5).
  - [A Decision-Language Model (DLM) for Dynamic Restless Multi-Armed Bandit Tasks in Public Health](https://proceedings.neurips.cc/paper_files/paper/2024/file/074f42212be2c8ee651db00f17965ec4-Paper-Conference.pdf)
