# Algorithmic reasoning
**Type:** Construct  
**Supporting papers:** 24  
**Also known as:** Algorithmic capability, Algorithmic processing, Algorithmic comprehension  

## State of the Field

**Space of definitions.** Across the surveyed work, the prevailing usage treats algorithmic reasoning as a latent ability or capacity to infer, devise, follow, or apply multi-step, generalizable procedures for solving problems. Most definitions contrast it with memorization, pattern matching, or solving isolated instances, and several emphasize procedures that solve a class of problems rather than a single case. A common narrower framing places it in programming, where generating code from a natural-language problem statement is described as requiring high-level algorithmic reasoning alongside low-level coding, while smaller strands broaden it to structured computations in transformers, graph traversal or pathfinding, arithmetic and sequence generation, iterative updates, or debugging deeper algorithmic design issues.

**Space of facets.** Papers do not present a single shared taxonomy, but they recurrently use nearby labels such as algorithmic capability, algorithmic processing, and algorithmic comprehension for largely overlapping phenomena. Across these variants, the stable distinction is structured rule- or procedure-following versus memorized instances or pattern matching, with some authors locating the construct as a model-internal latent capacity and others describing it through task performance. The same label is applied across high-level program design, search procedures over permutations, word sorting and multi-step arithmetic, graph problems such as reachability and maximum-sum path, and correction of higher-level programming logic, so scope varies from broad procedural computation to specific code-centered reasoning.

**Space of measurement.** Operationalization is relatively concentrated: papers link algorithmic reasoning to 4 measurement instruments, BIG-Bench Hard, CodeContests, HumanEval+, and MBPP, and to 3 behavioral indicators, chain of thought, code generation, and integer addition. The instruments make the construct concrete through word sorting and multi-step arithmetic in BIG-Bench Hard, competitive programming tasks in CodeContests, and HumanEval+ and MBPP+ in work that evaluates reasoning and programming. These choices mostly match definitions that emphasize stepwise procedures and algorithm design, though the measurements lean toward programming and arithmetic-style tasks even when some definitions describe broader transformer computations or debugging of algorithmic flaws.

**Links.** Outside measurement, papers mostly relate algorithmic reasoning to neighboring constructs rather than report correlations. It is reported as related to graph reasoning, problem-solving ability, mathematical reasoning, code generation, and integer addition, and one paper claims a causal relationship from chain of thought to algorithmic reasoning, stating that chain-of-thought helps substantially on problems requiring mathematical, logical, or algorithmic reasoning.

## Sources

**Algorithmic reasoning** (7 papers: [DyVal: Dynamic Evaluation of Large Language Models for Reasoning Tasks](https://proceedings.iclr.cc/paper_files/paper/2024/file/4ea4a1ea4d9ff273688c8e92bd087112-Paper-Conference.pdf), [LLM-Assisted Code Cleaning For Training Accurate Code Generators](https://proceedings.iclr.cc/paper_files/paper/2024/file/41137f3997ade899893ccd3973592d4b-Paper-Conference.pdf), [Large Language Models as Tool Makers](https://proceedings.iclr.cc/paper_files/paper/2024/file/ed91353f700d113e5d848c7e04a858b0-Paper-Conference.pdf), [StrategyLLM: Large Language Models as Strategy Generators, Executors, Optimizers, and Evaluators for Problem Solving](https://proceedings.neurips.cc/paper_files/paper/2024/file/af7cc9e2366b8f8837a6ef339810277a-Paper-Conference.pdf), [What Makes Large Language Models Reason in (Multi-Turn) Code Generation?](https://proceedings.iclr.cc/paper_files/paper/2025/file/63fef0802863f47775c3563e18cbba17-Paper-Conference.pdf), [Universal Length Generalization with Turing Programs](https://raw.githubusercontent.com/mlresearch/v267/main/assets/hou25a/hou25a.pdf), [NL-Debugging: Exploiting Natural Language as an Intermediate Representation for Code Debugging](https://aclanthology.org/2025.emnlp-main.80.pdf))
> The ability to infer and apply multi-step algorithms needed to solve programming problems from natural-language specifications.

**Algorithmic capability** (1 paper: [Algorithmic Capabilities of Random Transformers](https://proceedings.neurips.cc/paper_files/paper/2024/file/bccdd196d798a51a4961989984a9ed4a-Paper-Conference.pdf))
> The latent capacity of a transformer to implement structured computations such as arithmetic, recall, balancing, or sequence generation across different tasks.

**Algorithmic processing** (1 paper: [Differentiation and Specialization of Attention Heads via the Refined Local Learning Coefficient](https://proceedings.iclr.cc/paper_files/paper/2025/file/fad7c708dda11f3e72cc1629bb130379-Paper-Conference.pdf))
> The model's ability to apply simple, generalizable rules or procedures to solve tasks, as opposed to relying on memorized instances.

**Algorithmic comprehension** (1 paper: [Arithmetic Without Algorithms: Language Models Solve Math with a Bag of Heuristics](https://proceedings.iclr.cc/paper_files/paper/2025/file/8c5f30296296d2ae402ebbd09aaa9c12-Paper-Conference.pdf))
> The ability to learn and apply robust, generalizable, step-by-step procedures to solve problems, as opposed to relying on pattern matching or memorization.

## Relationships

### Algorithmic reasoning →
- **BIG-Bench Hard** (measurement instrument): *measured_by*, 1 paper
  > algorithmic reasoning [BBH, 55] (Introduction).
  - [Many-Shot In-Context Learning](https://proceedings.neurips.cc/paper_files/paper/2024/file/8cb564df771e9eacbfe9d72bd46a24a9-Paper-Conference.pdf)
- **CodeContests** (measurement instrument): *measured_by*, 1 paper
  > complex algorithmic reasoning tasks, such as those found in competitive programming benchmarks like CodeContests
  - [What Makes Large Language Models Reason in (Multi-Turn) Code Generation?](https://proceedings.iclr.cc/paper_files/paper/2025/file/63fef0802863f47775c3563e18cbba17-Paper-Conference.pdf)
- **MBPP** (measurement instrument): *measured_by*, 1 paper
  > Our experiments demonstrate that RaLU significantly outperforms existing baselines in mathematical reasoning (GSM8K, MATH) and algorithmic reasoning (HumanEval+, MBPP+), underscoring its potential to advance LLM reasoning and programming by offering enhanced accuracy and interpretability. (Abstract)
  - [Reasoning-as-Logic-Units: Scaling Test-Time Reasoning in Large Language Models Through Logic Unit Alignment](https://raw.githubusercontent.com/mlresearch/v267/main/assets/li25df/li25df.pdf)
- **HumanEval+** (measurement instrument): *measured_by*, 1 paper
  > Our experiments demonstrate that RaLU significantly outperforms existing baselines in mathematical reasoning (GSM8K, MATH) and algorithmic reasoning (HumanEval+, MBPP+), underscoring its potential to advance LLM reasoning and programming by offering enhanced accuracy and interpretability. (Abstract)
  - [Reasoning-as-Logic-Units: Scaling Test-Time Reasoning in Large Language Models Through Logic Unit Alignment](https://raw.githubusercontent.com/mlresearch/v267/main/assets/li25df/li25df.pdf)

### → Algorithmic reasoning
- **Chain of thought** (behavioral indicator): *causes*, 1 paper
  > Finding 1: CoT only helps substantially on problems requiring mathematical, logical, or algorithmic reasoning. (Section 1)
  - [To CoT or not to CoT? Chain-of-thought helps mainly on math and symbolic reasoning](https://proceedings.iclr.cc/paper_files/paper/2025/file/ead542f13a38179d1b55b88610f959a1-Paper-Conference.pdf)

### Associated with
- **Graph reasoning** (construct), 1 paper
  > In this work, we focus on classes of transformers solving algorithmic reasoning problems on graphs. (Section 1)
  - [Understanding Transformer Reasoning Capabilities via Graph Algorithms](https://proceedings.neurips.cc/paper_files/paper/2024/file/8f395480c04ac6dfb2c2326a639df88e-Paper-Conference.pdf)
- **Problem-solving ability** (construct), 1 paper
  > Algorithmic reasoning is a fundamental cognitive ability that plays a pivotal role in problem-solving and decision-making processes. (Abstract)
  - [PUZZLES: A Benchmark for Neural Algorithmic Reasoning](https://proceedings.neurips.cc/paper_files/paper/2024/file/e5d1eaadeed651ba1021c09149db4b92-Paper-Datasets_and_Benchmarks_Track.pdf)
- **Mathematical reasoning** (construct), 1 paper
  > Arithmetic reasoning provides a lens for this investigation, as it can be solved using various methods: learning known algorithms, developing novel approaches, or by memorizing vast quantities of input-output pairs. (Section 1)
  - [Arithmetic Without Algorithms: Language Models Solve Math with a Bag of Heuristics](https://proceedings.iclr.cc/paper_files/paper/2025/file/8c5f30296296d2ae402ebbd09aaa9c12-Paper-Conference.pdf)
- **Code generation** (behavioral indicator), 1 paper
  > However, complex programming tasks requiring multi-step algorithmic reasoning—such as implementing dynamic programming solutions or optimizing parallel computation patterns—remain challenging (Section 1)
  - [Reasoning Through Execution: Unifying Process and Outcome Rewards for Code Generation](https://raw.githubusercontent.com/mlresearch/v267/main/assets/yu25f/yu25f.pdf)
- **Integer addition** (behavioral indicator), 1 paper
  > “To study algorithmic reasoning in a sterile laboratory setting, the academic community focuses on simple arithmetic test problems like addition.”
  - [Transformers Can Do Arithmetic with the Right Embeddings](https://proceedings.neurips.cc/paper_files/paper/2024/file/c35986bc1ee29b31c1011481b77fe540-Paper-Conference.pdf)
