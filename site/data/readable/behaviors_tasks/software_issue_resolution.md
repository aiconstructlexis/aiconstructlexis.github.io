# Software issue resolution
**Type:** Behavioral indicator  
**Supporting papers:** 3  
**Also known as:** Issue resolution  

## State of the Field

**Space of definitions.** The definition treats this behavior as an end-to-end software fixing task: a model receives a software issue described in natural language and succeeds only if it produces a fix that results in a passing test suite. Quoted passages describe this operationally as generating patches that successfully resolve issues, and papers report performance in terms of issue resolution rate.

**Variants.** The reported settings are SWE-bench Lite, described as a more self-contained evaluation of functional bug fixes, and SWE-bench Verified. Across these settings, the task remains framed as resolving natural-language-described issues by producing patches that fix them.

**Space of elicitation and scores.** Papers measure this behavior with 2 instruments, most often SWE-bench Lite and also SWE-bench Verified. These instruments are used to report issue resolution rate, and SWE-bench Lite is described as a 300-instance subset intended to provide a more self-contained evaluation of functional bug fixes.

**What it is taken as evidence of.** The papers do not link this behavior to any construct.

## Sources

**Issue resolution** (1 paper: [Nemotron-CORTEXA: Enhancing LLM Agents for Software Engineering Tasks via Improved Localization and Solution Diversity](https://raw.githubusercontent.com/mlresearch/v267/main/assets/sohrabizadeh25a/sohrabizadeh25a.pdf))
> The end-to-end task of successfully fixing a software issue described in natural language, resulting in a passing test suite.

## Relationships

### Software issue resolution →
- **SWE-bench Lite** (measurement instrument): *measured_by*, 2 papers
  > We conduct our experiments on SWE-Bench Lite, a 300-instance subset sampled from the full SWE-Bench for providing a more self-contained evaluation of functional bug fixes (Jimenez et al., 2024).
  - [Diversity Empowers Intelligence: Integrating Expertise of Software Engineering Agents](https://proceedings.iclr.cc/paper_files/paper/2025/file/d7b50b8ac2c781a12f26155f48310d8d-Paper-Conference.pdf)
  - [Nemotron-CORTEXA: Enhancing LLM Agents for Software Engineering Tasks via Improved Localization and Solution Diversity](https://raw.githubusercontent.com/mlresearch/v267/main/assets/sohrabizadeh25a/sohrabizadeh25a.pdf)
- **SWE-bench Verified** (measurement instrument): *measured_by*, 1 paper
  > NEMOTRON-CORTEXA achieves an issue resolution rate of 42.00% on the SWE-bench Lite and 52.60% on SWE-bench Verified, while costing only $0.51 per instance. (Section 1)
  - [Nemotron-CORTEXA: Enhancing LLM Agents for Software Engineering Tasks via Improved Localization and Solution Diversity](https://raw.githubusercontent.com/mlresearch/v267/main/assets/sohrabizadeh25a/sohrabizadeh25a.pdf)
