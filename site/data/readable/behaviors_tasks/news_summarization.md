# News summarization
**Type:** Behavioral indicator  
**Supporting papers:** 4  

## State of the Field

**Space of definitions.** Across the definitions, the prevailing usage treats news summarization as generating a concise or shorter version of a news article. Papers agree that the summary should preserve the article's main ideas and information, and some operationalizations make the input format explicit by requiring both a prompt and the original article. A more specific prompting example asks the model to summarize the news in two sentences.

**Variants.** Variants are limited and mostly concern evaluation setting rather than a different task name. Papers study it in zero-shot generative evaluation, as the English summarization subset of XLSum, and as one of the RAG task types in RAGTruth. A narrower formulation asks for two-sentence summaries.

**Space of elicitation and scores.** News summarization is measured by three linked instruments, all used as data resources: CNN/DailyMail, RAGTruth, and the English summarization subset of XLSum. In the linked papers, CNN/DailyMail is used for zero-shot generative evaluation, RAGTruth includes news summarization as one of three RAG task types, and XLSum is used through its English summarization subset.

**What it is taken as evidence of.** The only linked construct is Model collapse, and the relationship is recorded as related. One paper describes news summarization with LLMs as a practical task that can exhibit model collapse when trained on generated data. No other construct link is recorded in the linked papers.

## Sources

**News summarization** (2 papers: [Progressive Mixed-Precision Decoding for Efficient LLM Inference](https://proceedings.iclr.cc/paper_files/paper/2025/file/5df4313ecd4875931fbdacc486cc1fcf-Paper-Conference.pdf), [Evaluating Small Language Models for News Summarization: Implications and Factors Influencing Performance](https://aclanthology.org/2025.naacl-long.253.pdf))
> The task of generating a concise summary of a news article.

## Relationships

### News summarization →
- **RAGTruth** (measurement instrument): *measured_by*, 1 paper
  > The data includes three RAG task types: Question Answering (QA), Data-to-Text Writing, and News Summarization.
  - [ReDeEP: Detecting Hallucination in Retrieval-Augmented Generation via Mechanistic Interpretability](https://proceedings.iclr.cc/paper_files/paper/2025/file/7daf60e805e596c3bd1e843e72ea5560-Paper-Conference.pdf)
- **XLSum** (measurement instrument): *measured_by*, 1 paper
  > We utilize the English summarization subset of the XLSUM dataset (Hasan et al., 2021)
  - [Beyond Model Collapse: Scaling Up with Synthesized Data Requires Verification](https://proceedings.iclr.cc/paper_files/paper/2025/file/df2d62b96a4003203450cf89cd338bb7-Paper-Conference.pdf)
- **CNN/DailyMail** (measurement instrument): *measured_by*, 1 paper
  > We conducted experiments on edge-deployable models... evaluating their zero-shot generative performance on news summarization... using the CNN/DM... dataset (Section 5)
  - [Progressive Mixed-Precision Decoding for Efficient LLM Inference](https://proceedings.iclr.cc/paper_files/paper/2025/file/5df4313ecd4875931fbdacc486cc1fcf-Paper-Conference.pdf)

### Associated with
- **Model collapse** (construct), 1 paper
  > We experiment with practical tasks – computing matrix eigenvalues with transformers and news summarization with LLMs – which both exhibit model collapse when trained on generated data
  - [Beyond Model Collapse: Scaling Up with Synthesized Data Requires Verification](https://proceedings.iclr.cc/paper_files/paper/2025/file/df2d62b96a4003203450cf89cd338bb7-Paper-Conference.pdf)
