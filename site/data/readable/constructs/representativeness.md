# Representativeness
**Type:** Construct  
**Supporting papers:** 3  

## State of the Field

**Space of definitions.** The definition treats representativeness as a property of a training-data subset relative to the full dataset: it is the degree to which the subset captures the essential information needed for a model to perform well across tasks, combining sufficiency and necessity with respect to the full dataset. The accompanying usage keeps this framing focused on identifying a "core subset of demonstrations" that is "tailored to specific LLMs" and serves as a "faithful representation" of the training dataset.

**Space of facets.** Rather than introducing subtypes, the paper organizes the concept around a subset versus full-dataset comparison and pairs representativeness with minimality. A high-quality subset is described as both representative of the entire training dataset and "as minimal in size as possible," with the stated dual objectives of maintaining data quality and minimizing computational expenses.

**Space of measurement.** No measurement instrument or behavioral indicator is linked to representativeness. In use, the construct is described through selecting a core subset of demonstrations and requiring that this subset be a faithful, minimal representation of the full training dataset, but no named benchmark, evaluation procedure, or other instrument is attached to it.

## Sources

**Representativeness** (1 paper: [Large Language Models are Demonstration Pre-Selectors for Themselves](https://raw.githubusercontent.com/mlresearch/v267/main/assets/jin25i/jin25i.pdf))
> The degree to which a subset of training data captures the essential information needed for a model to perform well across tasks, reflecting both sufficiency and necessity with respect to the full dataset.
