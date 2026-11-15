# Syntactic competence
**Type:** Construct  
**Supporting papers:** 21  
**Also known as:** Syntactic awareness, Syntactic understanding, Syntax learning, Syntactic ability, Formal competence, Syntactic generalization, Grammatical knowledge, Grammatical competence, Grammatical awareness, Grammatical abstraction, Grammatical accuracy, Syntactic knowledge  

## State of the Field

**Space of definitions.** Across papers, the prevailing usage treats syntactic competence as a latent ability, capacity, or knowledge through which a model represents and applies grammatical structure and rules. Most definitions center on processing or judging grammaticality, including agreement, word order, sentence hierarchy, and acceptable versus unacceptable contrasts, sometimes with reference to native-speaker intuitions; a smaller line instead defines it through internal representations that encode part-of-speech, dependency, or phrase-type information. Other minority framings narrow it to formal competence independent of meaning, to abstraction over schematic category constraints rather than specific word forms, or to producing syntactically correct outputs, including L2 English agreement phenomena and cases where semantic errors remain.

**Space of facets.** Papers use several labels for closely related framings, including syntactic awareness, syntactic understanding, syntactic ability, grammatical knowledge, grammatical competence, formal competence, grammatical awareness, and syntactic knowledge. The construct is broken into facets such as part-of-speech tags, dependency labels, phrase types, agreement, word order, sentence hierarchy, and specific constructions like passive voice, relative clauses, coordination, and subordination. Some definitions widen the scope to morphology and the syntax-semantics interface, while one paper explicitly contrasts formal constraints with semantic constraints, marking a form versus meaning distinction.

**Space of measurement.** Papers link syntactic competence to 2 measurement instruments and 2 behavioral indicators. Operationalization is mostly benchmark-based: BLiMP, the most common instrument, is described as a minimal-pair and targeted evaluation resource for syntactic generalization, probing syntax, the syntax-semantics interface, and morphology; SyntaxGym is another test suite for the same purpose. The linked behavioral indicators are grammatical acceptability judgment and event extraction; quoted passages also mention acceptability tasks, robustness checks for word order and subordination, probing grammatical knowledge or hidden representations, and one block-placement evaluation of syntactic reasoning. These operationalizations mostly align with definitions focused on grammatical contrasts and judgments, though some definitions instead target internal representations or syntactically well-formed output.

**Links.** Outside measurement, one paper claims a causal relationship from syntactic competence to event extraction, stating that syntax information has been found beneficial for the task. Papers also relate syntactic competence to grammatical acceptability judgment, describing grammaticality judgment and acceptability tasks as settings where models exploit grammatical information and where researchers assess robustness against grammatical errors or probe grammatical knowledge. A separate paper relates it to semantic understanding through a form-meaning asymmetry, where models learn formal constraints almost perfectly but fail semantic constraints. No correlational link is reported.

## Sources

**Syntactic awareness** (1 paper: [STARE at the Structure: Steering ICL Exemplar Selection with Structural Alignment](https://aclanthology.org/2025.emnlp-main.746.pdf))
> The degree to which a model's internal representations encode and utilize grammatical structure such as part-of-speech, dependency relations, and phrase types to inform processing decisions.

**Syntactic understanding** (1 paper: [Explainability and Interpretability of Multilingual Large Language Models: A Survey](https://aclanthology.org/2025.emnlp-main.1033.pdf))
> The latent ability to represent and process grammatical structures such as agreement, word order, and sentence hierarchy across languages.

**Syntactic ability** (1 paper: [Child-Directed Language Does Not Consistently Boost Syntax Learning in Language Models](https://aclanthology.org/2025.emnlp-main.999.pdf))
> The latent capacity of a language model to acquire and apply grammatical rules, particularly in distinguishing grammatical from ungrammatical sentence structures.

**Formal competence** (1 paper: [Unpacking Let Alone: Human-Scale Models Generalize to a Rare Construction in Form but not Meaning](https://aclanthology.org/2025.emnlp-main.1399.pdf))
> A model's ability to correctly identify and apply the syntactic and structural rules of a linguistic construction, independent of its meaning.

**Syntactic competence** (1 paper: [TurBLiMP: A Turkish Benchmark of Linguistic Minimal Pairs](https://aclanthology.org/2025.emnlp-main.834.pdf))
> The latent ability of a language model to correctly process and judge grammatical structures in accordance with native speaker intuitions.

**Grammatical knowledge** (1 paper: [QFrCoLA: a Quebec-French Corpus of Linguistic Acceptability Judgments](https://aclanthology.org/2025.emnlp-main.6.pdf))
> The model's internalized representation of a language's formal rules of grammar.

**Grammatical competence** (1 paper: [Layer-wise Minimal Pair Probing Reveals Contextual Grammatical-Conceptual Hierarchy in Speech Representations](https://aclanthology.org/2025.emnlp-main.1790.pdf))
> The latent capacity to encode and distinguish acceptable versus unacceptable grammatical contrasts across syntax, syntax-semantics interface, and morphology.

**Grammatical awareness** (1 paper: [BIRD: Bronze Inscription Restoration and Dating](https://aclanthology.org/2025.emnlp-main.1073.pdf))
> The inferred ability of a model to produce outputs that conform to the syntactic rules and categories of a language, even when making semantic errors.

**Grammatical abstraction** (1 paper: [BabyLM's First Constructions: Causal interventions provide a signal of learning](https://aclanthology.org/2025.emnlp-main.113.pdf))
> The capacity to generalize beyond specific word forms to abstract syntactic and semantic categories, such as recognizing that a construction requires a comparative adjective rather than a particular word.

**Grammatical accuracy** (1 paper: [Can LLMs Simulate L2-English Dialogue? An Information-Theoretic Analysis of L1-Dependent Biases](https://aclanthology.org/2025.acl-long.219.pdf))
> The latent ability to produce syntactically correct constructions in L2 English, particularly in agreement phenomena such as number, tense, and subject-verb consistency, despite L1 interference.

**Syntactic knowledge** (1 paper: [LinguaLens: Towards Interpreting Linguistic Mechanisms of Large Language Models via Sparse Auto-Encoder](https://aclanthology.org/2025.emnlp-main.1433.pdf))
> The latent representation of grammatical structure and sentence-level form, including constructions like passive voice, relative clauses, and coordination.

## Relationships

### Syntactic competence →
- **BLiMP** (measurement instrument): *measured_by*, 4 papers
  > We use the BLiMP (Warstadt et al., 2020) and SyntaxGym (SG, Gauthier et al., 2020) test suites to evaluate LMs for syntactic generalization.
  - [Sneaking Syntax into Transformer Language Models with Tree Regularization](https://aclanthology.org/2025.naacl-long.407.pdf)
  - [Child-Directed Language Does Not Consistently Boost Syntax Learning in Language Models](https://aclanthology.org/2025.emnlp-main.999.pdf)
  - [Layer-wise Minimal Pair Probing Reveals Contextual Grammatical-Conceptual Hierarchy in Speech Representations](https://aclanthology.org/2025.emnlp-main.1790.pdf)
  - [Mechanisms vs. Outcomes: Probing for Syntax Fails to Explain Performance on Targeted Syntactic Evaluations](https://aclanthology.org/2025.emnlp-main.1712.pdf)
- **Event extraction** (behavioral indicator): *causes*, 1 paper
  > Among EE literature, syntax information has been found beneficial for the task (Nguyen et al., 2016; Yan et al., 2019; Liu et al., 2019a; Lai et al., 2020). (Section 1)
  - [Soft Syntactic Reinforcement for Neural Event Extraction](https://aclanthology.org/2025.naacl-long.479.pdf)
- **SyntaxGym** (measurement instrument): *measured_by*, 1 paper
  > We use the BLiMP (Warstadt et al., 2020) and SyntaxGym (SG, Gauthier et al., 2020) test suites to evaluate LMs for syntactic generalization.
  - [Sneaking Syntax into Transformer Language Models with Tree Regularization](https://aclanthology.org/2025.naacl-long.407.pdf)

### Associated with
- **Grammatical acceptability judgment** (behavioral indicator), 2 papers
  > However, LLMs can exploit grammatical information, given an appropriate task—e.g. grammaticality judgment or IGT prediction—and more useful grammatical data in the form of our typological prompt, which achieves leading results on these linguistic tasks. (Section 6)
  - [Can LLMs Really Learn to Translate a Low-Resource Language from One Grammar Book?](https://proceedings.iclr.cc/paper_files/paper/2025/file/20f44da80080d76bbc35bca0027f14e6-Paper-Conference.pdf)
  - [QFrCoLA: a Quebec-French Corpus of Linguistic Acceptability Judgments](https://aclanthology.org/2025.emnlp-main.6.pdf)
- **Semantic understanding** (construct), 1 paper
  > Our experiments show strong evidence for a form–meaning asymmetry: Human-scale models learn LET-ALONE’s formal constraints almost perfectly (§4), but fail to learn any semantic constraints (§5).
  - [Unpacking Let Alone: Human-Scale Models Generalize to a Rare Construction in Form but not Meaning](https://aclanthology.org/2025.emnlp-main.1399.pdf)
