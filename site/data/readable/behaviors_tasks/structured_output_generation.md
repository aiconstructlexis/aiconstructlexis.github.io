# Structured output generation
**Type:** Behavioral indicator  
**Supporting papers:** 18  
**Also known as:** Result formatting, Configuration generation, JSON generation, Netlist generation, Formalized representation generation, Table generation, Structured generation, Structured text generation  

## State of the Field

**Space of definitions.** Across the literature, the prevailing usage is outputting text that must conform to a prescribed structure, most often a parseable or schema-bound format such as JSON and API or function-call specifications. Papers commonly treat success as strict format compliance, for example exact matching to an API definition, syntactically valid JSON, or adherence to another requested format such as XML, YAML, markdown, HTML, code, or chain-of-thought traces. A smaller line of work uses the same behavior for domain-specific structures, including standardized workflow artifacts, incident-encoded circuit netlists, formalized dialogue representations with intention, slots, and reasoning, and tabular summaries, sometimes with the added requirement of accurate information extraction or valid domain content.

**Variants.** Papers study this behavior under several neighboring task names. Common variants are JSON generation, result formatting, configuration generation, netlist generation, and table generation, while other papers call it structured generation, structured text generation, or formalized representation generation. The settings range from converting solver outputs into a fixed JSON format, to generating YAML experiment configurations from prior feedback, to turning dialogue utterances into formalized turn representations, to producing tables from text or scientific papers, and one paper also contrasts JSON with plain string outputs under compression.

**Space of elicitation and scores.** It is measured by one linked instrument, TACT. In that instrument, models are asked to generate the appropriate table from a TACT instruction and its corresponding text, so the measurement operationalizes this behavior as constructing the correct table under an explicit instruction. No other measurement instrument is linked to it.

**What it is taken as evidence of.** No construct is linked to this behavior. The papers therefore do not state a shared construct that structured output generation is taken to indicate.

## Sources

**Structured output generation** (5 papers: [ToolACE: Winning the Points of LLM Function Calling](https://proceedings.iclr.cc/paper_files/paper/2025/file/663865ea167425c6c562cb0b6bcf76c7-Paper-Conference.pdf), [Can Compressed LLMs Truly Act? An Empirical Evaluation of Agentic Capabilities in LLM Compression](https://raw.githubusercontent.com/mlresearch/v267/main/assets/dong25k/dong25k.pdf), [DICE: Structured Reasoning in LLMs through SLM-Guided Chain-of-Thought Correction](https://aclanthology.org/2025.emnlp-main.355.pdf), [MetaGPT: Meta Programming for A Multi-Agent Collaborative Framework](https://proceedings.iclr.cc/paper_files/paper/2024/file/6507b115562bb0a305f1958ccc87355a-Paper-Conference.pdf), [PROMPTEVALS: A Dataset of Assertions and Guardrails for Custom Production Large Language Model Pipelines](https://aclanthology.org/2025.naacl-long.213.pdf))
> Producing outputs in a required structured format that matches API or function-call specifications.

**Result formatting** (1 paper: [Planning Anything with Rigor: General-Purpose Zero-Shot Planning with LLM-based Formalized Programming](https://proceedings.iclr.cc/paper_files/paper/2025/file/a1c8a68e52499c9396854e3f967e37c0-Paper-Conference.pdf))
> Converting solver outputs into a fixed structured output format.

**JSON generation** (1 paper: [Earley-Driven Dynamic Pruning for Efficient Structured Decoding](https://raw.githubusercontent.com/mlresearch/v267/main/assets/sun25v/sun25v.pdf))
> The task of producing text that is a syntactically valid JSON object, often based on a natural language prompt or other input.

**Netlist generation** (1 paper: [AUTOCIRCUIT-RL: Reinforcement Learning-Driven LLM for Automated Circuit Topology Generation](https://raw.githubusercontent.com/mlresearch/v267/main/assets/vijayaraghavan25a/vijayaraghavan25a.pdf))
> Outputting a textual representation of a circuit as a list of component-to-node connections, formatted using incident encoding.

**Configuration generation** (1 paper: [PINNsAgent: Automated PDE Surrogation with Large Language Models](https://raw.githubusercontent.com/mlresearch/v267/main/assets/wuwu25a/wuwu25a.pdf))
> The task of producing structured configuration files, such as in YAML format, that specify the hyperparameters and settings for an experiment.

**Formalized representation generation** (1 paper: [From Schema to State: Zero-Shot Scheme-Only Dialogue State Tracking via Diverse Synthetic Dialogue and Step-by-Step Distillation](https://aclanthology.org/2025.emnlp-main.85.pdf))
> The production of structured, unambiguous dialogue turn representations that include speaker intention, relevant slots, and explanatory reasoning, derived from natural language utterances.

**Table generation** (1 paper: [From Automation to Autonomy: A Survey on Large Language Models in Scientific Discovery](https://aclanthology.org/2025.emnlp-main.895.pdf))
> Creating structured tabular summaries from scientific literature or data.

**Structured generation** (1 paper: [Pre3: Enabling Deterministic Pushdown Automata for Faster Structured LLM Generation](https://aclanthology.org/2025.acl-long.551.pdf))
> Producing model outputs that conform to a specified syntactic format such as JSON, code, or chain-of-thought traces.

**Structured text generation** (1 paper: [Middle-Layer Representation Alignment for Cross-Lingual Transfer in Fine-Tuned LLMs](https://aclanthology.org/2025.acl-long.778.pdf))
> Producing well-formed, structured outputs such as JSON from natural language input, requiring adherence to format and accurate information extraction.

## Relationships

### Structured output generation →
- **TACT** (measurement instrument): *measured_by*, 1 paper
  > We assess the capabilities of LLMs to generate the appropriate tables given a TACT instruction and its corresponding text, tasking the model to construct the correct table based on the specified instruction. (Section 5.1)
  - [TACT: Advancing Complex Aggregative Reasoning with Information Extraction Tools](https://proceedings.neurips.cc/paper_files/paper/2024/file/3d7025dc9bd4c8b6fb1eef80cc618008-Paper-Datasets_and_Benchmarks_Track.pdf)
