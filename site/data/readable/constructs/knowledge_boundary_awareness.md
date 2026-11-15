# Knowledge boundary awareness
**Type:** Construct  
**Supporting papers:** 25  
**Also known as:** Knowledge boundary cognition, Knowledge boundary perception, Knowledge boundary, Self-knowledge, Capability awareness, Knowledge awareness, Awareness of knowledge limits, Entity recognition  

## State of the Field

**Space of definitions.** Most definitions treat it as a latent ability or property by which a model recognizes the limits of its own knowledge, separating questions, statements, or entities that fall within its stored or parametric knowledge from those that do not. This prevailing usage appears under labels such as knowledge boundary cognition, perception, awareness, knowledge awareness, and self-knowledge, and is commonly tied to appropriate uncertainty, declining to answer, or avoiding overconfident unsupported claims. A smaller line narrows the construct to specific settings, such as factual question answering, multimodal questions that need knowledge not shown in the image, or entity-level recognition of whether the model can recall facts. The main definitional shift is between the model's internal awareness and the boundary itself, which some papers describe as an unobservable limit or internal scope of factual understanding, sometimes referenced to parametric knowledge, outward verification, or universal human knowledge.

**Space of facets.** Papers use multiple labels for overlapping ideas, with knowledge boundary cognition, perception, awareness, knowledge awareness, self-knowledge, and awareness of knowledge limits all centering on knowing what is known versus unknown. Some works place it inside broader frameworks, treating capability awareness as a facet of self-awareness and knowledge awareness as a fine-grained type under epistemic uncertainty awareness. Another line decomposes the boundary itself into outward, parametric, and universal knowledge boundaries, with one subsuming another, while narrower variants isolate awareness of knowledge limits as one cognition level, pair it with knowledge acquisition direction, or focus on entity recognition at the entity token.

**Space of measurement.** No measurement instrument is linked to it, and papers link it to 3 behavioral indicators: hallucination, abstention, and confidence estimation. Papers operationalize it with probes and analyses of internal states, for example testing whether hidden activations or middle to middle-upper layers distinguish known from unknown questions, including across languages, and with confidence-oriented procedures such as reasoning step confidence calibration or consistency-based calibration under question reformulation. Other papers assess it through semi-open-ended question answering, sampling-based inference to depict a model's boundary, and role-guided self-reflection, so operationalization spans both internal-state detection and outward behaviors like uncertainty expression or declining to answer.

**Links.** A few papers claim a causal relationship from knowledge boundary awareness to hallucination: one says the model may begin to hallucinate beyond its boundary of factual understanding, and another says enhancing knowledge boundary awareness reduces hallucination. Beyond that, papers report 4 related constructs and 2 related behavioral indicators. In the recorded direction, it is related to self-awareness and one additional construct, while epistemic uncertainty awareness, confidence estimation, abstention, and one other construct are related to it.

## Sources

**Knowledge boundary cognition** (1 paper: [Analyzing LLMs' Knowledge Boundary Cognition Across Languages Through the Lens of Internal Representations](https://aclanthology.org/2025.acl-long.1174.pdf))
> The latent ability of an LLM to internally recognize whether a given question or statement falls within or beyond its stored knowledge, enabling discrimination between known and unknown information across languages.

**Knowledge boundary perception** (1 paper: [Towards Fully Exploiting LLM Internal States to Enhance Knowledge Boundary Perception](https://aclanthology.org/2025.acl-long.1184.pdf))
> The latent ability of an LLM to accurately recognize the limits of its own knowledge, distinguishing between what it knows and does not know.

**Knowledge boundary awareness** (2 papers: [MMBoundary: Advancing MLLM Knowledge Boundary Awareness through Reasoning Step Confidence Calibration](https://aclanthology.org/2025.acl-long.802.pdf), [MAC-Tuning: LLM Multi-Compositional Problem Reasoning with Enhanced Knowledge Boundary Awareness](https://aclanthology.org/2025.emnlp-main.35.pdf))
> The latent ability of a model to recognize the limits of its own knowledge during reasoning, enabling it to express uncertainty where appropriate and avoid overconfident incorrect assertions.

**Knowledge awareness** (2 papers: [FacLens: Transferable Probe for Foreseeing Non-Factuality in Fact-Seeking Question Answering of Large Language Models](https://aclanthology.org/2025.emnlp-main.937.pdf), [CertainlyUncertain: A Benchmark and Metric for Multimodal Epistemic and Aleatoric Awareness](https://proceedings.iclr.cc/paper_files/paper/2025/file/21b5788d81f886ff81671379b4ff9453-Paper-Conference.pdf))
> The latent ability of an LLM to implicitly recognize whether it possesses the factual knowledge required to correctly answer a given question, as evidenced by patterns in its internal representations prior to response generation.

**Knowledge boundary** (2 papers: [Detecting Knowledge Boundary of Vision Large Language Models by Sampling-Based Inference](https://aclanthology.org/2025.emnlp-main.1458.pdf), [Perception of Knowledge Boundary for Large Language Models through Semi-open-ended Question Answering](https://proceedings.neurips.cc/paper_files/paper/2024/file/a1e0d6fa0c30b7d4f75dd9c7ed6189f2-Paper-Conference.pdf))
> The latent property of a VLLM that determines whether a given query falls within the model's internal knowledge scope, distinguishing between what the model knows and what requires external retrieval.

**Self-knowledge** (1 paper: [Evaluating Large Language Models through Role-Guide and Self-Reflection: A Comparative Study](https://proceedings.iclr.cc/paper_files/paper/2025/file/0b8705a611ed1ce19cdb759031078705-Paper-Conference.pdf))
> The ability of a model to accurately assess its own internal knowledge, distinguishing between what it knows and what it does not, to avoid making false or unsupported claims.

**Capability awareness** (1 paper: [Position: LLMs Need a Bayesian Meta-Reasoning Framework for More Robust and Generalizable Reasoning](https://raw.githubusercontent.com/mlresearch/v267/main/assets/yan25g/yan25g.pdf))
> A facet of self-awareness concerning the model's ability to accurately assess its own knowledge and skills for a given task.

**Awareness of knowledge limits** (1 paper: [Right this way: Can VLMs Guide Us to See More to Answer Questions?](https://proceedings.neurips.cc/paper_files/paper/2024/file/efe4e50d492fedc0dfd2959f3320a974-Paper-Conference.pdf))
> A metacognitive ability to recognize when the model lacks sufficient information to answer a question accurately, representing the 'knowing what's unknown' level of cognition.

**Entity recognition** (1 paper: [Do I Know This Entity? Knowledge Awareness and Hallucinations in Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/c1c44e46358e0fb94dc94ec495a7fb1a-Paper-Conference.pdf))
> The latent capacity to distinguish entities the model recognizes from entities it does not recognize, especially from internal representations at the entity token.

## Relationships

### Knowledge boundary awareness →
- **Hallucination** (behavioral indicator): *causes*, 2 papers
  > “The knowledge boundary of an LLM limits its factual understanding, beyond which it may begin to hallucinate.”
  - [Perception of Knowledge Boundary for Large Language Models through Semi-open-ended Question Answering](https://proceedings.neurips.cc/paper_files/paper/2024/file/a1e0d6fa0c30b7d4f75dd9c7ed6189f2-Paper-Conference.pdf)
  - [MAC-Tuning: LLM Multi-Compositional Problem Reasoning with Enhanced Knowledge Boundary Awareness](https://aclanthology.org/2025.emnlp-main.35.pdf)

### Associated with
- **Believability** (construct), 1 paper
  > For the agent evaluation, we perform a controlled evaluation to test whether the agents produce believable individual behaviors, where the self-knowledge, reaction and general abilities are evaluated. (Section 1)
  - [RoleAgent: Building, Interacting, and Benchmarking High-quality Role-Playing Agents from Scripts](https://proceedings.neurips.cc/paper_files/paper/2024/file/5875aca1ef70285a35940afbbce0f9fb-Paper-Datasets_and_Benchmarks_Track.pdf)
- **Epistemic uncertainty awareness** (construct), 1 paper
  > “We further categorize the awareness of epistemic uncertainty into 3 finegrained types: • Knowledge awareness means understanding that some questions require information or common sense that is not shown in the image.”
  - [CertainlyUncertain: A Benchmark and Metric for Multimodal Epistemic and Aleatoric Awareness](https://proceedings.iclr.cc/paper_files/paper/2025/file/21b5788d81f886ff81671379b4ff9453-Paper-Conference.pdf)
- **Self-awareness** (construct), 1 paper
  > Our self-awareness module (Fig. 3) comprises two core components...: (1) assessing the task’s solvability p(ΘI) and p(ΘE), based on the model’s technic and cognitive capabilities, where capability-aware solvability and mission-aware solvability are considered simultaneously
  - [Position: LLMs Need a Bayesian Meta-Reasoning Framework for More Robust and Generalizable Reasoning](https://raw.githubusercontent.com/mlresearch/v267/main/assets/yan25g/yan25g.pdf)
- **Confidence estimation** (behavioral indicator), 1 paper
  > While assessing capability-aware solvability of LLMs is underexplored, confidence or uncertainty estimation (Geng et al., 2024; Wen et al., 2024) offers a viable alternative.
  - [Position: LLMs Need a Bayesian Meta-Reasoning Framework for More Robust and Generalizable Reasoning](https://raw.githubusercontent.com/mlresearch/v267/main/assets/yan25g/yan25g.pdf)
- **Overconfidence** (construct), 1 paper
  > Overconfidence is a fraction of incorrect answers where the method was confident about self-knowledge reflecting how often the method incorrectly assumes that the model possesses the required knowledge when it does not.
  - [Adaptive Retrieval Without Self-Knowledge? Bringing Uncertainty Back Home](https://aclanthology.org/2025.acl-long.319.pdf)
- **Abstention** (behavioral indicator), 1 paper
  > To address the critical limitation of RAFT models regarding their inability to abstain from answering when queries fall outside both knowledge boundaries (✘✘), we construct a comprehensive preference dataset that captures the desired behavior for each quadrant. (Section 5)
  - [Divide-Then-Align: Honest Alignment based on the Knowledge Boundary of RAG](https://aclanthology.org/2025.acl-long.561.pdf)
