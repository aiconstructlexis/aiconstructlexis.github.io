# Information extraction
**Type:** Behavioral indicator  
**Supporting papers:** 144  
**Also known as:** Attribute value extraction, Object entity extraction, Source/sink extraction, Attribute extraction, Patient attribute extraction, Observation extraction, Entity extraction, Slot filling, Numerical answer extraction, Key answer extraction, Choice identification, Proposition extraction, Keyword extraction, Atomic proposition grounding, Frequent words extraction, Knowledge extraction, Cognitive pathway extraction, Schema extraction, Symptom extraction, Value extraction, Argument component identification, Value identification, Feature extraction from text, Fine-grained semantic extraction, Aspect extraction, Unstructured evidence extraction, Emotion-cause annotation, Emotion-cause extraction, Attentional focus extraction, Clinical finding extraction, Factual assertion extraction, Candidate extraction, Edge extraction, Node extraction, Property extraction, Sticker extraction, Constraint type extraction, Constraint extraction, Content extraction, Topic extraction, Graph structure extraction, Evidence extraction, Promise extraction, Reference extraction, Inorganic synthesis recipe extraction, Key-fact extraction, Causal tree extraction, Cause-effect span extraction, Frame-semantic argument extraction, Knowledge slice extraction, Numeric data extraction, Nested field extraction, Parallel term extraction, Spatial primitive extraction, Information Extraction, Table extraction, Implicit target extraction, Text extraction, Character relationship extraction, Clinical entity extraction, Contextual parameter identification, Legal element recognition, Legal relation extraction, Relation analysis, Relation mining, Structured information extraction, Slot-filling, Emotion cause extraction  

## State of the Field

**Space of definitions.** Most definitions treat this behavior as identifying and extracting structured information from unstructured text, commonly as facts, entities, relations, events, values, or other structured outputs. Closely related formulations extend the source material to semi-structured documents, tables, charts, audio, webpages, and images, but keep the same basic criterion: the model must isolate the relevant content from a larger input. Papers differ mainly in what must be returned, with some requiring direct attribute or evidence selection, some span copying, and others structured outputs such as triples, JSON objects, schemas, or causal trees.

**Variants.** A recurring set of narrower names includes slot filling, entity extraction, attribute or value extraction, proposition extraction, and evidence or promise span extraction, alongside many other task-specific forms. Papers study these forms in visually rich documents and receipts, tables and scientific articles, charts and audio, clinical notes and legal texts, webpages and dialogue, and diagram-like inputs where nodes, edges, schemas, or graph structure are extracted. A smaller line treats the behavior as interactive acquisition, where an interviewer is rewarded for obtaining more information items from a source, or as direct table-attribute extraction without full table retrieval.

**Space of elicitation and scores.** Papers link this behavior to 11 measurement instruments. The most frequently linked are SLURP, T-REx, ZsRE, FUNSD, and Human evaluation; these are mostly datasets or benchmarks for slot filling and information extraction, with additional linked instruments covering audio understanding, long-term memory, dialogue, scientific relation extraction, and visually rich documents. A smaller measurement line uses human evaluation rather than a benchmark dataset.

**What it is taken as evidence of.** Papers link this behavior to 7 constructs, with reasoning appearing first among the recorded links. Some papers claim a causal relationship from information extraction to reasoning, describing extracted knowledge as contributing to the path from a question to its answer, and another paper claims a causal relationship from information extraction to hallucination resistance by focusing on relevant table cells to reduce hallucinations in reasoning. Other papers record it as related to long-context understanding, long-term memory, and spatial reasoning, with additional related construct links also present, so the construct framing is mixed rather than uniform.

## Sources

**Information extraction** (10 papers: [Achieving Human Parity in Content-Grounded Datasets Generation](https://proceedings.iclr.cc/paper_files/paper/2024/file/a774503daed55eb53c634847ae071ec7-Paper-Conference.pdf), [Hybrid LLM: Cost-Efficient and Quality-Aware Query Routing](https://proceedings.iclr.cc/paper_files/paper/2024/file/b47d93c99fa22ac0b377578af0a1f63a-Paper-Conference.pdf), [CharXiv: Charting Gaps in Realistic Chart Understanding in Multimodal LLMs](https://proceedings.neurips.cc/paper_files/paper/2024/file/cdf6f8e9fd9aeaf79b6024caec24f15b-Paper-Datasets_and_Benchmarks_Track.pdf), [CURIE: Evaluating LLMs on Multitask Scientific Long-Context Understanding and Reasoning](https://proceedings.iclr.cc/paper_files/paper/2025/file/1ae4999aefb509d75d8608e07280922c-Paper-Conference.pdf), [Audio Flamingo 2: An Audio-Language Model with Long-Audio Understanding and Expert Reasoning Abilities](https://raw.githubusercontent.com/mlresearch/v267/main/assets/ghosh25b/ghosh25b.pdf), [DeepResearcher: Scaling Deep Research via Reinforcement Learning in Real-world Environments](https://aclanthology.org/2025.emnlp-main.22.pdf), [Information Extraction from Visually Rich Documents using LLM-based Organization of Documents into Independent Textual Segments](https://aclanthology.org/2025.acl-long.844.pdf), [NewsInterview: a Dataset and a Playground to Evaluate LLMs' Grounding Gap via Informational Interviews](https://aclanthology.org/2025.acl-long.1580.pdf), [Towards Robust Universal Information Extraction: Dataset, Evaluation, and Solution](https://aclanthology.org/2025.acl-long.1360.pdf), [Label Drop for Multi-Aspect Relation Modeling in Universal Information Extraction](https://aclanthology.org/2025.naacl-long.259.pdf))
> The task of identifying and extracting structured information from unstructured text.

**Attribute value extraction** (1 paper: [Shopping MMLU: A Massive Multi-Task Online Shopping Benchmark for Large Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/2049d75dd13db049897562bcf7d59da8-Paper-Datasets_and_Benchmarks_Track.pdf))
> The task of identifying and extracting the value of a specific attribute from product metadata.

**Object entity extraction** (1 paper: [Image Textualization: An Automatic Framework for Generating Rich and Detailed Image Descriptions](https://proceedings.neurips.cc/paper_files/paper/2024/file/c37d94c04effc86d72ab2258ba9b76c7-Paper-Datasets_and_Benchmarks_Track.pdf))
> The task of identifying and extracting noun phrases that refer to objects from a given textual description.

**Source/sink extraction** (1 paper: [LLMDFA: Analyzing Dataflow in Code with Large Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/ed9dcde1eb9c597f68c1d375bbecf3fc-Paper-Conference.pdf))
> Identifying program variables or expressions that serve as designated starting points and endpoints for dataflow analysis.

**Attribute extraction** (2 papers: [MO-DDN: A Coarse-to-Fine Attribute-based Exploration Agent for Multi-Object Demand-driven Navigation](https://proceedings.neurips.cc/paper_files/paper/2024/file/7565f036ceb20a2c74d341bfaa9fffad-Paper-Conference.pdf), [LLM-Driven Completeness and Consistency Evaluation for Cultural Heritage Data Augmentation in Cross-Modal Retrieval](https://aclanthology.org/2025.emnlp-main.980.pdf))
> The observable action of identifying and listing semantic attributes for instructions or objects via prompting.

**Patient attribute extraction** (1 paper: [MedCalc-Bench: Evaluating Large Language Models for Medical Calculations](https://proceedings.neurips.cc/paper_files/paper/2024/file/99e81750f3fdfcaf9613db2dbf4bd623-Paper-Datasets_and_Benchmarks_Track.pdf))
> Extracting relevant numerical or categorical values from a long patient note for use in a calculation.

**Observation extraction** (1 paper: [DiReCT: Diagnostic Reasoning for Clinical Notes via Large Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/892850bf793e03b5c410dfd9425b94c8-Paper-Datasets_and_Benchmarks_Track.pdf))
> The task of identifying and extracting specific text spans from a clinical note that serve as evidence (observations) for a particular diagnostic conclusion.

**Entity extraction** (2 papers: [Reasoning of Large Language Models over Knowledge Graphs with Super-Relations](https://proceedings.iclr.cc/paper_files/paper/2025/file/0c6799a1a5db47be8864fed46ba77697-Paper-Conference.pdf), [Can LLMs be Good Graph Judge for Knowledge Graph Construction?](https://aclanthology.org/2025.emnlp-main.554.pdf))
> Identifying entities at the end of a reasoning path that may serve as candidate answers.

**Slot filling** (1 paper: [RAG-DDR: Optimizing Retrieval-Augmented Generation Using Differentiable Data Rewards](https://proceedings.iclr.cc/paper_files/paper/2025/file/1a87980b9853e84dfb295855b425c262-Paper-Conference.pdf))
> The task of identifying and extracting specific, predefined types of information (slots) from unstructured text.

**Numerical answer extraction** (1 paper: [OptiBench Meets ReSocratic: Measure and Improve LLMs for Optimization Modeling](https://proceedings.iclr.cc/paper_files/paper/2025/file/3deb687c44d3687ace0729e5db3b4efd-Paper-Conference.pdf))
> The task of parsing the output of an executed code solver to identify and report the specific numerical values for decision variables and the objective function.

**Key answer extraction** (1 paper: [xFinder: Large Language Models as Automated Evaluators for Reliable Evaluation](https://proceedings.iclr.cc/paper_files/paper/2025/file/9602d22a8c791f23f8e4d1398e3fb5be-Paper-Conference.pdf))
> The observable task of identifying and isolating the specific, final answer from a model's potentially verbose or complex textual response.

**Choice identification** (1 paper: [Empowering Users in Digital Privacy Management through Interactive LLM-Based Agents](https://proceedings.iclr.cc/paper_files/paper/2025/file/bef8e5620c699630405adafaa86cb038-Paper-Conference.pdf))
> The observable task of identifying and extracting sections of a privacy policy that describe user choices or opt-out mechanisms.

**Proposition extraction** (2 papers: [SiReRAG: Indexing Similar and Related Information for Multihop Reasoning](https://proceedings.iclr.cc/paper_files/paper/2025/file/f9668d223e713943634dce9c66e8f2c1-Paper-Conference.pdf), [PropRAG: Guiding Retrieval with Beam Search over Proposition Paths](https://aclanthology.org/2025.emnlp-main.317.pdf))
> Identifying factual statements from text that capture important information, preferably about entities.

**Keyword extraction** (6 papers: [Unnatural Languages Are Not Bugs but Features for LLMs](https://raw.githubusercontent.com/mlresearch/v267/main/assets/duan25c/duan25c.pdf), [From Chat Logs to Collective Insights: Aggregative Question Answering](https://aclanthology.org/2025.emnlp-main.1667.pdf), [Hierarchical Level-Wise News Article Clustering via Multilingual Matryoshka Embeddings](https://aclanthology.org/2025.acl-long.124.pdf), [Making FETCH! Happen: Finding Emergent Dog Whistles Through Common Habitats](https://aclanthology.org/2025.acl-long.284.pdf), [Enhancing Small Medical Learners with Privacy-preserving Contextual Prompting](https://proceedings.iclr.cc/paper_files/paper/2024/file/79322f3668888f8f7fc99bbd98fbbaed-Paper-Conference.pdf), [VTechAGP: An Academic-to-General-Audience Text Paraphrase Dataset and Benchmark Models](https://aclanthology.org/2025.naacl-long.311.pdf))
> Identifying and retaining tokens from unnatural inputs that appear in the corresponding natural language version, while disregarding noise.

**Atomic proposition grounding** (1 paper: [Grammar-Forced Translation of Natural Language to Temporal Logic using LLMs](https://raw.githubusercontent.com/mlresearch/v267/main/assets/english25a/english25a.pdf))
> The process of identifying and extracting atomic predicates (state variables or events) from a natural language input as a pre-processing step for translation.

**Knowledge extraction** (3 papers: [Overtrained Language Models Are Harder to Fine-Tune](https://raw.githubusercontent.com/mlresearch/v267/main/assets/springer25a/springer25a.pdf), [Diagram-Driven Course Questions Generation](https://aclanthology.org/2025.emnlp-main.305.pdf), [Boosting the Potential of Large Language Models with an Intelligent Information Assistant](https://proceedings.neurips.cc/paper_files/paper/2024/file/28d38c036365420f61ce03300418e44a-Paper-Conference.pdf))
> The task of identifying and retrieving specific pieces of factual information from unstructured text.

**Frequent words extraction** (1 paper: [ShadowKV: KV Cache in Shadows for High-Throughput Long-Context LLM Inference](https://raw.githubusercontent.com/mlresearch/v267/main/assets/sun25b/sun25b.pdf))
> Identifying and extracting the most frequently occurring words from a given text.

**Cognitive pathway extraction** (1 paper: [MentalGLM Series: Explainable Large Language Models for Mental Health Analysis on Chinese Social Media](https://aclanthology.org/2025.emnlp-main.686.pdf))
> Extracting structured representations of cognitive-behavioral patterns from text, including triggering events, thoughts, emotions, and behavioral responses, based on CBT theory.

**Symptom extraction** (1 paper: [Knowledge-Aware Co-Reasoning for Multidisciplinary Collaboration](https://aclanthology.org/2025.emnlp-main.687.pdf))
> Identifying relevant symptom entities from a patient's natural language description for use in diagnostic reasoning.

**Schema extraction** (2 papers: [PPTAgent: Generating and Evaluating Presentations Beyond Text-to-Slides](https://aclanthology.org/2025.emnlp-main.728.pdf), [Track-SQL: Enhancing Generative Language Models with Dual-Extractive Modules for Schema and Context Tracking in Multi-turn Text-to-SQL](https://aclanthology.org/2025.naacl-long.536.pdf))
> The process of identifying and structuring the constituent elements of a slide into a defined format, including each element's category, description, and content.

**Value extraction** (1 paper: [From Scores to Steps: Diagnosing and Improving LLM Performance in Evidence-Based Medical Calculations](https://aclanthology.org/2025.emnlp-main.548.pdf))
> The model correctly identifies and extracts numerical and categorical variables (e.g., age, creatinine level) from clinical vignettes for use in calculations.

**Argument component identification** (1 paper: [Exploring Quality and Diversity in Synthetic Data Generation for Argument Mining](https://aclanthology.org/2025.emnlp-main.1351.pdf))
> The observable task of identifying a set of argument components in a text, where each component is defined by its start and end token indices and its type (e.g., 'Claim', 'Premise').

**Value identification** (1 paper: [SQUiD: Synthesizing Relational Databases from Unstructured Text](https://aclanthology.org/2025.emnlp-main.1629.pdf))
> Extracting relevant data values from text such as names, dates, and attributes, and organizing them into structured intermediate representations.

**Feature extraction from text** (1 paper: [Model-based Large Language Model Customization as Service](https://aclanthology.org/2025.emnlp-main.248.pdf))
> Identifying and converting named entities and values from unstructured natural language descriptions into structured feature vectors consistent with a predefined schema.

**Fine-grained semantic extraction** (1 paper: [LLM-Guided Semantic Relational Reasoning for Multimodal Intent Recognition](https://aclanthology.org/2025.emnlp-main.1130.pdf))
> Identifying detailed semantic cues such as actions, facial expressions, and interactions from multimodal inputs.

**Aspect extraction** (1 paper: [LaMP-QA: A Benchmark for Personalized Long-form Question Answering](https://aclanthology.org/2025.emnlp-main.60.pdf))
> Identifying and listing key information needs or expectations from a user's question narrative, used to form evaluation rubrics.

**Unstructured evidence extraction** (1 paper: [Unstructured Evidence Attribution for Long Context Query Focused Summarization](https://aclanthology.org/2025.emnlp-main.95.pdf))
> Copying arbitrary-length text spans from a long input context to serve as supporting evidence for summary sentences, without constraints on span boundaries such as sentence or paragraph limits.

**Emotion-cause extraction** (1 paper: [ECC: An Emotion-Cause Conversation Dataset for Empathy Response](https://aclanthology.org/2025.emnlp-main.306.pdf))
> Identifying the dialogue sentences that express the emotion and the sentences that express the cause.

**Emotion-cause annotation** (1 paper: [ECC: An Emotion-Cause Conversation Dataset for Empathy Response](https://aclanthology.org/2025.emnlp-main.306.pdf))
> The process of identifying and labeling utterances in a dialogue that express an emotion and its underlying cause, based on predefined seeds and contextual alignment.

**Attentional focus extraction** (1 paper: [Uncovering Argumentative Flow: A Question-Focus Discourse Structuring Framework](https://aclanthology.org/2025.emnlp-main.416.pdf))
> The process of identifying and listing key analytical aspects or dimensions emphasized in an argumentative unit, such as social groups or conceptual perspectives.

**Clinical finding extraction** (1 paper: [Structuring Radiology Reports: Challenging LLMs with Lightweight Models](https://aclanthology.org/2025.emnlp-main.392.pdf))
> Identifying and organizing relevant clinical observations (e.g., abnormalities, normal findings) under appropriate organ system categories in the Findings section.

**Factual assertion extraction** (1 paper: [Uncovering Argumentative Flow: A Question-Focus Discourse Structuring Framework](https://aclanthology.org/2025.emnlp-main.416.pdf))
> The task of identifying and extracting verifiable statements of fact from a source text.

**Candidate extraction** (1 paper: [Answering Narrative-Driven Recommendation Queries via a Retrieve–Rank Paradigm and the OCG-Agent](https://aclanthology.org/2025.emnlp-main.667.pdf))
> The behavior of identifying and extracting potential recommendation items from retrieved text fragments based on a structured template.

**Edge extraction** (1 paper: [Evaluating LLM-Generated Diagrams as Graphs](https://aclanthology.org/2025.emnlp-main.640.pdf))
> Detecting directed connections between diagram elements by analyzing visual cues such as arrows and lines, using vision-capable LLMs to infer logical flows.

**Node extraction** (2 papers: [Evaluating LLM-Generated Diagrams as Graphs](https://aclanthology.org/2025.emnlp-main.640.pdf), [Beyond End-to-End VLMs: Leveraging Intermediate Text Representations for Superior Flowchart Understanding](https://aclanthology.org/2025.naacl-long.180.pdf))
> Identifying and grouping text elements in an SVG diagram into coherent nodes, using spatial and semantic criteria, potentially refined with multimodal LLMs.

**Property extraction** (1 paper: [Facilitating Long Context Understanding via Supervised Chain-of-Thought Reasoning](https://aclanthology.org/2025.emnlp-main.615.pdf))
> Identifying key measurable metrics and their associated subjects from a query to support answering, such as 'revenue' and '<Company A>’s 2018 annual report'.

**Sticker extraction** (1 paper: [Sticker-TTS: Learn to Utilize Historical Experience with a Sticker-driven Test-Time Scaling Framework](https://aclanthology.org/2025.emnlp-main.621.pdf))
> Producing a structured summary of key conditions, strategies, and limitations from a prior reasoning trace to serve as a compact guide for future reasoning.

**Constraint type extraction** (1 paper: [ConstraintLLM: A Neuro-Symbolic Framework for Industrial-Level Constraint Programming](https://aclanthology.org/2025.emnlp-main.809.pdf))
> The observable process of identifying and classifying the specific types of constraints (e.g., AllDifferent, Cumulative) present in a natural language problem description.

**Constraint extraction** (1 paper: [PlanGEN: A Multi-Agent Framework for Generating Planning and Reasoning Trajectories for Complex Problem Solving](https://aclanthology.org/2025.emnlp-main.1042.pdf))
> Identifying the relevant rules, schedules, concepts, or other instance-specific requirements from a problem statement.

**Content extraction** (1 paper: [Web Intellectual Property at Risk: Preventing Unauthorized Real-Time Retrieval by Large Language Models](https://aclanthology.org/2025.emnlp-main.870.pdf))
> Parsing and extracting textual information from retrieved webpages, including visible elements and hidden source-code components.

**Topic extraction** (1 paper: [PychoAgent: Psychology-driven LLM Agents for Explainable Panic Prediction on Social Media during Sudden Disaster Events](https://aclanthology.org/2025.emnlp-main.865.pdf))
> The process of identifying and consolidating the main themes or subjects present in a user's historical posts.

**Graph structure extraction** (1 paper: [MA-GTS: A Multi-Agent Framework for Solving Complex Graph Problems in Real-World Applications](https://aclanthology.org/2025.emnlp-main.973.pdf))
> The task of identifying and parsing graph components like nodes, edges, and weights from unstructured or semi-structured text.

**Evidence extraction** (1 paper: [ML-Promise: A Multilingual Dataset for Corporate Promise Verification](https://aclanthology.org/2025.emnlp-main.1028.pdf))
> The task of extracting the specific text span corresponding to the evidence supporting a corporate promise from a document.

**Promise extraction** (1 paper: [ML-Promise: A Multilingual Dataset for Corporate Promise Verification](https://aclanthology.org/2025.emnlp-main.1028.pdf))
> The task of extracting the specific text span corresponding to a corporate promise from a document.

**Reference extraction** (1 paper: [InterIDEAS: Philosophical Intertextuality via LLMs](https://aclanthology.org/2025.emnlp-main.1180.pdf))
> Identifying and isolating mentions of people, texts, events, or ideas within philosophical writings, including both explicit and implicit references.

**Inorganic synthesis recipe extraction** (1 paper: [LLaMP: Large Language Model Made Powerful for High-fidelity Materials Knowledge Retrieval](https://aclanthology.org/2025.emnlp-main.1280.pdf))
> The task of extracting and summarizing step-by-step procedures for synthesizing inorganic materials from scientific literature.

**Key-fact extraction** (1 paper: [Towards a Holistic and Automated Evaluation Framework for Multi-Level Comprehension of LLMs in Book-Length Contexts](https://aclanthology.org/2025.emnlp-main.1241.pdf))
> Identifying and structuring central themes, supporting ideas, and fine-grained details from text segments into a hierarchical representation.

**Causal tree extraction** (1 paper: [Causal Tree Extraction from Medical Case Reports: A Novel Task for Experts-like Text Comprehension](https://aclanthology.org/2025.emnlp-main.1313.pdf))
> The task of generating a structured, multi-layered causal tree from an unstructured medical case report, where nodes are medical entities and edges represent causal or evidential relationships.

**Cause-effect span extraction** (1 paper: [A Multi-Level Benchmark for Causal Language Understanding in Social Media Discourse](https://aclanthology.org/2025.emnlp-main.1464.pdf))
> The task of identifying and labeling the specific text segments (spans) that correspond to the cause and the effect in a causal relationship.

**Knowledge slice extraction** (1 paper: [TaxoAlign: Scholarly Taxonomy Generation Using Language Models](https://aclanthology.org/2025.emnlp-main.1536.pdf))
> Identifying and extracting text segments from research papers that are highly relevant to a given taxonomy topic.

**Numeric data extraction** (1 paper: [Enhancing Study-Level Inference from Clinical Trial Papers via Reinforcement Learning-Based Numeric Reasoning](https://aclanthology.org/2025.emnlp-main.1544.pdf))
> The observable task of identifying and extracting specific numerical values, such as event counts or standard deviations, from unstructured text and presenting them in a structured format.

**Nested field extraction** (1 paper: [Beyond Human Labels: A Multi-Linguistic Auto-Generated Benchmark for Evaluating Large Language Models on Resume Parsing](https://aclanthology.org/2025.emnlp-main.1626.pdf))
> The specific task of extracting information from hierarchical or nested structures within a document, such as job roles within a work experience section.

**Parallel term extraction** (1 paper: [Translating Domain-Specific Terminology in Typologically-Diverse Languages: A Study in Tax and Financial Education](https://aclanthology.org/2025.emnlp-main.1774.pdf))
> The task of identifying and extracting the translation of a specific source term from a parallel text, which consists of a source sentence and its corresponding translation.

**Spatial primitive extraction** (1 paper: [FoREST: Frame of Reference Evaluation in Spatial Reasoning Tasks](https://aclanthology.org/2025.emnlp-main.1772.pdf))
> Identifying and outputting directional, topological, and distal spatial relations along with Frame of Reference from a spatial expression to support downstream reasoning tasks.

**Information Extraction** (1 paper: [TRANSIENTTABLES: Evaluating LLMs' Reasoning on Temporally Evolving Semi-structured Tables](https://aclanthology.org/2025.naacl-long.332.pdf))
> A two-stage evaluation method that tests a model's ability to directly extract relevant attributes from tables without full table retrieval, focusing on fine-grained evidence extraction.

**Table extraction** (1 paper: [SciLitLLM: How to Adapt LLMs for Scientific Literature Understanding](https://proceedings.iclr.cc/paper_files/paper/2025/file/8cb240de90aa20207db944c6c88a7cc0-Paper-Conference.pdf))
> Reading scientific text or tables and producing structured table-like information from the source content.

**Implicit target extraction** (1 paper: [LLM-Driven Implicit Target Augmentation and Fine-Grained Contextual Modeling for Zero-Shot and Few-Shot Stance Detection](https://aclanthology.org/2025.emnlp-main.299.pdf))
> The observable process of identifying targets not explicitly mentioned in the text but semantically implied, such as inferring 'democracy' as a target in a discussion about corporate regulation.

**Text extraction** (3 papers: [VisRAG: Vision-based Retrieval-augmented Generation on Multi-modality Documents](https://proceedings.iclr.cc/paper_files/paper/2025/file/3640a1997a4c9571cea9db2c82e1fc35-Paper-Conference.pdf), [Smoothie: Label Free Language Model Routing](https://proceedings.neurips.cc/paper_files/paper/2024/file/e6b57a990462df5afa58d64ce2709db9-Paper-Conference.pdf), [UFO: A UI-Focused Agent for Windows OS Interaction](https://aclanthology.org/2025.naacl-long.26.pdf))
> Converting visual text within document images into machine-readable text format.

**Character relationship extraction** (1 paper: [Agent-as-Judge for Factual Summarization of Long Narratives](https://aclanthology.org/2025.emnlp-main.1204.pdf))
> Identifying and representing subject-predicate-object triples that describe interactions, states, and roles among characters in a narrative.

**Clinical entity extraction** (1 paper: [CMedCalc-Bench: A Fine-Grained Benchmark for Chinese Medical Calculations in LLM](https://aclanthology.org/2025.emnlp-main.1302.pdf))
> Identifying relevant patient attributes, such as lab values, vital signs, or symptoms, from clinical notes.

**Contextual parameter identification** (1 paper: [Context Reasoner: Incentivizing Reasoning Capability for Contextualized Privacy and Safety Compliance via Reinforcement Learning](https://aclanthology.org/2025.emnlp-main.44.pdf))
> Correctly identifying elements of information flow such as sender, subject, recipient, and information type in a legal scenario based on contextual cues.

**Legal element recognition** (1 paper: [LexEval: A Comprehensive Chinese Legal Benchmark for Evaluating Large Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/2cb40fc022ca7bdc1a9a78b793661284-Paper-Datasets_and_Benchmarks_Track.pdf))
> Identifying the legal elements contained in a legal text from answer options.

**Legal relation extraction** (1 paper: [LexEval: A Comprehensive Chinese Legal Benchmark for Evaluating Large Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/2cb40fc022ca7bdc1a9a78b793661284-Paper-Datasets_and_Benchmarks_Track.pdf))
> Identifying and extracting specific types of legal relationship triples from a given legal text.

**Relation analysis** (1 paper: [Synthetic continued pretraining](https://proceedings.iclr.cc/paper_files/paper/2025/file/6dcf277ea32ce3288914faf369fe6de0-Paper-Conference.pdf))
> The task of describing the relationships between a given set of entities within the context of a source document.

**Relation mining** (1 paper: [Unified Parameter-Efficient Unlearning for LLMs](https://proceedings.iclr.cc/paper_files/paper/2025/file/8d537430e55a283a97e9b6e682e994a3-Paper-Conference.pdf))
> The observable task of identifying relationships between entities or concepts using Multimodal Large Language Models.

**Structured information extraction** (1 paper: [MatViX: Multimodal Information Extraction from Visually Rich Articles](https://aclanthology.org/2025.naacl-long.185.pdf))
> Producing structured JSON outputs that capture both material compositions and associated property data from full-length scientific articles containing text, tables, and figures.

**Slot-filling** (2 papers: [INJONGO: A Multicultural Intent Detection and Slot-filling Dataset for 16 African Languages](https://aclanthology.org/2025.acl-long.464.pdf), [Middle-Layer Representation Alignment for Cross-Lingual Transfer in Fine-Tuned LLMs](https://aclanthology.org/2025.acl-long.778.pdf))
> Extracting specific entities (slots) from a user utterance, such as amounts, locations, or dates, to support task execution in dialogue systems.

**Emotion cause extraction** (1 paper: [One Unified Model for Diverse Tasks: Emotion Cause Analysis via Self-Promote Cognitive Structure Modeling](https://aclanthology.org/2025.naacl-long.516.pdf))
> Identifying text clauses that describe events causing a specified emotion experienced by characters in the text.

## Relationships

### Information extraction →
- **T-REx** (measurement instrument): *measured_by*, 2 papers
  > two slot filling datasets: T-REx (ElSahar et al., 2018) and Zero-Shot RE (Petroni et al., 2021);
  - [Think-on-Graph: Deep and Responsible Reasoning of Large Language Model on Knowledge Graph](https://proceedings.iclr.cc/paper_files/paper/2024/file/10a6bdcabbd5a3d36b760daa295f63c1-Paper-Conference.pdf)
  - [A Theory for Token-Level Harmonization in Retrieval-Augmented Generation](https://proceedings.iclr.cc/paper_files/paper/2025/file/5a461bdff86cc07e976bb6c518810398-Paper-Conference.pdf)
- **ZsRE** (measurement instrument): *measured_by*, 2 papers
  > two slot filling datasets: T-REx (ElSahar et al., 2018) and Zero-Shot RE (Petroni et al., 2021);
  - [Think-on-Graph: Deep and Responsible Reasoning of Large Language Model on Knowledge Graph](https://proceedings.iclr.cc/paper_files/paper/2024/file/10a6bdcabbd5a3d36b760daa295f63c1-Paper-Conference.pdf)
  - [Think-on-Graph 2.0: Deep and Faithful Large Language Model Reasoning with Knowledge-guided Retrieval Augmented Generation](https://proceedings.iclr.cc/paper_files/paper/2025/file/830b1abc6d2da85f23d41169fa44d185-Paper-Conference.pdf)
- **SLURP** (measurement instrument): *measured_by*, 2 papers
  > “SF SLURP ...”
  - [SALMONN: Towards Generic Hearing Abilities for Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/476ab8f369e489c04187ba84f68cfa68-Paper-Conference.pdf)
  - [Bayesian WeakS-to-Strong from Text Classification to Generation](https://proceedings.iclr.cc/paper_files/paper/2025/file/495e55f361708bedbab5d81f92048dcd-Paper-Conference.pdf)
- **Reasoning** (construct): *causes*, 2 papers
  > The tasks of question decomposition, knowledge extraction, and note-taking are interconnected, each contributing towards navigating the reasoning path from a question to its answer.
  - [Boosting the Potential of Large Language Models with an Intelligent Information Assistant](https://proceedings.neurips.cc/paper_files/paper/2024/file/28d38c036365420f61ce03300418e44a-Paper-Conference.pdf)
  - [Visual Description Grounding Reduces Hallucinations and Boosts Reasoning in LVLMs](https://proceedings.iclr.cc/paper_files/paper/2025/file/a6805b5564bd8d813a81c4b5a97e5ca6-Paper-Conference.pdf)
- **SWDE** (measurement instrument): *measured_by*, 1 paper
  > we consider the following six recall-intensive tasks: information extraction tasks like FDA and SWDE (Arora et al., 2024a; 2023b; Wu et al., 2021; Deng et al., 2022) (Section 5.2)
  - [Longhorn: State Space Models are Amortized Online Learners](https://proceedings.iclr.cc/paper_files/paper/2025/file/ee0e45ff4de76cbfdf07015a7839f339-Paper-Conference.pdf)
- **MMAU** (measurement instrument): *measured_by*, 1 paper
  > “It includes information extraction1 and reasoning 2 questions”
  - [MMAU: A Massive Multi-Task Audio Understanding and Reasoning Benchmark](https://proceedings.iclr.cc/paper_files/paper/2025/file/d36f208919582785db965fe648b9fe59-Paper-Conference.pdf)
- **LongMemEval** (measurement instrument): *measured_by*, 1 paper
  > We introduce LONGMEMEVAL, a comprehensive benchmark designed to evaluate five core long-term memory abilities of chat assistants: information extraction, multi-session reasoning, temporal reasoning, knowledge updates, and abstention. (Abstract)
  - [LongMemEval: Benchmarking Chat Assistants on Long-Term Interactive Memory](https://proceedings.iclr.cc/paper_files/paper/2025/file/d813d324dbf0598bbdc9c8e79740ed01-Paper-Conference.pdf)
- **Hallucination resistance** (construct): *causes*, 1 paper
  > Focusing on relevant table cells helps LLMs by providing the right context, thus reducing hallucinations in reasoning. (Section 2)
  - [H-STAR: LLM-driven Hybrid SQL-Text Adaptive Reasoning on Tables](https://aclanthology.org/2025.naacl-long.445.pdf)
- **FUNSD** (measurement instrument): *measured_by*, 1 paper
  > We evaluate BLOCKIE on three established information extraction benchmarks: CORD (Park et al., 2019)... FUNSD (Jaume et al., 2019)... (Section 5.1)
  - [Information Extraction from Visually Rich Documents using LLM-based Organization of Documents into Independent Textual Segments](https://aclanthology.org/2025.acl-long.844.pdf)
- **SROIE** (measurement instrument): *measured_by*, 1 paper
  > We evaluate BLOCKIE on three established information extraction benchmarks: ... SROIE (Huang et al., 2019), a receipt information extraction dataset. (Section 5.1)
  - [Information Extraction from Visually Rich Documents using LLM-based Organization of Documents into Independent Textual Segments](https://aclanthology.org/2025.acl-long.844.pdf)
- **Human evaluation** (measurement instrument): *measured_by*, 1 paper
  > The proposed method achieves a human evaluation score of 82.7, which substantially outperforms the baseline (Ozaki et al., 2022) by 20.2 points. (Abstract)
  - [Causal Tree Extraction from Medical Case Reports: A Novel Task for Experts-like Text Comprehension](https://aclanthology.org/2025.emnlp-main.1313.pdf)
- **SciERC** (measurement instrument): *measured_by*, 1 paper
  > “SciERC | IE(Rel) | CS abstract | 6 entity types”
  - [SciRIFF: A Resource to Enhance Language Model Instruction-Following over Scientific Literature](https://aclanthology.org/2025.emnlp-main.310.pdf)
- **MT-Bench** (measurement instrument): *measured_by*, 1 paper
  > MT-Bench (Zheng et al., 2024), consists of 80 multi-turn dialogues spanning various domains, including writing, roleplay, reasoning, math, coding, extraction, STEM, and humanities. (Section 3.1)
  - [FuseChat: Knowledge Fusion of Chat Models](https://aclanthology.org/2025.emnlp-main.1096.pdf)

### Associated with
- **Understanding** (construct), 1 paper
  > Tasks at the Understanding level examine the ability to comprehend and interpret facts, entities, concepts, and relationships in legal texts, which serves as a foundational requirement for applying knowledge to downstream tasks. We construct five tasks at this level: Legal Element Recognition (2-1)... (Section C.3.2)
  - [LexEval: A Comprehensive Chinese Legal Benchmark for Evaluating Large Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/2cb40fc022ca7bdc1a9a78b793661284-Paper-Datasets_and_Benchmarks_Track.pdf)
- **Long-term memory** (construct), 1 paper
  > To comprehensively reflect the challenge, LONGMEMEVAL formulates five core long-term memory abilities: • Information Extraction (IE): Ability to recall specific information from extensive interactive histories... (Section 3.2)
  - [LongMemEval: Benchmarking Chat Assistants on Long-Term Interactive Memory](https://proceedings.iclr.cc/paper_files/paper/2025/file/d813d324dbf0598bbdc9c8e79740ed01-Paper-Conference.pdf)
- **Ranking** (behavioral indicator), 1 paper
  > To leverage the instruction following abilities in modern LLMs, we formulate the re-ranking task into either question answering (QA) or information extraction (IE) tasks, which are more commonly seen by LLMs. (Section 3.1)
  - [Attention in Large Language Models Yields Efficient Zero-Shot Re-Rankers](https://proceedings.iclr.cc/paper_files/paper/2025/file/b5b1890a7c1a79fe9b32b0f442347089-Paper-Conference.pdf)
- **Long-context understanding** (construct), 1 paper
  > Medical scenarios involve complex case histories, and selecting values from these contexts tests the capacity for long-context processing. (Section 1)
  - [MeNTi: Bridging Medical Calculator and LLM Agent with Nested Tool Calling](https://aclanthology.org/2025.naacl-long.263.pdf)
- **Spatial reasoning** (construct), 1 paper
  > Documents exhibit diverse formats and structures, requiring spatial reasoning to correctly associate text with their semantic roles. (Section 1)
  - [Information Extraction from Visually Rich Documents using LLM-based Organization of Documents into Independent Textual Segments](https://aclanthology.org/2025.acl-long.844.pdf)
- **Table reasoning** (construct), 1 paper
  > Our qualitative analysis of model responses reveals that Table-R1-Zero not only acquires multi-step reasoning and reflection abilities like other reasoning models, but also develops essential table-specific reasoning skills such as semantic understanding, information extraction, and arithmetic computation. (Section 1)
  - [Table-R1: Inference-Time Scaling for Table Reasoning Tasks](https://aclanthology.org/2025.emnlp-main.1040.pdf)
- **Instruction following** (behavioral indicator), 1 paper
  > to identify hallucinations existed in the reference description, we first extract object entities (object nouns and phrases) from it. Here, we leverage the strong instruction following ability of the Large Language Model (LLM). (Sec. 3.2.1)
  - [Image Textualization: An Automatic Framework for Generating Rich and Detailed Image Descriptions](https://proceedings.neurips.cc/paper_files/paper/2024/file/c37d94c04effc86d72ab2258ba9b76c7-Paper-Datasets_and_Benchmarks_Track.pdf)
