# Protein understanding
**Type:** Behavioral indicator  
**Supporting papers:** 9  
**Also known as:** Fitness prediction, Mutation effect prediction, Protein variant fitness prediction, Zero-shot fitness prediction, Protein fitness prediction, Iterative sequence editing, Binding prediction, Binding affinity prediction, Zero-shot prediction  

## State of the Field

**Space of definitions.** Across papers, the prevailing usage treats protein understanding as predicting protein fitness or mutational effects from amino acid sequences. Most definitions describe assigning a fitness score, scalar value, or relative ranking based on functional or biophysical properties, and several narrow this to the fitness impact of substitutions or other mutations. Some papers study zero-shot versions, though they differ in formulation: some define zero-shot as using no support-set examples for the target task, while others score mutated sequences relative to a wild type sequence without fine-tuning on labeled fitness data, using model likelihood differences or log odds ratios. A smaller line of work uses the same space for antibody-antigen interaction tasks, either classifying binding versus non-binding or predicting continuous binding affinity, and some work frames it as iteratively editing a seed sequence to propose higher-fitness variants.

**Variants.** Variants are named in several overlapping ways: fitness prediction, protein fitness prediction, protein variant fitness prediction, mutation effect prediction, and zero-shot fitness prediction or zero-shot prediction. Within these variants, papers study residue-based mutant fitness estimation, preference-based ranking of query sequences by fitness, and sequence editing that starts from a seed sequence and iteratively proposes improvements. Another branch focuses on antibody settings, with binding prediction for unknown antibodies and binding affinity prediction as separate classification and continuous-value tasks.

**Space of elicitation and scores.** Only one measurement instrument is explicitly linked to this behavior, ProteinGym, which papers describe as an established fitness-prediction benchmark. Beyond that instrument link, scoring varies by variant: fitness prediction can be evaluated as a regression task with a Spearman coefficient at sequence level, other formulations use scalar fitness values or preference-based rankings, and the binding variants are cast as binary classification or continuous affinity prediction.

**What it is taken as evidence of.** The construct links are split across two constructs rather than a single shared one. Some work relates this behavior to Representation quality, describing binding-prediction benchmarks as a way to assess the representation capabilities of antibody language models. Other work claims a causal relationship from Meta-learning to Protein understanding, reporting positive transfer from meta-learning over standard fitness prediction tasks to unseen fitness prediction tasks.

## Sources

**Fitness prediction** (1 paper: [Training Compute-Optimal Protein Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/8066ae1446b2bbccb5159587cc3b3bcc-Paper-Conference.pdf))
> A regression task to predict a protein's fitness, a measure of its functional performance.

**Protein variant fitness prediction** (1 paper: [Bio-xLSTM: Generative modeling, representation and in-context learning of biological and chemical sequences](https://proceedings.iclr.cc/paper_files/paper/2025/file/60cefc59610f8f59ea10099f99a36726-Paper-Conference.pdf))
> The task of predicting the functional effect or fitness impact of amino acid substitutions (mutations) in a protein sequence.

**Zero-shot fitness prediction** (1 paper: [Protein Language Model Fitness is a Matter of Preference](https://proceedings.iclr.cc/paper_files/paper/2025/file/62cf81a87f367758cebabce08e8d40d8-Paper-Conference.pdf))
> The observable task of assigning a score to a mutated protein sequence relative to a wild type sequence to predict its functional fitness, without any fine-tuning on labeled fitness data.

**Mutation effect prediction** (1 paper: [Protein Language Model Fitness is a Matter of Preference](https://proceedings.iclr.cc/paper_files/paper/2025/file/62cf81a87f367758cebabce08e8d40d8-Paper-Conference.pdf))
> The specific task of predicting the functional outcome of one or more mutations in a protein sequence, often as a log odds ratio.

**Protein fitness prediction** (2 papers: [Metalic: Meta-Learning In-Context with Protein Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/798095a4827e2ce739b16cf23acc876c-Paper-Conference.pdf), [AutoEval Done Right: Using Synthetic Data for Model Evaluation](https://raw.githubusercontent.com/mlresearch/v267/main/assets/boyeau25a/boyeau25a.pdf))
> The task of assigning a scalar value or a relative ranking to protein sequences based on their predicted biophysical or functional properties.

**Iterative sequence editing** (1 paper: [Data Distillation for extrapolative protein design through exact preference optimization](https://proceedings.iclr.cc/paper_files/paper/2025/file/a9ea92ef18aae17627d133534209e640-Paper-Conference.pdf))
> The observable process where a model proposes modifications to a given protein sequence to generate a new sequence with a predicted higher fitness value.

**Binding prediction** (1 paper: [A SARS-CoV-2 Interaction Dataset and VHH Sequence Corpus for Antibody Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/d2a1e47f7dc635fac77fbd6e2ec799e4-Paper-Datasets_and_Benchmarks_Track.pdf))
> The task of classifying whether a given antibody sequence will bind to a specific antigen, typically framed as a binary or multi-class classification problem.

**Binding affinity prediction** (1 paper: [A SARS-CoV-2 Interaction Dataset and VHH Sequence Corpus for Antibody Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/d2a1e47f7dc635fac77fbd6e2ec799e4-Paper-Datasets_and_Benchmarks_Track.pdf))
> The task of predicting a continuous value representing the strength or affinity of the binding interaction between an antibody and an antigen.

**Zero-shot prediction** (1 paper: [Metalic: Meta-Learning In-Context with Protein Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/798095a4827e2ce739b16cf23acc876c-Paper-Conference.pdf))
> Making fitness predictions without any support-set examples for the target task.

## Relationships

### Protein understanding →
- **ProteinGym** (measurement instrument): *measured_by*, 1 paper
  > our method sets a new state-of-the-art in low-data settings on ProteinGym, an established fitness-prediction benchmark. (ABSTRACT)
  - [Metalic: Meta-Learning In-Context with Protein Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/798095a4827e2ce739b16cf23acc876c-Paper-Conference.pdf)

### → Protein understanding
- **Meta-learning** (construct): *causes*, 1 paper
  > we propose meta-learning over a distribution of standard fitness prediction tasks, and demonstrate positive transfer to unseen fitness prediction tasks. (ABSTRACT)
  - [Metalic: Meta-Learning In-Context with Protein Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/798095a4827e2ce739b16cf23acc876c-Paper-Conference.pdf)

### Associated with
- **Representation quality** (construct), 1 paper
  > These results conﬁrm that AVIDa-SARS-CoV-2 provides valuable benchmarks for assessing the representation capabilities of antibody language models for binding prediction, thereby facilitating the development of AI-driven antibody discovery.
  - [A SARS-CoV-2 Interaction Dataset and VHH Sequence Corpus for Antibody Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/d2a1e47f7dc635fac77fbd6e2ec799e4-Paper-Datasets_and_Benchmarks_Track.pdf)
