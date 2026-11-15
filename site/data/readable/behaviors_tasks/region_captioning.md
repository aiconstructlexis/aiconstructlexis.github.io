# Region captioning
**Type:** Behavioral indicator  
**Supporting papers:** 7  
**Also known as:** Region-level captioning, Referring description, Visual referring  

## State of the Field

**Space of definitions.** Across definitions, region captioning is most commonly described as producing a natural-language description for a specific image region that has been marked or referred to in the input. The papers agree that the output is region-specific text, but differ on brevity: some formulations ask for concise or brief descriptions, including prompts to "provide a brief description of each marked region in the image", while others ask for a detailed description of a referred region. One formulation also defines it as a task where the model "provides a textual description corresponding to a visual prompt".

**Variants.** The behavior appears under several names, most commonly region-level captioning, with referring description and visual referring as alternative labels. The studied settings vary between marked regions, visually prompted regions, and referred regions, and between describing each marked region versus one referred region. One paper also situates region-level captioning within MDVP-Bench alongside point-level captioning.

**Space of elicitation and scores.** Papers link region captioning to 3 measurement instruments. The most frequently linked are RefCOCOg and Visual Genome, which papers describe as established region captioning benchmarks and use to assess "region-level caption ability"; Ferret-Bench is also linked, through its Referring Description and Referring Reasoning tasks. Across these instruments, the measurement takes the form of benchmark evaluation of generated descriptions for designated regions.

**What it is taken as evidence of.** Rather than converging on a single construct it reflects, papers relate region captioning to 2 constructs. The prevailing link is to Region-level understanding: papers say region captioning is used to access "region understanding capabilities" or assess a model's "ability of region-level understanding". A smaller line of work relates it to Visual grounding, described as the counterpart task to visual referring.

## Sources

**Region-level captioning** (1 paper: [Draw-and-Understand: Leveraging Visual Prompts to Enable MLLMs to Comprehend What You Want](https://proceedings.iclr.cc/paper_files/paper/2025/file/727658ad24ba28e02dffd379bdc69448-Paper-Conference.pdf))
> Generating concise or detailed natural language descriptions for specific marked regions in an image.

**Referring description** (1 paper: [Draw-and-Understand: Leveraging Visual Prompts to Enable MLLMs to Comprehend What You Want](https://proceedings.iclr.cc/paper_files/paper/2025/file/727658ad24ba28e02dffd379bdc69448-Paper-Conference.pdf))
> An observable task, evaluated on Ferret-Bench, where the model provides a textual description corresponding to a visual prompt.

**Visual referring** (1 paper: [ClawMachine: Learning to Fetch Visual Tokens for Referential Comprehension](https://proceedings.iclr.cc/paper_files/paper/2025/file/b1abd42eb5aace7f0ad9ba9cfb029f54-Paper-Conference.pdf))
> Given an image and a referred region, the model produces a detailed natural-language description of that region.

## Relationships

### Region captioning →
- **RefCOCOg** (measurement instrument): *measured_by*, 3 papers
  > To assess the region-level caption ability, we also evaluate ASM on the Visual Genome (Krishna et al., 2017) and RefCOCOg (Mao et al., 2016).
  - [The All-Seeing Project: Towards Panoptic Visual Recognition and Understanding of the Open World](https://proceedings.iclr.cc/paper_files/paper/2024/file/68a3919db3858f548dea769f2dbba611-Paper-Conference.pdf)
  - [ClawMachine: Learning to Fetch Visual Tokens for Referential Comprehension](https://proceedings.iclr.cc/paper_files/paper/2025/file/b1abd42eb5aace7f0ad9ba9cfb029f54-Paper-Conference.pdf)
  - [Draw-and-Understand: Leveraging Visual Prompts to Enable MLLMs to Comprehend What You Want](https://proceedings.iclr.cc/paper_files/paper/2025/file/727658ad24ba28e02dffd379bdc69448-Paper-Conference.pdf)
- **Visual Genome** (measurement instrument): *measured_by*, 2 papers
  > To assess the region-level caption ability, we also evaluate ASM on the Visual Genome (Krishna et al., 2017) and RefCOCOg (Mao et al., 2016).
  - [The All-Seeing Project: Towards Panoptic Visual Recognition and Understanding of the Open World](https://proceedings.iclr.cc/paper_files/paper/2024/file/68a3919db3858f548dea769f2dbba611-Paper-Conference.pdf)
  - [ClawMachine: Learning to Fetch Visual Tokens for Referential Comprehension](https://proceedings.iclr.cc/paper_files/paper/2025/file/b1abd42eb5aace7f0ad9ba9cfb029f54-Paper-Conference.pdf)
- **Ferret-Bench** (measurement instrument): *measured_by*, 1 paper
  > Experiments are conducted on the Referring Description and Referring Reasoning tasks within Ferret-Bench, with the results presented in Table 3.
  - [Draw-and-Understand: Leveraging Visual Prompts to Enable MLLMs to Comprehend What You Want](https://proceedings.iclr.cc/paper_files/paper/2025/file/727658ad24ba28e02dffd379bdc69448-Paper-Conference.pdf)

### Associated with
- **Region-level understanding** (construct), 2 papers
  > "Region Captioning. To access the region understanding capabilities of VisionLLM v2, we evaluate our models on two prominent benchmarks: RefCOCOg [126] and Visual Genome [86]."
  - [VisionLLM v2: An End-to-End Generalist Multimodal Large Language Model for Hundreds of Vision-Language Tasks](https://proceedings.neurips.cc/paper_files/paper/2024/file/81a60d18e010b27b36cd465c6604b915-Paper-Conference.pdf)
  - [ClawMachine: Learning to Fetch Visual Tokens for Referential Comprehension](https://proceedings.iclr.cc/paper_files/paper/2025/file/b1abd42eb5aace7f0ad9ba9cfb029f54-Paper-Conference.pdf)
- **Visual grounding** (construct), 1 paper
  > Next, we study visual grounding, a.k.a. referring expression comprehension (REC), the counterpart task to visual referring that requires the model to identify the location of an object with language descriptions.
  - [ClawMachine: Learning to Fetch Visual Tokens for Referential Comprehension](https://proceedings.iclr.cc/paper_files/paper/2025/file/b1abd42eb5aace7f0ad9ba9cfb029f54-Paper-Conference.pdf)
