# Dialogue state tracking
**Type:** Behavioral indicator  
**Supporting papers:** 5  

## State of the Field

**Space of definitions.** Across the surveyed work, the dominant framing treats dialogue state tracking as a multi-turn task-oriented dialogue task that extracts, maintains, identifies, and updates a user's goals, requests, and constraints as the conversation unfolds. Most descriptions represent the state as slot-value pairs tracking user needs across turns, while a smaller formulation specifies the output as domain-slot-value triples. Papers describe success as keeping this evolving state current from turn to turn, for example by predicting the set of slot-value pairs, or domain-slot-value triples, needed to fulfill the user's goal.

**Variants.** Papers study dialogue state tracking in several settings, with zero-shot formulations appearing most often, including scheme-only and open-vocabulary versions. Another paper includes it as one task within continual learning alongside other NLP task types. One paper also relates dialogue state tracking to question answering by reformulating it as a question-answering task for less capable models, and one paper claims a causal relationship from chain of thought to dialogue state tracking, reporting approximately 10% higher zero-shot accuracy when CoT from Step 1 is incorporated.

**Space of elicitation and scores.** Papers link one measurement instrument to dialogue state tracking: SGD. The linked evidence uses SGD as a dataset for comparative analysis of language models on the dialogue state tracking task, and no other measurement instrument is linked.

**What it is taken as evidence of.** Among the papers, the only construct linked to dialogue state tracking is dialogue understanding, so there is no competing construct-level framing in the linked relations. That link is reported as a related relationship rather than an explicit measurement or correlation claim, and it is described through understanding user needs and executing appropriate system actions in task-oriented dialogues.

## Sources

**Dialogue state tracking** (4 papers: [From Schema to State: Zero-Shot Scheme-Only Dialogue State Tracking via Diverse Synthetic Dialogue and Step-by-Step Distillation](https://aclanthology.org/2025.emnlp-main.85.pdf), [A Zero-Shot Open-Vocabulary Pipeline for Dialogue Understanding](https://aclanthology.org/2025.naacl-long.387.pdf), [PicPersona-TOD : A Dataset for Personalizing Utterance Style in Task-Oriented Dialogue with Image Persona](https://aclanthology.org/2025.naacl-long.403.pdf), [Prototype Conditioned Generative Replay for Continual Learning in NLP](https://aclanthology.org/2025.naacl-long.636.pdf))
> The observable task of identifying and updating domain-slot-value triples across conversation turns to reflect the evolving user intent in a task-oriented dialogue.

## Relationships

### Dialogue state tracking →
- **SGD** (measurement instrument): *measured_by*, 1 paper
  > Our main results for the DST task are given Table 2, offering a comparative analysis of various language models on the MultiWOZ 2.1, 2.4 and SGD datasets.
  - [A Zero-Shot Open-Vocabulary Pipeline for Dialogue Understanding](https://aclanthology.org/2025.naacl-long.387.pdf)

### → Dialogue state tracking
- **Chain of thought** (behavioral indicator): *causes*, 1 paper
  > The results in Table 4 show that incorporating the CoT from Step 1 provides an approximately 10% improvement in zero-shot accuracy by offering a more robust representation for each turn. (Section 4.6)
  - [From Schema to State: Zero-Shot Scheme-Only Dialogue State Tracking via Diverse Synthetic Dialogue and Step-by-Step Distillation](https://aclanthology.org/2025.emnlp-main.85.pdf)

### Associated with
- **Dialogue understanding** (construct), 1 paper
  > Dialogue State Tracking (DST) is crucial for understanding user needs and executing appropriate system actions in task-oriented dialogues.
  - [A Zero-Shot Open-Vocabulary Pipeline for Dialogue Understanding](https://aclanthology.org/2025.naacl-long.387.pdf)
- **Question answering** (behavioral indicator), 1 paper
  > Our approach includes reformulating DST as a question-answering task for less capable models and employing self-refining prompts for more adaptable ones.
  - [A Zero-Shot Open-Vocabulary Pipeline for Dialogue Understanding](https://aclanthology.org/2025.naacl-long.387.pdf)
