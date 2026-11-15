# SentEval
**Type:** Measurement instrument  
**Supporting papers:** 4  

## State of the Field

**What it is.** Most directly, papers describe SentEval as a standard transfer learning evaluation suite for sentence embeddings, with tasks such as sentiment classification (MR, SST-2), subjectivity detection (SUBJ), and question classification (TREC). One paper adds that it provides standard transfer learning tasks including MR, CR, SUBJ, MPQA, SST-2, TREC, and MRPC (Token Prepending: A Training-Free Approach for Eliciting Better Sentence Embeddings from LLMs). A separate paper uses SentEval as an evaluation tool for semantic textual similarity and says it contains seven STS subsets: STS 2012-2016, the STS-Benchmark, and SICK Relatedness.

**What it is claimed to measure.** Papers link SentEval to no constructs and no behavioral indicators. Instead, they report it as evaluating sentence embeddings through standard transfer learning tasks, and one paper relates it to STS tasks where model performance is measured with Spearman's correlation. No paper explicitly names a construct that SentEval measures.

**Space of uses.** The only linked measurement instrument is STS tasks. One paper relates SentEval to STS tasks by adopting it as the evaluation tool for seven STS subsets and measuring model performance with Spearman's correlation (Enhancing Unsupervised Sentence Embeddings via Knowledge-Driven Data Augmentation and Gaussian-Decayed Contrastive Learning). Another paper uses SentEval as the source of standard transfer learning tasks for sentence embeddings.

## Sources

**SentEval** (1 paper: [Token Prepending: A Training-Free Approach for Eliciting Better Sentence Embeddings from LLMs](https://aclanthology.org/2025.acl-long.159.pdf))
> Standard transfer learning evaluation suite for sentence embeddings, including tasks like sentiment classification (MR, SST-2), subjectivity detection (SUBJ), and question classification (TREC).

## Relationships

### Associated with
- **STS tasks** (measurement instrument), 1 paper
  > To validate our method for sentence embeddings, we evaluated the model’s performance on semantic textual similarity (STS) tasks, we use the standard evaluation method, measuring model performance with Spearman’s correlation, and we adopt SentEval (Conneau and Kiela, 2018) as the evaluation tool, which contains seven STS subsets: STS 2012-2016, the STS-Benchmark and the SICK Relatedness. (Section 4.1)
  - [Enhancing Unsupervised Sentence Embeddings via Knowledge-Driven Data Augmentation and Gaussian-Decayed Contrastive Learning](https://aclanthology.org/2025.acl-long.244.pdf)
