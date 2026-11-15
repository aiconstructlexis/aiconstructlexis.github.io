# Object hallucination
**Type:** Behavioral indicator  
**Supporting papers:** 43  
**Also known as:** Hallucinated object generation  

## State of the Field

**Space of definitions.** Across papers, the prevailing usage treats object hallucination as outputs that mention or describe objects absent from the visual input, usually an image and in one definition a video frame. Several papers phrase this more broadly as responses "not factually aligned with image inputs," but the recurring concrete criterion is an incorrect object claim, whether in a free-form description or an affirmative answer such as "Yes, there is a white chair in the image." A smaller line of work also counts neglecting visible objects or "omitting essential features" as part of the behavior.

**Variants.** Most studies examine the behavior in image descriptions and captioning, while another common setting is yes/no object-presence questioning, including work that says models "hallucinate in response to yes/no questions." POPE-based papers further divide this probing into Popular, Random, and Adversarial balanced yes/no VQA, and one definition explicitly extends the setting from images to video frames. Some evaluations operationalize hallucination with subtasks such as Existence, Count, Position, and Color, or with object, attribute, and relation hallucinations, and one paper uses the alternate name "hallucinated object generation."

**Space of elicitation and scores.** Papers measure object hallucination with 11 instruments. The most common are POPE, CHAIR, AMBER, MME, and MS-COCO: POPE is repeatedly described as balanced yes/no VQA or binary classification about whether a named object is present, while CHAIR scores caption outputs by checking whether mentioned objects appear in ground-truth labels or objects. AMBER evaluates generative and discriminative tasks, MME uses perception subtasks such as Existence, Count, Position, and Color, and MS-COCO is used in caption-oriented evaluation; other papers also use judge-based and human annotation setups.

**What it is taken as evidence of.** Papers do not converge on a single construct that this behavior reflects. The most recurrent construct link is a claimed causal relationship from multimodal alignment to object hallucination, with papers saying inferior alignment or insufficient interaction between visual and instruction tokens leads to object hallucinations. Elsewhere, object hallucination is reported to correlate with representational stability, and separate papers relate it to faithfulness and visual perception.

## Sources

**Object hallucination** (8 papers: [VideoLLM-MoD: Efficient Video-Language Streaming with Mixture-of-Depths Vision Computation](https://proceedings.neurips.cc/paper_files/paper/2024/file/c6a79e139ec4f371701ea8cc9e06018e-Paper-Conference.pdf), [MLLM can see? Dynamic Correction Decoding for Hallucination Mitigation](https://proceedings.iclr.cc/paper_files/paper/2025/file/24079b91da7257cb78805262996152b8-Paper-Conference.pdf), [ModRWKV: Transformer Multimodality in Linear Time](https://aclanthology.org/2025.emnlp-main.204.pdf), [Mitigating Object Hallucination via Concentric Causal Attention](https://proceedings.neurips.cc/paper_files/paper/2024/file/a76ed4a8ef522c823d73925e7fff16d4-Paper-Conference.pdf), [Analyzing and Mitigating Object Hallucination in Large Vision-Language Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/fc625e831361cfcc82cb74224fdc66cb-Paper-Conference.pdf), [Beyond task performance: evaluating and reducing the flaws of large multimodal models with in-context-learning](https://proceedings.iclr.cc/paper_files/paper/2024/file/5df817c5dd95293ebf6d1583303a8c73-Paper-Conference.pdf), [Ferret: Refer and Ground Anything Anywhere at Any Granularity](https://proceedings.iclr.cc/paper_files/paper/2024/file/fd6613131889a4b656206c50a8bd7790-Paper-Conference.pdf), [Tuning LayerNorm in Attention: Towards Efficient Multi-Modal LLM Finetuning](https://proceedings.iclr.cc/paper_files/paper/2024/file/7cc16e8635e6f27c295355bd214ef8d8-Paper-Conference.pdf))
> An observable failure mode where the model generates text that refers to objects not present in the corresponding image or video frame.

**Hallucinated object generation** (1 paper: [Mitigating Object Hallucination in Large Vision-Language Models via Image-Grounded Guidance](https://raw.githubusercontent.com/mlresearch/v267/main/assets/zhao25j/zhao25j.pdf))
> The observable output of referring to objects in an image that are not actually present, as evidenced by incorrect affirmative answers or false descriptions.

## Relationships

### Object hallucination →
- **POPE** (measurement instrument): *measured_by*, 33 papers
  > POPE (Li et al., 2023b) is used to evaluate the level of object hallucinations in MLLMs, which consists of three versions of balanced yes/no VQA tasks (i.e., Popular/Random/Adversarial) considering objects in the given image. (Section 3)
  - [Tuning LayerNorm in Attention: Towards Efficient Multi-Modal LLM Finetuning](https://proceedings.iclr.cc/paper_files/paper/2024/file/7cc16e8635e6f27c295355bd214ef8d8-Paper-Conference.pdf)
  - [Ferret: Refer and Ground Anything Anywhere at Any Granularity](https://proceedings.iclr.cc/paper_files/paper/2024/file/fd6613131889a4b656206c50a8bd7790-Paper-Conference.pdf)
  - [Mitigating Hallucination in Large Multi-Modal Models via Robust Instruction Tuning](https://proceedings.iclr.cc/paper_files/paper/2024/file/fed9263d7f1086e735904ff690527a53-Paper-Conference.pdf)
  - [VisionLLM v2: An End-to-End Generalist Multimodal Large Language Model for Hundreds of Vision-Language Tasks](https://proceedings.neurips.cc/paper_files/paper/2024/file/81a60d18e010b27b36cd465c6604b915-Paper-Conference.pdf)
  - [Mitigating Object Hallucination via Concentric Causal Attention](https://proceedings.neurips.cc/paper_files/paper/2024/file/a76ed4a8ef522c823d73925e7fff16d4-Paper-Conference.pdf)
  - [GraphVis: Boosting LLMs with Visual Knowledge Graph Integration](https://proceedings.neurips.cc/paper_files/paper/2024/file/7cb04f510593c9ba30da398f5e0a7e7b-Paper-Conference.pdf)
  - [LOVA3: Learning to Visual Question Answering, Asking and Assessment](https://proceedings.neurips.cc/paper_files/paper/2024/file/d0822540916cd716add52e1846a6e18d-Paper-Conference.pdf)
  - [Efficient Large Multi-modal Models via Visual Context Compression](https://proceedings.neurips.cc/paper_files/paper/2024/file/871ed095b734818cfba48db6aeb25a62-Paper-Conference.pdf)
  - [CODE: Contrasting Self-generated Description to Combat Hallucination in Large Multi-modal Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/f1592b0d4ab737e18bb1899484d28d96-Paper-Conference.pdf)
  - [Automated Multi-level Preference for MLLMs](https://proceedings.neurips.cc/paper_files/paper/2024/file/2e3073cb65608aa887bb945c382e687f-Paper-Conference.pdf)
  - [Alleviating Hallucinations in Large Vision-Language Models through Hallucination-Induced Optimization](https://proceedings.neurips.cc/paper_files/paper/2024/file/dde040998d82553cf7f689e8ae173d5a-Paper-Conference.pdf)
  - [Unified Generative and Discriminative Training for Multi-modal Large Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/29416b66c2149872b9d1415a3fd2c5e0-Paper-Conference.pdf)
  - [From Pixels to Tokens: Byte-Pair Encoding on Quantized Visual Modalities](https://proceedings.iclr.cc/paper_files/paper/2025/file/68933e3533add841e115a5605c76eeba-Paper-Conference.pdf)
  - [Locality Alignment Improves Vision-Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/ce6326ac4794bb04d5eb16f597446baf-Paper-Conference.pdf)
  - [EMMA: Empowering Multi-modal Mamba with Structural and Hierarchical Alignment](https://proceedings.iclr.cc/paper_files/paper/2025/file/3760dbb5835bf0b771c3f83cb27ef2c0-Paper-Conference.pdf)
  - [Benchmarking Vision Language Model Unlearning via Fictitious Facial Identity Dataset](https://proceedings.iclr.cc/paper_files/paper/2025/file/dafb7f4ced9ac559e077fc611d6e96e5-Paper-Conference.pdf)
  - [Re-Imagining Multimodal Instruction Tuning: A Representation View](https://proceedings.iclr.cc/paper_files/paper/2025/file/dcf88cbc8d01ce7309b83d0ebaeb9d29-Paper-Conference.pdf)
  - [ClawMachine: Learning to Fetch Visual Tokens for Referential Comprehension](https://proceedings.iclr.cc/paper_files/paper/2025/file/b1abd42eb5aace7f0ad9ba9cfb029f54-Paper-Conference.pdf)
  - [Reducing Hallucinations in Large Vision-Language Models via Latent Space Steering](https://proceedings.iclr.cc/paper_files/paper/2025/file/b4008025c2182bfe16fcc8566ee14d64-Paper-Conference.pdf)
  - [DAMO: Decoding by Accumulating Activations Momentum for Mitigating Hallucinations in Vision-Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/8f0f23417ce1d00212a7c85c2560c392-Paper-Conference.pdf)
  - [Intervening Anchor Token: Decoding Strategy in Alleviating Hallucinations for MLLMs](https://proceedings.iclr.cc/paper_files/paper/2025/file/4537e2172096d966228d68c428392894-Paper-Conference.pdf)
  - [Do You Keep an Eye on What I Ask? Mitigating Multimodal Hallucination via Attention-Guided Ensemble Decoding](https://proceedings.iclr.cc/paper_files/paper/2025/file/637b275a6e65924719198188fc939632-Paper-Conference.pdf)
  - [Self-Introspective Decoding: Alleviating Hallucinations for Large Vision-Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/3cc87f2bd3e3b4df8f9217326761c322-Paper-Conference.pdf)
  - [CertainlyUncertain: A Benchmark and Metric for Multimodal Epistemic and Aleatoric Awareness](https://proceedings.iclr.cc/paper_files/paper/2025/file/21b5788d81f886ff81671379b4ff9453-Paper-Conference.pdf)
  - [Mitigating Object Hallucination in Large Vision-Language Models via Image-Grounded Guidance](https://raw.githubusercontent.com/mlresearch/v267/main/assets/zhao25j/zhao25j.pdf)
  - [The Hidden Life of Tokens: Reducing Hallucination of Large Vision-Language Models Via Visual Information Steering](https://raw.githubusercontent.com/mlresearch/v267/main/assets/li25ca/li25ca.pdf)
  - [SECOND: Mitigating Perceptual Hallucination in Vision-Language Models via Selective and Contrastive Decoding](https://raw.githubusercontent.com/mlresearch/v267/main/assets/park25c/park25c.pdf)
  - [Does Acceleration Cause Hidden Instability in Vision Language Models? Uncovering Instance-Level Divergence Through a Large-Scale Empirical Study](https://aclanthology.org/2025.emnlp-main.425.pdf)
  - [Advancing Fine-Grained Visual Understanding with Multi-Scale Alignment in Multi-Modal Models](https://aclanthology.org/2025.emnlp-main.721.pdf)
  - [SHARP: Steering Hallucination in LVLMs via Representation Engineering](https://aclanthology.org/2025.emnlp-main.725.pdf)
  - [Multi-Frequency Contrastive Decoding: Alleviating Hallucinations for Large Vision-Language Models](https://aclanthology.org/2025.emnlp-main.1452.pdf)
  - [Mitigating Hallucinations in Vision-Language Models through Image-Guided Head Suppression](https://aclanthology.org/2025.emnlp-main.631.pdf)
  - [From Redundancy to Relevance: Information Flow in LVLMs Across Reasoning Tasks](https://aclanthology.org/2025.naacl-long.115.pdf)
- **CHAIR** (measurement instrument): *measured_by*, 15 papers
  > Caption Hallucination Assessment with Image Relevance (CHAIR) (Rohrbach et al., 2018) is a widely-used metric for evaluating object hallucination in image captioning tasks.
  - [Analyzing and Mitigating Object Hallucination in Large Vision-Language Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/fc625e831361cfcc82cb74224fdc66cb-Paper-Conference.pdf)
  - [Unleashing Region Understanding in Intermediate Layers for MLLM-based Referring Expression Generation](https://proceedings.neurips.cc/paper_files/paper/2024/file/da76884a4e003ad0de97804ec4578e5b-Paper-Conference.pdf)
  - [Mitigating Object Hallucination via Concentric Causal Attention](https://proceedings.neurips.cc/paper_files/paper/2024/file/a76ed4a8ef522c823d73925e7fff16d4-Paper-Conference.pdf)
  - [Do You Keep an Eye on What I Ask? Mitigating Multimodal Hallucination via Attention-Guided Ensemble Decoding](https://proceedings.iclr.cc/paper_files/paper/2025/file/637b275a6e65924719198188fc939632-Paper-Conference.pdf)
  - [Reducing Hallucinations in Large Vision-Language Models via Latent Space Steering](https://proceedings.iclr.cc/paper_files/paper/2025/file/b4008025c2182bfe16fcc8566ee14d64-Paper-Conference.pdf)
  - [Mitigating Object Hallucination in MLLMs via Data-augmented Phrase-level Alignment](https://proceedings.iclr.cc/paper_files/paper/2025/file/b73228d026ef49bfa49f95b7e330513e-Paper-Conference.pdf)
  - [PerturboLLaVA: Reducing Multimodal Hallucinations with Perturbative Visual Training](https://proceedings.iclr.cc/paper_files/paper/2025/file/9a8eb202c060b7d81f5889631cbcd47e-Paper-Conference.pdf)
  - [Intervening Anchor Token: Decoding Strategy in Alleviating Hallucinations for MLLMs](https://proceedings.iclr.cc/paper_files/paper/2025/file/4537e2172096d966228d68c428392894-Paper-Conference.pdf)
  - [Self-Introspective Decoding: Alleviating Hallucinations for Large Vision-Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/3cc87f2bd3e3b4df8f9217326761c322-Paper-Conference.pdf)
  - [Activation Steering Decoding: Mitigating Hallucination in Large Vision-Language Models through Bidirectional Hidden State Intervention](https://aclanthology.org/2025.acl-long.634.pdf)
  - [Mitigating Object Hallucination in Large Vision-Language Models via Image-Grounded Guidance](https://raw.githubusercontent.com/mlresearch/v267/main/assets/zhao25j/zhao25j.pdf)
  - [The Hidden Life of Tokens: Reducing Hallucination of Large Vision-Language Models Via Visual Information Steering](https://raw.githubusercontent.com/mlresearch/v267/main/assets/li25ca/li25ca.pdf)
  - [Multi-Frequency Contrastive Decoding: Alleviating Hallucinations for Large Vision-Language Models](https://aclanthology.org/2025.emnlp-main.1452.pdf)
  - [Mitigating Hallucinations in Large Vision-Language Models via Entity-Centric Multimodal Preference Optimization](https://aclanthology.org/2025.emnlp-main.982.pdf)
  - [Mitigating Hallucinations in Vision-Language Models through Image-Guided Head Suppression](https://aclanthology.org/2025.emnlp-main.631.pdf)
- **MS-COCO** (measurement instrument): *measured_by*, 3 papers
  > Object hallucination. CIDEr (↑) for captioning and CHAIRs (↓) for hallucination on COCO dataset. (Figure 2a)
  - [Beyond task performance: evaluating and reducing the flaws of large multimodal models with in-context-learning](https://proceedings.iclr.cc/paper_files/paper/2024/file/5df817c5dd95293ebf6d1583303a8c73-Paper-Conference.pdf)
  - [Understanding and Mitigating Hallucination in Large Vision-Language Models via Modular Attribution and Intervention](https://proceedings.iclr.cc/paper_files/paper/2025/file/8001c3568152d134d821cd46d4d84768-Paper-Conference.pdf)
  - [DAMO: Decoding by Accumulating Activations Momentum for Mitigating Hallucinations in Vision-Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/8f0f23417ce1d00212a7c85c2560c392-Paper-Conference.pdf)
- **MME** (measurement instrument): *measured_by*, 3 papers
  > The MME hallucination subset extends scope beyond object hallucination. Following [34], we evaluation 4 perception sub-tasks that examines LVLMs on object-level and attribute-level hallucinations... (Sec. 5.4)
  - [Mitigating Object Hallucination via Concentric Causal Attention](https://proceedings.neurips.cc/paper_files/paper/2024/file/a76ed4a8ef522c823d73925e7fff16d4-Paper-Conference.pdf)
  - [Do You Keep an Eye on What I Ask? Mitigating Multimodal Hallucination via Attention-Guided Ensemble Decoding](https://proceedings.iclr.cc/paper_files/paper/2025/file/637b275a6e65924719198188fc939632-Paper-Conference.pdf)
  - [Multi-Frequency Contrastive Decoding: Alleviating Hallucinations for Large Vision-Language Models](https://aclanthology.org/2025.emnlp-main.1452.pdf)
- **AMBER** (measurement instrument): *measured_by*, 3 papers
  > To evaluate performance on both generative and discriminative tasks, we use AMBER (Wang et al., 2023b), which measures hallucination using several metrics. For generative tasks, AMBER assesses the frequency of hallucinated objects in image descriptions... (Section 4.1)
  - [Mitigating Object Hallucination in MLLMs via Data-augmented Phrase-level Alignment](https://proceedings.iclr.cc/paper_files/paper/2025/file/b73228d026ef49bfa49f95b7e330513e-Paper-Conference.pdf)
  - [Evaluating and Mitigating Object Hallucination in Large Vision-Language Models: Can They Still See Removed Objects?](https://aclanthology.org/2025.naacl-long.349.pdf)
  - [SHARP: Steering Hallucination in LVLMs via Representation Engineering](https://aclanthology.org/2025.emnlp-main.725.pdf)
- **Object HalBench** (measurement instrument): *measured_by*, 3 papers
  > To ensure that oDPO effectively mitigates object hallucinations in LVLMs, we conduct evaluations on four widely used object hallucination benchmarks: Object HalBench (Rohrbach et al., 2018), MME-Hall (Fu et al., 2023), AMBER (Wang et al., 2023a) and MMHalBench (Sun et al., 2024). (Section 4.2)
  - [Evaluating and Mitigating Object Hallucination in Large Vision-Language Models: Can They Still See Removed Objects?](https://aclanthology.org/2025.naacl-long.349.pdf)
  - [DAMA: Data- and Model-aware Alignment of Multi-modal LLMs](https://raw.githubusercontent.com/mlresearch/v267/main/assets/lu25m/lu25m.pdf)
  - [Mitigating Hallucinations in Large Vision-Language Models via Entity-Centric Multimodal Preference Optimization](https://aclanthology.org/2025.emnlp-main.982.pdf)
- **LLM-as-a-judge** (measurement instrument): *measured_by*, 2 papers
  > "we evaluate LURE on six open-source LVLMs and found it outperforms the previous best approach in both general object hallucination evaluation metrics, GPT, and human evaluations" (Abstract); "In addition to human evaluation, inspired from (Zheng et al., 2023), we also prompt GPT-3.5 to compare different descriptions. In this GPT evaluation" (Section 4.1)
  - [Analyzing and Mitigating Object Hallucination in Large Vision-Language Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/fc625e831361cfcc82cb74224fdc66cb-Paper-Conference.pdf)
  - [Mitigating Object Hallucination in Large Vision-Language Models via Image-Grounded Guidance](https://raw.githubusercontent.com/mlresearch/v267/main/assets/zhao25j/zhao25j.pdf)
- **Human evaluation** (measurement instrument): *measured_by*, 1 paper
  > In this human evaluation, participants are assigned the task of annotating hallucinatory objects and we rank different methods based on human feedback.
  - [Analyzing and Mitigating Object Hallucination in Large Vision-Language Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/fc625e831361cfcc82cb74224fdc66cb-Paper-Conference.pdf)
- **NoCaps** (measurement instrument): *measured_by*, 1 paper
  > To evaluate object hallucination in visual caption, we use images from the COCO validation and Nocaps (Agrawal et al., 2019) datasets (Section 5.1).
  - [Understanding and Mitigating Hallucination in Large Vision-Language Models via Modular Attribution and Intervention](https://proceedings.iclr.cc/paper_files/paper/2025/file/8001c3568152d134d821cd46d4d84768-Paper-Conference.pdf)
- **Representational stability** (construct): *correlates*, 1 paper
  > We comprehensively present and analyze the correlation between vision feature stability and model hallucinations in Section 3.
  - [Reducing Hallucinations in Large Vision-Language Models via Latent Space Steering](https://proceedings.iclr.cc/paper_files/paper/2025/file/b4008025c2182bfe16fcc8566ee14d64-Paper-Conference.pdf)
- **A-OKVQA** (measurement instrument): *measured_by*, 1 paper
  > we... examined object hallucination using the SEEM-annotated MSCOCO and A-OKVQA datasets from POPE. (Section 4)
  - [DAMO: Decoding by Accumulating Activations Momentum for Mitigating Hallucinations in Vision-Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/8f0f23417ce1d00212a7c85c2560c392-Paper-Conference.pdf)
- **MMHal-Bench** (measurement instrument): *measured_by*, 1 paper
  > “We utilize MMHal-Bench (Sun et al., 2023), which evaluates hallucination across 12 object-topics, including object attributes, presence of adversarial objects, and spatial relations, among others.”
  - [Mitigating Object Hallucination in MLLMs via Data-augmented Phrase-level Alignment](https://proceedings.iclr.cc/paper_files/paper/2025/file/b73228d026ef49bfa49f95b7e330513e-Paper-Conference.pdf)

### → Object hallucination
- **Multimodal alignment** (construct): *causes*, 1 paper
  > this design leads to long-term decay [61] in multimodal alignment... but induces insufficient interactions between visual tokens and instruction tokens, leading to inferior multimodal alignment and object hallucinations in the trained LVLMs (see our experiments in Sec. 3 for details). (Introduction)
  - [Mitigating Object Hallucination via Concentric Causal Attention](https://proceedings.neurips.cc/paper_files/paper/2024/file/a76ed4a8ef522c823d73925e7fff16d4-Paper-Conference.pdf)

### Associated with
- **Hallucination** (behavioral indicator), 2 papers
  > In the realm of MLLMs, “hallucination” typically refers to “object hallucination,” where the models generate plausible outputs containing objects that are either absent from or mismatched with the images (Section 2)
  - [Unleashing Region Understanding in Intermediate Layers for MLLM-based Referring Expression Generation](https://proceedings.neurips.cc/paper_files/paper/2024/file/da76884a4e003ad0de97804ec4578e5b-Paper-Conference.pdf)
  - [Mitigating Object Hallucination in MLLMs via Data-augmented Phrase-level Alignment](https://proceedings.iclr.cc/paper_files/paper/2025/file/b73228d026ef49bfa49f95b7e330513e-Paper-Conference.pdf)
- **Faithfulness** (construct), 1 paper
  > Such phenomenon challenges the faithfulness and reliability of LVLMs in practical use, impeding their deployments to real-world applications [14]. (Introduction)
  - [Mitigating Object Hallucination via Concentric Causal Attention](https://proceedings.neurips.cc/paper_files/paper/2024/file/a76ed4a8ef522c823d73925e7fff16d4-Paper-Conference.pdf)
- **Visual perception** (construct), 1 paper
  > With CCA, visual tokens can better interact with instruction tokens, thereby enhancing model’s perception capability and alleviating object hallucination. (Abstract)
  - [Mitigating Object Hallucination via Concentric Causal Attention](https://proceedings.neurips.cc/paper_files/paper/2024/file/a76ed4a8ef522c823d73925e7fff16d4-Paper-Conference.pdf)
- **Image captioning** (behavioral indicator), 1 paper
  > “HALVA substantially reduces hallucination in image descriptions compared to the base variants.”
  - [Mitigating Object Hallucination in MLLMs via Data-augmented Phrase-level Alignment](https://proceedings.iclr.cc/paper_files/paper/2025/file/b73228d026ef49bfa49f95b7e330513e-Paper-Conference.pdf)
- **Visual question answering** (behavioral indicator), 1 paper
  > “we compare the performance of MLLMs on visual question-answering tasks using both object hallucination (AMBER) and general vision-language (TextVQA) benchmarks.”
  - [Mitigating Object Hallucination in MLLMs via Data-augmented Phrase-level Alignment](https://proceedings.iclr.cc/paper_files/paper/2025/file/b73228d026ef49bfa49f95b7e330513e-Paper-Conference.pdf)
