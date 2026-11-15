# Parameter extraction
**Type:** Behavioral indicator  
**Supporting papers:** 4  
**Also known as:** Parameter resolution, Parameterization, Parameter selection  

## State of the Field

**Space of definitions.** Across definitions, the common framing is the observable step of getting the right parameter or argument values for a tool, function, or API call. Papers variously describe this as extracting values from a natural-language query, assigning correct values to a selected function's parameters, or providing the correct arguments for a selected tool call; a narrower dialogue-oriented framing treats it as filling missing API values from dialogue context or user replies. The success criterion is usually correctness of the chosen values, reflected in examples such as extracting visitor counts, ticket types, or special conditions, or stating that a parameter has a specific value such as "fried chicken" or "Lyft".

**Variants.** Papers use several near-names for the same behavior: parameter extraction, parameter resolution, parameterization, and parameter selection. The studied settings differ, including natural-language orders converted into code arguments, dialogue-based API completion, and single-tool or per-dialogue-turn tool-calling evaluation. One paper also relates it to Tool use in a medical slot-filling setup, where comprehensive medical records, tool descriptions, and function docstrings are used to facilitate slot filling and then use the tool appropriately.

**Space of elicitation and scores.** No measurement instrument is linked to this behavior. In operational use, papers nonetheless describe scoring with accuracy-style measures, including "parameter resolution accuracy" and "Parameter Selection Accuracy (PS)," and one quoted passage refers to per-dialogue-turn accuracy of tool and parameter selection.

**What it is taken as evidence of.** No construct is linked to this behavior, so the papers here do not present it as evidence of any particular construct. The only recorded cross-entity connection outside measurement is that one paper reports it as related to Tool use, rather than tying it to a construct.

## Sources

**Parameter extraction** (1 paper: [PricingLogic: Evaluating LLMs Reasoning on Complex Tourism Pricing Tasks](https://aclanthology.org/2025.emnlp-main.393.pdf))
> The observable task of identifying and extracting specific values from a natural language query to serve as arguments for a function call.

**Parameter resolution** (1 paper: [AskToAct: Enhancing LLMs Tool Use via Self-Correcting Clarification](https://aclanthology.org/2025.emnlp-main.682.pdf))
> The model fills in missing API parameter values from dialogue context or user replies.

**Parameterization** (1 paper: [Improving Large Language Models Function Calling and Interpretability via Guided-Structured Templates](https://aclanthology.org/2025.emnlp-main.1242.pdf))
> The observable action of identifying and assigning correct values to the parameters required by a selected function.

**Parameter selection** (1 paper: [MTU-Bench: A Multi-granularity Tool-Use Benchmark for Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/4d13b2d99519c5415661dad44ab7edcd-Paper-Conference.pdf))
> The observable action of identifying and providing the correct arguments or parameters for a selected tool call.

## Relationships

### Associated with
- **Tool use** (behavioral indicator), 1 paper
  > In the first step, we facilitate the slot filling by inputting comprehensive medical records, tool descriptions, and their function docstrings into the LLM... enabling accurate information choices, and then to use the tool appropriately. (Section 3.3)
  - [MeNTi: Bridging Medical Calculator and LLM Agent with Nested Tool Calling](https://aclanthology.org/2025.naacl-long.263.pdf)
