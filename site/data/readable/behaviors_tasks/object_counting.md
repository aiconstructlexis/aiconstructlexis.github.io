# Object counting
**Type:** Behavioral indicator  
**Supporting papers:** 19  
**Also known as:** Object count  

## State of the Field

**Space of definitions.** Across the surveyed work, the dominant framing is a task where a model determines how many instances of a specified object category are present, most often in an image. Papers commonly treat success as returning the correct quantity for the queried object, sometimes in a natural-language question and answer format, and one image-based description says the model must delineate instances of a given object type for counting. A smaller line of work uses the same label for counting entities listed in a textual prompt or context, and another uses it for counting how many instances of an object appear in a video.

**Variants.** Variants differ mainly by modality and setting. Image-based work includes general perception tasks, cluttered environments, and visual equation settings built from repeated visual elements, and one paper explicitly uses images with 1-4 instances. Other papers name a count subtask, or Object Count (OC), in animal-centric video understanding, while text-oriented work studies counting over verbally enumerated entities.

**Space of elicitation and scores.** Papers link object counting to five measurement instruments: BIG-Bench Hard, BIG-bench, MME, MME-RealWorld, and Waste-Bench. The measured_by links are to MME, where Count is one of four subtasks and performance uses a combined accuracy and accuracy+ metric, to MME-RealWorld, where object counting is one of three perception tasks, to BIG-Bench Hard, which one paper uses as the dataset for object counting in prompt optimization, and to Waste-Bench, where counting asks for the number of specific items or categories within an image. One additional paper treats BIG-bench as related, describing an adapted task for object classification and counting.

**What it is taken as evidence of.** Construct links are sparse. The only linked construct is Multimodal reasoning, and that connection is recorded as related rather than as a causal claim or correlation: one paper presents better object counting and OCR within multi-modal reasoning examples. Beyond that, papers do not connect object counting to other constructs.

## Sources

**Object counting** (6 papers: [Cambrian-1: A Fully Open, Vision-Centric Exploration of Multimodal LLMs](https://proceedings.neurips.cc/paper_files/paper/2024/file/9ee3a664ccfeabc0da16ac6f1f1cfe59-Paper-Conference.pdf), [Can Textual Gradient Work in Federated Learning?](https://proceedings.iclr.cc/paper_files/paper/2025/file/1a25185fe1b0d46241de7738ea320710-Paper-Conference.pdf), [Hyperband-based Bayesian Optimization for Black-box Prompt Selection](https://raw.githubusercontent.com/mlresearch/v267/main/assets/schneider25b/schneider25b.pdf), [Response Wide Shut? Surprising Observations in Basic Vision Language Model Capabilities](https://aclanthology.org/2025.acl-long.1241.pdf), [Can Vision-Language Models Solve Visual Math Equations?](https://aclanthology.org/2025.emnlp-main.547.pdf), [LLaMA-Adapter: Efficient Fine-tuning of Large Language Models with Zero-initialized Attention](https://proceedings.iclr.cc/paper_files/paper/2024/file/c196239c5f9481e0db2755f31fe4585f-Paper-Conference.pdf))
> Determining the number of instances of a specific object category present in an image.

**Object count** (1 paper: [Animal-Bench: Benchmarking Multimodal Video Models for Animal-centric Video Understanding](https://proceedings.neurips.cc/paper_files/paper/2024/file/8fa604a81e5a236e2f38e917109571a3-Paper-Conference.pdf))
> Counting how many instances of an object appear in a video.

## Relationships

### Object counting →
- **MME** (measurement instrument): *measured_by*, 1 paper
  > Following Yin et al. (2023), we evaluate hallucination using four subtasks: Existence, Count, Position, and Color, with performance measured by the combined metric of accuracy and accuracy+ (Section 4.1).
  - [Do You Keep an Eye on What I Ask? Mitigating Multimodal Hallucination via Attention-Guided Ensemble Decoding](https://proceedings.iclr.cc/paper_files/paper/2025/file/637b275a6e65924719198188fc939632-Paper-Conference.pdf)
- **MME-RealWorld** (measurement instrument): *measured_by*, 1 paper
  > There are 3 perception tasks: object counting, color recognition, and spatial relationship understanding. (Section 2.2)
  - [MME-RealWorld: Could Your Multimodal LLM Challenge High-Resolution Real-World Scenarios that are Difficult for Humans?](https://proceedings.iclr.cc/paper_files/paper/2025/file/df29d63af05cb91d705cf06ba5945b9d-Paper-Conference.pdf)
- **BIG-Bench Hard** (measurement instrument): *measured_by*, 1 paper
  > For prompt optimization, we use the Big Bench Hard dataset (Suzgun et al., 2022) for Object Counting... (Section 4)
  - [Revolve: Optimizing AI Systems by Tracking Response Evolution in Textual Optimization](https://raw.githubusercontent.com/mlresearch/v267/main/assets/zhang25aj/zhang25aj.pdf)
- **Waste-Bench** (measurement instrument): *measured_by*, 1 paper
  > Counting: This category involves tasks where the model must count the number of specific items or categories within an image.
  - [Waste-Bench: A Comprehensive Benchmark for Evaluating VLLMs in Cluttered Environments](https://aclanthology.org/2025.emnlp-main.1578.pdf)

### Associated with
- **BIG-bench** (measurement instrument), 1 paper
  > Adapted from BIG-bench (Bench authors, 2023), this task tests object classification and counting. (Section 4.3)
  - [A Causal Lens for Evaluating Faithfulness Metrics](https://aclanthology.org/2025.emnlp-main.1496.pdf)
- **Multimodal reasoning** (construct), 1 paper
  > We also show some multi-modal reasoning examples in Figure 6. Our approach exhibits better object counting, OCR, and commence reasoning performance. (Section 4.2)
  - [LLaMA-Adapter: Efficient Fine-tuning of Large Language Models with Zero-initialized Attention](https://proceedings.iclr.cc/paper_files/paper/2024/file/c196239c5f9481e0db2755f31fe4585f-Paper-Conference.pdf)
