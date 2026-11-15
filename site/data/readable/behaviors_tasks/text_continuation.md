# Text continuation
**Type:** Behavioral indicator  
**Supporting papers:** 13  
**Also known as:** Text completion, Text continuation generation, Open-ended text completion  

## State of the Field

**Space of definitions.** Across the papers, the prevailing usage treats text continuation as generating the next portion of text from a given prefix, prompt, sentence, or opening passage. Most definitions describe success as producing a continuation that coherently and contextually follows the input, and some add that it should logically follow the prefix or preserve stylistic consistency with it. Smaller lines of work formulate it as regenerating the remaining part of a truncated passage, continuing from compressed memory slots, or generating continuations under added logical constraints or in red-teaming setups.

**Variants.** Papers use several nearby names, including text completion, text continuation generation, open-ended text completion, and transcript continuation. The task appears in sentence and article completion, five-token prompt continuation for trial and demonstration settings, continuation from a truncated movie review or other passage prefix, and continuation from speech-derived prompts where paralinguistic cues may shape the preferred completion. Some variants explicitly condition the continuation on style or control requirements, such as continuing in AAE or producing a single continuation that follows logical constraints.

**Space of elicitation and scores.** Only two measurement instruments are linked in the papers: GSM8K and WikiText-103. One paper describes GSM8K as a text-completion benchmark, while another describes WikiText-103 as a standard benchmark for language modeling.

**What it is taken as evidence of.** Across these papers, text continuation is not linked to any construct, so the papers do not specify a construct that it is taken to indicate.

## Sources

**Text continuation** (7 papers: [Curiosity-driven Red-teaming for Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/56ed2bd15b66f709cd81cb1aaa0496b9-Paper-Conference.pdf), [In-context Autoencoder for Context Compression in a Large Language Model](https://proceedings.iclr.cc/paper_files/paper/2024/file/0b276510ec2d3f6613a8b60c41ff0438-Paper-Conference.pdf), [Spoken Question Answering and Speech Continuation Using Spectrogram-Powered LLM](https://proceedings.iclr.cc/paper_files/paper/2024/file/e393677793767624f2821cec8bdd02f1-Paper-Conference.pdf), [Babysit A Language Model From Scratch: Interactive Language Learning by Trials and Demonstrations](https://aclanthology.org/2025.naacl-long.46.pdf), [My LLM might Mimic AAE - But When Should It?](https://aclanthology.org/2025.naacl-long.273.pdf), [Adaptable Logical Control for Large Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/d15c16cf5619a2b1606da5fc88e3f1a9-Paper-Conference.pdf), [Exploring LLMs' Ability to Spontaneously and Conditionally Modify Moral Expressions through Text Manipulation](https://aclanthology.org/2025.acl-long.883.pdf))
> Generating subsequent text following the original context based on memory slots, used to evaluate the model's ability to maintain predictive capability after compression.

**Text completion** (2 papers: [The Impossibility of Fair LLMs](https://aclanthology.org/2025.acl-long.5.pdf), [Adapting Large Language Models via Reading Comprehension](https://proceedings.iclr.cc/paper_files/paper/2024/file/d51cd79a85833b022841f7a2383b32d3-Paper-Conference.pdf))
> The task of generating text to continue a given prompt or sentence.

**Text continuation generation** (1 paper: [DNA-GPT: Divergent N-Gram Analysis for Training-Free Detection of GPT-Generated Text](https://proceedings.iclr.cc/paper_files/paper/2024/file/d4ce6738e84876aa79f13c8bc8b7c5eb-Paper-Conference.pdf))
> Generating the remaining portion of a passage from a truncated prefix.

**Open-ended text completion** (1 paper: [Verifiable by Design: Aligning Language Models to Quote from Pre-Training Data](https://aclanthology.org/2025.naacl-long.191.pdf))
> Continuing a given text prompt in a coherent and contextually appropriate manner without specific task constraints, often used to evaluate generative fluency and consistency.

## Relationships

### Text continuation →
- **WikiText-103** (measurement instrument): *measured_by*, 1 paper
  > WikiText-103 (Merity et al., 2017) is a standard benchmark for language modeling... (Section 4.1, Text completion)
  - [Nearest Neighbor Speculative Decoding for LLM Generation and Attribution](https://proceedings.neurips.cc/paper_files/paper/2024/file/93c099bb4cde51b724eaa6d6d4a4b5e4-Paper-Conference.pdf)
- **GSM8K** (measurement instrument): *measured_by*, 1 paper
  > Choice permutation applies to all benchmarks except GSM8K which is a text-completion benchmark, not a multiple-choice benchmark. (Section 3.1, footnote 7)
  - [metabench - A Sparse Benchmark of Reasoning and Knowledge in Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/4ebc26584810a189ef1e4f173aba4319-Paper-Conference.pdf)
