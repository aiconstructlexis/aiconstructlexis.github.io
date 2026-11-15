# Detoxify
**Type:** Measurement instrument  
**Supporting papers:** 14  

## State of the Field

**What it is.** Across the surveyed work, Detoxify is most commonly described as a model-based toxicity scoring or classification tool for text. Papers variously refer to it as a machine learning model, library, classifier, or evaluation procedure, but the prevailing usage is to assign a toxicity score to generated text, responses, or continuations, with higher scores indicating more toxic generation; some authors also describe it as automatically generating disutility measures for LLM outputs. One paper uses the classifier with six attributes, toxicity, severe toxicity, obscene, threat, insult, and identity attack, and another reports retraining Detoxify on a biased subset of the Jigsaw Unintended Bias in Toxicity Classification dataset.

**What it is claimed to measure.** The reported links are concentrated rather than spread across many targets: papers use Detoxify to measure one construct, Toxicity, and one behavioral indicator, Harmful content generation. The prevailing use is for Toxicity, with papers describing it as assessing the toxicity of responses, generated text, continuations, or tweets; some operationalizations use the raw score, while others derive metrics such as Toxicity Probability and Expected Maximum Toxicity from repeated generations. A smaller line of work links it to Harmful content generation, where a prompt is counted as successful when the chatbot response is flagged by Detoxify or the OpenAI Moderation API.

**Space of uses.** Across papers, Detoxify is typically used as an automatic scorer applied after generation within broader evaluation pipelines. Several papers use it alongside the OpenAI Moderation API, and another uses it with Perspective API; papers also report thresholded use, including 0.1 in one study and 0.7 in another. Beyond these pairings, the reported use is mainly as a toxicity check over model outputs, including responses, continuations, and tweets.

**Concerns raised.** Explicit concerns are limited, but one comparison study reports weaker flagging of harmful fine-tuning examples under a thresholded setup: at a threshold of at least 0.7, Detoxify flagged 6% of 100 harmful instructions, compared with 17% for OpenAI's API and 4% for Perspective API in the same experiment.

## Sources

**Detoxify** (7 papers: [Fine-tuning Aligned Language Models Compromises Safety, Even When Users Do Not Intend To!](https://proceedings.iclr.cc/paper_files/paper/2024/file/83b7da3ed13f06c13ce82235c8eedf35-Paper-Conference.pdf), [Model Merging by Uncertainty-Based Gradient Matching](https://proceedings.iclr.cc/paper_files/paper/2024/file/327b9b8d4e45c3f81568e11ffc505f77-Paper-Conference.pdf), [Prompt Risk Control: A Rigorous Framework for Responsible Deployment of Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/114292cf3f930ba157ed33f66997fee2-Paper-Conference.pdf), [WildChat: 1M ChatGPT Interaction Logs in the Wild](https://proceedings.iclr.cc/paper_files/paper/2024/file/9421261e06f1a63a352b068f1ac90609-Paper-Conference.pdf), [Model Editing as a Robust and Denoised variant of DPO: A Case Study on Toxicity](https://proceedings.iclr.cc/paper_files/paper/2025/file/acb7ce5aab6e134300a2361dd90a501f-Paper-Conference.pdf), [Conformal Tail Risk Control for Large Language Model Alignment](https://raw.githubusercontent.com/mlresearch/v267/main/assets/chen25bd/chen25bd.pdf), [PBI-Attack: Prior-Guided Bimodal Interactive Black-Box Jailbreak Attack for Toxicity Maximization](https://aclanthology.org/2025.emnlp-main.32.pdf))
> Model-based toxicity scoring system that assigns a toxicity score to generated text.

## Relationships

### → Detoxify
- **Toxicity** (construct): *measured_by*, 10 papers
  > We detect unsafe content using two toxicity classification tools: the OpenAI Moderation API and Detoxify (Section 4).
  - [WildChat: 1M ChatGPT Interaction Logs in the Wild](https://proceedings.iclr.cc/paper_files/paper/2024/file/9421261e06f1a63a352b068f1ac90609-Paper-Conference.pdf)
  - [Model Merging by Uncertainty-Based Gradient Matching](https://proceedings.iclr.cc/paper_files/paper/2024/file/327b9b8d4e45c3f81568e11ffc505f77-Paper-Conference.pdf)
  - [UniDetox: Universal Detoxification of Large Language Models via Dataset Distillation](https://proceedings.iclr.cc/paper_files/paper/2025/file/c4800e97411c7f199b2895425f2933a5-Paper-Conference.pdf)
  - [Model Editing as a Robust and Denoised variant of DPO: A Case Study on Toxicity](https://proceedings.iclr.cc/paper_files/paper/2025/file/acb7ce5aab6e134300a2361dd90a501f-Paper-Conference.pdf)
  - [Improving and Assessing the Fidelity of Large Language Models Alignment to Online Communities](https://aclanthology.org/2025.naacl-long.5.pdf)
  - [Conformal Tail Risk Control for Large Language Model Alignment](https://raw.githubusercontent.com/mlresearch/v267/main/assets/chen25bd/chen25bd.pdf)
  - [Metadata Conditioning Accelerates Language Model Pre-training](https://raw.githubusercontent.com/mlresearch/v267/main/assets/gao25p/gao25p.pdf)
  - [Breaking Bad Tokens: Detoxification of LLMs Using Sparse Autoencoders](https://aclanthology.org/2025.emnlp-main.641.pdf)
  - [Who Holds the Pen? Caricature and Perspective in LLM Retellings of History](https://aclanthology.org/2025.emnlp-main.996.pdf)
  - [How Does DPO Reduce Toxicity? A Mechanistic Neuron-Level Analysis](https://aclanthology.org/2025.emnlp-main.1501.pdf)
- **Harmful content generation** (behavioral indicator): *measured_by*, 1 paper
  > The success rate for each prompt was determined by whether the chatbot’s response to such a prompt was flagged by either Detoxify or OpenAI Moderation API (Section 4).
  - [WildChat: 1M ChatGPT Interaction Logs in the Wild](https://proceedings.iclr.cc/paper_files/paper/2024/file/9421261e06f1a63a352b068f1ac90609-Paper-Conference.pdf)
