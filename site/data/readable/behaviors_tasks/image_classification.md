# Image classification
**Type:** Behavioral indicator  
**Supporting papers:** 140  
**Also known as:** Object classification, Cell type classification, Few-shot classification, Visual classification, Image recognition, Zero-shot object recognition, Zero-shot image classification  

## State of the Field

**Space of definitions.** Across papers, the prevailing usage is assigning a class or category label to an input or entire image from a predefined set of categories, with success framed as producing the correct label. Many papers cast this in vision-language or prompt-conditioned terms, often in zero-shot form by comparing the image to text prompts or class descriptions, as one paper describes 'image classification via pretrained vision-language models' (Understanding prompt engineering may not require rethinking generalization). A smaller line of work formulates the same behavior through labeled in-context examples, or narrows the required label to a scientific species name or a cell type.

**Variants.** Papers use several nearby names for the behavior, including object classification, visual classification, image recognition, few-shot classification, zero-shot image classification, and zero-shot object recognition. The studied settings range from whole-image classification to identifying individual cropped objects, industrial products, organisms, and microscopy cell types, and from general image classification to fine-grained visual classification and adaptation tasks. Some work also studies distribution shift across environments, where 'the goal is to obtain a predictor that correctly classifies x in new cities' (Context is Environment).

**Space of elicitation and scores.** Papers link this behavior to 24 measurement instruments. The most frequently used are ImageNet-1k, CIFAR-10, CIFAR-100, VTAB-1k, and Food-101, and the linked instruments are typically described as image classification datasets, benchmarks, or suites of classification tasks. When scoring is stated, papers report classification accuracy, including zero-shot accuracy and top-1 accuracy, and other linked instruments extend the task to fine-grained, transfer, and specialized-domain settings.

**What it is taken as evidence of.** Papers do not converge on a single construct that this behavior reflects. Instead, they link it to five constructs with mixed relation types and directions. One paper claims a causal relationship from Image classification to General ability, stating that enhanced classification performance transfers to general capabilities, while other papers report that Image classification is related to Visual understanding and In-context learning; Generalization and Fine-grained perception are also reported as related to Image classification.

## Sources

**Image classification** (27 papers: [A Multi-Level Framework for Accelerating Training Transformer Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/33f2c200b71ce947d356d171022458ec-Paper-Conference.pdf), [An Image Is Worth 1000 Lies: Transferability of Adversarial Images across Prompts on Vision-Language Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/674ad201bc8fa74b3c9979230aa0c63b-Paper-Conference.pdf), [Batch Calibration: Rethinking Calibration for In-Context Learning and Prompt Engineering](https://proceedings.iclr.cc/paper_files/paper/2024/file/003e438cf04e3caf0a5c908495e484fe-Paper-Conference.pdf), [Bootstrapping Variational Information Pursuit with Large Language and Vision Models for Interpretable Image Classification](https://proceedings.iclr.cc/paper_files/paper/2024/file/8e12ba543adc673da5b89c9311fcf72c-Paper-Conference.pdf), [Context is Environment](https://proceedings.iclr.cc/paper_files/paper/2024/file/03645743ea35690f30d795d6bac149a5-Paper-Conference.pdf), [Faithful Vision-Language Interpretation via Concept Bottleneck Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/678cffc05549fdabda971127602084c6-Paper-Conference.pdf), [Follow-Up Differential Descriptions: Language Models Resolve Ambiguities for Image Classification](https://proceedings.iclr.cc/paper_files/paper/2024/file/17eca81974d2fd34f458916e0bfd820d-Paper-Conference.pdf), [Frozen Transformers in Language Models Are Effective Visual Encoder Layers](https://proceedings.iclr.cc/paper_files/paper/2024/file/03cd3cf3f74d4f9ce5958de269960884-Paper-Conference.pdf), [Improving LoRA in Privacy-preserving Federated Learning](https://proceedings.iclr.cc/paper_files/paper/2024/file/4e243e95c913b367775d71d7182b99d9-Paper-Conference.pdf), [Increasing Model Capacity for Free: A Simple Strategy for Parameter Efficient Fine-tuning](https://proceedings.iclr.cc/paper_files/paper/2024/file/ce3fd6b9dfe458dc258a8164a5e95bd2-Paper-Conference.pdf), [Is attention required for ICL? Exploring the Relationship Between Model Architecture and In-Context Learning Ability](https://proceedings.iclr.cc/paper_files/paper/2024/file/ea6d17af54f827336fc8fed27ca0319d-Paper-Conference.pdf), [Model Merging by Uncertainty-Based Gradient Matching](https://proceedings.iclr.cc/paper_files/paper/2024/file/327b9b8d4e45c3f81568e11ffc505f77-Paper-Conference.pdf), [NOLA: Compressing LoRA using Linear Combination of Random Basis](https://proceedings.iclr.cc/paper_files/paper/2024/file/66b99dbf9ed172abac5cb5ccfc82d1e2-Paper-Conference.pdf), [Octavius: Mitigating Task Interference in MLLMs via LoRA-MoE](https://proceedings.iclr.cc/paper_files/paper/2024/file/6b3b238c5786536dc9f835760e2dba02-Paper-Conference.pdf), [Parameter-Efficient Multi-Task Model Fusion with Partial Linearization](https://proceedings.iclr.cc/paper_files/paper/2024/file/5bacb12bf81e98e2ee0eed953a23c656-Paper-Conference.pdf), [Parameter-Efficient Orthogonal Finetuning via Butterfly Factorization](https://proceedings.iclr.cc/paper_files/paper/2024/file/a63ce8e6867a1bf4b4ca62e5077814d9-Paper-Conference.pdf), [Repeated Random Sampling for Minimizing the Time-to-Accuracy of Learning](https://proceedings.iclr.cc/paper_files/paper/2024/file/68b8d2bc77268facfc75a78782da9559-Paper-Conference.pdf), [The Hedgehog & the Porcupine: Expressive Linear Attentions with Softmax Mimicry](https://proceedings.iclr.cc/paper_files/paper/2024/file/ebba182cb97864368fdb6ae00773a5e4-Paper-Conference.pdf), [Understanding prompt engineering may not require rethinking generalization](https://proceedings.iclr.cc/paper_files/paper/2024/file/803b9c4a8e4784072fdd791c54d614e2-Paper-Conference.pdf), [VeRA: Vector-based Random Matrix Adaptation](https://proceedings.iclr.cc/paper_files/paper/2024/file/1b53ad08de383a049e9668a9d0b6a053-Paper-Conference.pdf), [Text-Guided Attention is All You Need for Zero-Shot Robustness in Vision-Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/aec2dfc4f5e19acf05c15587c889dbc4-Paper-Conference.pdf), [Model merging with SVD to tie the Knots](https://proceedings.iclr.cc/paper_files/paper/2025/file/0d4f8a5109c5083b5307fcd0bddae7a7-Paper-Conference.pdf), [SSH: Sparse Spectrum Adaptation via Discrete Hartley Transformation](https://aclanthology.org/2025.naacl-long.522.pdf), [QAVA: Query-Agnostic Visual Attack to Large Vision-Language Models](https://aclanthology.org/2025.naacl-long.512.pdf), [UORA: Uniform Orthogonal Reinitialization Adaptation in Parameter Efficient Fine-Tuning of Large Models](https://aclanthology.org/2025.acl-long.575.pdf), [AutoEval Done Right: Using Synthetic Data for Model Evaluation](https://raw.githubusercontent.com/mlresearch/v267/main/assets/boyeau25a/boyeau25a.pdf), [Tiny Budgets, Big Gains: Parameter Placement Strategy in Parameter Super-Efficient Fine-Tuning](https://aclanthology.org/2025.emnlp-main.321.pdf))
> Assigning a label to an image using a vision-language model by comparing it to text prompts, in a zero-shot setting.

**Object classification** (3 papers: [UniBench: Visual Reasoning Requires Rethinking Vision-Language Beyond Scaling](https://proceedings.neurips.cc/paper_files/paper/2024/file/96271227d3e204501d199433e56af289-Paper-Datasets_and_Benchmarks_Track.pdf), [MMAD: A Comprehensive Benchmark for Multimodal Large Language Models in Industrial Anomaly Detection](https://proceedings.iclr.cc/paper_files/paper/2025/file/d91ffbe9c126765755ff52d36b715683-Paper-Conference.pdf), [Open-ended VQA benchmarking of Vision-Language models by exploiting Classification datasets and their semantic hierarchy](https://proceedings.iclr.cc/paper_files/paper/2024/file/cb1c4782f159b55380b4584671c4fd88-Paper-Conference.pdf))
> Observably identifying and classifying objects within images across various categories.

**Species classification** (1 paper: [VLM4Bio: A Benchmark Dataset to Evaluate Pretrained Vision-Language Models for Trait Discovery from Biological Images](https://proceedings.neurips.cc/paper_files/paper/2024/file/eced4a5fbc776e81b45e2f72447f0164-Paper-Datasets_and_Benchmarks_Track.pdf))
> The task of identifying and providing the correct scientific name (species class) for an organism shown in an image.

**Cell type classification** (1 paper: [Micro-Bench: A Microscopy Benchmark for Vision-Language Understanding](https://proceedings.neurips.cc/paper_files/paper/2024/file/36b31e1bb8ecd4f4081686448e9eff2d-Paper-Datasets_and_Benchmarks_Track.pdf))
> The task of identifying the specific type of cell present in a microscopy image.

**Few-shot classification** (2 papers: [Bridging Compressed Image Latents and Multimodal Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/17061a94c3c7fda5fa24bbdd1832fa99-Paper-Conference.pdf), [Overthinking the Truth: Understanding how Language Models Process False Demonstrations](https://proceedings.iclr.cc/paper_files/paper/2024/file/bb63841e1ad12370a34504f15c60db4f-Paper-Conference.pdf))
> An image classification task where the model must generalize to new classes given only a few examples of each.

**Visual classification** (2 papers: [Privacy-Preserving Personalized Federated Prompt Learning for Multimodal Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/4431224d3762aa655f0aee4eaf04ff16-Paper-Conference.pdf), [SAN: Hypothesizing Long-Term Synaptic Development and Neural Engram Mechanism in Scalable Model’s Parameter-Efficient Fine-Tuning](https://raw.githubusercontent.com/mlresearch/v267/main/assets/dai25e/dai25e.pdf))
> Assigning an image to one of several classes using a prompt-conditioned multimodal model.

**Image recognition** (1 paper: [Disentangling and Integrating Relational and Sensory Information in Transformer Architectures](https://raw.githubusercontent.com/mlresearch/v267/main/assets/altabaa25a/altabaa25a.pdf))
> The observable task of classifying an image into one of a predefined set of categories.

**Zero-shot object recognition** (1 paper: [Kernel-based Unsupervised Embedding Alignment for Enhanced Visual Representation in Vision-language Models](https://raw.githubusercontent.com/mlresearch/v267/main/assets/gong25b/gong25b.pdf))
> The task of classifying an image into one of several categories without having seen any training examples for those specific categories.

**Zero-shot image classification** (3 papers: [VisMin: Visual Minimal-Change Understanding](https://proceedings.neurips.cc/paper_files/paper/2024/file/c3070c3388552a08a3326f0d28dc2af9-Paper-Conference.pdf), [MAP: Low-compute Model Merging with Amortized Pareto Fronts via Quadratic Approximation](https://proceedings.iclr.cc/paper_files/paper/2025/file/a3724221b623bf1966e92cd266ac6177-Paper-Conference.pdf), [What If We Recaption Billions of Web Images with LLaMA-3?](https://raw.githubusercontent.com/mlresearch/v267/main/assets/li25ch/li25ch.pdf))
> The task of classifying an image into one of several categories without having seen any training examples for those specific categories.

## Relationships

### Image classification →
- **ImageNet-1k** (measurement instrument): *measured_by*, 35 papers
  > We evaluate our method on 12 image recognition datasets. We use the ... ImageNet (Deng et al., 2009)... (Section 4)
  - [Follow-Up Differential Descriptions: Language Models Resolve Ambiguities for Image Classification](https://proceedings.iclr.cc/paper_files/paper/2024/file/17eca81974d2fd34f458916e0bfd820d-Paper-Conference.pdf)
  - [The Hedgehog & the Porcupine: Expressive Linear Attentions with Softmax Mimicry](https://proceedings.iclr.cc/paper_files/paper/2024/file/ebba182cb97864368fdb6ae00773a5e4-Paper-Conference.pdf)
  - [Megalodon: Efficient LLM Pretraining and Inference with Unlimited Context Length](https://proceedings.neurips.cc/paper_files/paper/2024/file/840abfadd04c967feaa2a49aba94a32d-Paper-Conference.pdf)
  - [LoTLIP: Improving Language-Image Pre-training for Long Text Understanding](https://proceedings.neurips.cc/paper_files/paper/2024/file/77828623211df05497ce3658300dafd9-Paper-Conference.pdf)
  - [MambaTree: Tree Topology is All You Need in State Space Model](https://proceedings.neurips.cc/paper_files/paper/2024/file/89b89c04f55ea7c7ca989992bb6a98c0-Paper-Conference.pdf)
  - [Multi-Head Mixture-of-Experts](https://proceedings.neurips.cc/paper_files/paper/2024/file/ab05dc8bf36a9f66edbff6992ec86f56-Paper-Conference.pdf)
  - [Why are Visually-Grounded Language Models Bad at Image Classification?](https://proceedings.neurips.cc/paper_files/paper/2024/file/5c7024041be305c94d7311cfcc53d93e-Paper-Conference.pdf)
  - [TripletCLIP: Improving Compositional Reasoning of CLIP via Synthetic Vision-Language Negatives](https://proceedings.neurips.cc/paper_files/paper/2024/file/39781da4b5d05bc2908ce08e43bc6404-Paper-Conference.pdf)
  - [4M-21: An Any-to-Any Vision Model for Tens of Tasks and Modalities](https://proceedings.neurips.cc/paper_files/paper/2024/file/71883294314045d60c900113a359934b-Paper-Conference.pdf)
  - [IPO: Interpretable Prompt Optimization for Vision-Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/e52e4de8689a9955b6d3ff421d019387-Paper-Conference.pdf)
  - [Orchid: Flexible and Data-Dependent Convolution for Sequence Modeling](https://proceedings.neurips.cc/paper_files/paper/2024/file/8ccc5ec30a8d46793d790e2216efd40d-Paper-Conference.pdf)
  - [Learning from Teaching Regularization: Generalizable Correlations Should be Easy to Imitate](https://proceedings.neurips.cc/paper_files/paper/2024/file/01ce1ae7f94d139e4917f9e4425a4f38-Paper-Conference.pdf)
  - [Mitigate the Gap: Improving Cross-Modal Alignment in CLIP](https://proceedings.iclr.cc/paper_files/paper/2025/file/cc1de06a58ba1db43538a37e076e466d-Paper-Conference.pdf)
  - [OATS: Outlier-Aware Pruning Through Sparse and Low Rank Decomposition](https://proceedings.iclr.cc/paper_files/paper/2025/file/7f2fc4053a66edfa430bcdf9a6ff3b17-Paper-Conference.pdf)
  - [Tight Clusters Make Specialized Experts](https://proceedings.iclr.cc/paper_files/paper/2025/file/854a9ab0f323b841955e70ca383b27d1-Paper-Conference.pdf)
  - [CAMEx: Curvature-aware Merging of Experts](https://proceedings.iclr.cc/paper_files/paper/2025/file/341d64b067e06c6ebea97a498c90d598-Paper-Conference.pdf)
  - [RandLoRA: Full rank parameter-efficient fine-tuning of large models](https://proceedings.iclr.cc/paper_files/paper/2025/file/382b95a6580cfb0b5ca33c74b4e0e770-Paper-Conference.pdf)
  - [Mix-LN: Unleashing the Power of Deeper Layers by Combining Pre-LN and Post-LN](https://proceedings.iclr.cc/paper_files/paper/2025/file/f3d637987f36563fa45f943f8eadc2d0-Paper-Conference.pdf)
  - [Longhorn: State Space Models are Amortized Online Learners](https://proceedings.iclr.cc/paper_files/paper/2025/file/ee0e45ff4de76cbfdf07015a7839f339-Paper-Conference.pdf)
  - [MambaQuant: Quantizing the Mamba Family with Variance Aligned Rotation Methods](https://proceedings.iclr.cc/paper_files/paper/2025/file/51ba8a68f471d952af625d1faf55e6c6-Paper-Conference.pdf)
  - [SageAttention: Accurate 8-Bit Attention for Plug-and-play Inference Acceleration](https://proceedings.iclr.cc/paper_files/paper/2025/file/b286c344d38e10d2466c0514b78e2f36-Paper-Conference.pdf)
  - [Causal Graphical Models for Vision-Language Compositional Understanding](https://proceedings.iclr.cc/paper_files/paper/2025/file/b9a17133e3943509243b5e197c1c23b2-Paper-Conference.pdf)
  - [Transformer Meets Twicing: Harnessing Unattended Residual Information](https://proceedings.iclr.cc/paper_files/paper/2025/file/90cdfb6ac8d9f96bdf0ce92f5f05c391-Paper-Conference.pdf)
  - [Bridging Compressed Image Latents and Multimodal Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/17061a94c3c7fda5fa24bbdd1832fa99-Paper-Conference.pdf)
  - [TopoNets: High performing vision and language models with brain-like topography](https://proceedings.iclr.cc/paper_files/paper/2025/file/6191ab7080c840f67eaf5dff7d5edfcb-Paper-Conference.pdf)
  - [Entropy-based Activation Function Optimization: A Method on Searching Better Activation Functions](https://proceedings.iclr.cc/paper_files/paper/2025/file/d5cbee19280e1fd9d9dba8c1febf48bd-Paper-Conference.pdf)
  - [Towards Semantic Equivalence of Tokenization in Multimodal LLM](https://proceedings.iclr.cc/paper_files/paper/2025/file/e95eb5206c867be843fbc14bbfe8c10e-Paper-Conference.pdf)
  - [QAVA: Query-Agnostic Visual Attack to Large Vision-Language Models](https://aclanthology.org/2025.naacl-long.512.pdf)
  - [LAuReL: Learned Augmented Residual Layer](https://raw.githubusercontent.com/mlresearch/v267/main/assets/menghani25a/menghani25a.pdf)
  - [RWKVQuant: Quantizing the RWKV Family with Proxy Guided Hybrid of Scalar and Vector Quantization](https://raw.githubusercontent.com/mlresearch/v267/main/assets/xu25at/xu25at.pdf)
  - [Dynamic Sparse Training of Diagonally Sparse Networks](https://raw.githubusercontent.com/mlresearch/v267/main/assets/tyagi25a/tyagi25a.pdf)
  - [LASER: Attention with Exponential Transformation](https://raw.githubusercontent.com/mlresearch/v267/main/assets/duvvuri25a/duvvuri25a.pdf)
  - [MoH: Multi-Head Attention as Mixture-of-Head Attention](https://raw.githubusercontent.com/mlresearch/v267/main/assets/jin25l/jin25l.pdf)
  - [Attention-Only Transformers via Unrolled Subspace Denoising](https://raw.githubusercontent.com/mlresearch/v267/main/assets/wang25bu/wang25bu.pdf)
  - [ModalPrompt: Towards Efficient Multimodal Continual Instruction Tuning with Dual-Modality Guided Prompt](https://aclanthology.org/2025.emnlp-main.609.pdf)
- **CIFAR-10** (measurement instrument): *measured_by*, 17 papers
  > We perform experiments on the image classification task... We use CIFAR10... datasets for finetuning. (Section 3.4)
  - [NOLA: Compressing LoRA using Linear Combination of Random Basis](https://proceedings.iclr.cc/paper_files/paper/2024/file/66b99dbf9ed172abac5cb5ccfc82d1e2-Paper-Conference.pdf)
  - [Faithful Vision-Language Interpretation via Concept Bottleneck Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/678cffc05549fdabda971127602084c6-Paper-Conference.pdf)
  - [Octavius: Mitigating Task Interference in MLLMs via LoRA-MoE](https://proceedings.iclr.cc/paper_files/paper/2024/file/6b3b238c5786536dc9f835760e2dba02-Paper-Conference.pdf)
  - [A Multi-Level Framework for Accelerating Training Transformer Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/33f2c200b71ce947d356d171022458ec-Paper-Conference.pdf)
  - [Sparse High Rank Adapters](https://proceedings.neurips.cc/paper_files/paper/2024/file/18c0102cb7f1a02c14f0929089b2e576-Paper-Conference.pdf)
  - [Orchid: Flexible and Data-Dependent Convolution for Sequence Modeling](https://proceedings.neurips.cc/paper_files/paper/2024/file/8ccc5ec30a8d46793d790e2216efd40d-Paper-Conference.pdf)
  - [Mitigate the Gap: Improving Cross-Modal Alignment in CLIP](https://proceedings.iclr.cc/paper_files/paper/2025/file/cc1de06a58ba1db43538a37e076e466d-Paper-Conference.pdf)
  - [MCNC: Manifold-Constrained Reparameterization for Neural Compression](https://proceedings.iclr.cc/paper_files/paper/2025/file/2f63d2963526bdd9ff1b8bcc2dc9905a-Paper-Conference.pdf)
  - [Quantum-PEFT: Ultra parameter-efficient fine-tuning](https://proceedings.iclr.cc/paper_files/paper/2025/file/4e52bbb99690d1e05c7ef7b4c8b3569a-Paper-Conference.pdf)
  - [Causal Graphical Models for Vision-Language Compositional Understanding](https://proceedings.iclr.cc/paper_files/paper/2025/file/b9a17133e3943509243b5e197c1c23b2-Paper-Conference.pdf)
  - [Large (Vision) Language Models are Unsupervised In-Context Learners](https://proceedings.iclr.cc/paper_files/paper/2025/file/3e887bf77d0ba6db38802e552a0d81d2-Paper-Conference.pdf)
  - [Transformer Block Coupling and its Correlation with Generalization in LLMs](https://proceedings.iclr.cc/paper_files/paper/2025/file/3f7f788b479a26348605a9f97c465d22-Paper-Conference.pdf)
  - [Entropy-based Activation Function Optimization: A Method on Searching Better Activation Functions](https://proceedings.iclr.cc/paper_files/paper/2025/file/d5cbee19280e1fd9d9dba8c1febf48bd-Paper-Conference.pdf)
  - [On Exact Bit-level Reversible Transformers Without Changing Architecture](https://raw.githubusercontent.com/mlresearch/v267/main/assets/zhang25ao/zhang25ao.pdf)
  - [Dynamic Sparse Training of Diagonally Sparse Networks](https://raw.githubusercontent.com/mlresearch/v267/main/assets/tyagi25a/tyagi25a.pdf)
  - [Disentangling and Integrating Relational and Sensory Information in Transformer Architectures](https://raw.githubusercontent.com/mlresearch/v267/main/assets/altabaa25a/altabaa25a.pdf)
  - [SAFE: Finding Sparse and Flat Minima to Improve Pruning](https://raw.githubusercontent.com/mlresearch/v267/main/assets/lee25s/lee25s.pdf)
- **CIFAR-100** (measurement instrument): *measured_by*, 16 papers
  > We perform experiments on the image classification task... We use... CIFAR100... datasets for finetuning. (Section 3.4)
  - [NOLA: Compressing LoRA using Linear Combination of Random Basis](https://proceedings.iclr.cc/paper_files/paper/2024/file/66b99dbf9ed172abac5cb5ccfc82d1e2-Paper-Conference.pdf)
  - [Faithful Vision-Language Interpretation via Concept Bottleneck Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/678cffc05549fdabda971127602084c6-Paper-Conference.pdf)
  - [A Multi-Level Framework for Accelerating Training Transformer Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/33f2c200b71ce947d356d171022458ec-Paper-Conference.pdf)
  - [Sparse High Rank Adapters](https://proceedings.neurips.cc/paper_files/paper/2024/file/18c0102cb7f1a02c14f0929089b2e576-Paper-Conference.pdf)
  - [Learning from Teaching Regularization: Generalizable Correlations Should be Easy to Imitate](https://proceedings.neurips.cc/paper_files/paper/2024/file/01ce1ae7f94d139e4917f9e4425a4f38-Paper-Conference.pdf)
  - [SVFT: Parameter-Efficient Fine-Tuning with Singular Vectors](https://proceedings.neurips.cc/paper_files/paper/2024/file/48c368f105e8145b945227b73255635a-Paper-Conference.pdf)
  - [Mitigate the Gap: Improving Cross-Modal Alignment in CLIP](https://proceedings.iclr.cc/paper_files/paper/2025/file/cc1de06a58ba1db43538a37e076e466d-Paper-Conference.pdf)
  - [MCNC: Manifold-Constrained Reparameterization for Neural Compression](https://proceedings.iclr.cc/paper_files/paper/2025/file/2f63d2963526bdd9ff1b8bcc2dc9905a-Paper-Conference.pdf)
  - [Causal Graphical Models for Vision-Language Compositional Understanding](https://proceedings.iclr.cc/paper_files/paper/2025/file/b9a17133e3943509243b5e197c1c23b2-Paper-Conference.pdf)
  - [Entropy-based Activation Function Optimization: A Method on Searching Better Activation Functions](https://proceedings.iclr.cc/paper_files/paper/2025/file/d5cbee19280e1fd9d9dba8c1febf48bd-Paper-Conference.pdf)
  - [SSH: Sparse Spectrum Adaptation via Discrete Hartley Transformation](https://aclanthology.org/2025.naacl-long.522.pdf)
  - [On Exact Bit-level Reversible Transformers Without Changing Architecture](https://raw.githubusercontent.com/mlresearch/v267/main/assets/zhang25ao/zhang25ao.pdf)
  - [Dynamic Sparse Training of Diagonally Sparse Networks](https://raw.githubusercontent.com/mlresearch/v267/main/assets/tyagi25a/tyagi25a.pdf)
  - [Disentangling and Integrating Relational and Sensory Information in Transformer Architectures](https://raw.githubusercontent.com/mlresearch/v267/main/assets/altabaa25a/altabaa25a.pdf)
  - [SAFE: Finding Sparse and Flat Minima to Improve Pruning](https://raw.githubusercontent.com/mlresearch/v267/main/assets/lee25s/lee25s.pdf)
  - [Towards Infinite-Long Prefix in Transformer](https://aclanthology.org/2025.emnlp-main.563.pdf)
- **VTAB-1k** (measurement instrument): *measured_by*, 7 papers
  > For the CV task, we use ViT-B/16 (Dosovitskiy et al., 2020) as our pre-trained model and evaluate the efficacy of our method on the VTAB-1k (Zhai et al., 2019) benchmark. (Section 4)
  - [Increasing Model Capacity for Free: A Simple Strategy for Parameter Efficient Fine-tuning](https://proceedings.iclr.cc/paper_files/paper/2024/file/ce3fd6b9dfe458dc258a8164a5e95bd2-Paper-Conference.pdf)
  - [Parameter-Efficient Orthogonal Finetuning via Butterfly Factorization](https://proceedings.iclr.cc/paper_files/paper/2024/file/a63ce8e6867a1bf4b4ca62e5077814d9-Paper-Conference.pdf)
  - [PACE: Marrying generalization in PArameter-efficient fine-tuning with Consistency rEgularization](https://proceedings.neurips.cc/paper_files/paper/2024/file/70a06501001e1820fd1eb9ee821302d2-Paper-Conference.pdf)
  - [Release the Powers of Prompt Tuning: Cross-Modality Prompt Transfer](https://proceedings.iclr.cc/paper_files/paper/2025/file/7ae9589ff1a691d09ef0528e4e309b2f-Paper-Conference.pdf)
  - [Promoting Ensemble Diversity with Interactive Bayesian Distributional Robustness for Fine-tuning Foundation Models](https://raw.githubusercontent.com/mlresearch/v267/main/assets/pham25b/pham25b.pdf)
  - [RepLoRA: Reparameterizing Low-rank Adaptation via the Perspective of Mixture of Experts](https://raw.githubusercontent.com/mlresearch/v267/main/assets/truong25a/truong25a.pdf)
  - [SAN: Hypothesizing Long-Term Synaptic Development and Neural Engram Mechanism in Scalable Model’s Parameter-Efficient Fine-Tuning](https://raw.githubusercontent.com/mlresearch/v267/main/assets/dai25e/dai25e.pdf)
- **Oxford Flowers-102** (measurement instrument): *measured_by*, 6 papers
  > We evaluate our method on 12 image recognition datasets. We use the ... Flowers102 (Nilsback & Zisserman, 2008)... (Section 4)
  - [Follow-Up Differential Descriptions: Language Models Resolve Ambiguities for Image Classification](https://proceedings.iclr.cc/paper_files/paper/2024/file/17eca81974d2fd34f458916e0bfd820d-Paper-Conference.pdf)
  - [A Multi-Level Framework for Accelerating Training Transformer Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/33f2c200b71ce947d356d171022458ec-Paper-Conference.pdf)
  - [Why are Visually-Grounded Language Models Bad at Image Classification?](https://proceedings.neurips.cc/paper_files/paper/2024/file/5c7024041be305c94d7311cfcc53d93e-Paper-Conference.pdf)
  - [IPO: Interpretable Prompt Optimization for Vision-Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/e52e4de8689a9955b6d3ff421d019387-Paper-Conference.pdf)
  - [SVFT: Parameter-Efficient Fine-Tuning with Singular Vectors](https://proceedings.neurips.cc/paper_files/paper/2024/file/48c368f105e8145b945227b73255635a-Paper-Conference.pdf)
  - [Mitigate the Gap: Improving Cross-Modal Alignment in CLIP](https://proceedings.iclr.cc/paper_files/paper/2025/file/cc1de06a58ba1db43538a37e076e466d-Paper-Conference.pdf)
- **Food-101** (measurement instrument): *measured_by*, 6 papers
  > We evaluate our method on 12 image recognition datasets. We use the ... Food101 (Bossard et al., 2014)... (Section 4)
  - [Follow-Up Differential Descriptions: Language Models Resolve Ambiguities for Image Classification](https://proceedings.iclr.cc/paper_files/paper/2024/file/17eca81974d2fd34f458916e0bfd820d-Paper-Conference.pdf)
  - [NOLA: Compressing LoRA using Linear Combination of Random Basis](https://proceedings.iclr.cc/paper_files/paper/2024/file/66b99dbf9ed172abac5cb5ccfc82d1e2-Paper-Conference.pdf)
  - [Sparse High Rank Adapters](https://proceedings.neurips.cc/paper_files/paper/2024/file/18c0102cb7f1a02c14f0929089b2e576-Paper-Conference.pdf)
  - [IPO: Interpretable Prompt Optimization for Vision-Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/e52e4de8689a9955b6d3ff421d019387-Paper-Conference.pdf)
  - [SVFT: Parameter-Efficient Fine-Tuning with Singular Vectors](https://proceedings.neurips.cc/paper_files/paper/2024/file/48c368f105e8145b945227b73255635a-Paper-Conference.pdf)
  - [Towards Infinite-Long Prefix in Transformer](https://aclanthology.org/2025.emnlp-main.563.pdf)
- **DTD** (measurement instrument): *measured_by*, 5 papers
  > We evaluate our method on 12 image recognition datasets. We use the ... Describable Textures Dataset (DTD) (Cimpoi et al., 2014) (texture classification)... (Section 4)
  - [Follow-Up Differential Descriptions: Language Models Resolve Ambiguities for Image Classification](https://proceedings.iclr.cc/paper_files/paper/2024/file/17eca81974d2fd34f458916e0bfd820d-Paper-Conference.pdf)
  - [Sparse High Rank Adapters](https://proceedings.neurips.cc/paper_files/paper/2024/file/18c0102cb7f1a02c14f0929089b2e576-Paper-Conference.pdf)
  - [LoRA-Pro: Are Low-Rank Adapters Properly Optimized?](https://proceedings.iclr.cc/paper_files/paper/2025/file/ea184f920a0f0f8d8030aa1bd7ac9fd4-Paper-Conference.pdf)
  - [SSH: Sparse Spectrum Adaptation via Discrete Hartley Transformation](https://aclanthology.org/2025.naacl-long.522.pdf)
  - [To See a World in a Spark of Neuron: Disentangling Multi-Task Interference for Training-Free Model Merging](https://aclanthology.org/2025.emnlp-main.793.pdf)
- **EuroSAT** (measurement instrument): *measured_by*, 4 papers
  > We evaluate our method on 12 image recognition datasets. We use the ... EuroSAT (Helber et al., 2019) (satellite image classification)... (Section 4)
  - [Follow-Up Differential Descriptions: Language Models Resolve Ambiguities for Image Classification](https://proceedings.iclr.cc/paper_files/paper/2024/file/17eca81974d2fd34f458916e0bfd820d-Paper-Conference.pdf)
  - [LoRA-Pro: Are Low-Rank Adapters Properly Optimized?](https://proceedings.iclr.cc/paper_files/paper/2025/file/ea184f920a0f0f8d8030aa1bd7ac9fd4-Paper-Conference.pdf)
  - [SSH: Sparse Spectrum Adaptation via Discrete Hartley Transformation](https://aclanthology.org/2025.naacl-long.522.pdf)
  - [To See a World in a Spark of Neuron: Disentangling Multi-Task Interference for Training-Free Model Merging](https://aclanthology.org/2025.emnlp-main.793.pdf)
- **Stanford Cars** (measurement instrument): *measured_by*, 4 papers
  > We evaluate our method on 12 image recognition datasets. We use the ... Stanford Cars (Krause et al., 2013)... (Section 4)
  - [Follow-Up Differential Descriptions: Language Models Resolve Ambiguities for Image Classification](https://proceedings.iclr.cc/paper_files/paper/2024/file/17eca81974d2fd34f458916e0bfd820d-Paper-Conference.pdf)
  - [A Multi-Level Framework for Accelerating Training Transformer Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/33f2c200b71ce947d356d171022458ec-Paper-Conference.pdf)
  - [Mitigate the Gap: Improving Cross-Modal Alignment in CLIP](https://proceedings.iclr.cc/paper_files/paper/2025/file/cc1de06a58ba1db43538a37e076e466d-Paper-Conference.pdf)
  - [To See a World in a Spark of Neuron: Disentangling Multi-Task Interference for Training-Free Model Merging](https://aclanthology.org/2025.emnlp-main.793.pdf)
- **FGVC** (measurement instrument): *measured_by*, 3 papers
  > We evaluate our method across four visual classification adaptation tasks: VTAB-1K [78], few-shot learning [30], FGVC [28] and domain adaptation [82] (Section 4).
  - [PACE: Marrying generalization in PArameter-efficient fine-tuning with Consistency rEgularization](https://proceedings.neurips.cc/paper_files/paper/2024/file/70a06501001e1820fd1eb9ee821302d2-Paper-Conference.pdf)
  - [WeGeFT: Weight-Generative Fine-Tuning for Multi-Faceted Efficient Adaptation of Large Models](https://raw.githubusercontent.com/mlresearch/v267/main/assets/savadikar25a/savadikar25a.pdf)
  - [SAN: Hypothesizing Long-Term Synaptic Development and Neural Engram Mechanism in Scalable Model’s Parameter-Efficient Fine-Tuning](https://raw.githubusercontent.com/mlresearch/v267/main/assets/dai25e/dai25e.pdf)
- **RESISC45** (measurement instrument): *measured_by*, 3 papers
  > Performance on image classification benchmarks – CIFAR-100 (C100), Food101 (F101), Flowers102 (F102), and Resisc-45 (R45). (Table 4)
  - [SVFT: Parameter-Efficient Fine-Tuning with Singular Vectors](https://proceedings.neurips.cc/paper_files/paper/2024/file/48c368f105e8145b945227b73255635a-Paper-Conference.pdf)
  - [LoRA-Pro: Are Low-Rank Adapters Properly Optimized?](https://proceedings.iclr.cc/paper_files/paper/2025/file/ea184f920a0f0f8d8030aa1bd7ac9fd4-Paper-Conference.pdf)
  - [To See a World in a Spark of Neuron: Disentangling Multi-Task Interference for Training-Free Model Merging](https://aclanthology.org/2025.emnlp-main.793.pdf)
- **SUN397** (measurement instrument): *measured_by*, 2 papers
  > We perform experiments on the image classification task... We use... SUN397... datasets for finetuning. (Section 3.4)
  - [NOLA: Compressing LoRA using Linear Combination of Random Basis](https://proceedings.iclr.cc/paper_files/paper/2024/file/66b99dbf9ed172abac5cb5ccfc82d1e2-Paper-Conference.pdf)
  - [To See a World in a Spark of Neuron: Disentangling Multi-Task Interference for Training-Free Model Merging](https://aclanthology.org/2025.emnlp-main.793.pdf)
- **Places365** (measurement instrument): *measured_by*, 2 papers
  > We evaluate our method on 12 image recognition datasets. We use the ... Places365 (Zhou et al., 2017)... (Section 4)
  - [Follow-Up Differential Descriptions: Language Models Resolve Ambiguities for Image Classification](https://proceedings.iclr.cc/paper_files/paper/2024/file/17eca81974d2fd34f458916e0bfd820d-Paper-Conference.pdf)
  - [Faithful Vision-Language Interpretation via Concept Bottleneck Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/678cffc05549fdabda971127602084c6-Paper-Conference.pdf)
- **CUB-200-2011** (measurement instrument): *measured_by*, 2 papers
  > We perform experiments on the image classification task... We use... CUB-200-2011... datasets for finetuning. (Section 3.4)
  - [NOLA: Compressing LoRA using Linear Combination of Random Basis](https://proceedings.iclr.cc/paper_files/paper/2024/file/66b99dbf9ed172abac5cb5ccfc82d1e2-Paper-Conference.pdf)
  - [Faithful Vision-Language Interpretation via Concept Bottleneck Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/678cffc05549fdabda971127602084c6-Paper-Conference.pdf)
- **Caltech101** (measurement instrument): *measured_by*, 2 papers
  > We evaluated the aforementioned models on four widely-used image classification benchmarks: ImageNet (shortened as , same below) [11], Flowers102 ( ) [35], StanfordCars ( ) [21], and Caltech101 ( ) [13] (Section 2.2)
  - [Why are Visually-Grounded Language Models Bad at Image Classification?](https://proceedings.neurips.cc/paper_files/paper/2024/file/5c7024041be305c94d7311cfcc53d93e-Paper-Conference.pdf)
  - [Privacy-Preserving Personalized Federated Prompt Learning for Multimodal Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/4431224d3762aa655f0aee4eaf04ff16-Paper-Conference.pdf)
- **MNIST** (measurement instrument): *measured_by*, 2 papers
  > We consider models trained on the MNIST dataset of handwritten digits and the Fashion-MNIST dataset of clothing images.
  - [Bilinear MLPs enable weight-based mechanistic interpretability](https://proceedings.iclr.cc/paper_files/paper/2025/file/7504142a20a3e1fe9dd7de42f475828c-Paper-Conference.pdf)
  - [To See a World in a Spark of Neuron: Disentangling Multi-Task Interference for Training-Free Model Merging](https://aclanthology.org/2025.emnlp-main.793.pdf)
- **SVHN** (measurement instrument): *measured_by*, 2 papers
  > We fine-tune the CLIP-ViT-B/16 (Radford et al., 2021) model on various datasets, including StanfordCars, DTD, EuroSAT, GTSRB, RESISC45, SUN397, and SVHN.
  - [LoRA-Pro: Are Low-Rank Adapters Properly Optimized?](https://proceedings.iclr.cc/paper_files/paper/2025/file/ea184f920a0f0f8d8030aa1bd7ac9fd4-Paper-Conference.pdf)
  - [To See a World in a Spark of Neuron: Disentangling Multi-Task Interference for Training-Free Model Merging](https://aclanthology.org/2025.emnlp-main.793.pdf)
- **FGVC-Aircraft** (measurement instrument): *measured_by*, 1 paper
  > We evaluate our method on 12 image recognition datasets. We use the ... FGVCAircraft (Maji et al., 2013) (aircraft model classification)... (Section 4)
  - [Follow-Up Differential Descriptions: Language Models Resolve Ambiguities for Image Classification](https://proceedings.iclr.cc/paper_files/paper/2024/file/17eca81974d2fd34f458916e0bfd820d-Paper-Conference.pdf)
- **ImageNetV2** (measurement instrument): *measured_by*, 1 paper
  > We evaluate our method on 12 image recognition datasets. We use the ... ImageNetV2 (Kornblith et al., 2019)... (Section 4)
  - [Follow-Up Differential Descriptions: Language Models Resolve Ambiguities for Image Classification](https://proceedings.iclr.cc/paper_files/paper/2024/file/17eca81974d2fd34f458916e0bfd820d-Paper-Conference.pdf)
- **Stanford Dogs** (measurement instrument): *measured_by*, 1 paper
  > We evaluate our method on 12 image recognition datasets. We use the ... Stanford Dogs (Khosla et al., 2011) datasets. (Section 4)
  - [Follow-Up Differential Descriptions: Language Models Resolve Ambiguities for Image Classification](https://proceedings.iclr.cc/paper_files/paper/2024/file/17eca81974d2fd34f458916e0bfd820d-Paper-Conference.pdf)
- **General ability** (construct): *causes*, 1 paper
  > enhanced classification performance of the VLM transfers to its general capabilities
  - [Why are Visually-Grounded Language Models Bad at Image Classification?](https://proceedings.neurips.cc/paper_files/paper/2024/file/5c7024041be305c94d7311cfcc53d93e-Paper-Conference.pdf)
- **ImageNet-100** (measurement instrument): *measured_by*, 1 paper
  > We begin by evaluating on training Vision Transformers from scratch on the ImageNet-100 dataset (Tian et al., 2020). (Section 4.1)
  - [MCNC: Manifold-Constrained Reparameterization for Neural Compression](https://proceedings.iclr.cc/paper_files/paper/2025/file/2f63d2963526bdd9ff1b8bcc2dc9905a-Paper-Conference.pdf)
- **ImageNet-Sketch** (measurement instrument): *measured_by*, 1 paper
  > TIMM is evaluated on on three image datasets: ImageNet (Deng et al., 2009), ImageNet-Sketch (Sketch) (Wang et al., 2019), and ImageNet-Rendition (ImageNet-r) (Hendrycks et al., 2021).
  - [SageAttention: Accurate 8-Bit Attention for Plug-and-play Inference Acceleration](https://proceedings.iclr.cc/paper_files/paper/2025/file/b286c344d38e10d2466c0514b78e2f36-Paper-Conference.pdf)
- **Oxford-IIIT Pets** (measurement instrument): *measured_by*, 1 paper
  > Image classification is performed on the CIFAR-100 (Krause et al., 2013), DTD (Cimpoi et al., 2014), EuroSAT (Helber et al., 2019), and Oxford-Pets (Parkhi et al., 2012) datasets. (Section 4.7)
  - [SSH: Sparse Spectrum Adaptation via Discrete Hartley Transformation](https://aclanthology.org/2025.naacl-long.522.pdf)
- **Tiny ImageNet** (measurement instrument): *measured_by*, 1 paper
  > We evaluate the method on three image classification datasets: CIFAR-100 (Krizhevsky et al., 2009), Food-101 (Bossard et al., 2014), and Tiny-Imagenet (mn-moustafa, 2017). (Section 6)
  - [Towards Infinite-Long Prefix in Transformer](https://aclanthology.org/2025.emnlp-main.563.pdf)

### Associated with
- **Visual understanding** (construct), 1 paper
  > To study the performance of the joint inference framework on tasks that require visual comprehension, we evaluate our methods on seven vision datasets, spanning both image classification tasks (CIFAR-10, CIFAR-100, Food101) and visual question-answering tasks (COCO-Color, COCO-Number, VQAv2 and VizWiz). (Section 5.2)
  - [Large (Vision) Language Models are Unsupervised In-Context Learners](https://proceedings.iclr.cc/paper_files/paper/2025/file/3e887bf77d0ba6db38802e552a0d81d2-Paper-Conference.pdf)
- **In-context learning** (construct), 1 paper
  > we design a 5-way 1-shot classification scenario to evaluate the performance with in-context learning (Section 4.1)
  - [Bridging Compressed Image Latents and Multimodal Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/17061a94c3c7fda5fa24bbdd1832fa99-Paper-Conference.pdf)
- **Generalization** (construct), 1 paper
  > Moreover, we extend our experiments to image classification tasks, aiming to evaluate the model's generalizability across diverse domains.
  - [Orchid: Flexible and Data-Dependent Convolution for Sequence Modeling](https://proceedings.neurips.cc/paper_files/paper/2024/file/8ccc5ec30a8d46793d790e2216efd40d-Paper-Conference.pdf)
- **Fine-grained perception** (construct), 1 paper
  > “The improvements are particularly notable for images with low resolution (e.g., CIFAR) or tiny objects (e.g., EuroSAT), highlighting enhanced fine-grained perception capabilities.”
  - [Kernel-based Unsupervised Embedding Alignment for Enhanced Visual Representation in Vision-language Models](https://raw.githubusercontent.com/mlresearch/v267/main/assets/gong25b/gong25b.pdf)
