# Memorization
**Type:** Construct  
**Supporting papers:** 150  
**Also known as:** Memorization capacity, Memorisation, Inadvertent memorization, Memorization propensity, Factual memory, Model capacity, Recall, Statistical recall  

## State of the Field

**Space of definitions.** Across papers, the prevailing usage treats memorization as storage of specific training data that can later be reproduced, often verbatim or near-verbatim, including private, copyrighted, benchmark, or rare content. This is usually framed either as a latent model property or tendency to retain examples in parameters, or as an output behavior that permits exact or near-exact replicas of seen data (To the Cutoff... and Beyond? A Longitudinal Perspective on LLM Data Contamination). Smaller lines of work broaden the term to compressed context retention and long-context working memory, to factual recall of isolated facts, or to answer production from recall rather than reasoning, with one paper labeling the latter blind memorization (LLMs Are Not Intelligent Thinkers: Introducing Mathematical Topic Tree Benchmark for Comprehensive Evaluation of LLMs). A separate capacity-oriented framing defines memorization capacity as how much arbitrary input-output or factual association information a model can store in its trainable parameters.

**Space of facets.** Papers partition the area into variants such as memorization capacity, inadvertent memorization, memorization propensity, factual memory, and statistical recall. These variants mark different scopes: some focus on finite storage capacity and association loading, some on stronger encoding of private, irrelevant, rare, or outlier-like samples, and some on performance that relies on statistical correlations instead of systematic reasoning. The naming is therefore not uniform: memorization can denote latent storage in parameters, successful reconstruction or extraction at inference time, or broader recall-like behavior, and one paper explicitly treats it as a multifaceted phenomenon shaped by factors tied to the sample, model, and corpus.

**Space of measurement.** Operationally, papers link memorization to 10 measurement instruments and 10 behavioral indicators, and the linked instruments are benchmark or dataset-based probes. AUXDATASET operationalizes it as exact 50-token overlap with a reference set, BookMIA contrasts unseen 2023 book excerpts with passages treated as memorized, HH-RLHF and LIMA are used to study memorization in RLHF settings, and LexEval includes memorization as one dimension of a legal benchmark. The remaining five instruments cover factual QA, cross-lingual recall, and factual-knowledge benchmark settings, while the behavioral indicators emphasize concrete recoverable behavior, such as exact or near-exact reproduction and successful retrieval of stored facts, so measurement often targets extractable outputs more narrowly than definitions that frame memorization as context retention or recall rather than reasoning.

**Links.** Papers link memorization to 15 constructs. The most recurrent link concerns Generalization: several papers claim a causal relationship from memorization to poor or limited generalization, while others describe the pair as related or report a correlation, and one paper separately claims a causal relationship from memorization to Overfitting. Several papers also claim causal relationships from memorization to Training data regurgitation and Privacy leakage, with closely related claims about extraction and verbatim reproduction, and many papers place memorization in relation to Reasoning by contrasting recall or pattern matching with reasoning-oriented performance. Other isolated causal claims point to additional downstream behaviors and task outcomes.

## Sources

**Memorization** (25 papers: [AutomaTikZ: Text-Guided Synthesis of Scientific Vector Graphics with TikZ](https://proceedings.iclr.cc/paper_files/paper/2024/file/f7641940c7dd9e5de58c20e39586eb64-Paper-Conference.pdf), [Can Sensitive Information Be Deleted From LLMs? Objectives for Defending Against Extraction Attacks](https://proceedings.iclr.cc/paper_files/paper/2024/file/c652e5f62fd1f5acbbf0d6413a1113e7-Paper-Conference.pdf), [Detecting Pretraining Data from Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/e32ad85fa27be4a9868d55703f01323e-Paper-Conference.pdf), [DyVal: Dynamic Evaluation of Large Language Models for Reasoning Tasks](https://proceedings.iclr.cc/paper_files/paper/2024/file/4ea4a1ea4d9ff273688c8e92bd087112-Paper-Conference.pdf), [In-context Autoencoder for Context Compression in a Large Language Model](https://proceedings.iclr.cc/paper_files/paper/2024/file/0b276510ec2d3f6613a8b60c41ff0438-Paper-Conference.pdf), [Llemma: An Open Language Model for Mathematics](https://proceedings.iclr.cc/paper_files/paper/2024/file/b225f5c7cd13615e9558c3931fa4e66f-Paper-Conference.pdf), [OpenWebMath: An Open Dataset of High-Quality Mathematical Web Text](https://proceedings.iclr.cc/paper_files/paper/2024/file/5949a8750a110ce1f0631b1776c500a2-Paper-Conference.pdf), [Proving Test Set Contamination in Black-Box Language Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/46e624c244cff669223d488defd4e835-Paper-Conference.pdf), [Scaling Laws for Associative Memories](https://proceedings.iclr.cc/paper_files/paper/2024/file/28f734334f9f325b515933e70b6b412c-Paper-Conference.pdf), [Teach LLMs to Phish: Stealing Private Information from Language Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/f206871468dc89cb20fefbc75f2de861-Paper-Conference.pdf), [To the Cutoff... and Beyond? A Longitudinal Perspective on LLM Data Contamination](https://proceedings.iclr.cc/paper_files/paper/2024/file/2d04d97593c8c33d415337f408ed0e1b-Paper-Conference.pdf), [Limits of Transformer Language Models on Learning to Compose Algorithms](https://proceedings.neurips.cc/paper_files/paper/2024/file/0e797d5139ad94fc2dc2080c09119f29-Paper-Conference.pdf), [Copyright-Protected Language Generation via Adaptive Model Fusion](https://proceedings.iclr.cc/paper_files/paper/2025/file/01953220e4becc6ac1078c24c1f8d3a7-Paper-Conference.pdf), [Measuring memorization in language models via probabilistic extraction](https://aclanthology.org/2025.naacl-long.469.pdf), [UNDIAL: Self-Distillation with Adjusted Logits for Robust Unlearning in Large Language Models](https://aclanthology.org/2025.naacl-long.444.pdf), [Verifiable by Design: Aligning Language Models to Quote from Pre-Training Data](https://aclanthology.org/2025.naacl-long.191.pdf), [ALPACA AGAINST VICUNA: Using LLMs to Uncover Memorization of LLMs](https://aclanthology.org/2025.naacl-long.421.pdf), [TurtleBench: A Visual Programming Benchmark in Turtle Geometry](https://aclanthology.org/2025.naacl-long.607.pdf), [HMT: Hierarchical Memory Transformer for Efficient Long Context Language Processing](https://aclanthology.org/2025.naacl-long.410.pdf), [The Stochastic Parrot on LLM's Shoulder: A Summative Assessment of Physical Concept Understanding](https://aclanthology.org/2025.naacl-long.569.pdf), [LLMs Are Not Intelligent Thinkers: Introducing Mathematical Topic Tree Benchmark for Comprehensive Evaluation of LLMs](https://aclanthology.org/2025.naacl-long.161.pdf), [PoisonedParrot: Subtle Data Poisoning Attacks to Elicit Copyright-Infringing Content from Large Language Models](https://aclanthology.org/2025.naacl-long.415.pdf), [Information-Guided Identification of Training Data Imprint in (Proprietary) Large Language Models](https://aclanthology.org/2025.naacl-long.99.pdf), [UnSeenTimeQA: Time-Sensitive Question-Answering Beyond LLMs' Memorization](https://aclanthology.org/2025.acl-long.94.pdf), [LingGym: How Far Are LLMs from Thinking Like Field Linguists?](https://aclanthology.org/2025.emnlp-main.69.pdf))
> The latent ability of an LLM to encode and retain information from a context in compressed form, analogous to human memory encoding, allowing for reconstruction or task performance based on partial or compressed representations.

**Memorization capacity** (3 papers: [Algorithmic Capabilities of Random Transformers](https://proceedings.neurips.cc/paper_files/paper/2024/file/bccdd196d798a51a4961989984a9ed4a-Paper-Conference.pdf), [Understanding Factual Recall in Transformers via Associative Memories](https://proceedings.iclr.cc/paper_files/paper/2025/file/0bf9f909c24c8879d1b7f86fa50a9e49-Paper-Conference.pdf), [How to inject knowledge efficiently? Knowledge Infusion Scaling Law for Pre-training Large Language Models](https://aclanthology.org/2025.emnlp-main.1331.pdf))
> The extent to which a model can store arbitrary input-output associations in its trainable parameters.

**Memorisation** (2 papers: [Are We Done with MMLU?](https://aclanthology.org/2025.naacl-long.262.pdf), [Less for More: Enhanced Feedback-aligned Mixed LLMs for Molecule Caption Generation and Fine-Grained NLI Evaluation](https://aclanthology.org/2025.acl-long.144.pdf))
> The extent to which a model has stored and can recall specific instances from its training data, rather than generating novel responses based on generalized knowledge.

**Inadvertent memorization** (1 paper: [Watch Out Your Album! On the Inadvertent Privacy Memorization in Multi-Modal Large Language Models](https://raw.githubusercontent.com/mlresearch/v267/main/assets/ju25a/ju25a.pdf))
> The latent tendency of MLLMs to encode private, task-irrelevant information into their parameters due to spurious correlations formed during mini-batch training, even when such information provides no benefit for the downstream task.

**Memorization propensity** (1 paper: [Underestimated Privacy Risks for Minority Populations in Large Language Model Unlearning](https://raw.githubusercontent.com/mlresearch/v267/main/assets/wei25d/wei25d.pdf))
> The latent tendency of a model to strongly encode and retain specific training data points, especially those that are rare or outlier-like, making them harder to unlearn.

**Factual memory** (1 paper: [From RAG to Memory: Non-Parametric Continual Learning for Large Language Models](https://raw.githubusercontent.com/mlresearch/v267/main/assets/gutierrez25a/gutierrez25a.pdf))
> The latent ability of a model to accurately recall and retrieve specific, isolated pieces of knowledge, such as entity attributes or simple facts.

**Model capacity** (3 papers: [Increasing Model Capacity for Free: A Simple Strategy for Parameter Efficient Fine-tuning](https://proceedings.iclr.cc/paper_files/paper/2024/file/ce3fd6b9dfe458dc258a8164a5e95bd2-Paper-Conference.pdf), [Scaling Laws for Associative Memories](https://proceedings.iclr.cc/paper_files/paper/2024/file/28f734334f9f325b515933e70b6b412c-Paper-Conference.pdf), [Parameters vs FLOPs: Scaling Laws for Optimal Sparsity for Mixture-of-Experts Language Models](https://raw.githubusercontent.com/mlresearch/v267/main/assets/abnar25a/abnar25a.pdf))
> The finite ability of a model, parameterized by the embedding dimension 'd', to store associations without performance degradation from interference.

**Recall** (1 paper: [Reasoning Elicitation in Language Models via Counterfactual Feedback](https://proceedings.iclr.cc/paper_files/paper/2025/file/bf145010b30dc5f14fa87dc152074e4d-Paper-Conference.pdf))
> The latent reliance on statistical correlations or training data retrieval rather than genuine reasoning processes.

**Statistical recall** (1 paper: [RE-IMAGINE: Symbolic Benchmark Synthesis for Reasoning Evaluation](https://raw.githubusercontent.com/mlresearch/v267/main/assets/xu25n/xu25n.pdf))
> The degree to which a model's performance relies on recognizing and reproducing patterns from its training data rather than engaging in systematic reasoning.

## Relationships

### Memorization →
- **Generalization** (construct): *causes*, 12 papers
  > This raises concerns about whether LLMs are merely memorizing and overfitting these benchmarks instead of learning how to solve the tasks [112], which may lead to poor generalization[67, 13, 9]. (Section 1)
  - [DARG: Dynamic Evaluation of Large Language Models via Adaptive Reasoning Graph](https://proceedings.neurips.cc/paper_files/paper/2024/file/f5198bc255e1d5f959edd6d1d1a86fab-Paper-Conference.pdf)
  - [Position: General Intelligence Requires Reward-based Pretraining](https://raw.githubusercontent.com/mlresearch/v267/main/assets/han25n/han25n.pdf)
  - [Grokking in the Wild: Data Augmentation for Real-World Multi-Hop Reasoning with Transformers](https://raw.githubusercontent.com/mlresearch/v267/main/assets/abramov25a/abramov25a.pdf)
  - [Memorization Sinks: Isolating Memorization during LLM Training](https://raw.githubusercontent.com/mlresearch/v267/main/assets/ghosal25a/ghosal25a.pdf)
  - [DyVal: Dynamic Evaluation of Large Language Models for Reasoning Tasks](https://proceedings.iclr.cc/paper_files/paper/2024/file/4ea4a1ea4d9ff273688c8e92bd087112-Paper-Conference.pdf)
  - [Attributing Culture-Conditioned Generations to Pretraining Corpora](https://proceedings.iclr.cc/paper_files/paper/2025/file/c4546b4f9e1a44ed15c253dd43307dd5-Paper-Conference.pdf)
  - [Decision Tree Induction Through LLMs via Semantically-Aware Evolution](https://proceedings.iclr.cc/paper_files/paper/2025/file/08857467641ad82f635023d530605b4c-Paper-Conference.pdf)
  - [Mitigating Memorization in Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/e50ff94d174465348f15c45760f58f9f-Paper-Conference.pdf)
  - [A Percolation Model of Emergence: Analyzing Transformers Trained on a Formal Language](https://proceedings.iclr.cc/paper_files/paper/2025/file/5cd2b0a6b7423af6369cbdbbb228e8d0-Paper-Conference.pdf)
  - [Less for More: Enhanced Feedback-aligned Mixed LLMs for Molecule Caption Generation and Fine-Grained NLI Evaluation](https://aclanthology.org/2025.acl-long.144.pdf)
  - [Controllable Memorization in LLMs via Weight Pruning](https://aclanthology.org/2025.emnlp-main.765.pdf)
  - [Enhancing Logical Reasoning in Language Models via Symbolically-Guided Monte Carlo Process Supervision](https://aclanthology.org/2025.emnlp-main.1624.pdf)
- **Training data regurgitation** (behavioral indicator): *causes*, 6 papers
  > Since verbatim reproduction often stems from memorization during training
  - [Copyright-Protected Language Generation via Adaptive Model Fusion](https://proceedings.iclr.cc/paper_files/paper/2025/file/01953220e4becc6ac1078c24c1f8d3a7-Paper-Conference.pdf)
  - [Scalable Extraction of Training Data from Aligned, Production Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/cce0e917b050208170151f77b497fc71-Paper-Conference.pdf)
  - [A Statistical Approach for Controlled Training Data Detection](https://proceedings.iclr.cc/paper_files/paper/2025/file/c859b99b5d717c9035e79d43dfd69435-Paper-Conference.pdf)
  - [Measuring memorization in RLHF for code completion](https://proceedings.iclr.cc/paper_files/paper/2025/file/22811d2089d4aa0ba66e52a5e47efb65-Paper-Conference.pdf)
  - [Measuring memorization in language models via probabilistic extraction](https://aclanthology.org/2025.naacl-long.469.pdf)
  - [The Canary’s Echo: Auditing Privacy Risks of LLM-Generated Synthetic Text](https://raw.githubusercontent.com/mlresearch/v267/main/assets/meeus25a/meeus25a.pdf)
- **Privacy leakage** (behavioral indicator): *causes*, 3 papers
  > there is also growing concern around the privacy risks of their deployment (McCallum, 2023; Bloomberg, 2023; Politico, 2023), because they can memorize some of their training data verbatim
  - [Privacy Auditing of Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/e76814a0012a46ade4f997591e86f972-Paper-Conference.pdf)
  - [Min-K%++: Improved Baseline for Pre-Training Data Detection from Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/a2e3b4132ab2e0b7a21e6e75da7f91a9-Paper-Conference.pdf)
  - [Merger-as-a-Stealer: Stealing Targeted PII from Aligned LLMs with Model Merging](https://aclanthology.org/2025.emnlp-main.295.pdf)
- **LexEval** (measurement instrument): *measured_by*, 1 paper
  > to systematically organize various evaluation tasks, we propose a Legal Cognitive Ability Taxonomy (LexAbility Taxonomy), which includes six aspects: Memorization, Understanding, Logic Inference, Discrimination, Generation, and Ethic. (Section 3.1)
  - [LexEval: A Comprehensive Chinese Legal Benchmark for Evaluating Large Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/2cb40fc022ca7bdc1a9a78b793661284-Paper-Datasets_and_Benchmarks_Track.pdf)
- **Overfitting** (construct): *causes*, 1 paper
  > This result suggests that some of the reason for overﬁtting is due to partial memorization of the test set. (Section 5.4)
  - [A Careful Examination of Large Language Model Performance on Grade School Arithmetic](https://proceedings.neurips.cc/paper_files/paper/2024/file/53384f2090c6a5cac952c598fd67992f-Paper-Datasets_and_Benchmarks_Track.pdf)
- **AUXDATASET** (measurement instrument): *measured_by*, 1 paper
  > We thus call a subsequence of a generation memorized if (as in Deﬁnition 1) a 50-token-length subsequence exactly appears in AUXDATASET. (Section 3)
  - [Scalable Extraction of Training Data from Aligned, Production Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/cce0e917b050208170151f77b497fc71-Paper-Conference.pdf)
- **Verbatim regurgitation** (behavioral indicator): *causes*, 1 paper
  > Language models (LMs) can “memorize” information, i.e., encode training data in their weights in such a way that inference-time queries can lead to verbatim regurgitation of that data. (Section 1)
  - [Mitigating Memorization in Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/e50ff94d174465348f15c45760f58f9f-Paper-Conference.pdf)
- **In-context learning** (construct): *causes*, 1 paper
  > we show that fine-tuning an LLM (Gemini Nano v1 Gemini Team, Google, 2023) to memorize certain data can result in a reduction of its ICL ability. (Section 1)
  - [Toward Understanding In-context vs. In-weight Learning](https://proceedings.iclr.cc/paper_files/paper/2025/file/ae338b3fe6624798efa80b6581924028-Paper-Conference.pdf)
- **MMLU** (measurement instrument): *measured_by*, 1 paper
  > Memorization was evaluated using a subset of the MMLU benchmark focused on factual knowledge domains
  - [Unveiling the Secret Recipe: A Guide For Supervised Fine-Tuning Small LLMs](https://proceedings.iclr.cc/paper_files/paper/2025/file/b6e2c96bc4702f761d7d108d6e31930f-Paper-Conference.pdf)
- **LIMA** (measurement instrument): *measured_by*, 1 paper
  > Finally, we explore RLHF memorization on different task domains by studying memorization on natural language datasets, LIMA (Zhou et al., 2024) and Anthropic HH (Bai et al., 2022). (Section 5.5)
  - [Measuring memorization in RLHF for code completion](https://proceedings.iclr.cc/paper_files/paper/2025/file/22811d2089d4aa0ba66e52a5e47efb65-Paper-Conference.pdf)
- **HH-RLHF** (measurement instrument): *measured_by*, 1 paper
  > Finally, we explore RLHF memorization on different task domains by studying memorization on natural language datasets, LIMA (Zhou et al., 2024) and Anthropic HH (Bai et al., 2022). (Section 5.5)
  - [Measuring memorization in RLHF for code completion](https://proceedings.iclr.cc/paper_files/paper/2025/file/22811d2089d4aa0ba66e52a5e47efb65-Paper-Conference.pdf)
- **Privacy preservation** (construct): *causes*, 1 paper
  > This repeated exposure enhances the likelihood of the model memorizing specific details, thereby increasing the potential for data leakage during privacy attacks. (Section 1)
  - [DocMIA: Document-Level Membership Inference Attacks against DocVQA Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/231a8daf4f64935d0c7c6586f290b24f-Paper-Conference.pdf)
- **BookMIA** (measurement instrument): *measured_by*, 1 paper
  > We use the BookMIA dataset (Shi et al., 2023), which consists of text excerpts from books published in 2023 (after the knowledge cutoff of the models we study) as examples of unseen text, and passages from popular books as memorized examples (Chang et al., 2023). (Section 4.1)
  - [Information-Guided Identification of Training Data Imprint in (Proprietary) Large Language Models](https://aclanthology.org/2025.naacl-long.99.pdf)
- **PopQA** (measurement instrument): *measured_by*, 1 paper
  > Evaluation of continual learning capabilities across three key dimensions: factual memory (NaturalQuestions, PopQA), sense-making (NarrativeQA), and associativity (MuSiQue, 2Wiki, HotpotQA, and LV-Eval) (Figure 1).
  - [From RAG to Memory: Non-Parametric Continual Learning for Large Language Models](https://raw.githubusercontent.com/mlresearch/v267/main/assets/gutierrez25a/gutierrez25a.pdf)
- **Natural Questions** (measurement instrument): *measured_by*, 1 paper
  > “Simple QA primarily evaluates the ability to recall and retrieve factual knowledge accurately.” and “we randomly collect 1, 000 queries from the NaturalQuestions (NQ) dataset”
  - [From RAG to Memory: Non-Parametric Continual Learning for Large Language Models](https://raw.githubusercontent.com/mlresearch/v267/main/assets/gutierrez25a/gutierrez25a.pdf)
- **OWL** (measurement instrument): *measured_by*, 1 paper
  > We design OWL as a testbed for memorization as well as cross-lingual knowledge transfer in LLMs. (Section 2)
  - [OWL: Probing Cross-Lingual Recall of Memorized Texts via World Literature](https://aclanthology.org/2025.emnlp-main.1314.pdf)
- **Hallucination** (behavioral indicator): *causes*, 1 paper
  > However, when the attacker’s merging rate is high, the merged model fails to retain the victim model’s memorization ability, leading to hallucination phenomenon. (Section 5.4.1)
  - [Merger-as-a-Stealer: Stealing Targeted PII from Aligned LLMs with Model Merging](https://aclanthology.org/2025.emnlp-main.295.pdf)
- **Pre-training data detection** (behavioral indicator): *causes*, 1 paper
  > The powerful learning capabilities of LLMs often lead to noticeable memory effects on training data. This characteristic is a key reason why pre-training data detection algorithms are effective (Carlini et al., 2021; Tirumala et al., 2022). (Section 3.5)
  - [Identifying Pre-training Data in LLMs: A Neuron Activation-Based Detection Framework](https://aclanthology.org/2025.emnlp-main.946.pdf)
- **Recommendation** (behavioral indicator): *causes*, 1 paper
  > The experiments show that META ID improves memorization and diversity score, which leads to improvements in various recommendation tasks. (Section 1)
  - [Improving LLMs for Recommendation with Out-Of-Vocabulary Tokens](https://raw.githubusercontent.com/mlresearch/v267/main/assets/huang25ar/huang25ar.pdf)
- **Factuality** (construct): *causes*, 1 paper
  > Being able to memorize the facts in the training corpus enables the model to answer fact-seeking, knowledge intensive tasks more factually and accurately.
  - [Memory Layers at Scale](https://raw.githubusercontent.com/mlresearch/v267/main/assets/berges25a/berges25a.pdf)

### Associated with
- **Reasoning** (construct), 4 papers
  > It may suggest that width is crucial for memorization, while depth is important for reasoning, a similar phenomenon that echos the intuition of [80] (Section 5).
  - [LISA: Layerwise Importance Sampling for Memory-Efficient Large Language Model Fine-Tuning](https://proceedings.neurips.cc/paper_files/paper/2024/file/687163285b8affc8ee933bdca8e75747-Paper-Conference.pdf)
  - [Reasoning with Latent Thoughts: On the Power of Looped Transformers](https://proceedings.iclr.cc/paper_files/paper/2025/file/2676109d49d1eb26d6bc584a8f556305-Paper-Conference.pdf)
  - [RE-IMAGINE: Symbolic Benchmark Synthesis for Reasoning Evaluation](https://raw.githubusercontent.com/mlresearch/v267/main/assets/xu25n/xu25n.pdf)
  - [SSA: Semantic Contamination of LLM-Driven Fake News Detection](https://aclanthology.org/2025.emnlp-main.744.pdf)
- **Mathematical reasoning** (construct), 2 papers
  > Arithmetic reasoning provides a lens for this investigation, as it can be solved using various methods: learning known algorithms, developing novel approaches, or by memorizing vast quantities of input-output pairs. (Section 1)
  - [Arithmetic Without Algorithms: Language Models Solve Math with a Bag of Heuristics](https://proceedings.iclr.cc/paper_files/paper/2025/file/8c5f30296296d2ae402ebbd09aaa9c12-Paper-Conference.pdf)
  - [Exposing the Achilles' Heel: Evaluating LLMs Ability to Handle Mistakes in Mathematical Reasoning](https://aclanthology.org/2025.acl-long.1313.pdf)
- **MATH** (measurement instrument), 1 paper
  > Table 7: LLEMMA-34b’s accuracy on hits (a 30-gram overlap between a problem or solution and a training sequence) and non-hits by MATH difficulty level. (Table 7)
  - [Llemma: An Open Language Model for Mathematics](https://proceedings.iclr.cc/paper_files/paper/2024/file/b225f5c7cd13615e9558c3931fa4e66f-Paper-Conference.pdf)
- **Verbatim memorization** (construct), 1 paper
  > the existing literature on memorization (Carlini et al., 2021) suggests that many models may verbatim memorize the order of examples in a benchmark dataset. We now focus on building tests that can reliably identify this form of memorization. (Section 2)
  - [Proving Test Set Contamination in Black-Box Language Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/46e624c244cff669223d488defd4e835-Paper-Conference.pdf)
- **Out-of-distribution generalization** (construct), 1 paper
  > In fact, the small two-layer model we study has such a low capacity that it entirely skips the in-distribution generalization phase and immediately jumps from pure memorization to out-of-distribution generalization. (Section 4.1)
  - [Learning to grok: Emergence of in-context learning and skill composition in modular arithmetic tasks](https://proceedings.neurips.cc/paper_files/paper/2024/file/17d60fef592086d1a5cb136f1946df59-Paper-Conference.pdf)
- **Grokking** (construct), 1 paper
  > Power et al. [24] discovered Grokking, where models trained on modular arithmetic datasets have an abrupt change from random guessing to generalization on the test set way after the model memorized the training set. (Section 2)
  - [Learning to grok: Emergence of in-context learning and skill composition in modular arithmetic tasks](https://proceedings.neurips.cc/paper_files/paper/2024/file/17d60fef592086d1a5cb136f1946df59-Paper-Conference.pdf)
- **Factual recall** (behavioral indicator), 1 paper
  > a model’s ability to recall memorized facts from its pretraining data deteriorates faster than its ability to recognize structured patterns as we decrease the size of the model through compression, distinguishing between compressible tasks where generalization is possible and incompressible tasks that correspond to sheer memorization. (Section 1)
  - [Unlocking Tokens as Data Points for Generalization Bounds on Larger Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/11715d433f6f8b9106baae0df023deb3-Paper-Conference.pdf)
- **Text generation** (behavioral indicator), 1 paper
  > we observe that LISA is much better than LoRA at memorization-centered tasks, such as Writing or depicting image details, while this gap is much smaller in reasoning-centered tasks like Code or Math (Section 5).
  - [LISA: Layerwise Importance Sampling for Memory-Efficient Large Language Model Fine-Tuning](https://proceedings.neurips.cc/paper_files/paper/2024/file/687163285b8affc8ee933bdca8e75747-Paper-Conference.pdf)
- **Image generation** (behavioral indicator), 1 paper
  > we observe that LISA is much better than LoRA at memorization-centered tasks, such as Writing or depicting image details, while this gap is much smaller in reasoning-centered tasks like Code or Math (Section 5).
  - [LISA: Layerwise Importance Sampling for Memory-Efficient Large Language Model Fine-Tuning](https://proceedings.neurips.cc/paper_files/paper/2024/file/687163285b8affc8ee933bdca8e75747-Paper-Conference.pdf)
- **Causal reasoning** (construct), 1 paper
  > we will focus on causal reasoning as it provides us with a clear distinction between recall and reasoning1: the former is limited to inferring statistical correlations, whereas the latter involves working with interventions and counterfactuals (Pearl, 2000).
  - [Reasoning Elicitation in Language Models via Counterfactual Feedback](https://proceedings.iclr.cc/paper_files/paper/2025/file/bf145010b30dc5f14fa87dc152074e4d-Paper-Conference.pdf)
- **Visual perception** (construct), 1 paper
  > It raises a critical concern: “Does the model genuinely perceive and understand the input, or is it merely memorizing it?” (Section 1)
  - [Dynamic Multimodal Evaluation with Flexible Complexity by Vision-Language Bootstrapping](https://proceedings.iclr.cc/paper_files/paper/2025/file/36d9468ebdb76b9b229fbd343fff84d5-Paper-Conference.pdf)
- **In-weights learning** (construct), 1 paper
  > we consider a bi-level model that learns a “memorizing” in-weight predictor g as well as an in-context predictor h (Section 2)
  - [Toward Understanding In-context vs. In-weight Learning](https://proceedings.iclr.cc/paper_files/paper/2025/file/ae338b3fe6624798efa80b6581924028-Paper-Conference.pdf)
- **Factual question answering** (behavioral indicator), 1 paper
  > “Simple QA primarily evaluates the ability to recall and retrieve factual knowledge accurately.”
  - [From RAG to Memory: Non-Parametric Continual Learning for Large Language Models](https://raw.githubusercontent.com/mlresearch/v267/main/assets/gutierrez25a/gutierrez25a.pdf)
- **Knowledge manipulation** (construct), 1 paper
  > Answering such questions requires the model to both memorize and comprehend the knowledge. (Section 1)
  - [Physics of Language Models: Part 3.2, Knowledge Manipulation](https://proceedings.iclr.cc/paper_files/paper/2025/file/d5494c8747276d3cdb2598e5617de89d-Paper-Conference.pdf)
- **Benchmark overfitting** (construct), 1 paper
  > The failures suggest potential overfitting, where models overly rely on surface-level cues, memorized patterns, or specific terminologies. (Section 6)
  - [Forget What You Know about LLMs Evaluations - LLMs are Like a Chameleon](https://aclanthology.org/2025.emnlp-main.1098.pdf)
