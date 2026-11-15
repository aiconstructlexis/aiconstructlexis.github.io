# OpenAI Moderation API
**Type:** Measurement instrument  
**Supporting papers:** 17  
**Also known as:** OpenAI moderation API, OpenAI Moderation, OpenAI-Moderation  

## State of the Field

**What it is.** Across papers, the prevailing usage treats OpenAI Moderation API as an OpenAI-provided content-safety tool or evaluation procedure for classifying text under safety policies. Definitions commonly describe it as assigning violation categories or scores for harms such as hate, harassment, self-harm, sexual content, and violence, and some papers add that it returns both a binary safe or harmful tag and a continuous harmfulness score. Papers use it to tag unsafe conversations, assess the safety of text data before and after alignment rewriting, detect and filter toxic or inappropriate content, and evaluate moderation or jailbreak responses; a smaller line of work refers to OpenAI Moderation as a query-classification benchmark or as a defense strategy in jailbreak evaluation.

**What it is claimed to measure.** In the recorded relationships, papers use it to measure 3 constructs and 2 behavioral indicators. The construct links are Toxicity, Harmlessness, and Safety, and the behavioral-indicator links are Content moderation and Harmful content generation. Across those claims, papers use it to flag unsafe or harmful text, judge whether a response is safe, and determine harmful content generation by whether a response is flagged.

**Space of uses.** Papers sometimes pair it with other moderation tools, with examples including Detoxify for unsafe-content detection and the Perspective API for flagging harmful fine-tuning data. Elsewhere it is positioned as a secondary evaluation method, a preprocessing filter to remove toxic content before training or evaluation, moderation testing for multilingual multi-turn alignment, and a tool for assessing the perceived harmfulness of generated scenarios. One jailbreak study also uses OpenAI-Moderation as a defense strategy and reports that it reduces ASR slightly by 3%-8%, and one query-classification setup lists it alongside ToxicChat.

## Sources

**OpenAI moderation API** (2 papers: [LMSYS-Chat-1M: A Large-Scale Real-World LLM Conversation Dataset](https://proceedings.iclr.cc/paper_files/paper/2024/file/5f9bfdfe3685e4ccdbc0e7fb29cccf2a-Paper-Conference.pdf), [M2Lingual: Enhancing Multilingual, Multi-Turn Instruction Alignment in Large Language Models](https://aclanthology.org/2025.naacl-long.489.pdf))
> OpenAI Moderation API, a content-safety evaluation procedure that assigns violation categories to messages and is used here to tag unsafe conversations and evaluate moderation and jailbreak responses.

**OpenAI Moderation API** (5 papers: [WildChat: 1M ChatGPT Interaction Logs in the Wild](https://proceedings.iclr.cc/paper_files/paper/2024/file/9421261e06f1a63a352b068f1ac90609-Paper-Conference.pdf), [ALI-Agent: Assessing LLMs' Alignment with Human Values via Agent-based Evaluation](https://proceedings.neurips.cc/paper_files/paper/2024/file/b35c38f70065ac6c694089ca93a015bb-Paper-Conference.pdf), [Semantic Loss Guided Data Efficient Supervised Fine Tuning for Safe Responses in LLMs](https://proceedings.iclr.cc/paper_files/paper/2025/file/598ec93b6d2ed4fed4927b957b80f18c-Paper-Conference.pdf), [Benign Samples Matter! Fine-tuning On Outlier Benign Samples Severely Breaks Safety](https://raw.githubusercontent.com/mlresearch/v267/main/assets/guan25c/guan25c.pdf), [Interpretable Mnemonic Generation for Kanji Learning via Expectation-Maximization](https://aclanthology.org/2025.emnlp-main.1294.pdf))
> Official API provided by OpenAI to classify text content based on safety policies, including categories like hate, harassment, self-harm, and sexual content.

**OpenAI Moderation** (2 papers: [Alignment at Pre-training! Towards Native Alignment for Arabic LLMs](https://proceedings.neurips.cc/paper_files/paper/2024/file/195c4e2910bedabd813f9fe4e70c642c-Paper-Conference.pdf), [BingoGuard: LLM Content Moderation Tools with Risk Levels](https://proceedings.iclr.cc/paper_files/paper/2025/file/782b6152c04e9948c2cb3833e9a288ef-Paper-Conference.pdf))
> A publicly available tool from OpenAI used to assess the safety of text data by scoring it on dimensions like harassment, sexual content, hate speech, and violence.

**OpenAI-Moderation** (1 paper: [Foot-In-The-Door: A Multi-turn Jailbreak for LLMs](https://aclanthology.org/2025.emnlp-main.100.pdf))
> A defense mechanism and content moderation tool from OpenAI, used in this paper as a procedure to evaluate the robustness of a jailbreak attack.

## Relationships

### → OpenAI Moderation API
- **Toxicity** (construct): *measured_by*, 2 papers
  > We detect unsafe content using two toxicity classification tools: the OpenAI Moderation API and Detoxify (Section 4).
  - [WildChat: 1M ChatGPT Interaction Logs in the Wild](https://proceedings.iclr.cc/paper_files/paper/2024/file/9421261e06f1a63a352b068f1ac90609-Paper-Conference.pdf)
  - [Do as I do (Safely): Mitigating Task-Specific Fine-tuning Risks in Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/70de9e3948645a1be2de657f14d85c6d-Paper-Conference.pdf)
- **Harmlessness** (construct): *measured_by*, 1 paper
  > To evaluate the toxicity and harmfulness of the fine-tuning examples by prompting strategy we use OpenAI’s Moderation API. (Section 3.1)
  - [Do as I do (Safely): Mitigating Task-Specific Fine-tuning Risks in Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/70de9e3948645a1be2de657f14d85c6d-Paper-Conference.pdf)
- **Harmful content generation** (behavioral indicator): *measured_by*, 1 paper
  > The success rate for each prompt was determined by whether the chatbot’s response to such a prompt was flagged by either Detoxify or OpenAI Moderation API (Section 4).
  - [WildChat: 1M ChatGPT Interaction Logs in the Wild](https://proceedings.iclr.cc/paper_files/paper/2024/file/9421261e06f1a63a352b068f1ac90609-Paper-Conference.pdf)
- **Content moderation** (behavioral indicator): *measured_by*, 1 paper
  > "We utilize the OpenAI moderation API4 (Markov et al., 2023) to tag all conversations."
  - [LMSYS-Chat-1M: A Large-Scale Real-World LLM Conversation Dataset](https://proceedings.iclr.cc/paper_files/paper/2024/file/5f9bfdfe3685e4ccdbc0e7fb29cccf2a-Paper-Conference.pdf)
- **Safety** (construct): *measured_by*, 1 paper
  > To address this limitation, we used the OpenAI Moderation API as a secondary evaluation method. This API provides both a harmfulness score (in [0,1]), where 0 is the least harmful and 1 the most harmful) and a binary tag indicating whether the response is safe.
  - [Semantic Loss Guided Data Efficient Supervised Fine Tuning for Safe Responses in LLMs](https://proceedings.iclr.cc/paper_files/paper/2025/file/598ec93b6d2ed4fed4927b957b80f18c-Paper-Conference.pdf)
