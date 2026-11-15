# Long-term memory
**Type:** Construct  
**Supporting papers:** 5  
**Also known as:** Long-term memory retention  

## State of the Field

**Space of definitions.** Across the definitions, the prevailing usage treats long-term memory as retaining, recalling, storing, or using relevant information over extended periods, interactions, or multi-step tasks. Most descriptions tie this to downstream coherence, either coherent and contextually consistent reasoning or consistent, human-like conversations, while one paper also characterizes it as a dynamic and interconnected knowledge structure. The main variation is scope: some papers place it in financial tasks or dialogue systems, while a smaller framing narrows it to long-term memory retention, emphasizing recall from prior interactions despite intervening irrelevant content.

**Space of facets.** One paper explicitly organizes long-term memory into core abilities and links it to information extraction, defined there as recalling specific information from extensive interactive histories. Across papers, the label is also used at different levels of abstraction: as a broad storage-and-retrieval ability, as a dialogue-system capacity for maintaining consistency over extended interactions, and as long-term memory retention focused on prior interactions. Another paper contrasts human long-term memory's dynamic, interconnected nature with vector retrieval.

**Space of measurement.** Operationalization is narrow: papers connect the construct to 1 measurement instrument and 1 behavioral indicator. The instrument is the benchmark LongMemEval, described as evaluating the long-context memory ability of chat assistants across memory tasks, and the only linked behavioral indicator is information extraction, described as recalling specific information from extensive interactive histories. This measurement emphasis is on recall from long interaction histories, while several definitions also include using retained information for coherent reasoning or conversation consistency.

**Links.** Papers link long-term memory to 2 constructs. One paper claims a causal relationship from long-term memory to knowledge integration, describing a framework inspired by human long-term memory to enable deeper and more efficient knowledge integration over new experiences, and one paper reports that long-horizon planning is related to long-term memory because partial observability creates demand to maintain past useful experiences. One paper also reports that information extraction is related to long-term memory, and no paper reports a correlational link.

## Sources

**Long-term memory** (3 papers: [FinEval: A Chinese Financial Domain Knowledge Evaluation Benchmark for Large Language Models](https://aclanthology.org/2025.naacl-long.318.pdf), [MADial-Bench: Towards Real-world Evaluation of Memory-Augmented Dialogue Generation](https://aclanthology.org/2025.naacl-long.499.pdf), [From RAG to Memory: Non-Parametric Continual Learning for Large Language Models](https://raw.githubusercontent.com/mlresearch/v267/main/assets/gutierrez25a/gutierrez25a.pdf))
> The capacity to retain and utilize relevant information across extended or multi-step financial tasks, supporting coherent and contextually consistent reasoning.

**Long-term memory retention** (1 paper: [From Tools to Teammates: Evaluating LLMs in Multi-Session Coding Interactions](https://aclanthology.org/2025.acl-long.964.pdf))
> The latent ability of an LLM to retain and recall relevant information from prior interactions over extended sequences of dialogue, despite intervening irrelevant content.

## Relationships

### Long-term memory →
- **Knowledge integration** (construct): *causes*, 1 paper
  > HippoRAG, a novel retrieval framework inspired by the hippocampal indexing theory of human long-term memory to enable deeper and more efficient knowledge integration over new experiences. (Abstract)
  - [HippoRAG: Neurobiologically Inspired Long-Term Memory for Large Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/6ddc001d07ca4f319af96a3024f6dbd1-Paper-Conference.pdf)
- **LongMemEval** (measurement instrument): *measured_by*, 1 paper
  > “LONGMEMEVAL ... was a challenging benchmark designed to evaluate the long-context memory ability of chat assistants across six memory tasks, including ... knowledge update (KU) ...”
  - [Recall with Reasoning: Chain-of-Thought Distillation for Mamba's Long-Context Memory and Extrapolation](https://aclanthology.org/2025.emnlp-main.235.pdf)

### Associated with
- **Information extraction** (behavioral indicator), 1 paper
  > To comprehensively reflect the challenge, LONGMEMEVAL formulates five core long-term memory abilities: • Information Extraction (IE): Ability to recall specific information from extensive interactive histories... (Section 3.2)
  - [LongMemEval: Benchmarking Chat Assistants on Long-Term Interactive Memory](https://proceedings.iclr.cc/paper_files/paper/2025/file/d813d324dbf0598bbdc9c8e79740ed01-Paper-Conference.pdf)
- **Long-horizon planning** (construct), 1 paper
  > “long-horizontal reasoning due to the partial observability of complex GCC tasks, which also leads to the demand for long-term memory to maintain past useful experiences”
  - [Cradle: Empowering Foundation Agents towards General Computer Control](https://raw.githubusercontent.com/mlresearch/v267/main/assets/tan25h/tan25h.pdf)
