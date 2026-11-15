# Polysemanticity
**Type:** Construct  
**Supporting papers:** 9  
**Also known as:** Neuronal entanglement  

## State of the Field

**Space of definitions.** Across the surveyed work, the prevailing usage describes polysemanticity as neurons activating for multiple, semantically distinct or unrelated concepts, features, or contexts, and papers commonly present this as making models harder to interpret. A smaller line broadens the locus from neurons to features, model components, or single attention heads that implement several distinct interpretable functions, and one definition further casts it as a latent property that increases representational capacity through distributed and overlapping feature encoding. Definitions mostly agree that multiple concepts are involved, and differ mainly on whether the term is applied narrowly to neurons or more broadly to other components, and on whether the emphasis is on interpretability limits or capacity.

**Space of facets.** Papers use the term across several representational units, most often neurons, but also features, broader model components, and attention heads. One paper treats neuronal entanglement as a manifestation of polysemanticity, defining it as the degree to which a neuron must separate similar input vectors into different output values, while another presents a popular model in which a neuron's activation is an OR of different concepts. In work on attention heads, polysemanticity appears as a single head exhibiting multiple interpretable behaviors, including a cited example where one head shows both successorship and acronym behavior.

**Space of measurement.** Papers do not link polysemanticity to any measurement instrument or behavioral indicator. No benchmark, human evaluation, LLM-as-a-judge setup, probe, or other measurement instrument is linked to it. Separately, one paper proposes the Wasserstein distance between a neuron's output distribution and a Gaussian as a metric of neuronal entanglement, which it presents as a manifestation of polysemanticity.

**Links.** A recurring connection is to Superposition: one paper claims a causal relationship from Superposition to Polysemanticity, describing superposition as a hypothesized cause, while another paper relates the two more generally. Other links appear in single papers: one paper relates polysemanticity to Interpretability and explainability, describing it as an obstacle to mechanistic interpretability, and one paper relates Polysemanticity to Redundancy, citing discussion of polysemantic code that favors redundancy for robustness.

## Sources

**Polysemanticity** (5 papers: [Sparse Autoencoders Find Highly Interpretable Features in Language Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/1fa1ab11f4bd5f94b2ec20e794dbfa3b-Paper-Conference.pdf), [Successor Heads: Recurring, Interpretable Attention Heads In The Wild](https://proceedings.iclr.cc/paper_files/paper/2024/file/2722a0ccf6acfe3d144fdbb0dedd80b5-Paper-Conference.pdf), [Monet: Mixture of Monosemantic Experts for Transformers](https://proceedings.iclr.cc/paper_files/paper/2025/file/382c35d1a57c07055dfcba58dd39e012-Paper-Conference.pdf), [Evaluating Neuron Explanations: A Unified Framework with Sanity Checks](https://raw.githubusercontent.com/mlresearch/v267/main/assets/oikarinen25a/oikarinen25a.pdf), [Polysemantic Dropout: Conformal OOD Detection for Specialized LLMs](https://aclanthology.org/2025.emnlp-main.595.pdf))
> The phenomenon where individual neurons in a neural network activate in multiple, semantically distinct contexts, hindering interpretability.

**Neuronal entanglement** (1 paper: [Wasserstein Distances, Neuronal Entanglement, and Sparsity](https://proceedings.iclr.cc/paper_files/paper/2025/file/e1c1624dd7d9fa75adacd7e93c40e6b2-Paper-Conference.pdf))
> The degree to which a neuron must differentiate between similar input vectors and map them to different output values, a manifestation of polysemanticity.

## Relationships

### → Polysemanticity
- **Superposition** (construct): *causes*, 2 papers
  > One hypothesised cause of polysemanticity is superposition, where neural networks represent more features than they have neurons by assigning features to an overcomplete set of directions in activation space, rather than to individual neurons. (Abstract)
  - [Sparse Autoencoders Find Highly Interpretable Features in Language Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/1fa1ab11f4bd5f94b2ec20e794dbfa3b-Paper-Conference.pdf)
  - [Mechanistic Permutability: Match Features Across Layers](https://proceedings.iclr.cc/paper_files/paper/2025/file/d1422213c9f2bdd5178b77d166fba86a-Paper-Conference.pdf)

### Associated with
- **Interpretability and explainability** (construct), 1 paper
  > A central obstacle to mechanistic interpretability is polysemanticity, where individual neurons encode multiple, unrelated concepts (Olah et al., 2020).
  - [Mixture of Experts Made Intrinsically Interpretable](https://raw.githubusercontent.com/mlresearch/v267/main/assets/yang25ag/yang25ag.pdf)
- **Redundancy** (construct), 1 paper
  > Marshall and Kirchner (2024) connect information theory with polysemanticity where polysemantic code learned by LLMs is not only efficient but also favors redundancy for robustness (Fig. 2 of their paper).
  - [Polysemantic Dropout: Conformal OOD Detection for Specialized LLMs](https://aclanthology.org/2025.emnlp-main.595.pdf)
