# G-Eval
**Type:** Measurement instrument  
**Supporting papers:** 13  
**Also known as:** G-EVAL, G-Eval-4  

## State of the Field

**What it is.** Across the papers, the prevailing usage treats G-Eval as an LLM-based automated evaluation framework for generated text. Most definitions describe GPT-4 assigning criterion-level, often 1-5 Likert-scale, scores from a prompt, sometimes step by step with chain-of-thought prompting; applications mentioned include summaries, patent claims, dialogue responses, and condition, answer, and citation-related outputs. A smaller line of work describes it as an auto-CoT framework that generates evaluation steps, as a GPT-4 rubric for helpfulness, honesty, and harmlessness, or as a logit-weighted scoring method that reweights score tokens by the model's own predicted probabilities. Papers also mention adaptations and variants, including GCC-Eval for chess and G-Eval-4, where GPT-4 is sampled 20 times and the average score is used.

**What it is claimed to measure.** The measurement claims cover multiple output-quality constructs rather than a single recurring one. Papers link it to eight constructs and one behavioral indicator, most frequently as a measure of Coherence, Fluency, Relevance, Empathy, and Faithfulness, with three other constructs also linked. The behavioral-indicator link is a related, not measured_by, claim, and some papers describe G-Eval as producing criterion-specific scores for fine-grained analysis.

**Space of uses.** In use, papers often place G-Eval alongside automatic evaluation and human judgment, and the only linked instrument is Human evaluation. One study reports that G-Eval has the closest alignment with human ratings, with a Pearson correlation coefficient of 0.41. Other papers position it as a baseline or reference LLM judge, including an auto-CoT baseline for assessment, and use or adapt it in domain-specific settings such as chess commentary.

**Concerns raised.** The main concern stated in the papers is evaluator dependence: one paper notes that the evaluation can be largely limited by the performance of the evaluator LLM itself.

## Sources

**G-Eval** (6 papers: [Learning to Summarize from LLM-generated Feedback](https://aclanthology.org/2025.naacl-long.38.pdf), [Patent-CR: A Dataset for Patent Claim Revision](https://aclanthology.org/2025.naacl-long.116.pdf), [Bridging the Gap between Expert and Language Models: Concept-guided Chess Commentary Generation and Evaluation](https://aclanthology.org/2025.naacl-long.481.pdf), [Towards Lifelong Dialogue Agents via Timeline-based Memory Management](https://aclanthology.org/2025.naacl-long.435.pdf), [Improving Preference Extraction In LLMs By Identifying Latent Knowledge Through Classifying Probes](https://aclanthology.org/2025.acl-long.444.pdf), [InsightBench: Evaluating Business Analytics Agents Through Multi-Step Insight Generation](https://proceedings.iclr.cc/paper_files/paper/2025/file/0dfe31d6e703e138d46a7d2fced38b7c-Paper-Conference.pdf))
> An automated evaluation protocol that uses a large language model (like GPT-4) to provide Likert-scale scores (1-5) for summary quality based on a given prompt.

**G-EVAL** (1 paper: [CSEval: Towards Automated, Multi-Dimensional, and Reference-Free Counterspeech Evaluation using Auto-Calibrated LLMs](https://aclanthology.org/2025.naacl-long.279.pdf))
> An auto-CoT prompting framework for natural language generation evaluation that uses chain-of-thought reasoning to generate evaluation steps, used here as a baseline for LLM-based assessment.

**G-Eval-4** (1 paper: [K-COMP: Retrieval-Augmented Medical Domain Question Answering With Knowledge-Injected Compressor](https://aclanthology.org/2025.naacl-long.351.pdf))
> Advanced LLM-based evaluation metric using GPT-4 to assess generated answers across multiple dimensions with high correlation to human judgment.

## Relationships

### G-Eval →
- **Human evaluation** (measurement instrument): *correlates*, 1 paper
  > G-Eval demonstrates the closest alignment with human ratings, with a Pearson correlation coefficient of 0.41.
  - [SPORTU: A Comprehensive Sports Understanding Benchmark for Multimodal Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/49c1879ae366644ce2c17fb39ddea982-Paper-Conference.pdf)

### → G-Eval
- **Coherence** (construct): *measured_by*, 3 papers
  > For LLM-based evaluation, we employed G-EVAL(Liu et al., 2023), a state-of-the-art metric designed to assess various qualitative aspects of large language model outputs, including Fluency, Coherence, Naturalness, Empathy, and Patient-Centricity, where higher scores indicate better performance. (Section 5.1)
  - [AI Chatbots as Professional Service Agents: Developing a Professional Identity](https://aclanthology.org/2025.emnlp-main.652.pdf)
  - [MemInsight: Autonomous Memory Augmentation for LLM Agents](https://aclanthology.org/2025.emnlp-main.1683.pdf)
  - [Paired by the Teacher: Turning Unpaired Data into High-Fidelity Pairs for Low-Resource Text Generation](https://aclanthology.org/2025.emnlp-main.1030.pdf)
- **Fluency** (construct): *measured_by*, 2 papers
  > For LLM-based evaluation, we employed G-EVAL(Liu et al., 2023), a state-of-the-art metric designed to assess various qualitative aspects of large language model outputs, including Fluency, Coherence, Naturalness, Empathy, and Patient-Centricity, where higher scores indicate better performance. (Section 5.1)
  - [AI Chatbots as Professional Service Agents: Developing a Professional Identity](https://aclanthology.org/2025.emnlp-main.652.pdf)
  - [Paired by the Teacher: Turning Unpaired Data into High-Fidelity Pairs for Low-Resource Text Generation](https://aclanthology.org/2025.emnlp-main.1030.pdf)
- **Relevance** (construct): *measured_by*, 2 papers
  > For Event Summarization, we adopt G-Eval (Liu et al., 2023b), an LLM-based metric that evaluates the relevance, consistency, and coherence of generated summaries against reference labels. (Section 4.3)
  - [MemInsight: Autonomous Memory Augmentation for LLM Agents](https://aclanthology.org/2025.emnlp-main.1683.pdf)
  - [Paired by the Teacher: Turning Unpaired Data into High-Fidelity Pairs for Low-Resource Text Generation](https://aclanthology.org/2025.emnlp-main.1030.pdf)
- **Faithfulness** (construct): *measured_by*, 1 paper
  > We provide the TALM with dialogue history that includes the API call results and use G-Eval (Liu et al., 2023) to assess whether the responses reflect the API call output. (Section 4.1)
  - [ToolDial: Multi-turn Dialogue Generation Method for Tool-Augmented Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/afb27164624b641e8fbba961b2301acf-Paper-Conference.pdf)
- **Interpretability and explainability** (construct): *measured_by*, 1 paper
  > G-EVAL generates criterion-specific scores, supporting fine-grained analysis of response quality, explainability, and reasoning. (Section 4.3)
  - [PAKTON: A Multi-Agent Framework for Question Answering in Long Legal Agreements](https://aclanthology.org/2025.emnlp-main.403.pdf)
- **Naturalness** (construct): *measured_by*, 1 paper
  > For LLM-based evaluation, we employed G-EVAL(Liu et al., 2023), a state-of-the-art metric designed to assess various qualitative aspects of large language model outputs, including Fluency, Coherence, Naturalness, Empathy, and Patient-Centricity, where higher scores indicate better performance. (Section 5.1)
  - [AI Chatbots as Professional Service Agents: Developing a Professional Identity](https://aclanthology.org/2025.emnlp-main.652.pdf)
- **Empathy** (construct): *measured_by*, 1 paper
  > For LLM-based evaluation, we employed G-EVAL(Liu et al., 2023), a state-of-the-art metric designed to assess various qualitative aspects of large language model outputs, including Fluency, Coherence, Naturalness, Empathy, and Patient-Centricity, where higher scores indicate better performance. (Section 5.1)
  - [AI Chatbots as Professional Service Agents: Developing a Professional Identity](https://aclanthology.org/2025.emnlp-main.652.pdf)
- **Patient-centricity** (construct): *measured_by*, 1 paper
  > For LLM-based evaluation, we employed G-EVAL(Liu et al., 2023), a state-of-the-art metric designed to assess various qualitative aspects of large language model outputs, including Fluency, Coherence, Naturalness, Empathy, and Patient-Centricity, where higher scores indicate better performance. (Section 5.1)
  - [AI Chatbots as Professional Service Agents: Developing a Professional Identity](https://aclanthology.org/2025.emnlp-main.652.pdf)

### Associated with
- **Chain of thought** (behavioral indicator), 1 paper
  > Furthermore, we report G-EVAL (Liu et al., 2023a), an auto-CoT prompting framework, and the current state-of-the-art in NLG evaluation. (Section 5.1)
  - [CSEval: Towards Automated, Multi-Dimensional, and Reference-Free Counterspeech Evaluation using Auto-Calibrated LLMs](https://aclanthology.org/2025.naacl-long.279.pdf)
