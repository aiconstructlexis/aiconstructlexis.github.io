# Image-to-text generation
**Type:** Behavioral indicator  
**Supporting papers:** 5  
**Also known as:** Image-grounded text generation  

## State of the Field

**Space of definitions.** Across papers, the prevailing usage treats this behavior as generating text from an input image, most commonly as a description or response based on that image. Definitions range from generating descriptions for input images to broader formulations that include conversation, detailed description, and complex reasoning. A smaller line of work makes the text input explicit, defining the task as producing a relevant and coherent response from an image plus an optional prompt, or as a response conditioned on and consistent with both an input image and a textual query.

**Variants.** Papers use several closely related names, including image-to-text generation, Image2Text, image-to-text (I2T) generation, and image-grounded text generation. The studied forms span plain image description, instruction-following or conversational responses, and broader responses involving detailed description or complex reasoning; one paper instantiates this as a Chinese-English bilingual multimodal chatbot responding to user instructions based on the input image. Some settings also pair the image with user-provided text or a textual query, and one paper treats it as a practical multimodal use case with LLaVA-like models.

**Space of elicitation and scores.** No measurement instrument is linked to it, so the papers do not identify a commonly linked instrument for eliciting or scoring this behavior.

**What it is taken as evidence of.** No construct is linked to it, so the papers do not explicitly relate this behavior to a named construct.

## Sources

**Image-to-text generation** (3 papers: [Large Multilingual Models Pivot Zero-Shot Multimodal Learning across Languages](https://proceedings.iclr.cc/paper_files/paper/2024/file/bd54a6d4dc60c82ae989154013e17754-Paper-Conference.pdf), [MixEval-X: Any-to-any Evaluations from Real-world Data Mixture](https://proceedings.iclr.cc/paper_files/paper/2025/file/6de2e84b8da47bb2eb5e2ac96c63d2b0-Paper-Conference.pdf), [Data-Juicer Sandbox: A Feedback-Driven Suite for Multimodal Data-Model Co-development](https://raw.githubusercontent.com/mlresearch/v267/main/assets/chen25bm/chen25bm.pdf))
> Producing textual descriptions or responses based on input images, including conversation, detailed description, and complex reasoning.

**Image-grounded text generation** (1 paper: [Look Twice Before You Answer: Memory-Space Visual Retracing for Hallucination Mitigation in Multimodal Large Language Models](https://raw.githubusercontent.com/mlresearch/v267/main/assets/zou25e/zou25e.pdf))
> The task of generating a textual response that is conditioned on and consistent with a given input image and a textual query.
