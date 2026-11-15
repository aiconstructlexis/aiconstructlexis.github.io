# Weak-to-strong generalization
**Type:** Construct  
**Supporting papers:** 13  
**Also known as:** Weak to strong generalization, Weak-to-Strong generalization  

## State of the Field

**Space of definitions.** Across the surveyed work, the dominant framing treats weak-to-strong generalization as a phenomenon or ability in which a stronger model, trained on weaker supervision, weaker demonstrations, or data labeled by a weaker model, exceeds the performance of the weak source policy or weak supervisor. Most definitions agree on this above-teacher criterion, while smaller variations emphasize different targets: some describe recovering the strong model's full capabilities or full potential under weak supervision, and another casts it as extending an alignment objective into areas beyond the weak supervisor's knowledge. A smaller line also presents it as a latent ability, rather than only an observed outcome.

**Space of facets.** Papers use the same label for several closely related notions: an observed phenomenon of outperforming weak teachers, an ability or latent ability of the strong model, and a training paradigm in which a strong model is supervised by a weaker model. They also vary in scope, with some treating it broadly as eliciting capabilities from noisy weak labels and others narrowing it to generalizing an alignment objective beyond the supervisor's knowledge boundary. One recurring contrast is that papers do not present it as simple replication of the weak model, but as learning the task's intent and rules from weakly labeled data.

**Space of measurement.** No measurement instrument is linked to it, and no behavioral indicator is linked to it. In the papers, it is operationalized directly through the training setup and comparative outcome: a stronger model is trained or fine-tuned on weaker demonstrations or labels from a weaker model, and the construct is evidenced when the student outperforms the weak supervisor, recovers part of the strong model's performance, or, in some definitions, recovers its full capabilities or full potential. This operationalization mostly matches the dominant definitions, though definitions that stress full capability recovery are broader than the minimal above-teacher criterion.

**Links.** It is linked to 3 constructs: parametric knowledge, critique ability, and overfitting. One paper claims a causal relationship from parametric knowledge to weak-to-strong generalization, stating that it is possible by eliciting latent knowledge from pre-trained LLMs. Other papers relate it to critique ability, describing weaker critics guiding stronger task models as a similar phenomenon, and to overfitting, noting that erroneous labels from weak supervisors may lead strong models to overfit in weak-to-strong generalization.

## Sources

**Weak-to-strong generalization** (4 papers: [Stress-Testing Capability Elicitation With Password-Locked Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/7ff97417474268e6b5a38bcbfae04944-Paper-Conference.pdf), [Super(ficial)-alignment: Strong Models May Deceive Weak Models in Weak-to-Strong Generalization](https://proceedings.iclr.cc/paper_files/paper/2025/file/092359ce5cf60a80e882378944bf1be4-Paper-Conference.pdf), [How to Mitigate Overfitting in Weak-to-strong Generalization?](https://aclanthology.org/2025.acl-long.784.pdf), [Relating Misfit to Gain in Weak-to-Strong Generalization Beyond the Squared Loss](https://raw.githubusercontent.com/mlresearch/v267/main/assets/mulgund25a/mulgund25a.pdf))
> The phenomenon where training on weaker demonstrations or weaker supervision still yields performance above the weak source policy.

**Weak to strong generalization** (1 paper: [Weak to Strong Generalization for Large Language Models with Multi-capabilities](https://proceedings.iclr.cc/paper_files/paper/2025/file/1ebcb8f051d0c178474619bbfb32b340-Paper-Conference.pdf))
> The ability of a more powerful model to learn a task and surpass the performance of a weaker supervisor model by training on data labeled by that weaker model.

**Weak-to-Strong generalization** (1 paper: [Bayesian WeakS-to-Strong from Text Classification to Generation](https://proceedings.iclr.cc/paper_files/paper/2025/file/495e55f361708bedbab5d81f92048dcd-Paper-Conference.pdf))
> The ability of a stronger model to recover its full capabilities when supervised only by the labels from a weaker, less capable model.

## Relationships

### → Weak-to-strong generalization
- **Parametric knowledge** (construct): *causes*, 1 paper
  > We prove that weak-to-strong generalization is possible by eliciting latent knowledge from pre-trained LLMs.
  - [A transfer learning framework for weak to strong generalization](https://proceedings.iclr.cc/paper_files/paper/2025/file/fa47ffc7b2033fd32d8b8734686f6ff4-Paper-Conference.pdf)

### Associated with
- **Critique ability** (construct), 1 paper
  > Our experiments demonstrate that relatively weaker critic models can effectively guide stronger task-performing models such as GPT-4o (Table 3), exhibiting a similar phenomenon to weak-to-strong generalization (Christiano et al., 2018; Burns et al., 2023), where weaker models can be trained to effectively supervise more capable ones. (Section 1)
  - [Teaching Language Models to Critique via Reinforcement Learning](https://raw.githubusercontent.com/mlresearch/v267/main/assets/xie25a/xie25a.pdf)
- **Overfitting** (construct), 1 paper
  > Although weak-to-strong generalization exhibiting certain generalization capabilities, strong models exhibit significant overfitting in weak-to-strong generalization: Due to the strong fit ability of strong models, erroneous labels from weak supervisors may lead to overfitting in strong models. (Section 1)
  - [How to Mitigate Overfitting in Weak-to-strong Generalization?](https://aclanthology.org/2025.acl-long.784.pdf)
