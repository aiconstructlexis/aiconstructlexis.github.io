# BookMIA
**Type:** Measurement instrument  
**Supporting papers:** 5  

## State of the Field

**What it is.** Most papers treat BookMIA as a benchmark or dataset of book excerpts, passages, or paragraphs, used as a membership inference benchmark and as a dataset for evaluating memorization. Descriptions differ in detail: some specify excerpts from copyrighted books, some specify books published after model knowledge cutoffs or model release as "unseen" examples, and one description pairs those with passages from popular books as memorized examples. One paper also characterizes it as a prior temporal detection dataset, and another use selects only the "unseen" subset.

**What it is claimed to measure.** The recorded measurement claims are narrow rather than spread across many targets: papers link BookMIA to one construct, Memorization, and one behavioral indicator, Pre-training data detection. One paper uses it to measure memorization by treating 2023 book excerpts as unseen text and passages from popular books as memorized examples, while another uses it to evaluate pre-training data detection methods.

**Space of uses.** When papers situate BookMIA relative to other evaluations, they present it as one benchmark among others, using it alongside WikiMIA, BookTection, ArXivTection, and Pile in evaluation. One paper also places it with WikiMIA and BookTection under the label of "previous membership inference benchmarks." A smaller usage restricts evaluation to data points labeled "unseen," meaning paragraphs from books published after the release of the models.

**Concerns raised.** One paper raises a temporal reliability concern, stating that previous membership inference benchmarks such as BookMIA "cannot be reliably used for Llama-3 because the model was trained more recently."

## Sources

**BookMIA** (3 papers: [Infilling Score: A Pretraining Data Detection Algorithm for Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/5709163243753c9c9ab7f4b4e5a8766d-Paper-Conference.pdf), [PoisonedParrot: Subtle Data Poisoning Attacks to Elicit Copyright-Infringing Content from Large Language Models](https://aclanthology.org/2025.naacl-long.415.pdf), [Information-Guided Identification of Training Data Imprint in (Proprietary) Large Language Models](https://aclanthology.org/2025.naacl-long.99.pdf))
> A membership inference benchmark for book excerpts used as a prior temporal detection dataset.

## Relationships

### → BookMIA
- **Pre-training data detection** (behavioral indicator): *measured_by*, 1 paper
  > To verify the effectiveness of detection methods, we employ four common benchmark datasets for evaluations, including WikiMIA (Shi et al., 2024), ArXivTection (Duarte et al., 2024), BookTection (Duarte et al., 2024) BookMIA (Shi et al., 2024) and Pile (Maini et al., 2024). (Section 4.1)
  - [Fine-tuning can Help Detect Pretraining Data from Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/98cda3e39e4ca2da449092a99c485e1a-Paper-Conference.pdf)
- **Memorization** (construct): *measured_by*, 1 paper
  > We use the BookMIA dataset (Shi et al., 2023), which consists of text excerpts from books published in 2023 (after the knowledge cutoff of the models we study) as examples of unseen text, and passages from popular books as memorized examples (Chang et al., 2023). (Section 4.1)
  - [Information-Guided Identification of Training Data Imprint in (Proprietary) Large Language Models](https://aclanthology.org/2025.naacl-long.99.pdf)

### Associated with
- **Membership inference attack** (measurement instrument), 1 paper
  > “Previous membership inference benchmarks such as WikiMIA, BookMIA (Shi et al., 2024), and BookTection (Duarte et al., 2024)”
  - [Infilling Score: A Pretraining Data Detection Algorithm for Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/5709163243753c9c9ab7f4b4e5a8766d-Paper-Conference.pdf)
