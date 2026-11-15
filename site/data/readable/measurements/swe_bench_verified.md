# SWE-bench Verified
**Type:** Measurement instrument  
**Supporting papers:** 8  
**Also known as:** SWE-Bench Verified  

## State of the Field

**What it is.** Most commonly described as a vetted subset of SWE-Bench, it contains 500 instances or samples that were further checked by human annotators. One definition emphasizes manual verification by professional software developers for appropriately scoped unit tests and well-specified issue descriptions, while another describes it more broadly as a benchmark dataset for automatically resolving software engineering issues; a quoted passage also says the vetted samples were verified to be non-problematic.

**What it is claimed to measure.** Across the linked claims, papers use it to measure Software issue resolution, for example by reporting an issue resolution rate on SWE-bench Verified. The claims converge on a single behavioral indicator: it is linked to one behavioral indicator, Software issue resolution, and no constructs.

**Space of uses.** Papers position it as a benchmark for automatically resolving software engineering issues. No measurement instruments are linked to it, and one source explicitly calls it "the most popular benchmark" for that task while another says it was introduced to improve the robustness and reliability of evaluation.

**Concerns raised.** The recurring concern is evaluation quality. Papers describe the benchmark as a manually vetted subset released to improve robustness and reliability, with instances checked to be non-problematic and to have appropriately scoped unit tests and well-specified issue descriptions.

## Sources

**SWE-Bench Verified** (1 paper: [UTBoost: Rigorous Evaluation of Coding Agents on SWE-Bench](https://aclanthology.org/2025.acl-long.189.pdf))
> A curated subset of 500 SWE-Bench samples that were manually verified by professional software developers to have appropriately scoped unit tests and well-specified issue descriptions.

**SWE-bench Verified** (1 paper: [Otter: Generating Tests from Issues to Validate SWE Patches](https://raw.githubusercontent.com/mlresearch/v267/main/assets/ahmed25b/ahmed25b.pdf))
> A benchmark dataset for automatically resolving software engineering issues, consisting of 500 instances vetted by human annotators.

## Relationships

### → SWE-bench Verified
- **Software issue resolution** (behavioral indicator): *measured_by*, 1 paper
  > NEMOTRON-CORTEXA achieves an issue resolution rate of 42.00% on the SWE-bench Lite and 52.60% on SWE-bench Verified, while costing only $0.51 per instance. (Section 1)
  - [Nemotron-CORTEXA: Enhancing LLM Agents for Software Engineering Tasks via Improved Localization and Solution Diversity](https://raw.githubusercontent.com/mlresearch/v267/main/assets/sohrabizadeh25a/sohrabizadeh25a.pdf)
