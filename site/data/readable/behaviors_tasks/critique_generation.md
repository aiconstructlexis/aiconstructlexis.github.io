# Critique generation
**Type:** Behavioral indicator  
**Supporting papers:** 15  
**Also known as:** Providing feedback, Response critique, Correction suggestion generation, Chain-of-thought verification, Natural language critique, Single-response critique generation, Solution critique, Textual critique generation  

## State of the Field

**Space of definitions.** Across papers, the prevailing usage is the generation of natural language critique or feedback about a response, solution, or evaluation. Most descriptions combine identifying errors, weaknesses, or unfaithful spans with suggestions for fixes or improvement, and some also include strengths or an explicit correctness judgement; in "Teaching Language Models to Critique via Reinforcement Learning," the critique space includes strengths and weaknesses, actionable improvement suggestions, and a final judgement of correctness. Some papers narrow the behavior to criterion-grounded or evidence-grounded explanations, such as critiques that cite which parts of a document support or contradict a claim, or step-by-step verification before a Yes/No decision.

**Variants.** Papers study nearby variants under labels such as providing feedback, response critique, textual critique generation, solution critique, and chain-of-thought verification, among other names. The settings vary from collaborative exchanges where a critic agent assists another agent, to evaluator or judge setups conditioned on evaluation criteria, to factuality checking against a document, mathematical solution review, and table or dialogue refinement. Some formulations target a single response, while others compare candidate responses or critique intermediate reasoning before a final decision.

**Space of elicitation and scores.** No measurement instrument is linked to it. In these papers, the behavior is instead operationalized directly as generated textual feedback, critique, rationale, or suggestion.

**What it is taken as evidence of.** Papers do not converge on a single construct framing for what this behavior indicates. The recorded construct links are split across 2 constructs, and both are causal rather than measurement links: one paper claims a causal relationship from critique generation to Reasoning, stating that critiques help a policy language model correct flawed reasoning steps and improve refined responses, and another paper claims a causal relationship from critique generation to Robustness in complex and uncertain environments. Outside the construct links, one paper also claims a causal relationship from critique generation to Self-correction.

## Sources

**Critique generation** (6 papers: [Self-Generated Critiques Boost Reward Modeling for Language Models](https://aclanthology.org/2025.naacl-long.573.pdf), [MAMM-Refine: A Recipe for Improving Faithfulness in Generation with Multi-Agent Collaboration](https://aclanthology.org/2025.naacl-long.498.pdf), [Teaching Language Models to Critique via Reinforcement Learning](https://raw.githubusercontent.com/mlresearch/v267/main/assets/xie25a/xie25a.pdf), [Direct Judgement Preference Optimization](https://aclanthology.org/2025.emnlp-main.103.pdf), [Praetor: A Fine-Grained Generative LLM Evaluator with Instance-Level Customizable Evaluation Criteria](https://aclanthology.org/2025.acl-long.513.pdf), [Table-Critic: A Multi-Agent Framework for Collaborative Criticism and Refinement in Table Reasoning](https://aclanthology.org/2025.acl-long.853.pdf))
> The observable behavior of producing a textual explanation that identifies error spans in a generated sentence and suggests fixes.

**Providing feedback** (1 paper: [ACC-Collab: An Actor-Critic Approach to Multi-Agent LLM Collaboration](https://proceedings.iclr.cc/paper_files/paper/2025/file/e187897ed7780a579a0d76fd4a35d107-Paper-Conference.pdf))
> Generating critique or guidance on another agent's answer during a collaborative exchange.

**Response critique** (1 paper: [An Architecture Search Framework for Inference-Time Techniques](https://raw.githubusercontent.com/mlresearch/v267/main/assets/saad-falcon25a/saad-falcon25a.pdf))
> Producing strengths and weaknesses for candidate responses so they can be improved or selected.

**Correction suggestion generation** (1 paper: [Enhancing Goal-oriented Proactive Dialogue Systems via Consistency Reflection and Correction](https://aclanthology.org/2025.acl-long.1050.pdf))
> The observable behavior of a model, after identifying an inconsistency, generating a specific suggestion for how to improve or correct the output.

**Chain-of-thought verification** (1 paper: [Generative Verifiers: Reward Modeling as Next-Token Prediction](https://proceedings.iclr.cc/paper_files/paper/2025/file/214308a2d5e3f83ef9ad2739e1cbc46d-Paper-Conference.pdf))
> The observable behavior of a model generating an explicit, step-by-step rationale to critique a solution before making a final correctness judgment.

**Natural language critique** (1 paper: [Generative Judge for Evaluating Alignment](https://proceedings.iclr.cc/paper_files/paper/2024/file/747dc7c6566c74eb9a663bcd8d057c78-Paper-Conference.pdf))
> Generating structured, explanatory text that justifies an evaluation decision by referencing specific criteria and response content.

**Single-response critique generation** (1 paper: [Generative Judge for Evaluating Alignment](https://proceedings.iclr.cc/paper_files/paper/2024/file/747dc7c6566c74eb9a663bcd8d057c78-Paper-Conference.pdf))
> Producing a natural language critique that identifies shortcomings in a single model-generated response relative to the query and evaluation criteria.

**Solution critique** (1 paper: [LLaMA-Berry: Pairwise Optimization for Olympiad-level Mathematical Reasoning via O1-like Monte Carlo Tree Search](https://aclanthology.org/2025.naacl-long.375.pdf))
> Identifying flaws, errors, or inefficiencies in a generated mathematical solution through self-generated feedback.

**Textual critique generation** (2 papers: [Improving Model Factuality with Fine-grained Critique-based Evaluator](https://aclanthology.org/2025.acl-long.400.pdf), [Test-Time Preference Optimization: On-the-Fly Alignment via Iterative Textual Feedback](https://raw.githubusercontent.com/mlresearch/v267/main/assets/li25ac/li25ac.pdf))
> Producing natural language explanations that justify a factuality judgment for a claim, indicating which parts of the document support or contradict it.

## Relationships

### Critique generation →
- **Reasoning** (construct): *causes*, 1 paper
  > Additionally, these critiques help the policy language model (LM) correct flawed reasoning steps, resulting in improved accuracy in refined responses.
  - [Self-Generated Critiques Boost Reward Modeling for Language Models](https://aclanthology.org/2025.naacl-long.573.pdf)
- **Self-correction** (behavioral indicator): *causes*, 1 paper
  > Additional studies confirm the utility of generated critiques for Critic-RM in identifying and correcting mistakes made by LLMs.
  - [Self-Generated Critiques Boost Reward Modeling for Language Models](https://aclanthology.org/2025.naacl-long.573.pdf)
- **Robustness** (construct): *causes*, 1 paper
  > This mechanism enhances the model’s robustness in complex and uncertain environments and fosters a dynamic learning phase, facilitating continuous improvement through error identification and rectification. (Section 3.4.1)
  - [CARE: A Disagreement Detection Framework with Concept Alignment and Reasoning Enhancement](https://aclanthology.org/2025.emnlp-main.671.pdf)
