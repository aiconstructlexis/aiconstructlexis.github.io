# Text rewriting
**Type:** Behavioral indicator  
**Supporting papers:** 10  

## State of the Field

**Space of definitions.** Across papers, the prevailing usage treats text rewriting as an LLM taking an existing text and producing a modified version in response to instructions such as "polish," "rewrite," "refine," or "rephrase." Most definitions describe success as changing wording, phrasing, structure, or style while preserving the original meaning or remaining semantically relevant to the input. A smaller line of work adds stricter requirements, asking the model to change one aspect, such as topic, style, or factual content, while preserving others, and some watermark papers frame the same behavior as modifying text to remove a watermark while preserving meaning.

**Variants.** Papers study several variants of this behavior. Common variants include paraphrasing, rephrasing, synonym substitution, and other structural or stylistic edits that preserve meaning, while another recurring setup rewrites documents so that topic, style, or factual content changes selectively. Some work applies rewriting in a poetry setting, where a parent poem is turned into an "inspired, different poem" or, under the name "LMX-rewrite," into an offspring with different diversity characteristics; a smaller line of work treats rewriting as an attack on watermarked text.

**Space of elicitation and scores.** No measurement instrument is linked to it. When papers elicit the behavior directly, they commonly use instruction prompts, and Raidar: geneRative AI Detection viA Rewriting describes detecting AI-generated content by "prompting LLMs to rewrite text and calculating the editing distance of the output." Detection-oriented work also describes scoring by measuring the edits after rewriting, but the papers do not link any named instrument to this behavior.

**What it is taken as evidence of.** The papers do not link this behavior to any construct, so they do not explicitly present it as evidence of any named construct.

## Sources

**Text rewriting** (8 papers: [A Semantic Invariant Robust Watermark for Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/1a2131ebe25bd55e4fc734126ea583ed-Paper-Conference.pdf), [An Unforgeable Publicly Verifiable Watermark for Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/214d2cffc381938be6f7254d5382904f-Paper-Conference.pdf), [Dissecting learning and forgetting in language model finetuning](https://proceedings.iclr.cc/paper_files/paper/2024/file/c4de749a4bd8802f0b4033d09a7867db-Paper-Conference.pdf), [LMSYS-Chat-1M: A Large-Scale Real-World LLM Conversation Dataset](https://proceedings.iclr.cc/paper_files/paper/2024/file/5f9bfdfe3685e4ccdbc0e7fb29cccf2a-Paper-Conference.pdf), [Quality-Diversity through AI Feedback](https://proceedings.iclr.cc/paper_files/paper/2024/file/5b9bef4eae0f574cedbf9f4bf29d8ae7-Paper-Conference.pdf), [Raidar: geneRative AI Detection viA Rewriting](https://proceedings.iclr.cc/paper_files/paper/2024/file/1888b9df34b0d9eea6e009a1fdd55c4f-Paper-Conference.pdf), [Enhancing LLM Text Detection with Retrieved Contexts and Logits Distribution Consistency](https://aclanthology.org/2025.emnlp-main.503.pdf), [Learning to Rewrite: Generalized LLM-Generated Text Detection](https://aclanthology.org/2025.acl-long.322.pdf))
> The observable act of a language model modifying input text according to a prompt such as 'rewrite this for me' or 'polish this,' producing a revised version that may vary in wording, structure, or style.
