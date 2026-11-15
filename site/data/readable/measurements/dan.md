# DAN
**Type:** Measurement instrument  
**Supporting papers:** 8  
**Also known as:** DoAnythingNow  

## State of the Field

**What it is.** Most commonly, papers treat DAN, often expanded as Do Anything Now, as a benchmark or prompt-based test for whether models resist malicious or jailbreak-enhanced instructions. Definitions describe it as a benchmark collection of jailbreak-enhanced instructions for evaluating resilience against diverse jailbreak attacks, or more generally as a benchmark for model safety against malicious instructions and jailbreak attacks. Some authors use a narrower prompt-level framing, calling DAN 13.0 a well-known jailbreaking prompt and baseline that overrides AI safety restrictions, and one paper refers to a dataset of forbidden prompts from the Do Anything Now jailbreak family. Separately, one paper uses the same name for "Expose Backdoors on the Way," a feature-based textual backdoor defense method evaluated against Query-Attack and Observation-Attack on WebShop.

**What it is claimed to measure.** Across the linked relationships, papers use it to measure two constructs, Safety and Safety robustness, and no behavioral indicators are linked to it. The reported measurement claims stay within this safety framing: one paper says it uses AdvBench and DoAnythingNow to assess the safety of LLMs, while another reports performance on the DoAnythingNow benchmark as part of its safety evaluation.

**Space of uses.** Papers do not link it to other measurement instruments. In use, it is positioned as a standalone safety or jailbreak evaluation, sometimes mentioned alongside STRONGREJECT, JAILBREAKV, and AdvBench, and some authors use DAN 13.0 specifically as a baseline bypass prompt to benchmark another method against an "established bypass." Another paper instead treats DAN as a defense method and reports its defending performance against Query-Attack and Observation-Attack on the WebShop dataset.

## Sources

**DAN** (4 papers: [TRIDENT: Enhancing Large Language Model Safety with Tri-Dimensional Diversified Red-Teaming Data Synthesis](https://aclanthology.org/2025.acl-long.733.pdf), [CoBia: Constructed Conversations Can Trigger Otherwise Concealed Societal Biases in LLMs](https://aclanthology.org/2025.emnlp-main.84.pdf), [A StrongREJECT for Empty Jailbreaks](https://proceedings.neurips.cc/paper_files/paper/2024/file/e2e06adf560b0706d3b1ddfca9f29756-Paper-Datasets_and_Benchmarks_Track.pdf), [Watch Out for Your Agents! Investigating Backdoor Threats to LLM-Based Agents](https://proceedings.neurips.cc/paper_files/paper/2024/file/b6e9d6f4f3428cd5f3f9e9bbae2cab10-Paper-Conference.pdf))
> A benchmark collection of jailbreak-enhanced instructions used to evaluate a model's resilience against diverse jailbreak attacks.

**DoAnythingNow** (1 paper: [Automatic Expert Discovery in LLM Upcycling via Sparse Interpolated Mixture-of-Experts](https://aclanthology.org/2025.acl-long.816.pdf))
> Benchmark designed to evaluate model safety by testing resilience against malicious instructions and jailbreak attacks.

## Relationships

### → DAN
- **Safety robustness** (construct): *measured_by*, 1 paper
  > use the AdvBench and DoAnythingNow (Shen et al., 2024) datasets to assess the safety of the LLMs. (Section 4.2.2)
  - [LSSF: Safety Alignment for Large Language Models through Low-Rank Safety Subspace Fusion](https://aclanthology.org/2025.acl-long.1479.pdf)
- **Safety** (construct): *measured_by*, 1 paper
  > Notably, SIMoE obtains excellent safety evaluation metrics, outperforming Tülu-v3-8B-SFT by 1.7% on Safety (Tab. 2), and a remarkable 10% on the DoAnythingNow (Shen et al., 2024) benchmark in particular (Tab. A9, detailed safety results across sub-datasets). (Section 4.2)
  - [Automatic Expert Discovery in LLM Upcycling via Sparse Interpolated Mixture-of-Experts](https://aclanthology.org/2025.acl-long.816.pdf)
