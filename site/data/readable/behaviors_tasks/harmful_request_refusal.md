# Harmful request refusal
**Type:** Behavioral indicator  
**Supporting papers:** 30  
**Also known as:** Harmful content refusal, Refusal of harmful requests, Harmful query refusal, Safety refusal, Harmful instruction refusal, Harmful prompt refusal  

## State of the Field

**Space of definitions.** Across papers, the prevailing usage treats this as an observable model behavior: declining, explicitly rejecting, or abstaining from a substantive answer when a prompt is judged harmful, unsafe, unethical, illegal, malicious, or against safety policies or guidelines. Definitions vary in what counts as the refusal signal, from polite non-compliance and explicit refusal answers to common refusal messages such as “I’m sorry, but I can’t...”; one paper also notes that a completion can begin with “I can’t” and still continue with harmful content.

**Variants.** Papers use several near-equivalent names, including harmful content refusal, refusal of harmful requests, harmful query refusal, harmful instruction refusal, harmful prompt refusal, and, in a smaller line, safety refusal. The requests studied range from broad harmful or toxic instructions to examples involving cryptocurrency scams, fraud, malware creation, dangerous activities, and malicious requests, and one paper examines whether such refusals generalize to downstream browser agents.

**Space of elicitation and scores.** Four measurement instruments are linked to this behavior. Papers most often measure it with AdvBench and HarmBench, and also with SORRY-Bench and XSTest, describing these as harmful-behavior or safety-refusal evaluations that test whether models reject harmful requests. Scoring is frequently framed with ASR or jailbreak ASR, where non-refusal responses count against refusal; some papers operationalize this with rejection keyword sets, while others use score functions based on the absence of refusal and direct addressal of the prompt.

**What it is taken as evidence of.** Papers most commonly connect this behavior to alignment constructs. They claim causal relationships from Safety alignment and from Alignment to harmful request refusal, describing alignment as teaching models to reject harmful queries and to provide refusal responses on unsafe or inappropriate topics. A smaller line of work reports it as related to Harmlessness, using refusals as examples of avoiding assistance on unethical actions.

## Sources

**Harmful content refusal** (3 papers: [Decoding-Time Language Model Alignment with Multiple Objectives](https://proceedings.neurips.cc/paper_files/paper/2024/file/57c89126d60c209f48d0e6395c766bb3-Paper-Conference.pdf), [FlipAttack: Jailbreak LLMs via Flipping](https://raw.githubusercontent.com/mlresearch/v267/main/assets/liu25z/liu25z.pdf), [Progressively Label Enhancement for Large Language Model Alignment](https://raw.githubusercontent.com/mlresearch/v267/main/assets/liu25cg/liu25cg.pdf))
> Declining to generate content that violates safety policies or requests harmful actions.

**Refusal of harmful requests** (5 papers: [Robust Prompt Optimization for Defending Language Models Against Jailbreaking Attacks](https://proceedings.neurips.cc/paper_files/paper/2024/file/46ed503889ab232c21c1162340ee17b2-Paper-Conference.pdf), [Adversarial Reasoning at Jailbreaking Time](https://raw.githubusercontent.com/mlresearch/v267/main/assets/sabbaghi25a/sabbaghi25a.pdf), [Automated Red Teaming with GOAT: the Generative Offensive Agent Tester](https://raw.githubusercontent.com/mlresearch/v267/main/assets/pavlova25a/pavlova25a.pdf), [Safety Alignment Can Be Not Superficial With Explicit Safety Signals](https://raw.githubusercontent.com/mlresearch/v267/main/assets/li25av/li25av.pdf), [Diversity Helps Jailbreak Large Language Models](https://aclanthology.org/2025.naacl-long.238.pdf))
> The observable action of a language model declining to fulfill a user's request on the grounds that it is harmful, unethical, or against its safety guidelines.

**Harmful query refusal** (1 paper: [Benign Samples Matter! Fine-tuning On Outlier Benign Samples Severely Breaks Safety](https://raw.githubusercontent.com/mlresearch/v267/main/assets/guan25c/guan25c.pdf))
> The observable behavior of a model explicitly rejecting or declining to respond to a user prompt that is identified as harmful or unsafe.

**Harmful request refusal** (1 paper: [AutoBencher: Towards Declarative Benchmark Construction](https://proceedings.iclr.cc/paper_files/paper/2025/file/eb216114f3eaad22506fd1bc7bbff0ca-Paper-Conference.pdf))
> The observable behavior of a model declining to provide a substantive response to a prompt that requests harmful, unsafe, or unethical information.

**Safety refusal** (1 paper: [Aligned LLMs Are Not Aligned Browser Agents](https://proceedings.iclr.cc/paper_files/paper/2025/file/42f92b78a6695f60db0cd38b54d57a41-Paper-Conference.pdf))
> The model's underlying disposition to reject instructions that are harmful, malicious, dangerous, illegal, or unethical.

**Harmful instruction refusal** (1 paper: [Safe Delta: Consistently Preserving Safety when Fine-Tuning LLMs on Diverse Datasets](https://raw.githubusercontent.com/mlresearch/v267/main/assets/lu25g/lu25g.pdf))
> The observable behavior of declining to respond to prompts that are identified as harmful or against usage policies.

**Harmful prompt refusal** (1 paper: [Activation Space Interventions Can Be Transferred Between Large Language Models](https://raw.githubusercontent.com/mlresearch/v267/main/assets/oozeer25a/oozeer25a.pdf))
> The observable action of a model declining to provide a substantive response to a prompt identified as harmful or unsafe.

## Relationships

### Harmful request refusal →
- **AdvBench** (measurement instrument): *measured_by*, 2 papers
  > “we evaluate on the first 80 prompts of AdvBench [51] ‘Harmful Behaviors’ split (Adv 80) with ASR as the safety metric.”
  - [Navigating the Safety Landscape: Measuring Risks in Finetuning Large Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/ada93fa6643735f294be51dc31eebbd4-Paper-Conference.pdf)
  - [The Logical Implication Steering Method for Conditional Interventions on Transformer Generation](https://raw.githubusercontent.com/mlresearch/v267/main/assets/kalajdzievski25a/kalajdzievski25a.pdf)
- **HarmBench** (measurement instrument): *measured_by*, 2 papers
  > In the harmful request refusal setting... We use a static set of test cases from HarmBench... to evaluate jailbreak ASR (Section 3.2).
  - [Tamper-Resistant Safeguards for Open-Weight LLMs](https://proceedings.iclr.cc/paper_files/paper/2025/file/fc49a629d33bc2461ed7a715ce44da68-Paper-Conference.pdf)
  - [AutoBencher: Towards Declarative Benchmark Construction](https://proceedings.iclr.cc/paper_files/paper/2025/file/eb216114f3eaad22506fd1bc7bbff0ca-Paper-Conference.pdf)
- **XSTest** (measurement instrument): *measured_by*, 1 paper
  > we compare with XSTest (Röttger et al., 2024) and HarmBench (Mazeika et al., 2024), which are popular safety datasets that evaluate whether a model can accurately reject harmful requests. (Section 5.1).
  - [AutoBencher: Towards Declarative Benchmark Construction](https://proceedings.iclr.cc/paper_files/paper/2025/file/eb216114f3eaad22506fd1bc7bbff0ca-Paper-Conference.pdf)
- **SORRY-Bench** (measurement instrument): *measured_by*, 1 paper
  > we identify three deficiencies underlying these existing evaluations, and address them with SORRY-Bench2, our proposed systematic benchmark to evaluate LLM safety refusal. (Section 1)
  - [SORRY-Bench: Systematically Evaluating Large Language Model Safety Refusal](https://proceedings.iclr.cc/paper_files/paper/2025/file/9622163c87b67fd5a4a0ec3247cf356e-Paper-Conference.pdf)

### → Harmful request refusal
- **Safety alignment** (construct): *causes*, 2 papers
  > During this alignment stage, LLMs learn to reject harmful queries, ensuring their behavior remains well within a defined safety scope. (Section 3.1)
  - [Benign Samples Matter! Fine-tuning On Outlier Benign Samples Severely Breaks Safety](https://raw.githubusercontent.com/mlresearch/v267/main/assets/guan25c/guan25c.pdf)
  - [Reshaping Representation Space to Balance the Safety and Over-rejection in Large Audio Language Models](https://aclanthology.org/2025.emnlp-main.510.pdf)
- **Alignment** (construct): *causes*, 1 paper
  > Alignment involves calibrating these models... such that they adhere to human values and safely follow human intents. The resultant aligned LLMs should not engage with user requests on certain unsafe or inappropriate topics... Instead, they provide a refusal response (Section 1)
  - [SORRY-Bench: Systematically Evaluating Large Language Model Safety Refusal](https://proceedings.iclr.cc/paper_files/paper/2025/file/9622163c87b67fd5a4a0ec3247cf356e-Paper-Conference.pdf)

### Associated with
- **Harmlessness** (construct), 1 paper
  > The first two responses demonstrate the model’s ability to avoid providing assistance on unethical actions... (Figure 4).
  - [Progressively Label Enhancement for Large Language Model Alignment](https://raw.githubusercontent.com/mlresearch/v267/main/assets/liu25cg/liu25cg.pdf)
