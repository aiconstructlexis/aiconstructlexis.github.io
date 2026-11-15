# Dialogue summarization
**Type:** Behavioral indicator  
**Supporting papers:** 13  
**Also known as:** Dialog summary, Conversational summarization, Dialog summarization  

## State of the Field

**Space of definitions.** Across the surveyed work, dialogue summarization is most commonly framed as producing a concise summary from a conversation or multi-turn dialogue. Definitions repeatedly emphasize concision, while one definition also requires accuracy and another says the summary should capture the conversation's salient semantics and key information, specifying the output as a sequence of summary sentences. A smaller line of work uses the summary more narrowly, prompting a summary of dialogue context that highlights information indicative of errors in the last agent utterance. As one paper puts it, the objective is to generate a summary that "succinctly captures the salient semantics and key information conveyed throughout the conversation" (PoSum-Bench: Benchmarking Position Bias in LLM-based Conversational Summarization).

**Variants.** Papers use several near-synonymous task names, including dialogue summarization, dialog summarization, dialog summary, and conversational summarization. The studied settings range from general dialogue transcripts to clinical interactions, especially pre-consultation and patient-doctor conversations that culminate in a brief medical report; another paper instead prompts a summary of dialogue context for conversational AI error discovery. SAMSum summarization is a recurring named setting, and one benchmark places the task in zero-shot abstractive summarization of complex inputs such as dialogues and meetings.

**Space of elicitation and scores.** Papers link this behavior to 5 measurement instruments. DialogSum is the most frequently linked instrument; other linked instruments are Human evaluation, PoSum-Bench, QMSum, and SAMSum. These are mostly datasets or benchmarks for dialogue summarization, while one paper also evaluates generated summaries with human evaluation via CrowdWorks.

**What it is taken as evidence of.** Papers do not link dialogue summarization to any construct, so the linked relations do not specify what construct it is evidence of. The only other linked behavior is Hallucination: one paper reports dialogue summarization is related to hallucination, describing dialogue summaries that "fabricate features not present in the source content."

## Sources

**Dialogue summarization** (4 papers: [MedJourney: Benchmark and Evaluation of Large Language Models over Patient Clinical Journey](https://proceedings.neurips.cc/paper_files/paper/2024/file/9f80af32390984cb709cdeb014d0df41-Paper-Datasets_and_Benchmarks_Track.pdf), [STAFF: Speculative Coreset Selection for Task-Specific Fine-tuning](https://proceedings.iclr.cc/paper_files/paper/2025/file/412360d2dd428c26f34918c8d682cf7e-Paper-Conference.pdf), [Towards Automated Error Discovery: A Study in Conversational AI](https://aclanthology.org/2025.emnlp-main.1.pdf), [The Hedgehog & the Porcupine: Expressive Linear Attentions with Softmax Mimicry](https://proceedings.iclr.cc/paper_files/paper/2024/file/ebba182cb97864368fdb6ae00773a5e4-Paper-Conference.pdf))
> The task of creating a concise summary from a multi-turn conversation, such as a pre-consultation dialogue or a patient-doctor interaction.

**Dialog summary** (1 paper: [BackdoorAlign: Mitigating Fine-tuning based Jailbreak Attack with Backdoor Enhanced Safety Alignment](https://proceedings.neurips.cc/paper_files/paper/2024/file/094324f386c836c75d4a26f3499d2ede-Paper-Conference.pdf))
> The task of generating a concise and accurate summary from a given conversation or dialogue.

**Conversational summarization** (1 paper: [PoSum-Bench: Benchmarking Position Bias in LLM-based Conversational Summarization](https://aclanthology.org/2025.emnlp-main.404.pdf))
> Generating a concise summary of a multi-turn dialogue that captures key information from the interaction, observable as a sequence of summary sentences produced from a conversation input.

**Dialog summarization** (1 paper: [Privacy-Preserving In-Context Learning for Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/572cd21bd5dea96b065476b77d21b3c6-Paper-Conference.pdf))
> The task of generating a concise summary of a given conversation or dialog.

## Relationships

### Dialogue summarization →
- **DialogSum** (measurement instrument): *measured_by*, 5 papers
  > DialogSum is a large-scale dialogue summarization dataset, consisting of 13,460 dialogues with corresponding manually labeled summaries and topics. (Appendix B.1)
  - [Aligner: Efficient Alignment by Learning to Correct](https://proceedings.neurips.cc/paper_files/paper/2024/file/a51a74b2d71387dc71cc29181b5519bb-Paper-Conference.pdf)
  - [Speculative Knowledge Distillation: Bridging the Teacher-Student Gap Through Interleaved Sampling](https://proceedings.iclr.cc/paper_files/paper/2025/file/a2747a3844ca1e4667fbff3f558eb39b-Paper-Conference.pdf)
  - [Progressive Mixed-Precision Decoding for Efficient LLM Inference](https://proceedings.iclr.cc/paper_files/paper/2025/file/5df4313ecd4875931fbdacc486cc1fcf-Paper-Conference.pdf)
  - [STAFF: Speculative Coreset Selection for Task-Specific Fine-tuning](https://proceedings.iclr.cc/paper_files/paper/2025/file/412360d2dd428c26f34918c8d682cf7e-Paper-Conference.pdf)
  - [Data Whisperer: Efficient Data Selection for Task-Specific LLM Fine-Tuning via Few-Shot In-Context Learning](https://aclanthology.org/2025.acl-long.1135.pdf)
- **SAMSum** (measurement instrument): *measured_by*, 2 papers
  > dialogue summarization: samsum (Gliwa et al., 2019) and qmsum (Zhong et al., 2021) from LongBench (Bai et al., 2024)
  - [ResQ: Mixed-Precision Quantization of Large Language Models with Low-Rank Residuals](https://raw.githubusercontent.com/mlresearch/v267/main/assets/saxena25b/saxena25b.pdf)
  - [Towards Sustainable NLP: Insights from Benchmarking Inference Energy in Large Language Models](https://aclanthology.org/2025.naacl-long.632.pdf)
- **QMSum** (measurement instrument): *measured_by*, 1 paper
  > dialogue summarization: samsum (Gliwa et al., 2019) and qmsum (Zhong et al., 2021) from LongBench (Bai et al., 2024)
  - [ResQ: Mixed-Precision Quantization of Large Language Models with Low-Rank Residuals](https://raw.githubusercontent.com/mlresearch/v267/main/assets/saxena25b/saxena25b.pdf)
- **PoSum-Bench** (measurement instrument): *measured_by*, 1 paper
  > we introduce PoSum-Bench, a comprehensive benchmark for evaluating positional bias in conversational summarization (Abstract)
  - [PoSum-Bench: Benchmarking Position Bias in LLM-based Conversational Summarization](https://aclanthology.org/2025.emnlp-main.404.pdf)
- **Human evaluation** (measurement instrument): *measured_by*, 1 paper
  > To evaluate generated dialogue summaries and item recommendation information, we conducted a human evaluation using CrowdWorks. (Section 4.7)
  - [Refining Text Generation for Realistic Conversational Recommendation via Direct Preference Optimization](https://aclanthology.org/2025.emnlp-main.1456.pdf)

### Associated with
- **Hallucination** (behavioral indicator), 1 paper
  > Finally, a notable limitation is the persistence of hallucinations in the generation of item recommendation information and dialogue summaries, where the model fabricates features not present in the source content. (Limitations)
  - [Refining Text Generation for Realistic Conversational Recommendation via Direct Preference Optimization](https://aclanthology.org/2025.emnlp-main.1456.pdf)
