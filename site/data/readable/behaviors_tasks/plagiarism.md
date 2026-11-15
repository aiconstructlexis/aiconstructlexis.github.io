# Plagiarism
**Type:** Behavioral indicator  
**Supporting papers:** 4  

## State of the Field

**Space of definitions.** Papers that define it treat plagiarism as submitting code that is highly similar to existing public solutions, with public Kaggle notebooks given as the example source. What counts as the behavior is the degree of similarity between the submitted code and those existing solutions.

**Space of elicitation and scores.** It is measured by one instrument, Dolos. In MLE-bench: Evaluating Machine Learning Agents on Machine Learning Engineering, Dolos is used to compare an agent's submitted code against the top 50 associated notebooks from the relevant Kaggle competition as a plagiarism check.

**What it is taken as evidence of.** The papers do not link this behavior to any construct.

## Sources

**Plagiarism** (2 papers: [MLE-bench: Evaluating Machine Learning Agents on Machine Learning Engineering](https://proceedings.iclr.cc/paper_files/paper/2025/file/7e3767db483c942b883eb4f8cfb74e31-Paper-Conference.pdf), [Online Detection of LLM-Generated Texts via Sequential Hypothesis Testing by Betting](https://raw.githubusercontent.com/mlresearch/v267/main/assets/chen25bn/chen25bn.pdf))
> The act of submitting code that is highly similar to existing public solutions, such as those found in public Kaggle notebooks.

## Relationships

### Plagiarism →
- **Dolos** (measurement instrument): *measured_by*, 1 paper
  > To prevent plagiarism, we use the source code plagiarism detection tool Dolos (Maertens et al., 2024) to compare the agent’s submitted code against the top 50 associated notebooks from the relevant Kaggle competition.
  - [MLE-bench: Evaluating Machine Learning Agents on Machine Learning Engineering](https://proceedings.iclr.cc/paper_files/paper/2025/file/7e3767db483c942b883eb4f8cfb74e31-Paper-Conference.pdf)
