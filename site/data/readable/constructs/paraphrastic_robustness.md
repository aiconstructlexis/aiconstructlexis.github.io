# Paraphrastic robustness
**Type:** Construct  
**Supporting papers:** 4  
**Also known as:** Robustness to paraphrases  

## State of the Field

**Space of definitions.** Across the definitions, the prevailing usage treats paraphrastic robustness as consistency under linguistic variation that leaves meaning or intention unchanged. Most formulations describe stable performance when a question, prompt, or instruction is rephrased, and embodied-task papers extend this to indirect object references so long as the underlying intention does not change. A smaller difference is whether authors present it as a latent ability of the model or directly as observed stability in performance or behavior.

**Space of facets.** Where papers locate the construct, the clearest framing places paraphrastic robustness under generalization: one paper defines it as a specific form of generalization in which performance remains stable under semantically equivalent rewordings of task instructions. Another recurring distinction is between stability under linguistic variation and behavior generalization, which one paper mentions alongside paraphrastic robustness as a separate evaluation target. Beyond that, the main organizing facet is the type of language change, paraphrases, rephrasings, and indirect object references, with task meaning held fixed.

**Space of measurement.** No measurement instrument or behavioral indicator is linked to this construct. Papers nonetheless operationalize it directly in their evaluation descriptions, for example as the percentage of datapoints where the model gets all paraphrases of a question correct, or by checking whether an agent produces the same, or the same optimal, behavior under a linguistic variation of an instruction. Another paper mentions unseen instruction datasets that measure paraphrastic robustness together with behavior generalization.

**Links.** One paper claims a causal relationship from Natural language understanding to Paraphrastic robustness, saying that this is expected because LLMs are known for their language understanding capabilities. No correlational or merely related links are recorded.

## Sources

**Robustness to paraphrases** (1 paper: [The Truth is in There: Improving Reasoning in Language Models with Layer-Selective Rank Reduction](https://proceedings.iclr.cc/paper_files/paper/2024/file/4c2092ec0b1370cce3fb5965ab255fae-Paper-Conference.pdf))
> The stability of a model's performance when a question or prompt is rephrased without changing its semantic meaning.

**Paraphrastic robustness** (2 papers: [Large Language Models as Generalizable Policies for Embodied Tasks](https://proceedings.iclr.cc/paper_files/paper/2024/file/8f9461d11e8ce9b0b28b21bfc645d74e-Paper-Conference.pdf), [Grounding Multimodal Large Language Models in Actions](https://proceedings.neurips.cc/paper_files/paper/2024/file/2406694fd7bc7e7bf257446a14f9ea63-Paper-Conference.pdf))
> The latent ability of a model to produce consistent, correct behavior despite linguistic variations in task instructions, such as rephrasing or indirect object references, when the underlying intention remains unchanged.

## Relationships

### → Paraphrastic robustness
- **Natural language understanding** (construct): *causes*, 1 paper
  > Althought this is expected for paraphrastic robustnes as LLMs are known for their language understanding capabilities, it is somewhat surprising to see that the LLM helps even for novel behaviors...
  - [Large Language Models as Generalizable Policies for Embodied Tasks](https://proceedings.iclr.cc/paper_files/paper/2024/file/8f9461d11e8ce9b0b28b21bfc645d74e-Paper-Conference.pdf)
