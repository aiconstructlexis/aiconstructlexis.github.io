# Context faithfulness
**Type:** Construct  
**Supporting papers:** 16  
**Also known as:** Contextual faithfulness, Context-faithfulness, Sensitivity to contextual knowledge, Knowledge sensitivity, Context fidelity, Source fidelity, Long-context factuality, Context-grounded reasoning, Contextual grounding  

## State of the Field

**Space of definitions.** Across papers, the prevailing usage treats context faithfulness as a model ability or degree of alignment in which outputs remain accurate, consistent, and grounded in provided context, avoiding unsupported, contradictory, irrelevant, or fabricated content. Most definitions also stress reliance on contextual information when it conflicts with internal or parametric knowledge, sometimes phrased as sensitivity to contextual knowledge rather than internal knowledge. Smaller variants narrow the reference point to source documents or long input contexts, or describe the same general idea as context-grounded reasoning.

**Space of facets.** Papers use several overlapping names for closely similar formulations, most often contextual faithfulness or context-faithfulness, but also context fidelity, source fidelity, sensitivity to contextual knowledge, and several narrower labels. The main axis of variation is scope: some papers speak broadly about provided context, while others restrict it to source documents, long-context settings, question-answering, or dialogue history. A recurring contrast places external context against internal or parametric knowledge, and one paper marks unfaithfulness at the sentence level, defining a response as unfaithful if any sentence contradicts or cannot be verified from the retrieved document.

**Space of measurement.** Papers link context faithfulness to 4 measurement instruments, led by NQ-Swap, CounterFact, and FaithEval, plus one other instrument. These are used as benchmark-style evaluations of whether a model relies on provided evidence or counterfactual context: NQ-Swap is described as testing the ability to identify and rely on the correct evidence, CounterFact as requiring the model to answer using provided counterfactual context, and FaithEval as a benchmark for faithfulness in contextual scenarios. Assessment is also tied to 3 behavioral indicators, most often Knowledge editing and Multi-hop question answering, with one other linked indicator; papers use knowledge-editing success rates and edited multi-hop QA accuracy to assess the construct. Overall, the measurements mostly match the prevailing definition, because they operationalize adherence to provided context, often under knowledge conflict.

**Links.** One paper claims a causal relationship from Factuality to context faithfulness, reporting that current factuality enhancement methods can undermine context-faithfulness; the same paper claims a causal relationship from Overconfidence to context faithfulness, describing overconfidence as producing setbacks for it. Papers also relate context faithfulness to Knowledge editing, Multi-hop question answering, and Self-verification: knowledge-editing success rate is used to assess it, a multi-hop editing task measures it through edited QA accuracy, and one dialogue-related or context-grounded reasoning setup discusses it for effective self-verification.

## Sources

**Contextual faithfulness** (3 papers: [Improving Contextual Faithfulness of Large Language Models via Retrieval Heads-Induced Optimization](https://aclanthology.org/2025.acl-long.826.pdf), [Continuously Steering LLMs Sensitivity to Contextual Knowledge with Proxy Models](https://aclanthology.org/2025.emnlp-main.233.pdf), [FaithEval: Can Your Language Model Stay Faithful to Context, Even If "The Moon is Made of Marshmallows"](https://proceedings.iclr.cc/paper_files/paper/2025/file/48404cd9ce03946c6b7177691f3267a1-Paper-Conference.pdf))
> The latent ability of a model to generate responses that are fully supported by and consistent with the provided contextual information, avoiding hallucinations or unsupported claims.

**Context-faithfulness** (2 papers: [Exploiting Contextual Knowledge in LLMs through V-usable Information based Layer Enhancement](https://aclanthology.org/2025.acl-long.1531.pdf), [Is Factuality Enhancement a Free Lunch For LLMs? Better Factuality Can Lead to Worse Context-Faithfulness](https://proceedings.iclr.cc/paper_files/paper/2025/file/660d0ed5885662219244b6e44aba8fe3-Paper-Conference.pdf))
> The latent ability of a model to generate responses that accurately reflect the provided contextual information, especially when it conflicts with the model's parametric knowledge.

**Context faithfulness** (1 paper: [Understanding and Leveraging the Expert Specialization of Context Faithfulness in Mixture-of-Experts LLMs](https://aclanthology.org/2025.emnlp-main.1114.pdf))
> The ability of a model to accurately ground its generated output in the provided contextual information, avoiding irrelevant or unsupported content.

**Sensitivity to contextual knowledge** (1 paper: [Continuously Steering LLMs Sensitivity to Contextual Knowledge with Proxy Models](https://aclanthology.org/2025.emnlp-main.233.pdf))
> The degree to which a language model adjusts its output to align with information provided in the context, especially when that information conflicts with its internal knowledge.

**Context fidelity** (1 paper: [Improving Context Fidelity via Native Retrieval-Augmented Reasoning](https://aclanthology.org/2025.emnlp-main.1075.pdf))
> The degree to which a model's answers remain grounded in and consistent with the provided input context rather than contradicting or fabricating information.

**Source fidelity** (1 paper: [Stronger Baselines for Retrieval-Augmented Generation with Long-Context Language Models](https://aclanthology.org/2025.emnlp-main.1656.pdf))
> The degree to which a model's outputs accurately reflect and are grounded in the provided source documents, without introducing unsupported information.

**Long-context factuality** (1 paper: [Retrieval Head Mechanistically Explains Long-Context Factuality](https://proceedings.iclr.cc/paper_files/paper/2025/file/9b77f07301b1ef1fe810aae96c12cb7b-Paper-Conference.pdf))
> The degree to which a model's outputs are faithful to the information presented in a long input context, as opposed to generating fabricated content.

**Context-grounded reasoning** (1 paper: [AutoMix: Automatically Mixing Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/ecda225cb187b40ea8edc1f46b03ffda-Paper-Conference.pdf))
> The ability to generate accurate and coherent answers that are consistent with a provided context, such as a document or dialogue history.

**Contextual grounding** (1 paper: [CoCoA: Confidence- and Context-Aware Adaptive Decoding for Resolving Knowledge Conflicts in Large Language Models](https://aclanthology.org/2025.emnlp-main.348.pdf))
> The model's capacity to align its output with the evidence present in the external context, particularly when that context contradicts its prior beliefs.

## Relationships

### Context faithfulness →
- **NQ-Swap** (measurement instrument): *measured_by*, 2 papers
  > we also include two counter-factual QA benchmarks: NQ-Swap and ConfiQA, offering a more challenging and complementary evaluation of a model’s ability to identify and rely on the correct evidence. (Section 3.2)
  - [Understanding and Leveraging the Expert Specialization of Context Faithfulness in Mixture-of-Experts LLMs](https://aclanthology.org/2025.emnlp-main.1114.pdf)
  - [In-Context Pretraining: Language Modeling Beyond Document Boundaries](https://proceedings.iclr.cc/paper_files/paper/2024/file/a1fe2365abdb691332537990a6385909-Paper-Conference.pdf)
- **FaithEval** (measurement instrument): *measured_by*, 1 paper
  > “we introduce FaithEval, a novel and comprehensive benchmark tailored to evaluate the faithfulness of LLMs in contextual scenarios”
  - [FaithEval: Can Your Language Model Stay Faithful to Context, Even If "The Moon is Made of Marshmallows"](https://proceedings.iclr.cc/paper_files/paper/2025/file/48404cd9ce03946c6b7177691f3267a1-Paper-Conference.pdf)
- **MQuAKE** (measurement instrument): *measured_by*, 1 paper
  > "We use LLAMA2-7B-CHAT and LLAMA2-13B-CHAT as baseline models to conduct experiments on MQUAKE ... This verifies whether knowledge has been properly edited and effectively demonstrates LLMs’ context-faithfulness."
  - [Is Factuality Enhancement a Free Lunch For LLMs? Better Factuality Can Lead to Worse Context-Faithfulness](https://proceedings.iclr.cc/paper_files/paper/2025/file/660d0ed5885662219244b6e44aba8fe3-Paper-Conference.pdf)
- **CounterFact** (measurement instrument): *measured_by*, 1 paper
  > we also conduct experiments on the CounterFact dataset (Meng et al., 2022), where the model must rely on the provided counterfactual context to answer a simple question correctly. The task does not require complex reasoning, making it well-suited for isolating and evaluating the role of context-faithful experts. (Section 3.3)
  - [Understanding and Leveraging the Expert Specialization of Context Faithfulness in Mixture-of-Experts LLMs](https://aclanthology.org/2025.emnlp-main.1114.pdf)

### → Context faithfulness
- **Factuality** (construct): *causes*, 1 paper
  > current factuality enhancement methods can significantly undermine the context-faithfulness of LLMs. (Section 1)
  - [Is Factuality Enhancement a Free Lunch For LLMs? Better Factuality Can Lead to Worse Context-Faithfulness](https://proceedings.iclr.cc/paper_files/paper/2025/file/660d0ed5885662219244b6e44aba8fe3-Paper-Conference.pdf)
- **Overconfidence** (construct): *causes*, 1 paper
  > overconfidence, resulting in a substantial setback for the context-faithfulness of LLMs. (Section 1)
  - [Is Factuality Enhancement a Free Lunch For LLMs? Better Factuality Can Lead to Worse Context-Faithfulness](https://proceedings.iclr.cc/paper_files/paper/2025/file/660d0ed5885662219244b6e44aba8fe3-Paper-Conference.pdf)

### Associated with
- **Self-verification** (behavioral indicator), 1 paper
  > Furthermore, AutoMix is designed with a dialogue-related or context-grounded reasoning setup in mind for effective self-verification, which does not include tasks like factual question-answering and commonsense reasoning. (Section 6)
  - [AutoMix: Automatically Mixing Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/ecda225cb187b40ea8edc1f46b03ffda-Paper-Conference.pdf)
- **Knowledge editing** (behavioral indicator), 1 paper
  > this paper uses the success rate of KE to assess the context-faithfulness of LLMs (Section 2.2)
  - [Is Factuality Enhancement a Free Lunch For LLMs? Better Factuality Can Lead to Worse Context-Faithfulness](https://proceedings.iclr.cc/paper_files/paper/2025/file/660d0ed5885662219244b6e44aba8fe3-Paper-Conference.pdf)
- **Multi-hop question answering** (behavioral indicator), 1 paper
  > We adopt a multi-hop editing task to measure context-faithfulness of LLMs in Section 4 by evaluating the accuracy of multi-hop question answering with fact edits. (Section 2.2)
  - [Is Factuality Enhancement a Free Lunch For LLMs? Better Factuality Can Lead to Worse Context-Faithfulness](https://proceedings.iclr.cc/paper_files/paper/2025/file/660d0ed5885662219244b6e44aba8fe3-Paper-Conference.pdf)
