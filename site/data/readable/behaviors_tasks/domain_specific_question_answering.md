# Domain-specific question answering
**Type:** Behavioral indicator  
**Supporting papers:** 3  

## State of the Field

**Space of definitions.** Across the definitions, the prevailing usage treats this behavior as answering natural language questions that depend on specialized domain knowledge, with success framed as producing accurate answers. One formulation centers on questions "derived from client’s tabular datasets" in domains such as finance or healthcare, while another frames it as answering facts contained in a specialized document or newly learned domain. A narrower task setup further constrains the response format to a single word, either "Yes" or "No" for binary cases or an uppercase letter for multiclass cases, and illustrates the task with questions such as "will my loan be approved?"

**Variants.** Papers study it in several settings: over structured tabular data, over facts in a specialized document, and over a newly learned domain. The named domains include finance and healthcare, and one recurring variant casts the questions as binary or multiclass decisions rather than open-ended responses.

**Space of elicitation and scores.** No measurement instrument is linked to it. In the task descriptions themselves, papers operationalize it through answer accuracy on domain-specific questions, including a setup that requires single-word labels and another that uses "60 domain-specific questions" to assess the knowledge contained within a document.

**What it is taken as evidence of.** No construct is linked to it in the papers, so the papers do not state what construct it serves as evidence of.

## Sources

**Domain-specific question answering** (2 papers: [Model-based Large Language Model Customization as Service](https://aclanthology.org/2025.emnlp-main.248.pdf), [Param$\Delta$ for Direct Mixing: Post-Train Large Language Model At Zero Cost](https://proceedings.iclr.cc/paper_files/paper/2025/file/78bca5cc621a0846cb1f8265e1927a2a-Paper-Conference.pdf))
> Producing accurate answers to natural language questions that require knowledge of a specific domain, such as finance or healthcare, based on structured tabular data.
