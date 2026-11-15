# Sign language translation
**Type:** Behavioral indicator  
**Supporting papers:** 6  
**Also known as:** Sign-to-text translation, Sentence-level translation  

## State of the Field

**Space of definitions.** Across the papers, the dominant framing is generating text in a spoken language from a sign language video sequence, described as either a fluent textual translation or written text that corresponds to the meaning of the signs. Some authors make the target more specific, such as translation from each sign language to its region's spoken language or producing a full English sentence from an American Sign Language clip, with success described in terms of preserving meaning and, in one definition, grammar and lexical content. A smaller strand uses the label sentence-level translation for translating one sentence or isolated sentence-length clip at a time, sometimes without broader document context.

**Variants.** The names vary, with papers using sign language translation, sign-to-text translation, and sentence-level translation. The recurring setting is sentence-level work on isolated clips, including American Sign Language to English and zero-shot sentence-level translation on FLEURS-ASL, while another benchmark description says the same resource is used primarily for sentence- and discourse-level translation. Another line frames the task as translation from each sign language to its region's spoken language.

**Space of elicitation and scores.** Papers link this behavior to 2 measurement instruments, FLEURS-ASL and How2Sign, both used as benchmarks or datasets for translation from sign language video to text. FLEURS-ASL is described as supporting primarily sentence- and discourse-level translation, and papers also report sentence-level translation results on FLEURS-ASL and How2Sign scored with BLEURT.

**What it is taken as evidence of.** Papers do not converge on a single construct that this behavior reflects, and instead link it to 3 constructs in different ways. One paper treats it as related to sign language understanding, explicitly listing it as a sub-task, and another relates it to contextual understanding through demands on "fine-grained comprehension and context awareness." A separate paper claims a causal relationship from cross-lingual generalization to sign language translation, reporting multilingual transfer benefits for higher- and lower-resource sign languages.

## Sources

**Sign language translation** (1 paper: [Uni-Sign: Toward Unified Sign Language Understanding at Scale](https://proceedings.iclr.cc/paper_files/paper/2025/file/260a14acce2a89dad36adc8eefe7c59e-Paper-Conference.pdf))
> The task of generating a fluent textual translation in a spoken language from a given sign language video sequence.

**Sign-to-text translation** (1 paper: [YouTube-SL-25: A Large-Scale, Open-Domain Multilingual Sign Language Parallel Corpus](https://proceedings.iclr.cc/paper_files/paper/2025/file/cbbb65dc108e8ac2f82cba25bc5992fc-Paper-Conference.pdf))
> The task of generating written text that corresponds to the meaning of a sequence of signs in a video.

**Sentence-level translation** (1 paper: [BOUQuET : dataset, Benchmark and Open initiative for Universal Quality Evaluation in Translation](https://aclanthology.org/2025.emnlp-main.1400.pdf))
> Translating text one sentence at a time, often without access to the broader document context.

## Relationships

### Sign language translation →
- **FLEURS-ASL** (measurement instrument): *measured_by*, 2 papers
  > We provide sentence-level translation (scored with BLEURT [29]) (speciﬁcally, BLEURT-20 [24]) and sign language identiﬁcation (scored with top-1 accuracy) results on benchmarks for 4 sign languages: American Sign Language (ase, FLEURS-ASL [34] & How2Sign [4])... (Section 3.3)
  - [YouTube-SL-25: A Large-Scale, Open-Domain Multilingual Sign Language Parallel Corpus](https://proceedings.iclr.cc/paper_files/paper/2025/file/cbbb65dc108e8ac2f82cba25bc5992fc-Paper-Conference.pdf)
  - [FLEURS-ASL: Including American Sign Language in Massively Multilingual Multitask Evaluation](https://aclanthology.org/2025.naacl-long.314.pdf)
- **How2Sign** (measurement instrument): *measured_by*, 2 papers
  > We provide sentence-level translation (scored with BLEURT [29]) (speciﬁcally, BLEURT-20 [24]) and sign language identiﬁcation (scored with top-1 accuracy) results on benchmarks for 4 sign languages: American Sign Language (ase, FLEURS-ASL [34] & How2Sign [4])... (Section 3.3)
  - [YouTube-SL-25: A Large-Scale, Open-Domain Multilingual Sign Language Parallel Corpus](https://proceedings.iclr.cc/paper_files/paper/2025/file/cbbb65dc108e8ac2f82cba25bc5992fc-Paper-Conference.pdf)
  - [Uni-Sign: Toward Unified Sign Language Understanding at Scale](https://proceedings.iclr.cc/paper_files/paper/2025/file/260a14acce2a89dad36adc8eefe7c59e-Paper-Conference.pdf)

### → Sign language translation
- **Cross-lingual generalization** (construct): *causes*, 1 paper
  > experiments in sentence-level translation and sign language identiﬁcation which demonstrate multilingual transfer beneﬁts both higher- and lower-resource sign languages. (Section 5)
  - [YouTube-SL-25: A Large-Scale, Open-Domain Multilingual Sign Language Parallel Corpus](https://proceedings.iclr.cc/paper_files/paper/2025/file/cbbb65dc108e8ac2f82cba25bc5992fc-Paper-Conference.pdf)

### Associated with
- **Sign language understanding** (construct), 1 paper
  > SLU can be subdivided into several sub-tasks, including isolated sign language recognition (ISLR), continuous sign language recognition (CSLR), and sign language translation (SLT). (Section 1)
  - [Uni-Sign: Toward Unified Sign Language Understanding at Scale](https://proceedings.iclr.cc/paper_files/paper/2025/file/260a14acce2a89dad36adc8eefe7c59e-Paper-Conference.pdf)
- **Contextual understanding** (construct), 1 paper
  > All these tasks [ISLR, CSLR, and SLT] impose indispensable demands on the model’s fine-grained comprehension and context awareness capabilities. (Section 1)
  - [Uni-Sign: Toward Unified Sign Language Understanding at Scale](https://proceedings.iclr.cc/paper_files/paper/2025/file/260a14acce2a89dad36adc8eefe7c59e-Paper-Conference.pdf)
