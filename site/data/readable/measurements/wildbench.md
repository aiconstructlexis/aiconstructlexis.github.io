# WildBench
**Type:** Measurement instrument  
**Supporting papers:** 14  
**Also known as:** Wildbench, Wild-Bench  

## State of the Field

**What it is.** Most papers describe WildBench as an instruction-following benchmark for evaluating LLM responses, usually with diverse task categories and a fine-grained grading scale against a reference answer. A smaller line of work describes it as an LLM-based evaluation framework or public dataset of model comparisons judged by an LLM judge, while other descriptions present it as a challenging instruction-following QA benchmark with long, multi-turn prompts, real-user questions, human preference judgments, and 1024 manually selected questions from the same source as WildChat; one paper also refers to a WildBench WB-Score.

**What it is claimed to measure.** Papers use WildBench to measure 7 constructs and 5 behavioral indicators. These links are spread across several abilities, including complex reasoning, conversational ability, creativity, instruction following ability, and long-context reasoning, plus 2 other construct links; behavioral indicators include creative writing, data analysis, instruction following, question answering, and role-playing. In the quoted descriptions, the tasks are also said to involve higher-order reasoning and multiple constraints.

**Space of uses.** A recurring usage is as one benchmark in suites that also include AlpacaEval or AlpacaEval2, Arena-Hard, and sometimes MT-Bench, for general instruction-following, chatbot scenarios, or subjective evaluation. Some papers use WildBench through its public dataset for LLM-based evaluation, and related work explicitly treats it as related to LLM-as-a-judge. One paper also reports that WildBench is correlated with Chatbot Arena, describing a strong correlation with human-voted Elo ratings on hard tasks.

**Concerns raised.** One line of work re-evaluates the evaluation protocols used in WildBench alongside other automatic instruction-following benchmarks.

## Sources

**WildBench** (5 papers: [Instruct-SkillMix: A Powerful Pipeline for LLM Instruction Tuning](https://proceedings.iclr.cc/paper_files/paper/2025/file/473a9a75edc46eff5ff224d53d5f7294-Paper-Conference.pdf), [Genius: A Generalizable and Purely Unsupervised Self-Training Framework For Advanced Reasoning](https://aclanthology.org/2025.acl-long.644.pdf), [R.I.P.: Better Models by Survival of the Fittest Prompts](https://raw.githubusercontent.com/mlresearch/v267/main/assets/yu25u/yu25u.pdf), [User Feedback in Human-LLM Dialogues: A Lens to Understand Users But Noisy as a Learning Signal](https://aclanthology.org/2025.emnlp-main.133.pdf), [ReIFE: Re-evaluating Instruction-Following Evaluation](https://aclanthology.org/2025.naacl-long.610.pdf))
> An instruction-following benchmark that uses a diverse distribution of task categories and a fine-grained grading scale to evaluate model responses against a reference answer.

**Wildbench** (1 paper: [Polyrating: A Cost-Effective and Bias-Aware Rating System for LLM Evaluation](https://proceedings.iclr.cc/paper_files/paper/2025/file/d06537b4b38ccf008a54559d2c56fa23-Paper-Conference.pdf))
> An LLM-based evaluation framework used as a public dataset of model comparisons judged by an LLM-based judge.

**Wild-Bench** (1 paper: [As Simple as Fine-tuning: LLM Alignment via Bidirectional Negative Feedback Loss](https://proceedings.iclr.cc/paper_files/paper/2025/file/4bc4e9ecd5ae4a75048dc216a770cba1-Paper-Conference.pdf))
> A challenging instruction-following QA benchmark featuring long, multi-turn prompts and difficult questions sourced from real users.

## Relationships

### → WildBench
- **Conversational ability** (construct): *measured_by*, 1 paper
  > In this section we evaluate the Jamba-1.5 models on two chatbot scenarios: Arena-Hard (Li et al., 2024b), a set of 500 challenging user queries that uses GPT4-Turbo as a judge, and WildBench (Lin et al., 2024)... (Section 7.3)
  - [Jamba: Hybrid Transformer-Mamba Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/a9ed43fa31dc8b4a7d7a673d713dcb5f-Paper-Conference.pdf)
- **Complex reasoning** (construct): *measured_by*, 1 paper
  > Complex real-user tasks usually have multiple constraints and require higher-order reasoning skills, which are well represented in WILDBENCH. (Figure 1)
  - [WildBench: Benchmarking LLMs with Challenging Tasks from Real Users in the Wild](https://proceedings.iclr.cc/paper_files/paper/2025/file/771155abaae744e08576f1f3b4b7ac0d-Paper-Conference.pdf)
- **Creativity** (construct): *measured_by*, 1 paper
  > These tasks often require critical thinking, creativity, and technical expertise, making WILDBENCH substantially more challenging than AlpacaEval... (Section 1)
  - [WildBench: Benchmarking LLMs with Challenging Tasks from Real Users in the Wild](https://proceedings.iclr.cc/paper_files/paper/2025/file/771155abaae744e08576f1f3b4b7ac0d-Paper-Conference.pdf)
- **Technical expertise** (construct): *measured_by*, 1 paper
  > These tasks often require critical thinking, creativity, and technical expertise, making WILDBENCH substantially more challenging than AlpacaEval... (Section 1)
  - [WildBench: Benchmarking LLMs with Challenging Tasks from Real Users in the Wild](https://proceedings.iclr.cc/paper_files/paper/2025/file/771155abaae744e08576f1f3b4b7ac0d-Paper-Conference.pdf)
- **Long-context reasoning** (construct): *measured_by*, 1 paper
  > Thanks to these realistic user activities, WILDBENCH is a more suitable benchmark for testing the long-context problem solving abilities of LLMs. (Section 2.2)
  - [WildBench: Benchmarking LLMs with Challenging Tasks from Real Users in the Wild](https://proceedings.iclr.cc/paper_files/paper/2025/file/771155abaae744e08576f1f3b4b7ac0d-Paper-Conference.pdf)
- **Data analysis** (behavioral indicator): *measured_by*, 1 paper
  > This dataset is particularly suited for conversion into an evaluation benchmark because it contains a diverse array of tasks that users expect LLMs to perform, such as writing assistance, coding, mathematics, data analysis, role playing, and planning. (Section 2.1)
  - [WildBench: Benchmarking LLMs with Challenging Tasks from Real Users in the Wild](https://proceedings.iclr.cc/paper_files/paper/2025/file/771155abaae744e08576f1f3b4b7ac0d-Paper-Conference.pdf)
- **Role-playing** (behavioral indicator): *measured_by*, 1 paper
  > This dataset is particularly suited for conversion into an evaluation benchmark because it contains a diverse array of tasks that users expect LLMs to perform, such as writing assistance, coding, mathematics, data analysis, role playing, and planning. (Section 2.1)
  - [WildBench: Benchmarking LLMs with Challenging Tasks from Real Users in the Wild](https://proceedings.iclr.cc/paper_files/paper/2025/file/771155abaae744e08576f1f3b4b7ac0d-Paper-Conference.pdf)
- **Planning** (construct): *measured_by*, 1 paper
  > This dataset is particularly suited for conversion into an evaluation benchmark because it contains a diverse array of tasks that users expect LLMs to perform, such as writing assistance, coding, mathematics, data analysis, role playing, and planning. (Section 2.1)
  - [WildBench: Benchmarking LLMs with Challenging Tasks from Real Users in the Wild](https://proceedings.iclr.cc/paper_files/paper/2025/file/771155abaae744e08576f1f3b4b7ac0d-Paper-Conference.pdf)
- **Question answering** (behavioral indicator): *measured_by*, 1 paper
  > We primarily evaluate all the models using two recent proposed instruction-following QA benchmarks: Arena-Hard (Li et al., 2024) and Wild-Bench(Lin et al., 2024).
  - [As Simple as Fine-tuning: LLM Alignment via Bidirectional Negative Feedback Loss](https://proceedings.iclr.cc/paper_files/paper/2025/file/4bc4e9ecd5ae4a75048dc216a770cba1-Paper-Conference.pdf)
- **Creative writing** (behavioral indicator): *measured_by*, 1 paper
  > “The tasks in WILDBENCH typically demand higher-order reasoning, such as ... creative writing with multiple constraints on the style and content”
  - [WildBench: Benchmarking LLMs with Challenging Tasks from Real Users in the Wild](https://proceedings.iclr.cc/paper_files/paper/2025/file/771155abaae744e08576f1f3b4b7ac0d-Paper-Conference.pdf)
- **Instruction following** (behavioral indicator): *measured_by*, 1 paper
  > "we evaluate the evaluation protocols used in three automatic LLM benchmarks for instruction-following4 – AlpacaEval (Li et al., 2023c), ArenaHard (Li et al., 2024b), and WildBench (Lin et al., 2024)"
  - [ReIFE: Re-evaluating Instruction-Following Evaluation](https://aclanthology.org/2025.naacl-long.610.pdf)
- **Instruction following ability** (construct): *measured_by*, 1 paper
  > We primarily assess models’ general instruction-following capabilities on three evaluation benchmarks: AlpacaEval2 (Li et al., 2023b), Arena-Hard (Li et al., 2024b) and Wild-Bench (Lin et al., 2024). (Section 5)
  - [R.I.P.: Better Models by Survival of the Fittest Prompts](https://raw.githubusercontent.com/mlresearch/v267/main/assets/yu25u/yu25u.pdf)
- **Chatbot Arena** (measurement instrument): *correlates*, 1 paper
  > “WILD-BENCH results demonstrate a strong correlation with the human-voted Elo ratings from Chatbot Arena on hard tasks.”
  - [WildBench: Benchmarking LLMs with Challenging Tasks from Real Users in the Wild](https://proceedings.iclr.cc/paper_files/paper/2025/file/771155abaae744e08576f1f3b4b7ac0d-Paper-Conference.pdf)

### Associated with
- **LLM-as-a-judge** (measurement instrument), 2 papers
  > We use the public dataset from Wildbench (Lin et al., 2024) to obtain our LLM-based evaluation. (Section 4.2)
  - [Polyrating: A Cost-Effective and Bias-Aware Rating System for LLM Evaluation](https://proceedings.iclr.cc/paper_files/paper/2025/file/d06537b4b38ccf008a54559d2c56fa23-Paper-Conference.pdf)
  - [Diverging Preferences: When do Annotators Disagree and do Models Know?](https://raw.githubusercontent.com/mlresearch/v267/main/assets/zhang25bx/zhang25bx.pdf)
