# PandaLM
**Type:** Measurement instrument  
**Supporting papers:** 6  

## State of the Field

**What it is.** Across the definitions, PandaLM is most commonly described as a fine-tuned LLM judge, based on Llama-7b, for preference judgment and automated evaluation of other LLMs. Some papers refer to the model specifically as PandaLM-7B and describe it as scoring or selecting outputs, while another definition presents it as a fine-tuned judge benchmark, trained on human preference data, that is used to evaluate model outputs.

**What it is claimed to measure.** In the recorded links, papers use PandaLM to measure one construct and one behavioral indicator: Helpfulness and Instruction following. The helpfulness link is explicit, with one paper saying it uses PandaLM "to evaluate the helpfulness of various models," while another paper frames PandaLM as addressing "relative conciseness, clarity, adherence to instructions, comprehensiveness, and formality," which is recorded as measuring instruction following.

**Space of uses.** In the descriptions, PandaLM is used as an automated judge in evaluator comparisons, and no measurement instrument is linked to it. Papers place it alongside other judge models such as JudgeLM and GPT-4, and another paper uses it as a comparison point when assessing tuned judges.

**Concerns raised.** A negative comparative assessment appears in one paper, which says that the judges it tuned "all outperforms strongly PandaLM".

## Sources

**PandaLM** (2 papers: [PiCO: Peer Review in LLMs based on Consistency Optimization](https://proceedings.iclr.cc/paper_files/paper/2025/file/39e9c5913c970e3e49c2df629daff636-Paper-Conference.pdf), [Tuning LLM Judge Design Decisions for 1/1000 of the Cost](https://raw.githubusercontent.com/mlresearch/v267/main/assets/salinas25a/salinas25a.pdf))
> A fine-tuned language model (based on Llama-7b) designed specifically to act as a judge for preference-based evaluation of other LLMs.

## Relationships

### → PandaLM
- **Instruction following** (behavioral indicator): *measured_by*, 1 paper
  > It addresses vital subjective factors such as relative conciseness, clarity, adherence to instructions, comprehensiveness, and formality.
  - [PandaLM: An Automatic Evaluation Benchmark for LLM Instruction Tuning Optimization](https://proceedings.iclr.cc/paper_files/paper/2024/file/be3b0d51a2b86cb4ffe50f13480217e0-Paper-Conference.pdf)
- **Helpfulness** (construct): *measured_by*, 1 paper
  > Specifically, we use PandaLM (Wang et al., 2023b, 2024) to evaluate the helpfulness of various models. (Section 4.1)
  - [Threshold Filtering Packing for Supervised Fine-Tuning: Training Related Samples within Packs](https://aclanthology.org/2025.naacl-long.226.pdf)
