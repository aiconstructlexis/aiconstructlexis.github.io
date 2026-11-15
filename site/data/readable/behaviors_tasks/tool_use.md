# Tool use
**Type:** Behavioral indicator  
**Supporting papers:** 164  
**Also known as:** Tool calling, Tool usage, Tool invocation, Tool-integrated reasoning, Function calling, API call generation, Tool execution, API selection, Multi-step tool calling, API chaining, Multi-API calling, Single-API calling, Dependent function calling, Parallel function calling, Tool usage updating, Code generation and execution, API interaction, Remote server interaction, API call selection, API calling, Function Calling, Nested tool calling, Parameter selection, Function selection, Tool selection, Tool interaction, Tool utilization, Tool application, API function calling, API call execution, Function invocation  

## State of the Field

**Space of definitions.** Across papers, the prevailing usage treats tool use as an observable behavior in which a model selects and invokes external tools, APIs, functions, or other systems to solve a sub-problem or complete a user request. Most definitions make success depend on choosing the appropriate tool and supplying the right arguments or parameters, often by generating a structured request such as JSON, an API call, or Python code; some also include executing the call and using returned feedback or tool-provided content in later reasoning and answer formation. A smaller line of work frames it more broadly as a latent ability to know when a tool is needed, use it effectively, and interpret outputs. As one paper puts it, the model may access tools by generating tool calls as code that conforms to the API specification (When2Call: When (not) to Call Tools).

**Variants.** Papers use several near-neighbor names, especially function calling, tool calling, tool invocation, tool usage, and API call generation or interaction. The most common variants split by call structure: single-API versus multi-API use, dependent or chained calls where one output feeds the next, parallel calls, multi-step sequences, and nested calling; another recurring variant is tool-integrated reasoning, where natural-language reasoning is interleaved with code generation and execution, often in Python. Finer-grained formulations isolate tool selection and parameter selection, and papers also study specialized settings such as multi-modal API selection, remote server interaction, OS or image-restoration tools, and domain-specific tools in geospatial, legal, clinical, financial, CRM, and IT automation tasks. One paper describes nested tool calling as introducing additional tools when current tools or information are insufficient (MeNTi: Bridging Medical Calculator and LLM Agent with Nested Tool Calling).

**Space of elicitation and scores.** Papers measure this behavior with 14 instruments. The most frequent are BFCL, ToolBench, API-Bank, BigCodeBench, and GAIA. Together these instruments cover function-calling benchmarks, multi-turn tool-use environments, code-generation benchmarks with diverse function calls, and real-world tool-use settings; some papers also use judge-based scoring when outputs have no fixed ground truth.

**What it is taken as evidence of.** Papers connect tool use to 7 constructs, and the mapping is not uniform. The most recurrent construct links are causal claims involving planning and reasoning: papers claim causal relationships from planning, reasoning, tool use ability, and instruction following ability to tool use, while other papers claim causal relationships from tool use to reasoning and to mathematical reasoning. Grounding and multi-hop reasoning are reported as related rather than causal, so papers do not converge on a single construct that tool use is taken to reflect.

## Sources

**Tool use** (14 papers: [RL-GPT: Integrating Reinforcement Learning and Code-as-policy](https://proceedings.neurips.cc/paper_files/paper/2024/file/31f119089f702e48ecfd138c1bc82c4a-Paper-Conference.pdf), [Re-Aligning Language to Visual Objects with an Agentic Workflow](https://proceedings.iclr.cc/paper_files/paper/2025/file/0d9057d84a9fc37523bf826232ea6820-Paper-Conference.pdf), [APPL: A Prompt Programming Language for Harmonious Integration of Programs and Large Language Model Prompts](https://aclanthology.org/2025.acl-long.63.pdf), [Tool Unlearning for Tool-Augmented LLMs](https://raw.githubusercontent.com/mlresearch/v267/main/assets/cheng25a/cheng25a.pdf), [PAFT: Prompt-Agnostic Fine-Tuning](https://aclanthology.org/2025.emnlp-main.37.pdf), [AgentVerse: Facilitating Multi-Agent Collaboration and Exploring Emergent Behaviors](https://proceedings.iclr.cc/paper_files/paper/2024/file/578e65cdee35d00c708d4c64bce32971-Paper-Conference.pdf), [Amortizing intractable inference in large language models](https://proceedings.iclr.cc/paper_files/paper/2024/file/bc667ac84ef58f2b5022da97a465cbab-Paper-Conference.pdf), [Identifying the Risks of LM Agents with an LM-Emulated Sandbox](https://proceedings.iclr.cc/paper_files/paper/2024/file/7274ed909a312d4d869cc328ad1c5f04-Paper-Conference.pdf), [MAmmoTH: Building Math Generalist Models through Hybrid Instruction Tuning](https://proceedings.iclr.cc/paper_files/paper/2024/file/b063829b922fdeb4fa3472dd3471ff43-Paper-Conference.pdf), [MINT: Evaluating LLMs in Multi-turn Interaction with Tools and Language Feedback](https://proceedings.iclr.cc/paper_files/paper/2024/file/8a0d3ae989a382ce6e50312bc35bf7e1-Paper-Conference.pdf), [ToRA: A Tool-Integrated Reasoning Agent for Mathematical Problem Solving](https://proceedings.iclr.cc/paper_files/paper/2024/file/d3cf1559a8795eb1ed2b3ad52409ac7d-Paper-Conference.pdf), [IHEval: Evaluating Language Models on Following the Instruction Hierarchy](https://aclanthology.org/2025.naacl-long.425.pdf), [Prompt Compression for Large Language Models: A Survey](https://aclanthology.org/2025.naacl-long.368.pdf), [Smurfs: Multi-Agent System using Context-Efficient DFSDT for Tool Planning](https://aclanthology.org/2025.naacl-long.169.pdf))
> The behavior of invoking and utilizing an external capability or system, such as an RL training pipeline, to solve a sub-problem.

**Tool calling** (4 papers: [Advancing Tool-Augmented Large Language Models: Integrating Insights from Errors in Inference Trees](https://proceedings.neurips.cc/paper_files/paper/2024/file/c0f7ee1901fef1da4dae2b88dfd43195-Paper-Conference.pdf), [Param$\Delta$ for Direct Mixing: Post-Train Large Language Model At Zero Cost](https://proceedings.iclr.cc/paper_files/paper/2025/file/78bca5cc621a0846cb1f8265e1927a2a-Paper-Conference.pdf), [PORTS: Preference-Optimized Retrievers for Tool Selection with Large Language Models](https://aclanthology.org/2025.emnlp-main.507.pdf), [Improving Retrospective Language Agents via Joint Policy Gradient Optimization](https://aclanthology.org/2025.naacl-long.6.pdf))
> The observable action of executing a chosen tool with specific parameters, typically by generating a formatted API request.

**Tool usage** (2 papers: [Unlocking the Capabilities of Thought: A Reasoning Boundary Framework to Quantify and Optimize Chain-of-Thought](https://proceedings.neurips.cc/paper_files/paper/2024/file/62ab1c2cb4b03e717005479efb211841-Paper-Conference.pdf), [Multi-modal Agent Tuning: Building a VLM-Driven Agent for Efficient Tool Usage](https://proceedings.iclr.cc/paper_files/paper/2025/file/238747e153a84f50b43fd50fa8504f33-Paper-Conference.pdf))
> Using external tools during reasoning to perform computations or other operations.

**Tool invocation** (9 papers: [UrbanKGent: A Unified Large Language Model Agent Framework for Urban Knowledge Graph Construction](https://proceedings.neurips.cc/paper_files/paper/2024/file/decd42d78c42cea59c95c7c3d40d5e0f-Paper-Conference.pdf), [Tool-Planner: Task Planning with Clusters across Multiple Tools](https://proceedings.iclr.cc/paper_files/paper/2025/file/7f605d59a0dbde101518b552cb616ddf-Paper-Conference.pdf), [IPIGuard: A Novel Tool Dependency Graph-Based Defense Against Indirect Prompt Injection in LLM Agents](https://aclanthology.org/2025.emnlp-main.53.pdf), [AGrail: A Lifelong Agent Guardrail with Effective and Adaptive Safety Detection](https://aclanthology.org/2025.acl-long.399.pdf), [LegalAgentBench: Evaluating LLM Agents in Legal Domain](https://aclanthology.org/2025.acl-long.116.pdf), [ReflecTool: Towards Reflection-Aware Tool-Augmented Clinical Agents](https://aclanthology.org/2025.acl-long.663.pdf), [ToolHop: A Query-Driven Benchmark for Evaluating Large Language Models in Multi-Hop Tool Use](https://aclanthology.org/2025.acl-long.150.pdf), [ITBench: Evaluating AI Agents across Diverse Real-World IT Automation Tasks](https://raw.githubusercontent.com/mlresearch/v267/main/assets/jha25a/jha25a.pdf), [Reducing Tool Hallucination via Reliability Alignment](https://raw.githubusercontent.com/mlresearch/v267/main/assets/xu25ap/xu25ap.pdf))
> The action of calling external, specialized functions, such as a distance calculator or geohash encoder, to obtain information needed for a reasoning process.

**Tool-integrated reasoning** (3 papers: [Not All Tokens Are What You Need for Pretraining](https://proceedings.neurips.cc/paper_files/paper/2024/file/3322a9a72a1707de14badd5e552ff466-Paper-Conference.pdf), [MathCoder2: Better Math Reasoning from Continued Pretraining on Model-translated Mathematical Code](https://proceedings.iclr.cc/paper_files/paper/2025/file/bea94fe9c5573e74294657f692069d89-Paper-Conference.pdf), [Position: Formal Mathematical Reasoning—A New Frontier in AI](https://raw.githubusercontent.com/mlresearch/v267/main/assets/yang25az/yang25az.pdf))
> The behavior of solving problems by generating and executing code or using other external tools as part of the reasoning process.

**Function calling** (5 papers: [Compact Language Models via Pruning and Knowledge Distillation](https://proceedings.neurips.cc/paper_files/paper/2024/file/4822991365c962105b1b95b1107d30e5-Paper-Conference.pdf), [{$\tau$}-bench: A Benchmark for \underline{T}ool-\underline{A}gent-\underline{U}ser Interaction in Real-World Domains](https://proceedings.iclr.cc/paper_files/paper/2025/file/1b126cc38b8638e07bef37e7b2bb72bf-Paper-Conference.pdf), [Can Compressed LLMs Truly Act? An Empirical Evaluation of Agentic Capabilities in LLM Compression](https://raw.githubusercontent.com/mlresearch/v267/main/assets/dong25k/dong25k.pdf), [MCIP: Protecting MCP Safety via Model Contextual Integrity Protocol](https://aclanthology.org/2025.emnlp-main.62.pdf), [Large Language Models as Tool Makers](https://proceedings.iclr.cc/paper_files/paper/2024/file/ed91353f700d113e5d848c7e04a858b0-Paper-Conference.pdf))
> The task of identifying when to use external tools or APIs based on a user's request and generating the correct function calls with appropriate arguments.

**API call generation** (2 papers: [Gorilla: Large Language Model Connected with Massive APIs](https://proceedings.neurips.cc/paper_files/paper/2024/file/e4c61f578ff07830f5c37378dd3ecb0d-Paper-Conference.pdf), [Grammar Pruning: Enabling Low-Latency Zero-Shot Task-Oriented Language Models for Edge AI](https://aclanthology.org/2025.emnlp-main.858.pdf))
> The task of producing a syntactically and semantically correct API call based on a natural language instruction.

**API selection** (1 paper: [ToolACE: Winning the Points of LLM Function Calling](https://proceedings.iclr.cc/paper_files/paper/2025/file/663865ea167425c6c562cb0b6bcf76c7-Paper-Conference.pdf))
> Choosing the appropriate API from a candidate tool list for a user request.

**Tool execution** (1 paper: [An Intelligent Agentic System for Complex Image Restoration Problems](https://proceedings.iclr.cc/paper_files/paper/2025/file/921ac785fa9edc73cacaf2664f43d234-Paper-Conference.pdf))
> Sequentially applying specific IR models or tools to the image according to the planned operations.

**API chaining** (1 paper: [ToolDial: Multi-turn Dialogue Generation Method for Tool-Augmented Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/afb27164624b641e8fbba961b2301acf-Paper-Conference.pdf))
> The observable behavior of calling multiple APIs in sequence where one API's output serves as another's input.

**Multi-step tool calling** (1 paper: [AgentHarm: A Benchmark for Measuring Harmfulness of LLM Agents](https://proceedings.iclr.cc/paper_files/paper/2025/file/c493d23af93118975cdbc32cbe7323f5-Paper-Conference.pdf))
> Executing several tool calls in sequence, often with dependencies between calls, to satisfy a request.

**Single-API calling** (1 paper: [Understanding the Generalization of In-Context Learning in Transformers: An Empirical Study](https://proceedings.iclr.cc/paper_files/paper/2025/file/bd19ca8039547b339a6a37bd4df24405-Paper-Conference.pdf))
> A specific tool-calling task that requires only a single API invocation to fulfill the user's instruction.

**Multi-API calling** (1 paper: [Understanding the Generalization of In-Context Learning in Transformers: An Empirical Study](https://proceedings.iclr.cc/paper_files/paper/2025/file/bd19ca8039547b339a6a37bd4df24405-Paper-Conference.pdf))
> A complex tool-calling task that requires the combined use of multiple API invocations to achieve a desired functionality.

**Dependent function calling** (1 paper: [ToolACE: Winning the Points of LLM Function Calling](https://proceedings.iclr.cc/paper_files/paper/2025/file/663865ea167425c6c562cb0b6bcf76c7-Paper-Conference.pdf))
> A specific type of function calling where the model makes a sequence of API calls, where the output of one call is used as the input for a subsequent call.

**Parallel function calling** (2 papers: [ToolACE: Winning the Points of LLM Function Calling](https://proceedings.iclr.cc/paper_files/paper/2025/file/663865ea167425c6c562cb0b6bcf76c7-Paper-Conference.pdf), [NESTFUL: A Benchmark for Evaluating LLMs on Nested Sequences of API Calls](https://aclanthology.org/2025.emnlp-main.1702.pdf))
> A specific type of function calling where the model makes multiple, independent API calls simultaneously to fulfill a user request.

**Tool usage updating** (1 paper: [Learning Evolving Tools for Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/d8d1d325f822e07d16866780cc23deb2-Paper-Conference.pdf))
> The observable process of a model summarizing the usage of a new or changed tool and incorporating that new definition into its available tool set, often within the prompt context.

**Code generation and execution** (1 paper: [Agentic Reasoning: A Streamlined Framework for Enhancing LLM Reasoning with Agentic Tools](https://aclanthology.org/2025.acl-long.1383.pdf))
> The behavior of writing and running code to perform computations or other programmatic tasks as part of a larger problem-solving process.

**Remote server interaction** (1 paper: [EnIGMA: Interactive Tools Substantially Assist LM Agents in Finding Security Vulnerabilities](https://raw.githubusercontent.com/mlresearch/v267/main/assets/abramovich25a/abramovich25a.pdf))
> The observable action of an agent using a tool to initiate, maintain, and terminate connections with an external server to send and receive data.

**API interaction** (1 paper: [MapEval: A Map-Based Evaluation of Geo-Spatial Reasoning in Foundation Models](https://raw.githubusercontent.com/mlresearch/v267/main/assets/dihan25a/dihan25a.pdf))
> Generating valid API queries, processing structured responses, and using the retrieved data to support reasoning and answer formulation.

**API call selection** (1 paper: [CIFLEX: Contextual Instruction Flow for Sub-task Execution in Multi-Turn Interactions with a Single On-Device LLM](https://aclanthology.org/2025.emnlp-main.533.pdf))
> Selecting and generating the appropriate API invocation based on a multi-modal user query, such as one involving an image reference.

**API calling** (1 paper: [Learning to Ask: When LLM Agents Meet Unclear Instruction](https://aclanthology.org/2025.emnlp-main.1104.pdf))
> The model generates function calls with arguments to invoke external tools in response to a user request.

**Function Calling** (1 paper: [CRMArena: Understanding the Capacity of LLM Agents to Perform Professional CRM Tasks in Realistic Environments](https://aclanthology.org/2025.naacl-long.194.pdf))
> An agentic evaluation setup in which the model interacts with the environment through Python wrapper functions that call CRM APIs.

**Nested tool calling** (1 paper: [MeNTi: Bridging Medical Calculator and LLM Agent with Nested Tool Calling](https://aclanthology.org/2025.naacl-long.263.pdf))
> The ability to recursively invoke additional tools during task execution when initial tools or information are insufficient, enabling resolution of complex dependencies such as unit mismatches or missing parameters.

**Parameter selection** (1 paper: [MTU-Bench: A Multi-granularity Tool-Use Benchmark for Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/4d13b2d99519c5415661dad44ab7edcd-Paper-Conference.pdf))
> The observable action of identifying and providing the correct arguments or parameters for a selected tool call.

**Function selection** (1 paper: [Robust Function-Calling for On-Device Language Model via Function Masking](https://proceedings.iclr.cc/paper_files/paper/2025/file/d45e0bfb5a39477d56b55c0824200008-Paper-Conference.pdf))
> Choosing the correct function from a set of candidate functions given a user intent and function descriptions.

**Tool selection** (5 papers: [TaskBench: Benchmarking Large Language Models for Task Automation](https://proceedings.neurips.cc/paper_files/paper/2024/file/085185ea97db31ae6dcac7497616fd3e-Paper-Datasets_and_Benchmarks_Track.pdf), [MTU-Bench: A Multi-granularity Tool-Use Benchmark for Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/4d13b2d99519c5415661dad44ab7edcd-Paper-Conference.pdf), [Prune ’n Predict: Optimizing LLM Decision-making with Conformal Prediction](https://raw.githubusercontent.com/mlresearch/v267/main/assets/vishwakarma25b/vishwakarma25b.pdf), [PlanningArena: A Modular Benchmark for Multidimensional Evaluation of Planning and Tool Learning](https://aclanthology.org/2025.acl-long.1499.pdf), [EASYTOOL: Enhancing LLM-based Agents with Concise Tool Instruction](https://aclanthology.org/2025.naacl-long.44.pdf))
> Choosing the appropriate tools for each subtask and representing their dependencies as a tool invocation graph.

**Tool interaction** (1 paper: [CRITIC: Large Language Models Can Self-Correct with Tool-Interactive Critiquing](https://proceedings.iclr.cc/paper_files/paper/2024/file/fef126561bbf9d4467dbb8d27334b8fe-Paper-Conference.pdf))
> The observable behavior of generating queries to and processing responses from external tools such as search engines or interpreters.

**Tool utilization** (2 papers: [ACT: Knowledgeable Agents to Design and Perform Complex Tasks](https://aclanthology.org/2025.acl-long.823.pdf), [Towards Rationality in Language and Multimodal Agents: A Survey](https://aclanthology.org/2025.naacl-long.186.pdf))
> The observable process of an LLM-based agent interacting with and using external tools to accomplish a task.

**Tool application** (2 papers: [Enhancing Open-Domain Task-Solving Capability of LLMs via Autonomous Tool Integration from GitHub](https://aclanthology.org/2025.acl-long.845.pdf), [FinEval: A Chinese Financial Domain Knowledge Evaluation Benchmark for Large Language Models](https://aclanthology.org/2025.naacl-long.318.pdf))
> Using external tools such as APIs to retrieve financial data or perform computations as part of solving a financial task, demonstrated through step-by-step operational descriptions.

**API function calling** (1 paper: [Hephaestus: Improving Fundamental Agent Capabilities of Large Language Models through Continual Pre-Training](https://aclanthology.org/2025.naacl-long.308.pdf))
> The observable action of generating a syntactically correct and semantically appropriate API function call, including function names and parameters, in response to a task description.

**API call execution** (1 paper: [AXIS: Efficient Human-Agent-Computer Interaction with API-First LLM-Based Agents](https://aclanthology.org/2025.acl-long.381.pdf))
> The model performs direct function calls to application programming interfaces to modify content or state, bypassing UI interactions.

**Function invocation** (1 paper: [The Berkeley Function Calling Leaderboard (BFCL): From Tool Use to Agentic Evaluation of Large Language Models](https://raw.githubusercontent.com/mlresearch/v267/main/assets/patil25a/patil25a.pdf))
> The observable act of generating a syntactically correct call to an external function or API with appropriate parameters.

## Relationships

### Tool use →
- **ToolBench** (measurement instrument): *measured_by*, 5 papers
  > The ability to use external tools is a significant milestone in the development of LLMs... For this purpose, we utilize the large-scale tool usage dataset ToolBench [21]... (Section 3.2)
  - [StreamBench: Towards Benchmarking Continuous Improvement of Language Agents](https://proceedings.neurips.cc/paper_files/paper/2024/file/c189915371c4474fe9789be3728113fc-Paper-Datasets_and_Benchmarks_Track.pdf)
  - [Understanding the Generalization of In-Context Learning in Transformers: An Empirical Study](https://proceedings.iclr.cc/paper_files/paper/2025/file/bd19ca8039547b339a6a37bd4df24405-Paper-Conference.pdf)
  - [xLAM: A Family of Large Action Models to Empower AI Agent Systems](https://aclanthology.org/2025.naacl-long.578.pdf)
  - [PORTS: Preference-Optimized Retrievers for Tool Selection with Large Language Models](https://aclanthology.org/2025.emnlp-main.507.pdf)
  - [ToolChain*: Efficient Action Space Navigation in Large Language Models with A* Search](https://proceedings.iclr.cc/paper_files/paper/2024/file/13250eb13871b3c2c0a0667b54bad165-Paper-Conference.pdf)
- **BFCL** (measurement instrument): *measured_by*, 5 papers
  > function calling (BFCL)
  - [Compact Language Models via Pruning and Knowledge Distillation](https://proceedings.neurips.cc/paper_files/paper/2024/file/4822991365c962105b1b95b1107d30e5-Paper-Conference.pdf)
  - [Param$\Delta$ for Direct Mixing: Post-Train Large Language Model At Zero Cost](https://proceedings.iclr.cc/paper_files/paper/2025/file/78bca5cc621a0846cb1f8265e1927a2a-Paper-Conference.pdf)
  - [When2Call: When (not) to Call Tools](https://aclanthology.org/2025.naacl-long.174.pdf)
  - [MoRAgent: Parameter Efficient Agent Tuning with Mixture-of-Roles](https://raw.githubusercontent.com/mlresearch/v267/main/assets/han25j/han25j.pdf)
  - [The Berkeley Function Calling Leaderboard (BFCL): From Tool Use to Agentic Evaluation of Large Language Models](https://raw.githubusercontent.com/mlresearch/v267/main/assets/patil25a/patil25a.pdf)
- **Hallucination** (behavioral indicator): *causes*, 3 papers
  > Recent studies have shown that LLMs can mitigate hallucination by accessing general-purpose tools (Schick et al., 2023; Tang et al., 2023; Patil et al., 2023; Qin et al., 2023; Wang et al., 2024b). (Section 1)
  - [Adapting While Learning: Grounding LLMs for Scientific Problems with Tool Usage Adaptation](https://raw.githubusercontent.com/mlresearch/v267/main/assets/lyu25a/lyu25a.pdf)
  - [Reducing Tool Hallucination via Reliability Alignment](https://raw.githubusercontent.com/mlresearch/v267/main/assets/xu25ap/xu25ap.pdf)
  - [SCRIBE: Structured Chain Reasoning for Interactive Behaviour Explanations using Tool Calling](https://aclanthology.org/2025.emnlp-main.1490.pdf)
- **GAIA** (measurement instrument): *measured_by*, 2 papers
  > We evaluate MaAS on six public benchmarks covering three domains: ... and (3) tool use, GAIA (Mialon et al., 2023) (Section 4.1).
  - [Multi-agent Architecture Search via Agentic Supernet](https://raw.githubusercontent.com/mlresearch/v267/main/assets/zhang25bi/zhang25bi.pdf)
  - [Compound AI Systems Optimization: A Survey of Methods, Challenges, and Future Directions](https://aclanthology.org/2025.emnlp-main.1463.pdf)
- **API-Bank** (measurement instrument): *measured_by*, 2 papers
  > In particular, when looking at the tool use evaluation sets (BFCL and API Bank), it is evident that the ability to use tools can be acquired effectively by adding ∆Θ to the base model...
  - [Param$\Delta$ for Direct Mixing: Post-Train Large Language Model At Zero Cost](https://proceedings.iclr.cc/paper_files/paper/2025/file/78bca5cc621a0846cb1f8265e1927a2a-Paper-Conference.pdf)
  - [PORTS: Preference-Optimized Retrievers for Tool Selection with Large Language Models](https://aclanthology.org/2025.emnlp-main.507.pdf)
- **BigCodeBench** (measurement instrument): *measured_by*, 2 papers
  > We introduce BigCodeBench, a new high-quality programming benchmark constructed via the collaboration between human experts and LLMs, assessing the capability of tool use and complex instruction following. (Section 6)
  - [BigCodeBench: Benchmarking Code Generation with Diverse Function Calls and Complex Instructions](https://proceedings.iclr.cc/paper_files/paper/2025/file/a6a90bcc2aa470c3871b2d39a67d26e8-Paper-Conference.pdf)
  - [Selective Prompt Anchoring for Code Generation](https://raw.githubusercontent.com/mlresearch/v267/main/assets/tian25a/tian25a.pdf)
- **LLM-as-a-judge** (measurement instrument): *measured_by*, 2 papers
  > Win Rate (Win%), which evaluates effectiveness through pairwise comparisons by a ChatGPT-based evaluator, capturing nuanced performance differences not reflected by rule-based metrics. (Section 3.1)
  - [From Exploration to Mastery: Enabling LLMs to Master Tools via Self-Driven Interactions](https://proceedings.iclr.cc/paper_files/paper/2025/file/8c22e5e918198702765ecff4b20d0a90-Paper-Conference.pdf)
  - [CIFLEX: Contextual Instruction Flow for Sub-task Execution in Multi-Turn Interactions with a Single On-Device LLM](https://aclanthology.org/2025.emnlp-main.533.pdf)
- **Reasoning** (construct): *causes*, 2 papers
  > Teaching large language models (LLMs) to use tools for solving complex problems can grant them human-like reasoning abilities. (Abstract)
  - [Smurfs: Multi-Agent System using Context-Efficient DFSDT for Tool Planning](https://aclanthology.org/2025.naacl-long.169.pdf)
  - [Multi-modal Agent Tuning: Building a VLM-Driven Agent for Efficient Tool Usage](https://proceedings.iclr.cc/paper_files/paper/2025/file/238747e153a84f50b43fd50fa8504f33-Paper-Conference.pdf)
- **HotpotQA** (measurement instrument): *measured_by*, 1 paper
  > HotPotQA [49] features natural, multi-hop questions, which challenge an agent’s ability to perform reasoning and utilize search tools.
  - [AGILE: A Novel Reinforcement Learning Framework of LLM Agents](https://proceedings.neurips.cc/paper_files/paper/2024/file/097c514162ea7126d40671d23e12f51b-Paper-Conference.pdf)
- **Complex reasoning question answering** (behavioral indicator): *causes*, 1 paper
  > These tools enable agents to perform complex tasks like multi-step problem-solving and retrieving diverse information, which is essential for complex retrieval and question-answering (QA) (Section 1).
  - [AvaTaR: Optimizing LLM Agents for Tool Usage via Contrastive Reasoning](https://proceedings.neurips.cc/paper_files/paper/2024/file/2db8ce969b000fe0b3fb172490c33ce8-Paper-Conference.pdf)
- **Mathematical reasoning** (construct): *causes*, 1 paper
  > They utilize integrated natural language reasoning steps and Python code to improve performance on mathematical reasoning tasks. (Section 1)
  - [MathCoder2: Better Math Reasoning from Continued Pretraining on Model-translated Mathematical Code](https://proceedings.iclr.cc/paper_files/paper/2025/file/bea94fe9c5573e74294657f692069d89-Paper-Conference.pdf)
- **ToolQA** (measurement instrument): *measured_by*, 1 paper
  > ToolQA (Zhuang et al., 2024) evaluates agents’ abilities to use external tools. (§4.2.1)
  - [OpenHands: An Open Platform for AI Software Developers as Generalist Agents](https://proceedings.iclr.cc/paper_files/paper/2025/file/a4b6ad6b48850c0c331d1259fc66a69c-Paper-Conference.pdf)
- **GPQA** (measurement instrument): *measured_by*, 1 paper
  > GPQA (Rein et al., 2023) evaluates agents’ ability for coordinated tool use when solving challenging graduate-level problems. (§4.4)
  - [OpenHands: An Open Platform for AI Software Developers as Generalist Agents](https://proceedings.iclr.cc/paper_files/paper/2025/file/a4b6ad6b48850c0c331d1259fc66a69c-Paper-Conference.pdf)
- **StableToolBench** (measurement instrument): *measured_by*, 1 paper
  > By comparing the accuracy of function calls with ToolLlama (Qin et al., 2024) and two one-shot baselines (Qwen-2-72B and GPT-4) on StableToolBench, we find that the above procedure is effective (shown in Figure 5). (Section 4.1)
  - [Benchmarking Agentic Workflow Generation](https://proceedings.iclr.cc/paper_files/paper/2025/file/adbe936993aa7cf41e45054d8b72f183-Paper-Conference.pdf)
- **Unit conversion** (behavioral indicator): *causes*, 1 paper
  > If MeNTi detects a mismatch in parameter units, it employs the nested tool calling mechanism to identify the need for additional tools. This mechanism enables iterative tool selection and utilization to resolve unit mismatches caused by complex toolchains requiring multiple tools. (Section 3.1)
  - [MeNTi: Bridging Medical Calculator and LLM Agent with Nested Tool Calling](https://aclanthology.org/2025.naacl-long.263.pdf)
- **ToolAlpaca** (measurement instrument): *measured_by*, 1 paper
  > ToolAlpaca contains 3.9k tool-use instances from a multi-agent simulation environment, which we augment to a MCQ format. (Section 4.1)
  - [Prune ’n Predict: Optimizing LLM Decision-making with Conformal Prediction](https://raw.githubusercontent.com/mlresearch/v267/main/assets/vishwakarma25b/vishwakarma25b.pdf)
- **MMAU** (measurement instrument): *measured_by*, 1 paper
  > We evaluate the tool use performance on MMAU (Yin et al., 2024) and report the performance on Tool Execution and Tool Planning.
  - [Instruction-Following Pruning for Large Language Models](https://raw.githubusercontent.com/mlresearch/v267/main/assets/hou25b/hou25b.pdf)
- **APIBench** (measurement instrument): *measured_by*, 1 paper
  > “We evaluate PORTS on six popular tool-augmented datasets: ToolBench (Qin et al., 2024), API-Bank (Li et al., 2023), APIBench (Peng et al., 2023), BFCL-v2 (Yan et al., 2024), ToolE (Huang et al., 2024), Octopus-v2 (Chen and Li, 2024).”
  - [PORTS: Preference-Optimized Retrievers for Tool Selection with Large Language Models](https://aclanthology.org/2025.emnlp-main.507.pdf)
- **BFCL-v2** (measurement instrument): *measured_by*, 1 paper
  > “We evaluate PORTS on six popular tool-augmented datasets: ToolBench (Qin et al., 2024), API-Bank (Li et al., 2023), APIBench (Peng et al., 2023), BFCL-v2 (Yan et al., 2024), ToolE (Huang et al., 2024), Octopus-v2 (Chen and Li, 2024).”
  - [PORTS: Preference-Optimized Retrievers for Tool Selection with Large Language Models](https://aclanthology.org/2025.emnlp-main.507.pdf)

### → Tool use
- **Planning** (construct): *causes*, 3 papers
  > After the planning step, our agent takes action to construct adaptive VL prompts for the tool models (i.e., VLM/LLM). (Section 1)
  - [Re-Aligning Language to Visual Objects with an Agentic Workflow](https://proceedings.iclr.cc/paper_files/paper/2025/file/0d9057d84a9fc37523bf826232ea6820-Paper-Conference.pdf)
  - [ShortcutsBench: A Large-Scale Real-world Benchmark for API-based Agents](https://proceedings.iclr.cc/paper_files/paper/2025/file/c16a99558b0b4f6b10966ca9bdb98ade-Paper-Conference.pdf)
  - [TC–RAG: Turing–Complete RAG's Case study on Medical LLM Systems](https://aclanthology.org/2025.acl-long.558.pdf)
- **Tool use ability** (construct): *causes*, 2 papers
  > Tool learning enables Large Language Models (LLMs) to interact with external environments by invoking tools, serving as an effective strategy to mitigate the limitations inherent in their pre-training data. (ABSTRACT)
  - [From Exploration to Mastery: Enabling LLMs to Master Tools via Self-Driven Interactions](https://proceedings.iclr.cc/paper_files/paper/2025/file/8c22e5e918198702765ecff4b20d0a90-Paper-Conference.pdf)
  - [Learning to Ask: When LLM Agents Meet Unclear Instruction](https://aclanthology.org/2025.emnlp-main.1104.pdf)
- **Reasoning** (construct): *causes*, 2 papers
  > The LLM must use reasoning to deduce the suitable tools to address the given tasks. (Section 1)
  - [GTA: A Benchmark for General Tool Agents](https://proceedings.neurips.cc/paper_files/paper/2024/file/8a75ee6d4b2eb0b777f549a32a5a5c28-Paper-Datasets_and_Benchmarks_Track.pdf)
  - [Multi-modal Agent Tuning: Building a VLM-Driven Agent for Efficient Tool Usage](https://proceedings.iclr.cc/paper_files/paper/2025/file/238747e153a84f50b43fd50fa8504f33-Paper-Conference.pdf)
- **Information retrieval** (behavioral indicator): *causes*, 2 papers
  > Recently, the focus has shifted towards the use of retrievers to effectively support LLMs in the tool selection process (Section 1).
  - [PORTS: Preference-Optimized Retrievers for Tool Selection with Large Language Models](https://aclanthology.org/2025.emnlp-main.507.pdf)
  - [EASYTOOL: Enhancing LLM-based Agents with Concise Tool Instruction](https://aclanthology.org/2025.naacl-long.44.pdf)
- **Instruction following ability** (construct): *causes*, 1 paper
  > lacks sufficient instruction-following ability to invoke tools in a correct format. (Section 4.3)
  - [GTA: A Benchmark for General Tool Agents](https://proceedings.neurips.cc/paper_files/paper/2024/file/8a75ee6d4b2eb0b777f549a32a5a5c28-Paper-Datasets_and_Benchmarks_Track.pdf)
- **Task decomposition** (behavioral indicator): *causes*, 1 paper
  > Through its task decomposition mechanism, Smurfs transforms long-context tasks into simpler ones, enabling the untrained model to effectively utilize external tools for managing complex tasks. (Section 4.1)
  - [Smurfs: Multi-Agent System using Context-Efficient DFSDT for Tool Planning](https://aclanthology.org/2025.naacl-long.169.pdf)

### Associated with
- **Action selection** (behavioral indicator), 2 papers
  > “Actions involve selecting which tool to call and the input to that tool.”
  - [NAT: Enhancing Agent Tuning with Negative Samples](https://aclanthology.org/2025.naacl-long.378.pdf)
  - [Prune ’n Predict: Optimizing LLM Decision-making with Conformal Prediction](https://raw.githubusercontent.com/mlresearch/v267/main/assets/vishwakarma25b/vishwakarma25b.pdf)
- **Code generation** (behavioral indicator), 1 paper
  > The actor then generates revised actions, which could include a combination of tool usage through programming language (code generation) along with natural language explanations of how the tools are employed. (Section 4.1).
  - [AvaTaR: Optimizing LLM Agents for Tool Usage via Contrastive Reasoning](https://proceedings.neurips.cc/paper_files/paper/2024/file/2db8ce969b000fe0b3fb172490c33ce8-Paper-Conference.pdf)
- **Explanation generation** (behavioral indicator), 1 paper
  > our proposed Tool-integrated Reasoning format interleaves rationales with program-based tool use. (Figure 2)
  - [ToRA: A Tool-Integrated Reasoning Agent for Mathematical Problem Solving](https://proceedings.iclr.cc/paper_files/paper/2024/file/d3cf1559a8795eb1ed2b3ad52409ac7d-Paper-Conference.pdf)
- **Chain of thought** (behavioral indicator), 1 paper
  > we opt for the framework of the ReAct agent that performs step-by-step reasoning for tool usage... In each step, the agent generates thought and corresponding code to execute tools.
  - [Multi-modal Agent Tuning: Building a VLM-Driven Agent for Efficient Tool Usage](https://proceedings.iclr.cc/paper_files/paper/2025/file/238747e153a84f50b43fd50fa8504f33-Paper-Conference.pdf)
- **Grounding** (construct), 1 paper
  > This requires decomposing a task, grounding intention to tools, and using the results for further actions, relying on natural language reasoning and programming abilities (Section 3.2)
  - [Lemur: Harmonizing Natural Language and Code for Language Agents](https://proceedings.iclr.cc/paper_files/paper/2024/file/41ec0e510c31883f3b50a782651fb5b9-Paper-Conference.pdf)
- **Web navigation** (behavioral indicator), 1 paper
  > Tool Use: The ability to interact with external tools and APIs, including functions such as web browsing, code execution, and file uploads. (Section 2.1)
  - [Law of the Weakest Link: Cross Capabilities of Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/63ea6a7d01a34a2c7334dcf1a2c3b03d-Paper-Conference.pdf)
- **Code execution** (behavioral indicator), 1 paper
  > Tool Use: The ability to interact with external tools and APIs, including functions such as web browsing, code execution, and file uploads. (Section 2.1)
  - [Law of the Weakest Link: Cross Capabilities of Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/63ea6a7d01a34a2c7334dcf1a2c3b03d-Paper-Conference.pdf)
- **Multi-hop reasoning** (construct), 1 paper
  > We propose SCRIBE, a framework for multi-hop tool reasoning, where models must flexibly call tools and self-reflect to generate high-quality responses. (Section 1)
  - [SCRIBE: Structured Chain Reasoning for Interactive Behaviour Explanations using Tool Calling](https://aclanthology.org/2025.emnlp-main.1490.pdf)
- **Self-reflection** (behavioral indicator), 1 paper
  > After the tool use step, the refined expression is sent to an LLM-based reflector for feedback (i.e., reflection). (Section 1)
  - [Re-Aligning Language to Visual Objects with an Agentic Workflow](https://proceedings.iclr.cc/paper_files/paper/2025/file/0d9057d84a9fc37523bf826232ea6820-Paper-Conference.pdf)
- **Parameter extraction** (behavioral indicator), 1 paper
  > In the first step, we facilitate the slot filling by inputting comprehensive medical records, tool descriptions, and their function docstrings into the LLM... enabling accurate information choices, and then to use the tool appropriately. (Section 3.3)
  - [MeNTi: Bridging Medical Calculator and LLM Agent with Nested Tool Calling](https://aclanthology.org/2025.naacl-long.263.pdf)
