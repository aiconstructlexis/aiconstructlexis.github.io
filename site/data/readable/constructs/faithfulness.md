# Faithfulness
**Type:** Construct  
**Supporting papers:** 201  
**Also known as:** Factual consistency, Information accuracy, Factual correctness, Unfaithfulness, Causal concept faithfulness, Supportiveness  

## State of the Field

**Space of definitions.** Most papers describe faithfulness as source- or context-groundedness in generation: outputs should be supported by the input, source document, retrieved passages, graph, image, or instruction, often framed as entailment and as avoiding hallucinated, unsupported, contradictory, or unverified content. A smaller but recurring line of work uses the term for explanation faithfulness, where an explanation should reflect the model's actual reasoning or decision process, sometimes with reliability under perturbations. Only a few definitions shift further, treating faithfulness as alignment between stated intentions and behavior in negotiations, or as sensitivity to logical changes in a conclusion; one line also separates it from external factuality by reserving faithfulness for fidelity to the provided context.

**Space of facets.** When papers systematize the construct, the clearest facet split is internal versus external consistency: one negotiation study checks whether agents' own acceptable offers match later behavior and whether they can predict the other party's acceptable offers. Explanation-oriented work also separates alignment with input features from alignment with outputs, and a causal variant defines faithfulness through the match between concepts' causal effects and how often explanations mention them. Across papers, nearby labels include factual consistency, factual accuracy, factual correctness, and supportiveness, while one line explicitly contrasts faithfulness with factuality, using the former for alignment with provided input rather than external knowledge.

**Space of measurement.** Papers link faithfulness to 11 measurement instruments and 5 behavioral indicators. The most recurrent instruments are LLM-as-a-judge, FActScore, Human evaluation, Expert evaluation, and G-Eval, with 6 other instruments also linked; together these cover judge-based scoring, human annotation, and automatic benchmarks. Operationalizations mostly follow the groundedness framing, using document-summary entailment, sentence support checks with NLI, the proportion of faithful summary sentences, hallucination detection, or graph-validity rates such as valid nodes, valid edges, and fully valid graphs; a smaller explanation-oriented strand instead uses rationale removal or alteration, comprehensiveness and sufficiency, or causal-concept alignment, and the negotiation framing uses internal and external consistency prompts.

**Links.** Several papers report that faithfulness correlates with Hallucination, often phrased as improving faithfulness while reducing hallucination or as treating unfaithfulness as hallucinated, ungrounded content. One paper reports that faithfulness correlates with Positional bias, describing a U-shaped pattern in long-form summarization, and one paper claims a causal relationship from Stability to Faithfulness. Papers also relate faithfulness to Ambiguity and Context utilization, and discuss it alongside several other constructs and behaviors.

## Sources

**Faithfulness** (24 papers: [Achieving Human Parity in Content-Grounded Datasets Generation](https://proceedings.iclr.cc/paper_files/paper/2024/file/a774503daed55eb53c634847ae071ec7-Paper-Conference.pdf), [BooookScore: A systematic exploration of book-length summarization in the era of LLMs](https://proceedings.iclr.cc/paper_files/paper/2024/file/f7b77476d89d5fb58aeb77691d2f40f5-Paper-Conference.pdf), [Bootstrapping Variational Information Pursuit with Large Language and Vision Models for Interpretable Image Classification](https://proceedings.iclr.cc/paper_files/paper/2024/file/8e12ba543adc673da5b89c9311fcf72c-Paper-Conference.pdf), [Evaluating Language Model Agency Through Negotiations](https://proceedings.iclr.cc/paper_files/paper/2024/file/03876dc6875571c18b3b09a624c77e96-Paper-Conference.pdf), [Faithful Explanations of Black-box NLP Models Using LLM-generated Counterfactuals](https://proceedings.iclr.cc/paper_files/paper/2024/file/d5ee23c149efa1b7fb8d96a3be9908d9-Paper-Conference.pdf), [Faithful Vision-Language Interpretation via Concept Bottleneck Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/678cffc05549fdabda971127602084c6-Paper-Conference.pdf), [In-Context Pretraining: Language Modeling Beyond Document Boundaries](https://proceedings.iclr.cc/paper_files/paper/2024/file/a1fe2365abdb691332537990a6385909-Paper-Conference.pdf), [Model Merging by Uncertainty-Based Gradient Matching](https://proceedings.iclr.cc/paper_files/paper/2024/file/327b9b8d4e45c3f81568e11ffc505f77-Paper-Conference.pdf), [RAPPER: Reinforced Rationale-Prompted Paradigm for Natural Language Explanation in Visual Question Answering](https://proceedings.iclr.cc/paper_files/paper/2024/file/b364c8cbb3f229f40d5873e877391bd2-Paper-Conference.pdf), [RECOMP: Improving Retrieval-Augmented LMs with Context Compression and Selective Augmentation](https://proceedings.iclr.cc/paper_files/paper/2024/file/bda88ed2892f5e61c9a9bf215c566913-Paper-Conference.pdf), [Reasoning on Graphs: Faithful and Interpretable Large Language Model Reasoning](https://proceedings.iclr.cc/paper_files/paper/2024/file/3e2aeb66481dd63a32421bf032b70384-Paper-Conference.pdf), [Faithful, Unfaithful or Ambiguous? Multi-Agent Debate with Initial Stance for Summary Evaluation](https://aclanthology.org/2025.naacl-long.609.pdf), [AdaCAD: Adaptively Decoding to Balance Conflicts between Contextual and Parametric Knowledge](https://aclanthology.org/2025.naacl-long.581.pdf), [Learning to Summarize from LLM-generated Feedback](https://aclanthology.org/2025.naacl-long.38.pdf), [Not all Hallucinations are Good to Throw Away When it Comes to Legal Abstractive Summarization](https://aclanthology.org/2025.naacl-long.275.pdf), [SylloBio-NLI: Evaluating Large Language Models on Biomedical Syllogistic Reasoning](https://aclanthology.org/2025.naacl-long.371.pdf), [Main Predicate and Their Arguments as Explanation Signals For Intent Classification](https://aclanthology.org/2025.naacl-long.539.pdf), [MIRAGE-Bench: Automatic Multilingual Benchmark Arena for Retrieval-Augmented Generation Systems](https://aclanthology.org/2025.naacl-long.14.pdf), [MAMM-Refine: A Recipe for Improving Faithfulness in Generation with Multi-Agent Collaboration](https://aclanthology.org/2025.naacl-long.498.pdf), [MatViX: Multimodal Information Extraction from Visually Rich Articles](https://aclanthology.org/2025.naacl-long.185.pdf), [On Positional Bias of Faithfulness for Long-form Summarization](https://aclanthology.org/2025.naacl-long.442.pdf), [GraphNarrator: Generating Textual Explanations for Graph Neural Networks](https://aclanthology.org/2025.acl-long.2.pdf), [Is the Top Still Spinning? Evaluating Subjectivity in Narrative Understanding](https://aclanthology.org/2025.emnlp-main.10.pdf), [G-Retriever: Retrieval-Augmented Generation for Textual Graph Understanding and Question Answering](https://proceedings.neurips.cc/paper_files/paper/2024/file/efaf1c9726648c8ba363a5c927440529-Paper-Conference.pdf))
> The degree to which a model's internal reasoning and stated intentions align with its actual behavior, including both internal consistency (own acceptable offers) and external consistency (predictions of opponent's acceptable offers).

**Factual consistency** (3 papers: [On-Policy Distillation of Language Models: Learning from Self-Generated Mistakes](https://proceedings.iclr.cc/paper_files/paper/2024/file/5be69a584901a26c521c2b51e40a4c20-Paper-Conference.pdf), [Large Language Models for Automated Literature Review: An Evaluation of Reference Generation, Abstract Writing, and Review Composition](https://aclanthology.org/2025.emnlp-main.83.pdf), [SeafloorAI: A Large-scale Vision-Language Dataset for Seafloor Geological Survey](https://proceedings.neurips.cc/paper_files/paper/2024/file/274de7d60333c0848f42e18ae97f13e3-Paper-Datasets_and_Benchmarks_Track.pdf))
> The degree to which generated text, such as a summary, is factually supported by and does not contradict a given source document.

**Factual accuracy** (1 paper: [TracSum: A New Benchmark for Aspect-Based Summarization with Sentence-Level Traceability in Medical Domain](https://aclanthology.org/2025.emnlp-main.43.pdf))
> The degree to which generated summaries correctly reflect the source content without hallucinated or incorrect statements.

**Information accuracy** (1 paper: [From General Reward to Targeted Reward: Improving Open-ended Long-context Generation Models](https://aclanthology.org/2025.emnlp-main.260.pdf))
> The degree to which a long-form response supports correct answers to specific proxy questions about the target content.

**Factual correctness** (1 paper: [MuCAL: Contrastive Alignment for Preference-Driven KG-to-Text Generation](https://aclanthology.org/2025.emnlp-main.720.pdf))
> The degree to which a model's generated text faithfully represents the semantic information and facts contained within the source knowledge graph.

**Unfaithfulness** (1 paper: [MMLONGBENCH-DOC: Benchmarking Long-context Document Understanding with Visualizations](https://proceedings.neurips.cc/paper_files/paper/2024/file/ae0e43289bffea0c1fa34633fc608e92-Paper-Datasets_and_Benchmarks_Track.pdf))
> The tendency of a model to generate information that is not grounded in the provided source document.

**Causal concept faithfulness** (1 paper: [Walk the Talk? Measuring the Faithfulness of Large Language Model Explanations](https://proceedings.iclr.cc/paper_files/paper/2025/file/b5ec50eb177908f21f78ed0d76ed525c-Paper-Conference.pdf))
> The alignment between which high-level concepts causally affect a model's answer and which of those concepts the model's explanation says were influential.

**Supportiveness** (1 paper: [Benchmarking Complex Instruction-Following with Multiple Constraints Composition](https://proceedings.neurips.cc/paper_files/paper/2024/file/f8c24b08b96a08ec7a7a975feea7777e-Paper-Datasets_and_Benchmarks_Track.pdf))
> The degree to which a response remains faithful to the input instruction or source text.

## Relationships

### Faithfulness →
- **Hallucination** (behavioral indicator): *correlates*, 9 papers
  > Informative Context Improves Faithfulness and Reduces Hallucination.
  - [RAGChecker: A Fine-grained Framework for Diagnosing Retrieval-Augmented Generation](https://proceedings.neurips.cc/paper_files/paper/2024/file/27245589131d17368cccdfa990cbf16e-Paper-Datasets_and_Benchmarks_Track.pdf)
  - [MMLONGBENCH-DOC: Benchmarking Long-context Document Understanding with Visualizations](https://proceedings.neurips.cc/paper_files/paper/2024/file/ae0e43289bffea0c1fa34633fc608e92-Paper-Datasets_and_Benchmarks_Track.pdf)
  - [On-Policy Distillation of Language Models: Learning from Self-Generated Mistakes](https://proceedings.iclr.cc/paper_files/paper/2024/file/5be69a584901a26c521c2b51e40a4c20-Paper-Conference.pdf)
  - [SCOPE: A Self-supervised Framework for Improving Faithfulness in Conditional Text Generation](https://proceedings.iclr.cc/paper_files/paper/2025/file/05d6b5b6901fb57d2c287e1d3ce6d63c-Paper-Conference.pdf)
  - [No Free Lunch: Fundamental Limits of Learning Non-Hallucinating Generative Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/f2a11632520f4b7473d7838f074a7d25-Paper-Conference.pdf)
  - [MuHBoost: Multi-Label Boosting For Practical Longitudinal Human Behavior Modeling](https://proceedings.iclr.cc/paper_files/paper/2025/file/ca2963d1cfb25e93362e86fb427a9524-Paper-Conference.pdf)
  - [MAMM-Refine: A Recipe for Improving Faithfulness in Generation with Multi-Agent Collaboration](https://aclanthology.org/2025.naacl-long.498.pdf)
  - [AdaCAD: Adaptively Decoding to Balance Conflicts between Contextual and Parametric Knowledge](https://aclanthology.org/2025.naacl-long.581.pdf)
  - [SARA: Salience-Aware Reinforced Adaptive Decoding for Large Language Models in Abstractive Summarization](https://aclanthology.org/2025.acl-long.1236.pdf)
- **LLM-as-a-judge** (measurement instrument): *measured_by*, 4 papers
  > In this work, we evaluate primarily our models using recent NLI-related metrics (Zha et al., 2023; Dušek & Kasner, 2020), and LLM-as-a-judge, focusing on faithfulness (Chiang & Lee, 2023; Gilardi et al., 2023). (Section 2)
  - [SCOPE: A Self-supervised Framework for Improving Faithfulness in Conditional Text Generation](https://proceedings.iclr.cc/paper_files/paper/2025/file/05d6b5b6901fb57d2c287e1d3ce6d63c-Paper-Conference.pdf)
  - [SARA: Salience-Aware Reinforced Adaptive Decoding for Large Language Models in Abstractive Summarization](https://aclanthology.org/2025.acl-long.1236.pdf)
  - [Fann or Flop: A Multigenre, Multiera Benchmark for Arabic Poetry Understanding in LLMs](https://aclanthology.org/2025.emnlp-main.1023.pdf)
  - [Keep Security! Benchmarking Security Policy Preservation in Large Language Model Contexts Against Indirect Attacks in Question Answering](https://aclanthology.org/2025.emnlp-main.345.pdf)
- **Human evaluation** (measurement instrument): *measured_by*, 3 papers
  > To qualitatively examine whether CoK could output factually consistent reasoning chains, we also conducted a human study. (Section 5.3).
  - [Chain-of-Knowledge: Grounding Large Language Models via Dynamic Knowledge Adapting over Heterogeneous Sources](https://proceedings.iclr.cc/paper_files/paper/2024/file/285ba60a67a66d2efeeb7cb25c5067fe-Paper-Conference.pdf)
  - [RAPPER: Reinforced Rationale-Prompted Paradigm for Natural Language Explanation in Visual Question Answering](https://proceedings.iclr.cc/paper_files/paper/2024/file/b364c8cbb3f229f40d5873e877391bd2-Paper-Conference.pdf)
  - [ToolDial: Multi-turn Dialogue Generation Method for Tool-Augmented Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/afb27164624b641e8fbba961b2301acf-Paper-Conference.pdf)
- **FActScore** (measurement instrument): *measured_by*, 3 papers
  > Faithfulness: We use the FactScore suite and the fact evaluator for faithful biography generation [51] (Section 4.2).
  - [PaCE: Parsimonious Concept Engineering for Large Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/b3cca813dcd78fe75e4d4df2e6a0b1a7-Paper-Conference.pdf)
  - [LongReward: Improving Long-context Large Language Models with AI Feedback](https://aclanthology.org/2025.acl-long.187.pdf)
  - [Introducing Spotlight: A Novel Approach for Generating Captivating Key Information from Documents](https://aclanthology.org/2025.emnlp-main.1796.pdf)
- **HelpSteer** (measurement instrument): *measured_by*, 1 paper
  > "For unpaired datasets, we used PKU BeaverTails [Ji et al., 2023] with over 300K samples and HelpSteer [Wang et al., 2023] with around 35K samples. Here, for each prompt, there is only a single response with a score defined by some attributes (e.g., safety, faithfulness, helpfulness, etc.)."
  - [Distributional Preference Alignment of LLMs via Optimal Transport](https://proceedings.neurips.cc/paper_files/paper/2024/file/bce96750dcb64f3257ceabadf0b9c9bf-Paper-Conference.pdf)
- **Human preference evaluation** (measurement instrument): *measured_by*, 1 paper
  > Annotators are tasked with rating which of the two descriptions is more faithful to the table. (Section 5)
  - [SCOPE: A Self-supervised Framework for Improving Faithfulness in Conditional Text Generation](https://proceedings.iclr.cc/paper_files/paper/2025/file/05d6b5b6901fb57d2c287e1d3ce6d63c-Paper-Conference.pdf)
- **G-Eval** (measurement instrument): *measured_by*, 1 paper
  > We provide the TALM with dialogue history that includes the API call results and use G-Eval (Liu et al., 2023) to assess whether the responses reflect the API call output. (Section 4.1)
  - [ToolDial: Multi-turn Dialogue Generation Method for Tool-Augmented Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/afb27164624b641e8fbba961b2301acf-Paper-Conference.pdf)
- **TofuEval** (measurement instrument): *measured_by*, 1 paper
  > Using TofuEval (Tang et al., 2024c), a dataset with human-annotated sentence-level faithfulness judgments and critiques, we design intrinsic evaluation tasks for each of the three subtasks, DETECT, CRITIQUE, and REFINE (Section 1)
  - [MAMM-Refine: A Recipe for Improving Faithfulness in Generation with Multi-Agent Collaboration](https://aclanthology.org/2025.naacl-long.498.pdf)
- **Positional bias** (construct): *correlates*, 1 paper
  > Analyzing LLM-generated summaries across six datasets, we find a "U-shaped" trend in faithfulness, where LLMs faithfully summarize the beginning and end of documents but neglect middle content.
  - [On Positional Bias of Faithfulness for Long-form Summarization](https://aclanthology.org/2025.naacl-long.442.pdf)
- **Expert evaluation** (measurement instrument): *measured_by*, 1 paper
  > Automatic evaluation of retrieval augmented generation (RAG) systems relies on fine-grained dimensions like faithfulness and relevance, as judged by expert human annotators.
  - [MEMERAG: A Multilingual End-to-End Meta-Evaluation Benchmark for Retrieval Augmented Generation](https://aclanthology.org/2025.acl-long.1101.pdf)
- **MMHal-Bench** (measurement instrument): *measured_by*, 1 paper
  > MMHal-Bench (Sun et al., 2023), which gauges the faithfulness of VLMs by identifying hallucinations in their outputs. (Section 5.2)
  - [The Devil Is in the Details: Tackling Unimodal Spurious Correlations for Generalizable Multimodal Reward Models](https://raw.githubusercontent.com/mlresearch/v267/main/assets/li25cw/li25cw.pdf)
- **TRUE** (measurement instrument): *measured_by*, 1 paper
  > for the Abstract Writing task, we employ TRUE (Honovich et al., 2022), along with GPT-4o as NLI models for evaluating factual consistency in context
  - [Large Language Models for Automated Literature Review: An Evaluation of Reference Generation, Abstract Writing, and Review Composition](https://aclanthology.org/2025.emnlp-main.83.pdf)
- **RAGAS** (measurement instrument): *measured_by*, 1 paper
  > Frameworks such as RAGAS (Shahul et al., 2023) and RAG-Checker (Ru et al., 2024) have demonstrated that LLMs can provide scalable and automated assessments of metrics such as context relevance and faithfulness
  - [RAG-Zeval: Enhancing RAG Responses Evaluator through End-to-End Reasoning and Ranking-Based Reinforcement Learning](https://aclanthology.org/2025.emnlp-main.1267.pdf)

### → Faithfulness
- **Stability** (construct): *causes*, 1 paper
  > Therefore, stability plays a pivotal role in ensuring explanation faithfulness.
  - [Faithful Vision-Language Interpretation via Concept Bottleneck Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/678cffc05549fdabda971127602084c6-Paper-Conference.pdf)

### Associated with
- **Object hallucination** (behavioral indicator), 1 paper
  > Such phenomenon challenges the faithfulness and reliability of LVLMs in practical use, impeding their deployments to real-world applications [14]. (Introduction)
  - [Mitigating Object Hallucination via Concentric Causal Attention](https://proceedings.neurips.cc/paper_files/paper/2024/file/a76ed4a8ef522c823d73925e7fff16d4-Paper-Conference.pdf)
- **Context utilization** (construct), 1 paper
  > When tuning the generator, the trilemma of context utilization, noise sensitivity, and faithfulness makes it difficult to improve all aspects simultaneously.
  - [RAGChecker: A Fine-grained Framework for Diagnosing Retrieval-Augmented Generation](https://proceedings.neurips.cc/paper_files/paper/2024/file/27245589131d17368cccdfa990cbf16e-Paper-Datasets_and_Benchmarks_Track.pdf)
- **Factuality** (construct), 1 paper
  > Factuality refers to whether the model’s generated information aligns with external, real-world knowledge and is typically evaluated against a reference dataset or established knowledge. Faithfulness, on the other hand, evaluates how accurately the generated content reflects the information provided in the input context. (Section 1)
  - [SCOPE: A Self-supervised Framework for Improving Faithfulness in Conditional Text Generation](https://proceedings.iclr.cc/paper_files/paper/2025/file/05d6b5b6901fb57d2c287e1d3ce6d63c-Paper-Conference.pdf)
- **Data-to-text generation** (behavioral indicator), 1 paper
  > Faithfulness is essential for both tasks to ensure the generated text accurately reflects the input data. (Section 1)
  - [SCOPE: A Self-supervised Framework for Improving Faithfulness in Conditional Text Generation](https://proceedings.iclr.cc/paper_files/paper/2025/file/05d6b5b6901fb57d2c287e1d3ce6d63c-Paper-Conference.pdf)
- **Generation diversity** (construct), 1 paper
  > We emphasize the importance of balancing faithfulness and diversity during post-training stages, providing a theoretical foundation for existing methodologies. (Section 5)
  - [Towards a Theoretical Understanding of Synthetic Data in LLM Post-Training: A Reverse-Bottleneck Perspective](https://proceedings.iclr.cc/paper_files/paper/2025/file/1e0bfe8bbaa0e70809f0a8ccd9c2ff3e-Paper-Conference.pdf)
- **Ambiguity** (construct), 1 paper
  > an ambiguous summary can be correctly interpreted in multiple ways given the source document, leading to different faithfulness judgments depending on the underlying assumptions.
  - [Faithful, Unfaithful or Ambiguous? Multi-Agent Debate with Initial Stance for Summary Evaluation](https://aclanthology.org/2025.naacl-long.609.pdf)
- **Fact checking** (behavioral indicator), 1 paper
  > We consider the task of fact-checking claims against grounding documents, where the goal is to assess factual consistency based on provided textual evidence (Section 1).
  - [GraphCheck: Breaking Long-Term Text Barriers with Extracted Knowledge Graph-Powered Fact-Checking](https://aclanthology.org/2025.acl-long.729.pdf)
- **Plausibility** (construct), 1 paper
  > In terms of interpretability, this paper focuses on the trade-off between plausibility and faithfulness. (Section 4.3)
  - [Judge and Improve: Towards a Better Reasoning of Knowledge Graphs with Large Language Models](https://aclanthology.org/2025.emnlp-main.269.pdf)
- **Citation quality** (construct), 1 paper
  > Using passage-level relevance judgments for all queries (or qrels) information available in MIRACL, we evaluate whether the system’s response cites the relevant passages, crucial for measuring faithfulness.
  - [MIRAGE-Bench: Automatic Multilingual Benchmark Arena for Retrieval-Augmented Generation Systems](https://aclanthology.org/2025.naacl-long.14.pdf)
- **Interpretability and explainability** (construct), 1 paper
  > We evaluate the explainability of all the models using plausibility and faithfulness metrics (DeYoung et al., 2019). (Section 6.1)
  - [Main Predicate and Their Arguments as Explanation Signals For Intent Classification](https://aclanthology.org/2025.naacl-long.539.pdf)
- **Reasoning** (construct), 1 paper
  > Faithfulness serves as a metric for evaluating the degree to which the model’s provided explanation aligns with its actual reasoning. (Section 6.1)
  - [Main Predicate and Their Arguments as Explanation Signals For Intent Classification](https://aclanthology.org/2025.naacl-long.539.pdf)
- **Explanation generation** (behavioral indicator), 1 paper
  > We evaluate the quality of our natural language explanations using two widely recognized metrics in explainable AI: faithfulness and simulatability.
  - [Explaining Differences Between Model Pairs in Natural Language through Sample Learning](https://aclanthology.org/2025.emnlp-main.1462.pdf)
- **Comprehensiveness** (construct), 1 paper
  > To assess the faithfulness of the aforementioned methods, we adopt two complementary criteria: comprehensiveness and sufficiency (DeYoung et al., 2020). (Section 4.2)
  - [NormXLogit: The Head-on-Top Never Lies](https://aclanthology.org/2025.emnlp-main.1769.pdf)
