# Token diversity
**Type:** Construct  
**Supporting papers:** 3  
**Also known as:** Token Diversity  

## State of the Field

**Space of definitions.** Across the surveyed work, the prevailing usage treats token diversity as variation in the distribution of generated tokens, especially as the opposite of repetitive output. Papers also describe it with entropy language, defining it as the degree of variation or entropy in model-produced tokens and, in one formulation, as reflecting the richness of the output distribution.

**Space of facets.** Papers do not introduce named subtypes or a larger taxonomy for this construct. The main distinctions in use are between varied and repetitive token distributions, and some descriptions pair token diversity closely with token entropy and with the richness of the output distribution rather than separating these as different constructs.

**Space of measurement.** No measurement instrument or behavioral indicator is linked to it. Even so, papers describe metric-based operationalization: a paper says it introduces "three additional metrics that evaluate token diversity," and names Token Entropy (TE) as measuring the diversity of tokens in the model's output. This operationalization targets the same token-level variation and entropy emphasized in the definitions.

**Links.** The only linked construct is Text generation quality. A paper claims a causal relationship from token diversity to text generation quality, reporting that quality is "compromised by low token diversity."

## Sources

**Token diversity** (1 paper: [A Closer Look at Machine Unlearning for Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/7b7db41ea66d624587f211aa15c07e45-Paper-Conference.pdf))
> The extent to which generated output uses a varied token distribution rather than repetitive tokens.

**Token Diversity** (1 paper: [Masked Diffusion Models are Secretly Time-Agnostic Masked Models and Exploit Inaccurate Categorical Sampling](https://proceedings.iclr.cc/paper_files/paper/2025/file/9e3b203e72c4e058de26d02a92a81844-Paper-Conference.pdf))
> The degree of variation and entropy in the tokens produced by the model during generation, reflecting the richness of the output distribution.

## Relationships

### Token diversity →
- **Text generation quality** (construct): *causes*, 1 paper
  > However, when we check the generated content, we discover that the quality is compromised by low token diversity
  - [Masked Diffusion Models are Secretly Time-Agnostic Masked Models and Exploit Inaccurate Categorical Sampling](https://proceedings.iclr.cc/paper_files/paper/2025/file/9e3b203e72c4e058de26d02a92a81844-Paper-Conference.pdf)
