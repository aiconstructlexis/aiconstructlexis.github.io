# Engagement
**Type:** Construct  
**Supporting papers:** 6  
**Also known as:** Interactive engagement, Engagingness  

## State of the Field

**Space of definitions.** Most papers treat engagement, or engagingness, as a response or dialogue quality, whether phrased as outputs that are interesting, captivating, likely to elicit further interaction, or judged engaging in social interaction. A smaller line of work narrows this to interactive engagement, described as a text's ability to "draw the user in" and encourage ongoing, dynamic contribution to the dialogue. Another usage shifts the construct to the discussion level, defining engagement as interest plus participation, combining reciprocity, response diversity, and discussion length, so the main difference across papers is whether engagement is located in model responses or in broader user participation.

**Space of facets.** Papers use several near-neighbor names, especially engagement, engagingness, and interactive engagement, for overlapping but not identical ideas. Most of these variants still center on maintaining attention or interest, and long-term dialogue work further frames engagingness as the ability to maintain an annotator's interest over time, with shared memories described as making dialogues more engaging. One paper also places engagement alongside honesty, helpfulness, harmlessness, and unbiasedness as one fine-grained alignment perspective, while the discussion-oriented usage broadens it by explicitly combining interest with participation.

**Space of measurement.** Papers link engagement to one measurement instrument, LLM-as-a-judge, and no behavioral indicators. In the linked operationalization, an LLM judge, GPT-4o, evaluates Engagingness; other quoted passages describe observer agents rating engagement, a dialog engagement classifier, and a Reddit upvote probability ranking model. These operationalizations largely match definitions that treat engagement as something judged from responses, while the discussion-level definition instead points to metrics such as reciprocity, response diversity, and discussion length.

## Sources

**Engagement** (3 papers: [Leftover Lunch: Advantage-based Offline Reinforcement Learning for Language Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/3b18d368150474ac6fc9bb665d3eb3da-Paper-Conference.pdf), [Training Socially Aligned Language Models on Simulated Social Interactions](https://proceedings.iclr.cc/paper_files/paper/2024/file/d763b4a2dde0ae7b77498516ce9f439e-Paper-Conference.pdf), [Evaluation and Facilitation of Online Discussions in the LLM Era: A Survey](https://aclanthology.org/2025.emnlp-main.1243.pdf))
> The model's ability to generate responses that are interesting, captivating, and likely to elicit further interaction from a user.

**Engagingness** (2 papers: [Flexibly Utilize Memory for Long-Term Conversation via a Fragment-then-Compose Framework](https://aclanthology.org/2025.emnlp-main.1069.pdf), [SHARE: Shared Memory-Aware Open-Domain Long-Term Dialogue Dataset Constructed from Movie Script](https://aclanthology.org/2025.acl-long.704.pdf))
> The perceived quality of a model's conversational responses to be interesting, captivating, and hold a user's attention.

**Interactive engagement** (1 paper: [Crab: A Novel Configurable Role-Playing LLM with Assessing Benchmark](https://aclanthology.org/2025.acl-long.731.pdf))
> The model's capacity to actively involve the user in the dialogue, encouraging ongoing interaction and dynamic contribution to the conversation.

## Relationships

### Engagement →
- **LLM-as-a-judge** (measurement instrument): *measured_by*, 1 paper
  > We use GPT-4o to evaluate Engagingness, Humanness, and Memorability. (Section 4.1)
  - [Flexibly Utilize Memory for Long-Term Conversation via a Fragment-then-Compose Framework](https://aclanthology.org/2025.emnlp-main.1069.pdf)
