# De-identification
**Type:** Behavioral indicator  
**Supporting papers:** 4  
**Also known as:** Text anonymization  

## State of the Field

**Space of definitions.** Across the papers, de-identification is treated as model-led text modification that removes identifying content from an input. A narrower healthcare framing describes it as automatically removing or replacing personally identifiable information, especially patient and sometimes provider information, to protect privacy, while a broader anonymization framing defines success as removing, obfuscating, or generalizing cues that could support inference about an author's attributes while maintaining the utility of the original text. As one paper states, an anonymizing LLM attempts to "remove, obfuscate, or generalize cues used in the inference by adapting relevant parts of the text" (Language Models are Advanced Anonymizers).

**Variants.** Papers use distinct names and settings for closely related versions of this behavior. One line of work uses the name de-identification for healthcare NLP, focused on patient and sometimes provider information, while another uses text anonymization for adapting text so personal attributes cannot be inferred; this broader framing is also described within an LLM-based adversarial anonymization framework. One paper also relates de-identification to Paraphrasing by using pure text paraphrasing to baseline anonymizing effect.

**Space of elicitation and scores.** No measurement instrument is linked to it. Papers instead operationalize the behavior directly in task terms, as automated removal or replacement of personally identifiable information, or as modification of text to remove, obfuscate, or generalize inferential cues.

**What it is taken as evidence of.** Across these papers, de-identification is related to Privacy preservation rather than linked to several different constructs. The linked formulation presents text anonymization as removing information that could lead to inference of pre-specified author attributes while maintaining the utility of the original text, and no other construct is linked to it.

## Sources

**De-identification** (1 paper: [Not What the Doctor Ordered: Surveying LLM-based De-identification and Quantifying Clinical Information Loss](https://aclanthology.org/2025.emnlp-main.1637.pdf))
> The task of processing text to automatically remove or replace personally identifiable information (PII) to protect patient privacy.

**Text anonymization** (1 paper: [Language Models are Advanced Anonymizers](https://proceedings.iclr.cc/paper_files/paper/2025/file/f478b2e8ad9ff0756bf5b79fb31c330f-Paper-Conference.pdf))
> The observable process of a model modifying a text to remove, obfuscate, or generalize information that could be used to infer an author's personal attributes.

## Relationships

### Associated with
- **Paraphrasing** (behavioral indicator), 1 paper
  > Additionally, we make use of the state-of-the-Art 11B transformer-based paraphrasing model Dipper (Krishna et al., 2024) to baseline the anonymizing effect of pure text paraphrasing. (Sec. 5)
  - [Language Models are Advanced Anonymizers](https://proceedings.iclr.cc/paper_files/paper/2025/file/f478b2e8ad9ff0756bf5b79fb31c330f-Paper-Conference.pdf)
- **Privacy preservation** (construct), 1 paper
  > “the goal of any text anonymization method is to remove all information that could lead to the inference of a set of pre-specified author attributes while maintaining the utility of the original text.”
  - [Language Models are Advanced Anonymizers](https://proceedings.iclr.cc/paper_files/paper/2025/file/f478b2e8ad9ff0756bf5b79fb31c330f-Paper-Conference.pdf)
