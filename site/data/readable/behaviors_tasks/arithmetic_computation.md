# Arithmetic computation
**Type:** Behavioral indicator  
**Supporting papers:** 30  
**Also known as:** Arithmetic expression evaluation, Three-operand arithmetic solving, Arithmetic calculation, Arithmetic execution, Arithmetic solving, Numerical calculation, Expected value calculation, Median finding, Linear function evaluation, Numerical computation, Numerical analysis, Mathematical calculation  

## State of the Field

**Space of definitions.** Across the surveyed work, the prevailing usage is direct calculation: producing the correct result for a numerical expression or other quantitative input. Most definitions describe arithmetic expressions with numbers and operators, sometimes with brackets or multi-step operator sequences, and one study says the goal is to calculate the input arithmetic expression and generate the correct result (Seq-VCR: Preventing Collapse in Intermediate Transformer Representations for Enhanced Reasoning). Final-answer correctness is the usual success criterion, though some papers tighten this to valid step-by-step arithmetic with correct order of operations and numerical precision, or to arithmetic carried out correctly within a larger reasoning chain.

**Variants.** Papers study this behavior under several names, most commonly arithmetic expression evaluation, arithmetic calculation, and numerical calculation, while varying both input structure and domain. Recurring variants include three-operand problems, basic addition and multiplication, structured expressions over binary inputs, modular arithmetic, expected value calculations, median finding, and linear function evaluation; other work places the same behavior in visual, tabular, medical, and financial settings, including calculations from tables and text, growth-rate and cross-period comparisons, and quantitative financial queries. A smaller line of work uses broader labels such as numerical analysis for arithmetic operations, comparisons, trend detection, or time-series style prediction.

**Space of elicitation and scores.** Papers link it to 1 measurement instrument, TableEval, which measures it through numerical-analysis style table question answering. Outside this explicit instrument link, elicitation is usually through arithmetic prompts or datasets, and scoring is usually answer correctness, sometimes against calculator-computed results or with a symbolic calculator tool. A smaller scoring line checks intermediate arithmetic directly, for example by verifying whether each arithmetic step is valid and flagging cases where the formula and inputs are correct but the math is wrong (From Scores to Steps: Diagnosing and Improving LLM Performance in Evidence-Based Medical Calculations).

**What it is taken as evidence of.** Papers do not converge on a broader construct that this behavior is taken to indicate. Only 1 construct is linked, Table reasoning, and that link is framed as related rather than as measurement or causation: one paper describes arithmetic computation alongside semantic understanding and information extraction as part of table-specific reasoning skills. Beyond that single related link, no further construct framing appears in the linked relations.

## Sources

**Arithmetic expression evaluation** (2 papers: [Seq-VCR: Preventing Collapse in Intermediate Transformer Representations for Enhanced Reasoning](https://proceedings.iclr.cc/paper_files/paper/2025/file/b577c062bd4f894b7e05fab6440373ed-Paper-Conference.pdf), [Task Generalization with Autoregressive Compositional Structure: Can Learning from $D$ Tasks Generalize to $D^T$ Tasks?](https://raw.githubusercontent.com/mlresearch/v267/main/assets/abedsoltan25a/abedsoltan25a.pdf))
> The task of calculating the value of a mathematical expression containing numbers, operators, and brackets, and generating the final result.

**Three-operand arithmetic solving** (1 paper: [Interpretability Analysis of Arithmetic In-Context Learning in Large Language Models](https://aclanthology.org/2025.emnlp-main.92.pdf))
> Generating the correct result for arithmetic expressions involving three operands and two operators, such as 'a + b + c = ?'.

**Arithmetic calculation** (3 papers: [On the Inductive Bias of Stacking Towards Improving Reasoning](https://proceedings.neurips.cc/paper_files/paper/2024/file/837bc5db12f3d394d220815a7687340c-Paper-Conference.pdf), [Can LLMs Understand Time Series Anomalies?](https://proceedings.iclr.cc/paper_files/paper/2025/file/05774fb74e863308c4b460c9f49f6918-Paper-Conference.pdf), [Probing for Arithmetic Errors in Language Models](https://aclanthology.org/2025.emnlp-main.411.pdf))
> The observable act of computing the result of a numerical expression.

**Arithmetic computation** (2 papers: [MedCalc-Bench: Evaluating Large Language Models for Medical Calculations](https://proceedings.neurips.cc/paper_files/paper/2024/file/99e81750f3fdfcaf9613db2dbf4bd623-Paper-Datasets_and_Benchmarks_Track.pdf), [Alignment for Efficient Tool Calling of Large Language Models](https://aclanthology.org/2025.emnlp-main.898.pdf))
> The observable action of performing mathematical calculations as part of a model's generated output or reasoning chain.

**Arithmetic execution** (1 paper: [How Is LLM Reasoning Distracted by Irrelevant Context? An Analysis Using a Controlled Benchmark](https://aclanthology.org/2025.emnlp-main.674.pdf))
> The observable behavior of performing numerical calculations as part of a reasoning process.

**Arithmetic solving** (1 paper: [Generalizing Reasoning Problems to Longer Lengths](https://proceedings.iclr.cc/paper_files/paper/2025/file/abcbdf504b621b4d1213aa7a5c489f8a-Paper-Conference.pdf))
> Producing correct arithmetic results for expressions or modular arithmetic problems.

**Numerical calculation** (2 papers: [Can We Predict Performance of Large Models across Vision-Language Tasks?](https://raw.githubusercontent.com/mlresearch/v267/main/assets/zhao25y/zhao25y.pdf), [FinTrust: A Comprehensive Benchmark of Trustworthiness Evaluation in Finance Domain](https://aclanthology.org/2025.emnlp-main.512.pdf))
> The task of performing mathematical calculations based on information presented in a visual format.

**Expected value calculation** (1 paper: [Language Models Trained to do Arithmetic Predict Human Risky and Intertemporal Choice](https://proceedings.iclr.cc/paper_files/paper/2025/file/a3372a60f76e0acce756cb24deead020-Paper-Conference.pdf))
> The observable computational task of determining the average outcome of a probabilistic event by summing the values of each outcome multiplied by its probability.

**Median finding** (1 paper: [Lower Bounds for Chain-of-Thought Reasoning in Hard-Attention Transformers](https://raw.githubusercontent.com/mlresearch/v267/main/assets/bavandpour25a/bavandpour25a.pdf))
> The task of identifying the median value from an input list of N numbers.

**Linear function evaluation** (1 paper: [Towards Understanding Fine-Tuning Mechanisms of LLMs via Circuit Analysis](https://raw.githubusercontent.com/mlresearch/v267/main/assets/wang25ak/wang25ak.pdf))
> Computing the value of a linear function such as y = mx + b for given inputs.

**Numerical computation** (1 paper: [OmniEval: An Omnidirectional and Automatic RAG Evaluation Benchmark in Financial Domain](https://aclanthology.org/2025.emnlp-main.292.pdf))
> The observable behavior of performing mathematical or financial calculations to answer a quantitative question.

**Numerical analysis** (1 paper: [TableEval: A Real-World Benchmark for Complex, Multilingual, and Multi-Structured Table Question Answering](https://aclanthology.org/2025.emnlp-main.363.pdf))
> Performing arithmetic operations, comparisons, or trend detection on numerical data extracted from tables, such as calculating growth rates or identifying maxima.

**Mathematical calculation** (1 paper: [From Scores to Steps: Diagnosing and Improving LLM Performance in Evidence-Based Medical Calculations](https://aclanthology.org/2025.emnlp-main.548.pdf))
> The model performs valid arithmetic operations step-by-step, following correct order of operations and numerical precision rules.

## Relationships

### Arithmetic computation →
- **TableEval** (measurement instrument): *measured_by*, 1 paper
  > "TableEval covers six high-level tasks and 16 fine-grained question types, ranging from simple lookup queries to numerical calculations, comparative analysis, and multi-hop questions."
  - [TableEval: A Real-World Benchmark for Complex, Multilingual, and Multi-Structured Table Question Answering](https://aclanthology.org/2025.emnlp-main.363.pdf)

### Associated with
- **Table reasoning** (construct), 1 paper
  > Our qualitative analysis of model responses reveals that Table-R1-Zero not only acquires multi-step reasoning and reflection abilities like other reasoning models, but also develops essential table-specific reasoning skills such as semantic understanding, information extraction, and arithmetic computation. (Section 1)
  - [Table-R1: Inference-Time Scaling for Table Reasoning Tasks](https://aclanthology.org/2025.emnlp-main.1040.pdf)
