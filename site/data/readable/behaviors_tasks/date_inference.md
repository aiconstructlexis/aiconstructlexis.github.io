# Date inference
**Type:** Behavioral indicator  
**Supporting papers:** 4  
**Also known as:** Date deduction, Date calculation, Date arithmetic, Weekday understanding, Date reasoning  

## State of the Field

**Space of definitions.** Across the surveyed work, the prevailing usage treats date inference as inferring a calendar date from context or natural-language descriptions, usually while accounting for calendar structure and date arithmetic. Definitions repeatedly describe deducing a date from a given context, and one description frames it as inferring dates from language while performing arithmetic operations on dates and using knowledge such as the number of days in February. Some papers broaden the behavior to reasoning over weekdays, multi-day spans, and valid scheduling windows, while others frame success as correctly interpreting and calculating dates or weekdays.

**Variants.** Papers use several nearby names for this behavior, including date deduction, date inference, date calculation, date arithmetic, and weekday understanding. The main variants are natural-language date understanding, arithmetic from a given base date, and longer calendar problems centered on weekdays, dates, and multi-day spans; one description says that long problems focus on "weekday understanding and calculations involving dates." Another variant studies addition and subtraction of days, weeks, and months under various token fragmentation settings.

**Space of elicitation and scores.** Papers link this behavior to 1 measurement instrument, Date Understanding. In the recorded relationship, date inference is measured by this instrument, which is described as a task involving inferring dates from natural-language descriptions and performing arithmetic operations on dates.

**What it is taken as evidence of.** Papers do not link this behavior to any construct as what it indicates.

## Sources

**Date deduction** (1 paper: [StrategyLLM: Large Language Models as Strategy Generators, Executors, Optimizers, and Evaluators for Problem Solving](https://proceedings.neurips.cc/paper_files/paper/2024/file/af7cc9e2366b8f8837a6ef339810277a-Paper-Conference.pdf))
> Inferring a calendar date from contextual clues and relative time offsets.

**Date inference** (1 paper: [Buffer of Thoughts: Thought-Augmented Reasoning with Large Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/cde328b7bf6358f5ebb91fe9c539745e-Paper-Conference.pdf))
> Inferring a date from a natural-language description while accounting for calendar structure and date arithmetic.

**Date calculation** (1 paper: [TCP: a Benchmark for Temporal Constraint-Based Planning](https://aclanthology.org/2025.emnlp-main.1142.pdf))
> Reasoning over calendar dates, weekdays, and multi-day spans to determine valid scheduling windows.

**Date arithmetic** (1 paper: [Date Fragments: A Hidden Bottleneck of Tokenization for Temporal Reasoning](https://aclanthology.org/2025.emnlp-main.159.pdf))
> The task of performing calculations such as addition or subtraction of days, weeks, or months from a given base date.

**Weekday understanding** (1 paper: [TCP: a Benchmark for Temporal Constraint-Based Planning](https://aclanthology.org/2025.emnlp-main.1142.pdf))
> The observable task of correctly interpreting and performing calculations involving days of the week and dates.

## Relationships

### Date inference →
- **Date Understanding** (measurement instrument): *measured_by*, 1 paper
  > “DateUnderstanding—a task that involves inferring dates from natural language descriptions, performing arithmetic operations on dates”
  - [Buffer of Thoughts: Thought-Augmented Reasoning with Large Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/cde328b7bf6358f5ebb91fe9c539745e-Paper-Conference.pdf)
