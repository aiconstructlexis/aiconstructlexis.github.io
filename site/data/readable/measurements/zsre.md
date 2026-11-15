# ZsRE
**Type:** Measurement instrument  
**Supporting papers:** 46  
**Also known as:** ZSRE, zsRE, Zero-Shot RE, Zero-shot relation extraction (zsRE), zs-RE, ZeroShot RE  

## State of the Field

**What it is.** Across these papers, ZsRE is most commonly described as a zero-shot relation extraction benchmark or dataset. Many definitions also frame it as a question-answering benchmark for knowledge editing, including short question-answer pairs derived from Wikipedia, a context-free or closed-book QA setting, and instances with a factual statement plus a paraphrased prompt; one paper also describes it as using reading-comprehension examples for relation-slot filling sourced primarily from WikiReading. A smaller line of work refers to it as a slot-filling or relation-extraction task, including as a KILT subset task, while several model-editing papers describe using it for knowledge insertion, modification, or factual editing.

**What it is claimed to measure.** Papers link ZsRE to 5 behavioral indicators and 4 constructs. The prevailing measurement claims use it to measure knowledge editing and question answering, and other papers report it as measuring information extraction, relation extraction, and hallucination. At the construct level, papers use it to measure editing locality, factual knowledge, generality, and knowledge integration efficacy, so its reported measurement role is spread across several targets rather than tied to only one.

**Space of uses.** In model-editing work, papers most commonly use ZsRE alongside CounterFact and describe the pair as widely adopted or representative editing benchmarks; smaller uses place it with Multi-CounterFact, CoQA, T-REx, and WikiDataCounterFact. Papers position it as a source of factual knowledge edits, knowledge insertion and modification examples, or closed-book QA edit prompts with paraphrases and locality prompts, while reasoning and retrieval papers use it as a slot-filling or relation-extraction evaluation task, sometimes within a KILT task set. One paper also reports it as related to BMIKE-53, which is constructed from zsRE, CounterFact, and WikiFactDiff.

**Concerns raised.** Only one explicit limitation is stated: a paper says ZsRE does not measure generative capabilities, and therefore evaluates models on it only by Efficacy, Generality, and Locality accuracy.

## Sources

**ZSRE** (7 papers: [BadEdit: Backdooring Large Language Models by Model Editing](https://proceedings.iclr.cc/paper_files/paper/2024/file/6f6fe6789e14796b6544a04b20d11902-Paper-Conference.pdf), [Perturbation-Restrained Sequential Model Editing](https://proceedings.iclr.cc/paper_files/paper/2025/file/2c15b0221da28bc6f4373a7e78b896dd-Paper-Conference.pdf), [Has this Fact been Edited? Detecting Knowledge Edits in Language Models](https://aclanthology.org/2025.naacl-long.492.pdf), [Reasons and Solutions for the Decline in Model Performance after Editing](https://proceedings.neurips.cc/paper_files/paper/2024/file/7f588e59e9ae6138d3ea9e4fdaa7e040-Paper-Conference.pdf), [Stealth edits to large language models](https://proceedings.neurips.cc/paper_files/paper/2024/file/5c8168a8eca2eb23f6b1f5019371043e-Paper-Conference.pdf), [VLKEB: A Large Vision-Language Model Knowledge Editing Benchmark](https://proceedings.neurips.cc/paper_files/paper/2024/file/1198b53fa686831d5f0c0860d7ec4f34-Paper-Datasets_and_Benchmarks_Track.pdf), [WISE: Rethinking the Knowledge Memory for Lifelong Model Editing of Large Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/60960ad78868fce5c165295fbd895060-Paper-Conference.pdf))
> A dataset for zero-shot relation extraction, used to evaluate a model's ability to identify relations it has not been explicitly trained on.

**zsRE** (3 papers: [Can Sensitive Information Be Deleted From LLMs? Objectives for Defending Against Extraction Attacks](https://proceedings.iclr.cc/paper_files/paper/2024/file/c652e5f62fd1f5acbbf0d6413a1113e7-Paper-Conference.pdf), [Massive Editing for Large Language Models via Meta Learning](https://proceedings.iclr.cc/paper_files/paper/2024/file/f074097f6f186947726ef28819d589e7-Paper-Conference.pdf), [CollabEdit: Towards Non-destructive Collaborative Knowledge Editing](https://proceedings.iclr.cc/paper_files/paper/2025/file/47eb71e8e778dc9def7780baa7b35687-Paper-Conference.pdf))
> A question-answer benchmark derived from Wikipedia that is used here to test factual editing and extraction of specific answers.

**ZsRE** (5 papers: [Precise Localization of Memories: A Fine-grained Neuron-level Knowledge Editing Technique for LLMs](https://proceedings.iclr.cc/paper_files/paper/2025/file/01db36a646c07c64dd39a92b4eceb417-Paper-Conference.pdf), [CoME: An Unlearning-based Approach to Conflict-free Model Editing](https://aclanthology.org/2025.naacl-long.325.pdf), [AdaEdit: Advancing Continuous Knowledge Editing For Large Language Models](https://aclanthology.org/2025.acl-long.208.pdf), [Towards Lifelong Model Editing via Simulating Ideal Editor](https://raw.githubusercontent.com/mlresearch/v267/main/assets/guo25c/guo25c.pdf), [LyapLock: Bounded Knowledge Preservation in Sequential Large Language Model Editing](https://aclanthology.org/2025.emnlp-main.327.pdf))
> A dataset for knowledge editing evaluation, originally developed for zero-shot relation extraction, used here for knowledge insertion and modification tasks.

**Zero-Shot RE** (3 papers: [RA-DIT: Retrieval-Augmented Dual Instruction Tuning](https://proceedings.iclr.cc/paper_files/paper/2024/file/536d18fbb454f80221465f1a42c6f389-Paper-Conference.pdf), [Think-on-Graph: Deep and Responsible Reasoning of Large Language Model on Knowledge Graph](https://proceedings.iclr.cc/paper_files/paper/2024/file/10a6bdcabbd5a3d36b760daa295f63c1-Paper-Conference.pdf), [Reasoning of Large Language Models over Knowledge Graphs with Super-Relations](https://proceedings.iclr.cc/paper_files/paper/2025/file/0c6799a1a5db47be8864fed46ba77697-Paper-Conference.pdf))
> A zero-shot relation extraction benchmark used to test relation prediction without task-specific training.

**zs-RE** (1 paper: [Training a Utility-based Retriever Through Shared Context Attribution for Retrieval-Augmented Language Models](https://aclanthology.org/2025.emnlp-main.33.pdf))
> zs-RE is a benchmark for zero-shot relation extraction, where models must identify relations between entities without prior examples for those specific relations.

**ZeroShot RE** (1 paper: [HydraRAG: Structured Cross-Source Enhanced Large Language Model Reasoning](https://aclanthology.org/2025.emnlp-main.730.pdf))
> A zero-shot relation extraction benchmark used to evaluate extracting relations from text without task-specific training.

## Relationships

### → ZsRE
- **Question answering** (behavioral indicator): *measured_by*, 4 papers
  > For GPT-2, T5-XL, and GPT-J, we use the zero-shot Relation Extraction (zsRE) question answering dataset (Levy et al., 2017) with the identical train/val splits with De Cao et al. (2021); Mitchell et al. (2022) (Section 5).
  - [Massive Editing for Large Language Models via Meta Learning](https://proceedings.iclr.cc/paper_files/paper/2024/file/f074097f6f186947726ef28819d589e7-Paper-Conference.pdf)
  - [WISE: Rethinking the Knowledge Memory for Lifelong Model Editing of Large Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/60960ad78868fce5c165295fbd895060-Paper-Conference.pdf)
  - [Composable Interventions for Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/7f5f9a88c6516469c83d074c6f2976fb-Paper-Conference.pdf)
  - [Think and Recall: Layer-Level Prompting for Lifelong Model Editing](https://aclanthology.org/2025.emnlp-main.733.pdf)
- **Knowledge editing** (behavioral indicator): *measured_by*, 4 papers
  > we edit different kinds of knowledge: WikiDatarecent, WikiDatacounterfact (Cohen et al., 2024), WikiBio (Hartvigsen et al., 2024), ConvSent (Mitchell et al., 2022), and ZsRE (Yao et al., 2023). (Section 3.1)
  - [Unlocking Efficient, Scalable, and Continual Knowledge Editing with Basis-Level Representation Fine-Tuning](https://proceedings.iclr.cc/paper_files/paper/2025/file/2f89a23a19d1617e7fb16d4f7a049ce2-Paper-Conference.pdf)
  - [AlphaEdit: Null-Space Constrained Knowledge Editing for Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/29c8c615b3187ee995029284702d3f43-Paper-Conference.pdf)
  - [Dynamic Retriever for In-Context Knowledge Editing via Policy Optimization](https://aclanthology.org/2025.emnlp-main.848.pdf)
  - [LyapLock: Bounded Knowledge Preservation in Sequential Large Language Model Editing](https://aclanthology.org/2025.emnlp-main.327.pdf)
- **Information extraction** (behavioral indicator): *measured_by*, 2 papers
  > two slot filling datasets: T-REx (ElSahar et al., 2018) and Zero-Shot RE (Petroni et al., 2021);
  - [Think-on-Graph: Deep and Responsible Reasoning of Large Language Model on Knowledge Graph](https://proceedings.iclr.cc/paper_files/paper/2024/file/10a6bdcabbd5a3d36b760daa295f63c1-Paper-Conference.pdf)
  - [Think-on-Graph 2.0: Deep and Faithful Large Language Model Reasoning with Knowledge-guided Retrieval Augmented Generation](https://proceedings.iclr.cc/paper_files/paper/2025/file/830b1abc6d2da85f23d41169fa44d185-Paper-Conference.pdf)
- **Relation extraction** (behavioral indicator): *measured_by*, 2 papers
  > We use a relation extraction dataset ZSRE (Meng et al., 2022a) and a conversational question answering dataset CoQA (Reddy et al., 2019) to represent unrelated tasks
  - [BadEdit: Backdooring Large Language Models by Model Editing](https://proceedings.iclr.cc/paper_files/paper/2024/file/6f6fe6789e14796b6544a04b20d11902-Paper-Conference.pdf)
  - [Training a Utility-based Retriever Through Shared Context Attribution for Retrieval-Augmented Language Models](https://aclanthology.org/2025.emnlp-main.33.pdf)
- **Generality** (construct): *measured_by*, 1 paper
  > Since ZsRE does not measure generative capabilities, we evaluate the models based only on accuracy in terms of Efficacy, Generality, and Locality. (Section 5.1)
  - [CoME: An Unlearning-based Approach to Conflict-free Model Editing](https://aclanthology.org/2025.naacl-long.325.pdf)
- **Editing locality** (construct): *measured_by*, 1 paper
  > Since ZsRE does not measure generative capabilities, we evaluate the models based only on accuracy in terms of Efficacy, Generality, and Locality. (Section 5.1)
  - [CoME: An Unlearning-based Approach to Conflict-free Model Editing](https://aclanthology.org/2025.naacl-long.325.pdf)
- **Hallucination** (behavioral indicator): *measured_by*, 1 paper
  > Our experiments require a source of hallucinations to edit, which we draw from the Multi-CounterFact (MCF) [26] and ZsRE [27] datasets. (Section 5)
  - [Stealth edits to large language models](https://proceedings.neurips.cc/paper_files/paper/2024/file/5c8168a8eca2eb23f6b1f5019371043e-Paper-Conference.pdf)
- **Factual knowledge** (construct): *measured_by*, 1 paper
  > For factual knowledge, two popular model editing datasets Zero-Shot Relation Extraction (ZSRE) (Levy et al., 2017) and COUNTERFACT (Meng et al., 2022) were adopted in our experiments. (Section 5.2)
  - [Perturbation-Restrained Sequential Model Editing](https://proceedings.iclr.cc/paper_files/paper/2025/file/2c15b0221da28bc6f4373a7e78b896dd-Paper-Conference.pdf)
- **Knowledge integration efficacy** (construct): *measured_by*, 1 paper
  > Since ZsRE does not measure generative capabilities, we evaluate the models based only on accuracy in terms of Efficacy, Generality, and Locality. (Section 5.1)
  - [CoME: An Unlearning-based Approach to Conflict-free Model Editing](https://aclanthology.org/2025.naacl-long.325.pdf)

### Associated with
- **BMIKE-53** (measurement instrument), 1 paper
  > BMIKE-53 is constructed from three monolingual KE datasets: zsRE, CounterFact, and WikiFactDiff
  - [BMIKE-53: Investigating Cross-Lingual Knowledge Editing with In-Context Learning](https://aclanthology.org/2025.acl-long.798.pdf)
