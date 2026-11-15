# Generation diversity
**Type:** Construct  
**Supporting papers:** 87  
**Also known as:** Diversity, Content diversity, Response diversity, Prediction diversity, Solution diversity, Plan diversity, Output diversity  

## State of the Field

**Space of definitions.** Across papers, the prevailing usage treats generation diversity as variety across a model's outputs, usually the extent to which generations are distinct and non-repetitive rather than mode-collapsed, often described through varied vocabulary, unique n-grams, or multiple different responses to the same prompt. Some papers broaden this to semantic, structural, syntactic, or logical variation, and one paper explicitly adds linguistic complexity and coverage of the real data distribution. A smaller line of work uses the same label for diversity across collections of texts, across ensemble predictions, across solution or plan paths, or for balanced yes and no perspectives in summaries, so definitions differ on whether the property belongs to sampled outputs, datasets, or broader search and representation coverage.

**Space of facets.** Papers most often use diversity, generation diversity, response diversity, output diversity, and content diversity as neighboring labels, usually for varied and non-repetitive generations. One paper breaks generation diversity into three aspects, multiple distinct responses for a prompt, linguistically complex responses, and coverage of the real data distribution, while other papers break it into lexical, semantic, structural, syntactic, or logical variety, or into diverse reasoning chains, plans, and solutions. The same name is also used more narrowly for prediction diversity across ensembled models and more broadly for support-set or task coverage in latent space, so adjacent terms are not fully separated.

**Space of measurement.** No measurement instrument is linked to it, and papers link it to 8 behavioral indicators. In practice, authors usually operationalize it with automatic analyses of repeated or similar generations, most often Distinct-n or other unique n-gram and repetition measures, followed by Self-BLEU, predictive entropy across multiple sampled responses, cosine or sentence-embedding similarity among generations, and LLM-evaluator judgments; other papers mention lexical-translation consistency or ROUGE-L proxies. These operationalizations generally match the dominant anti-repetition framing, though some extend measurement to semantic variety, structural variety, or balance between opposing perspectives.

**Links.** Several papers connect generation diversity to mode collapse and text generation quality: one paper claims a causal relationship from mode collapse to generation diversity, while other papers relate reduced diversity to mode collapse, and several papers relate generation diversity to text generation quality in trade-off terms. Single papers also claim causal relationships from generation diversity to catastrophic forgetting and alignment tax, with the recorded evidence framing preserved diversity as mitigating forgetting and suppressed alternatives as leading to alignment tax, and another paper claims a causal relationship from self-improvement to generation diversity. Across relationships, it is linked to 13 constructs and 8 behavioral indicators through other related, causal, and one correlational claim.

## Sources

**Diversity** (9 papers: [Transfer Q-star : Principled Decoding for LLM Alignment](https://proceedings.neurips.cc/paper_files/paper/2024/file/b8700a8a005032fe869c741b0a75274b-Paper-Conference.pdf), [Combatting Dimensional Collapse in LLM Pre-Training Data via Submodular File Selection](https://proceedings.iclr.cc/paper_files/paper/2025/file/136729ae4b0fee25a0d28077442506da-Paper-Conference.pdf), [MoDS: Moderating a Mixture of Document Speakers to Summarize Debatable Queries in Document Collections](https://aclanthology.org/2025.naacl-long.20.pdf), [Active Few-Shot Learning for Text Classification](https://aclanthology.org/2025.naacl-long.340.pdf), [ToolFlow: Boosting LLM Tool-Calling Through Natural and Coherent Dialogue Synthesis](https://aclanthology.org/2025.naacl-long.214.pdf), [VTechAGP: An Academic-to-General-Audience Text Paraphrase Dataset and Benchmark Models](https://aclanthology.org/2025.naacl-long.311.pdf), [Generating Diverse Training Samples for Relation Extraction with Large Language Models](https://aclanthology.org/2025.acl-long.35.pdf), [Language Models as Implicit Tree Search](https://raw.githubusercontent.com/mlresearch/v267/main/assets/chen25ag/chen25ag.pdf), [Biased Tales: Cultural and Topic Bias in Generating Children's Stories](https://aclanthology.org/2025.emnlp-main.3.pdf))
> The extent to which generated text varies in wording and avoids repetitive n-gram patterns across outputs.

**Content diversity** (1 paper: [Does Writing with Language Models Reduce Content Diversity?](https://proceedings.iclr.cc/paper_files/paper/2024/file/02dec8877fb7c6aa9a79f81661baca7c-Paper-Conference.pdf))
> The degree to which written content varies in lexical expressions and key ideas across a collection of texts, reflecting the range of unique perspectives and phrasings present.

**Generation diversity** (6 papers: [Beyond Reverse KL: Generalizing Direct Preference Optimization with Diverse Divergence Constraints](https://proceedings.iclr.cc/paper_files/paper/2024/file/2b1d1e5affe5fdb70372cd90dd8afd49-Paper-Conference.pdf), [MiniLLM: Knowledge Distillation of Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/8ac015d409635f196f9e3e9dcfb9a94e-Paper-Conference.pdf), [On-Policy Distillation of Language Models: Learning from Self-Generated Mistakes](https://proceedings.iclr.cc/paper_files/paper/2024/file/5be69a584901a26c521c2b51e40a4c20-Paper-Conference.pdf), [Correlation and Navigation in the Vocabulary Key Representation Space of Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/4910370ecd9afa7b31e85000748c0857-Paper-Conference.pdf), [Elucidating the Design Space of Multimodal Protein Language Models](https://raw.githubusercontent.com/mlresearch/v267/main/assets/hsieh25a/hsieh25a.pdf), [Deliberate Reasoning in Language Models as Structure-Aware Planning with an Accurate World Model](https://aclanthology.org/2025.acl-long.1540.pdf))
> The degree to which a model produces a wide variety of distinct outputs rather than repetitive or mode-collapsed responses.

**Response diversity** (5 papers: [Leftover Lunch: Advantage-based Offline Reinforcement Learning for Language Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/3b18d368150474ac6fc9bb665d3eb3da-Paper-Conference.pdf), [Multiagent Finetuning: Self Improvement with Diverse Reasoning Chains](https://proceedings.iclr.cc/paper_files/paper/2025/file/1d50221b03ced7152d8750c9d1e66cba-Paper-Conference.pdf), [Evaluating Language Models as Synthetic Data Generators](https://aclanthology.org/2025.acl-long.320.pdf), [Towards Cost-Effective Reward Guided Text Generation](https://raw.githubusercontent.com/mlresearch/v267/main/assets/rashid25a/rashid25a.pdf), [Diverse, not Short: A Length-Controlled Data Selection Strategy for Improving Response Diversity of Language Models](https://aclanthology.org/2025.emnlp-main.1721.pdf))
> The variety of linguistic expressions and content generated by a model, measured by the uniqueness of n-grams across outputs.

**Output diversity** (3 papers: [Understanding the Effects of RLHF on LLM Generalisation and Diversity](https://proceedings.iclr.cc/paper_files/paper/2024/file/5a68d05006d5b05dd9463dd9c0219db0-Paper-Conference.pdf), [Progress or Regress? Self-Improvement Reversal in Post-training](https://proceedings.iclr.cc/paper_files/paper/2025/file/1fa0c4e5a7e189729230d018b229abc7-Paper-Conference.pdf), [Curiosity-Driven Reinforcement Learning from Human Feedback](https://aclanthology.org/2025.acl-long.1146.pdf))
> The model's ability to generate a wide variety of syntactic, semantic, and logical outputs for a given input or across a range of inputs.

**Prediction diversity** (1 paper: [Uncertainty-Aware Decoding with Minimum Bayes Risk](https://proceedings.iclr.cc/paper_files/paper/2025/file/1588dc2b2ef339d6e4c47d212e36f991-Paper-Conference.pdf))
> The degree of dissimilarity in the outputs generated by a set of ensembled models for the same input.

**Solution diversity** (1 paper: [SFS: Smarter Code Space Search improves LLM Inference Scaling](https://proceedings.iclr.cc/paper_files/paper/2025/file/387982dbf23d9975c7fc45813dd3dabc-Paper-Conference.pdf))
> The degree to which multiple solutions generated for the same problem differ from one another, which is crucial for effective exploration of the solution space.

**Plan diversity** (1 paper: [Dualformer: Controllable Fast and Slow Thinking by Learning with Randomized Reasoning Traces](https://proceedings.iclr.cc/paper_files/paper/2025/file/ed45d6a03de84cc650cae0655f699356-Paper-Conference.pdf))
> The latent capacity of the model to generate a variety of unique valid solutions or paths for a given problem rather than converging on a single output.

## Relationships

### Generation diversity →
- **General ability** (construct): *causes*, 1 paper
  > Diversity loss can harm both capabilities and representation. (Section 3.1)
  - [Diverse Preference Learning for Capabilities and Alignment](https://proceedings.iclr.cc/paper_files/paper/2025/file/3df1eca840e82b11bbc33f68c773c38e-Paper-Conference.pdf)
- **Catastrophic forgetting** (behavioral indicator): *causes*, 1 paper
  > preserving output diversity has the added benefit of mitigating forgetting, as maintaining diverse outputs encourages models to retain pre-trained knowledge throughout the training process. (Section 1)
  - [Preserving Diversity in Supervised Fine-Tuning of Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/a548ef984f30bca3abdc09f43743827f-Paper-Conference.pdf)
- **Alignment tax** (construct): *causes*, 1 paper
  > by suppressing alternative plausible outputs during training, CE can lead to “knowledge forgetting” or “alignment tax”, eroding the pre-trained model’s encoded knowledge (Section 1)
  - [Preserving Diversity in Supervised Fine-Tuning of Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/a548ef984f30bca3abdc09f43743827f-Paper-Conference.pdf)

### → Generation diversity
- **Mode collapse** (behavioral indicator): *causes*, 3 papers
  > Large Language Models (LLMs) often suffer from mode collapse, repeatedly generating the same few completions even when many valid answers exist, limiting their diversity across a wide range of tasks.
  - [Group-Aware Reinforcement Learning for Output Diversity in Large Language Models](https://aclanthology.org/2025.emnlp-main.1649.pdf)
  - [Understanding the Effects of RLHF on LLM Generalisation and Diversity](https://proceedings.iclr.cc/paper_files/paper/2024/file/5a68d05006d5b05dd9463dd9c0219db0-Paper-Conference.pdf)
  - [Representative Language Generation](https://raw.githubusercontent.com/mlresearch/v267/main/assets/peale25a/peale25a.pdf)
- **Self-improvement** (construct): *causes*, 1 paper
  > The evaluation results highlight a critical trade-off in iterative self-improvement: while aiming for higher accuracy, the diversity of outputs, which can be crucial for creativity and robustness in problem-solving, is compromised. (Section 5.2)
  - [Progress or Regress? Self-Improvement Reversal in Post-training](https://proceedings.iclr.cc/paper_files/paper/2025/file/1fa0c4e5a7e189729230d018b229abc7-Paper-Conference.pdf)
- **Code debugging** (behavioral indicator): *correlates*, 1 paper
  > The superior performance of AuPairs produced by Gemini-1.5-Pro corresponds to highly diverse fixes (Fig. 8, top right). (Section 3.7. High Code-specific Diversity)
  - [AuPair: Golden Example Pairs for Code Repair](https://raw.githubusercontent.com/mlresearch/v267/main/assets/mavalankar25a/mavalankar25a.pdf)
- **Representation learning** (construct): *causes*, 1 paper
  > Introducing representation-level learning and architectural innovations infuses geometric inductive biases and effectively refines generation diversity. (Section 1)
  - [Elucidating the Design Space of Multimodal Protein Language Models](https://raw.githubusercontent.com/mlresearch/v267/main/assets/hsieh25a/hsieh25a.pdf)
- **Reward hacking** (behavioral indicator): *causes*, 1 paper
  > Reward hacking suppresses all behavioral characteristics in rejected completions, resulting in poor expressive ability and the deterioration of generation diversity. (Section 3.2)
  - [Weights-Rotated Preference Optimization for Large Language Models](https://aclanthology.org/2025.emnlp-main.1329.pdf)

### Associated with
- **Text generation quality** (construct), 2 papers
  > Decoding-based approaches offer greater adaptability but face a fundamental diversity–quality trade-off. (Section 1)
  - [G2: Guided Generation for Enhanced Output Diversity in LLMs](https://aclanthology.org/2025.emnlp-main.713.pdf)
  - [Synthesize, Partition, then Adapt: Eliciting Diverse Samples from Foundation Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/6e2861dabad3fe21a71914ccfbfff976-Paper-Conference.pdf)
- **Text generation** (behavioral indicator), 1 paper
  > Diversity: This metric measures the ability to generate texts with a wide range of vocabulary.
  - [Collab: Controlled Decoding using Mixture of Agents for LLM Alignment](https://proceedings.iclr.cc/paper_files/paper/2025/file/2e79dce47c5bbe738dff9c05ace8a037-Paper-Conference.pdf)
- **Coherence** (construct), 1 paper
  > Thus, the best choice of threshold must strike a balance between diversity (i.e., including as many tokens as possible in the set of candidates) and coherence (i.e., avoiding sampling tokens outside the true support). (Section 2)
  - [Closing the Curious Case of Neural Text Degeneration](https://proceedings.iclr.cc/paper_files/paper/2024/file/34899013589ef41aea4d7b2f0ef310c1-Paper-Conference.pdf)
- **Out-of-distribution generalization** (construct), 1 paper
  > We demonstrate an inherent tradeoff between generalisation performance and output diversity when choosing between these methods (Section 7).
  - [Understanding the Effects of RLHF on LLM Generalisation and Diversity](https://proceedings.iclr.cc/paper_files/paper/2024/file/5a68d05006d5b05dd9463dd9c0219db0-Paper-Conference.pdf)
- **Downstream task performance** (behavioral indicator), 1 paper
  > “Our experiments demonstrate particularly strong gains for IRL on the Pareto front of task performance and diversity of model generations.”
  - [Imitating Language via Scalable Inverse Reinforcement Learning](https://proceedings.neurips.cc/paper_files/paper/2024/file/a5036c166e44b731f214f41813364d01-Paper-Conference.pdf)
- **Creativity** (construct), 1 paper
  > hindering the exploration of novel and diverse ideas — a cornerstone of creativity.
  - [Diversity-Rewarded CFG Distillation](https://proceedings.iclr.cc/paper_files/paper/2025/file/a59a11e8580a7ac850cb792f6179c7a0-Paper-Conference.pdf)
- **Music generation** (behavioral indicator), 1 paper
  > We apply our strategy to text-to-music generation, a creative task where balancing quality and diversity is key.
  - [Diversity-Rewarded CFG Distillation](https://proceedings.iclr.cc/paper_files/paper/2025/file/a59a11e8580a7ac850cb792f6179c7a0-Paper-Conference.pdf)
- **Epistemic uncertainty** (construct), 1 paper
  > The performance of uncertainty-aware MBR is highly correlated with the prediction diversity across the combined models. (Introduction)
  - [Uncertainty-Aware Decoding with Minimum Bayes Risk](https://proceedings.iclr.cc/paper_files/paper/2025/file/1588dc2b2ef339d6e4c47d212e36f991-Paper-Conference.pdf)
- **Faithfulness** (construct), 1 paper
  > We emphasize the importance of balancing faithfulness and diversity during post-training stages, providing a theoretical foundation for existing methodologies. (Section 5)
  - [Towards a Theoretical Understanding of Synthetic Data in LLM Post-Training: A Reverse-Bottleneck Perspective](https://proceedings.iclr.cc/paper_files/paper/2025/file/1e0bfe8bbaa0e70809f0a8ccd9c2ff3e-Paper-Conference.pdf)
- **Robustness** (construct), 1 paper
  > We posit that a model’s capacity to produce diverse solutions is indicative of its robustness and flexibility in problem-solving. (Section 5.2)
  - [Progress or Regress? Self-Improvement Reversal in Post-training](https://proceedings.iclr.cc/paper_files/paper/2025/file/1fa0c4e5a7e189729230d018b229abc7-Paper-Conference.pdf)
- **Controllability** (construct), 1 paper
  > Recent advancements in DPO focus on mainly two directions: efficiency i.e., further simplifying the constraints of DPO, and controllability i.e., keeping the balance between alignment and generation diversity. (Section 1. Introduction)
  - [Constrain Alignment with Sparse Autoencoders](https://raw.githubusercontent.com/mlresearch/v267/main/assets/yin25a/yin25a.pdf)
- **Instruction following** (behavioral indicator), 1 paper
  > This limitation [in output diversity] hinders their performance in tasks that demand diverse and informative responses, such as open-domain question answering, instruction following, and test-time scaling for reasoning (Zhang et al., 2024a). (Section 1)
  - [G2: Guided Generation for Enhanced Output Diversity in LLMs](https://aclanthology.org/2025.emnlp-main.713.pdf)
- **Stability** (construct), 1 paper
  > Furthermore, stability implies an intuitive notion of diversity, suggesting that tokens with similar logits should have comparable probabilities of being selected.
  - [Permute-and-Flip: An optimally stable and watermarkable decoder for LLMs](https://proceedings.iclr.cc/paper_files/paper/2025/file/50be7e77b9c883144940be925b608acc-Paper-Conference.pdf)
