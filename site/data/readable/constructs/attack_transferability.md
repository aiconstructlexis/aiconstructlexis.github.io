# Attack transferability
**Type:** Construct  
**Supporting papers:** 3  
**Also known as:** Strategy transferability, Super transferability  

## State of the Field

**Space of definitions.** Across the definitions, the prevailing usage treats attack transferability as whether an attack developed in one setting remains effective in another, most often from one model to other models. Papers describe this for prompt-level and embedding-level attacks, and one definition explicitly ties such transfer to shared vulnerabilities in models' safety mechanisms. Some authors cast the same general idea as strategy transferability, meaning jailbreak strategies that keep high attack success rates across target models, attacker models, or datasets, while a smaller line uses the broader label super transferability for a single perturbation that works across data samples, domains, models, and tasks at the same time.

**Space of facets.** Papers organize the construct mainly by what is being transferred and across which axes. One recurring distinction is between prompt-level and embedding-level attacks, and another is between transfer of a specific attack and transfer of a learned strategy library. The label super transferability marks a broader variant: instead of cross-model or cross-dataset reuse alone, it denotes simultaneous cross-data, cross-domain, cross-model, and cross-task effectiveness from one perturbation, so the terminology is not fully uniform in scope.

**Space of measurement.** When papers operationalize the construct, the only linked measurement instrument is HarmBench, and the only linked behavioral indicator is Jailbreaking. The explicit measurement uses HarmBench ASR: one setup fixes a strategy library and measures attack success without updating it, and another reports transfer to out-of-distribution tasks from HarmBench. This operationalization lines up with definitions centered on effectiveness across target models or datasets, but it is narrower than the super transferability framing, which also includes cross-data, cross-domain, and cross-task transfer of a single perturbation.

**Links.** Beyond measurement, one paper reports that attack transferability is related to Jailbreaking, evaluating suffixes across behaviors and target models in terms of transferability. Separately, one paper claims a causal relationship from Model similarity to Attack transferability, citing prior work that aligning white-box and target models in the safety domain can improve the transferability of adversarial prompts.

## Sources

**Attack transferability** (1 paper: [Uncovering Safety Risks of Large Language Models through Concept Activation Vector](https://proceedings.neurips.cc/paper_files/paper/2024/file/d3a230d716e65afab578a8eb31a8d25f-Paper-Conference.pdf))
> The extent to which attacks, either at the prompt or embedding level, developed for one model are effective against other models, suggesting shared vulnerabilities in their safety mechanisms.

**Strategy transferability** (1 paper: [AutoDAN-Turbo: A Lifelong Agent for Strategy Self-Exploration to Jailbreak LLMs](https://proceedings.iclr.cc/paper_files/paper/2025/file/1bff3663270ba47f801e917f782d7935-Paper-Conference.pdf))
> The extent to which discovered jailbreak strategies remain effective across different target models, attacker models, or datasets.

**Super transferability** (1 paper: [X-Transfer Attacks: Towards Super Transferable Adversarial Attacks on CLIP](https://raw.githubusercontent.com/mlresearch/v267/main/assets/huang25h/huang25h.pdf))
> A property of an adversarial attack where a single perturbation is effective across different data samples, domains, models, and tasks simultaneously.

## Relationships

### Attack transferability →
- **HarmBench** (measurement instrument): *measured_by*, 2 papers
  > “we test if the strategy library can be directly used without any updates, by fixing the strategy library and measuring the Harmbench ASR (noted as Pre-ASR).”
  - [AutoDAN-Turbo: A Lifelong Agent for Strategy Self-Exploration to Jailbreak LLMs](https://proceedings.iclr.cc/paper_files/paper/2025/file/1bff3663270ba47f801e917f782d7935-Paper-Conference.pdf)
  - [Jailbreaking as a Reward Misspecification Problem](https://proceedings.iclr.cc/paper_files/paper/2025/file/cf00c2fdf92882989b1fc0e3094a2abf-Paper-Conference.pdf)

### → Attack transferability
- **Model similarity** (construct): *causes*, 1 paper
  > “Building on previous work suggesting that aligning white-box and target models in the safety domain can improve the transferability of adversarial prompts”
  - [Stealthy Jailbreak Attacks on Large Language Models via Benign Data Mirroring](https://aclanthology.org/2025.naacl-long.88.pdf)

### Associated with
- **Jailbreaking** (behavioral indicator), 1 paper
  > We evaluate each suffix on all 50 behaviors (universality) including the one it is directly optimized for and on all five target models (transferability) including the one it is optimized on. (Section 3.1)
  - [Stronger Universal and Transferable Attacks by Suppressing Refusals](https://aclanthology.org/2025.naacl-long.302.pdf)
