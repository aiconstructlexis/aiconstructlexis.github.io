# Request compliance
**Type:** Behavioral indicator  
**Supporting papers:** 5  
**Also known as:** Compliance, Compliant response generation, Instruction acceptance  

## State of the Field

**Space of definitions.** Across the papers, the prevailing usage treats request compliance as observable answer behavior: following a user's instruction or attempting to fulfill a request, and responding directly rather than refusing. Most definitions add that the answer should be substantive or helpful, so compliance is usually framed as a direct answer to the prompt or query, contrasted with refusal.

**Variants.** A recurring setting is compliance with harmless or benign prompts versus refusal of harmful ones. The labels vary, with compliance the most common wording, alongside compliant response generation and instruction acceptance; one helpfulness setting measures acceptance on benign prompts that share keywords with AdvBench but do not contain harmful intent, and another notes lower acceptance in a Sensitive category.

**Space of elicitation and scores.** No measurement instrument is linked to it. Papers nevertheless operationalize the behavior through refusal-versus-compliance judgments, including whether WildGuard classifies the response as refusal or compliance on XStest, through instruction acceptance rate on benign prompts, and in one study through the minimal gamma found by line search that generates a compliant response for a query.

**What it is taken as evidence of.** No construct is linked to it.

## Sources

**Compliance** (2 papers: [Programming Refusal with Conditional Activation Steering](https://proceedings.iclr.cc/paper_files/paper/2025/file/e2dd53601de57c773343a7cdf09fae1c-Paper-Conference.pdf), [Test-Time Preference Optimization: On-the-Fly Alignment via Iterative Textual Feedback](https://raw.githubusercontent.com/mlresearch/v267/main/assets/li25ac/li25ac.pdf))
> The model's observable action of following a user's instruction and providing a direct, substantive answer to the prompt.

**Compliant response generation** (1 paper: [Just Enough Shifts: Mitigating Over-Refusal in Aligned Language Models with Targeted Representation Fine-Tuning](https://raw.githubusercontent.com/mlresearch/v267/main/assets/dabas25a/dabas25a.pdf))
> The observable act of a model providing a direct and helpful answer to a user's query, as opposed to refusing it.

**Instruction acceptance** (1 paper: [Harmful Prompt Laundering: Jailbreaking LLMs with Abductive Styles and Symbolic Encoding](https://aclanthology.org/2025.emnlp-main.1296.pdf))
> The model's behavior of complying with and attempting to fulfill the instructions in a given prompt, as opposed to refusing.
