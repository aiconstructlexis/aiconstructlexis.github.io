# Safety
**Type:** Construct  
**Supporting papers:** 122  
**Also known as:** Security alignment, LLM security, Safety capability, Safety performance, Trust and safety  

## State of the Field

**Space of definitions.** Across the surveyed work, the prevailing usage treats safety as a latent model or agent property, variously called a disposition, ability, capability, or performance, to avoid harmful, unsafe, toxic, offensive, unethical, illegal, or dangerous outputs, often while aligning with human values or societal norms, especially under malicious, adversarial, or unsafe prompts. Many papers make refusal central, and one explicitly states that safety means "stopping models from following malicious instructions and generating toxic content"; other definitions describe it as refusing unsafe requests or producing benign responses to unsafe prompts. Definitions differ mainly on scope: most stay at text generation, some extend to tool use and environment interaction, and a broader "trust and safety" framing centers on protecting users from harm, misinformation, abuse, and unsafe content while fostering confidence.

**Space of facets.** Papers organize the term in several ways. A recurring pattern is to place safety as one axis within broader multidimensional evaluations or as one core capability of language or vision-language models. A smaller line of work uses nearby labels differently: harmlessness is sometimes used interchangeably with safety, while security alignment names the process of keeping behavior within safe boundaries and LLM security the resulting property of recognizing and refusing malicious questions. Some evaluations further structure safety through refusal versus compliance, toxicity, jailbreaking, overcautiousness, and risky agent actions.

**Space of measurement.** Papers operationalize safety with 29 linked measurement instruments and 6 linked behavioral indicators. The most recurrent instruments are AdvBench, RewardBench, ToxiGen, TruthfulQA, and Llama Guard 2, with 24 other instruments also linked; benchmarks dominate, complemented by human pairwise judgments and LLM or moderation judges. Across these measures, safety is scored through refusal rates, attack success rates, safer-response win rates, toxicity or harmfulness classifications, preferences for refusal over compliance, and scalar safety ratings, which mostly track the dominant definitions of refusing harmful requests or avoiding toxic output, though some instruments extend the construct to multimodal, multilingual, and agent settings.

**Links.** Across 11 linked constructs, papers most often connect safety to alignment, harmlessness, helpfulness, toxicity, and backdoor vulnerability, with other constructs appearing less often. Several papers claim a causal relationship from Alignment to Safety, while the other frequent links are recorded as related: harmlessness is sometimes treated as interchangeable with safety, helpfulness is discussed as something to balance against safety, and toxicity and backdoor vulnerability are framed as safety problems or threats. Smaller strands add two more causal claims and several related ties to behavioral indicators and other constructs, and no correlations are reported.

## Sources

**Safety** (18 papers: [CRITIC: Large Language Models Can Self-Correct with Tool-Interactive Critiquing](https://proceedings.iclr.cc/paper_files/paper/2024/file/fef126561bbf9d4467dbb8d27334b8fe-Paper-Conference.pdf), [Identifying the Risks of LM Agents with an LM-Emulated Sandbox](https://proceedings.iclr.cc/paper_files/paper/2024/file/7274ed909a312d4d869cc328ad1c5f04-Paper-Conference.pdf), [Leftover Lunch: Advantage-based Offline Reinforcement Learning for Language Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/3b18d368150474ac6fc9bb665d3eb3da-Paper-Conference.pdf), [Safety-Tuned LLaMAs: Lessons From Improving the Safety of Large Language Models that Follow Instructions](https://proceedings.iclr.cc/paper_files/paper/2024/file/9178ece87f0a5d6558f49f43ec1e8a1a-Paper-Conference.pdf), [Test-Time Training on Nearest Neighbors for Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/f02f1185b97518ab5bd7ebde466992d3-Paper-Conference.pdf), [VHELM: A Holistic Evaluation of Vision Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/fe2fc7dc60b55ccd8886220b40fb1f74-Paper-Datasets_and_Benchmarks_Track.pdf), [A Distributional Approach to Uncertainty-Aware Preference Alignment Using Offline Demonstrations](https://proceedings.iclr.cc/paper_files/paper/2025/file/084cf2b3d73abafa1705336a0e9ebb1c-Paper-Conference.pdf), [Improve Safety Training of Large Language Models with Safety-Critical Singular Vectors Localization](https://aclanthology.org/2025.acl-long.245.pdf), [Biased Tales: Cultural and Topic Bias in Generating Children's Stories](https://aclanthology.org/2025.emnlp-main.3.pdf), [SafetyQuizzer: Timely and Dynamic Evaluation on the Safety of LLMs](https://aclanthology.org/2025.naacl-long.85.pdf), [Arabic Dataset for LLM Safeguard Evaluation](https://aclanthology.org/2025.naacl-long.285.pdf), [From Distributional to Overton Pluralism: Investigating Large Language Model Alignment](https://aclanthology.org/2025.naacl-long.346.pdf), [DPL: Diverse Preference Learning Without A Reference Model](https://aclanthology.org/2025.naacl-long.190.pdf), [MICE for CATs: Model-Internal Confidence Estimation for Calibrating Agents with Tools](https://aclanthology.org/2025.naacl-long.615.pdf), [RAG LLMs are Not Safer: A Safety Analysis of Retrieval-Augmented Generation for Large Language Models](https://aclanthology.org/2025.naacl-long.281.pdf), [Goal-Conditioned DPO: Prioritizing Safety in Misaligned Instructions](https://aclanthology.org/2025.naacl-long.369.pdf), [Exploring Safety-Utility Trade-Offs in Personalized Language Models](https://aclanthology.org/2025.naacl-long.565.pdf), [The BiGGen Bench: A Principled Benchmark for Fine-grained Evaluation of Language Models with Language Models](https://aclanthology.org/2025.naacl-long.303.pdf))
> The model's disposition to avoid generating harmful, unethical, or dangerous content, particularly in response to adversarial prompts.

**Security alignment** (1 paper: [Safety Layers in Aligned Large Language Models: The Key to LLM Security](https://proceedings.iclr.cc/paper_files/paper/2025/file/f3bfbd65743e60c685a3845bd61ce15f-Paper-Conference.pdf))
> The extent to which an LLM has been aligned to distinguish malicious from normal inputs and keep its behavior within safe boundaries.

**LLM security** (1 paper: [Safety Layers in Aligned Large Language Models: The Key to LLM Security](https://proceedings.iclr.cc/paper_files/paper/2025/file/f3bfbd65743e60c685a3845bd61ce15f-Paper-Conference.pdf))
> The model-level property of resisting harmful or malicious prompts by refusing unsafe requests and avoiding harmful outputs.

**Safety capability** (1 paper: [On the Role of Attention Heads in Large Language Model Safety](https://proceedings.iclr.cc/paper_files/paper/2025/file/d0bcff6425bbf850ec87d5327a965db9-Paper-Conference.pdf))
> The latent property of a large language model that enables it to align with human values by avoiding the generation of unsafe, toxic, or harmful content in response to queries.

**Safety performance** (1 paper: [MPO: Multilingual Safety Alignment via Reward Gap Optimization](https://aclanthology.org/2025.acl-long.1149.pdf))
> The underlying trait reflecting how effectively a model resists generating unsafe content, inferred from patterns of refusal across diverse linguistic and cultural contexts.

**Trust and safety** (1 paper: [Position: Generative AI Regulation Can Learn from Social Media Regulation](https://raw.githubusercontent.com/mlresearch/v267/main/assets/appel25a/appel25a.pdf))
> The latent property of a system that ensures user protection from harm, including misinformation, abuse, and unsafe content, while fostering user confidence in the technology.

## Relationships

### Safety →
- **AdvBench** (measurement instrument): *measured_by*, 6 papers
  > Also, we wonder if weakening model’s exaggerated safety will also lead to a drop in its overall safety, hence we conducted another experiment on AdvBench (Zou et al. [2023b]), which contains 500 harmful instructions. (Section 4.2)
  - [Enhancing Multiple Dimensions of Trustworthiness in LLMs via Sparse Activation Control](https://proceedings.neurips.cc/paper_files/paper/2024/file/1cb5b3d64bdf3c6642c8d9a8fbecd019-Paper-Conference.pdf)
  - [PaCE: Parsimonious Concept Engineering for Large Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/b3cca813dcd78fe75e4d4df2e6a0b1a7-Paper-Conference.pdf)
  - [Beware of Your Po! Measuring and Mitigating AI Safety Risks in Role-Play Fine-Tuning of LLMs](https://aclanthology.org/2025.acl-long.544.pdf)
  - [Constrain Alignment with Sparse Autoencoders](https://raw.githubusercontent.com/mlresearch/v267/main/assets/yin25a/yin25a.pdf)
  - [Assessing Safety Risks and Quantization-aware Safety Patching for Quantized Large Language Models](https://raw.githubusercontent.com/mlresearch/v267/main/assets/chen25ci/chen25ci.pdf)
  - [SaLoRA: Safety-Alignment Preserved Low-Rank Adaptation](https://proceedings.iclr.cc/paper_files/paper/2025/file/e24d9d028e3c7f6f13e6032919ee021e-Paper-Conference.pdf)
- **ToxiGen** (measurement instrument): *measured_by*, 5 papers
  > Results of MOD ... achieving precise control over general capabilities, including safety (Toxigen), coding (Codex), and reasoning (∗ COT).
  - [Decoding-Time Language Model Alignment with Multiple Objectives](https://proceedings.neurips.cc/paper_files/paper/2024/file/57c89126d60c209f48d0e6395c766bb3-Paper-Conference.pdf)
  - [Unpacking DPO and PPO: Disentangling Best Practices for Learning from Preference Feedback](https://proceedings.neurips.cc/paper_files/paper/2024/file/404df2480b6eef0486a1679e371894b0-Paper-Conference.pdf)
  - [Instruction Tuning With Loss Over Instructions](https://proceedings.neurips.cc/paper_files/paper/2024/file/7ffb43adf37b3eeaba559098bc084cc6-Paper-Conference.pdf)
  - [Should We Really Edit Language Models? On the Evaluation of Edited Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/370fa2e691f57eb319bc263a07dad4a5-Paper-Conference.pdf)
  - [Data Mixing Optimization for Supervised Fine-Tuning of Large Language Models](https://raw.githubusercontent.com/mlresearch/v267/main/assets/li25bh/li25bh.pdf)
- **RewardBench** (measurement instrument): *measured_by*, 5 papers
  > RewardBench is a new benchmark designed to evaluate the capabilities and safety of reward models (Section 4).
  - [Regularizing Hidden States Enables Learning Generalizable Reward Model for LLMs](https://proceedings.neurips.cc/paper_files/paper/2024/file/71f7154547c748c8041505521ca433ab-Paper-Conference.pdf)
  - [HelpSteer 2: Open-source dataset for training top-performing reward models](https://proceedings.neurips.cc/paper_files/paper/2024/file/02fd91a387a6a5a5751e81b58a75af90-Paper-Datasets_and_Benchmarks_Track.pdf)
  - [OpenPRM: Building Open-domain Process-based Reward Models with Preference Trees](https://proceedings.iclr.cc/paper_files/paper/2025/file/c919a2b5ec1de69f2629f9119676e336-Paper-Conference.pdf)
  - [HelpSteer2-Preference: Complementing Ratings with Preferences](https://proceedings.iclr.cc/paper_files/paper/2025/file/8e237ec6d3bc86f6d4967e9c7eef37ff-Paper-Conference.pdf)
  - [Improving Model Alignment Through Collective Intelligence of Open-Source Models](https://raw.githubusercontent.com/mlresearch/v267/main/assets/wang25dr/wang25dr.pdf)
- **TruthfulQA** (measurement instrument): *measured_by*, 5 papers
  > Safety and Helpfulness comprises TruthfulQA [38], ToxiGen [21], and Hendrycks Ethics [23]. (Section 4.1)
  - [Instruction Tuning With Loss Over Instructions](https://proceedings.neurips.cc/paper_files/paper/2024/file/7ffb43adf37b3eeaba559098bc084cc6-Paper-Conference.pdf)
  - [Should We Really Edit Language Models? On the Evaluation of Edited Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/370fa2e691f57eb319bc263a07dad4a5-Paper-Conference.pdf)
  - [Jamba: Hybrid Transformer-Mamba Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/a9ed43fa31dc8b4a7d7a673d713dcb5f-Paper-Conference.pdf)
  - [Model Swarms: Collaborative Search to Adapt LLM Experts via Swarm Intelligence](https://raw.githubusercontent.com/mlresearch/v267/main/assets/feng25o/feng25o.pdf)
  - [Data Mixing Optimization for Supervised Fine-Tuning of Large Language Models](https://raw.githubusercontent.com/mlresearch/v267/main/assets/li25bh/li25bh.pdf)
- **XSTest** (measurement instrument): *measured_by*, 3 papers
  > We evaluate models on 11 different benchmarks, covering skills such as ... safety (ToxiGen [19], XSTest [42]) (Section 2.2).
  - [Unpacking DPO and PPO: Disentangling Best Practices for Learning from Preference Feedback](https://proceedings.neurips.cc/paper_files/paper/2024/file/404df2480b6eef0486a1679e371894b0-Paper-Conference.pdf)
  - [Test-Time Preference Optimization: On-the-Fly Alignment via Iterative Textual Feedback](https://raw.githubusercontent.com/mlresearch/v267/main/assets/li25ac/li25ac.pdf)
  - [Aligning Spoken Dialogue Models from User Interactions](https://raw.githubusercontent.com/mlresearch/v267/main/assets/wu25t/wu25t.pdf)
- **Llama Guard 2** (measurement instrument): *measured_by*, 3 papers
  > In our experiments, we use Llama Guard 2 (Meta, 2024) to measure how safe (conversely, how harmful) a conversation is. (Section 6.1)
  - [Broaden your SCOPE! Efficient Multi-turn Conversation Planning for LLMs with Semantic Space](https://proceedings.iclr.cc/paper_files/paper/2025/file/32e41d6b0a51a63a9a90697da19d235d-Paper-Conference.pdf)
  - [Forewarned is Forearmed: Harnessing LLMs for Data Synthesis via Failure-induced Exploration](https://proceedings.iclr.cc/paper_files/paper/2025/file/1cded4f97cf5f01a284c574110b7e3b9-Paper-Conference.pdf)
  - [RAG LLMs are Not Safer: A Safety Analysis of Retrieval-Augmented Generation for Large Language Models](https://aclanthology.org/2025.naacl-long.281.pdf)
- **LLM-as-a-judge** (measurement instrument): *measured_by*, 2 papers
  > We use GPT-4 [1] to measure the helpfulness and harmlessness (i.e., safety) of the responses generated by the LM policies.
  - [Stepwise Alignment for Constrained Language Model Policy Optimization](https://proceedings.neurips.cc/paper_files/paper/2024/file/bcfcf7232cb74e1ef82d751880ff835b-Paper-Conference.pdf)
  - [DPL: Diverse Preference Learning Without A Reference Model](https://aclanthology.org/2025.naacl-long.190.pdf)
- **HarmBench** (measurement instrument): *measured_by*, 2 papers
  > We evaluate the safety performance of the models on the standard version of HarmBench(Mazeika et al., 2024), which consists of 200 harmful instructions. (Section 4.2).
  - [Improve Safety Training of Large Language Models with Safety-Critical Singular Vectors Localization](https://aclanthology.org/2025.acl-long.245.pdf)
  - [Learning Safety Constraints for Large Language Models](https://raw.githubusercontent.com/mlresearch/v267/main/assets/chen25b/chen25b.pdf)
- **MM-SafetyBench** (measurement instrument): *measured_by*, 2 papers
  > We evaluate the VLMs with MM-Safety-Bench [28] to judge the resiliency of VLMs when they are prompted with harm-inducing instructions. (Section 3.1)
  - [VHELM: A Holistic Evaluation of Vision Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/fe2fc7dc60b55ccd8886220b40fb1f74-Paper-Datasets_and_Benchmarks_Track.pdf)
  - [How Does Vision-Language Adaptation Impact the Safety of Vision Language Models?](https://proceedings.iclr.cc/paper_files/paper/2025/file/84d286e32bbee8fa3a86ee9c50e00081-Paper-Conference.pdf)
- **RealToxicityPrompts** (measurement instrument): *measured_by*, 2 papers
  > Finally, we report safety evaluations on RealToxicity (Gehman et al., 2020) and TruthfulQA (Lin et al., 2022). (Section 7.2)
  - [Jamba: Hybrid Transformer-Mamba Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/a9ed43fa31dc8b4a7d7a673d713dcb5f-Paper-Conference.pdf)
  - [Model Swarms: Collaborative Search to Adapt LLM Experts via Swarm Intelligence](https://raw.githubusercontent.com/mlresearch/v267/main/assets/feng25o/feng25o.pdf)
- **StrongREJECT** (measurement instrument): *measured_by*, 2 papers
  > For evaluating safety, we use do-not-answer (DNA) (Wang et al., 2023) and StrongReject (Souly et al., 2024) datasets. (Section 3)
  - [Exploring Safety-Utility Trade-Offs in Personalized Language Models](https://aclanthology.org/2025.naacl-long.565.pdf)
  - [Reasoning Model Unlearning: Forgetting Traces, Not Just Answers, While Preserving Reasoning Skills](https://aclanthology.org/2025.emnlp-main.220.pdf)
- **HEx-PHI** (measurement instrument): *measured_by*, 2 papers
  > For the former, we use three widely recognized safety benchmarks. Specifically, we include all 520 harmful samples from AdvBench (Zou et al., 2023), all 330 samples from HEx-PHI (Qi et al., 2024b), and a randomly selected subset of 1,000 samples from BeaverTails (Ji et al., 2024).
  - [Beware of Your Po! Measuring and Mitigating AI Safety Risks in Role-Play Fine-Tuning of LLMs](https://aclanthology.org/2025.acl-long.544.pdf)
  - [Safe Delta: Consistently Preserving Safety when Fine-Tuning LLMs on Diverse Datasets](https://raw.githubusercontent.com/mlresearch/v267/main/assets/lu25g/lu25g.pdf)
- **HH-RLHF** (measurement instrument): *measured_by*, 1 paper
  > we applied our approach to HH-RLHF (Anthropic, 2022), a commonly used preference dataset for safety alignment. (Section 5.2)
  - [RuleAdapter: Dynamic Rules for training Safety Reward Models in RLHF](https://raw.githubusercontent.com/mlresearch/v267/main/assets/li25o/li25o.pdf)
- **MaliciousInstruct** (measurement instrument): *measured_by*, 1 paper
  > We attack LLM using jailbreak methods on the AdvExtent (Lu et al., 2024) and MaliciousInstruct (Huang et al., 2024), collect responses, and use the string matching method... to identify whether responses lacked keywords indicating instruction rejection. (Section 6.1)
  - [Safety Alignment via Constrained Knowledge Unlearning](https://aclanthology.org/2025.acl-long.1240.pdf)
- **SORRY-Bench** (measurement instrument): *measured_by*, 1 paper
  > For text-only safety, we use SorryBench (Xie et al., 2024) and WildJailbreak (Jiang et al., 2024) (Section 3.3)
  - [How Does Vision-Language Adaptation Impact the Safety of Vision Language Models?](https://proceedings.iclr.cc/paper_files/paper/2025/file/84d286e32bbee8fa3a86ee9c50e00081-Paper-Conference.pdf)
- **SIUO** (measurement instrument): *measured_by*, 1 paper
  > for multimodal safety, we utilize MM-Safetybench (Liu et al., 2023c), SIUO (Wang et al., 2024), and Figstep (Gong et al., 2023a). (Section 3.3)
  - [How Does Vision-Language Adaptation Impact the Safety of Vision Language Models?](https://proceedings.iclr.cc/paper_files/paper/2025/file/84d286e32bbee8fa3a86ee9c50e00081-Paper-Conference.pdf)
- **FigStep** (measurement instrument): *measured_by*, 1 paper
  > for multimodal safety, we utilize MM-Safetybench (Liu et al., 2023c), SIUO (Wang et al., 2024), and Figstep (Gong et al., 2023a). (Section 3.3)
  - [How Does Vision-Language Adaptation Impact the Safety of Vision Language Models?](https://proceedings.iclr.cc/paper_files/paper/2025/file/84d286e32bbee8fa3a86ee9c50e00081-Paper-Conference.pdf)
- **Llama Guard 3** (measurement instrument): *measured_by*, 1 paper
  > To measure ASR, we utilize LLaMA-Guard 3 8B (Inan et al., 2023), a LLM trained for content safety classification. (Section 3.4)
  - [How Does Vision-Language Adaptation Impact the Safety of Vision Language Models?](https://proceedings.iclr.cc/paper_files/paper/2025/file/84d286e32bbee8fa3a86ee9c50e00081-Paper-Conference.pdf)
- **JailbreakBench** (measurement instrument): *measured_by*, 1 paper
  > We evaluated Jailbreak Antidote using JailbreakBench (Chao et al., 2024) for assessing safety, focusing on 100 harmful prompts. (Section 5.1)
  - [Jailbreak Antidote: Runtime Safety-Utility Balance via Sparse Representation Adjustment in Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/36e3f9e6162d597adada4e0e4fce6861-Paper-Conference.pdf)
- **OpenAI Moderation API** (measurement instrument): *measured_by*, 1 paper
  > To address this limitation, we used the OpenAI Moderation API as a secondary evaluation method. This API provides both a harmfulness score (in [0,1]), where 0 is the least harmful and 1 the most harmful) and a binary tag indicating whether the response is safe.
  - [Semantic Loss Guided Data Efficient Supervised Fine Tuning for Safe Responses in LLMs](https://proceedings.iclr.cc/paper_files/paper/2025/file/598ec93b6d2ed4fed4927b957b80f18c-Paper-Conference.pdf)
- **BeaverTails** (measurement instrument): *measured_by*, 1 paper
  > Conversely, further introducing unsafe guidelines into the system prompt reduces the safety performance on BeaverTails (Ji et al., 2024) (91.40 vs. 63.30). (Section 2.2)
  - [Beware of Your Po! Measuring and Mitigating AI Safety Risks in Role-Play Fine-Tuning of LLMs](https://aclanthology.org/2025.acl-long.544.pdf)
- **DAN** (measurement instrument): *measured_by*, 1 paper
  > Notably, SIMoE obtains excellent safety evaluation metrics, outperforming Tülu-v3-8B-SFT by 1.7% on Safety (Tab. 2), and a remarkable 10% on the DoAnythingNow (Shen et al., 2024) benchmark in particular (Tab. A9, detailed safety results across sub-datasets). (Section 4.2)
  - [Automatic Expert Discovery in LLM Upcycling via Sparse Interpolated Mixture-of-Experts](https://aclanthology.org/2025.acl-long.816.pdf)
- **TRACE** (measurement instrument): *measured_by*, 1 paper
  > TRACE, another continual instruction tuning benchmark, is designed to evaluate the general ability, instruction following, and safety for LLMs (Wang et al., 2023). (Section 2. Related Work)
  - [Large Continual Instruction Assistant](https://raw.githubusercontent.com/mlresearch/v267/main/assets/qiao25e/qiao25e.pdf)
- **BeaverTails-Evaluation** (measurement instrument): *measured_by*, 1 paper
  > We evaluate our models using a comprehensive set of benchmarks that address various aspects, including... safety (BeaverTails-Evaluation Ji et al., 2023 and XSTest R¨ottger et al., 2024) (Section 5).
  - [Test-Time Preference Optimization: On-the-Fly Alignment via Iterative Textual Feedback](https://raw.githubusercontent.com/mlresearch/v267/main/assets/li25ac/li25ac.pdf)
- **FINTRUST** (measurement instrument): *measured_by*, 1 paper
  > we curate 15, 680 instances to evaluate LLM trustworthiness in the financial domain. We ... incorporate seven core dimensions: Truthfulness, Safety, Fairness, Robustness, Privacy, Transparency, and Knowledge Discovery. (Section 2)
  - [FinTrust: A Comprehensive Benchmark of Trustworthiness Evaluation in Finance Domain](https://aclanthology.org/2025.emnlp-main.512.pdf)
- **VoiceBench** (measurement instrument): *measured_by*, 1 paper
  > For example, VoiceBench (Chen et al., 2024c) and Roh et al. (2025) synthesize datasets like AdvBench (Zou et al., 2023) into spoken queries, evaluating LALMs on their ability to reject them.
  - [Towards Holistic Evaluation of Large Audio-Language Models: A Comprehensive Survey](https://aclanthology.org/2025.emnlp-main.514.pdf)
- **PKU-SafeRLHF** (measurement instrument): *measured_by*, 1 paper
  > We evaluate model safety on the PKU-SafeRLHF and BigBench-HHH datasets. (Section 4.1)
  - [Governance in Motion: Co-evolution of Constitutions and AI models for Scalable Safety](https://aclanthology.org/2025.emnlp-main.869.pdf)
- **PLLuM-Align** (measurement instrument): *measured_by*, 1 paper
  > For scalar multi-attribute rating, annotators evaluated each response on a 5-point Likert scale across seven criteria: i) truthfulness, (ii) linguistic correctness, (iii) safety, (iv) fairness, (v) conciseness, (vi) coherence & reasoning, as well as vii) helpfulness & instruction-following.
  - [PLLuM-Align: Polish Preference Dataset for Large Language Model Alignment](https://aclanthology.org/2025.emnlp-main.1219.pdf)
- **AgentHarm** (measurement instrument): *measured_by*, 1 paper
  > AgentHarm (Andriushchenko et al., 2024) measures the potential harm from agents executing malicious tasks.
  - [OS Agents: A Survey on MLLM-based Agents for Computer, Phone and Browser Use](https://aclanthology.org/2025.acl-long.369.pdf)

### → Safety
- **Alignment** (construct): *causes*, 3 papers
  > “Alignment methods are designed to reduce such undesirable outputs”
  - [PaCE: Parsimonious Concept Engineering for Large Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/b3cca813dcd78fe75e4d4df2e6a0b1a7-Paper-Conference.pdf)
  - [BOND: Aligning LLMs with Best-of-N Distillation](https://proceedings.iclr.cc/paper_files/paper/2025/file/947f37882a394140f7add476bb99d1d3-Paper-Conference.pdf)
  - [PLLuM-Align: Polish Preference Dataset for Large Language Model Alignment](https://aclanthology.org/2025.emnlp-main.1219.pdf)
- **Safe response generation** (behavioral indicator): *causes*, 1 paper
  > Improving Safety by Response Detoxification (Section 4.1).
  - [PaCE: Parsimonious Concept Engineering for Large Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/b3cca813dcd78fe75e4d4df2e6a0b1a7-Paper-Conference.pdf)
- **Interpretability and explainability** (construct): *causes*, 1 paper
  > The embedded interpretability empowers users to transparently identify harmful content, steer model behavior, and unlearn undesired concepts – significantly enhancing the safety, reliability, and trustworthiness of LLMs, which are critical capabilities notably absent in existing language models.
  - [Concept Bottleneck Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/de4ce91dfe56b919ee1c228d6a78f866-Paper-Conference.pdf)

### Associated with
- **Harmlessness** (construct), 2 papers
  > safety assesses harmlessness (Section 4.1).
  - [Style Outweighs Substance: Failure Modes of LLM Judges in Alignment Benchmarking](https://proceedings.iclr.cc/paper_files/paper/2025/file/1eb36d07ebb13be16ddbda679a95018b-Paper-Conference.pdf)
  - [A Simple Yet Effective Method for Non-Refusing Context Relevant Fine-grained Safety Steering in LLMs](https://aclanthology.org/2025.emnlp-main.1781.pdf)
- **Toxicity** (construct), 2 papers
  > Two most significant topics in the literature of large model safety [124, 132] are the toxicity of AI-generated content [47], which could greatly impact user interactions, and model jailbreaking (Sec. 2.2.2)
  - [MultiTrust: A Comprehensive Benchmark Towards Trustworthy Multimodal Large Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/586640cda3db2dc77349013dcefee456-Paper-Datasets_and_Benchmarks_Track.pdf)
  - [CARES: A Comprehensive Benchmark of Trustworthiness in Medical Vision Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/fde7f40f8ced5735006810534dc66b33-Paper-Datasets_and_Benchmarks_Track.pdf)
- **Helpfulness** (construct), 2 papers
  > α is a hyperparameter to adjust the balance between safety and usefulness.
  - [Adaptive Deployment of Untrusted LLMs Reduces Distributed Threats](https://proceedings.iclr.cc/paper_files/paper/2025/file/699c5a2bb87a8aa32c4ad541d9997361-Paper-Conference.pdf)
  - [How Does Vision-Language Adaptation Impact the Safety of Vision Language Models?](https://proceedings.iclr.cc/paper_files/paper/2025/file/84d286e32bbee8fa3a86ee9c50e00081-Paper-Conference.pdf)
- **Trustworthiness** (construct), 1 paper
  > We assess the trustworthiness of Med-LVLMs across five dimensions, including trustfulness, fairness, safety, privacy, and robustness. (Abstract)
  - [CARES: A Comprehensive Benchmark of Trustworthiness in Medical Vision Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/fde7f40f8ced5735006810534dc66b33-Paper-Datasets_and_Benchmarks_Track.pdf)
- **Robustness** (construct), 1 paper
  > We assert that robustness is fundamentally insufficient for ensuring safety goals due to inferential threats from dual-intent queries, with current defenses and evaluations failing to account for these risks. (Section 1)
  - [Breach By A Thousand Leaks: Unsafe Information Leakage in 'Safe' AI Responses](https://proceedings.iclr.cc/paper_files/paper/2025/file/801a6708014185e951a95108b8cc8349-Paper-Conference.pdf)
- **Backdoor vulnerability** (construct), 1 paper
  > In this work, we take the first step to investigate one of the typical safety threats, backdoor attack, to LLM-based agents. (Abstract)
  - [Watch Out for Your Agents! Investigating Backdoor Threats to LLM-Based Agents](https://proceedings.neurips.cc/paper_files/paper/2024/file/b6e9d6f4f3428cd5f3f9e9bbae2cab10-Paper-Conference.pdf)
- **Text generation quality** (construct), 1 paper
  > In such applications, the quality (e.g., user engagement, safety) of a conversation is important and can only be exactly known at the end of the conversation. (ABSTRACT)
  - [Broaden your SCOPE! Efficient Multi-turn Conversation Planning for LLMs with Semantic Space](https://proceedings.iclr.cc/paper_files/paper/2025/file/32e41d6b0a51a63a9a90697da19d235d-Paper-Conference.pdf)
- **Refusal** (behavioral indicator), 1 paper
  > These insights highlight that LLM safety relies on maximizing the probability of generating rejection tokens in response to harmful queries. (Section 2)
  - [On the Role of Attention Heads in Large Language Model Safety](https://proceedings.iclr.cc/paper_files/paper/2025/file/d0bcff6425bbf850ec87d5327a965db9-Paper-Conference.pdf)
- **Instruction following** (behavioral indicator), 1 paper
  > this balance creates vulnerabilities when the model’s instruction-following objective from u conflicts with the safety goals defined in g.
  - [Goal-Conditioned DPO: Prioritizing Safety in Misaligned Instructions](https://aclanthology.org/2025.naacl-long.369.pdf)
- **Ethical alignment** (construct), 1 paper
  > Ethical Considerations assess adherence to ethical principles, including safety, privacy, fairness, and harm avoidance, ensuring responses are free from harmful or biased content. (Section 2.3)
  - [MM-RLHF: The Next Step Forward in Multimodal LLM Alignment](https://raw.githubusercontent.com/mlresearch/v267/main/assets/zhang25cs/zhang25cs.pdf)
- **Overrefusal** (behavioral indicator), 1 paper
  > Bianchi et al. (2023) highlights that incorporating safety-related examples during finetuning enhances model safety but often results in increased overrefusal. (Section 2.1. Instruction Finetuning)
  - [POROver: Improving Safety and Reducing Overrefusal in Large Language Models with Overgeneration and Preference Optimization](https://raw.githubusercontent.com/mlresearch/v267/main/assets/karaman25a/karaman25a.pdf)
- **Harmful content generation** (behavioral indicator), 1 paper
  > Here, safety is defined as stopping models from following malicious instructions and generating toxic content. (Section 3)
  - [Safety-Tuned LLaMAs: Lessons From Improving the Safety of Large Language Models that Follow Instructions](https://proceedings.iclr.cc/paper_files/paper/2024/file/9178ece87f0a5d6558f49f43ec1e8a1a-Paper-Conference.pdf)
- **Harmful content detection** (behavioral indicator), 1 paper
  > Considering the potential harm that these memes may cause, this task can be used to evaluate the safety of LLMs. (Section 6)
  - [Towards Comprehensive Detection of Chinese Harmful Memes](https://proceedings.neurips.cc/paper_files/paper/2024/file/17fc467c11997914127c001fdc801bea-Paper-Datasets_and_Benchmarks_Track.pdf)
- **Impermissible information leakage** (construct), 1 paper
  > Thus, we propose to evaluate safety risk through Impermissible Information Leakage (IIL). (Section 3.1)
  - [Breach By A Thousand Leaks: Unsafe Information Leakage in 'Safe' AI Responses](https://proceedings.iclr.cc/paper_files/paper/2025/file/801a6708014185e951a95108b8cc8349-Paper-Conference.pdf)
