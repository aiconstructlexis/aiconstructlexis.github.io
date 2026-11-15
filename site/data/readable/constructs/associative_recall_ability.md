# Associative recall ability
**Type:** Construct  
**Supporting papers:** 7  
**Also known as:** Associative recall, Associative memory retrieval  

## State of the Field

**Space of definitions.** Across the definitions, the common thread is cue-based retrieval. One paper gives a narrow formulation, the ability to retrieve a specific value when prompted with its associated key, while another uses a broader latent-memory framing: retrieving stored patterns or knowledge by matching a query to the most relevant memory through similarity-based dynamics. A nearby usage places associative recall within in-context retrieval, described as precisely locating and extracting tokens presented earlier in the sequence.

**Space of facets.** Papers mainly situate this construct inside broader retrieval and memory language. It is explicitly treated as an instance of in-context retrieval, and the alternative label associative memory retrieval casts prompt-based inference as a memory retrieval process in which attention retrieves a stored vector from key-value pairs that best matches a query embedding. The main variation is between a direct key-to-value retrieval description and a broader memory-matching description.

**Space of measurement.** Papers link it to 3 measurement instruments: MQAR, SQuAD v1.1, and SWDE, with no behavioral indicators or other constructs linked to it. The operationalization is explicit task performance: one paper says the model's recall capability is assessed using the MQAR Task, while another uses "Recall" as the average performance across FDA, SWDE, and SQuAD, which ties the construct here to SWDE and SQuAD v1.1. In these papers, the construct is therefore measured through performance on named retrieval tasks.

## Sources

**Associative recall** (1 paper: [Gated Delta Networks: Improving Mamba2 with Delta Rule](https://proceedings.iclr.cc/paper_files/paper/2025/file/4904fad153f6434a7bcf04465d4be2cc-Paper-Conference.pdf))
> The ability to retrieve a specific value when prompted with its associated key.

**Associative memory retrieval** (1 paper: [In-Context Learning as Conditioned Associative Memory Retrieval](https://raw.githubusercontent.com/mlresearch/v267/main/assets/wu25k/wu25k.pdf))
> The latent capacity of a model to retrieve stored patterns or knowledge by matching a query to the most relevant memory through similarity-based dynamics, akin to Hopfield network behavior.

## Relationships

### Associative recall ability →
- **MQAR** (measurement instrument): *measured_by*, 1 paper
  > The model’s recall capability is assessed using the MQAR Task (See Appendix D.7), as described in Arora et al. (2024a). (Figure 1)
  - [Rodimus*: Breaking the Accuracy-Efficiency Trade-Off with Efficient Attentions](https://proceedings.iclr.cc/paper_files/paper/2025/file/59c08508131c3a50991f42dae7f69e1c-Paper-Conference.pdf)
- **SWDE** (measurement instrument): *measured_by*, 1 paper
  > “Recall” represents the average performance across FDA, SWDE, and SQuAD. (Table 7)
  - [Scaling up the State Size of RNN LLMs for Long-Context Scenarios](https://aclanthology.org/2025.acl-long.564.pdf)
- **SQuAD v1.1** (measurement instrument): *measured_by*, 1 paper
  > “Recall” represents the average performance across FDA, SWDE, and SQuAD. (Table 7)
  - [Scaling up the State Size of RNN LLMs for Long-Context Scenarios](https://aclanthology.org/2025.acl-long.564.pdf)
