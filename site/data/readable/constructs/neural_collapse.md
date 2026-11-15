# Neural collapse
**Type:** Construct  
**Supporting papers:** 3  
**Also known as:** Within-class variability collapse  

## State of the Field

**Space of definitions.** Across the papers, the prevailing usage frames neural collapse as a late-training geometric phenomenon in deep networks, centered on last-layer or penultimate representations and classifier weights adopting a simplified structure. The common description is that samples from the same class converge to a class mean, and one paper further specifies that these class means form a simplex equiangular tight frame; some descriptions also tie the phenomenon to the terminal phase of training with cross-entropy for classification, or to models that reach zero training error on sufficiently large, balanced data. A narrower usage in one paper focuses on one component, "within-class variability collapse," where "top-layer representations collapse to their class means," so the main difference is between the broader overall geometry and a specific within-class facet.

**Space of facets.** The clearest internal breakdown is one paper's labeling of within-class variability collapse as NC1, defined as reduced dispersion within a class so that embeddings become tightly clustered around the class mean. Beyond that, papers mostly use neural collapse as the umbrella name for the overall last-layer geometry, combining within-class convergence with the arrangement of class means and classifier weights. The main systematic distinction that appears is broad neural collapse versus its NC1 subphenomenon.

**Space of measurement.** Operationalization is sparse in the linked literature: no measurement instrument is linked to neural collapse, and no behavioral indicator is linked to it. Papers do not link it to any named benchmark, human evaluation, LLM-as-a-judge, probe, or analysis. One paper nevertheless refers to a "higher degree of neural collapse (lower ΔTCD)," which shows that some authors treat it as varying in degree even when no dedicated measurement record is linked.

**Links.** Papers connect neural collapse to three other constructs: robustness, fairness, and generalization. One paper claims a causal relationship from neural collapse to fairness, saying that explicitly enforcing it can promote fairness in pretrained language models; another claims a causal relationship from neural collapse to stronger generalizability in text classification tasks, phrased as a higher degree of neural collapse (lower ΔTCD) leading to stronger generalizability. Robustness is linked in two ways: one paper claims a causal relationship from neural collapse to improved robustness during LoRA fine-tuning in personalized learning, while another reports neural-collapse-related behaviors as associated with robustness under specific conditions.

## Sources

**Neural collapse** (2 papers: [Collapsed Language Models Promote Fairness](https://proceedings.iclr.cc/paper_files/paper/2025/file/96db0c53484428513ebc537fe48ddb7a-Paper-Conference.pdf), [Advancing Personalized Learning with Neural Collapse for Long-Tail Challenge](https://raw.githubusercontent.com/mlresearch/v267/main/assets/hu25f/hu25f.pdf))
> A learning phenomenon in deep neural networks where last-layer representations and classifier weights adopt a specific, simplified geometric structure during the terminal phase of training.

**Within-class variability collapse** (1 paper: [Linguistic Collapse: Neural Collapse in (Large) Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/f88cc8930b47a45ec4733123bf3039b9-Paper-Conference.pdf))
> The reduction of dispersion among representations belonging to the same class, so that same-class embeddings become tightly clustered around their class mean.

## Relationships

### Neural collapse →
- **Robustness** (construct): *causes*, 2 papers
  > In this paper, we are the first to apply neural collapse to address the long-tail problem in data-based personalized learning and improve the robustness of large language models during LoRA fine-tuning in personalized learning scenarios. (Section 2)
  - [Advancing Personalized Learning with Neural Collapse for Long-Tail Challenge](https://raw.githubusercontent.com/mlresearch/v267/main/assets/hu25f/hu25f.pdf)
  - [Linguistic Collapse: Neural Collapse in (Large) Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/f88cc8930b47a45ec4733123bf3039b9-Paper-Conference.pdf)
- **Fairness** (construct): *causes*, 1 paper
  > This observation further inspires us to explicitly enforce neural collapse to promote fairness in pretrained language models. (Section 1)
  - [Collapsed Language Models Promote Fairness](https://proceedings.iclr.cc/paper_files/paper/2025/file/96db0c53484428513ebc537fe48ddb7a-Paper-Conference.pdf)
- **Generalization** (construct): *causes*, 1 paper
  > A higher degree of neural collapse (lower ∆TCD) leads to stronger generalizability in text classification tasks. (Section 4.1)
  - [Advancing Personalized Learning with Neural Collapse for Long-Tail Challenge](https://raw.githubusercontent.com/mlresearch/v267/main/assets/hu25f/hu25f.pdf)
