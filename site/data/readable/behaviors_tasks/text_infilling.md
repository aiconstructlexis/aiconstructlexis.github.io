# Text infilling
**Type:** Behavioral indicator  
**Supporting papers:** 15  
**Also known as:** Sequence infilling, Story infilling, Masked token infilling, Cloze completion, Fill-in-the-blank completion, Text insertion, Infilling  

## State of the Field

**Space of definitions.** Across papers, the prevailing usage is generating missing text from surrounding context, usually a prefix and suffix, with the output expected to fit coherently between them. Several definitions describe filling masked spans, fragments, or the middle of a document or sequence, and some make this concrete as infilling middle tokens from given initial and final tokens or generating the middle of a story from its beginning and end. A smaller line of work narrows the task to masked-token or cloze prediction, including single scientific terms or entity names, and some fill-in-the-blank setups allow either generating or selecting the missing completion.

**Variants.** Papers use several narrower names and settings for this behavior, most often story infilling, masked token infilling, cloze completion, fill-in-the-blank completion, and text insertion. The settings range from short stories with masked fragments, to Arabic [MASK] fillings used to compare Arab and Western entity preferences, to climate-science blanks requiring a single scientific word, localized medical prompts with traditional versus allopathic candidates, knowledge probes with a blanked fact, and profile-based blanks targeting details such as residence, employment, and hobbies. A smaller diffusion-oriented line also studies non-sequential or flexible-length infilling, where span lengths and positions vary and the model may not be given oracle positions.

**Space of elicitation and scores.** Papers link text infilling to 2 measurement instruments, ROCStories and WikiText-103. ROCStories is a story corpus used for sentence-level infilling, described as generating the fourth sentence from the first three sentences and the last sentence, while WikiText-103 is used for prompt-mask evaluation of infilling performance, with MAUVE reported on validation sequences. Other papers elicit the behavior through masked fragments, candidate completions, or single-blank prompts, but those are presented as task formats rather than additional named instruments.

**What it is taken as evidence of.** Only 1 construct is linked to text infilling, knowledge memorization, and that link is reported as related rather than as a direct measurement claim. The paper connects the behavior to memorization by using fill-in-the-blank probes to examine memory of original training data related to unlearning targets. No additional construct links are recorded; separately, another paper relates text infilling to cultural text adaptation through Arab versus Western entity fillings.

## Sources

**Story infilling** (2 papers: [Scaling Diffusion Language Models via Adaptation from Autoregressive Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/0fa81c3f0d57f95b8776de3a248ef0ed-Paper-Conference.pdf), [Amortizing intractable inference in large language models](https://proceedings.iclr.cc/paper_files/paper/2024/file/bc667ac84ef58f2b5022da97a465cbab-Paper-Conference.pdf))
> The specific infilling task of generating a coherent narrative segment to complete a story.

**Text infilling** (5 papers: [Glauber Generative Model: Discrete Diffusion Models via Binary Classification](https://proceedings.iclr.cc/paper_files/paper/2025/file/125be378b39b10676f56e12e6923b902-Paper-Conference.pdf), [On The Origin of Cultural Biases in Language Models: From Pre-training Data to Linguistic Phenomena](https://aclanthology.org/2025.naacl-long.326.pdf), [CultureInstruct: Curating Multi-Cultural Instructions at Scale](https://aclanthology.org/2025.naacl-long.465.pdf), [Flexible-length Text Infilling for Discrete Diffusion Models](https://aclanthology.org/2025.emnlp-main.1597.pdf), [Adaptable Logical Control for Large Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/d15c16cf5619a2b1606da5fc88e3f1a9-Paper-Conference.pdf))
> The task of generating text to fill in a missing portion of a document given the surrounding context (prefix and suffix).

**Sequence infilling** (1 paper: [Efficient Perplexity Bound and Ratio Matching in Discrete Diffusion Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/23e6f78bdec844a9f7b6c957de2aae91-Paper-Conference.pdf))
> Filling in missing parts of a sequence non-sequentially during discrete diffusion generation.

**Masked token infilling** (1 paper: [Hidden No More: Attacking and Defending Private Third-Party LLM Inference](https://raw.githubusercontent.com/mlresearch/v267/main/assets/thomas25b/thomas25b.pdf))
> The task of predicting missing tokens in a sequence given the surrounding context, used as a proxy to evaluate the difficulty of reconstructing a full prompt from a partial one.

**Cloze completion** (1 paper: [ClimaQA: An Automated Evaluation Framework for Climate Question Answering Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/3eff068e195daace49955348de9f8398-Paper-Conference.pdf))
> Filling in a missing scientific term in a sentence or phrase using the surrounding context.

**Fill-in-the-blank completion** (3 papers: [Africa Health Check: Probing Cultural Bias in Medical LLMs](https://aclanthology.org/2025.emnlp-main.1639.pdf), [RWKU: Benchmarking Real-World Knowledge Unlearning for Large Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/b1f78dfc9ca0156498241012aec4efa0-Paper-Datasets_and_Benchmarks_Track.pdf), [Protecting Privacy in Multimodal Large Language Models with MLLMU-Bench](https://aclanthology.org/2025.naacl-long.207.pdf))
> Generating or selecting a treatment completion for a medical scenario when presented with a prompt and two candidate responses—one traditional and one allopathic.

**Text insertion** (1 paper: [Adaptable Logical Control for Large Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/d15c16cf5619a2b1606da5fc88e3f1a9-Paper-Conference.pdf))
> The task of generating text to fill a gap between a given prefix and suffix, ensuring coherence with both contexts.

**Infilling** (1 paper: [Amortizing intractable inference in large language models](https://proceedings.iclr.cc/paper_files/paper/2024/file/bc667ac84ef58f2b5022da97a465cbab-Paper-Conference.pdf))
> The task of generating a sequence of tokens that fits coherently between a given prefix and suffix context.

## Relationships

### Text infilling →
- **ROCStories** (measurement instrument): *measured_by*, 1 paper
  > “We use the ROCStories corpus ... Given the first 3 sentences and the last sentence, the goal is to generate the fourth sentence”
  - [Amortizing intractable inference in large language models](https://proceedings.iclr.cc/paper_files/paper/2024/file/bc667ac84ef58f2b5022da97a465cbab-Paper-Conference.pdf)
- **WikiText-103** (measurement instrument): *measured_by*, 1 paper
  > Evaluation of text infilling performance using the MAUVE score (↑) with 5 prompt masks... For all methods, we use the same set of 2,000 text sequences from the validation set of WikiText-103
  - [Discrete Copula Diffusion](https://proceedings.iclr.cc/paper_files/paper/2025/file/dd1fef536655685898a6602bfbf16857-Paper-Conference.pdf)

### Associated with
- **Knowledge memorization** (construct), 1 paper
  > We use fill-in-the-blank style probes (FB) to examine the memory of the original training data related to the unlearning targets. (Section 3.3.1)
  - [RWKU: Benchmarking Real-World Knowledge Unlearning for Large Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/b1f78dfc9ca0156498241012aec4efa0-Paper-Datasets_and_Benchmarks_Track.pdf)
- **Cultural text adaptation** (behavioral indicator), 1 paper
  > We compare the ability of LMs at adapting to cultural contexts in Arabic and English by analyzing their preference for Arab vs. Western entities as [MASK] token fillings of CAMeL-2 contexts. (Section 3.2)
  - [On The Origin of Cultural Biases in Language Models: From Pre-training Data to Linguistic Phenomena](https://aclanthology.org/2025.naacl-long.326.pdf)
