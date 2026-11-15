# Explanation faithfulness
**Type:** Construct  
**Supporting papers:** 5  
**Also known as:** Causal faithfulness  

## State of the Field

**Space of definitions.** Across the papers, usage splits between two closely related framings rather than converging on one. One framing, under the label causal faithfulness, treats it as how well a feature interpretation matches the feature's causal role in computation, so that features are "interpretable in a way consistent with their causal role" (Towards Principled Evaluations of Sparse Autoencoders for Interpretability and Control). Another framing treats explanation faithfulness as how accurately and reliably a textual explanation describes the behavior of a specific neural network unit, with the stated goal of evaluating "how faithfully this explanation describes the neuron" (Evaluating Neuron Explanations: A Unified Framework with Sanity Checks).

**Space of facets.** The main variation is in what is being evaluated and against what standard. One paper centers feature interpretations and whether they match causal role, while another centers textual explanations and whether they accurately describe a unit's behavior; the difference is between matching causal role and accurately describing behavior. In the unit-explanation framing, papers also discuss faithfulness alongside reliability, truthfulness, and trustworthiness when describing what such evaluations should establish.

**Space of measurement.** Papers do not link this construct to any measurement instrument or behavioral indicator. No recorded operationalization is attached to it.

## Sources

**Causal faithfulness** (1 paper: [Towards Principled Evaluations of Sparse Autoencoders for Interpretability and Control](https://proceedings.iclr.cc/paper_files/paper/2025/file/53356aebeea8ffd40a8ac3bb66243162-Paper-Conference.pdf))
> The extent to which a feature's interpretation matches its causal role in the model's computation.

**Explanation faithfulness** (1 paper: [Evaluating Neuron Explanations: A Unified Framework with Sanity Checks](https://raw.githubusercontent.com/mlresearch/v267/main/assets/oikarinen25a/oikarinen25a.pdf))
> The degree to which a textual explanation accurately and reliably describes the behavior of a specific neural network unit, such as a neuron.
