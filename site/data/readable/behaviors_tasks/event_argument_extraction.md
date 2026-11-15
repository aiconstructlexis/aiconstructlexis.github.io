# Event argument extraction
**Type:** Behavioral indicator  
**Supporting papers:** 6  
**Also known as:** Event Argument Extraction, Argument extraction  

## State of the Field

**Space of definitions.** Across the surveyed work, the prevailing usage treats event argument extraction as identifying event arguments in text and assigning each argument its role, explicitly assuming that the event trigger is already given. A smaller line of work uses the shorter label argument extraction for scientific events, where the task is to find the text spans that serve as arguments for a scientific activity and classify them into roles such as context, method, or result. Across both framings, the shared task is to recover argument spans and label them with semantic roles, though they differ in whether the trigger-given setup is stated explicitly and in the role inventory they foreground.

**Variants.** Papers study this behavior in multiple settings. One recurring setting is cross-lingual transfer, described as event argument extraction spanning 20 languages. Another is scientific event extraction, where the task is decomposed into Argument Identification, predicting the set of argument spans for each event, and Argument Classification, predicting the semantic role for each identified span.

**Space of elicitation and scores.** Papers link this behavior to one measurement instrument, TextEE. In the linked usage, authors say they adopt TextEE to compare models while focusing on defining correctness at the event argument level.

**What it is taken as evidence of.** The papers do not link event argument extraction to any construct, so they do not make an explicit claim about what broader construct this behavior indicates.

## Sources

**Event Argument Extraction** (2 papers: [Constrained Decoding for Cross-lingual Label Projection](https://proceedings.iclr.cc/paper_files/paper/2024/file/67390075fe466276797f489115582cdc-Paper-Conference.pdf), [GoLLIE: Annotation Guidelines improve Zero-Shot Information-Extraction](https://proceedings.iclr.cc/paper_files/paper/2024/file/cda04d7ea67ea1376bf8c6962d8541e0-Paper-Conference.pdf))
> The task of identifying event arguments and their specific roles in text, given the presence of an event trigger.

**Argument extraction** (1 paper: [SciEvent: Benchmarking Multi-domain Scientific Event Extraction](https://aclanthology.org/2025.emnlp-main.871.pdf))
> The task of identifying text spans that serve as arguments for a scientific event and classifying them into specific semantic roles like Context, Method, or Result.

## Relationships

### Event argument extraction →
- **TextEE** (measurement instrument): *measured_by*, 1 paper
  > In our study, while we adopt TextEE to compare models, our primary focus is on defining correctness at the event argument level. (Section 3).
  - [BEMEAE: Moving Beyond Exact Span Match for Event Argument Extraction](https://aclanthology.org/2025.naacl-long.295.pdf)
