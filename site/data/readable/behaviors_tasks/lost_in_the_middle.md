# Lost-in-the-middle
**Type:** Behavioral indicator  
**Supporting papers:** 10  
**Also known as:** Lost-in-the-middle phenomenon, Lost-in-the-middle effect, Token shifting, Serial position effect  

## State of the Field

**Space of definitions.** Across the papers, the prevailing usage treats lost-in-the-middle as a position-sensitive drop in performance when relevant information sits in the middle of the context rather than at the beginning or end. Most descriptions center on retrieval and other long-input tasks, where retrieval accuracy or recall is lower for mid-positioned content and can follow a U-shape over answer position, with one account noting slightly better performance at the beginning than at the end. A smaller framing describes the behavior through token shifting, where incorrect tokens at critical output positions lead to retrieval failure, and another uses the name serial position effect for better accuracy on beginning and end items than middle ones.

**Variants.** Papers study it mainly in long-input retrieval settings, and often operationalize the middle as content appearing between 20% and 80% of the input. Some work focuses on lower recall for leaf-level content, while other work examines element pairs in lists or critical output positions where a single wrong token can trigger retrieval failure. The naming varies, with lost-in-the-middle phenomenon or effect the common labels, and token shifting or serial position effect used in smaller lines of work.

**Space of elicitation and scores.** No measurement instrument is linked to it. In use, papers score the behavior through retrieval accuracy, recall for mid-positioned content, and whether the model answers correctly for items at different sequence positions. A smaller line of work also treats erroneous token generation at critical positions as the observable failure signature.

**What it is taken as evidence of.** Among linked constructs, papers most commonly connect it to long-context understanding: papers claim a causal relationship from lost-in-the-middle to long-context understanding, describing degraded performance with increasing context length and discussing it in evaluations of long-context capability. Papers also report that lost-in-the-middle is related to positional bias, and one paper relates context utilization to lost-in-the-middle through uneven utilization of lengthy inputs and a tendency to overlook the middle portion. Overall, the linked work does not converge on a single construct it reflects.

## Sources

**Lost-in-the-middle phenomenon** (1 paper: [On the Emergence of Position Bias in Transformers](https://raw.githubusercontent.com/mlresearch/v267/main/assets/wu25ad/wu25ad.pdf))
> The observable degradation in a model's performance, particularly in retrieval tasks, when relevant information is located in the middle of the input context compared to the beginning or end.

**Lost-in-the-middle effect** (1 paper: [Towards a Holistic and Automated Evaluation Framework for Multi-Level Comprehension of LLMs in Book-Length Contexts](https://aclanthology.org/2025.emnlp-main.1241.pdf))
> A failure mode where models underperform on information located in the middle portion of long inputs, leading to lower recall for mid-positioned content.

**Token shifting** (1 paper: [POSITION BIAS MITIGATES POSITION BIAS: Mitigate Position Bias Through Inter-Position Knowledge Distillation](https://aclanthology.org/2025.emnlp-main.78.pdf))
> The observable phenomenon where a model generates incorrect tokens at critical positions in the output sequence due to the position of the relevant input information, leading to retrieval failure.

**Serial position effect** (1 paper: [Position: Principles of Animal Cognition to Improve LLM Evaluations](https://raw.githubusercontent.com/mlresearch/v267/main/assets/rane25a/rane25a.pdf))
> A pattern of performance in which a model is more accurate when responding to items at the beginning or end of a sequence compared to those in the middle, mirroring a well-documented cognitive bias in humans and animals.

## Relationships

### Lost-in-the-middle →
- **Long-context understanding** (construct): *causes*, 3 papers
  > the “lost in the middle” (Liu et al., 2024c; Song et al., 2024) phenomenon degrades performance with increasing context length (Section 1).
  - [CoMemo: LVLMs Need Image Context with Image Memory](https://raw.githubusercontent.com/mlresearch/v267/main/assets/liu25bn/liu25bn.pdf)
  - [Retrieval meets Long Context Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/d75f29006df67df084e6586f1cb8458c-Paper-Conference.pdf)
  - [An Efficient Recipe for Long Context Extension via Middle-Focused Positional Encoding](https://proceedings.neurips.cc/paper_files/paper/2024/file/66944d3a3e77ebe366793f6a6126f3a4-Paper-Conference.pdf)

### Associated with
- **Positional bias** (construct), 2 papers
  > “We observed significant positional bias in LMMs, reminiscent of the ‘lost-in-the-middle’ pathology found in NLP tasks”
  - [Visual Haystacks: A Vision-Centric Needle-In-A-Haystack Benchmark](https://proceedings.iclr.cc/paper_files/paper/2025/file/a264726ebd222124514a32bf0143b83d-Paper-Conference.pdf)
  - [On the Emergence of Position Bias in Transformers](https://raw.githubusercontent.com/mlresearch/v267/main/assets/wu25ad/wu25ad.pdf)
- **Context utilization** (construct), 1 paper
  > Despite the extended context window, LLMs still face a significant challenge in long-context inference due to the uneven utilization of lengthy inputs. [15] conducted a pivotal investigation, revealing that LLMs tend to overlook the middle portion of the input. (Section 2.2)
  - [Found in the Middle: How Language Models Use Long Contexts Better via Plug-and-Play Positional Encoding](https://proceedings.neurips.cc/paper_files/paper/2024/file/6ffdbbe354893979367f93e2121e37dd-Paper-Conference.pdf)
