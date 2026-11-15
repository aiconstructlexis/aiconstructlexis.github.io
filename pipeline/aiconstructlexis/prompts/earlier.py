"""The earlier revision of the extraction prompts.

The entity and relationship extraction prompts were revised once while the venues of
release v0.0.1 were being extracted. NeurIPS 2024, ICLR 2025 and part of NAACL 2025 and
ICLR 2024 were extracted with the two texts below; every other prompt is the one in
``default``. Run a pipeline with this set by pointing a configuration at it:
``prompts: aiconstructlexis.prompts.earlier``.
"""
import json

from aiconstructlexis.prompts.default import *  # noqa: F401,F403  (the unchanged prompts and helpers)
from aiconstructlexis.prompts.default import example_nomological_network


EXTRACT_ENTITIES_PROMPT = (
    """Your task is to act as a research assistant. Analyze the following academic paper and extract **entities only** (no relationships yet) for a **psychometric-style nomological network** for **Large Language Models (LLMs)**: abstract constructs, measurement instruments (benchmarks, user studies, surveys, and other evaluation procedures), and observable behaviors/tasks. **Faithfulness is more important than coverage**—if you cannot tie an item to a quote from the paper text, **omit** it.

## High-Level Analysis
- **Paper Summary:** 1–3 sentences on core topic and findings.
- **Notes:** Brief relevance/comments.

## Entity Definitions

### 1. Constructs — latent traits inferred from observable evidence

A construct is an **unobservable property of the model itself** — a cognitive ability, disposition, risk, or quality that persists across different tasks and settings. You never see a construct directly; you infer it from patterns of behavior and measurement. In psychometrics these are analogous to intelligence, personality factors, or aptitudes.

**Decision rules (apply in order):**

1. **"Could I watch the model do it?"** If you can point to specific model inputs and outputs that directly demonstrate it, it is a **behavior**, not a construct. If you can only infer it from patterns across multiple tasks or measurements, it is a **construct**.
2. **"Does it generalize as a trait across tasks?"** A construct should describe the model in a way that transfers across many different evaluation settings — the way "intelligence" transfers across math, verbal, and spatial tests. If it only describes what the model does in one specific task setting, it is probably a behavior.
3. **"Is it a property of the model, or of the experimental setup?"** Constructs are properties of the model. Benchmarks, architectures, training methods, and system names are not.

**Typical construct categories** (use as a guide, not a checklist — extract whatever the paper discusses):
- **Cognitive abilities:** reasoning (and its facets: mathematical, logical, commonsense, causal, analogical, spatial, temporal, abductive, etc.), language understanding, knowledge, perception, planning, creativity, abstraction
- **Safety and alignment traits:** harmlessness, helpfulness, toxicity, bias, fairness, robustness, sycophancy, trustworthiness, honesty, deception, safety
- **Model-level properties as latent traits:** generalization, memorization, calibration, interpretability, compositionality, multilinguality, instruction-following, in-context learning, few-shot learning, transfer learning

**What is NEVER a construct:**
- **Observable tasks or actions** → these are behaviors (see below)
- **Architecture components or mechanisms** (e.g. attention heads, mixture-of-experts routing, early-exit layers)
- **Training methods or algorithms** (e.g. RLHF, DPO, process supervision, distillation)
- **System or framework names** (e.g. a named pipeline, toolkit, or agent system)
- **Implementation details** (e.g. inference speed, memory usage, cost-efficiency of a method)
- **Benchmark/instrument names** → these are measurement instruments; **metric/scoring-function names** (accuracy, F1, BLEU, MSE, etc.) → exclude entirely (they are neither constructs nor measurement instruments)

**Resolving borderline cases — when a term names both a faculty and a task:**

Many terms (e.g. "reasoning", "comprehension", "commonsense reasoning") can refer to either a latent faculty or a task depending on context. Apply these rules:

- If a term describes a **broad cognitive ability** that explains performance across multiple tasks → **always classify as construct**, even if the paper also evaluates the model on tasks involving that ability. Terms like "commonsense reasoning", "mathematical reasoning", "language understanding", "logical reasoning" are **always constructs** — they name latent faculties, not specific observable tasks.
- Only classify something as a behavior if it describes a **specific, concrete task format** the model performs (e.g. "multiple-choice question answering", "code generation", "text summarization"). The task must be defined by its input/output format, not by the underlying ability.
- **When in doubt, prefer construct.** If a term could reasonably be either, classify it as a construct. It is better to over-include constructs than to misclassify latent abilities as behaviors.
- The corresponding behavior, if needed, should be named by the **task format** (e.g. construct "Commonsense reasoning" → behavior "Commonsense question answering"; construct "Mathematical reasoning" → behavior "Mathematical problem solving").

**Granularity rules:**
- **Split** distinct facets into separate constructs when the paper treats them as distinguishable abilities (e.g. "mathematical reasoning" and "logical reasoning" should be separate if the paper evaluates or discusses them differently).
- **Do not over-split:** if the paper mentions a term once in passing, it does not warrant a separate construct. The paper must discuss or evaluate it substantively.
- **Do not under-split:** if the paper explicitly contrasts two facets, they must be separate constructs.
- Use the **most specific name the paper supports.** If it discusses "spatial reasoning" specifically, use that — not the broader "Reasoning".

**Naming conventions:**
- Use **concise, community-standard noun phrases** that another researcher studying a different paper about the same trait would recognize.
- **Drop filler suffixes** like "ability", "capability", "skill" unless needed to disambiguate. Prefer "Mathematical reasoning" over "Mathematical reasoning ability".
- **Capitalize** only the first word (sentence case): "Mathematical reasoning", not "Mathematical Reasoning".

**Field requirements for each construct:**
- `name`: Concise noun-phrase label (2–5 words typical).
- `description`: One sentence that **defines** the latent trait so a reader who has not seen the paper can understand it. Do NOT just restate the name — add real explanatory content (e.g. for "Calibration" write "The degree to which the model's expressed confidence matches its actual accuracy across predictions").
- `source_snippets`: **Non-empty list**. Each entry is a **verbatim quote** copied directly from the paper text, optionally followed by a location reference like "(Sec. 3)" or "(Table 2)". Keep each snippet to the relevant phrase or sentence — not the whole paragraph. Do not paraphrase.

### 2. Behaviors — what you can observe the model doing

A behavior is an **observable task the model performs or output it produces**. If you could write an evaluation script that directly checks whether the model is doing it, it is a behavior.

**Decision rules:**

1. **"Is this a task/action I can directly observe, or a trait I infer?"** Task/action → behavior. Underlying trait → construct.
2. **"Would this be a row in a leaderboard, or a column?"** Measurement instruments assess behaviors (rows); the latent trait the instrument is designed to probe is a construct (column).

**Typical behavior categories** (use as a guide — extract whatever the paper discusses):
- **Generation tasks:** text generation, code generation, translation, summarization, image captioning, dialogue generation, data-to-text generation
- **Comprehension tasks:** question answering, reading comprehension, natural language inference, sentiment analysis, textual entailment
- **Structured output tasks:** information extraction, named entity recognition, parsing, table generation, relation extraction
- **Interactive tasks:** instruction following, tool use, multi-turn conversation, negotiation, web navigation
- **Safety-related behaviors:** harmful content refusal, jailbreak resistance, response under adversarial perturbation, toxic content generation
- **Domain-specific tasks:** clinical note generation, legal document analysis, scientific literature review, financial forecasting, robot manipulation

**Naming conventions:**
- Use **generic, reusable task names** that would apply across papers studying the same task — not paper-specific method names or overly narrow phrasings.
- **Abstract away** paper-specific framing to the standard community task name (e.g. "grade-school arithmetic solving" → "mathematical problem solving"; "vulnerability repair" → "code repair"; "step-level beam search inference" → the behavior it performs, not the method name).
- A measurement instrument that *assesses* a behavior is not itself a behavior. The behavior is the task; the instrument is how you test it. Do not use instrument names as behavior names.
- Use **present-tense gerund or noun form**: "Code generation", "Question answering", not "Generates code" or "Answer questions".
- **Capitalize** only the first word (sentence case).

**Field requirements for each behavior:**
- `name`: Concise noun-phrase label (2–5 words typical).
- `description`: One sentence describing what the model observably does, written so a reader can understand it without seeing the paper. Do NOT just restate the name — describe the task concretely enough that someone could design an evaluation for it.
- `source_snippets`: Same rules as constructs — verbatim quotes with optional location references. Non-empty list.

### 3. Measurement instruments — how constructs and behaviors are assessed

A measurement instrument is any **named, reproducible procedure used to assess model capabilities or behaviors**. This is broader than just benchmarks — it includes any structured way researchers gather evidence about a model.

**Categories of measurement instruments** (extract whatever the paper uses):
- **Benchmarks and datasets:** Named test sets the model is evaluated on (e.g. MMLU, HumanEval, SQuAD, ImageNet)
- **Human evaluation protocols:** User studies, preference studies, Likert-scale surveys, A/B tests, expert annotation tasks, crowdsourced ratings, inter-annotator agreement studies
- **Standardized questionnaires and scales:** Psychometric instruments, personality inventories, bias probes, Turing-test-style evaluations, red-teaming protocols
- **Evaluation suites and frameworks:** Named collections of tests (e.g. HELM, BIG-Bench, lm-eval-harness)
- **Domain-specific assessment procedures:** Clinical vignette evaluations, legal case analysis tasks, structured interviews with the model, simulation-based assessments

**What to include:** Any instrument the paper actually uses or explicitly references for evaluation that has a recognizable name or well-defined protocol. The instrument must be concrete enough that another researcher could replicate or reference it.

**What to exclude — scoring functions and evaluation metrics:** Any formula or algorithm that takes model output and returns a number is a **metric**, not a measurement instrument. Metrics are *how you score*; measurement instruments are *what you use to gather the data you score*. Exclude: accuracy, F1, BLEU, ROUGE, METEOR, BERTScore, MSE, MAE, RMSE, perplexity, pass@k, win rate, CIDEr, SPICE, EM (exact match), precision, recall, any "*-score" metric. Also exclude: evaluation settings (5-shot, zero-shot), training datasets (unless also used for evaluation), unnamed or ad-hoc test sets, and vague references like "our evaluation" or "the test set".

**Naming conventions:**
- Use the **community-standard short name** of the instrument — the name other researchers would use to look it up (e.g. the acronym if widely used).
- For human evaluations without a standard name, use a descriptive label that captures the method (e.g. "User preference study", "Expert annotation evaluation", "Red-teaming assessment").
- Put the full name and a brief description of what it assesses in the `description` field.
- Do NOT embed metric names or evaluation settings in the instrument name.
- **Capitalize** the name exactly as the community standard dictates (benchmark names are often acronyms or proper nouns; descriptive human evaluation names use sentence case).

**Field requirements for each measurement instrument:**
- `name`: The standard short name of the instrument or a descriptive label for the evaluation method.
- `description`: Full name (if the short name is an acronym) plus one sentence on what domain/ability/task it assesses and how (e.g. format, modality, population). Self-contained for a reader who has not seen the paper.
- `source_snippets`: Same rules as constructs — verbatim quotes with optional location references. Non-empty list.

### How constructs, behaviors, and measurement instruments relate

The three entity types form a layered structure:
- A **construct** (latent trait) manifests through one or more **behaviors** (observable tasks).
- A **measurement instrument** (benchmark, user study, evaluation protocol, etc.) is a procedure that directly tests a behavior and indirectly probes a construct.
- Example pattern: [Construct: latent trait] → [Behavior: observable task] ← [Measurement instrument: benchmark or evaluation]. The construct is *why* the model can do it; the behavior is *what* you see it do; the measurement instrument is the procedure you use to test it.
- The same instrument can relate to both a behavior (the task being measured) and a construct (the latent trait being probed). Include both links when the paper supports them.

**Final disambiguation check:** When in doubt between construct and behavior, **prefer construct**. If a term names a cognitive faculty or general ability (e.g. "reasoning", "comprehension", "commonsense reasoning"), it is always a construct. Only use behavior for terms that describe a specific, concrete task format defined by its inputs and outputs.

## Self-Check

After drafting, re-read the paper and run these checks:

1. **Quote check:** Every quote in `source_snippets` must actually appear in the paper text. Delete or fix any that fail.
2. **Category check:** Re-apply the decision rules for every entity:
   - For each construct: "Could I watch the model do it?" (must be no) and "Does it generalize as a trait?" (must be yes). If a term names a cognitive faculty, it stays as a construct even if the paper also uses it in a task context.
   - For each behavior: "Is this a specific, concrete observable task defined by its input/output format?" (must be yes). If it is actually a latent trait or general ability name, reclassify as a construct.
   - For each measurement instrument: "Is this a named/described procedure for gathering evidence about a model?" (must be yes). If it is a scoring function (accuracy, F1, BLEU, MSE, ROUGE, BERTScore, win rate, etc.), **remove it** — metrics are not measurement instruments.
3. **Naming check:** For each entity, ask: "Would another researcher studying a different paper about the same ability/task use the same name?" Normalize to community-standard terms.

## Output Format (JSON)

Return a single JSON object with keys: `Title`, `Notes`, `Paper Summary`, `Nomological Network`.
The `Nomological Network` must have exactly:
- `"constructs": [ { "name", "description", "source_snippets" }, ... ]`
- `"measurements": [ { "name", "description", "source_snippets" }, ... ]`
- `"behaviors": [ { "name", "description", "source_snippets" }, ... ]`

**Do NOT include a `relationships` key.** Relationships will be extracted in a separate step.

If the paper has no LLM-relevant content, use empty lists.

Example shape (illustrative only):
"""
    + json.dumps(
        {
            k: v
            for k, v in example_nomological_network.items()
            if k != "relationships"
        },
        indent=2,
        ensure_ascii=False,
    )
    + """
"""
)

EXTRACT_RELATIONSHIPS_PROMPT = """Your task is to act as a research assistant. You are given an academic paper and a set of **already-extracted entities** (constructs, measurement instruments, behaviors). Extract **relationships** between these entities that are explicitly supported by the paper text.

## Already-Extracted Entities

{entities_json}

## Relationship Extraction Rules

- **ONLY use entities from the list above** as source and target. Do NOT introduce new entity names.
- **`type` must be exactly one of:**
  - `causes` — explicit or strong causal claim ("X improves Y", "X enables Y", "X leads to Y")
  - `correlates` — empirical association, regression, or "predicts" in the statistical sense ("X is associated with Y", "higher X corresponds to higher Y")
  - `measured_by` — a construct or behavior is evaluated/operationalized by a measurement instrument ("We evaluate X using benchmark Y", "We conducted a user study to assess X")
  - `related` — a stated conceptual or empirical link that is NOT merely co-occurrence. The paper must describe HOW or WHY the two entities are connected.

### Evidence Quality Rules (STRICT)

- **`evidence`:** must be a **quoted substring** from the paper that **directly describes the connection** between source and target — not just mentions both in the same sentence.
- **Do NOT extract a relationship just because two entities appear in the same list, table, or sentence.** Listing instruments together (e.g. "we evaluate on MMLU, HumanEval, and GSM8K") does NOT create relationships between those instruments.
- **Do NOT extract a relationship if the evidence only shows co-occurrence** (e.g. "We test reasoning and code generation" does NOT mean reasoning → code generation).
- The evidence must answer: **"What does the paper say about how/why these two entities are connected?"** If you cannot answer that from the quote, do not include the relationship.

WRONG — co-occurrence, no stated connection:
  source: "Reasoning", target: "Code generation", evidence: "We conduct experiments on reasoning tasks (language understanding, code generation, and mathematical reasoning)"

RIGHT — stated connection:
  source: "Reasoning", target: "Aesthetic understanding", evidence: "to make further development of aesthetic understanding, reasoning is essential"

RIGHT — measurement instrument relationship:
  source: "Bias", target: "PAIRS", type: "measured_by", evidence: "We use PAIRS to probe social biases in VLMs"

RIGHT — human evaluation relationship:
  source: "Helpfulness", target: "User preference study", type: "measured_by", evidence: "We conducted a user preference study with 200 participants to evaluate helpfulness"

- **Allowed source–target patterns** (any combination justified by the text):
  - construct ↔ construct
  - construct ↔ behavior
  - construct → measurement instrument (measured_by)
  - measurement instrument → behavior
  - behavior ↔ behavior

## Self-Check

After drafting, verify:
- Every source and target name **exactly matches** an entity name from the list above.
- Every evidence quote **appears** in the supplied paper text.
- The evidence **describes a connection**, not just co-occurrence.
- Direction and `type` match the paper's claims.
- Prefer fewer, higher-quality relationships over many weak ones.

## Output Format (JSON)

Return a single JSON object with exactly:
{{
  "relationships": [
    {{
      "source": "Entity Name (from above list)",
      "target": "Entity Name (from above list)",
      "type": "causes | correlates | measured_by | related",
      "evidence": "Quoted text from the paper that directly describes the connection (Section/Table ref)."
    }}
  ]
}}

If no relationships are supported, return `{{"relationships": []}}`.

Return only the JSON object, no additional text."""


