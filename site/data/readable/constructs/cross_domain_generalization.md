# Cross-domain generalization
**Type:** Construct  
**Supporting papers:** 29  
**Also known as:** Generalization to unseen targets, Domain transfer, Cross-domain generalizability, Domain generalization, Cross-domain transfer, Cross-domain adaptability, Out-of-domain generalization, Domain transferability, Cross-platform generalization  

## State of the Field

**Space of definitions.** Across papers, the prevailing usage treats cross-domain generalization as transfer or maintenance of model performance when training and evaluation come from different domains, topics, prompt distributions, or environments. Most definitions describe performance on unseen targets or domains, including new topics, websites, databases, operating systems, and recommendation contexts. A smaller line of work specifies what transfers more narrowly: reasoning performance across fundamentally different domains, learned preferences and concept importance across domains, or learned representations and safety checks carried from one domain to another. The main disagreement is therefore about what counts as the domain boundary and whether the construct refers to overall task performance or to narrower objects such as reasoning, preferences, representations, or risk patterns.

**Space of facets.** Papers use a broad family of near-synonymous names for this construct, including domain transfer, cross-domain transfer, domain generalization, cross-domain generalizability, out-of-domain generalization, domain transferability, and cross-platform generalization. They also distinguish settings by the source-target split being tested, such as unseen stance targets, leave-one-out held-out domains, disjoint training and test databases, or movement across domains with fundamentally different structures like math, code generation, and language understanding. Some papers contrast it with in-domain performance or note that domain-specific improvement may come at the cost of broader generalization, while one paper explicitly frames it as shared patterns plus domain-specific deviations.

**Space of measurement.** Operationalization is dominated by benchmark-based transfer tests: papers link the construct to 14 measurement instruments and 1 behavioral indicator overall. The most frequently linked instruments are ALFWorld, Arena-Hard, BIRD, CrossNER, and GLUE-X, with 9 other instruments also used; these instruments are used as held-out-domain, external, or disjoint-train-test evaluations, including benchmarks described as spanning multiple domains or separating training and test databases. This mostly matches the definitions, because papers usually operationalize the construct by testing whether performance carries to unseen domains, prompts, targets, or environments.

**Links.** In the relationship evidence, one paper claims a causal relationship from Schema linking to cross-domain generalization, describing schema-linking as improving generalization by associating queries with database items. Papers also describe cross-domain generalization as related to Zero-shot generalization and to Prompt robustness, with the latter framed through training prompts as a source domain and novel test prompts as a target domain. No correlation links are reported.

## Sources

**Domain transfer** (1 paper: [ViClaim: A Multilingual Multilabel Dataset for Automatic Claim Detection in Videos](https://aclanthology.org/2025.emnlp-main.21.pdf))
> The capability of a model trained on a set of source domains or topics to perform effectively on a different target domain or topic.

**Generalization to unseen targets** (1 paper: [T-MAD: Target-driven Multimodal Alignment for Stance Detection](https://aclanthology.org/2025.emnlp-main.30.pdf))
> The model's ability to accurately detect stances toward targets not encountered during training, reflecting adaptability to novel topics in social media discourse.

**Cross-domain generalization** (4 papers: [PAFT: Prompt-Agnostic Fine-Tuning](https://aclanthology.org/2025.emnlp-main.37.pdf), [Single-to-mix Modality Alignment with Multimodal Large Language Model for Document Image Machine Translation](https://aclanthology.org/2025.acl-long.606.pdf), [Youku Dense Caption: A Large-scale Chinese Video Dense Caption Dataset and Benchmarks](https://proceedings.iclr.cc/paper_files/paper/2025/file/1f3cbee17170c3ffff3e413d2df54f6b-Paper-Conference.pdf), [AdaptiveStep: Automatically Dividing Reasoning Step through Model Confidence](https://raw.githubusercontent.com/mlresearch/v267/main/assets/liu25aq/liu25aq.pdf))
> The ability of a model to transfer knowledge and performance from one domain or prompt distribution to another, particularly when training and test prompts differ significantly.

**Cross-domain generalizability** (1 paper: [Warm Up Before You Train: Unlocking General Reasoning in Resource-Constrained Settings](https://aclanthology.org/2025.emnlp-main.727.pdf))
> The capacity of a model to maintain or transfer reasoning performance across fundamentally different task domains after specialized training.

**Domain generalization** (1 paper: [Multi-Domain Explainability of Preferences](https://aclanthology.org/2025.emnlp-main.736.pdf))
> The degree to which a model's learned preferences and concept importance generalize across different domains, capturing both shared patterns and domain-specific deviations.

**Cross-domain transfer** (2 papers: [M-ABSA: A Multilingual Dataset for Aspect-Based Sentiment Analysis](https://aclanthology.org/2025.emnlp-main.128.pdf), [NatureLM-audio: an Audio-Language Foundation Model for Bioacoustics](https://proceedings.iclr.cc/paper_files/paper/2025/file/36c20807317ae6cb3817acd554da2d32-Paper-Conference.pdf))
> The ability of a model to apply knowledge learned in one specific domain to perform tasks in a different, unseen domain.

**Cross-domain adaptability** (1 paper: [RecGPT: A Foundation Model for Sequential Recommendation](https://aclanthology.org/2025.emnlp-main.513.pdf))
> The model's inherent capability to transfer knowledge and maintain performance across different recommendation contexts and platforms, such as e-commerce, games, and social media.

**Out-of-domain generalization** (1 paper: [WebEvolver: Enhancing Web Agent Self-Improvement with Co-evolving World Model](https://aclanthology.org/2025.emnlp-main.454.pdf))
> The ability to transfer web-agent performance to websites or query settings not seen during training.

**Domain transferability** (1 paper: [AGrail: A Lifelong Agent Guardrail with Effective and Adaptive Safety Detection](https://aclanthology.org/2025.acl-long.399.pdf))
> The extent to which optimized safety checks and learned risk patterns generalize from one task domain to another without performance degradation.

**Cross-platform generalization** (1 paper: [Navigating the Digital World as Humans Do: Universal Visual Grounding for GUI Agents](https://proceedings.iclr.cc/paper_files/paper/2025/file/4ca0e369689dadb25a5345ba9755ad6f-Paper-Conference.pdf))
> The degree to which a model's performance transfers across different operating systems and environments (web, desktop, mobile) without specific training on all platforms.

## Relationships

### Cross-domain generalization →
- **VATEX** (measurement instrument): *measured_by*, 1 paper
  > we evaluate both the VATEX validation set and the generation benchmark on YDC, which are of nearly the same scale. This dual evaluation aims to assess the cross-domain generalization capabilities of the training results (Section 6).
  - [Youku Dense Caption: A Large-scale Chinese Video Dense Caption Dataset and Benchmarks](https://proceedings.iclr.cc/paper_files/paper/2025/file/1f3cbee17170c3ffff3e413d2df54f6b-Paper-Conference.pdf)
- **CrossNER** (measurement instrument): *measured_by*, 1 paper
  > CrossNER provides datasets that spans multiple domains... which is suited for evaluating zero-shot NER tasks. (Section 4.2)
  - [Handling Missing Entities in Zero-Shot Named Entity Recognition: Integrated Recall and Retrieval Augmentation](https://aclanthology.org/2025.naacl-long.540.pdf)
- **LEMON** (measurement instrument): *measured_by*, 1 paper
  > Notably, LEMON includes test sets from seven different domains but does not provide in-domain training sets, making it an ideal benchmark for evaluating a model’s cross-domain generalization capability. (Section 4.1)
  - [Mixture of Small and Large Models for Chinese Spelling Check](https://aclanthology.org/2025.acl-long.1372.pdf)
- **VirtualHome** (measurement instrument): *measured_by*, 1 paper
  > We evaluate our WorMI on the VirtualHome and ALFWorld benchmarks, demonstrating superior zero-shot and few-shot performance compared to several LLM-based approaches across a range of unseen domains. These results highlight the framework’s potential for scalable, real-world deployment in embodied agent scenarios where adaptability and data efficiency are essential. (Abstract).
  - [World Model Implanting for Test-time Adaptation of Embodied Agents](https://raw.githubusercontent.com/mlresearch/v267/main/assets/yoo25a/yoo25a.pdf)
- **ALFWorld** (measurement instrument): *measured_by*, 1 paper
  > We evaluate our WorMI on the VirtualHome and ALFWorld benchmarks, demonstrating superior zero-shot and few-shot performance compared to several LLM-based approaches across a range of unseen domains. These results highlight the framework’s potential for scalable, real-world deployment in embodied agent scenarios where adaptability and data efficiency are essential. (Abstract).
  - [World Model Implanting for Test-time Adaptation of Embodied Agents](https://raw.githubusercontent.com/mlresearch/v267/main/assets/yoo25a/yoo25a.pdf)
- **Spider** (measurement instrument): *measured_by*, 1 paper
  > Benchmarks like Spider(Yu et al., 2019) and BIRD(Li et al., 2023b) evaluate cross-domain generalization, where training and test databases are disjoint. (Section 1)
  - [GenLink: Generation-Driven Schema-Linking via Multi-Model Learning for Text-to-SQL](https://aclanthology.org/2025.emnlp-main.1518.pdf)
- **BIRD** (measurement instrument): *measured_by*, 1 paper
  > Benchmarks like Spider(Yu et al., 2019) and BIRD(Li et al., 2023b) evaluate cross-domain generalization, where training and test databases are disjoint. (Section 1)
  - [GenLink: Generation-Driven Schema-Linking via Multi-Model Learning for Text-to-SQL](https://aclanthology.org/2025.emnlp-main.1518.pdf)
- **MT-Bench** (measurement instrument): *measured_by*, 1 paper
  > "we further introduce the complex instruction-following dataset InfoBench(Qin et al., 2024b), the general natural instruction evaluation set MT-Bench (Zheng et al., 2023) and the real-world chatbot evaluation set Arena-hard (Zheng et al., 2023) as cross domain validation."
  - [Self-play with Execution Feedback: Improving Instruction-following Capabilities of Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/62203a74e233e933b160711e791e1a02-Paper-Conference.pdf)
- **MATH** (measurement instrument): *measured_by*, 1 paper
  > We find that fine-tuning generalizes perfectly across domains for MATH, which is not very surprising given the near-perfect generalization from few samples to the full distribution in Figure 3. (Section 5.2)
  - [Stress-Testing Capability Elicitation With Password-Locked Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/7ff97417474268e6b5a38bcbfae04944-Paper-Conference.pdf)
- **InfoBench** (measurement instrument): *measured_by*, 1 paper
  > "we further introduce the complex instruction-following dataset InfoBench(Qin et al., 2024b), the general natural instruction evaluation set MT-Bench (Zheng et al., 2023) and the real-world chatbot evaluation set Arena-hard (Zheng et al., 2023) as cross domain validation."
  - [Self-play with Execution Feedback: Improving Instruction-following Capabilities of Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/62203a74e233e933b160711e791e1a02-Paper-Conference.pdf)
- **Arena-Hard** (measurement instrument): *measured_by*, 1 paper
  > "we further introduce the complex instruction-following dataset InfoBench(Qin et al., 2024b), the general natural instruction evaluation set MT-Bench (Zheng et al., 2023) and the real-world chatbot evaluation set Arena-hard (Zheng et al., 2023) as cross domain validation."
  - [Self-play with Execution Feedback: Improving Instruction-following Capabilities of Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/62203a74e233e933b160711e791e1a02-Paper-Conference.pdf)
- **SST-2** (measurement instrument): *measured_by*, 1 paper
  > To further demonstrate the generalization ability of our method, we conduct cross-domain experiments. We use three sentiment datasets on SST-2 (Socher et al., 2013), IMDb (Maas et al., 2011), FineFood (McAuley and Leskovec, 2013). (Section 4.1)
  - [SALAD: Improving Robustness and Generalization through Contrastive Learning with Structure-Aware and LLM-Driven Augmented Data](https://aclanthology.org/2025.naacl-long.634.pdf)
- **GLUE-X** (measurement instrument): *measured_by*, 1 paper
  > We focus on domain generalization... To this end, we conduct experiments using GLUE-X (Yang et al., 2023a). (Section 5)
  - [Mitigating Shortcut Learning with InterpoLated Learning](https://aclanthology.org/2025.acl-long.450.pdf)
- **ToxiCloakCN** (measurement instrument): *measured_by*, 1 paper
  > To further evaluate the generalization capacity of our homophone-aware training strategy under cross-domain settings, we conduct experiments on the ToxiCloakCN dataset as an external benchmark (Xiao et al., 2024). (Section 5.5.5)
  - [Enhancing Chinese Offensive Language Detection with Homophonic Perturbation](https://aclanthology.org/2025.emnlp-main.1154.pdf)

### → Cross-domain generalization
- **Schema linking** (behavioral indicator): *causes*, 1 paper
  > Schema-linking is widely recognized as key to improving generalization by adaptively associating queries with database items. (Section 1)
  - [GenLink: Generation-Driven Schema-Linking via Multi-Model Learning for Text-to-SQL](https://aclanthology.org/2025.emnlp-main.1518.pdf)

### Associated with
- **Zero-shot generalization** (construct), 1 paper
  > This critical limitation creates an urgent need for a transformative recommendation paradigm with robust Zero-Shot Generalization capabilities that can adapt seamlessly across diverse scenarios without prior exposure to specific users or items (Section 1)
  - [RecGPT: A Foundation Model for Sequential Recommendation](https://aclanthology.org/2025.emnlp-main.513.pdf)
- **Prompt robustness** (construct), 1 paper
  > The capability of PAFT to generalize effectively to unseen prompt formulations can be rigorously understood through the lens of domain adaptation theory... In this theoretical construct, the collection of training prompts Ptrain along with the task-specific training data Dtrain delineates the source domain. Besdies, the set of novel test prompts Ptest, paired with Dtest, represents the target domain (Section 6).
  - [PAFT: Prompt-Agnostic Fine-Tuning](https://aclanthology.org/2025.emnlp-main.37.pdf)
