# Groundedness
**Type:** Construct  
**Supporting papers:** 12  
**Also known as:** Argument groundedness, Factual reliability  

## State of the Field

**Space of definitions.** Most papers treat groundedness as a property of responses or outputs that stay within provided or retrieved evidence, rather than drawing on the model's internal parametric knowledge, and that can be verified against those sources. A stricter formulation says a response is grounded only if it answers using only the attached documents and its claims can be inferred from inline citations. Smaller variations narrow the construct to arguments, defined by factual support and consistency with retrieved evidence, or broaden the evidence base to input contracts and external legal sources, while one paper shifts the locus from the output to the retrieval and reasoning process under the label factual reliability.

**Space of facets.** Papers do not offer a detailed subtype taxonomy, but they do separate groundedness by locus. The prevailing usage is response or output groundedness, while smaller lines of work discuss argument groundedness and a closely related process-oriented framing, factual reliability. Across these uses, authors repeatedly contrast grounded content with hallucination, contradiction, unsupported claims, and reliance on parametric knowledge, and some papers describe better groundedness as greater faithfulness to the retrieved context.

**Space of measurement.** No measurement instrument is linked to groundedness, and it is linked to two behavioral indicators, Chain of thought and Hallucination. Even so, papers operationalize the construct concretely: one requires answers to use only attached documents and be inferable from inline citations, another reports a human study of grounded justifications, and argument-focused work discusses groundedness scores together with checks for hallucinated content by LLM judges. These operationalizations mostly follow the dominant definitions by testing whether outputs remain supported by provided or retrieved evidence.

**Links.** The reported links are narrow and all involve behavioral indicators. One paper reports that groundedness is related to Hallucination, asking whether groundedness predictions detect argument hallucinations. Another paper claims a causal relationship from Chain of thought to Groundedness, describing a chain-of-knowledge in which free-form thoughts are replaced with document-grounded knowledge triples to ensure factual reliability.

## Sources

**Groundedness** (3 papers: [Measuring and Enhancing Trustworthiness of LLMs in RAG through Grounded Attributions and Learning to Refuse](https://proceedings.iclr.cc/paper_files/paper/2025/file/4c88827decab6c046b881a2c3a99c76f-Paper-Conference.pdf), [CoCoLex: Confidence-guided Copy-based Decoding for Grounded Legal Text Generation](https://aclanthology.org/2025.acl-long.931.pdf), [PAKTON: A Multi-Agent Framework for Question Answering in Long Legal Agreements](https://aclanthology.org/2025.emnlp-main.403.pdf))
> The extent to which an LLM's response is derived solely from the information within provided documents rather than its internal parametric knowledge.

**Argument groundedness** (1 paper: [ConQRet: A New Benchmark for Fine-Grained Automatic Evaluation of Retrieval Augmented Computational Argumentation](https://aclanthology.org/2025.naacl-long.293.pdf))
> The extent to which a generated argument is factually supported by and consistent with the retrieved evidence, minimizing hallucination or contradiction.

**Factual reliability** (1 paper: [KiRAG: Knowledge-Driven Iterative Retriever for Enhancing Retrieval-Augmented Generation](https://aclanthology.org/2025.acl-long.929.pdf))
> The degree to which the retrieval and reasoning process avoids hallucinated or factually inaccurate content by grounding in document-derived knowledge.

## Relationships

### → Groundedness
- **Chain of thought** (behavioral indicator): *causes*, 1 paper
  > ...we instruct the LLM to generate a chain-of-knowledge (CoK) (Wang et al., 2024a), where free-form thoughts are replaced with document-grounded knowledge triples to ensure factual reliability. (Section 3.2)
  - [KiRAG: Knowledge-Driven Iterative Retriever for Enhancing Retrieval-Augmented Generation](https://aclanthology.org/2025.acl-long.929.pdf)

### Associated with
- **Hallucination** (behavioral indicator), 1 paper
  > Do groundedness predictions detect argument hallucinations? (Section 6.3)
  - [ConQRet: A New Benchmark for Fine-Grained Automatic Evaluation of Retrieval Augmented Computational Argumentation](https://aclanthology.org/2025.naacl-long.293.pdf)
