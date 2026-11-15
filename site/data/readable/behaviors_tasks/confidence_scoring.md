# Confidence scoring
**Type:** Behavioral indicator  
**Supporting papers:** 3  

## State of the Field

**Space of definitions.** Across the papers, the prevailing usage is to treat confidence scoring as producing a numerical confidence value for a model judgment. Most formulations use a 0 to 1 scale, applied to the truth of a target statement, the shared authorship of documents, or a diagnostic decision: one recurring setup directly asks "True or False? {target statement}" and derives confidence from the next-token probabilities of "True" and "False," while another asks for a score in [0,1] indicating confidence in shared authorship. A smaller variant scores each candidate match on a 0 to 100 scale and allows "None of the above" when no suitable match exists.

**Variants.** The behavior appears in several settings, and papers vary mainly in what the score is attached to. Some score single statements, some score shared authorship across documents, and some score diagnostic decisions using factual consistency and evidence from a reasoning subgraph; one paper also relates confidence scoring to schema matching, describing a program composed of candidate generation, refinement, and confidence scoring. The clearest variant departs from the common [0,1] form by using MCQ-style candidate scoring with an abstain option, "NONE of the above."

**Space of elicitation and scores.** No measurement instrument is linked to it. The described operationalizations instead use direct prompting and score extraction: papers elicit "True" or "False" and read next-token probabilities, request an explicit score in [0,1], repurpose a Critic to assess a diagnostic confidence score, or ask for a 0 to 100 relevance score in an MCQ format that includes "NONE of the above."

**What it is taken as evidence of.** Papers do not link confidence scoring to any construct. The only reported relationship is that one paper relates it to schema matching.

## Sources

**Confidence scoring** (3 papers: [CAVE: Controllable Authorship Verification Explanations](https://aclanthology.org/2025.naacl-long.451.pdf), [A Probabilistic Framework for LLM Hallucination Detection via Belief Tree Propagation](https://aclanthology.org/2025.naacl-long.158.pdf), [Knowledge-Aware Co-Reasoning for Multidisciplinary Collaboration](https://aclanthology.org/2025.emnlp-main.687.pdf))
> Assigning a numerical confidence score between 0 and 1 to a statement based on the LLM's next-token prediction probabilities for 'True' or 'False'.

## Relationships

### Associated with
- **Schema matching** (behavioral indicator), 1 paper
  > we propose Matchmaker - a compositional language model program for schema matching, comprised of candidate generation, refinement and confidence scoring. (Abstract)
  - [Bootstrapping Self-Improvement of Language Model Programs for Zero-Shot Schema Matching](https://raw.githubusercontent.com/mlresearch/v267/main/assets/seedat25a/seedat25a.pdf)
