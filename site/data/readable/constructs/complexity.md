# Complexity
**Type:** Construct  
**Supporting papers:** 5  

## State of the Field

**Space of definitions.** Across the cited work, the prevailing usage treats complexity as a response-level dimension, defined as the level of sophistication, depth, intricacy, or elaboration in a model-generated response. The definitions are closely aligned rather than contested: one emphasizes sophistication, depth, and intricacy, and another frames complexity as the degree of elaboration or sophistication used as a rating dimension in preference annotation.

**Space of facets.** Papers do not break complexity into subtypes or offer competing taxonomies. Instead, they place it in a recurring bundle with helpfulness, correctness, coherence, and verbosity, describing these collectively as reward attributes or as aspects used in preference annotation.

**Space of measurement.** Operationally, complexity is linked to one measurement instrument and no behavioral indicators. The only named instrument is HelpSteer, described as a model alignment and steering dataset, and papers use it to score complexity alongside helpfulness, correctness, coherence, and verbosity, so the operationalization treats complexity as a directly rated response attribute.

**Links.** Beyond measurement, one paper reports that complexity correlates with helpfulness: lower Pearson's R values for complexity in HelpSteer2 are described as indicating that annotators were less influenced by response complexity when assessing overall helpfulness. No papers report a causal relationship or a generic related link involving complexity.

## Sources

**Complexity** (2 papers: [Decoding-Time Language Model Alignment with Multiple Objectives](https://proceedings.neurips.cc/paper_files/paper/2024/file/57c89126d60c209f48d0e6395c766bb3-Paper-Conference.pdf), [RuleAdapter: Dynamic Rules for training Safety Reward Models in RLHF](https://raw.githubusercontent.com/mlresearch/v267/main/assets/li25o/li25o.pdf))
> The level of sophistication, depth, or intricacy in the model's generated response.

## Relationships

### Complexity →
- **HelpSteer** (measurement instrument): *measured_by*, 2 papers
  > For HelpSteer, we use https://huggingface.co/Haoxiang-Wang/ RewardModel-Mistral-7B-for-DPA-v1 for all attributes of rewards, including helpfulness, correctness, coherence, complexity and verbosity.
  - [Decoding-Time Language Model Alignment with Multiple Objectives](https://proceedings.neurips.cc/paper_files/paper/2024/file/57c89126d60c209f48d0e6395c766bb3-Paper-Conference.pdf)
  - [Learning Goal-Conditioned Representations for Language Reward Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/d46f127a80dc58cbc0732a717285c43a-Paper-Conference.pdf)
- **Helpfulness** (construct): *correlates*, 1 paper
  > Additionally, the Pearson’s R values for both complexity (0.2361 to 0.1805) and verbosity (0.2555 to 0.0600) have decreased, indicating that annotators are less influenced by the complexity and verbosity of responses when assessing overall helpfulness in HelpSteer2.
  - [HelpSteer 2: Open-source dataset for training top-performing reward models](https://proceedings.neurips.cc/paper_files/paper/2024/file/02fd91a387a6a5a5751e81b58a75af90-Paper-Datasets_and_Benchmarks_Track.pdf)
