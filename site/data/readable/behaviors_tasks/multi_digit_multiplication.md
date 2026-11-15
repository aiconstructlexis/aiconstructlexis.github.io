# Multi-digit multiplication
**Type:** Behavioral indicator  
**Supporting papers:** 8  
**Also known as:** Integer multiplication, MUL  

## State of the Field

**Space of definitions.** Across papers, the prevailing usage treats this behavior as multiplying two multi-digit integers in base 10 and outputting the product. Most formulations describe either an explicit output-producing task or the task of calculating the product and generating the correct numerical result; as one paper puts it, "The Multiplication (MUL) task [16] involves multiplying two multi-digit numbers in base 10" (Limits of Transformer Language Models on Learning to Compose Algorithms).

**Variants.** Papers use closely related names, most often "multi-digit multiplication" or "integer multiplication", and sometimes the abbreviation "MUL". The main variants differ by operand length and setting, including 4-by-3-digit, 4 × 4, and 5 × 5 problems, and one line of work describes multiplication where both multiplier and multiplicand can vary in length, framed as generalization over both operand lengths.

**Space of elicitation and scores.** Only one linked measurement instrument appears, BIG-bench, which a paper describes as the benchmark containing the multi-digit multiplication task. Scoring is reported with accuracy, and one paper specifically reports exact match accuracy on 5 × 5 integer multiplication.

**What it is taken as evidence of.** Papers do not link this behavior to any construct, and no recorded claim states what construct it reflects.

## Sources

**Multi-digit multiplication** (2 papers: [Limits of Transformer Language Models on Learning to Compose Algorithms](https://proceedings.neurips.cc/paper_files/paper/2024/file/0e797d5139ad94fc2dc2080c09119f29-Paper-Conference.pdf), [Limits of Deep Learning: Sequence Modeling through the Lens of Complexity Theory](https://proceedings.iclr.cc/paper_files/paper/2025/file/62868cc2fc1eb5cdf321d05b4b88510c-Paper-Conference.pdf))
> Multiplying two multi-digit numbers in base 10 as an explicit output-producing task.

**Integer multiplication** (2 papers: [Seq-VCR: Preventing Collapse in Intermediate Transformer Representations for Enhanced Reasoning](https://proceedings.iclr.cc/paper_files/paper/2025/file/b577c062bd4f894b7e05fab6440373ed-Paper-Conference.pdf), [Do Large Language Models Truly Grasp Addition? A Rule-Focused Diagnostic Using Two-Integer Arithmetic](https://aclanthology.org/2025.emnlp-main.681.pdf))
> The task of calculating the product of two multi-digit integers and generating the correct numerical result.

**MUL** (1 paper: [Limits of Transformer Language Models on Learning to Compose Algorithms](https://proceedings.neurips.cc/paper_files/paper/2024/file/0e797d5139ad94fc2dc2080c09119f29-Paper-Conference.pdf))
> Multiplication, a benchmark involving multiplication of two multi-digit base-10 numbers.

## Relationships

### Multi-digit multiplication →
- **BIG-bench** (measurement instrument): *measured_by*, 1 paper
  > "we first consider the multi-digit multiplication task from the BIG-bench benchmark"
  - [Seq-VCR: Preventing Collapse in Intermediate Transformer Representations for Enhanced Reasoning](https://proceedings.iclr.cc/paper_files/paper/2025/file/b577c062bd4f894b7e05fab6440373ed-Paper-Conference.pdf)
