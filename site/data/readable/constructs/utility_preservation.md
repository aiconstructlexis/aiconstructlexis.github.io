# Utility preservation
**Type:** Construct  
**Supporting papers:** 22  
**Also known as:** General capability preservation, Model performance preservation, Capabilities preservation, Capability preservation, Utility, Tool knowledge retention, Utility retention, Performance retention, Model integrity, Performance preservation  

## State of the Field

**Space of definitions.** Across papers, the prevailing usage treats utility preservation as retention of a model's general performance or capabilities after a targeted intervention, most often unlearning, but also after alignment, editing, steering, pruning, compression, layer skipping, or fine-tuning. Most definitions focus on maintaining performance on non-target data or general downstream tasks, often phrased as preserving the retain set or avoiding degradation on benign tasks. The main variation is the reference standard: some papers compare against non-target or retain-set performance, others against the original or reference model's core capabilities, and narrower variants focus on preserving functional code generation or retained tool use.

**Space of facets.** Papers use a broad family of near-synonymous labels for this construct, including capability preservation, general capability preservation, utility retention, performance retention, model integrity, and performance preservation, usually for the same broad idea of retaining prior abilities after intervention. A narrower subtype is tool knowledge retention, which isolates preservation of knowledge about tools not marked for unlearning. Some papers make the preserved content explicit as factual knowledge, truthfulness, reasoning, text and code generation, instruction following, or functional correctness, and one unlearning benchmark places utility preservation as one of six desirable properties of an unlearned model.

**Space of measurement.** Across papers, utility preservation is measured by 12 instruments and linked to 3 behavioral indicators. The most common instruments are MT-Bench, AlpacaEval, MMLU, GSM8K, and AgentDojo, with papers using them to assess general capabilities, benign-task performance, knowledge reasoning, conversational ability, and utility preservation in agent settings. Almost all of these operationalizations are benchmark-based, and they mostly match the dominant definition by checking post-intervention performance on general or non-target tasks, though some evaluations narrow the construct to particular domains such as code or speech.

**Links.** A recurring cross-paper link is a trade-off with forget quality: one paper reports that utility preservation correlates with forget quality, and another treats the two as related when explicit retain data or reference-model knowledge may blur forget and retain data. Single-paper causal claims run from truthfulness to utility preservation, where increased truthfulness negatively impacts utility, and from overrefusal to utility preservation, where stronger refusal on benign inputs limits overall utility. Other papers relate utility preservation to privacy preservation through a privacy-utility trade-off, to knowledge memorization via retain-set evaluation, and more broadly to retaining other general abilities after intervention.

## Sources

**Utility preservation** (2 papers: [MUSE: Machine Unlearning Six-Way Evaluation for Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/4556f5398bd2c61bd7500e306b4e560a-Paper-Conference.pdf), [ProSec: Fortifying Code LLMs with Proactive Security Alignment](https://raw.githubusercontent.com/mlresearch/v267/main/assets/xu25aa/xu25aa.pdf))
> The extent to which an unlearned model maintains its general performance on data not intended for removal.

**Capability preservation** (1 paper: [Theoretical guarantees on the best-of-n alignment policy](https://raw.githubusercontent.com/mlresearch/v267/main/assets/beirami25a/beirami25a.pdf))
> The extent to which an aligned model retains the core abilities and knowledge of the original reference model from which it was derived.

**Model performance preservation** (1 paper: [DLP: Dynamic Layerwise Pruning in Large Language Models](https://raw.githubusercontent.com/mlresearch/v267/main/assets/chen25l/chen25l.pdf))
> The ability of a pruned model to retain its original language modeling and downstream task performance despite high sparsity.

**General capability preservation** (1 paper: [Reinforced Lifelong Editing for Language Models](https://raw.githubusercontent.com/mlresearch/v267/main/assets/li25an/li25an.pdf))
> The ability of a model editing method to maintain the LLM's performance on general downstream tasks while performing targeted knowledge updates.

**Capabilities preservation** (1 paper: [AxBench: Steering LLMs? Even Simple Baselines Outperform Sparse Autoencoders](https://raw.githubusercontent.com/mlresearch/v267/main/assets/wu25a/wu25a.pdf))
> The extent to which a steering intervention avoids degrading the model's underlying general abilities while controlling a target concept.

**Utility** (1 paper: [Get more for less: Principled Data Selection for Warming Up Fine-Tuning in LLMs](https://proceedings.iclr.cc/paper_files/paper/2024/file/b36dc39b319ba6ba2a0fd7601951efb4-Paper-Conference.pdf))
> The model's ability to maintain its performance on general downstream tasks after a targeted intervention like detoxification.

**Tool knowledge retention** (1 paper: [Tool Unlearning for Tool-Augmented LLMs](https://raw.githubusercontent.com/mlresearch/v267/main/assets/cheng25a/cheng25a.pdf))
> The latent ability of a model to preserve its learned capability to use tools that are not marked for unlearning, maintaining performance on those tools post-unlearning.

**Utility retention** (1 paper: [Adaptive Localization of Knowledge Negation for Continual LLM Unlearning](https://raw.githubusercontent.com/mlresearch/v267/main/assets/wuerkaixi25a/wuerkaixi25a.pdf))
> The degree to which an LLM preserves its general knowledge and capabilities on non-target data after undergoing an unlearning process.

**Performance retention** (1 paper: [Let LLM Tell What to Prune and How Much to Prune](https://raw.githubusercontent.com/mlresearch/v267/main/assets/yang25p/yang25p.pdf))
> The extent to which a pruned model preserves the original model's functional capabilities and accuracy after compression, particularly in language modeling and downstream tasks.

**Model integrity** (1 paper: [Unified Parameter-Efficient Unlearning for LLMs](https://proceedings.iclr.cc/paper_files/paper/2025/file/8d537430e55a283a97e9b6e682e994a3-Paper-Conference.pdf))
> The degree to which a model maintains its overall performance and efficacy after undergoing unlearning procedures.

**Performance preservation** (1 paper: [Router-Tuning: A Simple and Effective Approach for Dynamic Depth](https://aclanthology.org/2025.emnlp-main.99.pdf))
> The latent ability of a model to retain its original task performance after undergoing structural or parametric modifications such as layer skipping or fine-tuning.

## Relationships

### Utility preservation →
- **MT-Bench** (measurement instrument): *measured_by*, 4 papers
  > The utility performance is evaluated on MT-Bench(Zheng et al., 2023), IFEval(Zhou et al., 2023) and GSM8K(Cobbe et al., 2021), along with the benign part of XSTest(Röttger et al., 2024). (Section 1).
  - [Improve Safety Training of Large Language Models with Safety-Critical Singular Vectors Localization](https://aclanthology.org/2025.acl-long.245.pdf)
  - [Safe Delta: Consistently Preserving Safety when Fine-Tuning LLMs on Diverse Datasets](https://raw.githubusercontent.com/mlresearch/v267/main/assets/lu25g/lu25g.pdf)
  - [Assessing Safety Risks and Quantization-aware Safety Patching for Quantized Large Language Models](https://raw.githubusercontent.com/mlresearch/v267/main/assets/chen25ci/chen25ci.pdf)
  - [Benign Samples Matter! Fine-tuning On Outlier Benign Samples Severely Breaks Safety](https://raw.githubusercontent.com/mlresearch/v267/main/assets/guan25c/guan25c.pdf)
- **AlpacaEval** (measurement instrument): *measured_by*, 3 papers
  > To measure model utility on benign tasks, we used AlpacaEval (Dubois et al., 2024). (Section 5.1)
  - [Jailbreak Antidote: Runtime Safety-Utility Balance via Sparse Representation Adjustment in Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/36e3f9e6162d597adada4e0e4fce6861-Paper-Conference.pdf)
  - [Assessing Safety Risks and Quantization-aware Safety Patching for Quantized Large Language Models](https://raw.githubusercontent.com/mlresearch/v267/main/assets/chen25ci/chen25ci.pdf)
  - [AdaSteer: Your Aligned LLM is Inherently an Adaptive Jailbreak Defender](https://aclanthology.org/2025.emnlp-main.1248.pdf)
- **MMLU** (measurement instrument): *measured_by*, 3 papers
  > For evaluating utility, we consider MMLU (Hendrycks et al., 2020), GSM8K (Cobbe et al., 2021), and MBPP (Austin et al., 2021) datasets. (Section 3)
  - [Exploring Safety-Utility Trade-Offs in Personalized Language Models](https://aclanthology.org/2025.naacl-long.565.pdf)
  - [Safe Delta: Consistently Preserving Safety when Fine-Tuning LLMs on Diverse Datasets](https://raw.githubusercontent.com/mlresearch/v267/main/assets/lu25g/lu25g.pdf)
  - [Improving LLM Safety Alignment with Dual-Objective Optimization](https://raw.githubusercontent.com/mlresearch/v267/main/assets/zhao25c/zhao25c.pdf)
- **GSM8K** (measurement instrument): *measured_by*, 2 papers
  > For evaluating utility, we consider MMLU (Hendrycks et al., 2020), GSM8K (Cobbe et al., 2021), and MBPP (Austin et al., 2021) datasets. (Section 3)
  - [Exploring Safety-Utility Trade-Offs in Personalized Language Models](https://aclanthology.org/2025.naacl-long.565.pdf)
  - [Improve Safety Training of Large Language Models with Safety-Critical Singular Vectors Localization](https://aclanthology.org/2025.acl-long.245.pdf)
- **MUSE** (measurement instrument): *measured_by*, 1 paper
  > We address this issue by proposing MUSE, a comprehensive machine unlearning evaluation benchmark that enumerates six diverse desirable properties for unlearned models: (1) no verbatim memorization, (2) no knowledge memorization, (3) no privacy leakage, (4) utility preservation on data not intended for removal, (5) scalability with respect to the size of removal requests, and (6) sustainability over sequential unlearning requests. (Section 1)
  - [MUSE: Machine Unlearning Six-Way Evaluation for Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/4556f5398bd2c61bd7500e306b4e560a-Paper-Conference.pdf)
- **MBPP** (measurement instrument): *measured_by*, 1 paper
  > For evaluating utility, we consider MMLU (Hendrycks et al., 2020), GSM8K (Cobbe et al., 2021), and MBPP (Austin et al., 2021) datasets. (Section 3)
  - [Exploring Safety-Utility Trade-Offs in Personalized Language Models](https://aclanthology.org/2025.naacl-long.565.pdf)
- **IFEval** (measurement instrument): *measured_by*, 1 paper
  > The utility performance is evaluated on MT-Bench(Zheng et al., 2023), IFEval(Zhou et al., 2023) and GSM8K(Cobbe et al., 2021), along with the benign part of XSTest(Röttger et al., 2024). (Section 1).
  - [Improve Safety Training of Large Language Models with Safety-Critical Singular Vectors Localization](https://aclanthology.org/2025.acl-long.245.pdf)
- **HellaSwag** (measurement instrument): *measured_by*, 1 paper
  > “we evaluate capabilities retention on benchmarks including MMLU and Hellaswag”
  - [Improving LLM Safety Alignment with Dual-Objective Optimization](https://raw.githubusercontent.com/mlresearch/v267/main/assets/zhao25c/zhao25c.pdf)
- **AgentDojo** (measurement instrument): *measured_by*, 1 paper
  > Extensive evaluation on the IPI benchmark AgentDojo demonstrates that MELON outperforms SOTA defenses in both attack prevention and utility preservation. (Section 1)
  - [MELON: Provable Defense Against Indirect Prompt Injection Attacks in AI Agents](https://raw.githubusercontent.com/mlresearch/v267/main/assets/zhu25z/zhu25z.pdf)
- **GLUE** (measurement instrument): *measured_by*, 1 paper
  > “we assessed downstream performance using 6 tests from GLUE”
  - [Reinforced Lifelong Editing for Language Models](https://raw.githubusercontent.com/mlresearch/v267/main/assets/li25an/li25an.pdf)
- **LibriSpeech** (measurement instrument): *measured_by*, 1 paper
  > For general utility evaluation, we use AIR-Bench Chat..., LibriSpeech (Panayotov et al., 2015), a benchmark dataset of clean read speech for standard ASR tasks, and MELD... (Section 8.1)
  - [SPIRIT: Patching Speech Language Models against Jailbreak Attacks](https://aclanthology.org/2025.emnlp-main.734.pdf)
- **MELD** (measurement instrument): *measured_by*, 1 paper
  > For general utility evaluation, we use AIR-Bench Chat..., LibriSpeech..., and MELD (Poria et al., 2019), an emotion classification benchmark... (Section 8.1)
  - [SPIRIT: Patching Speech Language Models against Jailbreak Attacks](https://aclanthology.org/2025.emnlp-main.734.pdf)

### → Utility preservation
- **Forget quality** (construct): *correlates*, 2 papers
  > Through the evaluation of four baseline VLM unlearning algorithms within FIUBENCH, we find that all methods remain limited in their unlearning performance, with significant trade-offs between model utility and forget quality.
  - [Benchmarking Vision Language Model Unlearning via Fictitious Facial Identity Dataset](https://proceedings.iclr.cc/paper_files/paper/2025/file/dafb7f4ced9ac559e077fc611d6e96e5-Paper-Conference.pdf)
  - [LLM Unlearning via Loss Adjustment with Only Forget Data](https://proceedings.iclr.cc/paper_files/paper/2025/file/6b315c0b736711b56f33cbacfb6d5d67-Paper-Conference.pdf)
- **Truthfulness** (construct): *causes*, 1 paper
  > Additionally, increase in truthfulness negatively impacts utility (-15%). (Section 1)
  - [AI-LieDar : Examine the Trade-off Between Utility and Truthfulness in LLM Agents](https://aclanthology.org/2025.naacl-long.595.pdf)
- **Overrefusal** (behavioral indicator): *causes*, 1 paper
  > for benign inputs, such reinforcement of refusal behavior significantly increases the risk of false rejections, limiting the model’s overall utility
  - [AdaSteer: Your Aligned LLM is Inherently an Adaptive Jailbreak Defender](https://aclanthology.org/2025.emnlp-main.1248.pdf)

### Associated with
- **Privacy preservation** (construct), 1 paper
  > For DP-based solutions, although they yield better efficiency but faces the trade-off between privacy and utility. (Section 2)
  - [Cape: Context-Aware Prompt Perturbation Mechanism with Differential Privacy](https://raw.githubusercontent.com/mlresearch/v267/main/assets/wu25g/wu25g.pdf)
- **Knowledge memorization** (construct), 1 paper
  > To quantify this, we evaluate the unlearned model’s performance on the retain set using the knowledge memorization metric KnowMem(funlearn, Dretain). (Section 3.1)
  - [MUSE: Machine Unlearning Six-Way Evaluation for Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/4556f5398bd2c61bd7500e306b4e560a-Paper-Conference.pdf)
- **Deception** (construct), 1 paper
  > However, a very useful agent (from the salesman’s perspective) may engage in deceptive practices such as obfuscation and overt lying, as shown in Figure 1. (Section 1)
  - [AI-LieDar : Examine the Trade-off Between Utility and Truthfulness in LLM Agents](https://aclanthology.org/2025.naacl-long.595.pdf)
- **Text generation** (behavioral indicator), 1 paper
  > As a foundation model, f ′ is expected to retain abilities such as text and code generation, question answering, instruction-following, and basic mathematical reasoning.
  - [Tool Unlearning for Tool-Augmented LLMs](https://raw.githubusercontent.com/mlresearch/v267/main/assets/cheng25a/cheng25a.pdf)
- **Code generation** (behavioral indicator), 1 paper
  > As a foundation model, f ′ is expected to retain abilities such as text and code generation, question answering, instruction-following, and basic mathematical reasoning.
  - [Tool Unlearning for Tool-Augmented LLMs](https://raw.githubusercontent.com/mlresearch/v267/main/assets/cheng25a/cheng25a.pdf)
- **Instruction following ability** (construct), 1 paper
  > As a foundation model, f ′ is expected to retain abilities such as text and code generation, question answering, instruction-following, and basic mathematical reasoning.
  - [Tool Unlearning for Tool-Augmented LLMs](https://raw.githubusercontent.com/mlresearch/v267/main/assets/cheng25a/cheng25a.pdf)
- **Mathematical reasoning** (construct), 1 paper
  > As a foundation model, f ′ is expected to retain abilities such as text and code generation, question answering, instruction-following, and basic mathematical reasoning.
  - [Tool Unlearning for Tool-Augmented LLMs](https://raw.githubusercontent.com/mlresearch/v267/main/assets/cheng25a/cheng25a.pdf)
