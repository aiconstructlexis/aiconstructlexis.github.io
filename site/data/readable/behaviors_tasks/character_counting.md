# Character counting
**Type:** Behavioral indicator  
**Supporting papers:** 4  
**Also known as:** Word length counting  

## State of the Field

**Space of definitions.** Across papers, the dominant framing is a character-level counting task that asks for a numeric answer from presented text. Most commonly, success means accurately reporting the total number of characters in a word or in a whitespace-free character sequence, using prompts such as "How many characters in the word \"Y\"?" or asking for the number of lowercase characters in a sequence; a smaller line of work broadens it to counting the occurrences of a specified character, and one definition explicitly says the task is used to probe the model's sub-token counting ability.

**Variants.** Papers study several variants under this label. They include word length counting, counting characters in raw lowercase letter sequences without whitespaces, counting a target character inside a word shown as an image, and multilingual text-level tasks named Occurrence, Length, and Distinct, which ask for the number of occurrences, total length, or number of distinct characters; one quoted passage also mentions sentence length prediction.

**Space of elicitation and scores.** Papers elicit the behavior with direct counting questions and expect a numeric answer that matches a ground-truth count, for example identifying that the answer for "strawberry" is 10 or counting letters in an image-displayed word. No measurement instrument is linked to it.

**What it is taken as evidence of.** One definition presents the task as a probe of the model's sub-token counting ability. Beyond that framing, papers do not link the behavior to any construct.

## Sources

**Character counting** (3 papers: [Language Models are Crossword Solvers](https://aclanthology.org/2025.naacl-long.104.pdf), [From Introspection to Best Practices: Principled Analysis of Demonstrations in Multimodal In-Context Learning](https://aclanthology.org/2025.naacl-long.170.pdf), [Enhancing Character-Level Understanding in LLMs through Token Internal Structure Learning](https://aclanthology.org/2025.acl-long.194.pdf))
> The observable task of predicting the number of characters in a given sequence of letters, used to probe the model's sub-token counting ability.

**Word length counting** (1 paper: [LLM The Genius Paradox: A Linguistic and Math Expert's Struggle with Simple Word-based Counting Problems](https://aclanthology.org/2025.naacl-long.172.pdf))
> The observable behavior of accurately reporting the total number of characters in a given word.
