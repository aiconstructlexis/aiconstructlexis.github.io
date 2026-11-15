# Honesty
**Type:** Construct  
**Supporting papers:** 42  
**Also known as:** Sincerity  

## State of the Field

**Space of definitions.** Across the surveyed work, the prevailing usage treats honesty as a latent model trait or disposition toward truthfulness, factual accuracy, and non-deception. Most definitions also fold in acknowledging limits, for example abstaining, saying "I don't know," declining to answer when information is insufficient, avoiding fabrication or hallucination, or matching stated confidence to accuracy. A smaller line of work narrows it to consistency with the model's internal beliefs or knowledge, and one survey uses the label "sincerity" for acting on what one believes to be true with sufficient evidence. Some authors describe honesty as a property of the model, while others describe it as the degree to which outputs are truthful and do not misrepresent facts or mislead.

**Space of facets.** Papers most often place honesty inside broader alignment taxonomies, especially alongside helpfulness and harmlessness as part of 3H or HHH, and one paper also lists it among five fine-grained alignment perspectives with unbiasedness and engagement. The concept is not fully stabilized against nearby terms: some papers separate honesty from truthfulness, with one defining honesty as stating what the model believes and truthfulness as stating what is objectively true, while other papers use truthfulness or factual accuracy inside their honesty definitions. "Sincerity" appears as an alternate label in cooperative settings, and work on strategic discussion explicitly contrasts honesty with deception.

**Space of measurement.** Papers operationalize honesty with 4 measurement instruments and 4 behavioral indicators. The most common linked instruments are UltraFeedback, a multi-aspect preference dataset with GPT-4 evaluations that includes an honest objective, LLM-as-a-judge ratings of honesty, and the QA benchmarks TriviaQA and TruthfulQA; behaviorally, honesty is tied to refusal, abstention, confidence expression, and hallucination. These measures track the same themes emphasized in many definitions: truthful or factual responses, uncertainty expression, and avoiding fabrication or hallucination.

**Links.** Some papers relate honesty to human preference alignment, treating it as one of the 3H or HHH principles, and some relate it to refusal or abstention, where honest behavior is giving "I don't know" or declining when knowledge is insufficient. Other papers relate honesty to calibration, confidence expression, hallucination, self-awareness of operational limits, truthfulness, sycophancy, and world knowledge; one paper says reducing sycophancy is a measure for enhancing honesty, and another says a model is more honest if it performs better on measures of world knowledge. One paper reports that harmlessness correlates with honesty and describes a potential trade-off, and one paper claims a causal relationship from honesty to trustworthiness.

## Sources

**Honesty** (7 papers: [AlpaGasus: Training a Better Alpaca with Fewer Data](https://proceedings.iclr.cc/paper_files/paper/2024/file/9543942c237ded1b39b1fd37259ff88e-Paper-Conference.pdf), [Beyond task performance: evaluating and reducing the flaws of large multimodal models with in-context-learning](https://proceedings.iclr.cc/paper_files/paper/2024/file/5df817c5dd95293ebf6d1583303a8c73-Paper-Conference.pdf), [How to Catch an AI Liar: Lie Detection in Black-Box LLMs by Asking Unrelated Questions](https://proceedings.iclr.cc/paper_files/paper/2024/file/efe79ae16496a0f5b57287873de072d1-Paper-Conference.pdf), [Improving Generalization of Alignment with Human Preferences through Group Invariant Learning](https://proceedings.iclr.cc/paper_files/paper/2024/file/c2d82a425af4c18a35049899fea5ee82-Paper-Conference.pdf), [SALMON: Self-Alignment with Instructable Reward Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/dda5cac5272a9bcd4bc73d90bc725ef1-Paper-Conference.pdf), [Training Socially Aligned Language Models on Simulated Social Interactions](https://proceedings.iclr.cc/paper_files/paper/2024/file/d763b4a2dde0ae7b77498516ce9f439e-Paper-Conference.pdf), [DeepResearcher: Scaling Deep Research via Reinforcement Learning in Real-world Environments](https://aclanthology.org/2025.emnlp-main.22.pdf))
> A desirable model trait encompassing truthfulness and the ability to acknowledge when it lacks information, for instance by abstaining from answering or avoiding hallucinations.

**Sincerity** (1 paper: [How to Enable Effective Cooperation Between Humans and NLP Models: A Survey of Principles, Formalizations, and Beyond](https://aclanthology.org/2025.acl-long.22.pdf))
> The latent tendency of a model to provide truthful and evidence-backed responses without deception during cooperation with humans.

## Relationships

### Honesty →
- **UltraFeedback** (measurement instrument): *measured_by*, 2 papers
  > UltraFeedback [7]: a multi-aspect alignment dataset with 64K prompts with preferences obtained from GPT-4, including "Instruction following", "Honest", "Truthful", and "Helpful" objectives (Section 4.1).
  - [MetaAligner: Towards Generalizable Multi-Objective Alignment of Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/3d03800841fa1bb2f43ef1750aafcce4-Paper-Conference.pdf)
  - [Textual Aesthetics in Large Language Models](https://aclanthology.org/2025.emnlp-main.696.pdf)
- **TriviaQA** (measurement instrument): *measured_by*, 1 paper
  > Results of LLaMA2-Chat-13B on the TriviaQA evaluation set are shown in Tab. 3... enhance the honesty score
  - [Alignment for Honesty](https://proceedings.neurips.cc/paper_files/paper/2024/file/7428e6db752171d6b832c53b2ed297ab-Paper-Conference.pdf)
- **Trustworthiness** (construct): *causes*, 1 paper
  > honesty—defined as consistently delivering accurate information and refraining from deceiving users—plays a crucial role in ensuring the trustworthy deployment of LLMs in real-world applications. (Section 1)
  - [HonestLLM: Toward an Honest and Helpful Large Language Model](https://proceedings.neurips.cc/paper_files/paper/2024/file/0d99a8c048befb6dd6e17d7684adacac-Paper-Conference.pdf)
- **LLM-as-a-judge** (measurement instrument): *measured_by*, 1 paper
  > “we conduct a one-shot ‘first-past-the-post’ (FPP)-style assessment with GPT-4o as the judge ... for quality ratings on a Likert scale between 1 to 5 ... including overall performance, honesty, helpfulness, truthfulness, and safety”
  - [DPL: Diverse Preference Learning Without A Reference Model](https://aclanthology.org/2025.naacl-long.190.pdf)
- **TruthfulQA** (measurement instrument): *measured_by*, 1 paper
  > For honesty, we utilize the TruthfulQA dataset (Lin et al., 2021) (Section 4.1).
  - [Too Helpful, Too Harmless, Too Honest or Just Right?](https://aclanthology.org/2025.emnlp-main.1510.pdf)

### → Honesty
- **Harmlessness** (construct): *correlates*, 1 paper
  > MiniGPT-v2 exhibits strong safety across several dimensions but underperforms on Truthfulness, suggesting a potential trade-off between honesty and harmlessness.
  - [MLLMGuard: A Multi-dimensional Safety Evaluation Suite for Multimodal Large Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/0d9dcd4ebef57f1839d871fe7d891e91-Paper-Datasets_and_Benchmarks_Track.pdf)

### Associated with
- **Human preference alignment** (construct), 2 papers
  > Additionally, we found SALMON capable to emphasize the distinct aspects of the alignment with respect to being Helpful, Honest, and Harmless) (HHH) (Askell et al., 2021) by customizing its preference principles.
  - [SALMON: Self-Alignment with Instructable Reward Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/dda5cac5272a9bcd4bc73d90bc725ef1-Paper-Conference.pdf)
  - [Icon2: Aligning Large Language Models Using Self-Synthetic Preference Data via Inherent Regulation](https://aclanthology.org/2025.emnlp-main.196.pdf)
- **Refusal** (behavioral indicator), 2 papers
  > In this paper, we argue for the importance of alignment for honesty, ensuring that LLMs proactively refuse to answer questions when they lack knowledge, while still not being overly conservative. (Abstract)
  - [Alignment for Honesty](https://proceedings.neurips.cc/paper_files/paper/2024/file/7428e6db752171d6b832c53b2ed297ab-Paper-Conference.pdf)
  - [Refine Knowledge of Large Language Models via Adaptive Contrastive Learning](https://proceedings.iclr.cc/paper_files/paper/2025/file/bbd010aed9a0d7f56144bd5dcaa95b9e-Paper-Conference.pdf)
- **Calibration** (construct), 1 paper
  > At its most basic level, the AI should provide accurate information, be well-calibrated, and express appropriate levels of uncertainty rather than misleading users. (Section 2)
  - [HonestLLM: Toward an Honest and Helpful Large Language Model](https://proceedings.neurips.cc/paper_files/paper/2024/file/0d99a8c048befb6dd6e17d7684adacac-Paper-Conference.pdf)
- **Abstention** (behavioral indicator), 1 paper
  > LMMs must be ... honest (e.g., abstention or the ability to say I don’t know...)
  - [Beyond task performance: evaluating and reducing the flaws of large multimodal models with in-context-learning](https://proceedings.iclr.cc/paper_files/paper/2024/file/5df817c5dd95293ebf6d1583303a8c73-Paper-Conference.pdf)
- **Truthfulness** (construct), 1 paper
  > According to Evans et al. (2021); Park et al. (2023), honesty entails a model stating what it believes, while an adjacent concept, truthfulness, demands it to state what is objectively true. (Section 5.1)
  - [Alignment for Honesty](https://proceedings.neurips.cc/paper_files/paper/2024/file/7428e6db752171d6b832c53b2ed297ab-Paper-Conference.pdf)
- **Hallucination** (behavioral indicator), 1 paper
  > we first refine and extend the definition of honesty in LLMs based on the definition proposed by Askell et al. [14], as the ability to recognize their limitations, remain objective without pandering, and thereby avoid spreading misinformation or inducing hallucinations. (Section 1)
  - [HonestLLM: Toward an Honest and Helpful Large Language Model](https://proceedings.neurips.cc/paper_files/paper/2024/file/0d99a8c048befb6dd6e17d7684adacac-Paper-Conference.pdf)
- **Self-awareness** (construct), 1 paper
  > Crucially, the AI should be honest about its capabilities and knowledge levels. This requires LLMs to have an awareness of their operational limits, a point highlighted by Huang et al. [19] which noted the general unawareness of LLMs to utilize external tools effectively. (Section 2)
  - [HonestLLM: Toward an Honest and Helpful Large Language Model](https://proceedings.neurips.cc/paper_files/paper/2024/file/0d99a8c048befb6dd6e17d7684adacac-Paper-Conference.pdf)
- **Sycophancy** (construct), 1 paper
  > Such behavior compromises the truthfulness of LLMs; therefore, reducing sycophancy is a critical measure for enhancing the honesty of LLMs [13]. (Section 2)
  - [HonestLLM: Toward an Honest and Helpful Large Language Model](https://proceedings.neurips.cc/paper_files/paper/2024/file/0d99a8c048befb6dd6e17d7684adacac-Paper-Conference.pdf)
- **World knowledge** (construct), 1 paper
  > Model A is more honest than model B IFF it exhibits statistically superior performance on measures of world knowledge (Section 5).
  - [Style Outweighs Substance: Failure Modes of LLM Judges in Alignment Benchmarking](https://proceedings.iclr.cc/paper_files/paper/2025/file/1eb36d07ebb13be16ddbda679a95018b-Paper-Conference.pdf)
- **Confidence expression** (behavioral indicator), 1 paper
  > the expression of uncertainty can serve as a valuable indicator of honesty, and we view calibration from the perspective of model knowledge as a finer-grained handling of knowns
  - [Alignment for Honesty](https://proceedings.neurips.cc/paper_files/paper/2024/file/7428e6db752171d6b832c53b2ed297ab-Paper-Conference.pdf)
