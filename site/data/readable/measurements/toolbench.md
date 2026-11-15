# ToolBench
**Type:** Measurement instrument  
**Supporting papers:** 22  
**Also known as:** Toolbench  

## State of the Field

**What it is.** Across the surveyed work, ToolBench is most commonly described as a benchmark or benchmark dataset for evaluating LLM agents' tool use, built around real-world REST APIs, user requests or instructions, and interaction traces or expert trajectories. Definitions vary on whether it is primarily an evaluation benchmark, an instruction-tuning dataset, or a serving workload: some papers describe more than 16k APIs from 49 categories, over 10,000 queries with full interactions, or training demonstrations with complex task-solving traces, while one paper characterizes it by prompts that include tool demonstrations and calls. Several papers also refer to specific slices of the resource, including a second release, test tasks, around 1,000 test cases, or four environments such as Home Search, Trip Booking, Google Sheets, and Virtual Home.

**What it is claimed to measure.** Papers link ToolBench to 3 constructs and 2 behavioral indicators. The prevailing claim is that it measures Tool use, with additional use for Information retrieval; at the construct level it is reported as measuring Decision-making, Reasoning, and Sequential decision-making. The recorded claims therefore spread across several named targets, with papers describing API-calling accuracy on ToolBench, saying it evaluates multi-turn reasoning and tool-usage abilities, and using it for intricate multi-step decision tasks.

**Space of uses.** No measurement instrument is linked to it through the recorded relations. In use, papers often treat ToolBench as one benchmark within broader suites, pairing it with Game of 24, WebShop, API-Bank, APIBench, and BFCL-v2, while other studies place it next to GSM8K or other open-source tool-learning benchmarks. Papers also use it in multiple roles: as a main evaluation set for test tasks or specific environments, as a corpus from which retrieval and end-to-end agent-tuning data are converted, and as a workload for serving experiments.

## Sources

**ToolBench** (9 papers: [ToolChain*: Efficient Action Space Navigation in Large Language Models with A* Search](https://proceedings.iclr.cc/paper_files/paper/2024/file/13250eb13871b3c2c0a0667b54bad165-Paper-Conference.pdf), [ToolLLM: Facilitating Large Language Models to Master 16000+ Real-world APIs](https://proceedings.iclr.cc/paper_files/paper/2024/file/28e50ee5b72e90b50e7196fde8ea260e-Paper-Conference.pdf), [Advancing Tool-Augmented Large Language Models: Integrating Insights from Errors in Inference Trees](https://proceedings.neurips.cc/paper_files/paper/2024/file/c0f7ee1901fef1da4dae2b88dfd43195-Paper-Conference.pdf), [Rational Decision-Making Agent with Learning Internal Utility Judgment](https://proceedings.iclr.cc/paper_files/paper/2025/file/45994782a61bb51cad5c2bae36834265-Paper-Conference.pdf), [From Allies to Adversaries: Manipulating LLM Tool-Calling through Adversarial Injection](https://aclanthology.org/2025.naacl-long.101.pdf), [EASYTOOL: Enhancing LLM-based Agents with Concise Tool Instruction](https://aclanthology.org/2025.naacl-long.44.pdf), [xLAM: A Family of Large Action Models to Empower AI Agent Systems](https://aclanthology.org/2025.naacl-long.578.pdf), [Mimicking the Familiar: Dynamic Command Generation for Information Theft Attacks in LLM Tool-Learning System](https://aclanthology.org/2025.acl-long.672.pdf), [Tool Unlearning for Tool-Augmented LLMs](https://raw.githubusercontent.com/mlresearch/v267/main/assets/cheng25a/cheng25a.pdf))
> A benchmark suite for evaluating the tool-use capabilities of LLM agents across various environments, including Home Search, Trip Booking, Google Sheets, and Virtual Home.

**Toolbench** (1 paper: [Preble: Efficient Distributed Prompt Scheduling for LLM Serving](https://proceedings.iclr.cc/paper_files/paper/2025/file/5bc342f48de8264779952fac378f96dc-Paper-Conference.pdf))
> A workload used to evaluate an LLM's ability to use tools, characterized by prompts that include tool demonstrations and calls.

## Relationships

### → ToolBench
- **Tool use** (behavioral indicator): *measured_by*, 5 papers
  > The ability to use external tools is a significant milestone in the development of LLMs... For this purpose, we utilize the large-scale tool usage dataset ToolBench [21]... (Section 3.2)
  - [StreamBench: Towards Benchmarking Continuous Improvement of Language Agents](https://proceedings.neurips.cc/paper_files/paper/2024/file/c189915371c4474fe9789be3728113fc-Paper-Datasets_and_Benchmarks_Track.pdf)
  - [Understanding the Generalization of In-Context Learning in Transformers: An Empirical Study](https://proceedings.iclr.cc/paper_files/paper/2025/file/bd19ca8039547b339a6a37bd4df24405-Paper-Conference.pdf)
  - [xLAM: A Family of Large Action Models to Empower AI Agent Systems](https://aclanthology.org/2025.naacl-long.578.pdf)
  - [PORTS: Preference-Optimized Retrievers for Tool Selection with Large Language Models](https://aclanthology.org/2025.emnlp-main.507.pdf)
  - [ToolChain*: Efficient Action Space Navigation in Large Language Models with A* Search](https://proceedings.iclr.cc/paper_files/paper/2024/file/13250eb13871b3c2c0a0667b54bad165-Paper-Conference.pdf)
- **Information retrieval** (behavioral indicator): *measured_by*, 1 paper
  > Our experiments are based on ToolBench, a real-world tool benchmark containing more 16k tool collections... Our retrieval and end-to-end agent-tuning data are converted from the original data in ToolBench. (Section 4.1)
  - [ToolGen: Unified Tool Retrieval and Calling via Generation](https://proceedings.iclr.cc/paper_files/paper/2025/file/b646bdebeb87dfafe2c6f77a63b564e1-Paper-Conference.pdf)
- **Sequential decision-making** (construct): *measured_by*, 1 paper
  > conduct extensive experiments on Game of 24 (Yao et al., 2023), WebShop (Yao et al., 2022a), ToolBench (Qin et al., 2023c) and RestBench (Song et al., 2023), which contains intricate multi-step decision tasks involving diverse scenarios.
  - [Rational Decision-Making Agent with Learning Internal Utility Judgment](https://proceedings.iclr.cc/paper_files/paper/2025/file/45994782a61bb51cad5c2bae36834265-Paper-Conference.pdf)
- **Decision-making** (construct): *measured_by*, 1 paper
  > We use 100, 500, and 500 instances for Game of 24, WebShop, and ToolBench to evaluate the decision-making ability respectively.
  - [Rational Decision-Making Agent with Learning Internal Utility Judgment](https://proceedings.iclr.cc/paper_files/paper/2025/file/45994782a61bb51cad5c2bae36834265-Paper-Conference.pdf)
- **Reasoning** (construct): *measured_by*, 1 paper
  > ToolBench (Qin et al., 2024) specifically evaluates multi-turn reasoning and tool-usage abilities
  - [xLAM: A Family of Large Action Models to Empower AI Agent Systems](https://aclanthology.org/2025.naacl-long.578.pdf)
