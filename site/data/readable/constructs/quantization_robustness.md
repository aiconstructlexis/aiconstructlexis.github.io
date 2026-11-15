# Quantization robustness
**Type:** Construct  
**Supporting papers:** 14  
**Also known as:** Quantization sensitivity, Error resilience, Quantizability  

## State of the Field

**Space of definitions.** Across the surveyed work, the prevailing usage treats quantization robustness as performance retention under reduced numerical precision, especially when weights and activations are pushed to low-bit settings such as 4-bit or across varying bit-widths. Papers describe it through whether performance degrades at low bitwidth, whether benefits become more pronounced as bit size decreases, and whether accuracy loss stays small after quantization. A smaller line of work uses related labels such as quantization sensitivity, error resilience, or quantizability, shifting the emphasis from whole-model robustness to component-wise sensitivity, output stability when computation is approximated or quantized, or a model property that permits lower-precision parameters while maintaining performance.

**Space of facets.** Papers break the construct down along several axes. One recurring breakdown is by what is quantized, weights and activations, and by the severity of precision reduction, ranging from 8-bit to 4-bit and to any specified bit, including non-integer values. Other papers localize it to different model parts or inference stages, reporting varying sensitivity across linear blocks and experts in MoE blocks, and distinct error resilience between prefill, earlier decoding, and later autoregressive generation. Taken together, the labels overlap but are not identical: some papers treat it as a whole-model property, while others attach it to components, outputs, or parameter complexity.

**Space of measurement.** No measurement instrument or behavioral indicator is linked to it. Papers nevertheless operationalize the construct through observed performance or accuracy loss after quantization, especially in low-bit settings: examples include low-bit PTQ performance degradation, less than 1% accuracy loss at 8-bit, stronger gains as bit size decreases, and a 3.2-bit model outperforming slightly higher-bit alternatives. These operationalizations mostly follow the dominant definition of maintaining performance under reduced precision, though some papers instead operationalize it through block-level sensitivity profiles or phase-specific sensitivity to approximation errors.

## Sources

**Quantization robustness** (4 papers: [OmniQuant: Omnidirectionally Calibrated Quantization for Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/c6483c8a68083af3383f91ee0dc6db95-Paper-Conference.pdf), [QLLM: Accurate and Efficient Low-Bitwidth Quantization for Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/437bc4ccafd3fc6d4289bd10940be42b-Paper-Conference.pdf), [MambaQuant: Quantizing the Mamba Family with Variance Aligned Rotation Methods](https://proceedings.iclr.cc/paper_files/paper/2025/file/51ba8a68f471d952af625d1faf55e6c6-Paper-Conference.pdf), [SKIM: Any-bit Quantization Pushing The Limits of Post-Training Quantization](https://raw.githubusercontent.com/mlresearch/v267/main/assets/bai25c/bai25c.pdf))
> The degree to which a model maintains performance when weights and activations are represented in low-precision formats, particularly under extreme conditions like 4-bit quantization.

**Quantization sensitivity** (1 paper: [MxMoE: Mixed-precision Quantization for MoE with Accuracy and Performance Co-Design](https://raw.githubusercontent.com/mlresearch/v267/main/assets/duanmu25a/duanmu25a.pdf))
> The degree to which different components of a model are affected by reduced numerical precision, influencing the accuracy loss when quantized.

**Error resilience** (1 paper: [Progressive Mixed-Precision Decoding for Efficient LLM Inference](https://proceedings.iclr.cc/paper_files/paper/2025/file/5df4313ecd4875931fbdacc486cc1fcf-Paper-Conference.pdf))
> The degree to which an LLM's outputs remain stable when its computations are approximated or quantized.

**Quantizability** (1 paper: [Compute-Optimal LLMs Provably Generalize Better with Scale](https://proceedings.iclr.cc/paper_files/paper/2025/file/4a13396b4c8a90e01dac61d2b0559ef7-Paper-Conference.pdf))
> The property of a model that allows its parameters to be represented with lower numerical precision while maintaining performance, indicating lower effective complexity.
