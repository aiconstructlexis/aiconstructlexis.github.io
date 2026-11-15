# Financial reasoning
**Type:** Construct  
**Supporting papers:** 5  
**Also known as:** Financial numerical reasoning, Present value calculation  

## State of the Field

**Space of definitions.** Most definitions treat financial reasoning as a latent ability rather than a directly observed task. The broader framing is the ability to solve finance-related questions that require reasoning over financial documents or calculations, while a narrower variant specializes it as financial numerical reasoning, multi-step computations over financial data that integrate text and tables, apply domain-specific logic, and generate executable programs to derive answers. A smaller line of work instead uses a task-level framing, present value calculation, as the observable computation of the current worth of future cash flows given a discount rate, so the main difference is between a broad latent ability, a narrower numerical version of that ability, and a specific observable task.

**Space of facets.** The papers split the label into a broad financial reasoning usage and narrower task-focused variants, rather than a stable set of named subconstructs. One specialization describes it as requiring "multi-step problem-solving including fact extraction, logical inference, and mathematical computation," and also emphasizes text-and-table integration and program generation; another instantiation focuses on present value calculation in intertemporal choice. No other construct-level equivalences, contrasts, or nested subtypes are reported.

**Space of measurement.** Papers operationalize the construct with 2 linked measurement instruments and no linked behavioral indicators. The instruments are FinQA and FinanceBench, both benchmark-style evaluations: FinQA is described as a dataset developed to benchmark models for numerical reasoning tasks in the financial domain, and FinanceBench tests financial document understanding with complex reasoning over reports. These measurements line up with the two main definitions, one centered on numerical reasoning and one on reasoning over financial documents.

**Links.** The reported links are limited to measurement. Papers say financial reasoning is measured by FinQA and by FinanceBench, and no causal, correlational, or other related links with other constructs or behaviors are reported.

## Sources

**Financial reasoning** (1 paper: [PlanGEN: A Multi-Agent Framework for Generating Planning and Reasoning Trajectories for Complex Problem Solving](https://aclanthology.org/2025.emnlp-main.1042.pdf))
> The latent ability to solve finance-related questions that require reasoning over financial documents or calculations.

**Financial numerical reasoning** (1 paper: [Program of Thoughts for Financial Reasoning: Leveraging Dynamic In-Context Examples and Generative Retrieval](https://aclanthology.org/2025.emnlp-main.1577.pdf))
> The latent ability of a model to perform multi-step computations involving financial data by integrating information from text and tables, applying domain-specific logic, and generating executable programs to derive correct answers.

**Present value calculation** (1 paper: [Language Models Trained to do Arithmetic Predict Human Risky and Intertemporal Choice](https://proceedings.iclr.cc/paper_files/paper/2025/file/a3372a60f76e0acce756cb24deead020-Paper-Conference.pdf))
> The observable computational task of determining the current worth of a future sum of money or stream of cash flows, given a specified rate of return or discount rate.

## Relationships

### Financial reasoning →
- **FinQA** (measurement instrument): *measured_by*, 1 paper
  > datasets such as FinQA (Chen et al., 2021b) and ConvFinQA (Chen et al., 2022) have been developed to benchmark deep learning models for such numerical reasoning tasks in the financial domain.
  - [Program of Thoughts for Financial Reasoning: Leveraging Dynamic In-Context Examples and Generative Retrieval](https://aclanthology.org/2025.emnlp-main.1577.pdf)
- **FinanceBench** (measurement instrument): *measured_by*, 1 paper
  > “FINANCEBENCH tests financial document understanding with complex reasoning over reports.”
  - [Cost-efficient Collaboration between On-device and Cloud Language Models](https://raw.githubusercontent.com/mlresearch/v267/main/assets/narayan25a/narayan25a.pdf)
