# Human annotation study
**Type:** Measurement instrument  
**Supporting papers:** 3  

## State of the Field

**What it is.** Across these papers, the prevailing use of "human annotation study" is as a flexible human evaluation protocol, but the concrete protocol varies by task. One framing uses 84 participants who each annotate 18 news stories, 9 real and 9 fake, and classify them as real or fake "without relying on the Internet." Another has humans annotate a subset of 390 examples from DEFREASING*N-alt, following the naturalistic prompt instructions, to compare model behavior with human tendencies. A further version uses three graduate students per episode to annotate an AI agent's truthfulness with fine-grained and coarse-grained categories, with omniscient access to background information, hidden details, and full conversation history.

**What it is claimed to measure.** Papers use this protocol to measure 2 constructs, Coverage and Truthfulness, and it is not linked to any behavioral indicators. The claims are spread across these two constructs rather than converging on a single one: papers report using the results of a human annotation study as ground truth for sentence-level coverage, and they also report having annotators label an agent's truthfulness using fine-grained and coarse-grained metrics.

**Space of uses.** Across the surveyed work, the dominant positioning is as a validation or comparison procedure rather than as a standalone benchmark. Papers use it to validate a truthfulness evaluator, to compare model behavior with human tendencies, and to supply ground truth for another evaluation. It is also linked to 1 other measurement instrument, STEER-BENCH, where papers relate a human annotation study to validating that generated demonstrations and questions "faithfully represent community views."

## Sources

**Human annotation study** (3 papers: [Have LLMs Reopened the Pandora's Box of AI-Generated Fake News?](https://aclanthology.org/2025.naacl-long.142.pdf), [AI-LieDar : Examine the Trade-off Between Utility and Truthfulness in LLM Agents](https://aclanthology.org/2025.naacl-long.595.pdf), [Evaluating Defeasible Reasoning in LLMs with DEFREASING](https://aclanthology.org/2025.naacl-long.529.pdf))
> A human evaluation protocol where 84 participants each analyzed and classified 18 news stories (9 real, 9 fake) as either real or fake without using the internet.

## Relationships

### → Human annotation study
- **Truthfulness** (construct): *measured_by*, 1 paper
  > For each episode, three graduate students annotate the AI agent’s truthfulness using both fine-grained (distinguishing between Concealment and Equivocation) and coarse-grained (using the Partial Lie category) metrics. (Section 4.2)
  - [AI-LieDar : Examine the Trade-off Between Utility and Truthfulness in LLM Agents](https://aclanthology.org/2025.naacl-long.595.pdf)
- **Coverage** (construct): *measured_by*, 1 paper
  > To evaluate sentence-level coverage (defined in § 2.2), we used the results of the human annotation study (§4.1.2) as ground truth.
  - [Towards Effective Extraction and Evaluation of Factual Claims](https://aclanthology.org/2025.acl-long.348.pdf)

### Associated with
- **STEER-BENCH** (measurement instrument), 1 paper
  > “To validate that generated demonstrations and questions faithfully represent community views, we conduct a human annotation study”
  - [STEER-BENCH: A Benchmark for Evaluating the Steerability of Large Language Models](https://aclanthology.org/2025.emnlp-main.925.pdf)
