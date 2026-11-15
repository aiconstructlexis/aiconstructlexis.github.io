# Parity checking
**Type:** Behavioral indicator  
**Supporting papers:** 12  
**Also known as:** Parity, Parity computation, Parity solving, Parity task  

## State of the Field

**Space of definitions.** Across the definitions, the prevailing usage treats parity checking as producing the parity result for a binary input, usually deciding whether a bit sequence contains an odd or even number of 1s. Closely related formulations describe it as computing the sum modulo 2 of boolean variables, and one paper states this as the parity of a sequence being 1 when the number of ones is odd and 0 when it is even. A narrower formulation presents a trivial version in which intermediate results are stored every other token, so the output is only a function of the last two tokens.

**Variants.** Papers use several nearby names, including Parity, Parity checking, Parity computation, Parity solving, and Parity task. The most common setting is a binary string or bit sequence whose output is the parity check result, while another formulation uses tuples of boolean variables and explicitly computes expressions such as a variable sum modulo 2. Some authors also frame it as a synthetic benchmark, and one paper studies a restricted version where the intermediate state is arranged so that only the last two tokens determine the answer.

**Space of elicitation and scores.** No measurement instrument is linked to it. In practice, the papers operationalize it through the model's produced parity label or modulo 2 answer for a binary sequence or boolean tuple. Separately, one paper claims a causal relationship from Chain of thought to parity checking, stating that difficulty on longer inputs is resolved by a CoT consisting of the parities of increasing prefixes.

**What it is taken as evidence of.** Only one construct is linked in the recorded relationships. Rather than converging on several construct interpretations, one paper reports that parity checking is related to State tracking ability, using tests on parity alongside other tasks to demonstrate improved state-tracking performance.

## Sources

**Parity** (1 paper: [Selective Attention Improves Transformer](https://proceedings.iclr.cc/paper_files/paper/2025/file/0cf3e7eefb9d643e93e16ff1d94090a7-Paper-Conference.pdf))
> A trivial task where the model's output is only a function of the last two tokens, with intermediate results stored every other token.

**Parity checking** (1 paper: [Looped Transformers for Length Generalization](https://proceedings.iclr.cc/paper_files/paper/2025/file/25cc3adf8c85f7c70989cb8a97a691a7-Paper-Conference.pdf))
> Producing the parity result for a binary input sequence.

**Parity computation** (1 paper: [Connecting the Dots: LLMs can Infer and Verbalize Latent Structure from Disparate Training Data](https://proceedings.neurips.cc/paper_files/paper/2024/file/fe489a28a54583ee802b8e2955c024c2-Paper-Conference.pdf))
> Calculating the sum modulo 2 of a tuple of boolean variables.

**Parity solving** (1 paper: [Unlocking State-Tracking in Linear RNNs Through Negative Eigenvalues](https://proceedings.iclr.cc/paper_files/paper/2025/file/5a0ce3abb720b740419e193c87afd080-Paper-Conference.pdf))
> Computing whether the total number of ones in a binary sequence is odd or even.

**Parity task** (1 paper: [How Far Can Transformers Reason? The Globality Barrier and Inductive Scratchpad](https://proceedings.neurips.cc/paper_files/paper/2024/file/3107e4bdb658c79053d7ef59cbc804dd-Paper-Conference.pdf))
> A synthetic benchmark where the model determines whether the number of 1s in a bit sequence is even or odd.

## Relationships

### → Parity checking
- **Chain of thought** (behavioral indicator): *causes*, 1 paper
  > Transformers empirically struggle to learn it on longer inputs (e.g. Bhattamishra et al., 2020a; Del´etang et al., 2023; Butoi et al., 2024; Hahn & Rofin, 2024), and this difficulty is resolved by a CoT consisting of the parities of increasing prefixes, as in Figure 1 (e.g. Anil et al., 2022). (Section 1)
  - [Lower Bounds for Chain-of-Thought Reasoning in Hard-Attention Transformers](https://raw.githubusercontent.com/mlresearch/v267/main/assets/bavandpour25a/bavandpour25a.pdf)

### Associated with
- **State tracking ability** (construct), 1 paper
  > We test the modified methods on parity, modular arithmetic, and permutation composition, demonstrating improved state-tracking performance.
  - [Unlocking State-Tracking in Linear RNNs Through Negative Eigenvalues](https://proceedings.iclr.cc/paper_files/paper/2025/file/5a0ce3abb720b740419e193c87afd080-Paper-Conference.pdf)
