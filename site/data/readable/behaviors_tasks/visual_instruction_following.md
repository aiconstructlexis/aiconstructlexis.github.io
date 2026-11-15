# Visual instruction following
**Type:** Behavioral indicator  
**Supporting papers:** 3  
**Also known as:** Image-conditioned instruction following  

## State of the Field

**Space of definitions.** Across the definitions, the prevailing usage treats it as producing a textual response to a natural language instruction or question given an accompanying image. The wording is consistent across papers: one definition emphasizes a response based on the combination of a visual image and language input, while another emphasizes that the instruction requires understanding and reasoning over the image. The quoted passages illustrate example responses such as identifying a place from an image or deciding whether to go left or right.

**Variants.** Papers use both "visual instruction following" and "image-conditioned instruction following" for this behavior, and they also place it in multimodal or visual-language settings. The studied formulations include evaluation on Mixed Visual Instruction Tuning 665k with seven datasets, including VQA-v2, GQA, and VisWiz, and one paper reports it is related to visual question answering in a multitask setup that includes VQA and region-level VQA. It also appears in discussions of instruction tuning for visual-language tasks.

**Space of elicitation and scores.** It is measured by 6 instruments in the papers. The most commonly linked instrument is LLaVA-Bench-in-the-Wild, and MM-Vet, MMBench, MME, and POPE are also used, along with 1 other benchmark. These instruments are described as instruction-following-based LMM benchmarks, and LLaVA-Bench-in-the-Wild is specifically described as a benchmark dataset of 60 questions for evaluating multimodal instruction following capabilities.

**What it is taken as evidence of.** Papers do not link this behavior to any construct, so there is no stated construct that it is taken to indicate. Separately, one paper reports that it is related to visual question answering.

## Sources

**Visual instruction following** (1 paper: [SAN: Hypothesizing Long-Term Synaptic Development and Neural Engram Mechanism in Scalable Model’s Parameter-Efficient Fine-Tuning](https://raw.githubusercontent.com/mlresearch/v267/main/assets/dai25e/dai25e.pdf))
> The observable task of generating a textual response based on a combination of a visual image and a natural language instruction or question.

**Image-conditioned instruction following** (1 paper: [LLaMA-Adapter: Efficient Fine-tuning of Large Language Models with Zero-initialized Attention](https://proceedings.iclr.cc/paper_files/paper/2024/file/c196239c5f9481e0db2755f31fe4585f-Paper-Conference.pdf))
> Responding to natural language instructions that require understanding and reasoning over an accompanying image input.

## Relationships

### Visual instruction following →
- **LLaVA-Bench-in-the-Wild** (measurement instrument): *measured_by*, 2 papers
  > ...as well as instruction-following-based LMM benchmarks including POPE [40], MME [17], MMBench [47], SEED-Bench [35], LLaVA-Wild [46], and MM-Vet [67]. (Section 4.1)
  - [CuMo: Scaling Multimodal LLM with Co-Upcycled Mixture-of-Experts](https://proceedings.neurips.cc/paper_files/paper/2024/file/ed1d3d4c64dc1b95332a8cde3f2a0bdf-Paper-Conference.pdf)
  - [CogVLM: Visual Expert for Pretrained Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/dc06d4d2792265fb5454a6092bfd5c6a-Paper-Conference.pdf)
- **POPE** (measurement instrument): *measured_by*, 1 paper
  > ...as well as instruction-following-based LMM benchmarks including POPE [40], MME [17], MMBench [47], SEED-Bench [35], LLaVA-Wild [46], and MM-Vet [67]. (Section 4.1)
  - [CuMo: Scaling Multimodal LLM with Co-Upcycled Mixture-of-Experts](https://proceedings.neurips.cc/paper_files/paper/2024/file/ed1d3d4c64dc1b95332a8cde3f2a0bdf-Paper-Conference.pdf)
- **MMBench** (measurement instrument): *measured_by*, 1 paper
  > ...as well as instruction-following-based LMM benchmarks including POPE [40], MME [17], MMBench [47], SEED-Bench [35], LLaVA-Wild [46], and MM-Vet [67]. (Section 4.1)
  - [CuMo: Scaling Multimodal LLM with Co-Upcycled Mixture-of-Experts](https://proceedings.neurips.cc/paper_files/paper/2024/file/ed1d3d4c64dc1b95332a8cde3f2a0bdf-Paper-Conference.pdf)
- **MME** (measurement instrument): *measured_by*, 1 paper
  > ...as well as instruction-following-based LMM benchmarks including POPE [40], MME [17], MMBench [47], SEED-Bench [35], LLaVA-Wild [46], and MM-Vet [67]. (Section 4.1)
  - [CuMo: Scaling Multimodal LLM with Co-Upcycled Mixture-of-Experts](https://proceedings.neurips.cc/paper_files/paper/2024/file/ed1d3d4c64dc1b95332a8cde3f2a0bdf-Paper-Conference.pdf)
- **SEED-Bench** (measurement instrument): *measured_by*, 1 paper
  > ...as well as instruction-following-based LMM benchmarks including POPE [40], MME [17], MMBench [47], SEED-Bench [35], LLaVA-Wild [46], and MM-Vet [67]. (Section 4.1)
  - [CuMo: Scaling Multimodal LLM with Co-Upcycled Mixture-of-Experts](https://proceedings.neurips.cc/paper_files/paper/2024/file/ed1d3d4c64dc1b95332a8cde3f2a0bdf-Paper-Conference.pdf)
- **MM-Vet** (measurement instrument): *measured_by*, 1 paper
  > ...as well as instruction-following-based LMM benchmarks including POPE [40], MME [17], MMBench [47], SEED-Bench [35], LLaVA-Wild [46], and MM-Vet [67]. (Section 4.1)
  - [CuMo: Scaling Multimodal LLM with Co-Upcycled Mixture-of-Experts](https://proceedings.neurips.cc/paper_files/paper/2024/file/ed1d3d4c64dc1b95332a8cde3f2a0bdf-Paper-Conference.pdf)

### Associated with
- **Visual question answering** (behavioral indicator), 1 paper
  > "The visual instruction tuning is performed in a multitask setting, including VQA ... region-level VQA ..."
  - [MiLoRA: Harnessing Minor Singular Components for Parameter-Efficient LLM Finetuning](https://aclanthology.org/2025.naacl-long.248.pdf)
