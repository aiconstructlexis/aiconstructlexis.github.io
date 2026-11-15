# Harmful content generation
**Type:** Behavioral indicator  
**Supporting papers:** 230  
**Also known as:** Toxic content generation, Unsafe text generation, Gaslighting response generation, Harmful knowledge generation, Harmful language generation, Harmful response generation, Jailbreak response generation, Unsafe response generation, Harmful-yet-helpful response generation, Unsafe generation, Toxic language generation, Toxic text generation, Malicious review generation, Unsafe output generation, Unsafe behavior, Harmful text generation, Malicious response generation, Phishing email generation, Toxic response generation, Compliance with malicious requests, Offensive language generation, Inappropriate content incorporation, Harmful instruction following, Following malicious instructions, Unsafe instruction fulfillment, Harmful question answering, Adversarial query answering, Dangerous question answering, Unsafe content generation, Compliance with harmful requests  

## State of the Field

**Space of definitions.** Across papers, the dominant framing treats this behavior as an LLM producing harmful, unsafe, toxic, offensive, biased, illegal, or otherwise policy-violating output, usually in response to harmful, adversarial, or jailbroken prompts. The prevailing success criterion is non-refusal: papers count outputs as harmful when the model answers or complies with a malicious request, offers actionable guidance, or directly assists unsafe intent. As one paper puts it, harmful answers are those that “provide concrete and helpful suggestions for malicious instructions” (Catastrophic Jailbreak of Open-source LLMs via Exploiting Generation), while another says fulfillment occurs when a response “provides substantial content that directly assists with the given unsafe instruction” (SORRY-Bench: Systematically Evaluating Large Language Model Safety Refusal). Some papers count even an attempted answer or stated willingness to answer as unsafe, while a smaller line of work narrows the behavior to particular forms such as toxic or aggressive wording, deceptive or false content, or replies that manipulate a user’s beliefs or self-perception.

**Variants.** Most variant labels narrow the same behavior around toxicity or unsafe compliance, especially toxic content generation, harmful response generation, toxic text generation, unsafe response generation, and unsafe content generation. Papers also recast it as instruction-following or question-answering behavior, where the relevant outcome is fulfillment or compliance with harmful requests rather than open-ended toxic text. Smaller variants focus on cases such as gaslighting responses, harmful knowledge generation, phishing email generation, malicious review generation, and harmful-yet-helpful outputs. The behavior is studied in text-only and multimodal settings, including vision-language and audio systems, and also in multilingual, Arabic, Indonesian, multi-turn, persona-conditioned, backdoor-triggered, data-poisoning, and retrieval-augmented conditions.

**Space of elicitation and scores.** Papers link this behavior to 18 measurement instruments. The most common are LLM-as-a-judge, Perspective API, AdvBench, BeaverTails, and Llama Guard 3: across papers these serve as automatic judges or safety classifiers, toxicity scoring tools, and harmful-prompt benchmarks. Scoring is most often framed as binary harmful versus benign judgments, harmfulness or toxicity scores, or attack success measures based on whether the model answers, is willing to answer, or is flagged as unsafe or toxic.

**What it is taken as evidence of.** Papers link it to eight constructs, but not to one shared target. Safety alignment is the most recurrent link, where several papers claim a causal relationship from Safety alignment to harmful content generation. Smaller claims add Harmlessness and Intent understanding as further causal sources, one paper claims a causal relationship from harmful content generation to Representational harm, and another line relates the behavior to Safety. Other papers add a few more causal or related constructs, so papers do not converge on a single construct that this behavior reflects.

## Sources

**Harmful content generation** (47 papers: [AutoDAN: Generating Stealthy Jailbreak Prompts on Aligned Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/f83cb637e159e789f5576ff6848874de-Paper-Conference.pdf), [Catastrophic Jailbreak of Open-source LLMs via Exploiting Generation](https://proceedings.iclr.cc/paper_files/paper/2024/file/3af25aa3de8b7b02ddbd1b6be5031be8-Paper-Conference.pdf), [Enabling Lanuguage Models to Implicitly Learn Self-Improvement](https://proceedings.iclr.cc/paper_files/paper/2024/file/194fa4536bf36f35a4505d20cd5dd6fc-Paper-Conference.pdf), [Fine-tuning Aligned Language Models Compromises Safety, Even When Users Do Not Intend To!](https://proceedings.iclr.cc/paper_files/paper/2024/file/83b7da3ed13f06c13ce82235c8eedf35-Paper-Conference.pdf), [Gaining Wisdom from Setbacks: Aligning Large Language Models via Mistake Analysis](https://proceedings.iclr.cc/paper_files/paper/2024/file/fe24df54d5ccd95cdf830a309f2bf5c0-Paper-Conference.pdf), [Jailbreak in pieces: Compositional Adversarial Attacks on Multi-Modal Language Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/83170ccee5543b872f4de71002f21aad-Paper-Conference.pdf), [On the Humanity of Conversational AI: Evaluating the Psychological Portrayal of LLMs](https://proceedings.iclr.cc/paper_files/paper/2024/file/c48dcd605cfb17d5b4f94ce106a915f7-Paper-Conference.pdf), [Safety-Tuned LLaMAs: Lessons From Improving the Safety of Large Language Models that Follow Instructions](https://proceedings.iclr.cc/paper_files/paper/2024/file/9178ece87f0a5d6558f49f43ec1e8a1a-Paper-Conference.pdf), [Understanding Catastrophic Forgetting in Language Models via Implicit Inference](https://proceedings.iclr.cc/paper_files/paper/2024/file/692ae28fda9bfbde7c01b13bf5a03395-Paper-Conference.pdf), [WildChat: 1M ChatGPT Interaction Logs in the Wild](https://proceedings.iclr.cc/paper_files/paper/2024/file/9421261e06f1a63a352b068f1ac90609-Paper-Conference.pdf), [Who's asking? User personas and the mechanics of latent misalignment](https://proceedings.neurips.cc/paper_files/paper/2024/file/e40d5118ee8f837729fa877add71c38f-Paper-Conference.pdf), [Improved Techniques for Optimization-Based Jailbreaking on Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/124256ed80af5d4bf4c4de17b66c4298-Paper-Conference.pdf), [SafetyQuizzer: Timely and Dynamic Evaluation on the Safety of LLMs](https://aclanthology.org/2025.naacl-long.85.pdf), [Beyond the Safety Bundle: Auditing the Helpful and Harmless Dataset](https://aclanthology.org/2025.naacl-long.596.pdf), [Arabic Dataset for LLM Safeguard Evaluation](https://aclanthology.org/2025.naacl-long.285.pdf), [Layer-Level Self-Exposure and Patch: Affirmative Token Mitigation for Jailbreak Attack Defense](https://aclanthology.org/2025.naacl-long.623.pdf), [Stealthy Jailbreak Attacks on Large Language Models via Benign Data Mirroring](https://aclanthology.org/2025.naacl-long.88.pdf), [SeqAR: Jailbreak LLMs with Sequential Auto-Generated Characters](https://aclanthology.org/2025.naacl-long.42.pdf), [Audio Is the Achilles' Heel: Red Teaming Audio Large Multimodal Models](https://aclanthology.org/2025.naacl-long.470.pdf), [BPO: Towards Balanced Preference Optimization between Knowledge Breadth and Depth in Alignment](https://aclanthology.org/2025.naacl-long.443.pdf), [Goal-Conditioned DPO: Prioritizing Safety in Misaligned Instructions](https://aclanthology.org/2025.naacl-long.369.pdf), [ImgTrojan: Jailbreaking Vision-Language Models with ONE Image](https://aclanthology.org/2025.naacl-long.360.pdf), [Diversity Helps Jailbreak Large Language Models](https://aclanthology.org/2025.naacl-long.238.pdf), [Extracting and Understanding the Superficial Knowledge in Alignment](https://aclanthology.org/2025.naacl-long.168.pdf), [Layer-wise Alignment: Examining Safety Alignment Across Image Encoder Layers in Vision Language Models](https://raw.githubusercontent.com/mlresearch/v267/main/assets/bachu25a/bachu25a.pdf), [Automating Steering for Safe Multimodal Large Language Models](https://aclanthology.org/2025.emnlp-main.41.pdf), [AGD: Adversarial Game Defense Against Jailbreak Attacks in Large Language Models](https://aclanthology.org/2025.acl-long.851.pdf), [Beware of Your Po! Measuring and Mitigating AI Safety Risks in Role-Play Fine-Tuning of LLMs](https://aclanthology.org/2025.acl-long.544.pdf), [Beyond Prompt Engineering: Robust Behavior Control in LLMs via Steering Target Atoms](https://aclanthology.org/2025.acl-long.1139.pdf), [Con Instruction: Universal Jailbreaking of Multimodal Large Language Models via Non-Textual Modalities](https://aclanthology.org/2025.acl-long.146.pdf), [Cross-model Transferability among Large Language Models on the Platonic Representations of Concepts](https://aclanthology.org/2025.acl-long.185.pdf), [DeAL: Decoding-time Alignment for Large Language Models](https://aclanthology.org/2025.acl-long.1274.pdf), [Jailbreak Large Vision-Language Models Through Multi-Modal Linkage](https://aclanthology.org/2025.acl-long.74.pdf), [JailbreakRadar: Comprehensive Assessment of Jailbreak Attacks Against LLMs](https://aclanthology.org/2025.acl-long.1045.pdf), [Jailbreaking? One Step Is Enough!](https://aclanthology.org/2025.acl-long.570.pdf), [LED-Merging: Mitigating Safety-Utility Conflicts in Model Merging with Location-Election-Disjoint](https://aclanthology.org/2025.acl-long.1055.pdf), [LLMs know their vulnerabilities: Uncover Safety Gaps through Natural Distribution Shifts](https://aclanthology.org/2025.acl-long.1207.pdf), [M2S: Multi-turn to Single-turn jailbreak in Red Teaming for LLMs](https://aclanthology.org/2025.acl-long.805.pdf), [MTSA: Multi-turn Safety Alignment for LLMs through Multi-round Red-teaming](https://aclanthology.org/2025.acl-long.1282.pdf), [PKU-SafeRLHF: Towards Multi-Level Safety Alignment for LLMs with Human Preference](https://aclanthology.org/2025.acl-long.1544.pdf), [Refuse Whenever You Feel Unsafe: Improving Safety in LLMs via Decoupled Refusal Training](https://aclanthology.org/2025.acl-long.158.pdf), [Representation Bending for Large Language Model Safety](https://aclanthology.org/2025.acl-long.1173.pdf), [Shaping the Safety Boundaries: Understanding and Defending Against Jailbreaks in Large Language Models](https://aclanthology.org/2025.acl-long.1233.pdf), [The TIP of the Iceberg: Revealing a Hidden Class of Task-in-Prompt Adversarial Attacks on LLMs](https://aclanthology.org/2025.acl-long.334.pdf), [What Really Matters in Many-Shot Attacks? An Empirical Study of Long-Context Vulnerabilities in LLMs](https://aclanthology.org/2025.acl-long.101.pdf), [Why Safeguarded Ships Run Aground? Aligned Large Language Models' Safety Mechanisms Tend to Be Anchored in The Template Region](https://aclanthology.org/2025.acl-long.738.pdf), [from Benign import Toxic: Jailbreaking the Language Model via Adversarial Metaphors](https://aclanthology.org/2025.acl-long.238.pdf))
> The production of toxic, offensive, or otherwise damaging content by a language model, which alignment methods aim to suppress.

**Toxic content generation** (7 papers: [Apathetic or Empathetic? Evaluating LLMs' Emotional Alignments with Humans](https://proceedings.neurips.cc/paper_files/paper/2024/file/b0049c3f9c53fb06f674ae66c2cf2376-Paper-Conference.pdf), [Large Language Models can Become Strong Self-Detoxifiers](https://proceedings.iclr.cc/paper_files/paper/2025/file/10df3b90b7caf44bf96b5a542a6935fe-Paper-Conference.pdf), [Metadata Conditioning Accelerates Language Model Pre-training](https://raw.githubusercontent.com/mlresearch/v267/main/assets/gao25p/gao25p.pdf), [PBI-Attack: Prior-Guided Bimodal Interactive Black-Box Jailbreak Attack for Toxicity Maximization](https://aclanthology.org/2025.emnlp-main.32.pdf), [CRITIC: Large Language Models Can Self-Correct with Tool-Interactive Critiquing](https://proceedings.iclr.cc/paper_files/paper/2024/file/fef126561bbf9d4467dbb8d27334b8fe-Paper-Conference.pdf), [Get more for less: Principled Data Selection for Warming Up Fine-Tuning in LLMs](https://proceedings.iclr.cc/paper_files/paper/2024/file/b36dc39b319ba6ba2a0fd7601951efb4-Paper-Conference.pdf), [PoisonedParrot: Subtle Data Poisoning Attacks to Elicit Copyright-Infringing Content from Large Language Models](https://aclanthology.org/2025.naacl-long.415.pdf))
> Producing responses that are considered toxic or aggressive in demographic-description prompts.

**Unsafe text generation** (1 paper: [Optimistic Verifiable Training by Controlling Hardware Nondeterminism](https://proceedings.neurips.cc/paper_files/paper/2024/file/ad885a9caafff30ee9cafdf0ee42fda2-Paper-Conference.pdf))
> The observable model behavior of producing harmful, undesirable, or toxic content, often as a result of data poisoning.

**Unsafe response generation** (3 papers: [ETA: Evaluating Then Aligning Safety of Vision Language Models at Inference Time](https://proceedings.iclr.cc/paper_files/paper/2025/file/06f9fe2915857be2b1e369419a531ad3-Paper-Conference.pdf), [Nullspace Disentanglement for Red Teaming Language Models](https://aclanthology.org/2025.emnlp-main.1083.pdf), [GPT-4 Is Too Smart To Be Safe: Stealthy Chat with LLMs via Cipher](https://proceedings.iclr.cc/paper_files/paper/2024/file/ed4c38fe7899d3653acf39b2102af8ba-Paper-Conference.pdf))
> The observable output of harmful or unsafe content by the model in response to malicious queries.

**Gaslighting response generation** (1 paper: [Can a Large Language Model be a Gaslighter?](https://proceedings.iclr.cc/paper_files/paper/2025/file/0769598fdeb4f23ee86fec1bc0777f44-Paper-Conference.pdf))
> Producing assistant replies that subtly manipulate a user's beliefs, self-doubt, or self-perception in a conversation.

**Harmful response generation** (6 papers: [Robust LLM safeguarding via refusal feature adversarial training](https://proceedings.iclr.cc/paper_files/paper/2025/file/1022661f3f43406065641f16ce25eafa-Paper-Conference.pdf), [IndoSafety: Culturally Grounded Safety for LLMs in Indonesian Languages](https://aclanthology.org/2025.emnlp-main.465.pdf), [Adversarial Reasoning at Jailbreaking Time](https://raw.githubusercontent.com/mlresearch/v267/main/assets/sabbaghi25a/sabbaghi25a.pdf), [Eliciting Language Model Behaviors with Investigator Agents](https://raw.githubusercontent.com/mlresearch/v267/main/assets/li25i/li25i.pdf), [PANDAS: Improving Many-shot Jailbreaking via Positive Affirmation, Negative Demonstration, and Adaptive Sampling](https://raw.githubusercontent.com/mlresearch/v267/main/assets/ma25q/ma25q.pdf), [Stronger Universal and Transferable Attacks by Suppressing Refusals](https://aclanthology.org/2025.naacl-long.302.pdf))
> Producing unsafe, harmful, sensitive, or false content in response to malicious prompts.

**Jailbreak response generation** (1 paper: [Injecting Universal Jailbreak Backdoors into LLMs in Minutes](https://proceedings.iclr.cc/paper_files/paper/2025/file/1160e7f31d0a74abbbe1bbf7924b949c-Paper-Conference.pdf))
> Producing instruction-following responses to harmful or restricted prompts when a backdoor trigger is activated.

**Harmful language generation** (1 paper: [Uncertainty-Aware Decoding with Minimum Bayes Risk](https://proceedings.iclr.cc/paper_files/paper/2025/file/1588dc2b2ef339d6e4c47d212e36f991-Paper-Conference.pdf))
> The generation of text that is toxic, biased, or otherwise harmful.

**Harmful knowledge generation** (2 papers: [Unlearning or Obfuscating? Jogging the Memory of Unlearned LLMs via Benign Relearning](https://proceedings.iclr.cc/paper_files/paper/2025/file/18fd48d9cbbf9a20e434c9d3db6973c5-Paper-Conference.pdf), [Why and How LLMs Benefit from Knowledge Introspection in Commonsense Reasoning](https://aclanthology.org/2025.emnlp-main.352.pdf))
> The observable model behavior of producing text containing dangerous, undesirable, or hazardous information, such as biosecurity threats.

**Unsafe generation** (1 paper: [Backtracking Improves Generation Safety](https://proceedings.iclr.cc/paper_files/paper/2025/file/65beb73449888fabcf601b3a3ef4b3a7-Paper-Conference.pdf))
> The observable production of harmful, malicious, or policy-violating text in response to a prompt.

**Harmful-yet-helpful response generation** (1 paper: [Failures to Find Transferable Image Jailbreaks Between Vision-Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/6e3daaeca6be8579573f69082b2dd58b-Paper-Conference.pdf))
> Producing outputs that are both harmful and instrumentally useful to a user's malicious goal.

**Toxic text generation** (4 papers: [Model Editing as a Robust and Denoised variant of DPO: A Case Study on Toxicity](https://proceedings.iclr.cc/paper_files/paper/2025/file/acb7ce5aab6e134300a2361dd90a501f-Paper-Conference.pdf), [Model Swarms: Collaborative Search to Adapt LLM Experts via Swarm Intelligence](https://raw.githubusercontent.com/mlresearch/v267/main/assets/feng25o/feng25o.pdf), [Detoxifying Large Language Models via the Diversity of Toxic Samples](https://aclanthology.org/2025.emnlp-main.298.pdf), [Transferable Post-training via Inverse Value Learning](https://aclanthology.org/2025.naacl-long.227.pdf))
> Producing continuations or outputs that contain harmful, offensive, or unsafe language when prompted.

**Toxic language generation** (2 papers: [Controlling Language and Diffusion Models by Transporting Activations](https://proceedings.iclr.cc/paper_files/paper/2025/file/df4f6e43446b1ee29c5a33d32c279f83-Paper-Conference.pdf), [Model Merging by Uncertainty-Based Gradient Matching](https://proceedings.iclr.cc/paper_files/paper/2024/file/327b9b8d4e45c3f81568e11ffc505f77-Paper-Conference.pdf))
> The observable act of a language model producing text that is considered toxic, harmful, or offensive.

**Unsafe output generation** (1 paper: [Learning Safety Constraints for Large Language Models](https://raw.githubusercontent.com/mlresearch/v267/main/assets/chen25b/chen25b.pdf))
> The model produces content that violates ethical or safety norms, such as generating harmful, illegal, or deceptive text in response to adversarial prompts.

**Malicious review generation** (1 paper: [Online Detection of LLM-Generated Texts via Sequential Hypothesis Testing by Betting](https://raw.githubusercontent.com/mlresearch/v267/main/assets/chen25bn/chen25bn.pdf))
> The creation of fake or deceptive product or service reviews.

**Compliance with malicious requests** (1 paper: [SafeArena: Evaluating the Safety of Autonomous Web Agents](https://raw.githubusercontent.com/mlresearch/v267/main/assets/tur25a/tur25a.pdf))
> The observable tendency of an agent to follow and execute instructions that are explicitly harmful or malicious.

**Malicious response generation** (1 paper: [Backdoor Attacks in Token Selection of Attention Mechanism](https://raw.githubusercontent.com/mlresearch/v267/main/assets/wang25c/wang25c.pdf))
> The model produces harmful, unsafe, or otherwise undesirable text as a result of an adversarial trigger.

**Toxic response generation** (2 papers: [LLMScan: Causal Scan for LLM Misbehavior Detection](https://raw.githubusercontent.com/mlresearch/v267/main/assets/zhang25al/zhang25al.pdf), [Curiosity-driven Red-teaming for Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/56ed2bd15b66f709cd81cb1aaa0496b9-Paper-Conference.pdf))
> The observable production of insulting, offensive, or aggressive language by an LLM in response to certain inputs.

**Phishing email generation** (1 paper: [UDora: A Unified Red Teaming Framework against LLM Agents by Dynamically Hijacking Their Own Reasoning](https://raw.githubusercontent.com/mlresearch/v267/main/assets/zhang25cl/zhang25cl.pdf))
> The production of deceptive emails designed to extract sensitive information, which the agent may be induced to write and send under adversarial prompting.

**Unsafe behavior** (1 paper: [MM-RLHF: The Next Step Forward in Multimodal LLM Alignment](https://raw.githubusercontent.com/mlresearch/v267/main/assets/zhang25cs/zhang25cs.pdf))
> The model's generation of outputs that are harmful, biased, unethical, or otherwise violate safety guidelines.

**Harmful text generation** (1 paper: [Weak-to-Strong Jailbreaking on Large Language Models](https://raw.githubusercontent.com/mlresearch/v267/main/assets/zhao25aa/zhao25aa.pdf))
> The observable output of text that is unethical, biased, dangerous, or otherwise violates safety guidelines.

**Offensive language generation** (1 paper: [Exploring Chain-of-Thought Reasoning for Steerable Pluralistic Alignment](https://aclanthology.org/2025.emnlp-main.1301.pdf))
> The observable, unintended behavior of producing text that is flagged as offensive, such as harassment or violent content.

**Inappropriate content incorporation** (1 paper: [Rescorla-Wagner Steering of LLMs for Undesired Behaviors over Disproportionate Inappropriate Context](https://aclanthology.org/2025.emnlp-main.1003.pdf))
> The observable phenomenon where an LLM includes harmful or irrelevant information—such as fake news, hate speech, or privacy violations—into its generated response despite the presence of accurate context.

**Harmful instruction following** (1 paper: [ALI-Agent: Assessing LLMs' Alignment with Human Values via Agent-based Evaluation](https://proceedings.neurips.cc/paper_files/paper/2024/file/b35c38f70065ac6c694089ca93a015bb-Paper-Conference.pdf))
> The observable behavior of a model complying with a harmful instruction to generate an unsafe or malicious response.

**Following malicious instructions** (1 paper: [Uncovering Safety Risks of Large Language Models through Concept Activation Vector](https://proceedings.neurips.cc/paper_files/paper/2024/file/d3a230d716e65afab578a8eb31a8d25f-Paper-Conference.pdf))
> The model generates a response that complies with a user's request for harmful, unethical, or dangerous content, rather than refusing.

**Unsafe instruction fulfillment** (1 paper: [SORRY-Bench: Systematically Evaluating Large Language Model Safety Refusal](https://proceedings.iclr.cc/paper_files/paper/2025/file/9622163c87b67fd5a4a0ec3247cf356e-Paper-Conference.pdf))
> The observable behavior where a model executes a potentially unsafe instruction by providing substantial content that directly assists with the user's unsafe intent.

**Harmful question answering** (1 paper: [On Evaluating the Durability of Safeguards for Open-Weight LLMs](https://proceedings.iclr.cc/paper_files/paper/2025/file/9d3a4cdf6f70559e8c6fe02170fba568-Paper-Conference.pdf))
> The observable behavior of a model complying with and providing a substantive answer to a harmful or malicious question.

**Adversarial query answering** (1 paper: [Who's asking? User personas and the mechanics of latent misalignment](https://proceedings.neurips.cc/paper_files/paper/2024/file/e40d5118ee8f837729fa877add71c38f-Paper-Conference.pdf))
> The act of providing a substantive, non-refusal response to a query designed to elicit harmful content.

**Dangerous question answering** (1 paper: [Can a Large Language Model be a Gaslighter?](https://proceedings.iclr.cc/paper_files/paper/2025/file/0769598fdeb4f23ee86fec1bc0777f44-Paper-Conference.pdf))
> Responding to harmful or unsafe user questions in a way that reveals whether the model refuses or complies.

**Unsafe content generation** (2 papers: [Multilingual Jailbreak Challenges in Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/6b396f766a50e0853a5164e68048540c-Paper-Conference.pdf), [RAG LLMs are Not Safer: A Safety Analysis of Retrieval-Augmented Generation for Large Language Models](https://aclanthology.org/2025.naacl-long.281.pdf))
> The observable production of harmful or inappropriate responses by an LLM when prompted with malicious or sensitive queries, particularly in non-English languages.

**Compliance with harmful requests** (1 paper: [Why Safeguarded Ships Run Aground? Aligned Large Language Models' Safety Mechanisms Tend to Be Anchored in The Template Region](https://aclanthology.org/2025.acl-long.738.pdf))
> The observable behavior of a model generating a response that fulfills a harmful or unethical user instruction, thereby bypassing its safety training.

## Relationships

### Harmful content generation →
- **Perspective API** (measurement instrument): *measured_by*, 5 papers
  > To measure the toxicity of these harmful generations, we employ automatic evaluation models pre-trained on toxic datasets, including Perspective API and toxic classifiers (Hanu & Unitary team, 2020) with BERT (Kenton & Toutanova, 2019) and RoBERTa (Liu et al., 2019). (Section 4)
  - [Jailbreak in pieces: Compositional Adversarial Attacks on Multi-Modal Language Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/83170ccee5543b872f4de71002f21aad-Paper-Conference.pdf)
  - [Scalable Extraction of Training Data from Aligned, Production Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/cce0e917b050208170151f77b497fc71-Paper-Conference.pdf)
  - [Monet: Mixture of Monosemantic Experts for Transformers](https://proceedings.iclr.cc/paper_files/paper/2025/file/382c35d1a57c07055dfcba58dd39e012-Paper-Conference.pdf)
  - [Uncovering Bias in Large Vision-Language Models at Scale with Counterfactuals](https://aclanthology.org/2025.naacl-long.305.pdf)
  - [Layer-wise Alignment: Examining Safety Alignment Across Image Encoder Layers in Vision Language Models](https://raw.githubusercontent.com/mlresearch/v267/main/assets/bachu25a/bachu25a.pdf)
- **LLM-as-a-judge** (measurement instrument): *measured_by*, 5 papers
  > To measure jailbreak success, we computed: (i) Cross-Entropy (Eqn. 1) and (ii) Claude 3 Opus Harmful-Yet-Helpful Score by prompting Claude 3 Opus to assess how helpful-yet-harmful sampled outputs are.
  - [Failures to Find Transferable Image Jailbreaks Between Vision-Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/6e3daaeca6be8579573f69082b2dd58b-Paper-Conference.pdf)
  - [EFFICIENT JAILBREAK ATTACK SEQUENCES ON LARGE LANGUAGE MODELS VIA MULTI-ARMED BANDIT-BASED CONTEXT SWITCHING](https://proceedings.iclr.cc/paper_files/paper/2025/file/52724c4ea3634f610b0ef0245ce5bd20-Paper-Conference.pdf)
  - [Safety Alignment Should be Made More Than Just a Few Tokens Deep](https://proceedings.iclr.cc/paper_files/paper/2025/file/88be023075a5a3ff3dc3b5d26623fa22-Paper-Conference.pdf)
  - [FlipAttack: Jailbreak LLMs via Flipping](https://raw.githubusercontent.com/mlresearch/v267/main/assets/liu25z/liu25z.pdf)
  - [Visual Contextual Attack: Jailbreaking MLLMs with Image-Driven Context Injection](https://aclanthology.org/2025.emnlp-main.487.pdf)
- **AdvBench** (measurement instrument): *measured_by*, 3 papers
  > For our prompts, we sample 100 instructions from AdvBench (Zou et al., 2023). We say that the model output reflects the ANSWER task if it attempts to answer the question... (Section 4.3)
  - [Understanding Catastrophic Forgetting in Language Models via Implicit Inference](https://proceedings.iclr.cc/paper_files/paper/2024/file/692ae28fda9bfbde7c01b13bf5a03395-Paper-Conference.pdf)
  - [Jailbreaking Large Language Models Against Moderation Guardrails via Cipher Characters](https://proceedings.neurips.cc/paper_files/paper/2024/file/6d56bc83ae9a4fafdce050bb36f04174-Paper-Conference.pdf)
  - [From Outcomes to Processes: Guiding PRM Learning from ORM for Inference-Time Alignment](https://aclanthology.org/2025.acl-long.946.pdf)
- **ToxiGen** (measurement instrument): *measured_by*, 3 papers
  > We take only the prompts designed to produce toxic language (‘hateful’ prompts) and use 500 prompts per group to reduce evaluation costs. (Appendix D).
  - [Unpacking DPO and PPO: Disentangling Best Practices for Learning from Preference Feedback](https://proceedings.neurips.cc/paper_files/paper/2024/file/404df2480b6eef0486a1679e371894b0-Paper-Conference.pdf)
  - [Extracting and Understanding the Superficial Knowledge in Alignment](https://aclanthology.org/2025.naacl-long.168.pdf)
  - [When Bad Data Leads to Good Models](https://raw.githubusercontent.com/mlresearch/v267/main/assets/li25d/li25d.pdf)
- **BeaverTails** (measurement instrument): *measured_by*, 3 papers
  > To calculate the harmful score, we sample 1000 instructions from the testing set of BeaverTails (Ji et al., 2023).
  - [Booster: Tackling Harmful Fine-tuning for Large Language Models via Attenuating Harmful Perturbation](https://proceedings.iclr.cc/paper_files/paper/2025/file/a7ac8a21e5a27e7ab31a5f42a0117bdb-Paper-Conference.pdf)
  - [On Evaluating the Durability of Safeguards for Open-Weight LLMs](https://proceedings.iclr.cc/paper_files/paper/2025/file/9d3a4cdf6f70559e8c6fe02170fba568-Paper-Conference.pdf)
  - [Antidote: Post-fine-tuning Safety Alignment for Large Language Models against Harmful Fine-tuning Attack](https://raw.githubusercontent.com/mlresearch/v267/main/assets/huang25b/huang25b.pdf)
- **Llama Guard 3** (measurement instrument): *measured_by*, 3 papers
  > Then evaluate the harmfulness score on its responses with the Llama-Guard-3-8B (Llama Team, 2024). We use 70% harmful prompts in the AdvBench dataset (Zou et al., 2023b) for InferAligner, Vaccine, and our SaLoRA. (Section 5.1).
  - [SaLoRA: Safety-Alignment Preserved Low-Rank Adaptation](https://proceedings.iclr.cc/paper_files/paper/2025/file/e24d9d028e3c7f6f13e6032919ee021e-Paper-Conference.pdf)
  - [Stealthy Jailbreak Attacks on Large Language Models via Benign Data Mirroring](https://aclanthology.org/2025.naacl-long.88.pdf)
  - [Audio Is the Achilles' Heel: Red Teaming Audio Large Multimodal Models](https://aclanthology.org/2025.naacl-long.470.pdf)
- **RealToxicityPrompts** (measurement instrument): *measured_by*, 2 papers
  > We randomly sample 1k prompts from the non-toxic prompts of the REALTOXICITYPROMPTS (Gehman et al., 2020), which was designed to elicit toxic responses. (Section 4.3)
  - [CRITIC: Large Language Models Can Self-Correct with Tool-Interactive Critiquing](https://proceedings.iclr.cc/paper_files/paper/2024/file/fef126561bbf9d4467dbb8d27334b8fe-Paper-Conference.pdf)
  - [When Bad Data Leads to Good Models](https://raw.githubusercontent.com/mlresearch/v267/main/assets/li25d/li25d.pdf)
- **HarmBench classifier** (measurement instrument): *measured_by*, 2 papers
  > To compute attack success rate, we use three LLM-as-a-judge models that are fine-tuned to assess output safety: the official HarmBench classifier... (Section 5)
  - [Robust LLM safeguarding via refusal feature adversarial training](https://proceedings.iclr.cc/paper_files/paper/2025/file/1022661f3f43406065641f16ce25eafa-Paper-Conference.pdf)
  - [Improving Large Language Model Safety with Contrastive Representation Learning](https://aclanthology.org/2025.emnlp-main.1430.pdf)
- **HarmBench** (measurement instrument): *measured_by*, 1 paper
  > our method not only induces the target LLM to answer and provide harmful content in more malicious requests, as measured by the Harmbench ASR
  - [AutoDAN-Turbo: A Lifelong Agent for Strategy Self-Exploration to Jailbreak LLMs](https://proceedings.iclr.cc/paper_files/paper/2025/file/1bff3663270ba47f801e917f782d7935-Paper-Conference.pdf)
- **OpenAI Moderation API** (measurement instrument): *measured_by*, 1 paper
  > The success rate for each prompt was determined by whether the chatbot’s response to such a prompt was flagged by either Detoxify or OpenAI Moderation API (Section 4).
  - [WildChat: 1M ChatGPT Interaction Logs in the Wild](https://proceedings.iclr.cc/paper_files/paper/2024/file/9421261e06f1a63a352b068f1ac90609-Paper-Conference.pdf)
- **Detoxify** (measurement instrument): *measured_by*, 1 paper
  > The success rate for each prompt was determined by whether the chatbot’s response to such a prompt was flagged by either Detoxify or OpenAI Moderation API (Section 4).
  - [WildChat: 1M ChatGPT Interaction Logs in the Wild](https://proceedings.iclr.cc/paper_files/paper/2024/file/9421261e06f1a63a352b068f1ac90609-Paper-Conference.pdf)
- **Llama Guard 2** (measurement instrument): *measured_by*, 1 paper
  > To compute attack success rate, we use three LLM-as-a-judge models that are fine-tuned to assess output safety: ... the Llama-Guard-2 safety classifier... (Section 5)
  - [Robust LLM safeguarding via refusal feature adversarial training](https://proceedings.iclr.cc/paper_files/paper/2025/file/1022661f3f43406065641f16ce25eafa-Paper-Conference.pdf)
- **StrongREJECT** (measurement instrument): *measured_by*, 1 paper
  > To compute attack success rate, we use three LLM-as-a-judge models that are fine-tuned to assess output safety: ... and the Gemma-2B version of the StrongReject safety classifier (Souly et al., 2024). (Section 5)
  - [Robust LLM safeguarding via refusal feature adversarial training](https://proceedings.iclr.cc/paper_files/paper/2025/file/1022661f3f43406065641f16ce25eafa-Paper-Conference.pdf)
- **HEx-PHI** (measurement instrument): *measured_by*, 1 paper
  > HEx-PHI and SORRY-bench are two dedicated benchmarks for evaluating harmfulness in the HarmfulQA context. (Section 2.2)
  - [On Evaluating the Durability of Safeguards for Open-Weight LLMs](https://proceedings.iclr.cc/paper_files/paper/2025/file/9d3a4cdf6f70559e8c6fe02170fba568-Paper-Conference.pdf)
- **SORRY-Bench** (measurement instrument): *measured_by*, 1 paper
  > HEx-PHI and SORRY-bench are two dedicated benchmarks for evaluating harmfulness in the HarmfulQA context. (Section 2.2)
  - [On Evaluating the Durability of Safeguards for Open-Weight LLMs](https://proceedings.iclr.cc/paper_files/paper/2025/file/9d3a4cdf6f70559e8c6fe02170fba568-Paper-Conference.pdf)
- **Human evaluation** (measurement instrument): *measured_by*, 1 paper
  > We determine the Attack Success Rate (ASR) by manually evaluating the responses generated by the target LLMs for each attack method, based on the evaluation criteria outlined in Appendix C. The ASR indicates the proportion of harmful responses generated. (Section 4.1)
  - [Refuse Whenever You Feel Unsafe: Improving Safety in LLMs via Decoupled Refusal Training](https://aclanthology.org/2025.acl-long.158.pdf)
- **Llama Guard** (measurement instrument): *measured_by*, 1 paper
  > To evaluate the VLM output harmfulness, we use the Attack Success Rate (ASR) metric via Llama Guard (Inan et al., 2023), following prior works (Zou et al., 2023; Shayegani et al., 2024; Luo et al., 2024). (Section 4.1)
  - [Layer-wise Alignment: Examining Safety Alignment Across Image Encoder Layers in Vision Language Models](https://raw.githubusercontent.com/mlresearch/v267/main/assets/bachu25a/bachu25a.pdf)
- **MM-SafetyBench** (measurement instrument): *measured_by*, 1 paper
  > MM-SafetyBench (Liu et al., 2024b), originally proposed as QR Attack, uses image-query-related inputs to elicit harmful responses from models. (Section 4.1)
  - [Visual Contextual Attack: Jailbreaking MLLMs with Image-Driven Context Injection](https://aclanthology.org/2025.emnlp-main.487.pdf)
- **Representational harm** (construct): *causes*, 1 paper
  > The former occur when PLMs propagate stereotypes, toxic language, and disparate judgments that depict one social group more unfavorably than another (Blodgett et al., 2020; Crawford, 2017)
  - [Social Bias in Multilingual Language Models: A Survey](https://aclanthology.org/2025.emnlp-main.1416.pdf)

### → Harmful content generation
- **Jailbreaking** (behavioral indicator): *causes*, 12 papers
  > We focus on identifying prompts that, when given a specific harmful request (e.g., “Tell me how to build a bomb”), induces the LLM to generate harmful content.
  - [Jailbreaking Leading Safety-Aligned LLMs with Simple Adaptive Attacks](https://proceedings.iclr.cc/paper_files/paper/2025/file/63fa7efdd3bcf944a4bd6e0ff6a50041-Paper-Conference.pdf)
  - [Does Refusal Training in LLMs Generalize to the Past Tense?](https://proceedings.iclr.cc/paper_files/paper/2025/file/d432fbe4877ee1a6a51632a18e69784f-Paper-Conference.pdf)
  - [ProAdvPrompter: A Two-Stage Journey to Effective Adversarial Prompting for LLMs](https://proceedings.iclr.cc/paper_files/paper/2025/file/1861027cac475192f2c2cd0ec568fc66-Paper-Conference.pdf)
  - [AutoDAN-Turbo: A Lifelong Agent for Strategy Self-Exploration to Jailbreak LLMs](https://proceedings.iclr.cc/paper_files/paper/2025/file/1bff3663270ba47f801e917f782d7935-Paper-Conference.pdf)
  - [Stronger Universal and Transferable Attacks by Suppressing Refusals](https://aclanthology.org/2025.naacl-long.302.pdf)
  - [TuCo: Measuring the Contribution of Fine-Tuning to Individual Responses of LLMs](https://raw.githubusercontent.com/mlresearch/v267/main/assets/nuti25a/nuti25a.pdf)
  - [Cannot See the Forest for the Trees: Invoking Heuristics and Biases to Elicit Irrational Choices of LLMs](https://raw.githubusercontent.com/mlresearch/v267/main/assets/yang25s/yang25s.pdf)
  - [Emoji Attack: Enhancing Jailbreak Attacks Against Judge LLM Detection](https://raw.githubusercontent.com/mlresearch/v267/main/assets/wei25g/wei25g.pdf)
  - [Weak-to-Strong Jailbreaking on Large Language Models](https://raw.githubusercontent.com/mlresearch/v267/main/assets/zhao25aa/zhao25aa.pdf)
  - [Stand on The Shoulders of Giants: Building JailExpert from Previous Attack Experience](https://aclanthology.org/2025.emnlp-main.190.pdf)
  - [DiffusionAttacker: Diffusion-Driven Prompt Manipulation for LLM Jailbreak](https://aclanthology.org/2025.emnlp-main.1128.pdf)
  - [Navigating the Safety Landscape: Measuring Risks in Finetuning Large Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/ada93fa6643735f294be51dc31eebbd4-Paper-Conference.pdf)
- **Safety alignment** (construct): *causes*, 7 papers
  > “Safety alignment is essential to prevent unintended model behaviors and mitigate risks in downstream applications.”
  - [Durable Quantization Conditioned Misalignment Attack on Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/376b1b131609e764f687afca832e62b3-Paper-Conference.pdf)
  - [Emerging Safety Attack and Defense in Federated Instruction Tuning of Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/8a3cb72448f9b914bf888db4f5f268d3-Paper-Conference.pdf)
  - [AdvWave: Stealthy Adversarial Jailbreak Attack against Large Audio-Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/45673dbf3f331fbd911b0689872de396-Paper-Conference.pdf)
  - [SaLoRA: Safety-Alignment Preserved Low-Rank Adaptation](https://proceedings.iclr.cc/paper_files/paper/2025/file/e24d9d028e3c7f6f13e6032919ee021e-Paper-Conference.pdf)
  - [AutoDAN-Turbo: A Lifelong Agent for Strategy Self-Exploration to Jailbreak LLMs](https://proceedings.iclr.cc/paper_files/paper/2025/file/1bff3663270ba47f801e917f782d7935-Paper-Conference.pdf)
  - [Reshaping Representation Space to Balance the Safety and Over-rejection in Large Audio Language Models](https://aclanthology.org/2025.emnlp-main.510.pdf)
  - [SPIRIT: Patching Speech Language Models against Jailbreak Attacks](https://aclanthology.org/2025.emnlp-main.734.pdf)
- **Safety robustness** (construct): *causes*, 1 paper
  > jailbreak attacks, which exploit vulnerabilities to elicit unintended or harmful outputs, threaten LLMs safety significantly. (Abstract)
  - [Layer-Level Self-Exposure and Patch: Affirmative Token Mitigation for Jailbreak Attack Defense](https://aclanthology.org/2025.naacl-long.623.pdf)
- **Instruction following** (behavioral indicator): *causes*, 1 paper
  > GPT-4 showed notably more unsafe behavior than Turbo in almost all cases when chatting with ciphers, due to its superior instruction understanding and adherence, thereby interpreting the cipher instruction and generating a relevant response. (Section 4.3)
  - [GPT-4 Is Too Smart To Be Safe: Stealthy Chat with LLMs via Cipher](https://proceedings.iclr.cc/paper_files/paper/2024/file/ed4c38fe7899d3653acf39b2102af8ba-Paper-Conference.pdf)
- **User modeling** (construct): *causes*, 1 paper
  > In this work, we show that whether they do so [divulge harmful information] depends signiﬁcantly on who they are talking to, which we refer to as user persona.
  - [Who's asking? User personas and the mechanics of latent misalignment](https://proceedings.neurips.cc/paper_files/paper/2024/file/e40d5118ee8f837729fa877add71c38f-Paper-Conference.pdf)
- **Intent understanding** (construct): *causes*, 1 paper
  > By incorporating adversarial sequences, these attacks can redirect the source LLM’s focus away from malicious-intent tokens in the original input, thereby obstructing the model’s intent recognition and eliciting harmful responses. (Abstract)
  - [Understanding and Enhancing the Transferability of Jailbreaking Attacks](https://proceedings.iclr.cc/paper_files/paper/2025/file/db988b089d8d97d0f159c15ed0be6a71-Paper-Conference.pdf)
- **Harmlessness** (construct): *causes*, 1 paper
  > Taking the concept of harmfulness as an example, L-Cross Modulation effectively steer LLMs to generate harmful content in 90% of outputs on test set, compared with 0% harmful content in the original responses;
  - [Cross-model Transferability among Large Language Models on the Platonic Representations of Concepts](https://aclanthology.org/2025.acl-long.185.pdf)

### Associated with
- **Safety** (construct), 1 paper
  > Here, safety is defined as stopping models from following malicious instructions and generating toxic content. (Section 3)
  - [Safety-Tuned LLaMAs: Lessons From Improving the Safety of Large Language Models that Follow Instructions](https://proceedings.iclr.cc/paper_files/paper/2024/file/9178ece87f0a5d6558f49f43ec1e8a1a-Paper-Conference.pdf)
- **Social bias** (construct), 1 paper
  > social attributes such as perceived race, gender, and physical characteristics depicted in images can significantly influence the generation of toxic content (Abstract).
  - [Uncovering Bias in Large Vision-Language Models at Scale with Counterfactuals](https://aclanthology.org/2025.naacl-long.305.pdf)
