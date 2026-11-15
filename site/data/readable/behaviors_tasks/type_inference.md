# Type inference
**Type:** Behavioral indicator  
**Supporting papers:** 3  
**Also known as:** Type annotation prediction, Type prediction  

## State of the Field

**Space of definitions.** Across the papers, the prevailing usage is inferring missing static type information and adding it back into code. One formulation focuses on Python code, where missing type hints are inserted for function parameters, return values, and variables, and phrases the goal as inferring types that could have been written by developers; another describes the task more broadly as assigning static types to variables and functions in a dynamically typed programming language.

**Variants.** Authors use both type annotation prediction and type prediction for this behavior. The clearest variant is work on untyped Python repositories, illustrated by adding annotations such as `def greet(name):` to `def greet(name: str) -> str:`, while a broader variant is stated at the level of variables and functions in dynamically typed languages without further subtask detail.

**Space of elicitation and scores.** No measurement instrument is linked to this behavior in the papers.

**What it is taken as evidence of.** No construct is linked to this behavior, so the papers do not state what broader construct it is taken to indicate.

## Sources

**Type annotation prediction** (1 paper: [TypyBench: Evaluating LLM Type Inference for Untyped Python Repositories](https://raw.githubusercontent.com/mlresearch/v267/main/assets/dong25l/dong25l.pdf))
> Inferring and inserting type hints for function parameters, return values, and variables in Python code where such annotations are missing.

**Type prediction** (1 paper: [EffiCoder: Enhancing Code Generation in Large Language Models through Efficiency-Aware Fine-tuning](https://raw.githubusercontent.com/mlresearch/v267/main/assets/huang25as/huang25as.pdf))
> The task of inferring and assigning static types to variables and functions in a dynamically typed programming language.
