# Information retrieval
**Type:** Behavioral indicator  
**Supporting papers:** 250  
**Also known as:** Evidence page retrieval, Evidence retrieval, Passage retrieval, Subgraph retrieval, Query matching, Material retrieval, Multi-table retrieval, Page-level retrieval, Table retrieval, Tool retrieval, Visual retrieval, Dependency retrieval, External knowledge retrieval, Long-term memory search, Short-term memory search, Document retrieval, Keyword-based file retrieval, Long-document retrieval, Memory retrieval, Retrieval, Semantic file retrieval, Sequence recall, Paper retrieval, Literature search, Document similarity search, Argumentative retrieval, File retrieval, Image crop retrieval, Sentence retrieval, Generative retrieval, Text retrieval, Long caption retrieval, Page retrieval, Prior case retrieval, Short caption retrieval, Statute retrieval, Argument retrieval, Literature retrieval, Tutorial retrieval, Legal case retrieval, Provision retrieval, Support sentence retrieval, Ad retrieval, Structured data retrieval, Cross-paragraph retrieval, Multi-step retrieval, Scientific literature search, Table-column retrieval, BioAssay retrieval, Content retrieval, Simple lookup, Cross-lingual retrieval, Relevant fact extraction, Web data retrieval, Database retrieval, Iterative retrieval, Reasoning with retrieved documents, Think-and-search, Image retrieval, Cross-file retrieval, Entity retrieval, Relation retrieval, Reasoning path retrieval, Dense retrieval, Material property retrieval, Multi-hop evidence retrieval, Multimodal document retrieval, Visual document retrieval, Cascade retrieval, Layout-level retrieval, Multilingual retrieval, Academic paper search, Factual knowledge retrieval, Information retrieval and localization, Retrievability, Associative memory retrieval, Causal retrieval, Information retrieval capability, Parametric knowledge retrieval, Task vector retrieval, Knowledge retrieval, Retrieval performance, Evidence recall, Implicit fact retrieval, Information Retrieval, Number retrieval, Subgraph extraction, Similar case identification  

## State of the Field

**Space of definitions.** Across papers, the prevailing usage is query-conditioned selection or extraction of relevant information from some store, most often a document corpus, memory store, knowledge base, or long context. Success is usually framed as retrieving the relevant item or ranked top-k set, for example the correct page, passage, sentence, table, or document, and some papers narrow this to locating a small needle, fact, value, or sentence inside a large context. A smaller line treats retrieval as a staged component, first fetching evidence or context for later reasoning or answer generation, or as online query matching against a pre-built index.

**Variants.** Papers use the label for many task variants. The most common cluster is text and document retrieval, under names such as passage retrieval, document retrieval, page-level retrieval, and evidence retrieval; another recurring cluster is table-centered work, including table retrieval, multi-table retrieval, table-column retrieval, and simple lookup. Other variants cover memory retrieval and long- or short-term memory search, visual and multimodal retrieval over document pages, images, or image crops, knowledge-graph retrieval such as subgraph and reasoning path retrieval, and smaller application domains such as tools and code files, legal cases and statutes, scientific literature, databases, materials, ads, and BioAssays.

**Space of elicitation and scores.** Papers link information retrieval to 31 measurement instruments. The most frequently listed are BEIR, MTEB, AIR-Bench (information retrieval), ArXivQA, and BABILong; the rest span long-context tests, document or visual question answering datasets, multilingual resources, and other domain-specific retrieval benchmarks. Scoring is usually by ranking or selection quality, with papers reporting retrieval accuracy, recall and precision, Recall@100, NDCG@10, Hits@1 or Hits@5, and MRR@5.

**What it is taken as evidence of.** Papers connect information retrieval to 8 constructs. The most frequently linked are Consistency, Cross-lingual alignment, Factual grounding, Interpretability and explainability, and Memory management, with additional links to other constructs, and the recorded links are mixed in direction rather than pointing to a single agreed construct. One line claims a causal relationship from Consistency to information retrieval, other papers claim causal relationships from information retrieval to Cross-lingual alignment, Factual grounding, and Interpretability and explainability, and another reports it is related to Memory management.

## Sources

**Information retrieval** (4 papers: [From Isolated Conversations to Hierarchical Schemas: Dynamic Tree Memory Representation for LLMs](https://proceedings.iclr.cc/paper_files/paper/2025/file/0382cb76309820f71c6eacd47b36ce71-Paper-Conference.pdf), [Star Attention: Efficient LLM Inference over Long Sequences](https://raw.githubusercontent.com/mlresearch/v267/main/assets/acharya25a/acharya25a.pdf), [OmniThink: Expanding Knowledge Boundaries in Machine Writing through Thinking](https://aclanthology.org/2025.emnlp-main.50.pdf), [IceFormer: Accelerated Inference with Long-Sequence Transformers on CPUs](https://proceedings.iclr.cc/paper_files/paper/2024/file/4059971112ab22fc7b6aed520aaca6b2-Paper-Conference.pdf))
> The process of finding and extracting relevant information from a memory store or document corpus in response to a query.

**Evidence page retrieval** (1 paper: [SV-RAG: LoRA-Contextualizing Adaptation of MLLMs for Long Document Understanding](https://proceedings.iclr.cc/paper_files/paper/2025/file/0d40c7b4d78bf7f08ba532542818f6c0-Paper-Conference.pdf))
> The observable task of identifying and fetching the most relevant page or pages from a multi-page document in response to a user's query.

**Passage retrieval** (3 papers: [TidalDecode: Fast and Accurate LLM Decoding with Position Persistent Sparse Attention](https://proceedings.iclr.cc/paper_files/paper/2025/file/11440c427f0f76f191ac06b50d7a2517-Paper-Conference.pdf), [From RAG to Memory: Non-Parametric Continual Learning for Large Language Models](https://raw.githubusercontent.com/mlresearch/v267/main/assets/gutierrez25a/gutierrez25a.pdf), [RPDR: A Round-trip Prediction-Based Data Augmentation Framework for Long-Tail Question Answering](https://aclanthology.org/2025.emnlp-main.1119.pdf))
> The task of identifying and retrieving text passages from a large corpus that are relevant to a given query.

**Subgraph retrieval** (2 papers: [Simple is Effective: The Roles of Graphs and Large Language Models in Knowledge-Graph-Based Retrieval-Augmented Generation](https://proceedings.iclr.cc/paper_files/paper/2025/file/11e1900e680f5fe1893a8e27362dbe2c-Paper-Conference.pdf), [SAFE: Schema-Driven Approximate Distance Join for Efficient Knowledge Graph Querying](https://aclanthology.org/2025.emnlp-main.883.pdf))
> Selecting a relevant subset of triples from a knowledge graph to support downstream reasoning.

**Evidence retrieval** (5 papers: [CofCA: A STEP-WISE Counterfactual Multi-hop QA benchmark](https://proceedings.iclr.cc/paper_files/paper/2025/file/2628d4d3b054c2d7ad33ab03435204f4-Paper-Conference.pdf), [DEFAME: Dynamic Evidence-based FAct-checking with Multimodal Experts](https://raw.githubusercontent.com/mlresearch/v267/main/assets/braun25b/braun25b.pdf), [ReAgent: Reversible Multi-Agent Reasoning for Knowledge-Enhanced Multi-Hop QA](https://aclanthology.org/2025.emnlp-main.202.pdf), [Unsupervised Pretraining for Fact Verification by Language Model Distillation](https://proceedings.iclr.cc/paper_files/paper/2024/file/238c98450b1d9e8055f94d22f303bb57-Paper-Conference.pdf), [Verify-in-the-Graph: Entity Disambiguation Enhancement for Complex Claim Verification with Interactive Graph Representation](https://aclanthology.org/2025.naacl-long.268.pdf))
> The process of identifying and extracting relevant pieces of information from a given set of passages or documents to support an answer.

**Multi-table retrieval** (1 paper: [MMQA: Evaluating LLMs with Multi-Table Multi-Hop Complex Questions](https://proceedings.iclr.cc/paper_files/paper/2025/file/794a425a2e47e05d29d30f79b79a692d-Paper-Conference.pdf))
> The task of selecting a set of relevant and joinable tables from a larger corpus in order to answer a given question.

**Material retrieval** (1 paper: [MatExpert: Decomposing Materials Discovery By Mimicking Human Experts](https://proceedings.iclr.cc/paper_files/paper/2025/file/7d6850f4c82520793f738d98a72aab9d-Paper-Conference.pdf))
> The observable task of identifying and retrieving an existing material from a database that most closely matches a user-provided description of desired properties.

**Tool retrieval** (4 papers: [From Exploration to Mastery: Enabling LLMs to Master Tools via Self-Driven Interactions](https://proceedings.iclr.cc/paper_files/paper/2025/file/8c22e5e918198702765ecff4b20d0a90-Paper-Conference.pdf), [PORTS: Preference-Optimized Retrievers for Tool Selection with Large Language Models](https://aclanthology.org/2025.emnlp-main.507.pdf), [CRAFT: Customizing LLMs by Creating and Retrieving from Specialized Toolsets](https://proceedings.iclr.cc/paper_files/paper/2024/file/af31604708f3e44b4de9fdfa6dcaa9d1-Paper-Conference.pdf), [EASYTOOL: Enhancing LLM-based Agents with Concise Tool Instruction](https://aclanthology.org/2025.naacl-long.44.pdf))
> The task of selecting the most relevant tool(s) from a large collection based on a user's query or a given problem context.

**Page-level retrieval** (2 papers: [ColPali: Efficient Document Retrieval with Vision Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/99e9e141aafc314f76b0ca3dd66898b3-Paper-Conference.pdf), [MMDocIR: Benchmarking Multimodal Retrieval for Long Documents](https://aclanthology.org/2025.emnlp-main.1576.pdf))
> Given a query, selecting the correct document page from a corpus of candidate pages.

**Table retrieval** (4 papers: [ColPali: Efficient Document Retrieval with Vision Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/99e9e141aafc314f76b0ca3dd66898b3-Paper-Conference.pdf), [SportReason: Evaluating Retrieval-Augmented Reasoning across Tables and Text for Sports Question Answering](https://aclanthology.org/2025.emnlp-main.34.pdf), [OpenTab: Advancing Large Language Models as Open-domain Table Reasoners](https://proceedings.iclr.cc/paper_files/paper/2024/file/055ff1d86ca33e84c744cf8cca65ec8f-Paper-Conference.pdf), [TRANSIENTTABLES: Evaluating LLMs' Reasoning on Temporally Evolving Semi-structured Tables](https://aclanthology.org/2025.naacl-long.332.pdf))
> The task of retrieving documents or pages based on the content of tables they contain.

**Query matching** (1 paper: [ColPali: Efficient Document Retrieval with Vision Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/99e9e141aafc314f76b0ca3dd66898b3-Paper-Conference.pdf))
> The online process of matching a query against a pre-built document index to rank and retrieve relevant documents.

**Visual retrieval** (2 papers: [MuirBench: A Comprehensive Benchmark for Robust Multi-image Understanding](https://proceedings.iclr.cc/paper_files/paper/2025/file/9cf6139382f98623d08cc595622f3fb1-Paper-Conference.pdf), [VisDoM: Multi-Document QA with Visually Rich Elements Using Multimodal Retrieval-Augmented Generation](https://aclanthology.org/2025.naacl-long.310.pdf))
> Finding an image that matches a target image or contains the same depicted entity or scene.

**Long-term memory search** (1 paper: [Streaming Video Understanding and Multi-round Interaction with Memory-enhanced Knowledge](https://proceedings.iclr.cc/paper_files/paper/2025/file/ad2fa437f7c23e4e9875599c6065d18a-Paper-Conference.pdf))
> Recalling and answering questions about events that occurred more than a minute prior to the user's query in a video.

**Short-term memory search** (1 paper: [Streaming Video Understanding and Multi-round Interaction with Memory-enhanced Knowledge](https://proceedings.iclr.cc/paper_files/paper/2025/file/ad2fa437f7c23e4e9875599c6065d18a-Paper-Conference.pdf))
> Responding to user queries about events that concluded less than 20 seconds prior, testing recall of recent activities.

**Knowledge retrieval** (2 papers: [Reasoning-Enhanced Healthcare Predictions with Knowledge Graph Community Retrieval](https://proceedings.iclr.cc/paper_files/paper/2025/file/cb5a3b4589c1a16f14740396625cbfc8-Paper-Conference.pdf), [HydraRAG: Structured Cross-Source Enhanced Large Language Model Reasoning](https://aclanthology.org/2025.emnlp-main.730.pdf))
> Retrieving relevant medical knowledge from a knowledge graph or corpus to support prediction.

**Dependency retrieval** (1 paper: [Rethinking and Improving Autoformalization: Towards a Faithful Metric and a Dependency Retrieval-based Approach](https://proceedings.iclr.cc/paper_files/paper/2025/file/d630537fc4402cfa3ebbc7450a0cac91-Paper-Conference.pdf))
> Selecting relevant formal objects from a library for an informal statement.

**External knowledge retrieval** (2 papers: [MMFakeBench: A Mixed-Source Multimodal Misinformation Detection Benchmark for LVLMs](https://proceedings.iclr.cc/paper_files/paper/2025/file/d6c53fe062716387ff0df73cc53de60c-Paper-Conference.pdf), [Search-o1: Agentic Search-Enhanced Large Reasoning Models](https://aclanthology.org/2025.emnlp-main.276.pdf))
> Querying outside knowledge sources to obtain evidence relevant to a verification decision.

**Document retrieval** (2 papers: [VisRAG: Vision-based Retrieval-augmented Generation on Multi-modality Documents](https://proceedings.iclr.cc/paper_files/paper/2025/file/3640a1997a4c9571cea9db2c82e1fc35-Paper-Conference.pdf), [Diffusion vs. Autoregressive Language Models: A Text Embedding Perspective](https://aclanthology.org/2025.emnlp-main.213.pdf))
> The process of selecting relevant document pages from a corpus based on a query.

**Semantic file retrieval** (1 paper: [From Commands to Prompts: LLM-based Semantic File System for AIOS](https://proceedings.iclr.cc/paper_files/paper/2025/file/517eb19e99947f60afff0cf93e451825-Paper-Conference.pdf))
> The observable task of retrieving files based on the semantic similarity of their content to a natural language query, rather than exact keyword matching.

**Keyword-based file retrieval** (1 paper: [From Commands to Prompts: LLM-based Semantic File System for AIOS](https://proceedings.iclr.cc/paper_files/paper/2025/file/517eb19e99947f60afff0cf93e451825-Paper-Conference.pdf))
> Retrieving files that contain specified keywords in their names or contents.

**Memory retrieval** (8 papers: [Agent Security Bench (ASB): Formalizing and Benchmarking Attacks and Defenses in LLM-based Agents](https://proceedings.iclr.cc/paper_files/paper/2025/file/5750f91d8fb9d5c02bd8ad2c3b44456b-Paper-Conference.pdf), [Minerva: A Programmable Memory Test Benchmark for Language Models](https://raw.githubusercontent.com/mlresearch/v267/main/assets/xia25c/xia25c.pdf), [Flexibly Utilize Memory for Long-Term Conversation via a Fragment-then-Compose Framework](https://aclanthology.org/2025.emnlp-main.1069.pdf), [RoleAgent: Building, Interacting, and Benchmarking High-quality Role-Playing Agents from Scripts](https://proceedings.neurips.cc/paper_files/paper/2024/file/5875aca1ef70285a35940afbbce0f9fb-Paper-Datasets_and_Benchmarks_Track.pdf), [HMT: Hierarchical Memory Transformer for Efficient Long Context Language Processing](https://aclanthology.org/2025.naacl-long.410.pdf), [Hello Again! LLM-powered Personalized Agent for Long-term Dialogue](https://aclanthology.org/2025.naacl-long.272.pdf), [MADial-Bench: Towards Real-world Evaluation of Memory-Augmented Dialogue Generation](https://aclanthology.org/2025.naacl-long.499.pdf), [Towards Lifelong Dialogue Agents via Timeline-based Memory Management](https://aclanthology.org/2025.naacl-long.435.pdf))
> The process of an agent accessing and retrieving relevant information from a memory database or knowledge base.

**Retrieval** (2 papers: [Making Text Embedders Few-Shot Learners](https://proceedings.iclr.cc/paper_files/paper/2025/file/5eba8556ce2d1afff57591464d48fbc3-Paper-Conference.pdf), [Accelerate Parallelizable Reasoning via Parallel Decoding within One Sequence](https://aclanthology.org/2025.emnlp-main.457.pdf))
> Selecting the most relevant passage or candidate for a query based on embedding similarity.

**Long-document retrieval** (2 papers: [Making Text Embedders Few-Shot Learners](https://proceedings.iclr.cc/paper_files/paper/2025/file/5eba8556ce2d1afff57591464d48fbc3-Paper-Conference.pdf), [SAKI-RAG: Mitigating Context Fragmentation in Long-Document RAG via Sentence-level Attention Knowledge Integration](https://aclanthology.org/2025.emnlp-main.63.pdf))
> The task of retrieving relevant information or documents from a collection of long-form texts in response to a query.

**Sequence recall** (1 paper: [Building, Reusing, and Generalizing Abstract Representations from Concrete Sequences](https://proceedings.iclr.cc/paper_files/paper/2025/file/e46984e056185b21ddb1e7973c365f14-Paper-Conference.pdf))
> The observable task of reproducing a sequence of items that was previously presented.

**Paper retrieval** (1 paper: [Can LLMs Generate Novel Research Ideas? A Large-Scale Human Study with 100+ NLP Researchers](https://proceedings.iclr.cc/paper_files/paper/2025/file/ea94957d81b1c1caf87ef5319fa6b467-Paper-Conference.pdf))
> The action of searching for and selecting relevant academic papers related to a given research topic.

**Literature search** (1 paper: [BioDiscoveryAgent: An AI Agent for Designing Genetic Perturbation Experiments](https://proceedings.iclr.cc/paper_files/paper/2025/file/4252dc94531833029000f85dc5fac792-Paper-Conference.pdf))
> A tool-enabled action where the agent formulates search queries, uses an API to find relevant scientific papers, and summarizes them to inform its gene selection.

**Document similarity search** (1 paper: [Fundamental Limitations on Subquadratic Alternatives to Transformers](https://proceedings.iclr.cc/paper_files/paper/2025/file/76012c39b10425b189c38850da053893-Paper-Conference.pdf))
> Selecting the most similar or least similar pair of documents from a set based on their embeddings.

**Argumentative retrieval** (1 paper: [LongRoPE2: Near-Lossless LLM Context Window Scaling](https://raw.githubusercontent.com/mlresearch/v267/main/assets/shang25a/shang25a.pdf))
> The task of retrieving text segments based on their argumentative content or stance.

**File retrieval** (1 paper: [Nemotron-CORTEXA: Enhancing LLM Agents for Software Engineering Tasks via Improved Localization and Solution Diversity](https://raw.githubusercontent.com/mlresearch/v267/main/assets/sohrabizadeh25a/sohrabizadeh25a.pdf))
> The process of identifying and retrieving source code files most relevant to a given software issue from a large codebase.

**Image crop retrieval** (1 paper: [Retrieval-Augmented Perception: High-resolution Image Perception Meets Visual RAG](https://raw.githubusercontent.com/mlresearch/v267/main/assets/wang25at/wang25at.pdf))
> Selecting and retrieving image regions most relevant to a query based on similarity scoring between the query and image crops.

**Sentence retrieval** (4 papers: [DocKS-RAG: Optimizing Document-Level Relation Extraction through LLM-Enhanced Hybrid Prompt Tuning](https://raw.githubusercontent.com/mlresearch/v267/main/assets/xu25am/xu25am.pdf), [LangSAMP: Language-Script Aware Multilingual Pretraining](https://aclanthology.org/2025.acl-long.88.pdf), [Mitigating Lost-in-Retrieval Problems in Retrieval Augmented Multi-Hop Question Answering](https://aclanthology.org/2025.acl-long.1089.pdf), [SetCSE: Set Operations using Contrastive Learning of Sentence Embeddings](https://proceedings.iclr.cc/paper_files/paper/2024/file/ed863220bf8b6ae698e26d66e86fb97d-Paper-Conference.pdf))
> Identifying and retrieving top-k sentences from a document that are semantically similar to a query to enrich contextual understanding.

**Generative retrieval** (1 paper: [MixLoRA-DSI: Dynamically Expandable Mixture-of-LoRA Experts for Rehearsal-Free Generative Retrieval over Dynamic Corpora](https://aclanthology.org/2025.emnlp-main.20.pdf))
> The task of using a generative model to directly produce document identifiers in response to a query, treating information retrieval as a sequence-to-sequence problem.

**Text retrieval** (2 papers: [Enhancing LLM Text Detection with Retrieved Contexts and Logits Distribution Consistency](https://aclanthology.org/2025.emnlp-main.503.pdf), [Matina: A Large-Scale 73B Token Persian Text Corpus](https://aclanthology.org/2025.naacl-long.462.pdf))
> The task of finding and returning relevant documents or passages from a large corpus based on a given query text.

**Page retrieval** (1 paper: [MoLoRAG: Bootstrapping Document Understanding via Multi-modal Logic-aware Retrieval](https://aclanthology.org/2025.emnlp-main.708.pdf))
> Selecting a subset of document pages most relevant to a given question for downstream processing.

**Short caption retrieval** (1 paper: [Vision-Free Retrieval: Rethinking Multimodal Search with Textual Scene Descriptions](https://aclanthology.org/2025.emnlp-main.709.pdf))
> A retrieval task where the textual queries are concise, often ungrammatical phrases or keywords, mimicking real-world user search behavior.

**Long caption retrieval** (1 paper: [Vision-Free Retrieval: Rethinking Multimodal Search with Textual Scene Descriptions](https://aclanthology.org/2025.emnlp-main.709.pdf))
> A retrieval task where the textual queries are lengthy, descriptive, paragraph-level sentences.

**Statute retrieval** (1 paper: [IL-PCSR: Legal Corpus for Prior Case and Statute Retrieval](https://aclanthology.org/2025.emnlp-main.738.pdf))
> The observable task of identifying and ranking relevant legal statutes (sections/articles of law) applicable to a given legal case judgment.

**Prior case retrieval** (1 paper: [IL-PCSR: Legal Corpus for Prior Case and Statute Retrieval](https://aclanthology.org/2025.emnlp-main.738.pdf))
> Given a query case, ranking prior cases or precedents that should be cited by that case.

**Argument retrieval** (1 paper: [Evaluating the Effectiveness and Scalability of LLM-Based Data Augmentation for Retrieval](https://aclanthology.org/2025.emnlp-main.888.pdf))
> A retrieval task that involves finding documents or passages containing arguments relevant to a specific topic or stance.

**Literature retrieval** (1 paper: [From Automation to Autonomy: A Survey on Large Language Models in Scientific Discovery](https://aclanthology.org/2025.emnlp-main.895.pdf))
> Automatically searching and retrieving relevant scientific literature based on research queries or objectives.

**Tutorial retrieval** (1 paper: [Retrieval-augmented GUI Agents with Generative Guidelines](https://aclanthology.org/2025.emnlp-main.902.pdf))
> Fetching potentially relevant web tutorials using the task description as a query, forming the basis for subsequent guidance generation.

**Support sentence retrieval** (1 paper: [Measuring Risk of Bias in Biomedical Reports: The RoBBR Benchmark](https://aclanthology.org/2025.emnlp-main.160.pdf))
> The observable behavior of identifying and outputting specific sentences from a biomedical paper that provide evidence for a risk-of-bias assessment.

**Legal case retrieval** (2 papers: [JUREX-4E: Juridical Expert-Annotated Four-Element Knowledge Base for Legal Reasoning](https://aclanthology.org/2025.emnlp-main.188.pdf), [IFIR: A Comprehensive Benchmark for Evaluating Instruction-Following in Expert-Domain Information Retrieval](https://aclanthology.org/2025.naacl-long.511.pdf))
> The task of identifying and ranking relevant legal cases from a large corpus in response to a query case.

**Provision retrieval** (1 paper: [KoBLEX: Open Legal Question Answering with Multi-hop Reasoning](https://aclanthology.org/2025.emnlp-main.200.pdf))
> Identifying and retrieving relevant statutory provisions from a legal corpus in response to a legal question, as part of a retrieval-augmented reasoning pipeline.

**Structured data retrieval** (1 paper: [Weaver: Interweaving SQL and LLM for Table Reasoning](https://aclanthology.org/2025.emnlp-main.1436.pdf))
> Performing SQL operations such as filtering, joining, aggregating, and grouping on tabular data to extract relevant information.

**Ad retrieval** (1 paper: [Real-time Ad Retrieval via LLM-generative Commercial Intention for Sponsored Search Advertising](https://aclanthology.org/2025.emnlp-main.1473.pdf))
> The process of selecting and returning relevant advertisements from a large corpus in response to a user query.

**Cross-paragraph retrieval** (1 paper: [SAKI-RAG: Mitigating Context Fragmentation in Long-Document RAG via Sentence-level Attention Knowledge Integration](https://aclanthology.org/2025.emnlp-main.63.pdf))
> The task of identifying and retrieving relevant information that is distributed across multiple paragraphs within a long document.

**Multi-step retrieval** (1 paper: [Investigating Pedagogical Teacher and Student LLM Agents: Genetic Adaptation Meets Retrieval-Augmented Generation Across Learning Styles](https://aclanthology.org/2025.emnlp-main.675.pdf))
> The process of retrieving information from a knowledge base in a series of discrete steps, where each step corresponds to a part of a larger reasoning plan.

**Context retrieval** (2 papers: [Efficient Context Selection for Long-Context QA: No Tuning, No Iteration, Just Adaptive-k](https://aclanthology.org/2025.emnlp-main.1017.pdf), [Handling Missing Entities in Zero-Shot Named Entity Recognition: Integrated Recall and Retrieval Augmentation](https://aclanthology.org/2025.naacl-long.540.pdf))
> Selecting and returning a subset of relevant documents or passages from a large corpus based on query similarity.

**Scientific literature search** (1 paper: [LimRank: Less is More for Reasoning-Intensive Information Reranking](https://aclanthology.org/2025.emnlp-main.1041.pdf))
> Retrieving relevant papers from a scientific literature corpus for natural-language queries.

**Table-column retrieval** (1 paper: [GRIT: Guided Relational Integration for Efficient Multi-Table Understanding](https://aclanthology.org/2025.emnlp-main.1118.pdf))
> The task of identifying and returning the specific tables and columns from a database that are relevant to answering a given natural language query.

**BioAssay retrieval** (1 paper: [Assay2Mol: Large Language Model-based Drug Design Using BioAssay Context](https://aclanthology.org/2025.emnlp-main.1390.pdf))
> Identifying and retrieving relevant biochemical screening records from PubChem based on textual similarity between a query protein description and assay metadata.

**Content retrieval** (1 paper: [TALON: A Multi-Agent Framework for Long-Table Exploration and Question Answering](https://aclanthology.org/2025.emnlp-main.1393.pdf))
> The behavior of locating and extracting specific rows, columns, or cell values from a table that are relevant to a given query.

**Simple lookup** (1 paper: [TableEval: A Real-World Benchmark for Complex, Multilingual, and Multi-Structured Table Question Answering](https://aclanthology.org/2025.emnlp-main.363.pdf))
> A basic form of information retrieval that involves finding a direct fact or value in a table.

**Cross-lingual retrieval** (2 papers: [Conan-Embedding-v2: Training an LLM from Scratch for Text Embeddings](https://aclanthology.org/2025.emnlp-main.758.pdf), [Steering into New Embedding Spaces: Analyzing Cross-Lingual Alignment Induced by Model Interventions in Multilingual Language Models](https://aclanthology.org/2025.acl-long.118.pdf))
> Retrieving relevant documents in one language (e.g., English) in response to a query in another language, based on aligned multilingual embeddings.

**Relevant fact extraction** (1 paper: [Program of Thoughts for Financial Reasoning: Leveraging Dynamic In-Context Examples and Generative Retrieval](https://aclanthology.org/2025.emnlp-main.1577.pdf))
> The observable task of identifying and retrieving specific pieces of information from a larger context of text and tables that are necessary to answer a given question.

**Web data retrieval** (1 paper: [Text2Vis: A Challenging and Diverse Benchmark for Generating Multimodal Visualizations from Text](https://aclanthology.org/2025.emnlp-main.1622.pdf))
> Locating and retrieving external data from the web before generating visualizations, in response to queries that do not provide complete data tables.

**Database retrieval** (1 paper: [LinkAlign: Scalable Schema Linking for Real-World Large-Scale Multi-Database Text-to-SQL](https://aclanthology.org/2025.emnlp-main.51.pdf))
> The observable process of selecting the correct target database from a large pool of candidate databases based on a natural language query.

**Iterative retrieval** (1 paper: [SportReason: Evaluating Retrieval-Augmented Reasoning across Tables and Text for Sports Question Answering](https://aclanthology.org/2025.emnlp-main.34.pdf))
> The process of generating multiple search queries in sequence, retrieving evidence at each step, and using the results to inform subsequent queries, as implemented in agentic RAG systems.

**Think-and-search** (1 paper: [LeTS: Learning to Think-and-Search via Process-and-Outcome Reward Hybridization](https://aclanthology.org/2025.emnlp-main.257.pdf))
> The observable behavior of an LLM alternating between internal reasoning (thinking) and external knowledge retrieval (searching) across multiple steps to answer complex queries.

**Reasoning with retrieved documents** (1 paper: [Search-o1: Agentic Search-Enhanced Large Reasoning Models](https://aclanthology.org/2025.emnlp-main.276.pdf))
> The behavior of incorporating retrieved external knowledge into the ongoing reasoning chain to support accurate problem solving.

**Image retrieval** (1 paper: [Re-Align: Aligning Vision Language Models via Retrieval-Augmented Direct Preference Optimization](https://aclanthology.org/2025.emnlp-main.121.pdf))
> Finding semantically similar images from a database based on visual content of a query image.

**Cross-file retrieval** (1 paper: [LMR-BENCH: Evaluating LLM Agent's Ability on Reproducing Language Modeling Research](https://aclanthology.org/2025.emnlp-main.314.pdf))
> Locating and utilizing relevant code, constants, or class definitions from files other than the one being modified, to ensure correct implementation.

**Entity retrieval** (1 paper: [Beyond Seen Data: Improving KBQA Generalization Through Schema-Guided Logical Form Generation](https://aclanthology.org/2025.emnlp-main.442.pdf))
> Identifying and retrieving candidate entities from a knowledge base that correspond to mentions in a natural language question.

**Relation retrieval** (1 paper: [Beyond Seen Data: Improving KBQA Generalization Through Schema-Guided Logical Form Generation](https://aclanthology.org/2025.emnlp-main.442.pdf))
> The process of identifying and retrieving relations from a knowledge base that are semantically relevant to a given question.

**Reasoning path retrieval** (2 papers: [RJE: A Retrieval-Judgment-Exploration Framework for Efficient Knowledge Graph Question Answering with LLMs](https://aclanthology.org/2025.emnlp-main.873.pdf), [Reasoning on Graphs: Faithful and Interpretable Large Language Model Reasoning](https://proceedings.iclr.cc/paper_files/paper/2024/file/3e2aeb66481dd63a32421bf032b70384-Paper-Conference.pdf))
> Extracting sequences of relations and entities from a knowledge graph that are semantically relevant to a natural language question.

**Dense retrieval** (1 paper: [ExpandR: Teaching Dense Retrievers Beyond Queries with LLM Guidance](https://aclanthology.org/2025.emnlp-main.963.pdf))
> The task of retrieving relevant documents from a collection by encoding queries and documents into a shared embedding space and finding the nearest neighbors.

**Material property retrieval** (1 paper: [LLaMP: Large Language Model Made Powerful for High-fidelity Materials Knowledge Retrieval](https://aclanthology.org/2025.emnlp-main.1280.pdf))
> The observable task of extracting specific physical or chemical properties of materials, such as bulk modulus, bandgap, or formation energy, from structured databases.

**Multi-hop evidence retrieval** (1 paper: [Improving Zero-shot Sentence Decontextualisation with Content Selection and Planning](https://aclanthology.org/2025.emnlp-main.1258.pdf))
> The task of retrieving secondary evidence based on an initial piece of information, used here to evaluate the utility of decontextualised sentences as intermediate reasoning steps.

**Multimodal document retrieval** (1 paper: [Zero-shot Multimodal Document Retrieval via Cross-modal Question Generation](https://aclanthology.org/2025.emnlp-main.1324.pdf))
> The task of identifying and returning the most relevant document pages, containing both text and images, from a large collection in response to a user's text query.

**Visual document retrieval** (1 paper: [SERVAL: Surprisingly Effective Zero-Shot Visual Document Retrieval Powered by Large Vision and Language Models](https://aclanthology.org/2025.emnlp-main.1568.pdf))
> Retrieving relevant documents from a collection given a text query over document images or their generated descriptions.

**Cascade retrieval** (1 paper: [MMDocIR: Benchmarking Multimodal Retrieval for Long Documents](https://aclanthology.org/2025.emnlp-main.1576.pdf))
> A two-stage retrieval process where page-level retrieval is performed first, followed by layout-level retrieval within the set of initially retrieved pages.

**Layout-level retrieval** (1 paper: [MMDocIR: Benchmarking Multimodal Retrieval for Long Documents](https://aclanthology.org/2025.emnlp-main.1576.pdf))
> The observable task of detecting and returning specific layout elements, such as paragraphs, figures, or tables, that contain the evidence for a user's query.

**Multilingual retrieval** (1 paper: [SERVAL: Surprisingly Effective Zero-Shot Visual Document Retrieval Powered by Large Vision and Language Models](https://aclanthology.org/2025.emnlp-main.1568.pdf))
> Retrieving relevant documents across multiple languages using queries and document collections in different languages.

**Academic paper search** (1 paper: [STaRK: Benchmarking LLM Retrieval on Textual and Relational Knowledge Bases](https://proceedings.neurips.cc/paper_files/paper/2024/file/e607b1419e9ae7cd5cb5b5bb60c2ad5c-Paper-Datasets_and_Benchmarks_Track.pdf))
> The task of retrieving relevant academic papers from a bibliographic knowledge base based on a user's query about authors, topics, institutions, or citations.

**Evidence recall** (1 paper: [NovelQA: Benchmarking Question Answering on Documents Exceeding 200K Tokens](https://proceedings.iclr.cc/paper_files/paper/2025/file/3adb85a348a18cdd74ce99fbbab20301-Paper-Conference.pdf))
> The observable behavior of retrieving and presenting specific textual excerpts from a source document that support a given answer.

**Implicit fact retrieval** (1 paper: [ImpliRet: Benchmarking the Implicit Fact Retrieval Challenge](https://aclanthology.org/2025.emnlp-main.1685.pdf))
> The observable behavior of retrieving a document that contains implicitly stated information necessary to answer a query, requiring inference beyond surface-level lexical or semantic similarity.

**Information Retrieval** (1 paper: [TRANSIENTTABLES: Evaluating LLMs' Reasoning on Temporally Evolving Semi-structured Tables](https://aclanthology.org/2025.naacl-long.332.pdf))
> A two-stage evaluation method that assesses a model's ability to first retrieve relevant tables from a timeline and then generate answers based on them, isolating the retrieval component of temporal reasoning.

**Number retrieval** (1 paper: [OmniKV: Dynamic Context Selection for Efficient Long-Context LLMs](https://proceedings.iclr.cc/paper_files/paper/2025/file/da1131a86ac3c70e0b7cae89c3d4df22-Paper-Conference.pdf))
> The task of accurately identifying and extracting a specific number from a long context.

**Subgraph extraction** (1 paper: [KG-CQR: Leveraging Structured Relation Representations in Knowledge Graphs for Contextual Query Retrieval](https://aclanthology.org/2025.emnlp-main.824.pdf))
> Identifying and retrieving a set of relevant knowledge graph triples that are semantically aligned with the input query, based on textual triplet representations.

**Similar case identification** (1 paper: [LexEval: A Comprehensive Chinese Legal Benchmark for Evaluating Large Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/2cb40fc022ca7bdc1a9a78b793661284-Paper-Datasets_and_Benchmarks_Track.pdf))
> Determining the most relevant case to a given query case from a list of candidates.

## Relationships

### Information retrieval →
- **BEIR** (measurement instrument): *measured_by*, 5 papers
  > “BEIR dataset [52] is a popular benchmark for evaluating dense retrievers’ zero-shot effectiveness”
  - [Enhancing LLM’s Cognition via Structurization](https://proceedings.neurips.cc/paper_files/paper/2024/file/f169ec4d47933ea4896b994af8ff4f17-Paper-Conference.pdf)
  - [NV-Embed: Improved Techniques for Training LLMs as Generalist Embedding Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/c4bf73386022473a652a18941e9ea6f8-Paper-Conference.pdf)
  - [BRIGHT: A Realistic and Challenging Benchmark for Reasoning-Intensive Retrieval](https://proceedings.iclr.cc/paper_files/paper/2025/file/7a0f8055c838df8e62329a76c7c6403d-Paper-Conference.pdf)
  - [Evaluating the Effectiveness and Scalability of LLM-Based Data Augmentation for Retrieval](https://aclanthology.org/2025.emnlp-main.888.pdf)
  - [Randomly Removing 50% of Dimensions in Text Embeddings has Minimal Impact on Retrieval and Classification Tasks](https://aclanthology.org/2025.emnlp-main.1410.pdf)
- **MTEB** (measurement instrument): *measured_by*, 4 papers
  > We evaluate 13 representative retrieval models, ranging from traditional bag-of-words models to large dense retrieval models, including the top performers from the retrieval set of the MTEB leaderboard (Muennighoff et al., 2023), BEIR (Thakur et al., 2021). (Section 4.1)
  - [BRIGHT: A Realistic and Challenging Benchmark for Reasoning-Intensive Retrieval](https://proceedings.iclr.cc/paper_files/paper/2025/file/7a0f8055c838df8e62329a76c7c6403d-Paper-Conference.pdf)
  - [Repetition Improves Language Model Embeddings](https://proceedings.iclr.cc/paper_files/paper/2025/file/e9b0c9480b03f9a6bca24ed8c08ee058-Paper-Conference.pdf)
  - [Conan-Embedding-v2: Training an LLM from Scratch for Text Embeddings](https://aclanthology.org/2025.emnlp-main.758.pdf)
  - [Time-Reversal Provides Unsupervised Feedback to LLMs](https://proceedings.neurips.cc/paper_files/paper/2024/file/34aec5ab2f99a8f592e0cca4974013f2-Paper-Conference.pdf)
- **Tool use** (behavioral indicator): *causes*, 2 papers
  > Recently, the focus has shifted towards the use of retrievers to effectively support LLMs in the tool selection process (Section 1).
  - [PORTS: Preference-Optimized Retrievers for Tool Selection with Large Language Models](https://aclanthology.org/2025.emnlp-main.507.pdf)
  - [EASYTOOL: Enhancing LLM-based Agents with Concise Tool Instruction](https://aclanthology.org/2025.naacl-long.44.pdf)
- **MS MARCO** (measurement instrument): *measured_by*, 1 paper
  > To evaluate the model’s robustness in non-Wikipedia scenarios where high-quality text and titles are not available, we conduct experiments on a subset of MS MARCO [3]
  - [Self-Retrieval: End-to-End Information Retrieval with One Large Language Model](https://proceedings.neurips.cc/paper_files/paper/2024/file/741ad162ab0f3da6f9aad60e9e34f5f1-Paper-Conference.pdf)
- **SlideVQA** (measurement instrument): *measured_by*, 1 paper
  > We first evaluate the retrieval accuracy of the Col-retrieval module within SV-RAG and compare it with several baselines on SlideVQA (Tanaka et al., 2023), MM-LongBench (Ma et al., 2024d), DUDE (Van Landeghem et al., 2023), DocVQA (Mathew et al., 2020; 2021) and VisR-Bench. (Section 5)
  - [SV-RAG: LoRA-Contextualizing Adaptation of MLLMs for Long Document Understanding](https://proceedings.iclr.cc/paper_files/paper/2025/file/0d40c7b4d78bf7f08ba532542818f6c0-Paper-Conference.pdf)
- **Flickr30k Entities** (measurement instrument): *measured_by*, 1 paper
  > We further experiment on FLICKR30K ENTITIES [35], an image retrieval dataset of 30k images with annotated bounding boxes and descriptive phrases (Appendix A). (Section 5.2).
  - [AvaTaR: Optimizing LLM Agents for Tool Usage via Contrastive Reasoning](https://proceedings.neurips.cc/paper_files/paper/2024/file/2db8ce969b000fe0b3fb172490c33ce8-Paper-Conference.pdf)
- **Natural Questions** (measurement instrument): *measured_by*, 1 paper
  > We conduct main experiments on Natural Questions (NQ) [21] and TriviaQA [18] datasets, both of which are widely used retrieval benchmarks... We use passage-level Hits@{1, 5} and Mean Reciprocal Rank (MRR)@5 as evaluation metrics.
  - [Self-Retrieval: End-to-End Information Retrieval with One Large Language Model](https://proceedings.neurips.cc/paper_files/paper/2024/file/741ad162ab0f3da6f9aad60e9e34f5f1-Paper-Conference.pdf)
- **TriviaQA** (measurement instrument): *measured_by*, 1 paper
  > We conduct main experiments on Natural Questions (NQ) [21] and TriviaQA [18] datasets, both of which are widely used retrieval benchmarks... We use passage-level Hits@{1, 5} and Mean Reciprocal Rank (MRR)@5 as evaluation metrics.
  - [Self-Retrieval: End-to-End Information Retrieval with One Large Language Model](https://proceedings.neurips.cc/paper_files/paper/2024/file/741ad162ab0f3da6f9aad60e9e34f5f1-Paper-Conference.pdf)
- **Interpretability and explainability** (construct): *causes*, 1 paper
  > This approach also allows us to enhance explainability by returning the retrieved subgraph. (Section 5)
  - [G-Retriever: Retrieval-Augmented Generation for Textual Graph Understanding and Question Answering](https://proceedings.neurips.cc/paper_files/paper/2024/file/efaf1c9726648c8ba363a5c927440529-Paper-Conference.pdf)
- **BABILong** (measurement instrument): *measured_by*, 1 paper
  > "We experiment with two options: (1) retrieval by chunks of size 512 tokens, denoted RAG-C and (2) retrieval by sentences, called RAG-S."
  - [BABILong: Testing the Limits of LLMs with Long Context Reasoning-in-a-Haystack](https://proceedings.neurips.cc/paper_files/paper/2024/file/c0d62e70dbc659cc9bd44cbcf1cb652f-Paper-Datasets_and_Benchmarks_Track.pdf)
- **LongBench** (measurement instrument): *measured_by*, 1 paper
  > EM-LLMS (surprise only) vs. RAG (NV-Embed-v2 retriever) vs. full-context, with LLaMA- 3.1-8B as the base LLM, evaluated on LongBench (Figure 1).
  - [Human-inspired Episodic Memory for Infinite Context LLMs](https://proceedings.iclr.cc/paper_files/paper/2025/file/c05144b635df16ac9bbf8246bbbd55ca-Paper-Conference.pdf)
- **AIR-Bench (information retrieval)** (measurement instrument): *measured_by*, 1 paper
  > Additionally, it secured the highest scores in Long Doc section and the second scores in QA section on the AIR-Benchmark which covers a range of out-of-domain information retrieval topics beyond those in MTEB. (Section 1)
  - [NV-Embed: Improved Techniques for Training LLMs as Generalist Embedding Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/c4bf73386022473a652a18941e9ea6f8-Paper-Conference.pdf)
- **DocVQA** (measurement instrument): *measured_by*, 1 paper
  > We first evaluate the retrieval accuracy of the Col-retrieval module within SV-RAG and compare it with several baselines on SlideVQA (Tanaka et al., 2023), MM-LongBench (Ma et al., 2024d), DUDE (Van Landeghem et al., 2023), DocVQA (Mathew et al., 2020; 2021) and VisR-Bench. (Section 5)
  - [SV-RAG: LoRA-Contextualizing Adaptation of MLLMs for Long Document Understanding](https://proceedings.iclr.cc/paper_files/paper/2025/file/0d40c7b4d78bf7f08ba532542818f6c0-Paper-Conference.pdf)
- **SQuAD 2.0** (measurement instrument): *measured_by*, 1 paper
  > Document Retrieval In this task the model receives a query and Ndocs randomly assorted documents, and its objective is to return the id of the matching document. Our data is sampled from SQuAD v2 (Rajpurkar et al., 2018). (Section 5)
  - [DeciMamba: Exploring the Length Extrapolation Potential of Mamba](https://proceedings.iclr.cc/paper_files/paper/2025/file/fae0a4535196bf7715c1aef2ccfe283f-Paper-Conference.pdf)
- **Autoformalization** (behavioral indicator): *causes*, 1 paper
  > RAutoformalizer uses the retrievals to enhance autoformalization.
  - [Rethinking and Improving Autoformalization: Towards a Faithful Metric and a Dependency Retrieval-based Approach](https://proceedings.iclr.cc/paper_files/paper/2025/file/d630537fc4402cfa3ebbc7450a0cac91-Paper-Conference.pdf)
- **InfiniteBench** (measurement instrument): *measured_by*, 1 paper
  > Table 3: NAMMs evaluation on InfiniteBench. Model/Task name Retrieval
  - [An Evolved Universal Transformer Memory](https://proceedings.iclr.cc/paper_files/paper/2025/file/da85790fb1cb4f11f431648455c561b5-Paper-Conference.pdf)
- **ToolBench** (measurement instrument): *measured_by*, 1 paper
  > Our experiments are based on ToolBench, a real-world tool benchmark containing more 16k tool collections... Our retrieval and end-to-end agent-tuning data are converted from the original data in ToolBench. (Section 4.1)
  - [ToolGen: Unified Tool Retrieval and Calling via Generation](https://proceedings.iclr.cc/paper_files/paper/2025/file/b646bdebeb87dfafe2c6f77a63b564e1-Paper-Conference.pdf)
- **MuirBench** (measurement instrument): *measured_by*, 1 paper
  > [VISUAL RETRIEVAL] aims to evaluate the ability of models to retrieval images that contain the same building. (Section 3.1)
  - [MuirBench: A Comprehensive Benchmark for Robust Multi-image Understanding](https://proceedings.iclr.cc/paper_files/paper/2025/file/9cf6139382f98623d08cc595622f3fb1-Paper-Conference.pdf)
- **Multi-table reasoning** (construct): *causes*, 1 paper
  > This task is fundamental because in the real-world scenario, the subsequent steps of reasoning and answering performance are based on the quality of the retrieved tables.
  - [MMQA: Evaluating LLMs with Multi-Table Multi-Hop Complex Questions](https://proceedings.iclr.cc/paper_files/paper/2025/file/794a425a2e47e05d29d30f79b79a692d-Paper-Conference.pdf)
- **FLEURS-ASL** (measurement instrument): *measured_by*, 1 paper
  > FLEURS-ASL can be used to evaluate a variety of tasks—... in principle caption alignment, retrieval, and multiple-choice receptive comprehension (Section 1)
  - [FLEURS-ASL: Including American Sign Language in Massively Multilingual Multitask Evaluation](https://aclanthology.org/2025.naacl-long.314.pdf)
- **MP-DocVQA** (measurement instrument): *measured_by*, 1 paper
  > We employ question-document pairs from various VQA datasets, each targeting distinct document types: MP-DocVQA (Tito et al., 2023) for industrial documents, ArXivQA (Li et al., 2024), ChartQA (Masry et al., 2022), InfographicsVQA (Mathew et al., 2022), and PlotQA (Methani et al., 2020) for different types of figures, as well as SlideVQA (Tanaka et al., 2023) for presentation slides. (Section 3.1)
  - [Unveil: Unified Visual-Textual Integration and Distillation for Multi-modal Document Retrieval](https://aclanthology.org/2025.acl-long.1166.pdf)
- **ArXivQA** (measurement instrument): *measured_by*, 1 paper
  > We employ question-document pairs from various VQA datasets, each targeting distinct document types: MP-DocVQA (Tito et al., 2023) for industrial documents, ArXivQA (Li et al., 2024), ChartQA (Masry et al., 2022), InfographicsVQA (Mathew et al., 2022), and PlotQA (Methani et al., 2020) for different types of figures, as well as SlideVQA (Tanaka et al., 2023) for presentation slides. (Section 3.1)
  - [Unveil: Unified Visual-Textual Integration and Distillation for Multi-modal Document Retrieval](https://aclanthology.org/2025.acl-long.1166.pdf)
- **ChartQA** (measurement instrument): *measured_by*, 1 paper
  > We employ question-document pairs from various VQA datasets, each targeting distinct document types: MP-DocVQA (Tito et al., 2023) for industrial documents, ArXivQA (Li et al., 2024), ChartQA (Masry et al., 2022), InfographicsVQA (Mathew et al., 2022), and PlotQA (Methani et al., 2020) for different types of figures, as well as SlideVQA (Tanaka et al., 2023) for presentation slides. (Section 3.1)
  - [Unveil: Unified Visual-Textual Integration and Distillation for Multi-modal Document Retrieval](https://aclanthology.org/2025.acl-long.1166.pdf)
- **LOFT** (measurement instrument): *measured_by*, 1 paper
  > “LOFT (7 retrieval tasks including argumentative retrieval, fact-checking, web search, multi-hop reasoning QA, etc)”
  - [LongRoPE2: Near-Lossless LLM Context Window Scaling](https://raw.githubusercontent.com/mlresearch/v267/main/assets/shang25a/shang25a.pdf)
- **Needle-in-a-Haystack** (measurement instrument): *measured_by*, 1 paper
  > To investigate whether the LOGO training strategy affects the information retrieval capabilities of LCMs, we conduct a Needle-in-a-Haystack (NIAH) testing (gkamradt, 2023). (Section 4.2)
  - [LOGO — Long cOntext aliGnment via efficient preference Optimization](https://raw.githubusercontent.com/mlresearch/v267/main/assets/tang25j/tang25j.pdf)
- **RULER** (measurement instrument): *measured_by*, 1 paper
  > RULER (Hsieh et al., 2024) is a suite of synthetically created tasks with controllable lengths, which ranges from retrieval, multi-hop tracking, real QA datasets, and context aggregation tasks. (Section 4.5)
  - [Speculative Prefill: Turbocharging TTFT with Lightweight and Training-Free Token Importance Estimation](https://raw.githubusercontent.com/mlresearch/v267/main/assets/liu25g/liu25g.pdf)
- **ViDoSeek** (measurement instrument): *measured_by*, 1 paper
  > Experimental results for the zero-shot closed-domain, multimodal document retrieval task on VidoSeek (Wang et al., 2025) and REAL-MM-RAG (Wasserman et al., 2025) (Table 1).
  - [Zero-shot Multimodal Document Retrieval via Cross-modal Question Generation](https://aclanthology.org/2025.emnlp-main.1324.pdf)
- **Real-MM-RAG** (measurement instrument): *measured_by*, 1 paper
  > Experimental results for the zero-shot closed-domain, multimodal document retrieval task on VidoSeek (Wang et al., 2025) and REAL-MM-RAG (Wasserman et al., 2025) (Table 1).
  - [Zero-shot Multimodal Document Retrieval via Cross-modal Question Generation](https://aclanthology.org/2025.emnlp-main.1324.pdf)
- **SQuAD v1.1** (measurement instrument): *measured_by*, 1 paper
  > Experimental results across four datasets—Dragonball, SQUAD, NFCORPUS, and SCI-DOCS demonstrate that SAKI-RAG achieves better recall and precision compared to other RAG frameworks in long-document retrieval scenarios (Abstract).
  - [SAKI-RAG: Mitigating Context Fragmentation in Long-Document RAG via Sentence-level Attention Knowledge Integration](https://aclanthology.org/2025.emnlp-main.63.pdf)
- **NFCorpus** (measurement instrument): *measured_by*, 1 paper
  > Experimental results across four datasets—Dragonball, SQUAD, NFCORPUS, and SCI-DOCS demonstrate that SAKI-RAG achieves better recall and precision compared to other RAG frameworks in long-document retrieval scenarios (Abstract).
  - [SAKI-RAG: Mitigating Context Fragmentation in Long-Document RAG via Sentence-level Attention Knowledge Integration](https://aclanthology.org/2025.emnlp-main.63.pdf)
- **Cross-lingual alignment** (construct): *causes*, 1 paper
  > we propose a cross-lingual retrieval dataset (CLR), which integrates representations across different languages through cross-lingual search, thereby narrowing the representation gap between them. (Section 3.3)
  - [Conan-Embedding-v2: Training an LLM from Scratch for Text Embeddings](https://aclanthology.org/2025.emnlp-main.758.pdf)
- **IMPLIRET** (measurement instrument): *measured_by*, 1 paper
  > IMPLIRET: Benchmarking the Implicit Fact Retrieval Challenge (Title).
  - [ImpliRet: Benchmarking the Implicit Fact Retrieval Challenge](https://aclanthology.org/2025.emnlp-main.1685.pdf)
- **Factual grounding** (construct): *causes*, 1 paper
  > Additionally, our reconstruction strategy uses retrieval-augmented generation to enhance factual grounding and reduce hallucination. (Limitations)
  - [Uncovering Argumentative Flow: A Question-Focus Discourse Structuring Framework](https://aclanthology.org/2025.emnlp-main.416.pdf)
- **MKQA** (measurement instrument): *measured_by*, 1 paper
  > “To evaluate cross-lingual retrieval performance, we conducted comprehensive experiments using the Multilingual Knowledge Questions & Answers (MKQA) benchmark”
  - [Conan-Embedding-v2: Training an LLM from Scratch for Text Embeddings](https://aclanthology.org/2025.emnlp-main.758.pdf)
- **MLDR** (measurement instrument): *measured_by*, 1 paper
  > Following Warner et al. (2024), we evaluate long-context performance using the English subset of MLDR (Chen et al., 2024), a retrieval benchmark consisting of over 200,000 long documents. (Section 5.5)
  - [Context-aware Biases for Length Extrapolation](https://aclanthology.org/2025.emnlp-main.1545.pdf)
- **TableEval** (measurement instrument): *measured_by*, 1 paper
  > This approach accommodates various task types within diverse real-world industrial scenarios, including information retrieval, numerical analysis, table reasoning, data analysis, multi-turn dialogue, and understanding of table structures. (Section 3.1)
  - [TableEval: A Real-World Benchmark for Complex, Multilingual, and Multi-Structured Table Question Answering](https://aclanthology.org/2025.emnlp-main.363.pdf)
- **MIRACL** (measurement instrument): *measured_by*, 1 paper
  > Recent efforts include the development of multilingual and cross-lingual IR resources, such as Mr. TyDi (Zhang et al., 2021), MIRACL (Zhang et al., 2023) and CIRAL (Adeyemi et al., 2024)... (Section 4.3)
  - [Charting the Landscape of African NLP: Mapping Progress and Shaping the Road Ahead](https://aclanthology.org/2025.emnlp-main.1414.pdf)

### → Information retrieval
- **Query rewriting** (behavioral indicator): *causes*, 3 papers
  > We find that using this rephrased query in retrieval drastically boosts the aesthetic quality more than we ever expected.
  - [Aligning Vision Models with Human Aesthetics in Retrieval: Benchmarks and Algorithms](https://proceedings.neurips.cc/paper_files/paper/2024/file/9d3faa41886997cfc2128b930077fa49-Paper-Conference.pdf)
  - [ReSCORE: Label-free Iterative Retriever Training for Multi-hop Question Answering with Relevance-Consistency Supervision](https://aclanthology.org/2025.acl-long.16.pdf)
  - [LinkAlign: Scalable Schema Linking for Real-World Large-Scale Multi-Database Text-to-SQL](https://aclanthology.org/2025.emnlp-main.51.pdf)
- **Question decomposition** (behavioral indicator): *causes*, 1 paper
  > QD provides noticeable improvements over MTR on multi-table retrieval tasks, for instance, in Top-2 retrieval, precision is improved from 65.3 to 72.3 and recall is improved from 62.3 to 64.7 in the 2-table subset. (Section 4.2)
  - [MMQA: Evaluating LLMs with Multi-Table Multi-Hop Complex Questions](https://proceedings.iclr.cc/paper_files/paper/2025/file/794a425a2e47e05d29d30f79b79a692d-Paper-Conference.pdf)
- **Semantic understanding** (construct): *causes*, 1 paper
  > To build semantic index for files in the LSFS, we leverage an a lightweight embedding model, i.e., all-MiniLM-L6-v2 (Reimers & Gurevych, 2019), commonly used in vector databases, thereby supporting more advanced file operations which requires semantic understanding of file content. (Section 3)
  - [From Commands to Prompts: LLM-based Semantic File System for AIOS](https://proceedings.iclr.cc/paper_files/paper/2025/file/517eb19e99947f60afff0cf93e451825-Paper-Conference.pdf)
- **Relevance** (construct): *causes*, 1 paper
  > By explicitly modeling both consistency and relevance, our method trains a retriever to retrieve the documents necessary for answering a given question. (Section 3.2)
  - [ReSCORE: Label-free Iterative Retriever Training for Multi-hop Question Answering with Relevance-Consistency Supervision](https://aclanthology.org/2025.acl-long.16.pdf)
- **Consistency** (construct): *causes*, 1 paper
  > By explicitly modeling both consistency and relevance, our method trains a retriever to retrieve the documents necessary for answering a given question. (Section 3.2)
  - [ReSCORE: Label-free Iterative Retriever Training for Multi-hop Question Answering with Relevance-Consistency Supervision](https://aclanthology.org/2025.acl-long.16.pdf)
- **Answer generation** (behavioral indicator): *correlates*, 1 paper
  > While the correlation is not very strong (up to r = 0.42), it confirms that with increased retrieval performance, the generation improves (Salemi and Zamani, 2024).
  - [PeerQA: A Scientific Question Answering Dataset from Peer Reviews](https://aclanthology.org/2025.naacl-long.22.pdf)
- **Relation extraction** (behavioral indicator): *causes*, 1 paper
  > KiRAG decomposes documents into knowledge triples and performs iterative retrieval with these triples to enable a factually reliable retrieval process. (Abstract)
  - [KiRAG: Knowledge-Driven Iterative Retriever for Enhancing Retrieval-Augmented Generation](https://aclanthology.org/2025.acl-long.929.pdf)

### Associated with
- **Fact checking** (behavioral indicator), 2 papers
  > Most recent works typically divide the fact verification task into two stages. The first stage retrieves a relatively small subset of evidence from a knowledge source (e.g. a knowledge graph) that is relevant to verify a given claim. (Section 2)
  - [Unsupervised Pretraining for Fact Verification by Language Model Distillation](https://proceedings.iclr.cc/paper_files/paper/2024/file/238c98450b1d9e8055f94d22f303bb57-Paper-Conference.pdf)
  - [DEFAME: Dynamic Evidence-based FAct-checking with Multimodal Experts](https://raw.githubusercontent.com/mlresearch/v267/main/assets/braun25b/braun25b.pdf)
- **Memory management** (construct), 1 paper
  > “Memory management involves integrating and analyzing content from internal memory” and “Memory Retriever. Given the question q and the assistant’s memory M, the memory retriever retrieves historically relevant memories”
  - [Boosting the Potential of Large Language Models with an Intelligent Information Assistant](https://proceedings.neurips.cc/paper_files/paper/2024/file/28d38c036365420f61ce03300418e44a-Paper-Conference.pdf)
- **Factual recall** (behavioral indicator), 1 paper
  > The two-stage theory states that the process of memory recall begins with a search and retrieval process, and then a decision or recognition process where the correct information is chosen from what has been retrieved (Bahrick, 1970; Watkins and Gardiner, 1979). (Section 2.1)
  - [MADial-Bench: Towards Real-world Evaluation of Memory-Augmented Dialogue Generation](https://aclanthology.org/2025.naacl-long.499.pdf)
- **Temporal grounding** (behavioral indicator), 1 paper
  > Temporal Grounding. Accurately identify and retrieve/extract the relevant set of tables necessary to answer the question. This can be regarded as retrieval over temporal information.
  - [TRANSIENTTABLES: Evaluating LLMs' Reasoning on Temporally Evolving Semi-structured Tables](https://aclanthology.org/2025.naacl-long.332.pdf)
- **Schema linking** (behavioral indicator), 1 paper
  > Through error analysis, we identify two major challenges in schema linking: (1) Database Retrieval: accurately selecting the target database from a large schema pool, while effectively filtering out irrelevant ones
  - [LinkAlign: Scalable Schema Linking for Real-World Large-Scale Multi-Database Text-to-SQL](https://aclanthology.org/2025.emnlp-main.51.pdf)
- **Task decomposition** (behavioral indicator), 1 paper
  > "we decompose the retrieval into three sub-processes, including problem decomposition, single-constraint resolution, and context merging."
  - [DRoC: Elevating Large Language Models for Complex Vehicle Routing via Decomposed Retrieval of Constraints](https://proceedings.iclr.cc/paper_files/paper/2025/file/73d6c3e4b214deebbbf8256e26d2cf45-Paper-Conference.pdf)
- **Named entity recognition** (behavioral indicator), 1 paper
  > Information Retrieval. Effective search functionality is essential in SNS. Models should interpret query intent and retrieve relevant information from large datasets, delivering the most accurate results. Tasks: (3) Note-NER. Extracts named entities from note content.
  - [SNS-Bench: Defining, Building, and Assessing Capabilities of Large Language Models in Social Networking Services](https://raw.githubusercontent.com/mlresearch/v267/main/assets/guo25o/guo25o.pdf)
