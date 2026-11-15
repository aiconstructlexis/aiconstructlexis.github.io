# MovieLens
**Type:** Measurement instrument  
**Supporting papers:** 6  

## State of the Field

**What it is.** Papers most commonly describe MovieLens as a widely used benchmark dataset for recommendation systems, centered on user movie ratings and movie metadata. Some descriptions are more task-specific, presenting it as movie-rating data for evaluating recommendation systems, query modification in LLM-based recommenders, simulation platforms, or personalized cover generation; one paper also describes it as including movie metadata, user demographics, and covers, and reports "86K movies, 0.3M users, and 3.3M ratings".

**What it is claimed to measure.** The reported measurement claims converge on one construct: MovieLens is linked to one construct, Generalization, and to no behavioral indicators. One paper, Customizing Language Models with Instance-wise LoRA for Sequential Recommendation, uses it to measure Generalization, stating that MovieLens was included "to validate the generalization ability" of the model in real-world recommendation scenarios.

**Space of uses.** Papers typically place MovieLens within multi-dataset evaluations. It is used alongside LastFM and Steam in sequential recommendation experiments, alongside Google Local and AmazonBook in simulation-platform evaluation, and in one study as one of two public datasets representing movie recommendation scenarios for personalized cover generation; papers do not link it to other measurement instruments.

## Sources

**MovieLens** (4 papers: [Customizing Language Models with Instance-wise LoRA for Sequential Recommendation](https://proceedings.neurips.cc/paper_files/paper/2024/file/cd476d01692c508ddf1cb43c6279a704-Paper-Conference.pdf), [Unified Parameter-Efficient Unlearning for LLMs](https://proceedings.iclr.cc/paper_files/paper/2025/file/8d537430e55a283a97e9b6e682e994a3-Paper-Conference.pdf), [Beyond Static Testbeds: An Interaction-Centric Agent Simulation Platform for Dynamic Recommender Systems](https://aclanthology.org/2025.emnlp-main.956.pdf), [ICG: Improving Cover Image Generation via MLLM-based Prompting and Personalized Preference Alignment](https://aclanthology.org/2025.emnlp-main.617.pdf))
> A widely used benchmark dataset in recommendation systems research, containing user ratings and metadata for movies.

## Relationships

### → MovieLens
- **Generalization** (construct): *measured_by*, 1 paper
  > “To validate the generalization ability of iLoRA, we conducted extensive experiments on three datasets derived from real-world recommendation scenarios: LastFM, MovieLens, and Steam”
  - [Customizing Language Models with Instance-wise LoRA for Sequential Recommendation](https://proceedings.neurips.cc/paper_files/paper/2024/file/cd476d01692c508ddf1cb43c6279a704-Paper-Conference.pdf)
