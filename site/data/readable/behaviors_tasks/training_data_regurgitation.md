# Training data regurgitation
**Type:** Behavioral indicator  
**Supporting papers:** 27  
**Also known as:** Training data leakage, Verbatim regurgitation, Verbatim Reproduction, Code reproduction, Quotation reproduction, Text reproduction, Literal copying, Secret canary recovery, Exact sequence reproduction, Verbatim recall, Recitation, Copyrighted text generation, Training data extraction, Verbatim memorization, Secret extraction, Verbatim quoting, Text regurgitation, Secret regurgitation  

## State of the Field

**Space of definitions.** Across papers, the prevailing use refers to a model outputting exact or near-exact material from its training data, usually when given a prefix or related context from the same example. Most definitions describe word-for-word copying of text, substrings, or subsequent tokens, while some focus on specific payloads such as PII, secrets, canaries, copyrighted passages, or quotations; success is typically the model reproducing the target continuation, exact digits, or another matching sequence. A smaller framing broadens this to training data leakage, where private or copyrighted content is exposed or inferred through outputs or internal signals, and a few papers allow overlap or strong similarity rather than strict exact match.

**Variants.** Papers use labels such as verbatim memorization, training data extraction, recitation, verbatim quoting, and secret regurgitation. The settings vary across ordinary text, code or configuration quoted passages, quotations from interviews or movies, high-quality pre-training sources such as Wikipedia, and privacy-sensitive content such as PII, credit card numbers, or inserted canaries. Some descriptions emphasize extraction by adversarial or benign users, while others test continuation from fixed prefixes or benchmark examples; in the recitation variant, the target is specifically a highly duplicated sequence from the training corpus.

**Space of elicitation and scores.** One measurement instrument is explicitly linked to this behavior: AUXDATASET, a proxy corpus of internet text used to verify whether extracted outputs match potential training data. Papers often elicit the behavior by prompting with the first tokens or another prefix from a source example and then comparing the continuation with the ground truth or source passage. Scoring ranges from exact substring or token reproduction to n-gram matching and similarity metrics such as BLEU and ROUGE-L, including character-level 25-gram membership inference in some work.

**What it is taken as evidence of.** Papers link this behavior to two constructs. The prevailing construct link is to memorization: several papers claim a causal relationship from memorization to training data regurgitation, and some others relate the two more generally, describing memorization in terms of whether a model can regurgitate an example from its training data or saying memorized samples can later be extracted. A smaller line of work also claims a causal relationship from alignment to training data regurgitation, phrasing alignment as a guardrail against "inadvertent memorization and ... regurgitation in model outputs," so papers do not converge on a single associated construct.

## Sources

**Training data leakage** (2 papers: [A Statistical Approach for Controlled Training Data Detection](https://proceedings.iclr.cc/paper_files/paper/2025/file/c859b99b5d717c9035e79d43dfd69435-Paper-Conference.pdf), [Interpreting the Repeated Token Phenomenon in Large Language Models](https://raw.githubusercontent.com/mlresearch/v267/main/assets/yona25a/yona25a.pdf))
> The risk or phenomenon where private or copyrighted content from the training corpus is exposed or inferred through the model's outputs or internal signals.

**Verbatim regurgitation** (1 paper: [Mitigating Memorization in Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/e50ff94d174465348f15c45760f58f9f-Paper-Conference.pdf))
> The observable act of a language model generating text that is an exact, word-for-word copy of a sequence from its training data.

**Verbatim Reproduction** (1 paper: [Copyright-Protected Language Generation via Adaptive Model Fusion](https://proceedings.iclr.cc/paper_files/paper/2025/file/01953220e4becc6ac1078c24c1f8d3a7-Paper-Conference.pdf))
> Generating exact substrings present in the training data, indicating potential copyright infringement.

**Training data regurgitation** (1 paper: [Measuring memorization in RLHF for code completion](https://proceedings.iclr.cc/paper_files/paper/2025/file/22811d2089d4aa0ba66e52a5e47efb65-Paper-Conference.pdf))
> Reproducing training examples or their targets in model outputs when prompted with related context.

**Code reproduction** (1 paper: [Measuring Non-Adversarial Reproduction of Training Data in Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/861777345d8b03ec648e768cd54f1c42-Paper-Conference.pdf))
> Generating code or configuration text that matches existing online code snippets.

**Quotation reproduction** (1 paper: [Measuring Non-Adversarial Reproduction of Training Data in Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/861777345d8b03ec648e768cd54f1c42-Paper-Conference.pdf))
> The act of generating verbatim quotations from sources like interviews or movies, sometimes with incorrect or missing attribution.

**Text reproduction** (1 paper: [Measuring Non-Adversarial Reproduction of Training Data in Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/861777345d8b03ec648e768cd54f1c42-Paper-Conference.pdf))
> Producing output that contains verbatim substrings found in existing web text or training-data proxies.

**Literal copying** (1 paper: [Position: Iterative Online-Offline Joint Optimization is Needed to Manage Complex LLM Copyright Risks](https://raw.githubusercontent.com/mlresearch/v267/main/assets/pan25i/pan25i.pdf))
> The act of a model generating content that is a verbatim or near-verbatim copy of copyrighted material.

**Secret canary recovery** (1 paper: [Trustworthy Machine Learning through Data-Specific Indistinguishability](https://raw.githubusercontent.com/mlresearch/v267/main/assets/xiao25h/xiao25h.pdf))
> The task of a model generating specific secret digits (a 'canary') that were inserted into the training data, when prompted with the prefix of the secret phrase.

**Exact sequence reproduction** (1 paper: [Trustworthy Machine Learning through Data-Specific Indistinguishability](https://raw.githubusercontent.com/mlresearch/v267/main/assets/xiao25h/xiao25h.pdf))
> The task of a model exactly generating a specific number of subsequent tokens from a training example when prompted with a preceding sequence of tokens from that same example.

**Verbatim recall** (1 paper: [Minerva: A Programmable Memory Test Benchmark for Language Models](https://raw.githubusercontent.com/mlresearch/v267/main/assets/xia25c/xia25c.pdf))
> Reproducing the entire memory content as a verbatim copy.

**Recitation** (1 paper: [Recite, Reconstruct, Recollect: Memorization in LMs as a Multifaceted Phenomenon](https://proceedings.iclr.cc/paper_files/paper/2025/file/bbd87a328be4c7e43aa0b900a0ebf79a-Paper-Conference.pdf))
> A type of memorization characterized by the verbatim reproduction of sequences that are highly duplicated in the training corpus.

**Copyrighted text generation** (1 paper: [LLM Unlearning via Loss Adjustment with Only Forget Data](https://proceedings.iclr.cc/paper_files/paper/2025/file/6b315c0b736711b56f33cbacfb6d5d67-Paper-Conference.pdf))
> Generating passages that overlap with or resemble copyrighted source text given a prefix from that text.

**Training data extraction** (2 papers: [Scalable Extraction of Training Data from Aligned, Production Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/cce0e917b050208170151f77b497fc71-Paper-Conference.pdf), [UNDIAL: Self-Distillation with Adjusted Logits for Robust Unlearning in Large Language Models](https://aclanthology.org/2025.naacl-long.444.pdf))
> The observable act of a model generating verbatim sequences of text from its training data in response to user prompts.

**Verbatim memorization** (3 papers: [Private Memorization Editing: Turning Memorization into a Defense to Strengthen Data Privacy in Large Language Models](https://aclanthology.org/2025.acl-long.810.pdf), [Proving Test Set Contamination in Black-Box Language Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/46e624c244cff669223d488defd4e835-Paper-Conference.pdf), [Unlearning as multi-task optimization: A normalized gradient difference approach with an adaptive learning rate](https://aclanthology.org/2025.naacl-long.563.pdf))
> The observable behavior of a language model generating text that is an exact, word-for-word copy of examples present in its training data.

**Secret extraction** (1 paper: [Teach LLMs to Phish: Stealing Private Information from Language Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/f206871468dc89cb20fefbc75f2de861-Paper-Conference.pdf))
> The observable generation of a sensitive string (e.g., credit card number) by the model when prompted with a prefix, indicating successful retrieval of memorized private information.

**Verbatim quoting** (1 paper: [Verifiable by Design: Aligning Language Models to Quote from Pre-Training Data](https://aclanthology.org/2025.naacl-long.191.pdf))
> The observable generation of exact text segments from a model's pre-training data, particularly from high-quality sources like Wikipedia, identifiable through n-gram matching.

**Text regurgitation** (1 paper: [PoisonedParrot: Subtle Data Poisoning Attacks to Elicit Copyright-Infringing Content from Large Language Models](https://aclanthology.org/2025.naacl-long.415.pdf))
> The observable act of the model reproducing content it has previously seen, particularly from its training data.

**Secret regurgitation** (1 paper: [Empirical Privacy Variance](https://raw.githubusercontent.com/mlresearch/v267/main/assets/hu25x/hu25x.pdf))
> The observable act of a model generating sensitive information (secrets) from its training data in response to a prompt.

## Relationships

### Training data regurgitation →
- **AUXDATASET** (measurement instrument): *measured_by*, 1 paper
  > To verify the success of our attack, we construct a 9 terabyte dataset (AUXDATASET), combining many sources of Internet text, to serve as a proxy for the unknown training datasets for these production models. (Section 1)
  - [Scalable Extraction of Training Data from Aligned, Production Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/cce0e917b050208170151f77b497fc71-Paper-Conference.pdf)

### → Training data regurgitation
- **Memorization** (construct): *causes*, 6 papers
  > Since verbatim reproduction often stems from memorization during training
  - [Copyright-Protected Language Generation via Adaptive Model Fusion](https://proceedings.iclr.cc/paper_files/paper/2025/file/01953220e4becc6ac1078c24c1f8d3a7-Paper-Conference.pdf)
  - [Scalable Extraction of Training Data from Aligned, Production Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/cce0e917b050208170151f77b497fc71-Paper-Conference.pdf)
  - [A Statistical Approach for Controlled Training Data Detection](https://proceedings.iclr.cc/paper_files/paper/2025/file/c859b99b5d717c9035e79d43dfd69435-Paper-Conference.pdf)
  - [Measuring memorization in RLHF for code completion](https://proceedings.iclr.cc/paper_files/paper/2025/file/22811d2089d4aa0ba66e52a5e47efb65-Paper-Conference.pdf)
  - [Measuring memorization in language models via probabilistic extraction](https://aclanthology.org/2025.naacl-long.469.pdf)
  - [The Canary’s Echo: Auditing Privacy Risks of LLM-Generated Synthetic Text](https://raw.githubusercontent.com/mlresearch/v267/main/assets/meeus25a/meeus25a.pdf)
- **Alignment** (construct): *causes*, 1 paper
  > Model alignment is a guardrail to prevent unwarranted behaviors, including “inadvertent memorization and [...] regurgitation in model outputs.” (Section 2)
  - [Scalable Extraction of Training Data from Aligned, Production Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/cce0e917b050208170151f77b497fc71-Paper-Conference.pdf)
- **Repetitive generation** (behavioral indicator): *causes*, 1 paper
  > Nasr et al. (2023) first observed that repeated tokens could confuse models, creating a vulnerability exploitable for training data leakage attacks. (Section 5)
  - [Interpreting the Repeated Token Phenomenon in Large Language Models](https://raw.githubusercontent.com/mlresearch/v267/main/assets/yona25a/yona25a.pdf)
