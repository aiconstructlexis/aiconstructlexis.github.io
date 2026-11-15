# Intent classification
**Type:** Behavioral indicator  
**Supporting papers:** 29  
**Also known as:** Intent detection, Intention recognition, Intent recognition, Multimodal intent recognition, Intent extraction  

## State of the Field

**Space of definitions.** Across papers, the prevailing usage treats this behavior as identifying a user's intent, intention, goal, or purpose from a spoken or written utterance, query, or command, usually in conversational AI or spoken language understanding settings. Most descriptions operationalize success as assigning a predefined intent label or semantic category, often as a multiclass classification problem, and one paper explicitly frames it as classifying an utterance into one of several predefined intents for a virtual assistant. Smaller variants widen the success criterion to identifying unknown intents, handling multi-intent cases as multi-label sequence prediction, or generating a free-form sentence that describes the inferred user intent from UI interaction traces.

**Variants.** Papers use several near-synonymous names, including intent detection, intent recognition, and intention recognition, with the same core task applied in different settings. The variants span text-only and speech utterances, spoken commands, virtual assistant data, and multimodal cases that combine text with video and audio; one video-focused study frames it as inferring intentions from agents' actions and subtle cues. A smaller line of work studies intent extraction from screenshots and action logs, where the output is a natural-language description rather than a class label.

**Space of elicitation and scores.** Papers measure this behavior with 7 linked instruments. The most frequently linked are BANKING77, CLINC150, and SNIPS; ATIS and MASSIVE also appear, along with 2 other instruments. These instruments are mostly benchmark datasets for intent label classification, while the less frequent ones cover speech SLU and multimodal intent recognition, including a multilingual virtual assistant dataset with intent and slot annotations and a large-scale dataset with fine-grained intent labels across text, video, and audio.

**What it is taken as evidence of.** Papers give little explicit evidence-of framing for this behavior. The only construct-level link is to Relational reasoning, and that link is described as related rather than as something the behavior measures or reflects: one paper calls for "relational reasoning methods concentrating on fine-grained semantics" for multimodal intent recognition. Beyond that, the papers do not converge on a shared construct that intent classification is taken to indicate.

## Sources

**Intent detection** (4 papers: [Towards Automated Error Discovery: A Study in Conversational AI](https://aclanthology.org/2025.emnlp-main.1.pdf), [ECLM: Entity Level Language Model for Spoken Language Understanding with Chain of Intent](https://aclanthology.org/2025.acl-long.1061.pdf), [INJONGO: A Multicultural Intent Detection and Slot-filling Dataset for 16 African Languages](https://aclanthology.org/2025.acl-long.464.pdf), [Prototype Conditioned Generative Replay for Continual Learning in NLP](https://aclanthology.org/2025.naacl-long.636.pdf))
> The task of identifying the user's intent from an utterance, used in this paper to assess the generalizability of the error detection method.

**Intent classification** (4 papers: [Comparing Specialised Small and General Large Language Models on Text Classification: 100 Labelled Samples to Achieve Break-Even Performance](https://aclanthology.org/2025.emnlp-main.9.pdf), [Tight Clusters Make Specialized Experts](https://proceedings.iclr.cc/paper_files/paper/2025/file/854a9ab0f323b841955e70ca383b27d1-Paper-Conference.pdf), [Wav2Prompt: End-to-End Speech Prompt Learning and Task-based Fine-tuning for Text-based LLMs](https://aclanthology.org/2025.naacl-long.354.pdf), [Main Predicate and Their Arguments as Explanation Signals For Intent Classification](https://aclanthology.org/2025.naacl-long.539.pdf))
> The task of identifying the user's intention or goal from a spoken or written utterance, typically in a conversational AI context.

**Intention recognition** (1 paper: [MultiAgentESC: A LLM-based Multi-Agent Collaboration Framework for Emotional Support Conversation](https://aclanthology.org/2025.emnlp-main.232.pdf))
> The observable task of identifying the underlying goal or intent of a user's utterances in a conversation.

**Intent recognition** (2 papers: [A Rigorous Evaluation of LLM Data Generation Strategies for Low-Resource Languages](https://aclanthology.org/2025.emnlp-main.418.pdf), [Understanding and Enhancing the Transferability of Jailbreaking Attacks](https://proceedings.iclr.cc/paper_files/paper/2025/file/db988b089d8d97d0f159c15ed0be6a71-Paper-Conference.pdf))
> The task of classifying a user's utterance into one of several predefined intents, typically in the context of a virtual assistant.

**Multimodal intent recognition** (1 paper: [LLM-Guided Semantic Relational Reasoning for Multimodal Intent Recognition](https://aclanthology.org/2025.emnlp-main.1130.pdf))
> Classifying the intent expressed in a multimodal sample using text together with video and audio cues.

**Intent extraction** (1 paper: [Small Models, Big Results: Achieving Superior Intent Extraction through Decomposition](https://aclanthology.org/2025.emnlp-main.949.pdf))
> Generating a free-form natural language description of the inferred user goal from a sequence of UI interactions, including screenshots and action logs.

## Relationships

### Intent classification →
- **BANKING77** (measurement instrument): *measured_by*, 2 papers
  > We report top-1 accuracy for finetuning classification tasks on the ... 77-class Banking-77 (B77) (Casanueva et al., 2020).
  - [Tight Clusters Make Specialized Experts](https://proceedings.iclr.cc/paper_files/paper/2025/file/854a9ab0f323b841955e70ca383b27d1-Paper-Conference.pdf)
  - [Towards Automated Error Discovery: A Study in Conversational AI](https://aclanthology.org/2025.emnlp-main.1.pdf)
- **CLINC150** (measurement instrument): *measured_by*, 2 papers
  > Intent Classification. CLINC150 (mis, 2020) is designed for intent classification, which comprises 150 classes across five domains... (Section 4.1).
  - [On Large Language Model Continual Unlearning](https://proceedings.iclr.cc/paper_files/paper/2025/file/fc28053a08f59fccb48b11f2e31e81c7-Paper-Conference.pdf)
  - [Towards Automated Error Discovery: A Study in Conversational AI](https://aclanthology.org/2025.emnlp-main.1.pdf)
- **SNIPS** (measurement instrument): *measured_by*, 2 papers
  > We use two intent classification benchmark datasets, ATIS (Hemphill et al., 1990), and SNIPS (Coucke et al., 2018). (Section 3)
  - [Main Predicate and Their Arguments as Explanation Signals For Intent Classification](https://aclanthology.org/2025.naacl-long.539.pdf)
  - [Comparing Specialised Small and General Large Language Models on Text Classification: 100 Labelled Samples to Achieve Break-Even Performance](https://aclanthology.org/2025.emnlp-main.9.pdf)
- **SLURP** (measurement instrument): *measured_by*, 1 paper
  > We evaluate them on three common speech tasks with corresponding common benchmarks: ... intent classification, a standard SLU task, with SLURP (Bastianelli et al., 2020) (Section 4.4).
  - [Joint Fine-tuning and Conversion of Pretrained Speech and Language Models towards Linear Complexity](https://proceedings.iclr.cc/paper_files/paper/2025/file/9b79416c0dc4b09feaa169ed5cdd63d4-Paper-Conference.pdf)
- **ATIS** (measurement instrument): *measured_by*, 1 paper
  > We use two intent classification benchmark datasets, ATIS (Hemphill et al., 1990), and SNIPS (Coucke et al., 2018). (Section 3)
  - [Main Predicate and Their Arguments as Explanation Signals For Intent Classification](https://aclanthology.org/2025.naacl-long.539.pdf)
- **MASSIVE** (measurement instrument): *measured_by*, 1 paper
  > For intent recognition, we use MASSIVE (FitzGerald et al., 2023), which is a multilingual dataset for virtual assistant evaluation with intent and slot annotations that supports 51 languages and 60 intents. (Section 3.2)
  - [A Rigorous Evaluation of LLM Data Generation Strategies for Low-Resource Languages](https://aclanthology.org/2025.emnlp-main.418.pdf)
- **MIntRec2.0** (measurement instrument): *measured_by*, 1 paper
  > MIntRec2.0 is a large-scale dataset with 30 fine-grained intent labels spanning text, video, and audio modalities. (Section 4.1)
  - [LLM-Guided Semantic Relational Reasoning for Multimodal Intent Recognition](https://aclanthology.org/2025.emnlp-main.1130.pdf)

### Associated with
- **Relational reasoning** (construct), 1 paper
  > Consequently, there is a need for relational reasoning methods concentrating on fine-grained semantics for multimodal intent recognition... (Introduction)
  - [LLM-Guided Semantic Relational Reasoning for Multimodal Intent Recognition](https://aclanthology.org/2025.emnlp-main.1130.pdf)
