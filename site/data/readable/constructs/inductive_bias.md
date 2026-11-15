# Inductive bias
**Type:** Construct  
**Supporting papers:** 15  

## State of the Field

**Space of definitions.** Across papers, the prevailing usage treats inductive bias as a model- or training-level set of implicit assumptions, preferences, or tendencies that make some solutions or generalizations more likely than others on new or unseen tasks. Many definitions tie it to architecture or training procedure, and some make the preference concrete as simpler or sparser solutions, while others describe it as assumptions supplied by pre-training or as tendencies that shape behavior even without explicit instruction. The main variation is scope: most definitions stay broad at the level of the model or training method, whereas a smaller line of work narrows it to particular architectures or components, such as transformer architectures or positional encodings.

**Space of facets.** Papers systematize the construct mainly by source and by what it favors. Some write of transformer-specific, model-specific, or component-level biases, including looped-transformer biases toward simpler or sparser solutions and positional-encoding biases that facilitate counting in different task formats. Another recurring split concerns distinctiveness: one paper says common architectures and training setups might encode "very similar" inductive biases, while another describes "idiosyncratic inductive biases" shaped by architecture, training, and tuning. Some papers also attach the term to a learning setting, discussing the inductive bias of in-context learning or of learning functions given by Fourier series.

**Space of measurement.** No measurement instrument is linked to inductive bias, and no behavioral indicator is linked either. Instead, papers operationalize it through comparisons of architectures, training setups, or components: butterfly factorization is said to introduce an implicit bias that benefits generalizability and prevents overfitting, looped versus unlooped transformers are used to study a bias toward simpler or sparser solutions, pre-trained LMs are credited with few-shot ability in low-data settings, and different positional encodings are said to encode different biases for counting. These uses stay close to the dominant definitions by focusing on architecture, training, and components rather than on a separately instrumented variable.

**Links.** Papers connect inductive bias to Generalization, Reasoning, Length generalization, and World modeling. For Generalization, one paper claims a causal relationship from inductive bias to generalization, describing a "desirable inductive bias" that improves generalization abilities, while another paper treats inductive bias as related to downstream generalization. One paper also claims a causal relationship from inductive bias to Reasoning, reporting a bias toward improving downstream tasks that require reasoning abilities. Other papers relate inductive bias to Length generalization, saying short validation reveals an architecture's bias when generalizing to longer lengths, and to World modeling, stating that a foundation model's inductive bias reveals its world model.

## Sources

**Inductive bias** (8 papers: [In-Context Learning through the Bayesian Prism](https://proceedings.iclr.cc/paper_files/paper/2024/file/d81cd83e7f6748af351485d73f305483-Paper-Conference.pdf), [Looped Transformers are Better at Learning Learning Algorithms](https://proceedings.iclr.cc/paper_files/paper/2024/file/b8402301e7f06bdc97a31bfaa653dc32-Paper-Conference.pdf), [Parameter-Efficient Orthogonal Finetuning via Butterfly Factorization](https://proceedings.iclr.cc/paper_files/paper/2024/file/a63ce8e6867a1bf4b4ca62e5077814d9-Paper-Conference.pdf), [Unleashing the Power of Pre-trained Language Models for Offline Reinforcement Learning](https://proceedings.iclr.cc/paper_files/paper/2024/file/c7793beb7f32b559df55d48370f2b8ae-Paper-Conference.pdf), [Algorithmic Capabilities of Random Transformers](https://proceedings.neurips.cc/paper_files/paper/2024/file/bccdd196d798a51a4961989984a9ed4a-Paper-Conference.pdf), [Language Models Need Inductive Biases to Count Inductively](https://proceedings.iclr.cc/paper_files/paper/2025/file/378226e5df7eded3e401de5c9493143c-Paper-Conference.pdf), [LLMs on the Line: Data Determines Loss-to-Loss Scaling Laws](https://raw.githubusercontent.com/mlresearch/v267/main/assets/mayilvahanan25a/mayilvahanan25a.pdf), [To Mask or to Mirror: Human-AI Alignment in Collective Reasoning](https://aclanthology.org/2025.emnlp-main.122.pdf))
> An inherent property of a model or training method that causes it to prefer certain solutions or generalizations over others, influencing its performance on new tasks.

## Relationships

### Inductive bias →
- **Generalization** (construct): *causes*, 2 papers
  > This suggests a desirable inductive bias of RAPTR that improves its generalization abilities beyond perplexity. (Section 4)
  - [Efficient stagewise pretraining via progressive subnetworks](https://proceedings.iclr.cc/paper_files/paper/2025/file/b21ae5a5df83632324b61b595ab653b9-Paper-Conference.pdf)
  - [LLMs on the Line: Data Determines Loss-to-Loss Scaling Laws](https://raw.githubusercontent.com/mlresearch/v267/main/assets/mayilvahanan25a/mayilvahanan25a.pdf)
- **Reasoning** (construct): *causes*, 1 paper
  > MIDAS is not only training-efﬁcient but surprisingly also has an inductive bias towards improving downstream tasks, especially tasks that require reasoning abilities like reading comprehension and math problems, despite having similar or slightly worse perplexity compared to baseline training. (Abstract)
  - [On the Inductive Bias of Stacking Towards Improving Reasoning](https://proceedings.neurips.cc/paper_files/paper/2024/file/837bc5db12f3d394d220815a7687340c-Paper-Conference.pdf)

### Associated with
- **Length generalization** (construct), 1 paper
  > The short validation set reveals an architecture’s inductive bias in the absence of any disambiguating information about how it should generalize to longer lengths, as in the experiments of Del´etang et al. (2023). (Section 4)
  - [Training Neural Networks as Recognizers of Formal Languages](https://proceedings.iclr.cc/paper_files/paper/2025/file/7256b2c07b6980aca382eb41606501c2-Paper-Conference.pdf)
- **World modeling** (construct), 1 paper
  > Similarly, the inductive bias of a foundation model reveals its world model.
  - [What Has a Foundation Model Found? Using Inductive Bias to Probe for World Models](https://raw.githubusercontent.com/mlresearch/v267/main/assets/vafa25a/vafa25a.pdf)
