# ImageNet-1k
**Type:** Measurement instrument  
**Supporting papers:** 84  
**Also known as:** ImageNet, ImageNet-1K, ImageNet-2012, ImageNet1k  

## State of the Field

**What it is.** Most papers describe ImageNet-1k as a large-scale image classification or object-recognition benchmark, usually defined over 1,000 categories or classes. Some definitions add scale details, describing over 1.2 million images, or over a million training images plus 50,000 validation images, and papers variously refer to ImageNet1k, ImageNet-1K, ImageNet-2012, or the ILSVRC2012 validation split. A smaller line of work also treats it as a benchmark for class-conditional image generation, while other papers use its images, categories, or class labels to build few-shot classification, fine-grained object VQA, structured-rationale, or attack evaluations.

**What it is claimed to measure.** Across papers, ImageNet-1k is linked to 3 constructs and 4 behavioral indicators. The prevailing usage is to measure image classification, with smaller lines of work using it to measure image generation, object recognition, and zero-shot classification. At the construct level, papers also use it to measure multimodal alignment, and more occasionally adaptability and generalization, for example through alignment scores or top-1 zero-shot accuracy on ImageNet, and through 16-shot domain adaptation evaluation.

**Space of uses.** Papers do not link it to another measurement instrument. They most often position it as a standard benchmark for training and evaluation: models are trained from scratch or with supervised learning on it, used for pre-training and downstream evaluation, or evaluated with top-1 accuracy, FID, Inception Score, and Brier score depending on the task. Quoted passages also place it in broader benchmark suites alongside CIFAR-10, CIFAR-100, MS-COCO, Flowers102, and Stanford-Cars.

## Sources

**ImageNet** (25 papers: [A Multi-Level Framework for Accelerating Training Transformer Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/33f2c200b71ce947d356d171022458ec-Paper-Conference.pdf), [Bootstrapping Variational Information Pursuit with Large Language and Vision Models for Interpretable Image Classification](https://proceedings.iclr.cc/paper_files/paper/2024/file/8e12ba543adc673da5b89c9311fcf72c-Paper-Conference.pdf), [Follow-Up Differential Descriptions: Language Models Resolve Ambiguities for Image Classification](https://proceedings.iclr.cc/paper_files/paper/2024/file/17eca81974d2fd34f458916e0bfd820d-Paper-Conference.pdf), [Frozen Transformers in Language Models Are Effective Visual Encoder Layers](https://proceedings.iclr.cc/paper_files/paper/2024/file/03cd3cf3f74d4f9ce5958de269960884-Paper-Conference.pdf), [Inducing High Energy-Latency of Large Vision-Language Models with Verbose Images](https://proceedings.iclr.cc/paper_files/paper/2024/file/4a6a5e2e8a27262501bda3463fcf7b21-Paper-Conference.pdf), [Language Model Beats Diffusion - Tokenizer is key to visual generation](https://proceedings.iclr.cc/paper_files/paper/2024/file/036912a83bdbb1fd792baf6532f102d8-Paper-Conference.pdf), [Language Modeling Is Compression](https://proceedings.iclr.cc/paper_files/paper/2024/file/3cbf627fa24fb6cb576e04e689b9428b-Paper-Conference.pdf), [Open-ended VQA benchmarking of Vision-Language models by exploiting Classification datasets and their semantic hierarchy](https://proceedings.iclr.cc/paper_files/paper/2024/file/cb1c4782f159b55380b4584671c4fd88-Paper-Conference.pdf), [Repeated Random Sampling for Minimizing the Time-to-Accuracy of Learning](https://proceedings.iclr.cc/paper_files/paper/2024/file/68b8d2bc77268facfc75a78782da9559-Paper-Conference.pdf), [Understanding prompt engineering may not require rethinking generalization](https://proceedings.iclr.cc/paper_files/paper/2024/file/803b9c4a8e4784072fdd791c54d614e2-Paper-Conference.pdf), [Unleashing the Power of Pre-trained Language Models for Offline Reinforcement Learning](https://proceedings.iclr.cc/paper_files/paper/2024/file/c7793beb7f32b559df55d48370f2b8ae-Paper-Conference.pdf), [Bridging Compressed Image Latents and Multimodal Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/17061a94c3c7fda5fa24bbdd1832fa99-Paper-Conference.pdf), [QAVA: Query-Agnostic Visual Attack to Large Vision-Language Models](https://aclanthology.org/2025.naacl-long.512.pdf), [Typographic Attacks in a Multi-Image Setting](https://aclanthology.org/2025.naacl-long.626.pdf), [AutoEval Done Right: Using Synthetic Data for Model Evaluation](https://raw.githubusercontent.com/mlresearch/v267/main/assets/boyeau25a/boyeau25a.pdf), [Beyond Accuracy: Ensuring Correct Predictions With Correct Rationales](https://proceedings.neurips.cc/paper_files/paper/2024/file/4bbeef01d9753fd5a29e9fd02d275698-Paper-Conference.pdf), [CoIN: A Benchmark of Continual Instruction Tuning for Multimodel Large Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/6a45500d9eda640deed90d8a62742be5-Paper-Datasets_and_Benchmarks_Track.pdf), [Fast yet Safe: Early-Exiting with Risk Control](https://proceedings.neurips.cc/paper_files/paper/2024/file/ea5a63f7ddb82e58623693fd1f4933f7-Paper-Conference.pdf), [IMPACT: A Large-scale Integrated Multimodal Patent Analysis and Creation Dataset for Design Patents](https://proceedings.neurips.cc/paper_files/paper/2024/file/e3301977b92f28e32639ec99eb08f4a1-Paper-Datasets_and_Benchmarks_Track.pdf), [IPO: Interpretable Prompt Optimization for Vision-Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/e52e4de8689a9955b6d3ff421d019387-Paper-Conference.pdf), [Neural Residual Diffusion Models for Deep Scalable Vision Generation](https://proceedings.neurips.cc/paper_files/paper/2024/file/d51ceadaf09a4699f18986702df24987-Paper-Conference.pdf), [PACE: Marrying generalization in PArameter-efficient fine-tuning with Consistency rEgularization](https://proceedings.neurips.cc/paper_files/paper/2024/file/70a06501001e1820fd1eb9ee821302d2-Paper-Conference.pdf), [Text-Guided Attention is All You Need for Zero-Shot Robustness in Vision-Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/aec2dfc4f5e19acf05c15587c889dbc4-Paper-Conference.pdf), [UniBench: Visual Reasoning Requires Rethinking Vision-Language Beyond Scaling](https://proceedings.neurips.cc/paper_files/paper/2024/file/96271227d3e204501d199433e56af289-Paper-Datasets_and_Benchmarks_Track.pdf), [Why are Visually-Grounded Language Models Bad at Image Classification?](https://proceedings.neurips.cc/paper_files/paper/2024/file/5c7024041be305c94d7311cfcc53d93e-Paper-Conference.pdf))
> Standard benchmark for image generation and classification, used here to evaluate class-conditional image generation quality using FID and Inception Score.

**ImageNet-1K** (1 paper: [MoH: Multi-Head Attention as Mixture-of-Head Attention](https://raw.githubusercontent.com/mlresearch/v267/main/assets/jin25l/jin25l.pdf))
> A large-scale dataset for object recognition and image classification containing over 1.2 million images across 1,000 categories.

**ImageNet-2012** (1 paper: [Loss Functions and Operators Generated by f-Divergences](https://raw.githubusercontent.com/mlresearch/v267/main/assets/roulet25a/roulet25a.pdf))
> A large-scale dataset for image classification containing over a million training images and 50,000 validation images across 1,000 distinct classes.

**ImageNet1k** (2 papers: [TripletCLIP: Improving Compositional Reasoning of CLIP via Synthetic Vision-Language Negatives](https://proceedings.neurips.cc/paper_files/paper/2024/file/39781da4b5d05bc2908ce08e43bc6404-Paper-Conference.pdf), [Theory, Analysis, and Best Practices for Sigmoid Self-Attention](https://proceedings.iclr.cc/paper_files/paper/2025/file/a43b459e9fab3a703148ba0c83b8a442-Paper-Conference.pdf))
> A large-scale image dataset with 1000 object classes, commonly used as a benchmark for zero-shot image classification.

**ImageNet-1k** (2 papers: [Multi-Head Mixture-of-Experts](https://proceedings.neurips.cc/paper_files/paper/2024/file/ab05dc8bf36a9f66edbff6992ec86f56-Paper-Conference.pdf), [CAMEx: Curvature-aware Merging of Experts](https://proceedings.iclr.cc/paper_files/paper/2025/file/341d64b067e06c6ebea97a498c90d598-Paper-Conference.pdf))
> Image classification benchmark used to evaluate pure vision tasks on 1,000 object categories.

## Relationships

### → ImageNet-1k
- **Image classification** (behavioral indicator): *measured_by*, 35 papers
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
- **Multimodal alignment** (construct): *measured_by*, 2 papers
  > We start by reporting and comparing the alignment scores when using CLIP, SharedCLIP, and AlignCLIP models on the ... ImageNet-1K ... test datasets. (Section 4.2)
  - [Mitigate the Gap: Improving Cross-Modal Alignment in CLIP](https://proceedings.iclr.cc/paper_files/paper/2025/file/cc1de06a58ba1db43538a37e076e466d-Paper-Conference.pdf)
  - [VILA-U: a Unified Foundation Model Integrating Visual Understanding and Generation](https://proceedings.iclr.cc/paper_files/paper/2025/file/e9e140df6de01afb672cb859d203c307-Paper-Conference.pdf)
- **Image generation** (behavioral indicator): *measured_by*, 2 papers
  > when evaluating on the ImageNet dataset, a gold standard benchmark for image generation (Section 1).
  - [Language Model Beats Diffusion - Tokenizer is key to visual generation](https://proceedings.iclr.cc/paper_files/paper/2024/file/036912a83bdbb1fd792baf6532f102d8-Paper-Conference.pdf)
  - [Elucidating the design space of language models for image generation](https://raw.githubusercontent.com/mlresearch/v267/main/assets/liu25w/liu25w.pdf)
- **Generalization** (construct): *measured_by*, 1 paper
  > In this section, we evaluate the generalization of discrete prompts generated by Greedy on CIFAR-10, CIFAR-100, ImageNet as well as domain generalization datasets fMoW (Christie et al., 2018) and OfficeHome (Venkateswara et al., 2017) (Section 5)
  - [Understanding prompt engineering may not require rethinking generalization](https://proceedings.iclr.cc/paper_files/paper/2024/file/803b9c4a8e4784072fdd791c54d614e2-Paper-Conference.pdf)
- **Adaptability** (construct): *measured_by*, 1 paper
  > For domain adaptation, following [82, 7], we train on ImageNet [11] with a 16-shot setting, use the validation split by [82] for hyperparameter selection and report the results on the official validation set (Section 4).
  - [PACE: Marrying generalization in PArameter-efficient fine-tuning with Consistency rEgularization](https://proceedings.neurips.cc/paper_files/paper/2024/file/70a06501001e1820fd1eb9ee821302d2-Paper-Conference.pdf)
- **Object recognition** (behavioral indicator): *measured_by*, 1 paper
  > "ImageNet, often considered a cornerstone in the field of computer vision, has been widely used as a benchmark to evaluate the performance of image recognition models."
  - [UniBench: Visual Reasoning Requires Rethinking Vision-Language Beyond Scaling](https://proceedings.neurips.cc/paper_files/paper/2024/file/96271227d3e204501d199433e56af289-Paper-Datasets_and_Benchmarks_Track.pdf)
- **Zero-shot classification** (behavioral indicator): *measured_by*, 1 paper
  > a lower proportion of SSC results in decreased accuracy in ImageNet zero-shot classification. (Section 4.1)
  - [Revisit Large-Scale Image-Caption Data in Pre-training Multimodal Foundation Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/ebba182cb97864368fdb6ae00773a5e4-Paper-Conference.pdf)
