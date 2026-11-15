# Editing locality
**Type:** Construct  
**Supporting papers:** 27  
**Also known as:** Locality, Editing Locality, Unrelated knowledge preservation  

## State of the Field

**Space of definitions.** Across definitions, the prevailing usage describes editing locality as the degree to which an edit stays confined to the targeted knowledge, leaving unrelated inputs, knowledge, or tasks unchanged and minimizing unintended side effects. A smaller line of work casts it either as a latent property of an editing method, namely modifying targeted knowledge without influencing unrelated knowledge or model capabilities, or as an observable outcome, "unrelated knowledge preservation," meaning maintained performance on untargeted knowledge. One definition instead uses locality for a bounded-distance constraint on relevant tokens for prediction, so the main disagreement is between a knowledge-editing preservation notion and a token-locality notion, and within the preservation notion between a method property and observed behavior.

**Space of facets.** The papers mainly differentiate it by what should remain unchanged after editing: unrelated knowledge, unrelated inputs, untargeted tasks, or broader model capabilities. The naming is mostly stable, with "locality" and "editing locality" used for the same idea, while "unrelated knowledge preservation" names the observable version. In surrounding evaluation schemes, locality is commonly treated as one criterion of knowledge editing alongside efficacy or accuracy and generality, and some papers discuss it together with reliability.

**Space of measurement.** Operationalization is benchmark-based: papers link editing locality to 10 measurement instruments, while its broader network also includes 1 behavioral indicator. CounterFact is the most common instrument, where locality is evaluated with success rates or specificity or neighborhood success; Natural Questions is used to supply unrelated tuples or locality questions; BIG-Bench Hard, CommonsenseQA, and GSM8K are also used to test whether edits leave unrelated knowledge and abilities intact, along with 5 other instruments. These operationalizations mostly match the dominant preservation framing by comparing behavior before and after editing or checking retained performance on unrelated benchmarks.

**Links.** Beyond measurement, papers claim a causal relationship from knowledge editing to editing locality, including a claim that direct editing of long-term memory can create conflicts with prior pretraining knowledge and result in poor locality. Papers also claim a causal relationship from editing locality to reliability, with one formulation stating that poor editing locality can lead to the persistence of irrelevant or inaccurate facts and compromise reliability. Editing locality is also related to generality, and one paper describes reliability, generalization, and locality as an impossible triangle in continual editing settings.

## Sources

**Locality** (5 papers: [VLKEB: A Large Vision-Language Model Knowledge Editing Benchmark](https://proceedings.neurips.cc/paper_files/paper/2024/file/1198b53fa686831d5f0c0860d7ec4f34-Paper-Datasets_and_Benchmarks_Track.pdf), [CKnowEdit: A New Chinese Knowledge Editing Dataset for Linguistics, Facts, and Logic Error Correction in LLMs](https://aclanthology.org/2025.acl-long.430.pdf), [Knowledge Editing through Chain-of-Thought](https://aclanthology.org/2025.emnlp-main.540.pdf), [MMKE-Bench: A Multimodal Editing Benchmark for Diverse Visual Knowledge](https://proceedings.iclr.cc/paper_files/paper/2025/file/01fb6de3360f9e32862665580e2c5853-Paper-Conference.pdf), [The Role of Sparsity for Length Generalization in LLMs](https://raw.githubusercontent.com/mlresearch/v267/main/assets/golowich25a/golowich25a.pdf))
> The extent to which a knowledge edit is localized, ensuring the model's behavior on unrelated inputs remains unchanged.

**Editing Locality** (1 paper: [Precise Localization of Memories: A Fine-grained Neuron-level Knowledge Editing Technique for LLMs](https://proceedings.iclr.cc/paper_files/paper/2025/file/01db36a646c07c64dd39a92b4eceb417-Paper-Conference.pdf))
> The latent property of an editing method to modify targeted knowledge without influencing unrelated knowledge or model capabilities.

**Unrelated knowledge preservation** (1 paper: [Reinforced Lifelong Editing for Language Models](https://raw.githubusercontent.com/mlresearch/v267/main/assets/li25an/li25an.pdf))
> The observable maintenance of model performance on knowledge not targeted for editing, indicating minimal interference from editing updates.

## Relationships

### Editing locality →
- **CounterFact** (measurement instrument): *measured_by*, 3 papers
  > In the Counterfact dataset, we evaluate the models on Efficacy, Generality, and Locality, using success rates as metrics. (Section 5.1)
  - [CoME: An Unlearning-based Approach to Conflict-free Model Editing](https://aclanthology.org/2025.naacl-long.325.pdf)
  - [REACT: Representation Extraction And Controllable Tuning to Overcome Overfitting in LLM Knowledge Editing](https://aclanthology.org/2025.emnlp-main.860.pdf)
  - [AlphaEdit: Null-Space Constrained Knowledge Editing for Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/29c8c615b3187ee995029284702d3f43-Paper-Conference.pdf)
- **Natural Questions** (measurement instrument): *measured_by*, 2 papers
  > The unrelated tuples (xu i , yu i )m i=1 are sampled from Natural Questions (NQ; Kwiatkowski et al., 2019). (Section 5).
  - [Massive Editing for Large Language Models via Meta Learning](https://proceedings.iclr.cc/paper_files/paper/2024/file/f074097f6f186947726ef28819d589e7-Paper-Conference.pdf)
  - [MMKE-Bench: A Multimodal Editing Benchmark for Diverse Visual Knowledge](https://proceedings.iclr.cc/paper_files/paper/2025/file/01fb6de3360f9e32862665580e2c5853-Paper-Conference.pdf)
- **Reliability** (construct): *causes*, 2 papers
  > "This limitation results in poor editing locality, which can lead to the persistence of irrelevant or inaccurate facts, ultimately compromising the reliability of LLMs."
  - [Precise Localization of Memories: A Fine-grained Neuron-level Knowledge Editing Technique for LLMs](https://proceedings.iclr.cc/paper_files/paper/2025/file/01db36a646c07c64dd39a92b4eceb417-Paper-Conference.pdf)
  - [WISE: Rethinking the Knowledge Memory for Lifelong Model Editing of Large Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/60960ad78868fce5c165295fbd895060-Paper-Conference.pdf)
- **ZsRE** (measurement instrument): *measured_by*, 1 paper
  > Since ZsRE does not measure generative capabilities, we evaluate the models based only on accuracy in terms of Efficacy, Generality, and Locality. (Section 5.1)
  - [CoME: An Unlearning-based Approach to Conflict-free Model Editing](https://aclanthology.org/2025.naacl-long.325.pdf)
- **RedPajama** (measurement instrument): *measured_by*, 1 paper
  > measure retention of pretraining data (xloc) from the base model: RedPajama
  - [WISE: Rethinking the Knowledge Memory for Lifelong Model Editing of Large Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/60960ad78868fce5c165295fbd895060-Paper-Conference.pdf)
- **WikiData_recent** (measurement instrument): *measured_by*, 1 paper
  > WikiDatarecent ... Locality ↑ (Table 2)
  - [In-Context Editing: Learning Knowledge from Self-Induced Distributions](https://proceedings.iclr.cc/paper_files/paper/2025/file/c0ff9e52e94ae331bc0f2d28be06a9ca-Paper-Conference.pdf)
- **WikiData_counterfact** (measurement instrument): *measured_by*, 1 paper
  > WikiDatacounterfact ... Locality ↑ (Table 3)
  - [In-Context Editing: Learning Knowledge from Self-Induced Distributions](https://proceedings.iclr.cc/paper_files/paper/2025/file/c0ff9e52e94ae331bc0f2d28be06a9ca-Paper-Conference.pdf)
- **CommonsenseQA** (measurement instrument): *measured_by*, 1 paper
  > For KE, we also need to consider locality, which ensures edits do not affect unrelated knowledge and abilities. To assess this, we evaluate the model on general benchmarks, including CommonsenseQA (Talmor et al., 2019), BigBench-Hard (Suzgun et al., 2023), MMLU (Hendrycks et al., 2021), and GSM8k (Cobbe et al., 2021) (Section 4.1).
  - [CaKE: Circuit-aware Editing Enables Generalizable Knowledge Learners](https://aclanthology.org/2025.emnlp-main.572.pdf)
- **BIG-Bench Hard** (measurement instrument): *measured_by*, 1 paper
  > For KE, we also need to consider locality, which ensures edits do not affect unrelated knowledge and abilities. To assess this, we evaluate the model on general benchmarks, including CommonsenseQA (Talmor et al., 2019), BigBench-Hard (Suzgun et al., 2023), MMLU (Hendrycks et al., 2021), and GSM8k (Cobbe et al., 2021) (Section 4.1).
  - [CaKE: Circuit-aware Editing Enables Generalizable Knowledge Learners](https://aclanthology.org/2025.emnlp-main.572.pdf)
- **MMLU** (measurement instrument): *measured_by*, 1 paper
  > For KE, we also need to consider locality, which ensures edits do not affect unrelated knowledge and abilities. To assess this, we evaluate the model on general benchmarks, including CommonsenseQA (Talmor et al., 2019), BigBench-Hard (Suzgun et al., 2023), MMLU (Hendrycks et al., 2021), and GSM8k (Cobbe et al., 2021) (Section 4.1).
  - [CaKE: Circuit-aware Editing Enables Generalizable Knowledge Learners](https://aclanthology.org/2025.emnlp-main.572.pdf)
- **GSM8K** (measurement instrument): *measured_by*, 1 paper
  > For KE, we also need to consider locality, which ensures edits do not affect unrelated knowledge and abilities. To assess this, we evaluate the model on general benchmarks, including CommonsenseQA (Talmor et al., 2019), BigBench-Hard (Suzgun et al., 2023), MMLU (Hendrycks et al., 2021), and GSM8k (Cobbe et al., 2021) (Section 4.1).
  - [CaKE: Circuit-aware Editing Enables Generalizable Knowledge Learners](https://aclanthology.org/2025.emnlp-main.572.pdf)

### → Editing locality
- **Knowledge editing** (behavioral indicator): *causes*, 3 papers
  > direct editing of long-term memory (ROME, MEMIT, etc.) creates conflicts with prior pretraining knowledge, resulting in poor locality (Section 3.2)
  - [WISE: Rethinking the Knowledge Memory for Lifelong Model Editing of Large Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/60960ad78868fce5c165295fbd895060-Paper-Conference.pdf)
  - [Unlocking Efficient, Scalable, and Continual Knowledge Editing with Basis-Level Representation Fine-Tuning](https://proceedings.iclr.cc/paper_files/paper/2025/file/2f89a23a19d1617e7fb16d4f7a049ce2-Paper-Conference.pdf)
  - [In-Context Editing: Learning Knowledge from Self-Induced Distributions](https://proceedings.iclr.cc/paper_files/paper/2025/file/c0ff9e52e94ae331bc0f2d28be06a9ca-Paper-Conference.pdf)

### Associated with
- **Generality** (construct), 1 paper
  > we find that it seems to be an impossible triangle—reliability, generalization, and locality can not be realized at the same time in the continual editing settings. (Section 1)
  - [WISE: Rethinking the Knowledge Memory for Lifelong Model Editing of Large Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/60960ad78868fce5c165295fbd895060-Paper-Conference.pdf)
