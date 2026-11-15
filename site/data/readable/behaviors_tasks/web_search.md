# Web search
**Type:** Behavioral indicator  
**Supporting papers:** 4  
**Also known as:** Web content retrieval  

## State of the Field

**Space of definitions.** Across the surveyed work, the prevailing usage treats web search as invoking a search tool, search engine, or search API with a generated or structured query to retrieve web information for answering a user query. A common formulation is retrieving a list of webpages from a live search engine, while one paper describes a fuller sequence in which the model formulates structured search queries, sends them through web search APIs, then "fetch[es] complete web pages, primarily the HTML content," extracts relevant text, and synthesizes an answer. Papers also describe it as web browsing used to answer a question.

**Variants.** Papers study several nearby forms of this behavior. Alongside the label "Web search," some authors use "Web content retrieval"; examples include general question answering, "complicated web browsing" to answer a question, searching for time-sensitive or source-specific information, and site-specific searches such as Google search or looking on BBC Good Food for recipes and ingredient lists.

**Space of elicitation and scores.** No measurement instrument is linked to it. Instead, papers describe the behavior procedurally through explicit tool use, such as generating a JSON-formatted request with the tool name web_search or sending structured queries to search engines via APIs.

**What it is taken as evidence of.** No construct is linked to it.

## Sources

**Web search** (2 papers: [DeepResearcher: Scaling Deep Research via Reinforcement Learning in Real-world Environments](https://aclanthology.org/2025.emnlp-main.22.pdf), [Multi-modal Agent Tuning: Building a VLM-Driven Agent for Efficient Tool Usage](https://proceedings.iclr.cc/paper_files/paper/2025/file/238747e153a84f50b43fd50fa8504f33-Paper-Conference.pdf))
> The action of invoking a search tool with a generated query to retrieve a list of webpages from a live search engine.

**Web content retrieval** (1 paper: [Web Intellectual Property at Risk: Preventing Unauthorized Real-Time Retrieval by Large Language Models](https://aclanthology.org/2025.emnlp-main.870.pdf))
> Observable behavior in which the LLM uses search APIs to retrieve and process HTML content from webpages relevant to a user query for response generation.
