# Action recognition
**Type:** Behavioral indicator  
**Supporting papers:** 18  
**Also known as:** Fine-grained keystep recognition, Step recognition, Activity recognition, Sport recognition, Sports recognition, Video action recognition, Activity classification  

## State of the Field

**Space of definitions.** Across the surveyed work, the prevailing usage treats action recognition as identifying or classifying the action in video clips, often as predicting an action label. Some papers broaden the target to activities or events, including real-world videos with human actions and interactions, and a smaller formulation tests whether models can distinguish activities by phrases that differ only in action verbs. Most formulations count success as naming the correct action or activity, though some use open-ended activity questions and one paper reformulates the task as multiple-choice generation at test time.

**Variants.** Variants span video clips, single images, video frames, and sequences or sets of images. Papers also use nearby names such as activity recognition, step recognition, fine-grained keystep recognition, sport or sports recognition, and activity classification. Procedural versions focus on identifying individual steps within instructional or egocentric videos, while sports-focused versions ask which sport is shown.

**Space of elicitation and scores.** Only a single paper explicitly links this behavior to measurement instruments, and it is measured by 3 instruments: ActivityNet, Something-Something V2, and UCF-101. Elsewhere, papers operationalize it through direct requests to identify an action, open-ended questions about an activity in an image, or a multiple-choice version of the original classification task.

**What it is taken as evidence of.** Papers do not link this behavior to any construct, so they do not specify what it is evidence of.

## Sources

**Action recognition** (7 papers: [Frozen Transformers in Language Models Are Effective Visual Encoder Layers](https://proceedings.iclr.cc/paper_files/paper/2024/file/03cd3cf3f74d4f9ce5958de269960884-Paper-Conference.pdf), [Language Model Beats Diffusion - Tokenizer is key to visual generation](https://proceedings.iclr.cc/paper_files/paper/2024/file/036912a83bdbb1fd792baf6532f102d8-Paper-Conference.pdf), [Look, Remember and Reason: Grounded Reasoning in Videos with Language Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/1df282080150537df7b00c20aadcafad-Paper-Conference.pdf), [ViLMA: A Zero-Shot Benchmark for Linguistic and Temporal Grounding in Video-Language Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/b176e960edbb8afe77f77f9039d2738a-Paper-Conference.pdf), [MaVEn: An Effective Multi-granularity Hybrid Visual Encoding Framework for Multimodal Large Language Model](https://proceedings.neurips.cc/paper_files/paper/2024/file/b8f21f324ff277ba26aed2e944b7576b-Paper-Conference.pdf), [MMIU: Multimodal Multi-image Understanding for Evaluating Large Vision-Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/5f92032278b1c70946e0b753068de51e-Paper-Conference.pdf), [Scaling Video-Language Models to 10K Frames via Hierarchical Differential Distillation](https://raw.githubusercontent.com/mlresearch/v267/main/assets/cheng25b/cheng25b.pdf))
> Classifying human actions in video clips using learned token representations as input or training targets.

**Fine-grained keystep recognition** (1 paper: [VideoLLM-MoD: Efficient Video-Language Streaming with Mixture-of-Depths Vision Computation](https://proceedings.neurips.cc/paper_files/paper/2024/file/c6a79e139ec4f371701ea8cc9e06018e-Paper-Conference.pdf))
> The task of identifying and labeling specific, detailed steps within a larger procedural activity shown in a video.

**Step recognition** (1 paper: [VideoLLM-MoD: Efficient Video-Language Streaming with Mixture-of-Depths Vision Computation](https://proceedings.neurips.cc/paper_files/paper/2024/file/c6a79e139ec4f371701ea8cc9e06018e-Paper-Conference.pdf))
> The task of identifying the individual steps of a procedure shown in an instructional video.

**Activity recognition** (2 papers: [Have the VLMs Lost Confidence? A Study of Sycophancy in VLMs](https://proceedings.iclr.cc/paper_files/paper/2025/file/07be1a0850e58ca29e2b6ce31fc0c791-Paper-Conference.pdf), [Mitigating Hallucination in Large Multi-Modal Models via Robust Instruction Tuning](https://proceedings.iclr.cc/paper_files/paper/2024/file/fed9263d7f1086e735904ff690527a53-Paper-Conference.pdf))
> The task of identifying and naming the primary action or event occurring in an image.

**Sport recognition** (1 paper: [Have the VLMs Lost Confidence? A Study of Sycophancy in VLMs](https://proceedings.iclr.cc/paper_files/paper/2025/file/07be1a0850e58ca29e2b6ce31fc0c791-Paper-Conference.pdf))
> The task of identifying the specific sport being played in an image.

**Sports recognition** (1 paper: [SPORTU: A Comprehensive Sports Understanding Benchmark for Multimodal Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/49c1879ae366644ce2c17fb39ddea982-Paper-Conference.pdf))
> The task of identifying the specific sport being played in a video clip.

**Video action recognition** (1 paper: [RepLoRA: Reparameterizing Low-rank Adaptation via the Perspective of Mixture of Experts](https://raw.githubusercontent.com/mlresearch/v267/main/assets/truong25a/truong25a.pdf))
> The task of identifying and classifying human actions or activities within video clips.

**Activity classification** (1 paper: [Open-ended VQA benchmarking of Vision-Language models by exploiting Classification datasets and their semantic hierarchy](https://proceedings.iclr.cc/paper_files/paper/2024/file/cb1c4782f159b55380b4584671c4fd88-Paper-Conference.pdf))
> Recognizing the type of action or activity occurring in an image derived from a video frame, using open-ended language generation.

## Relationships

### Action recognition →
- **ActivityNet** (measurement instrument): *measured_by*, 1 paper
  > For the action recognition task, we incorporate two baselines: Adaframe (Wu et al., 2019) and MGSampler (Zhi et al., 2021), and evaluate them alongside VILAMP on three benchmarks: ActivityNet (Caba Heilbron et al., 2015), Something-Something V2 (Sth-V2) (Goyal et al., 2017), and UCF-101 (Soomro et al., 2012). (Section 5.4)
  - [Scaling Video-Language Models to 10K Frames via Hierarchical Differential Distillation](https://raw.githubusercontent.com/mlresearch/v267/main/assets/cheng25b/cheng25b.pdf)
- **Something-Something V2** (measurement instrument): *measured_by*, 1 paper
  > For the action recognition task, we incorporate two baselines: Adaframe (Wu et al., 2019) and MGSampler (Zhi et al., 2021), and evaluate them alongside VILAMP on three benchmarks: ActivityNet (Caba Heilbron et al., 2015), Something-Something V2 (Sth-V2) (Goyal et al., 2017), and UCF-101 (Soomro et al., 2012). (Section 5.4)
  - [Scaling Video-Language Models to 10K Frames via Hierarchical Differential Distillation](https://raw.githubusercontent.com/mlresearch/v267/main/assets/cheng25b/cheng25b.pdf)
- **UCF-101** (measurement instrument): *measured_by*, 1 paper
  > For the action recognition task, we incorporate two baselines: Adaframe (Wu et al., 2019) and MGSampler (Zhi et al., 2021), and evaluate them alongside VILAMP on three benchmarks: ActivityNet (Caba Heilbron et al., 2015), Something-Something V2 (Sth-V2) (Goyal et al., 2017), and UCF-101 (Soomro et al., 2012). (Section 5.4)
  - [Scaling Video-Language Models to 10K Frames via Hierarchical Differential Distillation](https://raw.githubusercontent.com/mlresearch/v267/main/assets/cheng25b/cheng25b.pdf)
