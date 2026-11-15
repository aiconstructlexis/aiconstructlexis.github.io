# Abstract reasoning
**Type:** Construct  
**Supporting papers:** 26  
**Also known as:** Abstract thinking, High-level reasoning, Advanced abstract reasoning, Visual analogy solving  

## State of the Field

**Space of definitions.** Most papers describe abstract reasoning as high-level reasoning over concepts, principles, relations, or problem structure, rather than concrete instances, direct computation, low-level details, symbolic manipulation, or precise step-by-step deduction. This framing appears in discussions of program properties, formal logic and commonsense, semantic analysis and planning, and prompts that use higher-level thoughts or an overarching perspective to guide reasoning. A smaller line of work uses the label for narrower abilities, such as inferring patterns from a few examples, generalizing event mentions by omitting spurious details, turning abstract equations or flowcharts into implementation decisions, handling difficult non-routine mathematics, or completing visual analogies.

**Space of facets.** Papers often align abstract reasoning with abstract thinking or high-level reasoning, and commonly contrast it with low-level reasoning, surface-level reasoning steps, and attention to concrete or irrelevant details. One theoretical account explicitly breaks it into abstraction, extracting common features from concrete entities, and reasoning, deriving new knowledge from existing information. Other papers systematize it through operations like simplifying a problem into an archetype, filtering out intellectually irrelevant components, mapping generalized cause or effect events back to mentions in context, or using analogical, inductive, or transductive strategies to apply a principle to a new case.

**Space of measurement.** Papers link abstract reasoning to 3 measurement instruments, ARC-AGI, Abstraction and Reasoning Corpus, and Bongard Problems, and to 1 behavioral indicator, iterative refinement. The linked instruments are all task-style evaluations: the Abstraction and Reasoning Corpus is described as evaluating abstract reasoning through solving visual puzzles, Bongard Problems as visual puzzles testing pattern recognition and abstract reasoning, and ARC-AGI as a challenge that exposes limitations in abstract reasoning. These operationalizations focus on puzzle solving and pattern recognition, while definitions also place the construct in program verification, formal logic, causal event abstraction, mathematical problem solving, and implementation synthesis; the linked behavioral indicator appears as a causal link rather than a direct measure.

**Links.** Papers link abstract reasoning to 5 constructs. One paper claims a causal relationship from code understanding to abstract reasoning, and another claims a causal relationship from symbolic reasoning to abstract reasoning, stating that emergent reasoning in neural networks depends on symbolic mechanisms. In the other direction, one paper claims a causal relationship from abstract reasoning to the linked behavioral indicator by integrating abstract reasoning into reflection to generate adaptive instruction. Abstract reasoning is also related to general reasoning, with one paper reporting a discrepancy between their performances, to geometric reasoning through the need for advanced spatial comprehension and abstract thinking, and to reasoning itself in an account that treats abstract reasoning as involving both abstraction and reasoning; no correlational link is reported.

## Sources

**Abstract reasoning** (10 papers: [Lemur: Integrating Large Language Models in Automated Program Verification](https://proceedings.iclr.cc/paper_files/paper/2024/file/0c86142265c5e2c900613dd1d031cb90-Paper-Conference.pdf), [MAmmoTH: Building Math Generalist Models through Hybrid Instruction Tuning](https://proceedings.iclr.cc/paper_files/paper/2024/file/b063829b922fdeb4fa3472dd3471ff43-Paper-Conference.pdf), [ToRA: A Tool-Integrated Reasoning Agent for Mathematical Problem Solving](https://proceedings.iclr.cc/paper_files/paper/2024/file/d3cf1559a8795eb1ed2b3ad52409ac7d-Paper-Conference.pdf), [LogiCity: Advancing Neuro-Symbolic AI with Abstract Urban Simulation](https://proceedings.neurips.cc/paper_files/paper/2024/file/8196be81e68289d7a9ece21ed7f5750a-Paper-Datasets_and_Benchmarks_Track.pdf), [Combining Induction and Transduction for Abstract Reasoning](https://proceedings.iclr.cc/paper_files/paper/2025/file/35ee921eb17e9b4c3e73b6e2ae0d55ba-Paper-Conference.pdf), [Instruct-of-Reflection: Enhancing Large Language Models Iterative Reflection Capabilities via Dynamic-Meta Instruction](https://aclanthology.org/2025.naacl-long.502.pdf), [IrokoBench: A New Benchmark for African Languages in the Age of Large Language Models](https://aclanthology.org/2025.naacl-long.139.pdf), [ACCESS : A Benchmark for Abstract Causal Event Discovery and Reasoning](https://aclanthology.org/2025.naacl-long.49.pdf), [The Surprising Effectiveness of Test-Time Training for Few-Shot Learning](https://raw.githubusercontent.com/mlresearch/v267/main/assets/akyurek25a/akyurek25a.pdf), [LMR-BENCH: Evaluating LLM Agent's Ability on Reproducing Language Modeling Research](https://aclanthology.org/2025.emnlp-main.314.pdf))
> The ability to reason about program properties and logic at a conceptual level, distinct from precise, step-by-step formal deduction.

**Abstract thinking** (2 papers: [ChartMimic: Evaluating LMM's Cross-Modal Reasoning Capability via Chart-to-Code Generation](https://proceedings.iclr.cc/paper_files/paper/2025/file/42806406dd99e30c3796bc98b2670fa2-Paper-Conference.pdf), [Forest for the Trees: Overarching Prompting Evokes High-Level Reasoning in Large Language Models](https://aclanthology.org/2025.naacl-long.66.pdf))
> The cognitive ability to work with concepts and principles independent of concrete instances, which is considered a prerequisite for demanding tasks like code generation.

**High-level reasoning** (1 paper: [Forest for the Trees: Overarching Prompting Evokes High-Level Reasoning in Large Language Models](https://aclanthology.org/2025.naacl-long.66.pdf))
> The latent ability of a model to reason from abstract, conceptual representations of a problem rather than from low-level details, enabling more robust and semantically precise inference.

**Advanced abstract reasoning** (1 paper: [Towards Robust Mathematical Reasoning](https://aclanthology.org/2025.emnlp-main.1794.pdf))
> The capacity to handle difficult combinatorial or other non-routine mathematical problems that require deeper abstraction and problem solving.

**Visual analogy solving** (1 paper: [VOILA: Evaluation of MLLMs For Perceptual Understanding and Analogical Reasoning](https://proceedings.iclr.cc/paper_files/paper/2025/file/adf17e7346b6be4c2f2bb40de572e5bc-Paper-Conference.pdf))
> Completing a visual analogy by inferring the missing image from a reference pair and an application pair.

## Relationships

### Abstract reasoning →
- **Iterative refinement** (behavioral indicator): *causes*, 1 paper
  > We propose Instruct-of-Reflection (IoRT), a dynamic iterative reflection framework that integrates abstract reasoning into the reflection process, generating adaptive instruction to regulate the iterative reflection. (§ 7)
  - [Instruct-of-Reflection: Enhancing Large Language Models Iterative Reflection Capabilities via Dynamic-Meta Instruction](https://aclanthology.org/2025.naacl-long.502.pdf)
- **ARC-AGI** (measurement instrument): *measured_by*, 1 paper
  > The Abstraction and Reasoning Corpus (ARC-AGI) poses a significant challenge for large language models (LLMs), exposing limitations in their abstract reasoning abilities. (Abstract)
  - [Product of Experts with LLMs: Boosting Performance on ARC Is a Matter of Perspective](https://raw.githubusercontent.com/mlresearch/v267/main/assets/franzen25a/franzen25a.pdf)
- **Bongard Problems** (measurement instrument): *measured_by*, 1 paper
  > “These visual puzzles test cognitive abilities in pattern recognition and abstract reasoning”
  - [Bongard in Wonderland: Visual Puzzles that Still Make AI Go Mad?](https://raw.githubusercontent.com/mlresearch/v267/main/assets/wust25a/wust25a.pdf)
- **Abstraction and Reasoning Corpus** (measurement instrument): *measured_by*, 1 paper
  > "The Abstraction and Reasoning Corpus (ARC) aims to evaluate the abstract reasoning capabilities of language models through their ability to solve visual puzzles."
  - [The Surprising Effectiveness of Test-Time Training for Few-Shot Learning](https://raw.githubusercontent.com/mlresearch/v267/main/assets/akyurek25a/akyurek25a.pdf)

### → Abstract reasoning
- **Code understanding** (construct): *causes*, 1 paper
  > This decomposition requires high-level reasoning that is difficult to automate using conventional formal methods, but plausibly could be performed by LLMs, with their documented code-understanding capability. (Section 2)
  - [Lemur: Integrating Large Language Models in Automated Program Verification](https://proceedings.iclr.cc/paper_files/paper/2024/file/0c86142265c5e2c900613dd1d031cb90-Paper-Conference.pdf)
- **Symbolic reasoning** (construct): *causes*, 1 paper
  > These results point toward a resolution of the longstanding debate between symbolic and neural network approaches, suggesting that emergent reasoning in neural networks depends on the emergence of symbolic mechanisms. (Abstract)
  - [Emergent Symbolic Mechanisms Support Abstract Reasoning in Large Language Models](https://raw.githubusercontent.com/mlresearch/v267/main/assets/yang25c/yang25c.pdf)

### Associated with
- **General reasoning** (construct), 1 paper
  > Our findings reveal a substantial discrepancy between their general reasoning and abstract reasoning performances. (Abstract)
  - [Meaningful Learning: Enhancing Abstract Reasoning in Large Language Models via Generic Fact Guidance](https://proceedings.neurips.cc/paper_files/paper/2024/file/da5498f88193ff61f0daea1940b819da-Paper-Conference.pdf)
- **Geometric reasoning** (construct), 1 paper
  > Geometric ability is a significant challenge for large language models (LLMs) due to the need for advanced spatial comprehension and abstract thinking.
  - [Do Large Language Models Truly Understand Geometric Structures?](https://proceedings.iclr.cc/paper_files/paper/2025/file/8de035590685bf7389da6a769fbcecce-Paper-Conference.pdf)
- **Reasoning** (construct), 1 paper
  > abstract reasoning involves two core processes: abstraction, the extraction of common features from concrete entities (Murphy, 2004), and reasoning, the derivation of new knowledge from existing information (Holyoak & Morrison, 2012).
  - [Benchmarking Abstract and Reasoning Abilities Through A Theoretical Perspective](https://raw.githubusercontent.com/mlresearch/v267/main/assets/ma25u/ma25u.pdf)
