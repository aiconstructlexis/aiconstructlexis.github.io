# Lexical diversity
**Type:** Construct  
**Supporting papers:** 8  

## State of the Field

**Space of definitions.** Across the surveyed work, the prevailing usage treats lexical diversity as the variety or richness of vocabulary, words, phrases, or n-grams in generated text or in collections of texts. Most definitions locate it in observable outputs, such as text produced across many examples, while one paper shifts the emphasis to the model's capacity to generate varied vocabulary and avoid repetitive n-gram patterns. The main variation is therefore whether it is framed as a property of texts and datasets or as a capacity of the model that produces them, with one paper also narrowing the description to lexical types with shared syntactic properties.

**Space of facets.** These papers do not present a detailed subtype taxonomy for lexical diversity. Instead, they vary the unit used to describe it, ranging from vocabulary, words and phrases, and n-grams to, in one paper, lexical types. Some authors also distinguish it from other forms of diversity by discussing it alongside diversity in the key points expressed, and one paper places it alongside order diversity in a generation setup.

**Space of measurement.** No measurement instrument is linked to lexical diversity, and no behavioral indicator is linked to it. In practice, papers operationalize it through analyses of output text: one calls the fraction of unique n-grams a straightforward measure, another reports computing vocd-D, and others compare reported diversity scores or assess whether a method generates 'lexically diverse continuations.' These operationalizations are applied comparatively, with one study reporting lower lexical diversity in essays written with InstructGPT and others reporting higher lexical diversity for synthetic or combined LLM-generated text than for human-authored text.

## Sources

**Lexical diversity** (5 papers: [ARGS: Alignment as Reward-Guided Search](https://proceedings.iclr.cc/paper_files/paper/2024/file/4d1344317478ad99ff5f4e414aeab689-Paper-Conference.pdf), [Achieving Human Parity in Content-Grounded Datasets Generation](https://proceedings.iclr.cc/paper_files/paper/2024/file/a774503daed55eb53c634847ae071ec7-Paper-Conference.pdf), [Does Writing with Language Models Reduce Content Diversity?](https://proceedings.iclr.cc/paper_files/paper/2024/file/02dec8877fb7c6aa9a79f81661baca7c-Paper-Conference.pdf), [Comparing LLM-generated and human-authored news text using formal syntactic theory](https://aclanthology.org/2025.acl-long.443.pdf), [Your Language Model Can Secretly Write Like Humans: Contrastive Paraphrase Attacks on LLM-Generated Text Detectors](https://aclanthology.org/2025.emnlp-main.433.pdf))
> The variety of words and phrases (n-grams) used within a collection of texts.
