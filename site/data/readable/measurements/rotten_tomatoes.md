# Rotten Tomatoes
**Type:** Measurement instrument  
**Supporting papers:** 13  
**Also known as:** MR, Movie Review  

## State of the Field

**What it is.** Across the surveyed papers, the prevailing usage treats Rotten Tomatoes as a sentiment classification dataset or benchmark built from movie reviews, typically for binary polarity labeling. Some authors refer to it as MR or Movie Review, and one description specifies movie reviews from the Rotten Tomatoes website, while others describe it more generally as a text classification dataset or benchmark used in projected-embedding, in-context learning, and prompt-based evaluations.

**What it is claimed to measure.** Papers use it to measure 2 behavioral indicators, Text classification and Sentiment analysis, and no constructs are linked to it. The linked claims stay within classification behavior: papers describe it as one of the datasets that 'all admit classification tasks' and as a benchmark for binary polarity tasks on movie reviews.

**Space of uses.** Papers most commonly use it as one dataset within a larger evaluation suite rather than in isolation. In the excerpts, it appears alongside SST-2, IMDB, AG News, Subj, and TREC, and it is used to evaluate projected embeddings, in-context learning and activation-vector methods, few-shot classification, polarity labeling, and non-reusable obfuscation for movie-review sentiment analysis. No measurement instrument is explicitly linked to it.

## Sources

**Rotten Tomatoes** (3 papers: [Vector-ICL: In-context Learning with Continuous Vector Representations](https://proceedings.iclr.cc/paper_files/paper/2025/file/46516c4204d6cab8299e55d4ebf7ccec-Paper-Conference.pdf), [LLaMAs Have Feelings Too: Unveiling Sentiment and Emotion Representations in LLaMA Models Through Probing](https://aclanthology.org/2025.acl-long.306.pdf), [Iterative Vectors: In-Context Gradient Steering without Backpropagation](https://raw.githubusercontent.com/mlresearch/v267/main/assets/liu25j/liu25j.pdf))
> A sentiment classification dataset used to evaluate text classification with projected embeddings.

**MR** (3 papers: [Connecting Large Language Models with Evolutionary Algorithms Yields Powerful Prompt Optimizers](https://proceedings.iclr.cc/paper_files/paper/2024/file/9156b0f6dfa9bbd18c79cc459ef5d61c-Paper-Conference.pdf), [Gen-Z: Generative Zero-Shot Text Classification with Contextualized Label Descriptions](https://proceedings.iclr.cc/paper_files/paper/2024/file/af7cc9e2366b8f8837a6ef339810277a-Paper-Conference.pdf), [Pareto Prompt Optimization](https://proceedings.iclr.cc/paper_files/paper/2025/file/13b45b44e26c353c64cba9529bf4724f-Paper-Conference.pdf))
> Movie Review sentiment classification benchmark used to evaluate polarity labeling.

**Movie Review** (1 paper: [EmojiPrompt: Generative Prompt Obfuscation for Privacy-Preserving Communication with Cloud-based LLMs](https://aclanthology.org/2025.naacl-long.614.pdf))
> A dataset used to evaluate non-reusable obfuscation for sentiment analysis of movie reviews.

## Relationships

### → Rotten Tomatoes
- **Text classification** (behavioral indicator): *measured_by*, 3 papers
  > We primarily evaluate our method on AG News (4 classes) [77], SST-2 (2 classes) [57], Rotten Tomatoes (2 classes) [50], and Subj (2 classes) [18] datasets which all admit classification tasks. (Section 5.2)
  - [DETAIL: Task DEmonsTration Attribution for Interpretable In-context Learning](https://proceedings.neurips.cc/paper_files/paper/2024/file/2ceda49041816da6d5a34eb3b612607f-Paper-Conference.pdf)
  - [Adaptive Transformer Programs: Bridging the Gap Between Performance and Interpretability in Transformers](https://proceedings.iclr.cc/paper_files/paper/2025/file/9d5609613524ecf4f15af0f7b31abca4-Paper-Conference.pdf)
  - [Vector-ICL: In-context Learning with Continuous Vector Representations](https://proceedings.iclr.cc/paper_files/paper/2025/file/46516c4204d6cab8299e55d4ebf7ccec-Paper-Conference.pdf)
- **Sentiment analysis** (behavioral indicator): *measured_by*, 2 papers
  > Our experiments utilize three benchmark datasets for sentiment classification: IMDB (Maas et al., 2011), SST-2 (Socher et al., 2013), and Rotten Tomatoes (Pang and Lee, 2005), all of which contain movie reviews for binary polarity tasks (e.g., positive or negative sentiment). (Section 3)
  - [LLaMAs Have Feelings Too: Unveiling Sentiment and Emotion Representations in LLaMA Models Through Probing](https://aclanthology.org/2025.acl-long.306.pdf)
  - [Disentangled Information Bottleneck for Adversarial Text Defense](https://aclanthology.org/2025.emnlp-main.1183.pdf)
