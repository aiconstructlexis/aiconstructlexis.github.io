# Tool use ability
**Type:** Construct  
**Supporting papers:** 38  
**Also known as:** Tool reliability, Execution, Tool selection, Tool utilization, Tool-use proficiency, Tool utilization capability, Tool-use capability, Tool-use ability, Tool Use, Tool-usage reasoning, Tool learning, Tool comprehension, Tool-using capability, Tool manipulation, Tool-calling decision-making, Tool-calling capability, Flexible tool selection, Function-calling capability, Tool-using ability, API call generation capability, Planning with functions, Function-calling ability, Contextualised tool use  

## State of the Field

**Space of definitions.** Across papers, the prevailing usage treats this as a latent capability of an LLM or agent to choose, invoke, and use external tools or APIs to complete tasks or satisfy user requests. Most definitions stay close to that core, while some broaden it to selecting parameters, coordinating or sequencing multiple tools, processing tool outputs, or leveraging tools such as web browsing, code execution, and file uploads. A smaller line of work narrows it to specific sub-capabilities, such as function calling, API call generation, flexible tool selection, or deciding whether to call a tool, ask for more information, admit inability, or answer directly. The clearest disagreement is latent capacity versus observable process: most papers use the former, while some uses of tool utilization describe a staged interaction pipeline, and another variant frames the construct as reliable interaction throughout a task that maximizes success while minimizing errors and hallucinations.

**Space of facets.** Papers break the construct into recurring facets: understanding what a tool does and when to invoke it, selecting the appropriate tool, generating valid function or API calls with suitable arguments, planning and sequencing calls for decomposed tasks, and applying or orchestrating tools through nested calling. Some versions make conversational context part of the construct, defining effective use through integration of dialogue history and user profile, while others emphasize reliability and hallucination control during tool invocation. One paper explicitly separates reasoning from execution, treating reasoning as analysis and planning that comes first, followed by selecting the correct functions and parameters. Labels vary across papers, including tool-use proficiency, tool-calling capability, function-calling ability, and tool utilization, and the last of these is used both for a latent ability and for an observable process.

**Space of measurement.** Operationalization is dominated by benchmarks and evaluators: papers link the construct to 7 measurement instruments and 1 behavioral indicator. The most frequently linked instruments are API-Bank, BFCL, BFCL-v2, GAIA, and GTA, plus 2 other instruments. API-Bank is described as a dialogue-style tool-call dataset in which models call predefined Python tools and are scored by whether tool return values match the ground truth, BFCL as a comprehensive executable function-call evaluation, GAIA as real-world questions requiring tool-use proficiency, and GTA as a benchmark with a step-by-step mode for fine-grained tool-use capability. The remaining linked instruments include an automatic evaluator and a simulator in which a model simulates tool returns and evaluates process and response accuracy. Across these measures, operationalization mostly centers on tool invocation and function calling, which aligns most directly with the common definitions, while contextualized use, follow-up questioning, and hallucination minimization are not foregrounded in the linked measurements.

**Links.** Beyond measurement, multiple papers claim a causal relationship from Tool use ability to Tool use, describing tool learning as enabling LLMs to interact with external environments by invoking tools. One paper claims a causal relationship from Instruction following ability to Tool use ability, reporting that models with better instruction-following capabilities achieve greater improvements with high-quality tool instructions. Tool use ability is also reported to correlate inversely with Irrelevance detection ability, and one paper relates it to Reasoning, describing reasoning as the comprehension, analysis, and planning that precede selecting the correct functions and parameters.

## Sources

**Tool reliability** (1 paper: [Reducing Tool Hallucination via Reliability Alignment](https://raw.githubusercontent.com/mlresearch/v267/main/assets/xu25ap/xu25ap.pdf))
> The ability of a large language model to accurately and effectively interact with external tools throughout a task, maximizing successful outcomes while minimizing errors and hallucinations.

**Execution** (1 paper: [MoRAgent: Parameter Efficient Agent Tuning with Mixture-of-Roles](https://raw.githubusercontent.com/mlresearch/v267/main/assets/han25j/han25j.pdf))
> The latent ability to select appropriate functions and parameters to invoke based on reasoning input, enabling tool use in agent tasks.

**Tool selection** (1 paper: [Can LLMs Help You at Work? A Sandbox for Evaluating LLM Agents in Enterprise Environments](https://aclanthology.org/2025.emnlp-main.466.pdf))
> The underlying capability of an LLM agent to identify and choose the appropriate enterprise tools or APIs required to perform a given subtask.

**Tool utilization** (5 papers: [Watch Out for Your Agents! Investigating Backdoor Threats to LLM-Based Agents](https://proceedings.neurips.cc/paper_files/paper/2024/file/b6e9d6f4f3428cd5f3f9e9bbae2cab10-Paper-Conference.pdf), [MeNTi: Bridging Medical Calculator and LLM Agent with Nested Tool Calling](https://aclanthology.org/2025.naacl-long.263.pdf), [EASYTOOL: Enhancing LLM-based Agents with Concise Tool Instruction](https://aclanthology.org/2025.naacl-long.44.pdf), [Towards Rationality in Language and Multimodal Agents: A Survey](https://aclanthology.org/2025.naacl-long.186.pdf), [MoRAgent: Parameter Efficient Agent Tuning with Mixture-of-Roles](https://raw.githubusercontent.com/mlresearch/v267/main/assets/han25j/han25j.pdf))
> The latent ability to select and invoke external tools appropriately during task execution.

**Tool-use proficiency** (1 paper: [GAIA: a benchmark for General AI Assistants](https://proceedings.iclr.cc/paper_files/paper/2024/file/25ae35b5b1738d80f1f03a8713e405ec-Paper-Conference.pdf))
> The general capability of an AI system to effectively select and utilize external tools, such as web browsers or code interpreters, to accomplish tasks.

**Tool utilization capability** (1 paper: [AgentVerse: Facilitating Multi-Agent Collaboration and Exploring Emergent Behaviors](https://proceedings.iclr.cc/paper_files/paper/2024/file/578e65cdee35d00c708d4c64bce32971-Paper-Conference.pdf))
> The model's latent ability to effectively select and use external tools to solve complex problems.

**Tool-use capability** (1 paper: [GTA: A Benchmark for General Tool Agents](https://proceedings.neurips.cc/paper_files/paper/2024/file/8a75ee6d4b2eb0b777f549a32a5a5c28-Paper-Datasets_and_Benchmarks_Track.pdf))
> The ability of a large language model to effectively select, invoke, and coordinate external tools to solve complex tasks.

**Tool-use ability** (1 paper: [MTU-Bench: A Multi-granularity Tool-Use Benchmark for Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/4d13b2d99519c5415661dad44ab7edcd-Paper-Conference.pdf))
> The latent capacity of an LLM to choose, call, and use external tools appropriately to satisfy user requests across dialogue settings.

**Tool Use** (1 paper: [Law of the Weakest Link: Cross Capabilities of Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/63ea6a7d01a34a2c7334dcf1a2c3b03d-Paper-Conference.pdf))
> The latent ability to interact with external tools and APIs, including functions such as web browsing, code execution, and file uploads.

**Tool-usage reasoning** (1 paper: [Multi-modal Agent Tuning: Building a VLM-Driven Agent for Efficient Tool Usage](https://proceedings.iclr.cc/paper_files/paper/2025/file/238747e153a84f50b43fd50fa8504f33-Paper-Conference.pdf))
> The latent ability to choose and sequence external tools effectively when solving multi-modal tasks.

**Tool learning** (1 paper: [Tool-Planner: Task Planning with Clusters across Multiple Tools](https://proceedings.iclr.cc/paper_files/paper/2025/file/7f605d59a0dbde101518b552cb616ddf-Paper-Conference.pdf))
> The capability of an LLM to understand and utilize external tools or APIs to solve problems that it cannot complete independently.

**Tool comprehension** (1 paper: [From Exploration to Mastery: Enabling LLMs to Master Tools via Self-Driven Interactions](https://proceedings.iclr.cc/paper_files/paper/2025/file/8c22e5e918198702765ecff4b20d0a90-Paper-Conference.pdf))
> The degree to which an LLM understands what a tool does, when to invoke it, and how to use it correctly from documentation and feedback.

**Tool-using capability** (1 paper: [From Exploration to Mastery: Enabling LLMs to Master Tools via Self-Driven Interactions](https://proceedings.iclr.cc/paper_files/paper/2025/file/8c22e5e918198702765ecff4b20d0a90-Paper-Conference.pdf))
> The latent ability of an LLM to effectively leverage external tools to solve complex real-world tasks.

**Tool manipulation** (1 paper: [Divergent Thoughts toward One Goal: LLM-based Multi-Agent Collaboration System for Electronic Design Automation](https://aclanthology.org/2025.naacl-long.83.pdf))
> The skill of interacting with and controlling external tools or APIs, typically by generating code or commands.

**Tool-calling decision-making** (1 paper: [When2Call: When (not) to Call Tools](https://aclanthology.org/2025.naacl-long.174.pdf))
> The latent ability of a model to determine whether to call a tool, ask for more information, admit inability to answer, or generate a direct response based on the availability and relevance of tools and input completeness.

**Tool-calling capability** (1 paper: [ToolFlow: Boosting LLM Tool-Calling Through Natural and Coherent Dialogue Synthesis](https://aclanthology.org/2025.naacl-long.214.pdf))
> The model's latent ability to understand user requests, select appropriate external tools, formulate correct API calls, and process their outputs.

**Flexible tool selection** (1 paper: [MeNTi: Bridging Medical Calculator and LLM Agent with Nested Tool Calling](https://aclanthology.org/2025.naacl-long.263.pdf))
> The ability to dynamically and accurately choose the most appropriate tool from a large and complex toolkit based on the specific requirements of a given task or scenario.

**Function-calling capability** (1 paper: [CONFETTI: Conversational Function-Calling Evaluation Through Turn-Level Interactions](https://aclanthology.org/2025.acl-long.394.pdf))
> The underlying ability of a large language model to generate appropriate function calls based on natural language input and a provided list of available functions.

**Tool-using ability** (1 paper: [MetaAgent: Automatically Constructing Multi-Agent Systems Based on Finite State Machines](https://raw.githubusercontent.com/mlresearch/v267/main/assets/zhang25bc/zhang25bc.pdf))
> The underlying capability of agents within a system to interact with external tools (e.g., code interpreter, search engine) to extend their functional scope and access real-world data.

**API call generation capability** (1 paper: [API Pack: A Massive Multi-Programming Language Dataset for API Call Generation](https://proceedings.iclr.cc/paper_files/paper/2025/file/63ca1cca58101545e937302be7050098-Paper-Conference.pdf))
> The model's latent ability to produce syntactically and semantically correct code snippets for invoking APIs based on natural language instructions.

**Planning with functions** (1 paper: [Facilitating Multi-turn Function Calling for LLMs via Compositional Instruction Tuning](https://proceedings.iclr.cc/paper_files/paper/2025/file/69c49f75ca31620f1f0d38093d9f3d9b-Paper-Conference.pdf))
> The cognitive capability to decompose complex tasks into manageable steps and determine the appropriate sequence of function calls required to solve them.

**Function-calling ability** (1 paper: [xLAM: A Family of Large Action Models to Empower AI Agent Systems](https://aclanthology.org/2025.naacl-long.578.pdf))
> The latent capacity of a model to correctly interpret user queries and generate valid function calls with appropriate arguments, given a set of available tools.

**Contextualised tool use** (1 paper: [TAPS: Tool-Augmented Personalisation via Structured Tagging](https://aclanthology.org/2025.emnlp-main.1200.pdf))
> The specific ability to use tools effectively by integrating information from the conversational history and user profile.

## Relationships

### Tool use ability →
- **API-Bank** (measurement instrument): *measured_by*, 2 papers
  > API-Bank (Li et al., 2023) provides a comprehensive dataset featuring 2,138 distinct APIs and 1,888 dialogues with 4,149 API calls. This dataset is designed to evaluate LLMs’ tool-utilization capabilities, including planning, retrieval, and API-calling proficiency. (Section 2)
  - [Robust Function-Calling for On-Device Language Model via Function Masking](https://proceedings.iclr.cc/paper_files/paper/2025/file/d45e0bfb5a39477d56b55c0824200008-Paper-Conference.pdf)
  - [ToolFlow: Boosting LLM Tool-Calling Through Natural and Coherent Dialogue Synthesis](https://aclanthology.org/2025.naacl-long.214.pdf)
- **Tool use** (behavioral indicator): *causes*, 2 papers
  > Tool learning enables Large Language Models (LLMs) to interact with external environments by invoking tools, serving as an effective strategy to mitigate the limitations inherent in their pre-training data. (ABSTRACT)
  - [From Exploration to Mastery: Enabling LLMs to Master Tools via Self-Driven Interactions](https://proceedings.iclr.cc/paper_files/paper/2025/file/8c22e5e918198702765ecff4b20d0a90-Paper-Conference.pdf)
  - [Learning to Ask: When LLM Agents Meet Unclear Instruction](https://aclanthology.org/2025.emnlp-main.1104.pdf)
- **GAIA** (measurement instrument): *measured_by*, 1 paper
  > GAIA proposes real-world questions that require a set of fundamental abilities such as reasoning, multi-modality handling, web browsing, and generally tool-use proficiency. (ABSTRACT)
  - [GAIA: a benchmark for General AI Assistants](https://proceedings.iclr.cc/paper_files/paper/2024/file/25ae35b5b1738d80f1f03a8713e405ec-Paper-Conference.pdf)
- **GTA** (measurement instrument): *measured_by*, 1 paper
  > Step-by-step mode is designed to evaluate the model’s fine-grained tool-use capabilities. (Section 4.1)
  - [GTA: A Benchmark for General Tool Agents](https://proceedings.neurips.cc/paper_files/paper/2024/file/8a75ee6d4b2eb0b777f549a32a5a5c28-Paper-Datasets_and_Benchmarks_Track.pdf)
- **BFCL** (measurement instrument): *measured_by*, 1 paper
  > Experiments are conducted on two representative benchmarks, including BFCL Yan et al. (2024) and API-Bank Li et al. (2023). The two benchmarks are comprehensive and executable function call evaluations specifically designed to assess the ability of LLMs to invoke functions.
  - [ToolACE: Winning the Points of LLM Function Calling](https://proceedings.iclr.cc/paper_files/paper/2025/file/663865ea167425c6c562cb0b6bcf76c7-Paper-Conference.pdf)
- **BFCL-v2** (measurement instrument): *measured_by*, 1 paper
  > We evaluated TOOLFLOW’s tool-calling ability on the BFCL. (Section 5.2.1)
  - [ToolFlow: Boosting LLM Tool-Calling Through Natural and Coherent Dialogue Synthesis](https://aclanthology.org/2025.naacl-long.214.pdf)
- **ToolAlpaca** (measurement instrument): *measured_by*, 1 paper
  > ToolAlpaca (Tang et al., 2023) establishes a multi-agent simulator. It utilizes GPT-4 (OpenAI et al., 2024) to simulate the return values of tools. The model can make modifications and re-call the tool based on the return values (e.g., error messages). Finally, GPT-4 evaluates the accuracy of Process and Response.
  - [ToolFlow: Boosting LLM Tool-Calling Through Natural and Coherent Dialogue Synthesis](https://aclanthology.org/2025.naacl-long.214.pdf)
- **ToolEval** (measurement instrument): *measured_by*, 1 paper
  > “To assess the tool-use capabilities of LLMs, we develop an automatic evaluator, ToolEval” and “We first present ToolBench, an instruction-tuning dataset for tool use”
  - [ToolLLM: Facilitating Large Language Models to Master 16000+ Real-world APIs](https://proceedings.iclr.cc/paper_files/paper/2024/file/28e50ee5b72e90b50e7196fde8ea260e-Paper-Conference.pdf)

### → Tool use ability
- **Irrelevance detection ability** (construct): *correlates*, 1 paper
  > we identified a concerning inverse relationship between the model's ability to accurately execute function calls and its capacity for irrelevance detection
  - [Robust Function-Calling for On-Device Language Model via Function Masking](https://proceedings.iclr.cc/paper_files/paper/2025/file/d45e0bfb5a39477d56b55c0824200008-Paper-Conference.pdf)
- **Instruction following ability** (construct): *causes*, 1 paper
  > Llama3.1-70B-Instruct outperforms Llama3.1-8B-Instruct with EASYTOOL, indicating that models with better instruction-following capabilities can achieve greater improvements with high-quality tool instructions. (Section 5.1)
  - [EASYTOOL: Enhancing LLM-based Agents with Concise Tool Instruction](https://aclanthology.org/2025.naacl-long.44.pdf)

### Associated with
- **Reasoning** (construct), 1 paper
  > LLMs must first comprehend the user’s query and perform a reasonable analysis and planning, demonstrating the ability of reasoning. Subsequently, it needs to invoke the correct functions with suitable parameters, reflecting the ability of execution.
  - [MoRAgent: Parameter Efficient Agent Tuning with Mixture-of-Roles](https://raw.githubusercontent.com/mlresearch/v267/main/assets/han25j/han25j.pdf)
