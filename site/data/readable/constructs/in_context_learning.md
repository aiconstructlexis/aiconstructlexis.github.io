# In-context learning
**Type:** Construct  
**Supporting papers:** 203  
**Also known as:** In-context learning capability, In-context learning ability, In-Context Learning ability, In-context learnability, In-context causal structure selection, Few-shot capability, Few-shot learning capability, Few-shot adaptation, Multi-modal long-context learning, Distributional alignment  

## State of the Field

**Space of definitions.** Across the papers, the dominant framing is a model ability at inference or test time: the model adapts to or performs a new task by conditioning on a few demonstrations, usually input-output or input-label pairs in the prompt, without updating weights or parameters. Many definitions make the task of the model explicit, namely inferring task rules, mappings, patterns, or functions from those examples and then answering a new query. A smaller line of work broadens the context beyond labeled demonstrations to instructions, unlabeled token sequences, reference texts, optimization histories, or other contextual information, and a minority of papers use the term for an observable few-shot prompting procedure or evaluation setup rather than a latent capability.

**Space of facets.** Papers use nearby labels such as in-context learning ability or capability, and some neighboring terms, especially few-shot capability or adaptation, describe the same prompt-conditioned task adaptation pattern. They also carve out narrower variants such as in-context causal structure selection and multi-modal long-context learning, while one theoretical line defines in-context learnability as a formal property of a task. Conceptual accounts most often contrast it with in-weights learning and frame it as meta-learning.

**Space of measurement.** Operationally, papers link in-context learning to 21 measurement instruments and 28 behavioral indicators. The most common named instruments are GSM8K, MMLU, MetaICL, BIG-Bench Hard, and the lm-evaluation-harness, usually in explicit few-shot setups such as 5-shot or 8-shot evaluation; other instruments extend this to long-context, general evaluation, and multimodal captioning or VQA benchmarks. The linked behavioral indicators center on few-shot task performance and task families such as text classification and forecasting, alongside training-sensitive behaviors such as catastrophic forgetting, so the prevailing operationalization matches the dominant definitions, though some evaluations broaden it to long-context, multimodal, or prompt-steering settings.

**Links.** Papers most often claim causal relationships from in-context learning to generalization, out-of-distribution generalization, and reasoning. The most recurrent related links connect it to in-weights learning and meta-learning. Other papers record additional causal or related ties to a broader set of model properties and downstream behaviors, and a smaller line of work reverses the direction by linking other constructs or training effects to in-context learning rather than the reverse.

## Sources

**In-context learning** (69 papers: [A Benchmark for Learning to Translate a New Language from One Grammar Book](https://proceedings.iclr.cc/paper_files/paper/2024/file/52d63f9e4b81f866bf69fb3c834aad47-Paper-Conference.pdf), [Are Human-generated Demonstrations Necessary for In-context Learning?](https://proceedings.iclr.cc/paper_files/paper/2024/file/19914b5bf19ab2b245d2e6ff7299e8f0-Paper-Conference.pdf), [BadChain: Backdoor Chain-of-Thought Prompting for Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/791d3337291b2c574545aeecfa75484c-Paper-Conference.pdf), [Batch Calibration: Rethinking Calibration for In-Context Learning and Prompt Engineering](https://proceedings.iclr.cc/paper_files/paper/2024/file/003e438cf04e3caf0a5c908495e484fe-Paper-Conference.pdf), [CausalLM is not optimal for in-context learning](https://proceedings.iclr.cc/paper_files/paper/2024/file/364071531ff2398e0fb8bae31f615b69-Paper-Conference.pdf), [Context is Environment](https://proceedings.iclr.cc/paper_files/paper/2024/file/03645743ea35690f30d795d6bac149a5-Paper-Conference.pdf), [DQ-LoRe: Dual Queries with Low Rank Approximation Re-ranking for In-Context Learning](https://proceedings.iclr.cc/paper_files/paper/2024/file/b3875605f2e35714fc8a807cadf8a5e8-Paper-Conference.pdf), [Democratizing Fine-grained Visual Recognition with Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/49299a8afda8053932a4cfd62fdfd1b9-Paper-Conference.pdf), [Emu: Generative Pretraining in Multimodality](https://proceedings.iclr.cc/paper_files/paper/2024/file/34d5143080c89a7ce10932c8c5e1907f-Paper-Conference.pdf), [Gen-Z: Generative Zero-Shot Text Classification with Contextualized Label Descriptions](https://proceedings.iclr.cc/paper_files/paper/2024/file/af7cc9e2366b8f8837a6ef339810277a-Paper-Conference.pdf), [Grounding Multimodal Large Language Models to the World](https://proceedings.iclr.cc/paper_files/paper/2024/file/e112a4671e8779aa9f640a0e3f81bd26-Paper-Conference.pdf), [How Do Transformers Learn In-Context Beyond Simple Functions? A Case Study on Learning with Representations](https://proceedings.iclr.cc/paper_files/paper/2024/file/c9694bf4f9bf3626f7d21158bab74f8e-Paper-Conference.pdf), [How Many Pretraining Tasks Are Needed for In-Context Learning of Linear Regression?](https://proceedings.iclr.cc/paper_files/paper/2024/file/fa3c139cf8084de7bfd944f1c90c8695-Paper-Conference.pdf), [IDEAL: Influence-Driven Selective Annotations Empower In-Context Learners in Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/a7f90da65dd41d699d00e95700e6fa1e-Paper-Conference.pdf), [In-Context Learning Learns Label Relationships but Is Not Conventional Learning](https://proceedings.iclr.cc/paper_files/paper/2024/file/0db404e9cc9d282be6dfe8538352408c-Paper-Conference.pdf), [In-Context Learning through the Bayesian Prism](https://proceedings.iclr.cc/paper_files/paper/2024/file/d81cd83e7f6748af351485d73f305483-Paper-Conference.pdf), [In-Context Pretraining: Language Modeling Beyond Document Boundaries](https://proceedings.iclr.cc/paper_files/paper/2024/file/a1fe2365abdb691332537990a6385909-Paper-Conference.pdf), [Is attention required for ICL? Exploring the Relationship Between Model Architecture and In-Context Learning Ability](https://proceedings.iclr.cc/paper_files/paper/2024/file/ea6d17af54f827336fc8fed27ca0319d-Paper-Conference.pdf), [Language Modeling Is Compression](https://proceedings.iclr.cc/paper_files/paper/2024/file/3cbf627fa24fb6cb576e04e689b9428b-Paper-Conference.pdf), [Language-Interfaced Tabular Oversampling via Progressive Imputation and Self-Authentication](https://proceedings.iclr.cc/paper_files/paper/2024/file/5d54d2df6ec8f7b920aa0fec9a6d1b2e-Paper-Conference.pdf), [Large Language Models as Analogical Reasoners](https://proceedings.iclr.cc/paper_files/paper/2024/file/4990dad2c1696224de42573d0222554a-Paper-Conference.pdf), [Large Language Models as Tool Makers](https://proceedings.iclr.cc/paper_files/paper/2024/file/ed91353f700d113e5d848c7e04a858b0-Paper-Conference.pdf), [Large Language Models to Enhance Bayesian Optimization](https://proceedings.iclr.cc/paper_files/paper/2024/file/84b8d9fcb4e262fcd429544697e1e720-Paper-Conference.pdf), [LoTa-Bench: Benchmarking Language-oriented Task Planners for Embodied Agents](https://proceedings.iclr.cc/paper_files/paper/2024/file/e91fb65c6324a984ea9ef39a5b84af04-Paper-Conference.pdf), [Looped Transformers are Better at Learning Learning Algorithms](https://proceedings.iclr.cc/paper_files/paper/2024/file/b8402301e7f06bdc97a31bfaa653dc32-Paper-Conference.pdf), [MEND: Meta Demonstration Distillation for Efficient and Effective In-Context Learning](https://proceedings.iclr.cc/paper_files/paper/2024/file/7ce1cbededb4b0d6202847ac1b484ee8-Paper-Conference.pdf), [One Step of Gradient Descent is Provably the Optimal In-Context Learner with One Layer of Linear Self-Attention](https://proceedings.iclr.cc/paper_files/paper/2024/file/87f476af4053961667c2c08e9f4b850e-Paper-Conference.pdf), [Privacy-Preserving In-Context Learning for Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/572cd21bd5dea96b065476b77d21b3c6-Paper-Conference.pdf), [Privacy-Preserving In-Context Learning with Differentially Private Few-Shot Generation](https://proceedings.iclr.cc/paper_files/paper/2024/file/8cb564df771e9eacbfe9d72bd46a24a9-Paper-Conference.pdf), [Retrieval meets Long Context Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/d75f29006df67df084e6586f1cb8458c-Paper-Conference.pdf), [Supervised Knowledge Makes Large Language Models Better In-context Learners](https://proceedings.iclr.cc/paper_files/paper/2024/file/bfa629625fd35bf5b880df464b584a57-Paper-Conference.pdf), [The Cost of Scaling Down Large Language Models: Reducing Model Size Affects Memory before In-context Learning](https://proceedings.iclr.cc/paper_files/paper/2024/file/bb68f698772f14b6d8eaef4529fb9176-Paper-Conference.pdf), [The mechanistic basis of data dependence and abrupt learning in an in-context classification task](https://proceedings.iclr.cc/paper_files/paper/2024/file/540a3bf4863672cdaebfed69fa2ce335-Paper-Conference.pdf), [Two-stage LLM Fine-tuning with Less Specialization and More Generalization](https://proceedings.iclr.cc/paper_files/paper/2024/file/597254dc45be8c166d3ccf0ba2d56325-Paper-Conference.pdf), [Understanding Catastrophic Forgetting in Language Models via Implicit Inference](https://proceedings.iclr.cc/paper_files/paper/2024/file/692ae28fda9bfbde7c01b13bf5a03395-Paper-Conference.pdf), [Understanding In-Context Learning from Repetitions](https://proceedings.iclr.cc/paper_files/paper/2024/file/d88f6f81e1aaf606776ffdd06fdf24ef-Paper-Conference.pdf), [Understanding In-Context Learning in Transformers and LLMs by Learning to Learn Discrete Functions](https://proceedings.iclr.cc/paper_files/paper/2024/file/f7e7fabd73b3df96c54a320862afcb78-Paper-Conference.pdf), [YaRN: Efficient Context Window Extension of Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/874a4d89f2d04b4bcf9a2c19545cf040-Paper-Conference.pdf), [UniAudio 1.5: Large Language Model-Driven Audio Codec is A Few-Shot Audio Task Learner](https://proceedings.neurips.cc/paper_files/paper/2024/file/6801fa3fd290229efc490ee0cf1c5687-Paper-Conference.pdf), [Differential Transformer](https://proceedings.iclr.cc/paper_files/paper/2025/file/00b67df24009747e8bbed4c2c6f9c825-Paper-Conference.pdf), [Retrieval, Reasoning, Re-ranking: A Context-Enriched Framework for Knowledge Graph Completion](https://aclanthology.org/2025.naacl-long.221.pdf), [LongLeader: A Comprehensive Leaderboard for Large Language Models in Long-context Scenarios](https://aclanthology.org/2025.naacl-long.439.pdf), [Mamba-Shedder: Post-Transformer Compression for Efficient Selective Structured State Space Models](https://aclanthology.org/2025.naacl-long.195.pdf), [Instantly Learning Preference Alignment via In-context DPO](https://aclanthology.org/2025.naacl-long.8.pdf), [SynthDetoxM: Modern LLMs are Few-Shot Parallel Detoxification Data Annotators](https://aclanthology.org/2025.naacl-long.294.pdf), [Few-Shot Natural Language to First-Order Logic Translation via Code Generation](https://aclanthology.org/2025.naacl-long.547.pdf), [IrokoBench: A New Benchmark for African Languages in the Age of Large Language Models](https://aclanthology.org/2025.naacl-long.139.pdf), [In-Context Learning with Long-Context Models: An In-Depth Exploration](https://aclanthology.org/2025.naacl-long.605.pdf), [Prompting with Phonemes: Enhancing LLMs' Multilinguality for Non-Latin Script Languages](https://aclanthology.org/2025.naacl-long.599.pdf), [Diverse In-Context Example Selection After Decomposing Programs and Aligned Utterances Improves Semantic Parsing](https://aclanthology.org/2025.naacl-long.289.pdf), [Benchmarking Large Language Models on Answering and Explaining Challenging Medical Questions](https://aclanthology.org/2025.naacl-long.182.pdf), [Is In-Context Learning a Type of Error-Driven Learning? Evidence from the Inverse Frequency Effect in Structural Priming](https://aclanthology.org/2025.naacl-long.586.pdf), [DenseSSM: State Space Models with Dense Hidden Connection for Efficient Large Language Models](https://aclanthology.org/2025.naacl-long.467.pdf), [ParaICL: Towards Parallel In-Context Learning](https://aclanthology.org/2025.naacl-long.621.pdf), [MILU: A Multi-task Indic Language Understanding Benchmark](https://aclanthology.org/2025.naacl-long.507.pdf), [Explanation based In-Context Demonstrations Retrieval for Multilingual Grammatical Error Correction](https://aclanthology.org/2025.naacl-long.251.pdf), [DAWN-ICL: Strategic Planning of Problem-solving Trajectories for Zero-Shot In-Context Learning](https://aclanthology.org/2025.naacl-long.96.pdf), [In-Context Learning (and Unlearning) of Length Biases](https://aclanthology.org/2025.naacl-long.390.pdf), [Divergent Thoughts toward One Goal: LLM-based Multi-Agent Collaboration System for Electronic Design Automation](https://aclanthology.org/2025.naacl-long.83.pdf), [Logit Separability-Driven Samples and Multiple Class-Related Words Selection for Advancing In-Context Learning](https://aclanthology.org/2025.naacl-long.343.pdf), [PICLe: Pseudo-annotations for In-Context Learning in Low-Resource Named Entity Detection](https://aclanthology.org/2025.naacl-long.518.pdf), [PromptRefine: Enhancing Few-Shot Performance on Low-Resource Indic Languages with Example Selection from related Example Banks](https://aclanthology.org/2025.naacl-long.17.pdf), [Learning vs Retrieval: The Role of In-Context Examples in Regression with Large Language Models](https://aclanthology.org/2025.naacl-long.417.pdf), [Emergence of Episodic Memory in Transformers: Characterizing Changes in Temporal Structure of Attention Scores During Training](https://aclanthology.org/2025.naacl-long.448.pdf), [Prompt Compression for Large Language Models: A Survey](https://aclanthology.org/2025.naacl-long.368.pdf), [JRE-L: Journalist, Reader, and Editor LLMs in the Loop for Science Journalism for the General Audience](https://aclanthology.org/2025.naacl-long.335.pdf), [D.Va: Validate Your Demonstration First Before You Use It](https://aclanthology.org/2025.acl-long.129.pdf), [Interpretability Analysis of Arithmetic In-Context Learning in Large Language Models](https://aclanthology.org/2025.emnlp-main.92.pdf), [What Makes In-context Learning Effective for Mathematical Reasoning](https://raw.githubusercontent.com/mlresearch/v267/main/assets/liu25ac/liu25ac.pdf))
> The ability of a language model to adapt to a new task by conditioning on a few input-label demonstrations provided in the prompt, without parameter updates.

**In-context learning capability** (2 papers: [LogiCity: Advancing Neuro-Symbolic AI with Abstract Urban Simulation](https://proceedings.neurips.cc/paper_files/paper/2024/file/8196be81e68289d7a9ece21ed7f5750a-Paper-Datasets_and_Benchmarks_Track.pdf), [Personalized Visual Instruction Tuning](https://proceedings.iclr.cc/paper_files/paper/2025/file/6b69dcf999ee89f48d08c6c9881a4c0d-Paper-Conference.pdf))
> The ability to infer task rules and answer new questions from a small set of demonstrations provided in the prompt.

**In-context learning ability** (4 papers: [Unlocking the Power of Function Vectors for Characterizing and Mitigating Catastrophic Forgetting in Continual Instruction Tuning](https://proceedings.iclr.cc/paper_files/paper/2025/file/74fc5575632191d96881d8015f79dde3-Paper-Conference.pdf), [Evaluating the Prompt Steerability of Large Language Models](https://aclanthology.org/2025.naacl-long.400.pdf), [Self-Instructed Derived Prompt Generation Meets In-Context Learning: Unlocking New Potential of Black-Box LLMs](https://aclanthology.org/2025.acl-long.92.pdf), [Targeted Distillation for Sentiment Analysis](https://aclanthology.org/2025.emnlp-main.1127.pdf))
> The model's capacity to perform evaluation tasks when conditioned on example input-output pairs in the prompt.

**In-Context Learning ability** (1 paper: [Training Nonlinear Transformers for Chain-of-Thought Inference: A Theoretical Generalization Analysis](https://proceedings.iclr.cc/paper_files/paper/2025/file/b295b3a940706f431076c86b78907757-Paper-Conference.pdf))
> The latent capability of a model to perform a task by conditioning on a few input-output examples provided in the prompt, without explicit intermediate reasoning steps.

**In-context causal structure selection** (1 paper: [Selective induction Heads: How Transformers Select Causal Structures in Context](https://proceedings.iclr.cc/paper_files/paper/2025/file/d7ed243b13831bdd468f35039936bcef-Paper-Conference.pdf))
> The ability of a model to dynamically identify the correct underlying causal relationship between tokens, such as the lag in a Markov chain, from the context and use it for prediction.

**In-context learnability** (1 paper: [Chain-of-Thought Provably Enables Learning the (Otherwise) Unlearnable](https://proceedings.iclr.cc/paper_files/paper/2025/file/da535999561b932f56efdd559498282e-Paper-Conference.pdf))
> A formal property of a task, indicating whether a model can successfully learn to solve it with high probability given a sufficient number of in-context examples.

**Few-shot capability** (1 paper: [From News to Forecast: Integrating Event Analysis in LLM-Based Time Series Forecasting with Reflection](https://proceedings.neurips.cc/paper_files/paper/2024/file/6aef8bffb372096ee73d98da30119f89-Paper-Conference.pdf))
> The ability of a pre-trained model to perform tasks effectively with only a small number of examples, without requiring extensive fine-tuning.

**Few-shot learning capability** (1 paper: [ORPP: Self-Optimizing Role-playing Prompts to Enhance Language Model Capabilities](https://aclanthology.org/2025.emnlp-main.1453.pdf))
> The model's ability to learn and perform a task based on a small number of examples provided within the prompt's context.

**Few-shot adaptation** (1 paper: [TAIA: Large Language Models are Out-of-Distribution Data Learners](https://proceedings.neurips.cc/paper_files/paper/2024/file/be0a8ecf8b2743a4117557c5eca0fb79-Paper-Conference.pdf))
> Learning contextually from demonstrations in a few-shot setting to improve performance on new tasks.

**Multi-modal long-context learning** (1 paper: [Efficient Multi-modal Long Context Learning for Training-free Adaptation](https://raw.githubusercontent.com/mlresearch/v267/main/assets/ma25v/ma25v.pdf))
> The ability of a multi-modal model to improve its performance on a downstream task by conditioning on a long context of many demonstration examples.

**Distributional alignment** (1 paper: [Fine-grained Analysis of In-context Linear Estimation: Data, Architecture, and Beyond](https://proceedings.neurips.cc/paper_files/paper/2024/file/f9dc462382fef56d58279e75de2438f3-Paper-Conference.pdf))
> The model's capacity to leverage statistical correlations within the in-context data, such as between task and feature vectors or between query and demonstration examples, to improve learning efficiency.

## Relationships

### In-context learning →
- **Generalization** (construct): *causes*, 16 papers
  > In-context learning is a key paradigm in large language models (LLMs) that enables them to generalize to new tasks and domains by simply prompting these models with a few exemplars without explicit parameter updates. (Abstract)
  - [Probing the Decision Boundaries of In-context Learning in Large Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/eb5dd4476448c44e55a759a985b3bbec-Paper-Conference.pdf)
  - [The Closeness of In-Context Learning and Weight Shifting for Softmax Regression](https://proceedings.neurips.cc/paper_files/paper/2024/file/726ab29b61a749b36d2593648716ae3c-Paper-Conference.pdf)
  - [MetaAligner: Towards Generalizable Multi-Objective Alignment of Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/3d03800841fa1bb2f43ef1750aafcce4-Paper-Conference.pdf)
  - [EHRCon: Dataset for Checking Consistency between Unstructured Notes and Structured Tables in Electronic Health Records](https://proceedings.neurips.cc/paper_files/paper/2024/file/a291dad965af9bc2e39ffeb2ca1c6dc0-Paper-Datasets_and_Benchmarks_Track.pdf)
  - [Towards Understanding How Transformers Learn In-context Through a Representation Learning Lens](https://proceedings.neurips.cc/paper_files/paper/2024/file/01a8d63f9cb6dcbaa3092ccddd2075ac-Paper-Conference.pdf)
  - [Transformers are Minimax Optimal Nonparametric In-Context Learners](https://proceedings.neurips.cc/paper_files/paper/2024/file/c11daad0a48ea5f3c5c6390c7b060720-Paper-Conference.pdf)
  - [Fine-grained Analysis of In-context Linear Estimation: Data, Architecture, and Beyond](https://proceedings.neurips.cc/paper_files/paper/2024/file/f9dc462382fef56d58279e75de2438f3-Paper-Conference.pdf)
  - [Enhancing In-Context Learning Performance with just SVD-Based Weight Pruning: A Theoretical Perspective](https://proceedings.neurips.cc/paper_files/paper/2024/file/448444518637da106d978ae7409d9789-Paper-Conference.pdf)
  - [Making Text Embedders Few-Shot Learners](https://proceedings.iclr.cc/paper_files/paper/2025/file/5eba8556ce2d1afff57591464d48fbc3-Paper-Conference.pdf)
  - [In-Context Editing: Learning Knowledge from Self-Induced Distributions](https://proceedings.iclr.cc/paper_files/paper/2025/file/c0ff9e52e94ae331bc0f2d28be06a9ca-Paper-Conference.pdf)
  - [APE: Faster and Longer Context-Augmented Generation via Adaptive Parallel Encoding](https://proceedings.iclr.cc/paper_files/paper/2025/file/ce186a37e63b37638ecd06dee6b9a355-Paper-Conference.pdf)
  - [LICO: Large Language Models for In-Context Molecular Optimization](https://proceedings.iclr.cc/paper_files/paper/2025/file/84b16af3773fc5825ddb64996190289a-Paper-Conference.pdf)
  - [Differential learning kinetics govern the transition from memorization to generalization during in-context learning](https://proceedings.iclr.cc/paper_files/paper/2025/file/187f9ba4cd5a59477305ac712282a1cd-Paper-Conference.pdf)
  - [Few-Shot Natural Language to First-Order Logic Translation via Code Generation](https://aclanthology.org/2025.naacl-long.547.pdf)
  - [Faster In-Context Learning for LLMs via N-Gram Trie Speculative Decoding](https://aclanthology.org/2025.emnlp-main.911.pdf)
  - [ALLabel: Three-stage Active Learning for LLM-based Entity Recognition using Demonstration Retrieval](https://aclanthology.org/2025.emnlp-main.1278.pdf)
- **Reasoning** (construct): *causes*, 4 papers
  > All stages utilize the in-context learning method with a few examples to maximize the reasoning ability of large language models (LLMs). (Section 4)
  - [EHRCon: Dataset for Checking Consistency between Unstructured Notes and Structured Tables in Electronic Health Records](https://proceedings.neurips.cc/paper_files/paper/2024/file/a291dad965af9bc2e39ffeb2ca1c6dc0-Paper-Datasets_and_Benchmarks_Track.pdf)
  - [Demonstration Selection for In-Context Learning via Reinforcement Learning](https://raw.githubusercontent.com/mlresearch/v267/main/assets/wang25dp/wang25dp.pdf)
  - [What Makes In-context Learning Effective for Mathematical Reasoning](https://raw.githubusercontent.com/mlresearch/v267/main/assets/liu25ac/liu25ac.pdf)
  - [MAPLE: Many-Shot Adaptive Pseudo-Labeling for In-Context Learning](https://raw.githubusercontent.com/mlresearch/v267/main/assets/chen25bo/chen25bo.pdf)
- **Out-of-distribution generalization** (construct): *causes*, 4 papers
  > We argue that context is environment, and posit that in-context learning holds the key to better domain generalization. (Section 1)
  - [Context is Environment](https://proceedings.iclr.cc/paper_files/paper/2024/file/03645743ea35690f30d795d6bac149a5-Paper-Conference.pdf)
  - [Learning to grok: Emergence of in-context learning and skill composition in modular arithmetic tasks](https://proceedings.neurips.cc/paper_files/paper/2024/file/17d60fef592086d1a5cb136f1946df59-Paper-Conference.pdf)
  - [Can In-context Learning Really Generalize to Out-of-distribution Tasks?](https://proceedings.iclr.cc/paper_files/paper/2025/file/cf7a83a5342befd11d3d65beba1be5b0-Paper-Conference.pdf)
  - [When can in-context learning generalize out of task distribution?](https://raw.githubusercontent.com/mlresearch/v267/main/assets/goddard25a/goddard25a.pdf)
- **MMLU** (measurement instrument): *measured_by*, 3 papers
  > evaluate the ICL capability of the finetuned models on two benchmarks: MMLU (Hendrycks et al., 2020) and BBH (Suzgun et al., 2022). (Section 5.3)
  - [CausalLM is not optimal for in-context learning](https://proceedings.iclr.cc/paper_files/paper/2024/file/364071531ff2398e0fb8bae31f615b69-Paper-Conference.pdf)
  - [Scaling Stick-Breaking Attention: An Efficient Implementation and In-depth Study](https://proceedings.iclr.cc/paper_files/paper/2025/file/0b9a261b9aca858b7e6ee44d8b2055be-Paper-Conference.pdf)
  - [APE: Faster and Longer Context-Augmented Generation via Adaptive Parallel Encoding](https://proceedings.iclr.cc/paper_files/paper/2025/file/ce186a37e63b37638ecd06dee6b9a355-Paper-Conference.pdf)
- **GSM8K** (measurement instrument): *measured_by*, 3 papers
  > “We quantitatively study how self-reinforced surface patterns lead to both beneﬁcial functions and detrimental effects in ICL. The experiments in this section are conducted over MMLU (Hendrycks et al., 2021) and GSM8K (Cobbe et al., 2021).”
  - [Understanding In-Context Learning from Repetitions](https://proceedings.iclr.cc/paper_files/paper/2024/file/d88f6f81e1aaf606776ffdd06fdf24ef-Paper-Conference.pdf)
  - [Scaling Stick-Breaking Attention: An Efficient Implementation and In-depth Study](https://proceedings.iclr.cc/paper_files/paper/2025/file/0b9a261b9aca858b7e6ee44d8b2055be-Paper-Conference.pdf)
  - [APE: Faster and Longer Context-Augmented Generation via Adaptive Parallel Encoding](https://proceedings.iclr.cc/paper_files/paper/2025/file/ce186a37e63b37638ecd06dee6b9a355-Paper-Conference.pdf)
- **MetaICL** (measurement instrument): *measured_by*, 3 papers
  > In the section, to validate our methodology, we employ the MetaICL dataset introduced by Min et al. (2022a), designed for in-context learning scenarios. (Section 4.1)
  - [MEND: Meta Demonstration Distillation for Efficient and Effective In-Context Learning](https://proceedings.iclr.cc/paper_files/paper/2024/file/7ce1cbededb4b0d6202847ac1b484ee8-Paper-Conference.pdf)
  - [Rethinking Invariance in In-context Learning](https://proceedings.iclr.cc/paper_files/paper/2025/file/01e8ecf628f8d9f62a1fd433d44d34ab-Paper-Conference.pdf)
  - [Generative Adapter: Contextualizing Language Models in Parameters with A Single Forward Pass](https://proceedings.iclr.cc/paper_files/paper/2025/file/447708674d7f30492ca5338b36b07d0c-Paper-Conference.pdf)
- **Robustness** (construct): *causes*, 3 papers
  > we believe that utilizing few-shot settings with example demonstrations could potentially enhance model performance and robustness. (Section 5.1)
  - [Are Multimodal LLMs Robust Against Adversarial Perturbations? RoMMath: A Systematic Evaluation on Multimodal Math Reasoning](https://aclanthology.org/2025.naacl-long.582.pdf)
  - [Iterative Vectors: In-Context Gradient Steering without Backpropagation](https://raw.githubusercontent.com/mlresearch/v267/main/assets/liu25j/liu25j.pdf)
  - [Mixture of Demonstrations for In-Context Learning](https://proceedings.neurips.cc/paper_files/paper/2024/file/a0da098e0031f58269efdcba40eedf47-Paper-Conference.pdf)
- **Time series forecasting** (behavioral indicator): *causes*, 3 papers
  > DICL projects trajectories into a disentangled feature space before performing zero-shot forecasting using a pre-trained LLM and in-context learning.
  - [Zero-shot Model-based Reinforcement Learning using Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/5fc1e662bd63c4a70b95088ba5d08cb8-Paper-Conference.pdf)
  - [From News to Forecast: Integrating Event Analysis in LLM-Based Time Series Forecasting with Reflection](https://proceedings.neurips.cc/paper_files/paper/2024/file/6aef8bffb372096ee73d98da30119f89-Paper-Conference.pdf)
  - [Time-FFM: Towards LM-Empowered Federated Foundation Model for Time Series Forecasting](https://proceedings.neurips.cc/paper_files/paper/2024/file/abc1943857a42935ceacff03c524bb44-Paper-Conference.pdf)
- **BIG-Bench Hard** (measurement instrument): *measured_by*, 2 papers
  > evaluate the ICL capability of the finetuned models on two benchmarks: MMLU (Hendrycks et al., 2020) and BBH (Suzgun et al., 2022). (Section 5.3)
  - [CausalLM is not optimal for in-context learning](https://proceedings.iclr.cc/paper_files/paper/2024/file/364071531ff2398e0fb8bae31f615b69-Paper-Conference.pdf)
  - [Block-Attention for Efficient Prefilling](https://proceedings.iclr.cc/paper_files/paper/2025/file/a03037317560b8c5f2fb4b6466d4c439-Paper-Conference.pdf)
- **lm-evaluation-harness** (measurement instrument): *measured_by*, 2 papers
  > We evaluate APE on three ICL tasks using the LM Evaluation Harness (Gao et al., 2024):: GSM8K (8-shot) (Cobbe et al., 2021a), TriviaQA (5-shot) (Joshi et al., 2017), and MMLU (5-shot) (Hendrycks et al., 2020a). (Section 5.2).
  - [APE: Faster and Longer Context-Augmented Generation via Adaptive Parallel Encoding](https://proceedings.iclr.cc/paper_files/paper/2025/file/ce186a37e63b37638ecd06dee6b9a355-Paper-Conference.pdf)
  - [DataMan: Data Manager for Pre-training Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/1abed6ee581b9ceb4e2ddf37822c7fcb-Paper-Conference.pdf)
- **Instruction following** (behavioral indicator): *causes*, 2 papers
  > “ICL can marginally help to adapt LMMs to follow instructions.”
  - [Beyond task performance: evaluating and reducing the flaws of large multimodal models with in-context-learning](https://proceedings.iclr.cc/paper_files/paper/2024/file/5df817c5dd95293ebf6d1583303a8c73-Paper-Conference.pdf)
  - [Understanding Catastrophic Forgetting in Language Models via Implicit Inference](https://proceedings.iclr.cc/paper_files/paper/2024/file/692ae28fda9bfbde7c01b13bf5a03395-Paper-Conference.pdf)
- **Privacy preservation** (construct): *causes*, 2 papers
  > We study the problem of in-context learning (ICL) with large language models (LLMs) on private datasets. This scenario poses privacy risks, as LLMs may leak or regurgitate the private examples demonstrated in the prompt. (Section 1)
  - [Privacy-Preserving In-Context Learning with Differentially Private Few-Shot Generation](https://proceedings.iclr.cc/paper_files/paper/2024/file/8cb564df771e9eacbfe9d72bd46a24a9-Paper-Conference.pdf)
  - [Privacy-Preserving In-Context Learning for Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/572cd21bd5dea96b065476b77d21b3c6-Paper-Conference.pdf)
- **Logical reasoning** (construct): *causes*, 2 papers
  > It has been shown that including task demonstrations in the prompt can enhance the capability of language models to apply common sense and logical reasoning [65, 72] and learn patterns from the supplied demonstrations [14], significantly enhancing the flexibility and generality of language models. (Introduction)
  - [DETAIL: Task DEmonsTration Attribution for Interpretable In-context Learning](https://proceedings.neurips.cc/paper_files/paper/2024/file/2ceda49041816da6d5a34eb3b612607f-Paper-Conference.pdf)
  - [From Unstructured Data to In-Context Learning: Exploring What Tasks Can Be Learned and When](https://proceedings.neurips.cc/paper_files/paper/2024/file/1da38b872e19f1f4a3c2846720e8f64a-Paper-Conference.pdf)
- **Calibration** (construct): *causes*, 2 papers
  > current exemplar selection strategies, by largely ignoring calibration, risk scenarios where gains in accuracy are achieved at the expense of degradation in calibration (Zhang et al., 2024b).
  - [COM-BOM: Bayesian Exemplar Search for Efficiently Exploring the Accuracy-Calibration Pareto Frontier](https://aclanthology.org/2025.emnlp-main.1027.pdf)
  - [Gen-Z: Generative Zero-Shot Text Classification with Contextualized Label Descriptions](https://proceedings.iclr.cc/paper_files/paper/2024/file/af7cc9e2366b8f8837a6ef339810277a-Paper-Conference.pdf)
- **HellaSwag** (measurement instrument): *measured_by*, 1 paper
  > IP = 1 N g PN g j=1 ˆa T e j N , which is the average in-context performance on N g general evaluation tasks... We set N g = 4 general evaluation tasks, covering Hellaswag (Zellers et al., 2019), CommonsenseQA (Talmor et al., 2018), Alpaca (Hendrycks et al., 2020), and BBH-Object-Count (Srivastava et al., 2022) (Section 3)
  - [Unlocking the Power of Function Vectors for Characterizing and Mitigating Catastrophic Forgetting in Continual Instruction Tuning](https://proceedings.iclr.cc/paper_files/paper/2025/file/74fc5575632191d96881d8015f79dde3-Paper-Conference.pdf)
- **Adaptability** (construct): *causes*, 1 paper
  > By leveraging in-context information during both pre-training and inference, Zebra dynamically adapts to new tasks by conditioning on input sequences that incorporate context example trajectories. (Abstract)
  - [Zebra: In-Context Generative Pretraining for Solving Parametric PDEs](https://raw.githubusercontent.com/mlresearch/v267/main/assets/serrano25a/serrano25a.pdf)
- **Embodied planning** (behavioral indicator): *causes*, 1 paper
  > These experiments confirm that the in-context example selecting strategy has a significant impact on the performance of LLM-based task planners (Section 6.1).
  - [LoTa-Bench: Benchmarking Language-oriented Task Planners for Embodied Agents](https://proceedings.iclr.cc/paper_files/paper/2024/file/e91fb65c6324a984ea9ef39a5b84af04-Paper-Conference.pdf)
- **SST-5** (measurement instrument): *measured_by*, 1 paper
  > We conduct experiments to investigate the correlation between subset influence and its corresponding in-context learning performance. (Section 4.3.1, Figure 4a on SST-5)
  - [IDEAL: Influence-Driven Selective Annotations Empower In-Context Learners in Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/a7f90da65dd41d699d00e95700e6fa1e-Paper-Conference.pdf)
- **MNLI** (measurement instrument): *measured_by*, 1 paper
  > We conduct experiments to investigate the correlation between subset influence and its corresponding in-context learning performance. (Section 4.3.1, Figure 4b on MNLI)
  - [IDEAL: Influence-Driven Selective Annotations Empower In-Context Learners in Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/a7f90da65dd41d699d00e95700e6fa1e-Paper-Conference.pdf)
- **Abstention** (behavioral indicator): *causes*, 1 paper
  > “ICL significantly improves abstention.”
  - [Beyond task performance: evaluating and reducing the flaws of large multimodal models with in-context-learning](https://proceedings.iclr.cc/paper_files/paper/2024/file/5df817c5dd95293ebf6d1583303a8c73-Paper-Conference.pdf)
- **MS-COCO** (measurement instrument): *measured_by*, 1 paper
  > The models are evaluated on four-shot and eight-shot in-context learning performance on various captioning benchmarks (COCO (Karpathy test) [Lin et al., 2014] and TextCaps (validation) [Sidorov et al., 2020]) and visual question answering datasets (VQAv2 (validation) [Agrawal et al., 2015], OK-VQA (validation) [Marino et al., 2019], TextVQA (validation) [Singh et al., 2019], and VizWiz (validation) [Gurari et al., 2018]). (Section 4.2)
  - [MINT-1T: Scaling Open-Source Multimodal Data by 10x: A Multimodal Dataset with One Trillion Tokens](https://proceedings.neurips.cc/paper_files/paper/2024/file/40b9196c25fe1d64d87ca3a80a91d0ce-Paper-Datasets_and_Benchmarks_Track.pdf)
- **VQA-v2** (measurement instrument): *measured_by*, 1 paper
  > The models are evaluated on four-shot and eight-shot in-context learning performance on various captioning benchmarks (COCO (Karpathy test) [Lin et al., 2014] and TextCaps (validation) [Sidorov et al., 2020]) and visual question answering datasets (VQAv2 (validation) [Agrawal et al., 2015], OK-VQA (validation) [Marino et al., 2019], TextVQA (validation) [Singh et al., 2019], and VizWiz (validation) [Gurari et al., 2018]). (Section 4.2)
  - [MINT-1T: Scaling Open-Source Multimodal Data by 10x: A Multimodal Dataset with One Trillion Tokens](https://proceedings.neurips.cc/paper_files/paper/2024/file/40b9196c25fe1d64d87ca3a80a91d0ce-Paper-Datasets_and_Benchmarks_Track.pdf)
- **OK-VQA** (measurement instrument): *measured_by*, 1 paper
  > The models are evaluated on four-shot and eight-shot in-context learning performance on various captioning benchmarks (COCO (Karpathy test) [Lin et al., 2014] and TextCaps (validation) [Sidorov et al., 2020]) and visual question answering datasets (VQAv2 (validation) [Agrawal et al., 2015], OK-VQA (validation) [Marino et al., 2019], TextVQA (validation) [Singh et al., 2019], and VizWiz (validation) [Gurari et al., 2018]). (Section 4.2)
  - [MINT-1T: Scaling Open-Source Multimodal Data by 10x: A Multimodal Dataset with One Trillion Tokens](https://proceedings.neurips.cc/paper_files/paper/2024/file/40b9196c25fe1d64d87ca3a80a91d0ce-Paper-Datasets_and_Benchmarks_Track.pdf)
- **TextVQA** (measurement instrument): *measured_by*, 1 paper
  > The models are evaluated on four-shot and eight-shot in-context learning performance on various captioning benchmarks (COCO (Karpathy test) [Lin et al., 2014] and TextCaps (validation) [Sidorov et al., 2020]) and visual question answering datasets (VQAv2 (validation) [Agrawal et al., 2015], OK-VQA (validation) [Marino et al., 2019], TextVQA (validation) [Singh et al., 2019], and VizWiz (validation) [Gurari et al., 2018]). (Section 4.2)
  - [MINT-1T: Scaling Open-Source Multimodal Data by 10x: A Multimodal Dataset with One Trillion Tokens](https://proceedings.neurips.cc/paper_files/paper/2024/file/40b9196c25fe1d64d87ca3a80a91d0ce-Paper-Datasets_and_Benchmarks_Track.pdf)
- **VizWiz** (measurement instrument): *measured_by*, 1 paper
  > The models are evaluated on four-shot and eight-shot in-context learning performance on various captioning benchmarks (COCO (Karpathy test) [Lin et al., 2014] and TextCaps (validation) [Sidorov et al., 2020]) and visual question answering datasets (VQAv2 (validation) [Agrawal et al., 2015], OK-VQA (validation) [Marino et al., 2019], TextVQA (validation) [Singh et al., 2019], and VizWiz (validation) [Gurari et al., 2018]). (Section 4.2)
  - [MINT-1T: Scaling Open-Source Multimodal Data by 10x: A Multimodal Dataset with One Trillion Tokens](https://proceedings.neurips.cc/paper_files/paper/2024/file/40b9196c25fe1d64d87ca3a80a91d0ce-Paper-Datasets_and_Benchmarks_Track.pdf)
- **Commonsense reasoning** (construct): *causes*, 1 paper
  > It has been shown that including task demonstrations in the prompt can enhance the capability of language models to apply common sense and logical reasoning [65, 72] and learn patterns from the supplied demonstrations [14], significantly enhancing the flexibility and generality of language models. (Introduction)
  - [DETAIL: Task DEmonsTration Attribution for Interpretable In-context Learning](https://proceedings.neurips.cc/paper_files/paper/2024/file/2ceda49041816da6d5a34eb3b612607f-Paper-Conference.pdf)
- **Schema matching** (behavioral indicator): *causes*, 1 paper
  > With in-context learning, off-the-shelf LLM can solve attribute alignment without fine-tuning. (Section 4.1)
  - [Tackling Uncertain Correspondences for Multi-Modal Entity Alignment](https://proceedings.neurips.cc/paper_files/paper/2024/file/d7ed243b13831bdd468f35039936bcef-Paper-Conference.pdf)
- **Query rewriting** (behavioral indicator): *causes*, 1 paper
  > we leverage the ICL capability of large language models (LLMs) [23, 30] to generate automatic keyword prompts similar to manually crafted prompts (Section 1).
  - [AP-Adapter: Improving Generalization of Automatic Prompts on Unseen Text-to-Image Diffusion Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/b2077e6d66da612fcb701589efa9ce88-Paper-Conference.pdf)
- **CommonsenseQA** (measurement instrument): *measured_by*, 1 paper
  > IP = 1 N g PN g j=1 ˆa T e j N , which is the average in-context performance on N g general evaluation tasks... We set N g = 4 general evaluation tasks, covering Hellaswag (Zellers et al., 2019), CommonsenseQA (Talmor et al., 2018), Alpaca (Hendrycks et al., 2020), and BBH-Object-Count (Srivastava et al., 2022) (Section 3)
  - [Unlocking the Power of Function Vectors for Characterizing and Mitigating Catastrophic Forgetting in Continual Instruction Tuning](https://proceedings.iclr.cc/paper_files/paper/2025/file/74fc5575632191d96881d8015f79dde3-Paper-Conference.pdf)
- **Alpaca instruction dataset** (measurement instrument): *measured_by*, 1 paper
  > IP = 1 N g PN g j=1 ˆa T e j N , which is the average in-context performance on N g general evaluation tasks... We set N g = 4 general evaluation tasks, covering Hellaswag (Zellers et al., 2019), CommonsenseQA (Talmor et al., 2018), Alpaca (Hendrycks et al., 2020), and BBH-Object-Count (Srivastava et al., 2022) (Section 3)
  - [Unlocking the Power of Function Vectors for Characterizing and Mitigating Catastrophic Forgetting in Continual Instruction Tuning](https://proceedings.iclr.cc/paper_files/paper/2025/file/74fc5575632191d96881d8015f79dde3-Paper-Conference.pdf)
- **BBH Object Counting** (measurement instrument): *measured_by*, 1 paper
  > IP = 1 N g PN g j=1 ˆa T e j N , which is the average in-context performance on N g general evaluation tasks... We set N g = 4 general evaluation tasks, covering Hellaswag (Zellers et al., 2019), CommonsenseQA (Talmor et al., 2018), Alpaca (Hendrycks et al., 2020), and BBH-Object-Count (Srivastava et al., 2022) (Section 3)
  - [Unlocking the Power of Function Vectors for Characterizing and Mitigating Catastrophic Forgetting in Continual Instruction Tuning](https://proceedings.iclr.cc/paper_files/paper/2025/file/74fc5575632191d96881d8015f79dde3-Paper-Conference.pdf)
- **DROP** (measurement instrument): *measured_by*, 1 paper
  > Please note that, among them, BBH, DROP, GSM8K, and MATH are ICL tasks with several independent in-context examples. (Section 3.1)
  - [Block-Attention for Efficient Prefilling](https://proceedings.iclr.cc/paper_files/paper/2025/file/a03037317560b8c5f2fb4b6466d4c439-Paper-Conference.pdf)
- **Compositional generalization** (construct): *causes*, 1 paper
  > What is striking is that learning in-context can under some circumstances lead to compositional generalization, that is generalization to unseen combinations of previously observed constituents
  - [Attention as a Hypernetwork](https://proceedings.iclr.cc/paper_files/paper/2025/file/abfa542f546df3c6c35695ec8d5bf4b9-Paper-Conference.pdf)
- **MAWPS** (measurement instrument): *measured_by*, 1 paper
  > We evaluate DiffuLLaMA’s math reasoning and in-context learning ability by evaluating on MAWPS (Koncel-Kedziorski et al., 2016) (Section 4.2).
  - [Scaling Diffusion Language Models via Adaptation from Autoregressive Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/0fa81c3f0d57f95b8776de3a248ef0ed-Paper-Conference.pdf)
- **Planning** (construct): *causes*, 1 paper
  > In this work, we explore how to improve the model planning capability through in-context learning (ICL), specifically, what signals can help select the exemplars. (Section Abstract)
  - [Improving Large Language Model Planning with Action Sequence Similarity](https://proceedings.iclr.cc/paper_files/paper/2025/file/b18c6549c77411d92e645027a25838a8-Paper-Conference.pdf)
- **Personalization** (construct): *causes*, 1 paper
  > This approach fully harnesses the in-context learning capabilities of MLLMs, allowing them to adapt to new individuals without additional training. (Section 3)
  - [Personalized Visual Instruction Tuning](https://proceedings.iclr.cc/paper_files/paper/2025/file/6b69dcf999ee89f48d08c6c9881a4c0d-Paper-Conference.pdf)
- **TriviaQA** (measurement instrument): *measured_by*, 1 paper
  > "We evaluate APE on three ICL tasks using the LM Evaluation Harness (Gao et al., 2024):: ... TriviaQA (5-shot)"
  - [APE: Faster and Longer Context-Augmented Generation via Adaptive Parallel Encoding](https://proceedings.iclr.cc/paper_files/paper/2025/file/ce186a37e63b37638ecd06dee6b9a355-Paper-Conference.pdf)
- **Text-to-SQL** (behavioral indicator): *causes*, 1 paper
  > With the demonstrations, our method fully leverages in-context learning capability and generate the target SQL correctly. (Section 3)
  - [DCG-SQL: Enhancing In-Context Learning for Text-to-SQL with Deep Contextual Schema Link Graph](https://aclanthology.org/2025.acl-long.748.pdf)
- **LongBench** (measurement instrument): *measured_by*, 1 paper
  > “LongBench (in-context learning and code completion)”
  - [LongRoPE2: Near-Lossless LLM Context Window Scaling](https://raw.githubusercontent.com/mlresearch/v267/main/assets/shang25a/shang25a.pdf)
- **Image editing** (behavioral indicator): *causes*, 1 paper
  > Notably, Orthus exhibits in-context learning capacity by performing image editing successfully when provided with examples rather than explicit instructions, which is not included in the training dataset. (Figure 3)
  - [Orthus: Autoregressive Interleaved Image-Text Generation with Modality-Specific Heads](https://raw.githubusercontent.com/mlresearch/v267/main/assets/kou25a/kou25a.pdf)
- **Hallucination detection** (behavioral indicator): *causes*, 1 paper
  > These results imply that In-Context Learning can immediately enhance hallucination detection performance for certain models, datasets, and tasks, particularly when balanced examples with pre-/post-negated text and hallucination/no-hallucination cases are included.
  - [The Impact of Negated Text on Hallucination with Large Language Models](https://aclanthology.org/2025.emnlp-main.684.pdf)
- **Knowledge application** (construct): *causes*, 1 paper
  > In-Context Learning (ICL) enhances the generalization and knowledge utilization capabilities of Large Language Models (LLMs) (Abstract).
  - [Faster In-Context Learning for LLMs via N-Gram Trie Speculative Decoding](https://aclanthology.org/2025.emnlp-main.911.pdf)
- **Length bias** (construct): *causes*, 1 paper
  > This indicates that models can pick up length biases in-context. (Section 4.2)
  - [In-Context Learning (and Unlearning) of Length Biases](https://aclanthology.org/2025.naacl-long.390.pdf)

### → In-context learning
- **Representation learning** (construct): *causes*, 3 papers
  > we show that ICL can improve upon the a priori optimal rate when the task class basis resides in a coarser Besov space by learning to encode informative basis representations, emphasizing the importance of pretraining on diverse tasks. (Section 1)
  - [Transformers are Minimax Optimal Nonparametric In-Context Learners](https://proceedings.neurips.cc/paper_files/paper/2024/file/c11daad0a48ea5f3c5c6390c7b060720-Paper-Conference.pdf)
  - [Towards Understanding How Transformers Learn In-context Through a Representation Learning Lens](https://proceedings.neurips.cc/paper_files/paper/2024/file/01a8d63f9cb6dcbaa3092ccddd2075ac-Paper-Conference.pdf)
  - [How Do Transformers Learn In-Context Beyond Simple Functions? A Case Study on Learning with Representations](https://proceedings.iclr.cc/paper_files/paper/2024/file/c9694bf4f9bf3626f7d21158bab74f8e-Paper-Conference.pdf)
- **Chain of thought** (behavioral indicator): *causes*, 2 papers
  > The foundational method for inducing in-context learning is the chain of thought approach
  - [Chain of Thoughtlessness? An Analysis of CoT in Planning](https://proceedings.neurips.cc/paper_files/paper/2024/file/3365d974ce309623bd8151082d78206c-Paper-Conference.pdf)
  - [Linear-Time Demonstration Selection for In-Context Learning via Gradient Estimation](https://aclanthology.org/2025.emnlp-main.832.pdf)
- **Catastrophic forgetting** (behavioral indicator): *causes*, 2 papers
  > We introduce Copain, a new benchmark for in-context learning (ICL), which reveals catastrophic forgetting early on CPT when English is not included. This in turn damages the ability of the model to generalize to downstream prompts in the target language as measured by perplexity...
  - [Emergent Abilities of Large Language Models under Continued Pre-training for Language Adaptation](https://aclanthology.org/2025.acl-long.1547.pdf)
  - [Unlocking the Power of Function Vectors for Characterizing and Mitigating Catastrophic Forgetting in Continual Instruction Tuning](https://proceedings.iclr.cc/paper_files/paper/2025/file/74fc5575632191d96881d8015f79dde3-Paper-Conference.pdf)
- **Generalization** (construct): *causes*, 1 paper
  > Our theoretical results of population loss reveal that model generalization, tightly with ICL abilities, is influenced by model size, optimization iterations, pre-training data and prompt length. This further demonstrates that ICL emerges from the excellent generalization of sequences and topics (Section 4.1 and Section 4.2).
  - [Towards Auto-Regressive Next-Token Prediction: In-context Learning Emerges from Generalization](https://proceedings.iclr.cc/paper_files/paper/2025/file/eedf422d321a20b2bd5e947c57c82e96-Paper-Conference.pdf)
- **Memorization** (construct): *causes*, 1 paper
  > we show that fine-tuning an LLM (Gemini Nano v1 Gemini Team, Google, 2023) to memorize certain data can result in a reduction of its ICL ability. (Section 1)
  - [Toward Understanding In-context vs. In-weight Learning](https://proceedings.iclr.cc/paper_files/paper/2025/file/ae338b3fe6624798efa80b6581924028-Paper-Conference.pdf)

### Associated with
- **In-weights learning** (construct), 3 papers
  > In-context learning (ICL) is the ability to predict the response to a query based on illustrative examples presented in the context, without any additional weight updates. This form of learning contrasts with in-weights learning (IWL) of query-response relationships encoded in the weights of the network.
  - [The mechanistic basis of data dependence and abrupt learning in an in-context classification task](https://proceedings.iclr.cc/paper_files/paper/2024/file/540a3bf4863672cdaebfed69fa2ce335-Paper-Conference.pdf)
  - [MLPs Learn In-Context on Regression and Classification Tasks](https://proceedings.iclr.cc/paper_files/paper/2025/file/62302a24b04589f9f9cdd5b02c344b6c-Paper-Conference.pdf)
  - [Toward Understanding In-context vs. In-weight Learning](https://proceedings.iclr.cc/paper_files/paper/2025/file/ae338b3fe6624798efa80b6581924028-Paper-Conference.pdf)
- **Meta-learning** (construct), 3 papers
  > Broadly speaking, current research identifies two main approaches to explain the ICL mechanism (Dong et al., 2024; Li et al., 2024): 1) Meta-learning, 2) Knowledge retrieval.
  - [Learning vs Retrieval: The Role of In-Context Examples in Regression with Large Language Models](https://aclanthology.org/2025.naacl-long.417.pdf)
  - [Beyond Induction Heads: In-Context Meta Learning Induces Multi-Phase Circuit Emergence](https://raw.githubusercontent.com/mlresearch/v267/main/assets/minegishi25a/minegishi25a.pdf)
  - [On Understanding Attention-Based In-Context Learning for Categorical Data](https://raw.githubusercontent.com/mlresearch/v267/main/assets/wang25u/wang25u.pdf)
- **Text classification** (behavioral indicator), 3 papers
  > We evaluate the in-context learnig ability of ICLM using 32 demonstration examples. We use seven text classification datasets... (Section 3.3.2)
  - [In-Context Pretraining: Language Modeling Beyond Document Boundaries](https://proceedings.iclr.cc/paper_files/paper/2024/file/a1fe2365abdb691332537990a6385909-Paper-Conference.pdf)
  - [Demonstration Selection for In-Context Learning via Reinforcement Learning](https://raw.githubusercontent.com/mlresearch/v267/main/assets/wang25dp/wang25dp.pdf)
  - [Implicit In-context Learning](https://proceedings.iclr.cc/paper_files/paper/2025/file/fc034d186280f55370b6aca7a3285a65-Paper-Conference.pdf)
- **Few-shot task performance** (behavioral indicator), 3 papers
  > "Prompting with task-specific demonstrations (i.e., in-context learning (Brown et al., 2020))"
  - [Generative Adapter: Contextualizing Language Models in Parameters with A Single Forward Pass](https://proceedings.iclr.cc/paper_files/paper/2025/file/447708674d7f30492ca5338b36b07d0c-Paper-Conference.pdf)
  - [Text-space Graph Foundation Models: Comprehensive Benchmarks and New Insights](https://proceedings.neurips.cc/paper_files/paper/2024/file/0e0b39c69663e9c073739adf547ed778-Paper-Datasets_and_Benchmarks_Track.pdf)
  - [Which Attention Heads Matter for In-Context Learning?](https://raw.githubusercontent.com/mlresearch/v267/main/assets/yin25e/yin25e.pdf)
- **Zero-shot generalization** (construct), 2 papers
  > our method randomly samples a varying number of examples during training, endowing the embedding model with in-context learning abilities while maintaining its zero-shot capabilities. (Abstract)
  - [Making Text Embedders Few-Shot Learners](https://proceedings.iclr.cc/paper_files/paper/2025/file/5eba8556ce2d1afff57591464d48fbc3-Paper-Conference.pdf)
  - [Zero-shot forecasting of chaotic systems](https://proceedings.iclr.cc/paper_files/paper/2025/file/ea4d65c59073e8faf79222654d25fbe2-Paper-Conference.pdf)
- **Knowledge transfer** (construct), 2 papers
  > Moreover, the absence of the need to update model parameters also allows a good attribution result for ICL to be transferable across different language models. (Introduction)
  - [DETAIL: Task DEmonsTration Attribution for Interpretable In-context Learning](https://proceedings.neurips.cc/paper_files/paper/2024/file/2ceda49041816da6d5a34eb3b612607f-Paper-Conference.pdf)
  - [BenTo: Benchmark Reduction with In-Context Transferability](https://proceedings.iclr.cc/paper_files/paper/2025/file/4798eef078de031518beaf54f4b5fb5f-Paper-Conference.pdf)
- **Key-value retrieval** (behavioral indicator), 2 papers
  > “we evaluate the capacity of various architectures to in-context learn associative recall”
  - [Is attention required for ICL? Exploring the Relationship Between Model Architecture and In-Context Learning Ability](https://proceedings.iclr.cc/paper_files/paper/2024/file/ea6d17af54f827336fc8fed27ca0319d-Paper-Conference.pdf)
  - [Orchid: Flexible and Data-Dependent Convolution for Sequence Modeling](https://proceedings.neurips.cc/paper_files/paper/2024/file/8ccc5ec30a8d46793d790e2216efd40d-Paper-Conference.pdf)
- **Consistency** (construct), 1 paper
  > Besides confirming the existence of ICL ability, we are particularly interested in ... determining if our trained models demonstrate consistency, i.e., whether their performance converges in probability to some ceiling.
  - [Is attention required for ICL? Exploring the Relationship Between Model Architecture and In-Context Learning Ability](https://proceedings.iclr.cc/paper_files/paper/2024/file/ea6d17af54f827336fc8fed27ca0319d-Paper-Conference.pdf)
- **In-context linear regression** (behavioral indicator), 1 paper
  > Based on our proposed training algorithm, empirical evidence demonstrates that looped transformer can be trained from scratch to in-context learn data generated from linear functions, sparse linear functions, decision trees, and 2-layer neural networks. (Section 1)
  - [Looped Transformers are Better at Learning Learning Algorithms](https://proceedings.iclr.cc/paper_files/paper/2024/file/b8402301e7f06bdc97a31bfaa653dc32-Paper-Conference.pdf)
- **Analogical reasoning** (construct), 1 paper
  > "Explicitly prompting them to recall relevant problems and solutions in the context guides LLMs to perform in-context learning to solve new problems."
  - [Large Language Models as Analogical Reasoners](https://proceedings.iclr.cc/paper_files/paper/2024/file/4990dad2c1696224de42573d0222554a-Paper-Conference.pdf)
- **Selectivity** (construct), 1 paper
  > In this paper, we give theoretical grounding to the selectivity mechanism, often linked to in-context learning, using tools from Rough Path Theory.
  - [Theoretical Foundations of Deep Selective State-Space Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/e6231c5f46598cfd09ff1970524e0436-Paper-Conference.pdf)
- **Contextual understanding** (construct), 1 paper
  > constraining their application in tasks demanding extensive contextual awareness, such as in-context learning [28, 46] (Introduction).
  - [Mixture of In-Context Experts Enhance LLMs' Long Context Awareness](https://proceedings.neurips.cc/paper_files/paper/2024/file/91315fbb83ce353ae5538cba395f70d1-Paper-Conference.pdf)
- **Expressive power** (construct), 1 paper
  > We theoretically prove that ICL with transformer is expressive enough to mimic existing meta-learners. (Section 1)
  - [Why In-Context Learning Models are Good Few-Shot Learners?](https://proceedings.iclr.cc/paper_files/paper/2025/file/6c7ca1889f01a9b767c631686fb5fd24-Paper-Conference.pdf)
- **Low-test-error preference** (construct), 1 paper
  > We theoretically prove the low-test-error preference of ICL prediction, i.e., the ICL prediction prefers to implement the pretraining function with low test error (Section 5.1).
  - [Can In-context Learning Really Generalize to Out-of-distribution Tasks?](https://proceedings.iclr.cc/paper_files/paper/2025/file/cf7a83a5342befd11d3d65beba1be5b0-Paper-Conference.pdf)
- **Input regurgitation** (behavioral indicator), 1 paper
  > We attribute this success to foundation models’ ability to perform in-context learning and identify context parroting as a simple mechanism used by these models to capture the long-term behavior of chaotic dynamical systems. (Abstract)
  - [Zero-shot forecasting of chaotic systems](https://proceedings.iclr.cc/paper_files/paper/2025/file/ea4d65c59073e8faf79222654d25fbe2-Paper-Conference.pdf)
- **Image classification** (behavioral indicator), 1 paper
  > we design a 5-way 1-shot classification scenario to evaluate the performance with in-context learning (Section 4.1)
  - [Bridging Compressed Image Latents and Multimodal Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/17061a94c3c7fda5fa24bbdd1832fa99-Paper-Conference.pdf)
- **In-context prediction** (behavioral indicator), 1 paper
  > The ICL class of functions H uses only labels in the context to make a prediction
  - [Toward Understanding In-context vs. In-weight Learning](https://proceedings.iclr.cc/paper_files/paper/2025/file/ae338b3fe6624798efa80b6581924028-Paper-Conference.pdf)
- **Grammatical error correction** (behavioral indicator), 1 paper
  > Our work extends the use of LLMs in multilingual GEC through an easy-to-use in-context learning approach. (Section 2.1)
  - [Explanation based In-Context Demonstrations Retrieval for Multilingual Grammatical Error Correction](https://aclanthology.org/2025.naacl-long.251.pdf)
- **Controllability** (construct), 1 paper
  > The prompt steerability of a model is related to how well a model can learn from in-context examples (Brown, 2020; Wies et al., 2024). (Section 1.1)
  - [Evaluating the Prompt Steerability of Large Language Models](https://aclanthology.org/2025.naacl-long.400.pdf)
- **Knowledge retrieval** (behavioral indicator), 1 paper
  > Broadly speaking, current research identifies two main approaches to explain the ICL mechanism (Dong et al., 2024; Li et al., 2024): 1) Meta-learning, 2) Knowledge retrieval.
  - [Learning vs Retrieval: The Role of In-Context Examples in Regression with Large Language Models](https://aclanthology.org/2025.naacl-long.417.pdf)
- **Long-context understanding** (construct), 1 paper
  > As LLMs have stronger capabilities and wider applications (Yang et al., 2024), its long-context capability becomes a vital bottleneck for various use cases (e.g. in-context learning, retrieval augmented generation, agent workflow etc.) (Agarwal et al., 2024; Xu et al., 2023; Weng, 2023). (Introduction)
  - [LongLeader: A Comprehensive Leaderboard for Large Language Models in Long-context Scenarios](https://aclanthology.org/2025.naacl-long.439.pdf)
- **Task learning** (construct), 1 paper
  > In effective ICL, the model infers the underlying task from the examples provided and refines its predictions based on the inferred task. (Section 2.1)
  - [Beyond Induction Heads: In-Context Meta Learning Induces Multi-Phase Circuit Emergence](https://raw.githubusercontent.com/mlresearch/v267/main/assets/minegishi25a/minegishi25a.pdf)
- **Latent variable inference** (construct), 1 paper
  > A plausible hypothesis behind the success of ICL is that since many tasks are based on some low-dimensional latents (e.g., complex games are described completely through their rules, linear regression through its underlying coefficients), Transformers might generalize to novel queries by inferring the task latents from the context
  - [Does learning the right latent variables necessarily improve in-context learning?](https://raw.githubusercontent.com/mlresearch/v267/main/assets/mittal25a/mittal25a.pdf)
- **Tabular classification** (behavioral indicator), 1 paper
  > Leveraging the in-context learning (ICL) capability of Large Language Models (LLMs) for tabular classification has gained significant attention for its training-free adaptability across diverse datasets. (Abstract)
  - [TabFlex: Scaling Tabular Learning to Millions with Linear Attention](https://raw.githubusercontent.com/mlresearch/v267/main/assets/zeng25b/zeng25b.pdf)
- **In-context classification** (behavioral indicator), 1 paper
  > In this work, we study the training dynamics of a single-layer transformer for both binary and multi-class classification of Gaussian mixtures during ICL, a fundamental problem in machine learning.
  - [On the Training Convergence of Transformers for In-Context Classification of Gaussian Mixtures](https://raw.githubusercontent.com/mlresearch/v267/main/assets/shen25q/shen25q.pdf)
- **Stability** (construct), 1 paper
  > We prove that the reasoning efficacy (measured by empirical prediction loss) can be bounded by an LLM-oriented semantic similarity and an inference stability of demonstrations, which is general for both one-shot and few-shot scenarios. (Abstract)
  - [What Makes In-context Learning Effective for Mathematical Reasoning](https://raw.githubusercontent.com/mlresearch/v267/main/assets/liu25ac/liu25ac.pdf)
- **Text summarization** (behavioral indicator), 1 paper
  > ICL has proven remarkably successful in handling complex tasks, including summarization (Jain et al., 2023; Baek et al., 2024) and reasoning (Wang et al., 2024a; Lee et al., 2024; Chen et al., 2024b). (Section 2)
  - [MAPLE: Many-Shot Adaptive Pseudo-Labeling for In-Context Learning](https://raw.githubusercontent.com/mlresearch/v267/main/assets/chen25bo/chen25bo.pdf)
- **Question answering** (behavioral indicator), 1 paper
  > For question-answering (QA) tasks, in-context learning (ICL) enables language models (LMs) to generate responses without modifying their parameters by leveraging examples provided in the input. (Abstract)
  - [Federated In-Context Learning: Iterative Refinement for Improved Answer Quality](https://raw.githubusercontent.com/mlresearch/v267/main/assets/wang25db/wang25db.pdf)
- **Emergent abilities** (construct), 1 paper
  > It significantly outperforms Transformer baselines in language and vision tasks and improves emergent abilities such as in-context learning with minimal overhead. (Section 5).
  - [MUDDFormer: Breaking Residual Bottlenecks in Transformers via Multiway Dynamic Dense Connections](https://raw.githubusercontent.com/mlresearch/v267/main/assets/xiao25d/xiao25d.pdf)
- **Factual recall** (behavioral indicator), 1 paper
  > While fact recall begins to significantly degrade when more than 30% of weights are removed through pruning, in-context learning capabilities show remarkable resilience, maintaining performance even with aggressive pruning of up to 60-70% of weights. (Section 5.1)
  - [Position: Enough of Scaling LLMs! Lets Focus on Downscaling](https://raw.githubusercontent.com/mlresearch/v267/main/assets/goel25c/goel25c.pdf)
- **Previous-token attention** (behavioral indicator), 1 paper
  > "when Layer 1 acts as previous token heads, the network exhibits ICL"
  - [Strategy Coopetition Explains the Emergence and Transience of In-Context Learning](https://raw.githubusercontent.com/mlresearch/v267/main/assets/singh25c/singh25c.pdf)
- **Task alignment** (construct), 1 paper
  > The alignment refers to the model’s ability to follow task-specific instructions and demonstrations, i.e., its in-context learning ability. (Section 2)
  - [Targeted Distillation for Sentiment Analysis](https://aclanthology.org/2025.emnlp-main.1127.pdf)
- **Text-to-speech synthesis** (behavioral indicator), 1 paper
  > We conduct experiments to validate the effectiveness of LLM-Codec in an in-context learning setting. ... we evaluate LLM-Codec on various audio understanding and generation tasks, such as speech emotion classification, audio classification, simple text-to-speech, and speech denoising.
  - [UniAudio 1.5: Large Language Model-Driven Audio Codec is A Few-Shot Audio Task Learner](https://proceedings.neurips.cc/paper_files/paper/2024/file/6801fa3fd290229efc490ee0cf1c5687-Paper-Conference.pdf)
- **Zero-shot inference** (behavioral indicator), 1 paper
  > our unsupervised ICL method improves upon the zero-shot inference by using a few self-generated examples as a context that are labeled by the model itself, thus without requiring any labeled examples. (Section 2)
  - [Large (Vision) Language Models are Unsupervised In-Context Learners](https://proceedings.iclr.cc/paper_files/paper/2025/file/3e887bf77d0ba6db38802e552a0d81d2-Paper-Conference.pdf)
- **Recursive stability** (construct), 1 paper
  > 2. Application to Transformers in In-Context Learning: This paper is the first to extend the theoretical framework to transformer models in in-context learning. We prove that transformers in this setting satisfy recursive stability
  - [A Theoretical Perspective: How to Prevent Model Collapse in Self-consuming Training Loops](https://proceedings.iclr.cc/paper_files/paper/2025/file/e92e6d20f7b5db5c2a1b23964d170fe2-Paper-Conference.pdf)
- **LASER** (measurement instrument), 1 paper
  > "LASER that leverages state-of-the-art LLMs’ in-context learning abilities to learn from prompts with detailed examples."
  - [LASER: An LLM-based ASR Scoring and Evaluation Rubric](https://aclanthology.org/2025.emnlp-main.1257.pdf)
