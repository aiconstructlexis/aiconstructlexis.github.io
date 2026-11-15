# LMSYS-Chat-1M
**Type:** Measurement instrument  
**Supporting papers:** 7  
**Also known as:** LMSYS-chat-1M, LMSys-Chat-1M, LmsysChat  

## State of the Field

**What it is.** Across papers, the prevailing description is a large dataset of real-world chat interactions. Definitions variously call it a dataset of real-world user prompts and conversations, real-world LLM conversations, or user-model conversations; one paper specifies an open-access collection of 1 million user conversations from the Chatbot Arena platform, while another describes real-world conversations with 25 state-of-the-art LLMs. Papers typically treat it as a source from which prompts or conversation samples are drawn for chat model fine-tuning and evaluation.

**What it is claimed to measure.** Papers do not explicitly present LMSYS-Chat-1M as measuring any named construct or behavioral indicator. Instead, papers use it as an evaluation source in several ways: to assess non-adversarial reproduction in practical chat settings, to supply out-of-distribution prompts for classifier generalization tests, to represent realistic use cases, and to analyze real-world usage patterns. These uses spread across several evaluation aims rather than converging on one named measured construct.

**Space of uses.** Most commonly, papers use LMSYS-Chat-1M as a prompt or conversation pool for downstream experiments. It appears most often alongside WildChat, either as a parallel dataset for rerunning analyses or as one of two open-access real-world conversation collections; a smaller line of work contrasts it with UltraChat as synthetic. Other papers draw samples from it for specific procedures, including prompt selection for model fine-tuning, sampling anthropomorphic outputs from commercial models, and taking a small set of prompts to better represent real-world use cases.

## Sources

**LMSYS-chat-1M** (1 paper: [Learning from negative feedback, or positive feedback or both](https://proceedings.iclr.cc/paper_files/paper/2025/file/162f1442c568f639b846a00ddc5edbd4-Paper-Conference.pdf))
> A large-scale dataset of real-world user prompts and conversations used as a source of inputs for fine-tuning and evaluating chat-oriented language models.

**LMSYS-Chat-1M** (3 papers: [Measuring Non-Adversarial Reproduction of Training Data in Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/861777345d8b03ec648e768cd54f1c42-Paper-Conference.pdf), [Position: Societal Impacts Research Requires Benchmarks for Creative Composition Tasks](https://raw.githubusercontent.com/mlresearch/v267/main/assets/shen25r/shen25r.pdf), [Estimating LLM Consistency: A User Baseline vs Surrogate Metrics](https://aclanthology.org/2025.emnlp-main.1554.pdf))
> A large dataset of real-world LLM conversations used here to assess non-adversarial reproduction in practical chat settings.

**LMSys-Chat-1M** (1 paper: [Dehumanizing Machines: Mitigating Anthropomorphic Behaviors in Text Generation Systems](https://aclanthology.org/2025.acl-long.1259.pdf))
> A dataset of real-world conversations with 25 state-of-the-art LLMs, used to sample anthropomorphic outputs from commercial models.

**LmsysChat** (1 paper: [Idiosyncrasies in Large Language Models](https://raw.githubusercontent.com/mlresearch/v267/main/assets/sun25z/sun25z.pdf))
> A dataset capturing real-world user interactions, used as a source of out-of-distribution prompts for testing classifier generalization.
