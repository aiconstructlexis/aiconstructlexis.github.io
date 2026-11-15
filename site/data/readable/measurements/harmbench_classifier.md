# HarmBench classifier
**Type:** Measurement instrument  
**Supporting papers:** 5  
**Also known as:** HarmBench Classifier, HarmBench evaluator, HarmBench judge, HarmBench-Llama2-13B-Chat  

## State of the Field

**What it is.** Across papers, the prevailing usage treats this as a HarmBench safety judge, an LLM-based classifier used to decide whether a model output is harmful or whether a response to a harmful instruction is unsafe. Definitions vary between an official HarmBench classifier of model response harmfulness, an evaluator used for HarmBench results, and a judge that checks whether a target response matches malicious intent and counts as a successful jailbreak. Some authors specify that it is fine-tuned from Llama-2-13B or refer to the HarmBench-Llama2-13B-Chat variant, while one paper places it as a baseline safety evaluator in a meta-evaluation.

**What it is claimed to measure.** Papers link it to 1 construct and 2 behavioral indicators. They use it to measure harmful content generation, assessing output safety or harmfulness and computing attack or adversarial success rates. They also use it to measure harmlessness, reporting the percentage of harmless responses or classifying whether prompting generated a harmful response, and it is reported as measuring jailbreaking through attack success rate using HarmBench's judge. These measurement claims are distributed across harmful content generation, harmlessness, and jailbreaking rather than concentrated on only one linked target.

**Space of uses.** Across the surveyed work, it is commonly positioned as the judge used in HarmBench evaluations: papers describe using it to determine whether a model's response to a harmful instruction is unsafe, to evaluate target LLM responses, and to make a binary success decision for jailbreak attacks, with one quoted passage formalizing it as Judge(Target(P), I) → {0, 1}. Papers use it to compute attack success rates, adversarial success rates, and harmless-response percentages, and one paper says it is deployed because of high alignment with human evaluations. Papers do not link it to any other measurement instrument, though one meta-evaluation places it alongside Llama-Guard-2-8B, MD-Judge, and WildGuard as a baseline safety evaluator.

## Sources

**HarmBench classifier** (1 paper: [Robust LLM safeguarding via refusal feature adversarial training](https://proceedings.iclr.cc/paper_files/paper/2025/file/1022661f3f43406065641f16ce25eafa-Paper-Conference.pdf))
> An LLM-as-a-judge safety classifier fine-tuned to assess whether model outputs are harmful.

**HarmBench Classifier** (1 paper: [SORRY-Bench: Systematically Evaluating Large Language Model Safety Refusal](https://proceedings.iclr.cc/paper_files/paper/2025/file/9622163c87b67fd5a4a0ec3247cf356e-Paper-Conference.pdf))
> A specific classifier from the HarmBench benchmark, used as a baseline safety evaluator in the meta-evaluation.

**HarmBench evaluator** (1 paper: [AdvPrompter: Fast Adaptive Adversarial Prompting for LLMs](https://raw.githubusercontent.com/mlresearch/v267/main/assets/paulus25a/paulus25a.pdf))
> LLM-based evaluation system used to determine if a model's response to a harmful instruction is unsafe, serving as a judge for attack success on the HarmBench dataset.

**HarmBench judge** (1 paper: [Adversarial Reasoning at Jailbreaking Time](https://raw.githubusercontent.com/mlresearch/v267/main/assets/sabbaghi25a/sabbaghi25a.pdf))
> A judge model/protocol from HarmBench that determines whether a target response matches the malicious intent and counts as a successful jailbreak.

**HarmBench-Llama2-13B-Chat** (1 paper: [Bi-Factorial Preference Optimization: Balancing Safety-Helpfulness in Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/ad77a15531fbccefa8be5e434b4b7908-Paper-Conference.pdf))
> A classifier used to judge whether generated responses are harmless or contain harmful content.

## Relationships

### → HarmBench classifier
- **Harmful content generation** (behavioral indicator): *measured_by*, 2 papers
  > To compute attack success rate, we use three LLM-as-a-judge models that are fine-tuned to assess output safety: the official HarmBench classifier... (Section 5)
  - [Robust LLM safeguarding via refusal feature adversarial training](https://proceedings.iclr.cc/paper_files/paper/2025/file/1022661f3f43406065641f16ce25eafa-Paper-Conference.pdf)
  - [Improving Large Language Model Safety with Contrastive Representation Learning](https://aclanthology.org/2025.emnlp-main.1430.pdf)
- **Harmlessness** (construct): *measured_by*, 2 papers
  > We report percentage of harmless responses based on the safety classifier HarmBench-Llama2-13B-Chat (Mazeika et al., 2024).
  - [Bi-Factorial Preference Optimization: Balancing Safety-Helpfulness in Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/ad77a15531fbccefa8be5e434b4b7908-Paper-Conference.pdf)
  - [Do as I do (Safely): Mitigating Task-Specific Fine-tuning Risks in Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/70de9e3948645a1be2de657f14d85c6d-Paper-Conference.pdf)
- **Jailbreaking** (behavioral indicator): *measured_by*, 1 paper
  > “we report the attack success rate (ASR) using HarmBench’s judge”
  - [REINFORCE Adversarial Attacks on Large Language Models: An Adaptive, Distributional, and Semantic Objective](https://raw.githubusercontent.com/mlresearch/v267/main/assets/geisler25a/geisler25a.pdf)
