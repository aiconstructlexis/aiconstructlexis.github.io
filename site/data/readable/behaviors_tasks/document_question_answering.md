# Document question answering
**Type:** Behavioral indicator  
**Supporting papers:** 48  
**Also known as:** Contextual question answering, Document-based question answering, Long-context question answering, Open-book question answering, Webpage question answering, Flexible length question answering, Long-book question answering, Long-document question answering, Context-based question answering, Privacy question answering, Privacy policy question answering, File reading, Long document understanding  

## State of the Field

**Space of definitions.** Across papers, the prevailing usage treats this behavior as answering a question from information supplied in a provided context or document, often a long one. A recurring formulation explicitly asks models to rely on the context rather than pretrained or parametric knowledge, sometimes even to give "the exact answer, using only the information provided in the context." Papers differ on the expected answer format: most ask for an answer based on the document or context, while some require concise and relevant answers to user queries, exact answers, or multi-statement answers whose claims are supported by sentence-level citations.

**Variants.** Most papers use nearby labels such as document question answering, long-context question answering, contextual question answering, long-document question answering, and open-book question answering. Within those variants, papers study single-document and multi-document settings, book-length or other lengthy contexts, multimodal documents with text, charts, and images, and tasks that require locating, aggregating, or filtering information from long inputs. Smaller lines of work narrow the setting to webpage content, privacy policies, file reading, or flexible-length True/False questions answerable from two key sentences; in SelfCite, answers are multi-statement and each statement cites supporting sentences in the context.

**Space of elicitation and scores.** Papers link this behavior to 13 measurement instruments, mostly benchmarks and datasets for long-context, long-document, document-grounded, or multimodal question answering. The most frequently named are InfiniteBench, NarrativeQA, LongBench, DocBench, and DocVQA, while other papers also use additional open-book, context-QA, and long-context evaluation suites.

**What it is taken as evidence of.** Papers make few explicit construct claims about what this behavior indicates. It is linked to one construct, Complex reasoning, and that claim is framed as a related link rather than a causal or correlational one: one paper reports improved question answering while describing a capability to perform complex reasoning about extended context. No other construct is linked by papers.

## Sources

**Document question answering** (5 papers: [Multimodal Task Vectors Enable Many-Shot Multimodal In-Context Learning](https://proceedings.neurips.cc/paper_files/paper/2024/file/27571b74d6cd650b8eb6cf1837953ae8-Paper-Conference.pdf), [From Isolated Conversations to Hierarchical Schemas: Dynamic Tree Memory Representation for LLMs](https://proceedings.iclr.cc/paper_files/paper/2025/file/0382cb76309820f71c6eacd47b36ce71-Paper-Conference.pdf), [Squeezed Attention: Accelerating Long Context Length LLM Inference](https://aclanthology.org/2025.acl-long.1568.pdf), [SmartBench: Is Your LLM Truly a Good Chinese Smartphone Assistant?](https://aclanthology.org/2025.emnlp-main.194.pdf), [Privacy-Preserving In-Context Learning for Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/572cd21bd5dea96b065476b77d21b3c6-Paper-Conference.pdf))
> The task of answering questions based on the content of multimodal documents that may contain text, charts, and images.

**Long-context question answering** (5 papers: [RazorAttention: Efficient KV Cache Compression Through Retrieval Heads](https://proceedings.iclr.cc/paper_files/paper/2025/file/2a98af4fea6a24b73af7b588ca95f755-Paper-Conference.pdf), [SelfCite: Self-Supervised Alignment for Context Attribution in Large Language Models](https://raw.githubusercontent.com/mlresearch/v267/main/assets/chuang25a/chuang25a.pdf), [LongReward: Improving Long-context Large Language Models with AI Feedback](https://aclanthology.org/2025.acl-long.187.pdf), [Self-Taught Agentic Long Context Understanding](https://aclanthology.org/2025.acl-long.275.pdf), [Functional Interpolation for Relative Positions improves Long Context Transformers](https://proceedings.iclr.cc/paper_files/paper/2024/file/2f55a8b7b1c2c6312eb86557bb9a2bd5-Paper-Conference.pdf))
> The observable action of generating answers to questions based on information contained within a lengthy input context.

**Open-book question answering** (2 papers: [AttriBoT: A Bag of Tricks for Efficiently Approximating Leave-One-Out Context Attribution](https://proceedings.iclr.cc/paper_files/paper/2025/file/2aab664e0d1656e8b56c74f868e1ea69-Paper-Conference.pdf), [The Cost of Scaling Down Large Language Models: Reducing Model Size Affects Memory before In-context Learning](https://proceedings.iclr.cc/paper_files/paper/2024/file/bb68f698772f14b6d8eaef4529fb9176-Paper-Conference.pdf))
> The task of answering a question using information provided in a given context, where the model is not expected to rely solely on its pre-trained knowledge.

**Webpage question answering** (1 paper: [Harnessing Webpage UIs for Text-Rich Visual Understanding](https://proceedings.iclr.cc/paper_files/paper/2025/file/2da53cd1abdae59150e35f4693834f32-Paper-Conference.pdf))
> Answering questions about non-image content in webpages using page structure and textual information.

**Document-based question answering** (2 papers: [Generative Adapter: Contextualizing Language Models in Parameters with A Single Forward Pass](https://proceedings.iclr.cc/paper_files/paper/2025/file/447708674d7f30492ca5338b36b07d0c-Paper-Conference.pdf), [Exploring the Impact of Instruction-Tuning on LLM's Susceptibility to Misinformation](https://aclanthology.org/2025.acl-long.1295.pdf))
> Answering questions using information contained in provided documents or passages, especially under varying context lengths.

**Contextual question answering** (4 papers: [FaithEval: Can Your Language Model Stay Faithful to Context, Even If "The Moon is Made of Marshmallows"](https://proceedings.iclr.cc/paper_files/paper/2025/file/48404cd9ce03946c6b7177691f3267a1-Paper-Conference.pdf), [T2: An Adaptive Test-Time Scaling Strategy for Contextual Question Answering](https://aclanthology.org/2025.emnlp-main.185.pdf), [SAM Decoding: Speculative Decoding via Suffix Automaton](https://aclanthology.org/2025.acl-long.595.pdf), [SelfElicit: Your Language Model Secretly Knows Where is the Relevant Evidence](https://aclanthology.org/2025.acl-long.448.pdf))
> The task of generating an answer to a question based solely on the information provided in a given context passage.

**Long-book question answering** (1 paper: [LongPO: Long Context Self-Evolution of Large Language Models through Short-to-Long Preference Optimization](https://proceedings.iclr.cc/paper_files/paper/2025/file/1332893b662f655660c9abdf793230cf-Paper-Conference.pdf))
> The observable task of answering questions based on information contained within an extensive, book-length text.

**Flexible length question answering** (1 paper: [From Artificial Needles to Real Haystacks: Improving Retrieval Capabilities in LLMs by Finetuning on Synthetic Data](https://proceedings.iclr.cc/paper_files/paper/2025/file/15a321fbfc19fce9b325ec6e77dfb597-Paper-Conference.pdf))
> The task of answering a True/False question that requires reasoning over two key sentences within a context of varying length.

**Long-document question answering** (4 papers: [SCBench: A KV Cache-Centric Analysis of Long-Context Methods](https://proceedings.iclr.cc/paper_files/paper/2025/file/a540b17fb2295c736d5afd6c507acf66-Paper-Conference.pdf), [Stronger Baselines for Retrieval-Augmented Generation with Long-Context Language Models](https://aclanthology.org/2025.emnlp-main.1656.pdf), [NExtLong: Toward Effective Long-Context Training without Long Documents](https://raw.githubusercontent.com/mlresearch/v267/main/assets/gao25n/gao25n.pdf), [Hierarchical Context Merging: Better Long Context Understanding for Pre-trained LLMs](https://proceedings.iclr.cc/paper_files/paper/2024/file/06694da057cb15fef11542270a592627-Paper-Conference.pdf))
> The observable task of answering questions by locating, aggregating, or filtering information from a long document provided in the context.

**Context-based question answering** (2 papers: [Context-Parametric Inversion: Why Instruction Finetuning May Not Actually Improve Context Reliance](https://proceedings.iclr.cc/paper_files/paper/2025/file/aa27ac7aca4e462da1439b43ceebc04c-Paper-Conference.pdf), [Unnatural Languages Are Not Bugs but Features for LLMs](https://raw.githubusercontent.com/mlresearch/v267/main/assets/duan25c/duan25c.pdf))
> Answering questions by using information supplied in the input context, especially when that context conflicts with pretrained knowledge.

**Privacy question answering** (1 paper: [Empowering Users in Digital Privacy Management through Interactive LLM-Based Agents](https://proceedings.iclr.cc/paper_files/paper/2025/file/bef8e5620c699630405adafaa86cb038-Paper-Conference.pdf))
> The observable task of providing accurate answers to specific user questions based on the content of a given privacy policy.

**Privacy policy question answering** (1 paper: [A Multi-Agent Framework for Mitigating Dialect Biases in Privacy Policy Question-Answering Systems](https://aclanthology.org/2025.acl-long.1554.pdf))
> The observable task of generating a concise and relevant answer to a user's query based on the text of a given privacy policy document.

**File reading** (1 paper: [Multi-agent Architecture Search via Agentic Supernet](https://raw.githubusercontent.com/mlresearch/v267/main/assets/zhang25bi/zhang25bi.pdf))
> Reading and extracting information from files or documents to answer a query.

**Long document understanding** (1 paper: [LV-XAttn: Distributed Cross-Attention for Long Visual Inputs in Multimodal Large Language Models](https://raw.githubusercontent.com/mlresearch/v267/main/assets/chang25c/chang25c.pdf))
> The task of processing and comprehending lengthy text documents to extract information or answer questions.

## Relationships

### Document question answering →
- **InfiniteBench** (measurement instrument): *measured_by*, 4 papers
  > En.QA is annotated by a pipeline that ensures the questions’ necessitating of long-range dependencies and reasoning, beyond simple short passage retrieval. (Section 4.1)
  - [ChatQA 2: Bridging the Gap to Proprietary LLMs in Long Context and RAG Capabilities](https://proceedings.iclr.cc/paper_files/paper/2025/file/a7b562dac391e9c7af691e8ef886ad10-Paper-Conference.pdf)
  - [LongPO: Long Context Self-Evolution of Large Language Models through Short-to-Long Preference Optimization](https://proceedings.iclr.cc/paper_files/paper/2025/file/1332893b662f655660c9abdf793230cf-Paper-Conference.pdf)
  - [Why Does the Effective Context Length of LLMs Fall Short?](https://proceedings.iclr.cc/paper_files/paper/2025/file/884baf65392170763b27c914087bde01-Paper-Conference.pdf)
  - [Stronger Baselines for Retrieval-Augmented Generation with Long-Context Language Models](https://aclanthology.org/2025.emnlp-main.1656.pdf)
- **NarrativeQA** (measurement instrument): *measured_by*, 4 papers
  > We use NarrativeQA (Koˇcisk´y et al., 2018) ... for evaluating long-document QA.
  - [HELMET: How to Evaluate Long-context Models Effectively and Thoroughly](https://proceedings.iclr.cc/paper_files/paper/2025/file/f5332c8273d02729730a9c24dec2135e-Paper-Conference.pdf)
  - [Self-Taught Agentic Long Context Understanding](https://aclanthology.org/2025.acl-long.275.pdf)
  - [Compute or Load KV Cache? Why Not Both?](https://raw.githubusercontent.com/mlresearch/v267/main/assets/jin25d/jin25d.pdf)
  - [Stronger Baselines for Retrieval-Augmented Generation with Long-Context Language Models](https://aclanthology.org/2025.emnlp-main.1656.pdf)
- **LongBench** (measurement instrument): *measured_by*, 2 papers
  > In this section, we comprehensively evaluate how structurization boosts QA ability on seven datasets from the LongBench benchmark [3] with a variety of LLMs to examine. (Section 4.1)
  - [Enhancing LLM’s Cognition via Structurization](https://proceedings.neurips.cc/paper_files/paper/2024/file/f169ec4d47933ea4896b994af8ff4f17-Paper-Conference.pdf)
  - [TurboRAG: Accelerating Retrieval-Augmented Generation with Precomputed KV Caches for Chunked Text](https://aclanthology.org/2025.emnlp-main.334.pdf)
- **RULER** (measurement instrument): *measured_by*, 1 paper
  > "The RULER benchmark (Hsieh et al., 2024) encompasses a variety of synthetic tasks, including eight variants of Needle-in-a-Haystack (NIAH), as well as tasks involving variable tracking, counting, and long-context question answering (QA)."
  - [Why Does the Effective Context Length of LLMs Fall Short?](https://proceedings.iclr.cc/paper_files/paper/2025/file/884baf65392170763b27c914087bde01-Paper-Conference.pdf)
- **DocVQA** (measurement instrument): *measured_by*, 1 paper
  > Then, we consider the document questions answering task... We adopt a dataset that originates from a Privacy Preserving Federated Learning Document VQA (PFL-DocVQA) competition (Tito et al., 2023). (Section 4.2)
  - [Privacy-Preserving In-Context Learning for Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/572cd21bd5dea96b065476b77d21b3c6-Paper-Conference.pdf)
- **SQuAD 2.0** (measurement instrument): *measured_by*, 1 paper
  > “To this end, we focus on three open-book QA datasets: 1. SQuAD 2.0 (Rajpurkar et al., 2018): A reading comprehension benchmark where a model is presented a question along with a Wikipedia article containing the answer.”
  - [AttriBoT: A Bag of Tricks for Efficiently Approximating Leave-One-Out Context Attribution](https://proceedings.iclr.cc/paper_files/paper/2025/file/2aab664e0d1656e8b56c74f868e1ea69-Paper-Conference.pdf)
- **HotpotQA** (measurement instrument): *measured_by*, 1 paper
  > “To this end, we focus on three open-book QA datasets: 2. HotpotQA (Yang et al., 2018): A multi-hop question answering benchmark that requires reason-ing across paragraphs from multiple Wikipedia pages”
  - [AttriBoT: A Bag of Tricks for Efficiently Approximating Leave-One-Out Context Attribution](https://proceedings.iclr.cc/paper_files/paper/2025/file/2aab664e0d1656e8b56c74f868e1ea69-Paper-Conference.pdf)
- **Qasper** (measurement instrument): *measured_by*, 1 paper
  > “To this end, we focus on three open-book QA datasets: 3. QASPER (Dasigi et al., 2021): A document-grounded, information-seeking question answering dataset”
  - [AttriBoT: A Bag of Tricks for Efficiently Approximating Leave-One-Out Context Attribution](https://proceedings.iclr.cc/paper_files/paper/2025/file/2aab664e0d1656e8b56c74f868e1ea69-Paper-Conference.pdf)
- **LongBench v2** (measurement instrument): *measured_by*, 1 paper
  > “We utilize LongBench v2 (Bai et al., 2024), a benchmark designed for challenging long-context question-answering”
  - [Graph World Model](https://raw.githubusercontent.com/mlresearch/v267/main/assets/feng25p/feng25p.pdf)
- **HELMET** (measurement instrument): *measured_by*, 1 paper
  > The evaluation spans five task types from the HELMET benchmark: synthetic recall, retrieval-augmented generation (RAG), many-shot in-context learning (ICL), passage re-ranking, and long-document QA, covering a total of 17 sub-tasks. (Section 4.1. Evaluation)
  - [NExtLong: Toward Effective Long-Context Training without Long Documents](https://raw.githubusercontent.com/mlresearch/v267/main/assets/gao25n/gao25n.pdf)
- **TriviaQA** (measurement instrument): *measured_by*, 1 paper
  > We evaluate Cake across various context lengths using three datasets with different task types: LongChat (Li et al., 2023) for multi-turn conversations, and TriviaQA and NarrativeQA (Bai et al., 2023) for long-document question-answering tasks.
  - [Compute or Load KV Cache? Why Not Both?](https://raw.githubusercontent.com/mlresearch/v267/main/assets/jin25d/jin25d.pdf)
- **DocBench** (measurement instrument): *measured_by*, 1 paper
  > We conduct experiments on two multi-modal long-context document understanding and question-answering benchmarks, including MMLongBench-Doc (Ma et al., 2024) and DocBench (Zou et al., 2025). (Section 4.1)
  - [DocAgent: An Agentic Framework for Multi-Modal Long-Context Document Understanding](https://aclanthology.org/2025.emnlp-main.893.pdf)
- **HAGRID** (measurement instrument): *measured_by*, 1 paper
  > ...and make Hagrid (Kamalloo et al., 2023) dataset for context QA task (Section 4.1.2).
  - [Faster In-Context Learning for LLMs via N-Gram Trie Speculative Decoding](https://aclanthology.org/2025.emnlp-main.911.pdf)

### Associated with
- **Complex reasoning** (construct), 1 paper
  > HOMER also improves the prediction accuracy on question answering by 3% (32.7% →35.7%), presenting its capability to perform complex reasoning about the content in the extended context length.
  - [Hierarchical Context Merging: Better Long Context Understanding for Pre-trained LLMs](https://proceedings.iclr.cc/paper_files/paper/2024/file/06694da057cb15fef11542270a592627-Paper-Conference.pdf)
