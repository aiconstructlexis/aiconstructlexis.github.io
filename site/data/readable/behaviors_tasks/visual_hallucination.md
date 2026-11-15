# Visual hallucination
**Type:** Behavioral indicator  
**Supporting papers:** 6  
**Also known as:** Multimodal hallucination  

## State of the Field

**Space of definitions.** Across the definitions, the prevailing usage treats visual hallucination as a failure mode in which an MLLM produces incorrect visual claims or unsupported descriptions while interpreting an image. Most formulations focus on text that mentions objects, attributes, or relationships not present in the image, and a smaller formulation uses the name multimodal hallucination for outputs that contain information inconsistent with or absent from the provided multimodal inputs. Success is correspondingly framed as keeping the response consistent with the image content, or more broadly with the given multimodal inputs.

**Variants.** Papers most commonly study it when models respond about an image, especially when they describe objects, attributes, or relationships that are not in the input image. A smaller line of work broadens the setting from images to multimodal inputs and uses the label multimodal hallucination. One quoted passage also highlights failures in granular visual recognition, such as identifying small and occluded objects.

**Space of elicitation and scores.** Papers measure it with four linked instruments. The most common is POPE, which papers describe as aiming to evaluate visual hallucinations of MLLMs and as an assessment of multimodal hallucination; CHAIR, HallusionBench, and MMHal-Bench are also used as named evaluation tools. One paper frames this as a visual hallucination task that checks whether the model response is consistent with the image content, while another uses HallusionBench to quantify the extent of hallucinations.

**What it is taken as evidence of.** Papers link it to one construct, visual perception. One paper claims a causal relationship from visual perception to visual hallucination, stating that impaired visual perception may lead to visual hallucinations, while another paper discusses visual perception and visual hallucinations together when examining model capabilities. No other construct is linked to it.

## Sources

**Visual hallucination** (2 papers: [Feast Your Eyes: Mixture-of-Resolution Adaptation for Multimodal Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/d2781f7df8825bbde6cef55adfbcd283-Paper-Conference.pdf), [Routing Experts: Learning to Route Dynamic Experts in Existing Multi-modal Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/49a4829a2ccaaa4706cc82e68c39a9c6-Paper-Conference.pdf))
> Producing incorrect visual claims or unsupported descriptions when interpreting an image.

**Multimodal hallucination** (1 paper: [Mitigating Modality Prior-Induced Hallucinations in Multimodal Large Language Models via Deciphering Attention Causality](https://proceedings.iclr.cc/paper_files/paper/2025/file/86fe62e3b315d2578721562d9fd1a433-Paper-Conference.pdf))
> A failure mode in Multimodal Large Language Models where the generated output contains information that is inconsistent with or absent from the provided multimodal inputs.

## Relationships

### Visual hallucination →
- **POPE** (measurement instrument): *measured_by*, 5 papers
  > We conducted extensive evaluations of DEEM on RobustVQA and two widely recognized benchmarks, POPE and MMVP, for visual hallucination and perception respectively (Section 1).
  - [DEEM: Diffusion models serve as the eyes of large language models for image perception](https://proceedings.iclr.cc/paper_files/paper/2025/file/a8399aace3dfa6dfb8b635117748c561-Paper-Conference.pdf)
  - [Feast Your Eyes: Mixture-of-Resolution Adaptation for Multimodal Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/d2781f7df8825bbde6cef55adfbcd283-Paper-Conference.pdf)
  - [See What You Are Told: Visual Attention Sink in Large Multimodal Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/da8a39bc39ae1c89dd6ebb1e3bcbb3f3-Paper-Conference.pdf)
  - [Routing Experts: Learning to Route Dynamic Experts in Existing Multi-modal Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/49a4829a2ccaaa4706cc82e68c39a9c6-Paper-Conference.pdf)
  - [Beyond One-Size-Fits-All: Tailored Benchmarks for Efficient Evaluation](https://aclanthology.org/2025.acl-long.759.pdf)
- **CHAIR** (measurement instrument): *measured_by*, 1 paper
  > Visual hallucination task evaluates whether the response of the model is consistent with the image content to ensure the trustworthiness and reliability of the model. We use CHAIR (Rohrbach et al., 2018), POPE (Li et al., 2023c), and MMHal-Bench (Sun et al., 2023).
  - [See What You Are Told: Visual Attention Sink in Large Multimodal Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/da8a39bc39ae1c89dd6ebb1e3bcbb3f3-Paper-Conference.pdf)
- **MMHal-Bench** (measurement instrument): *measured_by*, 1 paper
  > Visual hallucination task evaluates whether the response of the model is consistent with the image content to ensure the trustworthiness and reliability of the model. We use CHAIR (Rohrbach et al., 2018), POPE (Li et al., 2023c), and MMHal-Bench (Sun et al., 2023).
  - [See What You Are Told: Visual Attention Sink in Large Multimodal Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/da8a39bc39ae1c89dd6ebb1e3bcbb3f3-Paper-Conference.pdf)
- **HallusionBench** (measurement instrument): *measured_by*, 1 paper
  > Furthermore, we use HallBench (Guan et al., 2024) to quantify the extent of visual hallucinations in VLMs or VRMs. (Section 4.1)
  - [Look Again, Think Slowly: Enhancing Visual Reflection in Vision-Language Models](https://aclanthology.org/2025.emnlp-main.470.pdf)

### → Visual hallucination
- **Visual perception** (construct): *causes*, 2 papers
  > “Neglecting to fine-tune the projector can significantly impair the model’s visual perception capabilities. This deficiency may lead to visual hallucinations”
  - [REMEDY: Recipe Merging Dynamics in Large Vision-Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/4065a881baab1744bfba208a4361bbb1-Paper-Conference.pdf)
  - [DEEM: Diffusion models serve as the eyes of large language models for image perception](https://proceedings.iclr.cc/paper_files/paper/2025/file/a8399aace3dfa6dfb8b635117748c561-Paper-Conference.pdf)
