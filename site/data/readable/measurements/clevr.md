# CLEVR
**Type:** Measurement instrument  
**Supporting papers:** 5  

## State of the Field

**What it is.** Across papers, the prevailing description is a visual reasoning benchmark or diagnostic dataset for compositional language and elementary visual reasoning. Some authors frame it differently in use: as an image classification task, as a scene reasoning domain for inductive program synthesis, or as an image-based dataset for multimodal data understanding and retrieving. One definition specifically uses the val split, described as containing 15,000 images with cylinders, cubes, and spheres that vary in number, size, and color.

**What it is claimed to measure.** Claims about what it measures are narrow. Papers link it to 1 construct and no behavioral indicators, and the only recorded measurement claim is that it measures Complex reasoning: one paper refers to "complex reasoning in CLEVR" when using it alongside Winoground. Across papers, measurement claims center on a single construct rather than multiple targets.

**Space of uses.** Papers use it in several roles rather than a single fixed protocol. It appears alongside SVHN and EuroSAT in image classification experiments, alongside REGEX and LOGO as one of three inductive program synthesis domains, and as a multimodal data understanding and retrieval dataset on the val split. Other papers position it more generally as a reasoning benchmark or challenge, including references to "the popular CLEVR challenge" and to benchmarks that test understanding of relationships between objects, spatial reasoning, and logical inference from visual input.

## Sources

**CLEVR** (5 papers: [Batch Calibration: Rethinking Calibration for In-Context Learning and Prompt Engineering](https://proceedings.iclr.cc/paper_files/paper/2024/file/003e438cf04e3caf0a5c908495e484fe-Paper-Conference.pdf), [LILO: Learning Interpretable Libraries by Compressing and Documenting Code](https://proceedings.iclr.cc/paper_files/paper/2024/file/819cebb05f993840e8a52d7564c5c282-Paper-Conference.pdf), [ClevrSkills: Compositional Language And Visual Reasoning in Robotics](https://proceedings.neurips.cc/paper_files/paper/2024/file/439539557e9ba0d04055773ff1f3241c-Paper-Datasets_and_Benchmarks_Track.pdf), [UQE: A Query Engine for Unstructured Databases](https://proceedings.neurips.cc/paper_files/paper/2024/file/34b3a40ec9752c1ae48fe85fef8fe8dc-Paper-Conference.pdf), [UniBench: Visual Reasoning Requires Rethinking Vision-Language Beyond Scaling](https://proceedings.neurips.cc/paper_files/paper/2024/file/96271227d3e204501d199433e56af289-Paper-Datasets_and_Benchmarks_Track.pdf))
> A visual reasoning benchmark used here as an image classification task.

## Relationships

### → CLEVR
- **Complex reasoning** (construct): *measured_by*, 1 paper
  > complex reasoning in CLEVR (Johnson et al., 2017) and Winoground (Thrush et al., 2022) (Section 4.1).
  - [VoCoT: Unleashing Visually Grounded Multi-Step Reasoning in Large Multi-Modal Models](https://aclanthology.org/2025.naacl-long.192.pdf)
