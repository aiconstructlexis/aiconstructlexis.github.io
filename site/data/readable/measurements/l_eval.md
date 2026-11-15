# L-Eval
**Type:** Measurement instrument  
**Supporting papers:** 8  
**Also known as:** L-eval  

## State of the Field

**What it is.** Across the surveyed work, the prevailing usage treats L-Eval as a benchmark, often described as a standardized long-context evaluation suite for language models. Most definitions frame it around long-context capability or performance, with closed-ended tasks, especially multiple-choice and true or false question answering, while some papers describe a broader suite with both closed-ended and open-ended tasks for understanding, reasoning, summarization, and open-format question answering over long inputs. A smaller line of work specifies its contents as 508 long documents from various domains, divided into 20 subtasks or "20 smaller long sequence datasets," and one paper notes that its tasks appear at varying input lengths.

**What it is claimed to measure.** Relationship claims are concentrated rather than spread broadly: papers link L-Eval to one construct and one behavioral indicator. The dominant claim is that it measures long-context understanding, with several papers describing it as a commonly used long-context benchmark or as part of a "comprehensive evaluation of long-context understanding." A smaller usage links it to long-context generation, where one paper reports evaluating models with L-Eval's closed-ended and open-ended task groups.

**Space of uses.** In practice, papers frequently use L-Eval alongside LongBench, and some place it with LooGLE as a multitask benchmark for long-context evaluation. Usage often narrows to subsets rather than the full suite: some studies focus on four closed-ended tasks, while another reports four open-ended QA tasks scored with F1 and four multiple-choice QA tasks scored with accuracy. One paper also cites it among specialized benchmarks when comparing CS-Bench with long-text and reasoning-oriented evaluations.

**Concerns raised.** Only a small number of papers state limitations directly. One reports that, although L-Eval is designed to assess long-form context understanding capabilities, its context lengths are relatively shorter, and another says that benchmarks such as L-Eval scale only up to 40,000 tokens.

## Sources

**L-eval** (4 papers: [CS-Bench: A Comprehensive Benchmark for Large Language Models towards Computer Science Mastery](https://proceedings.iclr.cc/paper_files/paper/2025/file/89c61fce5a8b73871d1c4073f486b134-Paper-Conference.pdf), [LCIRC: A Recurrent Compression Approach for Efficient Long-form Context and Query Dependent Modeling in LLMs](https://aclanthology.org/2025.naacl-long.524.pdf), [BABILong: Testing the Limits of LLMs with Long Context Reasoning-in-a-Haystack](https://proceedings.neurips.cc/paper_files/paper/2024/file/c0d62e70dbc659cc9bd44cbcf1cb652f-Paper-Datasets_and_Benchmarks_Track.pdf), [Mixture of In-Context Experts Enhance LLMs' Long Context Awareness](https://proceedings.neurips.cc/paper_files/paper/2024/file/91315fbb83ce353ae5538cba395f70d1-Paper-Conference.pdf))
> L-eval is a benchmark used for comparing CS-Bench with long-text and reasoning-oriented evaluations.

**L-Eval** (2 papers: [Bridging Context Gaps: Leveraging Coreference Resolution for Long Contextual Understanding](https://proceedings.iclr.cc/paper_files/paper/2025/file/a1b71d48d4806ecbe5a9e19fa3f10fdc-Paper-Conference.pdf), [Extending LLM Context Window with Adaptive Grouped Positional Encoding: A Training-Free Method](https://aclanthology.org/2025.acl-long.28.pdf))
> L-Eval is a benchmark designed to assess the long-context capabilities of LLMs, featuring closed-ended tasks such as multiple-choice and true/false question answering.

## Relationships

### → L-Eval
- **Long-context understanding** (construct): *measured_by*, 5 papers
  > Following the L-Eval benchmark [1], we evaluated the LLM with tasks categorized into two main groups: closed-ended and open-ended tasks. Closed-ended tasks primarily focus on the capacity for understanding and reasoning within long contexts... (Section 4.2).
  - [Mixture of In-Context Experts Enhance LLMs' Long Context Awareness](https://proceedings.neurips.cc/paper_files/paper/2024/file/91315fbb83ce353ae5538cba395f70d1-Paper-Conference.pdf)
  - [ReAttention: Training-Free Infinite Context with Finite Attention Scope](https://proceedings.iclr.cc/paper_files/paper/2025/file/ee1f0da706829d7f198eac0edaacc338-Paper-Conference.pdf)
  - [Bridging Context Gaps: Leveraging Coreference Resolution for Long Contextual Understanding](https://proceedings.iclr.cc/paper_files/paper/2025/file/a1b71d48d4806ecbe5a9e19fa3f10fdc-Paper-Conference.pdf)
  - [LCIRC: A Recurrent Compression Approach for Efficient Long-form Context and Query Dependent Modeling in LLMs](https://aclanthology.org/2025.naacl-long.524.pdf)
  - [Extending LLM Context Window with Adaptive Grouped Positional Encoding: A Training-Free Method](https://aclanthology.org/2025.acl-long.28.pdf)
- **Long-context generation** (behavioral indicator): *measured_by*, 1 paper
  > evaluate the enhanced LLM's capability to zero-shot undertake multiple tasks in long context understanding and generation, as detailed in Section 4.2... Following the L-Eval benchmark [1]
  - [Mixture of In-Context Experts Enhance LLMs' Long Context Awareness](https://proceedings.neurips.cc/paper_files/paper/2024/file/91315fbb83ce353ae5538cba395f70d1-Paper-Conference.pdf)
