"""Prompts of the AI Construct Lexis pipeline.

These are the prompt texts of the release run: paper screening, two-pass entity and
relationship extraction, harmonization (grouping and merging of surface names) and the
per-entity summaries. The extraction prompts were revised once during the run; ``earlier``
holds the revision used for the venues extracted before it (docs/MODEL_CARD.md). Edit them
only when you intend to run a differently prompted pipeline; the summary section labels
below also drive the site export.
"""
import json


# Constructs = abstract latent variables (capabilities, risks, traits). Behaviors = tasks/outputs/performance outcomes.
# Measurements = measurement instruments (benchmarks, datasets, user studies, surveys, etc.); no scores/metrics in extraction.
# Relationships: type is one of related, causes, correlates, measured_by. Every node needs source_snippets; evidence must quote the paper.
example_nomological_network = {
    "constructs": [
        {
            "name": "Spatial reasoning",
            "description": "The latent ability to mentally represent and manipulate spatial relationships between objects.",
            "source_snippets": [
                '"we evaluate spatial reasoning through block-placement tasks" (Sec. 3)'
            ],
        },
        {
            "name": "Robustness",
            "description": "The degree to which model performance is stable under input perturbations.",
            "source_snippets": [
                '"robustness to adversarial rephrasings" (Abstract)'
            ],
        },
    ],
    "measurements": [
        {
            "name": "BlocksWorld",
            "description": "Planning benchmark requiring multi-step block rearrangement.",
            "source_snippets": ['"evaluated on BlocksWorld" (Table 1)'],
        },
        {
            "name": "User preference study",
            "description": "Human evaluation in which participants rate or rank model outputs on criteria such as helpfulness and coherence.",
            "source_snippets": [
                '"we conducted a user study with 50 participants rating outputs" (Sec. 5)'
            ],
        },
    ],
    "behaviors": [
        {
            "name": "Multi-step planning",
            "description": "Producing a sequence of actions to achieve a goal state from an initial state.",
            "source_snippets": [
                '"the model generates step-by-step plans" (Sec. 4)'
            ],
        },
    ],
    "relationships": [
        {
            "source": "Spatial reasoning",
            "target": "Multi-step planning",
            "type": "related",
            "evidence": '"spatial reasoning underlies the planning steps required" (Sec. 5).',
        },
        {
            "source": "BlocksWorld",
            "target": "Multi-step planning",
            "type": "related",
            "evidence": '"BlocksWorld directly measures multi-step planning ability" (Sec. 3).',
        },
    ],
}


EXTRACT_ENTITIES_PROMPT = (
    """Your task is to act as a research assistant. Analyze the following academic paper and extract **entities only** (no relationships yet) for a **psychometric-style nomological network** for **Large Language Models (LLMs)**: abstract constructs, measurement instruments (benchmarks, user studies, surveys, and other evaluation procedures), and observable behaviors/tasks. **Faithfulness is more important than coverage**—if you cannot tie an item to a quote from the paper text, **omit** it.

## High-Level Analysis
- **Paper Summary:** 1–3 sentences on core topic and findings.
- **Notes:** Brief relevance/comments.

## Entity Definitions

The three entity types form a layered structure: a **construct** (latent trait) manifests through one or more **behaviors** (observable tasks), and a **measurement instrument** is the procedure used to test a behavior and thereby probe a construct. The construct is *why* the model can do it; the behavior is *what* you see it do; the instrument is *how* you test it. The same instrument can relate to both a behavior and a construct — include both links when the paper supports them.

### 1. Constructs — latent traits inferred from observable evidence

A construct is an **unobservable property of the model** — a cognitive ability, disposition, risk, or quality that persists across tasks. You never see it directly; you infer it from patterns of behavior and measurement. Analogous to intelligence or personality factors in psychometrics.

**Decision rules (apply in order):**
1. **"Could I watch the model do it?"** If specific inputs and outputs directly demonstrate it → **behavior**. If you can only infer it from patterns across many tasks → **construct**.
2. **"Does it generalize as a trait across tasks?"** A construct transfers across different evaluation settings (the way "intelligence" transfers across math, verbal, and spatial tests). If it only describes one specific task setting, it is probably a behavior.
3. **"Is it a property of the model, or of the experimental setup?"** Only model properties count. Architectures, training methods, system/framework names, and implementation details (inference speed, memory, cost) are never constructs. Metric/scoring-function names (accuracy, F1, BLEU, MSE, etc.) are excluded entirely — they are neither constructs nor instruments.

**When in doubt between construct and behavior, prefer construct.** If a term names a cognitive faculty or general ability (e.g. "reasoning", "comprehension", "commonsense reasoning", "mathematical reasoning", "language understanding"), classify as construct even if the paper also evaluates tasks involving it. Only use behavior for terms defined by a specific input/output task format (e.g. "multiple-choice question answering", "code generation"). Corresponding behavior names should come from the task format (construct "Commonsense reasoning" → behavior "Commonsense question answering").

**Examples to give you a flavor of construct categories** (illustrative only — extract whatever the paper actually discusses, including things not listed here):
- *Cognitive abilities:* reasoning and its facets (mathematical, logical, commonsense, causal, spatial, temporal, …), language understanding, planning, creativity, abstraction
- *Safety and alignment traits:* harmlessness, helpfulness, toxicity, bias, fairness, robustness, sycophancy, honesty, deception
- *Model-level latent properties:* generalization, memorization, calibration, interpretability, compositionality, multilinguality, instruction-following, in-context learning

**Granularity:** split distinct facets into separate constructs when the paper treats them as distinguishable (e.g. "mathematical reasoning" vs "logical reasoning" if evaluated separately); do not over-split for passing mentions; use the most specific name the paper supports.

**Naming:** concise noun phrases another researcher would recognize; drop filler suffixes like "ability"/"capability"/"skill" unless needed to disambiguate; sentence case ("Mathematical reasoning", not "Mathematical Reasoning").

**Field requirements:**
- `name`: concise noun-phrase label (2–5 words typical).
- `description`: one sentence that **defines** the latent trait for a reader who has not seen the paper. Do NOT just restate the name — add real explanatory content (e.g. for "Calibration": "The degree to which the model's expressed confidence matches its actual accuracy across predictions").
- `source_snippets`: **non-empty list** of **verbatim quotes** from the paper, each optionally followed by a location reference like "(Sec. 3)". Keep to the relevant phrase or sentence. Do not paraphrase.

### 2. Behaviors — what you can observe the model doing

A behavior is an **observable action, output, or phenomenon the model exhibits** — both intentional task performance AND emergent/unintended behaviors. If you could write an evaluation script that directly checks whether the model is doing it, it is a behavior.

**Two kinds:**
1. **Task behaviors** — what the model is asked to do (code generation, question answering, translation); defined by input/output format.
2. **Non-task behaviors** — observable output patterns not defined by a task format: emergent phenomena (hallucination, sycophancy, memorization), failure modes (reward hacking, mode collapse, catastrophic forgetting), or other patterns (self-correction, verbose generation, refusal).

**Row-vs-column heuristic:** measurement instruments assess behaviors (rows); the latent trait being probed is a construct (column). A measurement instrument that *assesses* a behavior is not itself a behavior — do not use instrument names as behavior names.

**Examples to give you a flavor of behavior categories** (illustrative only — extract whatever the paper actually discusses, including things not listed here):
- *Generation:* text/code generation, translation, summarization, image captioning, dialogue
- *Comprehension:* question answering, reading comprehension, natural language inference, sentiment analysis
- *Structured output:* information extraction, NER, parsing, relation extraction
- *Interactive:* instruction following, tool use, multi-turn conversation, web navigation
- *Safety-related:* harmful-content refusal, jailbreak resistance, response under adversarial perturbation
- *Non-task patterns:* hallucination, sycophancy, memorization, reward hacking, mode collapse, refusal, self-correction

**Naming:** use generic, reusable task names that apply across papers — not paper-specific method names. Abstract paper framing to the community-standard name (e.g. "grade-school arithmetic solving" → "Mathematical problem solving"). Use noun/gerund form ("Code generation", not "Generates code"). Sentence case.

**Field requirements:**
- `name`: concise noun-phrase label (2–5 words typical).
- `description`: one sentence describing what the model observably does, concrete enough that someone could design an evaluation for it. Do NOT just restate the name.
- `source_snippets`: same rules as constructs — verbatim quotes, non-empty list.

### 3. Measurement instruments — how constructs and behaviors are assessed

A measurement instrument is any **named, reproducible procedure used to assess model capabilities or behaviors** — broader than benchmarks.

**Examples to give you a flavor of instrument categories** (illustrative only — extract whatever the paper actually uses, including things not listed here):
- *Benchmarks and datasets:* named test sets (MMLU, HumanEval, SQuAD, ImageNet, …)
- *Human evaluation protocols:* user studies, preference studies, Likert surveys, A/B tests, expert annotation, crowdsourced ratings, inter-annotator agreement
- *Standardized questionnaires and scales:* psychometric instruments, personality inventories, bias probes, Turing-test evaluations, red-teaming protocols
- *Evaluation suites:* HELM, BIG-Bench, lm-eval-harness, …
- *Domain-specific procedures:* clinical vignette evaluations, legal case analysis, simulation-based assessments

**Include** any instrument the paper uses or references that has a recognizable name or well-defined protocol, concrete enough to replicate.

**Exclude scoring functions/metrics entirely.** Metrics are *how you score*; instruments are *what you use to gather the data you score*. Exclude: accuracy, F1, BLEU, ROUGE, METEOR, BERTScore, MSE/MAE/RMSE, perplexity, pass@k, win rate, CIDEr, SPICE, EM, precision, recall, any "*-score" metric. Also exclude: evaluation settings (5-shot, zero-shot), training-only datasets, unnamed/ad-hoc test sets, and vague references ("our evaluation", "the test set").

**Naming:** use the community-standard short name (often an acronym). For unnamed human evaluations, use a descriptive label ("User preference study", "Expert annotation evaluation", "Red-teaming assessment"). Put the full name in `description`. Do not embed metric names or settings in the instrument name.

**Field requirements:**
- `name`: standard short name or descriptive label for the evaluation method.
- `description`: full name (if acronym) + one sentence on what domain/ability/task it assesses and how (format, modality, population). Self-contained.
- `source_snippets`: same rules as constructs — verbatim quotes, non-empty list.

## Self-Check

Before finalizing:
1. **Quote check:** every `source_snippets` entry must actually appear in the paper text. Delete or fix any that fail.
2. **Category check:** reapply the decision rules. Move latent traits misclassified as behaviors back to constructs; remove any metrics (accuracy, F1, BLEU, etc.) listed as instruments.
3. **Naming check:** would another researcher studying a different paper about the same ability/task use the same name? Normalize to community-standard terms.

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
  - measurement instrument ↔ measurement instrument (e.g. a benchmark suite contains a sub-benchmark, or two instruments measure overlapping domains)
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


SCREENING_PAPERS_PROMPT = """
You are a document classifier. Determine if the following paper is about large language model (LLM) capabilities, risks, evaluation, behavior, or tasks.

Answer "Yes" if the paper:
- Discusses LLM capabilities, risks, safety, fairness, understanding, benchmarks, performance, etc.
- Evaluates or measures LLMs (benchmarks, tasks, metrics).
- Addresses LLM behavior, risks, or real-world use.

Answer "No" if the paper is not about LLMs or does not address capabilities, risks, safety, fairness, understanding, benchmarks, performance, etc.

Respond with exactly one word: Yes or No.

Response:
"""


_SHARED_MERGE_PRINCIPLE = """**The principle:** two names refer to the same concept when a domain expert would use them interchangeably in a paper. If you can swap one for the other in a sentence and the meaning is unchanged, they are the same concept and should merge. If the swap would change the meaning, scope, or specificity, they are different concepts and should stay separate.

In practice, this means **merging surface variants** (different ways of writing the same idea) and **keeping conceptual variants separate** (different ideas, even if related).

A few illustrative examples — extrapolate the spirit, don't treat as an exhaustive checklist:

- *Surface variants → merge*: hyphenation/spacing ("Multi-step" / "Multistep" / "Multi step"), grammatical inflection ("ability" / "abilities" / "capability" / "capabilities"), morphology ("Logical" / "Logic"), interchangeable synonyms ("understanding" / "comprehension" / "awareness"), equivalent prefixes (e.g. "Multimodal" / "Cross-modal"), rephrasings of the same idea ("Alignment with human preferences" / "Preference alignment").

- *Conceptual variants → keep separate*: hierarchical relationships ("Reasoning" vs "Mathematical reasoning"), distinct facets ("Mathematical reasoning" vs "Commonsense reasoning"), different domains ("Legal reasoning" vs "Medical reasoning"), different cognitive modes ("Deductive" vs "Inductive" vs "Abductive"), qualified/scoped variants vs bare parent ("Adversarial robustness" vs "Robustness").

When two surface forms differ only in trivial ways (filler words like "ability"/"capability"/"capacity"/"skill" — singular or plural — that don't change the concept; whitespace; punctuation; case; common synonym verbs), strongly prefer to merge. Save the "keep separate" judgment for cases where the underlying concepts genuinely differ."""


AGGREGATE_CONSTRUCTS_PROMPT = (
    """Deduplicate constructs (latent LLM capabilities, risks, traits) by grouping rows that name the **same concept** under different wording.

Each input row has an `id`. Output only the grouping as `{canonical_name: [ids]}`. All metadata (definitions, papers, snippets) is resolved from the IDs programmatically — do NOT repeat them.

**Canonical name:** concise, community-standard noun phrase, sentence case. When several surface forms collapse to one concept, pick the bare form a domain expert would use in writing — strip filler words like "ability"/"capability" when they're separable, but keep them when they're integral to the term ("Interpretability", "Scalability").

"""
    + _SHARED_MERGE_PRINCIPLE
    + """

**Output format:**
```json
{"groups": {"Reasoning": [0, 3, 7, 11], "Logical reasoning": [5]}, "ungrouped": [12]}
```
`ungrouped` lists IDs that don't merge with anything else. Every input ID must appear exactly once.

**Input rows:**
{constructs_json}

Return only the JSON object."""
)


AGGREGATE_MEASUREMENTS_PROMPT = (
    """Deduplicate measurement instruments (benchmarks, datasets, user studies, surveys, human evaluations, and other named evaluation procedures) by grouping rows that refer to the **same instrument** under different names. Do NOT merge or split based on reported metrics or scores.

Each input row has an `id`. Output only the grouping as `{canonical_name: [ids]}`. All metadata is resolved from the IDs programmatically — do NOT repeat descriptions, papers, or snippets.

**Canonical name:** community-standard short name of the instrument (e.g. "MMLU", "HumanEval", "HELM Math"). Name the instrument only — never the metric ("MMLU Accuracy" → "MMLU"). Include a subset qualifier when the input row is about a specific subset. For human evaluations, use a descriptive label that captures the method.

"""
    + _SHARED_MERGE_PRINCIPLE
    + """

**Instrument-specific notes:** acronym↔full-name pairs ("MMLU" ≡ "Massive Multitask Language Understanding") merge; procedural rephrasings of the same evaluation method merge. But subsets, distribution-shift variants, and different experimental conditions are *different* instruments — keep them separate (e.g. "MMLU Math" ≠ "MMLU"; "ImageNet-A" ≠ "ImageNet"; "User preference study" ≠ "Expert annotation evaluation").

**Output format:**
```json
{"groups": {"MMLU": [0, 4], "HumanEval": [2], "User preference study": [6, 9]}, "ungrouped": [1, 3, 5]}
```
`ungrouped` lists IDs that don't merge with anything else. Every input ID must appear exactly once.

**Input rows:**
{measurements_json}

Return only the JSON object."""
)


AGGREGATE_BEHAVIORS_PROMPT = (
    """Deduplicate behaviors (observable tasks, outputs, performance outcomes, and non-task observable phenomena like hallucination, sycophancy, memorization — not latent constructs, not measurement instruments) by grouping rows that name the **same observable behavior** under different wording.

Each input row has an `id`. Output only the grouping as `{canonical_name: [ids]}`. All metadata is resolved from the IDs programmatically — do NOT repeat definitions, papers, or snippets.

**Canonical name:** concise, community-standard noun phrase, sentence case (e.g. "Code generation", "Question answering", "Hallucination").

"""
    + _SHARED_MERGE_PRINCIPLE
    + """

**Behavior-specific notes:** the *core action* is what makes a behavior distinctive — predicting, generating, classifying, retrieving, refusing, etc. are different behaviors even when applied to the same target. Specific task instances aren't the same as their generic umbrella ("Moving a sliding door" ≠ "Task completion"). Different methods/strategies for the same outcome are different behaviors.

**Output format:**
```json
{"groups": {"Code generation": [0, 4], "Question answering": [2]}, "ungrouped": [1, 3, 5]}
```
`ungrouped` lists IDs that don't merge with anything else. Every input ID must appear exactly once.

**Input rows:**
{behaviors_json}

Return only the JSON object."""
)


def build_aggregate_grouping_prompt(
    node_type: str,
    nodes_json: str,
    existing_mapping_json: str = "",
) -> str:
    """Full user prompt for one AGGREGATE_* grouping call.

    When *existing_mapping_json* is non-empty, a preamble is prepended that
    shows the LLM which names already have canonical forms so it can merge
    new names into existing canonical groups (or revise them).
    """
    if node_type == "constructs":
        base = AGGREGATE_CONSTRUCTS_PROMPT.replace(
            "{constructs_json}", nodes_json
        )
    elif node_type == "measurements":
        base = AGGREGATE_MEASUREMENTS_PROMPT.replace(
            "{measurements_json}", nodes_json
        )
    elif node_type == "behaviors":
        base = AGGREGATE_BEHAVIORS_PROMPT.replace(
            "{behaviors_json}", nodes_json
        )
    else:
        raise ValueError(
            f"Unknown node_type for aggregate grouping: {node_type}"
        )

    if existing_mapping_json:
        mapping_ctx = (
            "\n\n**Existing name mapping (original → canonical) from prior runs.**\n"
            "Use these as a starting point: prefer reusing these canonical names when "
            "a node clearly refers to the same concept.  You may revise or merge "
            "canonical names if the evidence warrants it.\n\n"
            f"```json\n{existing_mapping_json}\n```\n"
        )
        base = mapping_ctx + "\n" + base

    return base


MERGE_GROUPS_PROMPT = (
    """You are merging groups of {node_type} that were extracted from many academic papers and grouped in separate batches. Your job is to identify groups that refer to the same concept and merge them.

Each input group has an `id`. Output only the merge mapping as `{{canonical_name: [ids]}}`. All metadata (definitions, papers, snippets) is resolved from the IDs programmatically — do NOT repeat them.

**Canonical name:** concise, community-standard noun phrase, sentence case. For measurement instruments, include subset qualifier when applicable.

"""
    + _SHARED_MERGE_PRINCIPLE
    + """

**Output format:**
```json
{{"groups": {{"Reasoning": [0, 3, 7], "Mathematical reasoning": [1, 9], "MMLU": [2, 5]}}, "ungrouped": [4, 6]}}
```
`groups` maps each canonical name to the list of input IDs that merge under it. `ungrouped` lists IDs that don't merge with anything else. Every input ID must appear exactly once across groups + ungrouped. A single-member group (e.g. `"Foo": [12]`) is fine when you want to pick the canonical name for it.

**Input groups:**
{groups_json}

Return only the JSON object."""
)


CHARACTERIZE_ENTITIES_PROMPT = """You are characterizing one entity from a nomological network of LLM research. You receive:
- its **canonical name** and **type** (construct, behavioral indicator, or measurement instrument)
- every **original definition** extracted from different papers (with paper titles)
- every **source snippet** (verbatim quotes from papers)
- every **relationship** this entity participates in: its type (measured_by, causes, correlates or related), direction, the papers that claim it, and evidence quotes
- **stats**: counts computed by the pipeline (how many measurement instruments, behavioral indicators and constructs the entity is linked to, with the most frequently linked ones listed first)

**STRICT SCOPE (HARD CONSTRAINT): use ONLY the evidence given in this prompt. Do not use prior knowledge, and do not interpret.**
- **No prior knowledge.** Do not draw on anything you know about the field, the entity, the benchmarks, the models or the papers, even when you are confident it is true. Do NOT add historical context, well-known facts, or general intuition that isn't present.
- **No interpretation.** Report what the papers say, in their terms. Do not add explanations, motivations, implications, trends, assessments of quality, or conclusions the evidence does not state: for example, do not say why papers disagree, that a concept is under-studied or maturing, or that an instrument is popular beyond what the counts show.
- **Traceable claims.** Every claim must be supported by a definition, snippet, relationship or number in the input for this entity. If the data is sparse, the summary should be short and faithful; do not pad it.
- **Counts as given.** Report the numbers in **stats** as given; never compute, estimate or round counts yourself. Do not report numbers of papers or of surface names: say how common something is in words ("most papers", "many", "a few", "one paper").

Your task: write a **summary of use** for this entity that is concise but has good coverage, and reads as a mini literature review, synthesizing how the field defines, operationalizes, and relates to this concept **strictly as represented in the provided data**.

**Throughout:** frequency-based framing wins over absolute claims. Say which framings are most common and which are minority or contested, using language like "the prevailing usage is…", "a smaller line of work treats it as…", "most papers…, though some…", "almost all papers in this set…", "only a few authors…".

{type_guidance}

**Relationships: use their recorded language.**
- Each relationship in the input records what papers claim about the link: its type, its direction and the papers that make the claim. Describe links in those terms and attribute them to the papers: "measured_by" as "is measured by" (or, for an instrument, "measures"); "causes" as "papers claim a causal relationship from X to Y" (the effect may be positive or negative, so never write "X causes Y", "X improves Y" or "X drives Y" unless the evidence quote itself states the direction of the effect); "correlates" as "is reported to correlate with"; "related" as "is related to".
- Keep each link's type and direction as recorded. Do not turn a "related" link into a causal claim, and do not soften a causal relationship into an association. Say how widely a link is claimed in words ("several papers claim…", "one paper reports…"), not with paper counts.

**Writing style:**
- Write as a field synthesis, NOT as a dictionary definition. Use language like "most commonly described as…", "some authors define it as…, though the prevailing usage is…", "across the surveyed work, the dominant framing is…".
- **Tone: descriptive and neutral (HARD CONSTRAINT).** NEVER use the words "crucial", "important", "essential", "significant", or "key", even when paraphrasing a paper. Replace with frequency-based alternatives: "commonly", "widely", "frequently", "prevalent", "a recurring theme", "a popular instrument". If a paper says something is "crucial", paraphrase as "widely discussed" or "commonly targeted".
- Weave in **specific evidence**: quote or paraphrase findings from the source snippets when they illuminate how the concept is used (e.g. "As one study notes, '…' (Paper Title)"). Name at most two paper titles in the whole summary, and keep each title clearly separated from your own text.
- Write each section as one short paragraph of plain prose, usually two to four sentences. No lists, no headings, and no section labels inside the text (the labels are added when the summary is displayed). Never use em dashes (—); use commas, colons or parentheses instead.
- Be selective: name at most the five most frequent measurement instruments, behavioral indicators or linked constructs in a section, most frequent first, and summarize the rest by count ("and 23 other instruments"). Do not list single-paper links one by one unless there are only a few links in total.
- If nothing of a kind is linked, say so in words ("no measurement instrument is linked to it") rather than as a zero.
- Write about the papers directly. Never refer to the input, the stats, the data, the pipeline, "this set" or "the provided snippets"; write "papers" or "definitions" instead.
- For entities with only one source paper, still provide a faithful description from all available data; do not pretend a single-paper concept is well-established.
- Do NOT start the first section with "X is…" as a flat definition. Start with how the field treats the concept.

Be precise and grounded in the evidence. Do not invent information not present in the inputs. If you cannot support a claim with something from the provided definitions/snippets/relationships, do not make the claim.

**Output format:** a JSON object with exactly the fields named in the list of what to cover above, each holding that section's text. Use an empty string for a section the input gives nothing for; do not fill it with a statement that there is no evidence.

Return ONLY the JSON object.

**Entity to characterize:**
{entities_json}

---

**Self-check before returning (do this silently; only emit the final JSON):**
1. Re-read every sentence of your draft characterization.
2. For each claim, locate the specific definition, snippet, or relationship in the input that supports it. If you cannot point to one, REMOVE the claim or rewrite it to match what the data actually says.
3. Confirm you did not import outside knowledge or add interpretation: no historical context, no well-known facts about the field/benchmark/concept that aren't in the input, no general intuition, no statistics or numbers that aren't present, and no explanations, implications or judgments the papers do not state.
4. Confirm frequency-based language is used wherever you describe how common a framing is (no "crucial", "important", "essential", "significant", "key").
5. Confirm every link is described with its recorded type and direction, and attributed to the papers that claim it.
6. Confirm every number appears in **stats**, no numbers of papers or surface names are reported, at most two paper titles are named, and there are no em dashes (replace any with commas, colons or parentheses).
7. Confirm the summary is concise: cut repetition across sections and anything the reader does not need, but keep coverage of every point in the list of what to cover.
8. Confirm the JSON has exactly the listed fields, with no labels or headings inside the text.
9. Confirm each section is selective (at most five named items, the rest by count) and never mentions the input, stats, data or pipeline.
Then return the final JSON."""


# Type-specific part of CHARACTERIZE_ENTITIES_PROMPT, filled into {type_guidance}
# by entity type (keys match the network's entity lists).
CHARACTERIZE_TYPE_GUIDANCE = {
    "constructs": """**What to cover for a construct (a latent ability, trait or property), in this order and as far as the evidence allows:**
1. **Definitions** (field `definition`). The dominant framing first, with a sense of how widespread it is, then the competing framings. Say where papers agree and where they disagree, and name the axis of disagreement when the definitions themselves differ along it (for example latent ability vs observable behavior, narrow vs broad scope, property of the model vs property of its outputs, different reference standards).
2. **Systematization** (field `systematization`). The facets or subtypes papers break it into; the constructs it is equated with, nested under, or contrasted against; places where papers use one name for different things, or different names for the same thing.
3. **Operationalization** (field `measurement`). The space of measurement: how many measurement instruments and behavioral indicators it is linked to (from **stats**), the ones used most often, what kinds of instruments they are (benchmarks, human evaluation, LLM-as-a-judge, probes or analyses), and whether these operationalizations line up with the definitions or diverge from them. Make the operationalization explicit; do not leave it abstract.
4. **Links** (field `links`). What papers claim it has a causal relationship with, correlates with, or is related to.

Return: {"definition": "...", "systematization": "...", "measurement": "...", "links": "..."}""",
    "behaviors": """**What to cover for a behavioral indicator (an observable task or output pattern), in this order and as far as the evidence allows:**
1. **What counts as the behavioral indicator** (field `definition`). The task formulations and success criteria papers use, the most common first. Say where papers agree and where they differ (for example task scope, what output counts as success, who or what judges it).
2. **Variants** (field `variants`). The sub-tasks, settings, domains or modalities papers study, and the names papers use for it.
3. **Elicitation and scoring** (field `measurement`). How many measurement instruments elicit or score it (from **stats**), the ones used most often, and what kinds of instruments they are.
4. **What it is evidence of** (field `evidence_of`). The constructs papers take it to indicate (from **stats**), and whether papers agree on which construct it reflects.

Return: {"definition": "...", "variants": "...", "measurement": "...", "evidence_of": "..."}""",
    "measurements": """**What to cover for a measurement instrument (a benchmark, dataset or evaluation protocol), in this order and as far as the evidence allows:**
1. **What it is** (field `description`). Its format and content, and any versions or subsets, as the definitions describe them. Note where papers describe it differently.
2. **What it is claimed to measure** (field `measures`). How many constructs and behavioral indicators it is linked to (from **stats**), the ones it is most often used for, and whether those claims converge on one construct or spread across many. Be specific about the connection ("papers use it to measure …", "it is reported as evaluating …").
3. **How it is used** (field `usage`). The instruments it is used alongside, and how papers position it (for example a headline benchmark or an auxiliary check), as far as the input shows.
4. **Concerns** (field `concerns`). Concerns papers raise about it, such as contamination, saturation or validity, only if they appear in the input.

Return: {"description": "...", "measures": "...", "usage": "...", "concerns": "..."}""",
}


# Section fields of each type's summary, in display order, with the label shown before
# each paragraph on the entity page (aiconstructlexis.summarize.characterize joins them).
CHARACTERIZE_SECTION_LABELS = {
    "constructs": [("definition", "Space of definitions."), ("systematization", "Space of facets."),
                   ("measurement", "Space of measurement."), ("links", "Links.")],
    "behaviors": [("definition", "Space of definitions."), ("variants", "Variants."),
                  ("measurement", "Space of elicitation and scores."), ("evidence_of", "What it is taken as evidence of.")],
    "measurements": [("description", "What it is."), ("measures", "What it is claimed to measure."),
                     ("usage", "Space of uses."), ("concerns", "Concerns raised.")],
}

