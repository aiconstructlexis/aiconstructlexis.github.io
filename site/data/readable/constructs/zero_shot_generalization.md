# Zero-shot generalization
**Type:** Construct  
**Supporting papers:** 64  
**Also known as:** Zero-shot generalizability, Zero-shot transfer, Zero-shot transferability, Zero-shot control, Zero-shot task classification, Zero-shot learning, Zero-shot learning ability, Zero-shot capability, Zero-shot inference, Zero-shot prompting capability, Zero-shot adaptability, Zero-shot performance  

## State of the Field

**Space of definitions.** Across the surveyed work, the prevailing usage treats this as a model ability to perform on unseen targets without task-specific exposure, usually framed as unseen tasks, datasets, domains, policies, constraints, objects, or categories. Most definitions also exclude task-specific fine-tuning or labeled examples, and many add that the model relies only on instructions or natural language descriptions, for example asking whether models can "generalize to novel instructions" or "follow unseen guidelines." A smaller line of work narrows the construct to specific settings such as clinical entity extraction, dialogue understanding, forecasting, control, or task classification, but the shared core remains zero-shot performance on previously unseen targets.

**Space of facets.** Papers use a broad family of near-synonymous labels for this construct, including zero-shot generalizability, zero-shot learning, zero-shot transfer, zero-shot transferability, zero-shot capability, zero-shot inference, zero-shot adaptability, and zero-shot performance. The same family of terms is applied both to broad cross-task ability and to narrower variants tied to instruction-only use, open-vocabulary dialogue understanding, unseen-domain forecasting, planning under unseen constraints, or natural-language-specified control. One paper also separates zero-shot generalization tests from compositional generalization tests and IID tests, showing that some authors treat it as one subtype within a wider generalization space.

**Space of measurement.** Operationalization is mostly benchmark-based: papers link the construct to 18 measurement instruments and 4 behavioral indicators, but the direct measured_by links are benchmark-style evaluations on unseen or out-of-domain datasets, plus one evaluation harness. The most frequently linked instruments are AG News, LAMBADA, WikiText, Arxiv, and CommonsenseQA. These operationalizations largely match the dominant definitions, because papers test transfer to unseen datasets, domains, tasks, or constraints, while instantiating that test in settings such as scientific QA, multimodal evaluation, KGQA, and time-series forecasting.

**Links.** Several papers claim causal relationships from instruction following, compositionality, and speech-text alignment to zero-shot generalization: one says multimodal instruction tuning enables it on previously unseen multimodal tasks, another says compositionality contributes to it, and another says correct speech-text alignment can preserve LLM zero-shot capability. Separate papers describe it as related to in-context learning and cross-domain generalization, with additional related links to several other constructs and behaviors. No correlational link is reported.

## Sources

**Zero-shot generalization** (12 papers: [Evaluating the Zero-shot Robustness of Instruction-tuned Language Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/d3221cdb27e49d9c1cd35ad254feccfe-Paper-Conference.pdf), [GoLLIE: Annotation Guidelines improve Zero-Shot Information-Extraction](https://proceedings.iclr.cc/paper_files/paper/2024/file/cda04d7ea67ea1376bf8c6962d8541e0-Paper-Conference.pdf), [Octavius: Mitigating Task Interference in MLLMs via LoRA-MoE](https://proceedings.iclr.cc/paper_files/paper/2024/file/6b3b238c5786536dc9f835760e2dba02-Paper-Conference.pdf), [TEMPO: Prompt-based Generative Pre-trained Transformer for Time Series Forecasting](https://proceedings.iclr.cc/paper_files/paper/2024/file/5132940b1bced8a7b28e9695d49d435a-Paper-Conference.pdf), [Vision-Language Foundation Models as Effective Robot Imitators](https://proceedings.iclr.cc/paper_files/paper/2024/file/71639c317fb0bf398835627b4418693e-Paper-Conference.pdf), [Combining Observational Data and Language for Species Range Estimation](https://proceedings.neurips.cc/paper_files/paper/2024/file/1f96b24df4b06f5d68389845a9a13ed9-Paper-Conference.pdf), [Multiagent Finetuning: Self Improvement with Diverse Reasoning Chains](https://proceedings.iclr.cc/paper_files/paper/2025/file/1d50221b03ced7152d8750c9d1e66cba-Paper-Conference.pdf), [Label Drop for Multi-Aspect Relation Modeling in Universal Information Extraction](https://aclanthology.org/2025.naacl-long.259.pdf), [Large Language Models Can Solve Real-World Planning Rigorously with Formal Verification Tools](https://aclanthology.org/2025.naacl-long.176.pdf), [SECRET: Semi-supervised Clinical Trial Document Similarity Search](https://aclanthology.org/2025.acl-long.264.pdf), [Text-to-LoRA: Instant Transformer Adaption](https://raw.githubusercontent.com/mlresearch/v267/main/assets/charakorn25a/charakorn25a.pdf), [TS-CLIP: Time Series Understanding by CLIP](https://aclanthology.org/2025.emnlp-main.231.pdf))
> The ability of a pre-trained model to perform well on unseen target datasets without exposure to their training history.

**Zero-shot generalizability** (2 papers: [SafeWatch: An Efficient Safety-Policy Following Video Guardrail Model with Transparent Explanations](https://proceedings.iclr.cc/paper_files/paper/2025/file/beac6bfb7eac3d651307c16ac747df01-Paper-Conference.pdf), [Kernel-based Unsupervised Embedding Alignment for Enhanced Visual Representation in Vision-language Models](https://raw.githubusercontent.com/mlresearch/v267/main/assets/gong25b/gong25b.pdf))
> The model's ability to perform effectively on new, unseen tasks, policies, or data categories without any specific fine-tuning on them.

**Zero-shot learning** (4 papers: [Entity Decomposition with Filtering: A Zero-Shot Clinical Named Entity Recognition Framework](https://aclanthology.org/2025.naacl-long.150.pdf), [Data-Driven Discovery of Dynamical Systems in Pharmacology using Large Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/aea8bdc42d8ba3a67a69b3f18be93f69-Paper-Conference.pdf), [How do Language Models Reshape Entity Alignment? A Survey of LM-Driven EA Methods: Advances, Benchmarks, and Future](https://aclanthology.org/2025.emnlp-main.1184.pdf), [Diffusion-based Neural Network Weights Generation](https://proceedings.iclr.cc/paper_files/paper/2025/file/f74d79573d71078848973009d0e99bdb-Paper-Conference.pdf))
> The capacity to perform clinical entity extraction without task-specific training examples for the target setting.

**Zero-shot transfer** (1 paper: [A Zero-Shot Open-Vocabulary Pipeline for Dialogue Understanding](https://aclanthology.org/2025.naacl-long.387.pdf))
> The ability to perform dialogue understanding tasks without task-specific fine-tuning or training on the target domains.

**Zero-shot transferability** (1 paper: [LangTime: A Language-Guided Unified Model for Time Series Forecasting with Proximal Policy Optimization](https://raw.githubusercontent.com/mlresearch/v267/main/assets/niu25e/niu25e.pdf))
> The ability of the pre-trained model to perform forecasting in unseen domains without task-specific fine-tuning.

**Zero-shot control** (1 paper: [MaestroMotif: Skill Design from Artificial Intelligence Feedback](https://proceedings.iclr.cc/paper_files/paper/2025/file/2dc5a0faac8102fd47363795f71126ee-Paper-Conference.pdf))
> The ability of an agent to perform a novel task specified in natural language without any task-specific training or fine-tuning.

**Zero-shot task classification** (1 paper: [SlimLLM: Accurate Structured Pruning for Large Language Models](https://raw.githubusercontent.com/mlresearch/v267/main/assets/guo25a/guo25a.pdf))
> The model's ability to correctly classify inputs into predefined categories without any task-specific fine-tuning, based solely on its pre-trained knowledge.

**Zero-shot learning ability** (1 paper: [From Instance Training to Instruction Learning: Task Adapters Generation from Instructions](https://proceedings.neurips.cc/paper_files/paper/2024/file/50ea4dbd1cff6bd3daef939eff10c092-Paper-Conference.pdf))
> The capability of a model to perform a task given only a natural language description, without having seen any specific training examples for that task.

**Zero-shot capability** (2 papers: [PromptFix: You Prompt and We Fix the Photo](https://proceedings.neurips.cc/paper_files/paper/2024/file/468c9ec4215e05b6488ac307d377662e-Paper-Conference.pdf), [GER-LLM: Efficient and Effective Geospatial Entity Resolution with Large Language Model](https://aclanthology.org/2025.emnlp-main.1186.pdf))
> The ability to perform a task without any specific training examples for that task or condition.

**Zero-shot inference** (1 paper: [FEDMEKI: A Benchmark for Scaling Medical Foundation Models via Federated Knowledge Injection](https://proceedings.neurips.cc/paper_files/paper/2024/file/0235cbb8cd6425d0b55daefce388fc0b-Paper-Datasets_and_Benchmarks_Track.pdf))
> The ability of a model to perform tasks for which it has not been explicitly trained, by leveraging knowledge gained from other tasks.

**Zero-shot prompting capability** (1 paper: [Boosting Weakly Supervised Referring Image Segmentation via Progressive Comprehension](https://proceedings.neurips.cc/paper_files/paper/2024/file/a97f0218b49bc17ea3f121a0e724f028-Paper-Conference.pdf))
> The ability of a Large Language Model to perform tasks based on instructions alone, without any provided examples (shots).

**Zero-shot adaptability** (1 paper: [Answering Narrative-Driven Recommendation Queries via a Retrieve–Rank Paradigm and the OCG-Agent](https://aclanthology.org/2025.emnlp-main.667.pdf))
> The model's ability to perform tasks, such as narrative recommendation, without any specific examples or fine-tuning for that task.

**Zero-shot performance** (1 paper: [On the Analysis and Distillation of Emergent Outlier Properties in Pre-trained Language Models](https://aclanthology.org/2025.naacl-long.430.pdf))
> The ability of a model to perform tasks without any task-specific fine-tuning or examples provided in the context.

## Relationships

### Zero-shot generalization →
- **WikiText** (measurement instrument): *measured_by*, 2 papers
  > We also evaluate the ability of BD3-LMs to generalize to unseen datasets in a zero-shot setting... We evaluate the likelihood of models trained with OWT on datasets... Wikitext... (Section 6.1)
  - [Block Diffusion: Interpolating Between Autoregressive and Diffusion Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/7ede97c3e082c6df10a8d6103a2eebd2-Paper-Conference.pdf)
  - [Energy-Based Diffusion Language Models for Text Generation](https://proceedings.iclr.cc/paper_files/paper/2025/file/535baca36883a4e0450423b26b150a48-Paper-Conference.pdf)
- **LAMBADA** (measurement instrument): *measured_by*, 2 papers
  > We also evaluate the ability of BD3-LMs to generalize to unseen datasets in a zero-shot setting... We evaluate the likelihood of models trained with OWT on datasets... Lambada... (Section 6.1)
  - [Block Diffusion: Interpolating Between Autoregressive and Diffusion Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/7ede97c3e082c6df10a8d6103a2eebd2-Paper-Conference.pdf)
  - [Energy-Based Diffusion Language Models for Text Generation](https://proceedings.iclr.cc/paper_files/paper/2025/file/535baca36883a4e0450423b26b150a48-Paper-Conference.pdf)
- **AG News** (measurement instrument): *measured_by*, 2 papers
  > We also evaluate the ability of BD3-LMs to generalize to unseen datasets in a zero-shot setting... We evaluate the likelihood of models trained with OWT on datasets... AG News... (Section 6.1)
  - [Block Diffusion: Interpolating Between Autoregressive and Diffusion Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/7ede97c3e082c6df10a8d6103a2eebd2-Paper-Conference.pdf)
  - [Energy-Based Diffusion Language Models for Text Generation](https://proceedings.iclr.cc/paper_files/paper/2025/file/535baca36883a4e0450423b26b150a48-Paper-Conference.pdf)
- **lm-evaluation-harness** (measurement instrument): *measured_by*, 1 paper
  > “Zero-shot performance was evaluated using the LM Evaluation Harness (Gao et al., 2021)”
  - [MoDeGPT: Modular Decomposition for Large Language Model Compression](https://proceedings.iclr.cc/paper_files/paper/2025/file/fb7214d2fdfd84165b08539d59c92e07-Paper-Conference.pdf)
- **ScienceQA** (measurement instrument): *measured_by*, 1 paper
  > ScienceQA with multiple choice are used to evaluate the zero-shot generalization on scientific question answering. (Section 4.1)
  - [Efficient Large Multi-modal Models via Visual Context Compression](https://proceedings.neurips.cc/paper_files/paper/2024/file/871ed095b734818cfba48db6aeb25a62-Paper-Conference.pdf)
- **LM1B** (measurement instrument): *measured_by*, 1 paper
  > We evaluate the model capacity for both the OpenWebText test set and seven out-of-domain unseen datasets, used to validate the models' ability in zero-shot generalization. These unseen datasets include Our Penn Tree Bank (PTB)... Wikitext... LM1B
  - [Energy-Based Diffusion Language Models for Text Generation](https://proceedings.iclr.cc/paper_files/paper/2025/file/535baca36883a4e0450423b26b150a48-Paper-Conference.pdf)
- **PubMed** (measurement instrument): *measured_by*, 1 paper
  > We evaluate the model capacity for both the OpenWebText test set and seven out-of-domain unseen datasets, used to validate the models' ability in zero-shot generalization. These unseen datasets include Our Penn Tree Bank (PTB)... Wikitext... LM1B, Lambada... AG News... Pubmed
  - [Energy-Based Diffusion Language Models for Text Generation](https://proceedings.iclr.cc/paper_files/paper/2025/file/535baca36883a4e0450423b26b150a48-Paper-Conference.pdf)
- **Arxiv** (measurement instrument): *measured_by*, 1 paper
  > We evaluate the model capacity for both the OpenWebText test set and seven out-of-domain unseen datasets, used to validate the models' ability in zero-shot generalization. These unseen datasets include Our Penn Tree Bank (PTB)... Wikitext... LM1B, Lambada... AG News... Pubmed and Arxiv
  - [Energy-Based Diffusion Language Models for Text Generation](https://proceedings.iclr.cc/paper_files/paper/2025/file/535baca36883a4e0450423b26b150a48-Paper-Conference.pdf)
- **MM-Vet** (measurement instrument): *measured_by*, 1 paper
  > Unseen tasks are datasets that were not involved in the recipe construction process. These tasks are used to evaluate the zero-shot generalizability of our method. Specifically, we employed the MM-Vet (Yu et al., 2024), MM-Bench (Zhang et al., 2023a), MM-Bench-Chinese (Zhang et al., 2023a), VizWiz (Gurari et al., 2018), and POPE (Li et al., 2023) datasets to assess this capability.
  - [REMEDY: Recipe Merging Dynamics in Large Vision-Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/4065a881baab1744bfba208a4361bbb1-Paper-Conference.pdf)
- **MMBench** (measurement instrument): *measured_by*, 1 paper
  > Unseen tasks are datasets that were not involved in the recipe construction process. These tasks are used to evaluate the zero-shot generalizability of our method. Specifically, we employed the MM-Vet (Yu et al., 2024), MM-Bench (Zhang et al., 2023a), MM-Bench-Chinese (Zhang et al., 2023a), VizWiz (Gurari et al., 2018), and POPE (Li et al., 2023) datasets to assess this capability.
  - [REMEDY: Recipe Merging Dynamics in Large Vision-Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/4065a881baab1744bfba208a4361bbb1-Paper-Conference.pdf)
- **VizWiz** (measurement instrument): *measured_by*, 1 paper
  > Unseen tasks are datasets that were not involved in the recipe construction process. These tasks are used to evaluate the zero-shot generalizability of our method. Specifically, we employed the MM-Vet (Yu et al., 2024), MM-Bench (Zhang et al., 2023a), MM-Bench-Chinese (Zhang et al., 2023a), VizWiz (Gurari et al., 2018), and POPE (Li et al., 2023) datasets to assess this capability.
  - [REMEDY: Recipe Merging Dynamics in Large Vision-Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/4065a881baab1744bfba208a4361bbb1-Paper-Conference.pdf)
- **POPE** (measurement instrument): *measured_by*, 1 paper
  > Unseen tasks are datasets that were not involved in the recipe construction process. These tasks are used to evaluate the zero-shot generalizability of our method. Specifically, we employed the MM-Vet (Yu et al., 2024), MM-Bench (Zhang et al., 2023a), MM-Bench-Chinese (Zhang et al., 2023a), VizWiz (Gurari et al., 2018), and POPE (Li et al., 2023) datasets to assess this capability.
  - [REMEDY: Recipe Merging Dynamics in Large Vision-Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/4065a881baab1744bfba208a4361bbb1-Paper-Conference.pdf)
- **GSM8K** (measurement instrument): *measured_by*, 1 paper
  > our method surpasses all the baseline methods, even though it has never seen data from the GSM dataset, indicating the strong zero-shot generalization capability of the proposed method. (Section 4.3)
  - [Multiagent Finetuning: Self Improvement with Diverse Reasoning Chains](https://proceedings.iclr.cc/paper_files/paper/2025/file/1d50221b03ced7152d8750c9d1e66cba-Paper-Conference.pdf)
- **Traffic** (measurement instrument): *measured_by*, 1 paper
  > Comparison of zero-shot performance of pre-trained models. The input sequence length is set to 96 for the Traffic dataset
  - [LangTime: A Language-Guided Unified Model for Time Series Forecasting with Proximal Policy Optimization](https://raw.githubusercontent.com/mlresearch/v267/main/assets/niu25e/niu25e.pdf)
- **FreebaseQA** (measurement instrument): *measured_by*, 1 paper
  > To further evaluate the generalizability of GCR, we conduct zero-shot transfer experiments on three new KGQA datasets: FreebaseQA, CSQA and MedQA (Section 5.1).
  - [Graph-constrained Reasoning: Faithful Reasoning on Knowledge Graphs with Large Language Models](https://raw.githubusercontent.com/mlresearch/v267/main/assets/luo25t/luo25t.pdf)
- **CommonsenseQA** (measurement instrument): *measured_by*, 1 paper
  > To further evaluate the generalizability of GCR, we conduct zero-shot transfer experiments on three new KGQA datasets: FreebaseQA, CSQA and MedQA (Section 5.1).
  - [Graph-constrained Reasoning: Faithful Reasoning on Knowledge Graphs with Large Language Models](https://raw.githubusercontent.com/mlresearch/v267/main/assets/luo25t/luo25t.pdf)
- **MedQA** (measurement instrument): *measured_by*, 1 paper
  > To further evaluate the generalizability of GCR, we conduct zero-shot transfer experiments on three new KGQA datasets: FreebaseQA, CSQA and MedQA (Section 5.1).
  - [Graph-constrained Reasoning: Faithful Reasoning on Knowledge Graphs with Large Language Models](https://raw.githubusercontent.com/mlresearch/v267/main/assets/luo25t/luo25t.pdf)
- **GrailQA** (measurement instrument): *measured_by*, 1 paper
  > In the validation and the test sets, 50% of the questions include KB elements that are unseen in the training set (zero-shot generalization tests), 25% consist of unseen compositions of KB elements seen in the training set (compositional generalization tests), and the remaining 25% are randomly sampled from the training set (I.I.D. tests). (Section 5.1)
  - [Beyond Seen Data: Improving KBQA Generalization Through Schema-Guided Logical Form Generation](https://aclanthology.org/2025.emnlp-main.442.pdf)

### → Zero-shot generalization
- **Instruction following** (behavioral indicator): *causes*, 1 paper
  > multimodal instruction tuning has been introduced (Liu et al., 2024), full fine-tuning pre-trained models with diverse multimodal instruction-following datasets, thereby enabling zero-shot generalization to previously unseen multimodal tasks. (Section 1)
  - [Re-Imagining Multimodal Instruction Tuning: A Representation View](https://proceedings.iclr.cc/paper_files/paper/2025/file/dcf88cbc8d01ce7309b83d0ebaeb9d29-Paper-Conference.pdf)
- **Compositionality** (construct): *causes*, 1 paper
  > “compositionality contributes significantly to zero-shot generalization”
  - [Human-Object Interaction Detection Collaborated with Large Relation-driven Diffusion Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/2a54def490213ee10631b991c5acc6b5-Paper-Conference.pdf)
- **Speech-text alignment** (construct): *causes*, 1 paper
  > ...through complex training pipelines gradually enables S to learn a correct alignment that can preserve the LLM zero-shot capability (Section 3).
  - [Wav2Prompt: End-to-End Speech Prompt Learning and Task-based Fine-tuning for Text-based LLMs](https://aclanthology.org/2025.naacl-long.354.pdf)

### Associated with
- **In-context learning** (construct), 2 papers
  > our method randomly samples a varying number of examples during training, endowing the embedding model with in-context learning abilities while maintaining its zero-shot capabilities. (Abstract)
  - [Making Text Embedders Few-Shot Learners](https://proceedings.iclr.cc/paper_files/paper/2025/file/5eba8556ce2d1afff57591464d48fbc3-Paper-Conference.pdf)
  - [Zero-shot forecasting of chaotic systems](https://proceedings.iclr.cc/paper_files/paper/2025/file/ea4d65c59073e8faf79222654d25fbe2-Paper-Conference.pdf)
- **Task generalization** (construct), 1 paper
  > for better cross-task generalization, the "zero-shot" learning ability of LLMs is crucial for real-world applications (Section 1 Introduction).
  - [From Instance Training to Instruction Learning: Task Adapters Generation from Instructions](https://proceedings.neurips.cc/paper_files/paper/2024/file/50ea4dbd1cff6bd3daef939eff10c092-Paper-Conference.pdf)
- **Image restoration** (behavioral indicator), 1 paper
  > Our proposed model also achieves comparable inference efficiency with these baseline models and exhibits superior zero-shot capabilities in blind restoration and combination tasks.
  - [PromptFix: You Prompt and We Fix the Photo](https://proceedings.neurips.cc/paper_files/paper/2024/file/468c9ec4215e05b6488ac307d377662e-Paper-Conference.pdf)
- **Emergent abilities** (construct), 1 paper
  > Examples include zero-shot task transfer (Radford et al., 2021) and few-shot learning (Brown et al., 2020). This is sometimes known as the emergent abilities of LLMs (Section 2).
  - [Wav2Prompt: End-to-End Speech Prompt Learning and Task-based Fine-tuning for Text-based LLMs](https://aclanthology.org/2025.naacl-long.354.pdf)
- **Cross-domain generalization** (construct), 1 paper
  > This critical limitation creates an urgent need for a transformative recommendation paradigm with robust Zero-Shot Generalization capabilities that can adapt seamlessly across diverse scenarios without prior exposure to specific users or items (Section 1)
  - [RecGPT: A Foundation Model for Sequential Recommendation](https://aclanthology.org/2025.emnlp-main.513.pdf)
- **Image inpainting** (behavioral indicator), 1 paper
  > VAR further showcases zero-shot generalization ability in downstream tasks including image in-painting, out-painting, and editing.
  - [Visual Autoregressive Modeling: Scalable Image Generation via Next-Scale Prediction](https://proceedings.neurips.cc/paper_files/paper/2024/file/9a24e284b187f662681440ba15c416fb-Paper-Conference.pdf)
- **Image outpainting** (behavioral indicator), 1 paper
  > VAR further showcases zero-shot generalization ability in downstream tasks including image in-painting, out-painting, and editing.
  - [Visual Autoregressive Modeling: Scalable Image Generation via Next-Scale Prediction](https://proceedings.neurips.cc/paper_files/paper/2024/file/9a24e284b187f662681440ba15c416fb-Paper-Conference.pdf)
- **Graph reasoning** (construct), 1 paper
  > “This highlights the strong zero-shot generalizability of its graph reasoning capabilities to unseen datasets and KGs without additional training.”
  - [Graph-constrained Reasoning: Faithful Reasoning on Knowledge Graphs with Large Language Models](https://raw.githubusercontent.com/mlresearch/v267/main/assets/luo25t/luo25t.pdf)
