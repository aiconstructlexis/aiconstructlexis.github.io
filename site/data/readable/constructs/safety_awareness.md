# Safety awareness
**Type:** Construct  
**Supporting papers:** 10  
**Also known as:** Risk awareness  

## State of the Field

**Space of definitions.** Across papers, the prevailing usage treats safety awareness as a latent disposition or ability to recognize sensitive, harmful, or high-stakes situations and respond cautiously, most often by seeking user confirmation before acting. Closely related work uses the label risk awareness for a similar framing, and one paper says an agent should "be aware of the potential risks and seek user confirmation before executing risky actions." A smaller line of work broadens it to a model's sensitivity to safety-related risks and tendency to avoid unsafe outputs across risk categories, while another defines it at the representation level, as whether internal states show clear distinctions between safe and toxic content. The main difference across definitions is whether the construct is located in action handling, output tendencies, or internal representations.

**Space of facets.** Papers do not offer a detailed subtype taxonomy, but they repeatedly organize the construct around a few recurring targets: sensitive or high-stakes actions, different risk categories, suspicious pop-ups, and safe versus toxic content. One line focuses on action sensitivity, for example whether a system can assess the sensitivity of each action and ask for confirmation; another focuses on output-side avoidance of unsafe responses across categories; and another treats it as a form of latent "self-awareness" visible in internal distinctions between safe and unsafe inputs. The alternate label risk awareness is used for a closely similar idea, and across the papers it is not explicitly nested under or contrasted with another construct.

**Space of measurement.** Papers link the construct to 1 measurement instrument and 1 behavioral indicator. The only named instrument is SIUO, described as a dataset used "for assessment of safety-awareness"; beyond that explicit instrument link, papers operationalize the construct through whether systems seek confirmation before risky actions, classify sensitive requests, avoid unsafe outputs across risk categories, and avoid harmful interactions such as suspicious pop-ups. One paper also operationalizes it with probing, looking for the layer where the model shows the clearest distinction between safe and toxic inputs, so operationalizations mostly follow the recognition-and-caution definitions but sometimes shift to output-level or representation-level evidence.

**Links.** Beyond measurement, one paper claims a causal relationship from Harmful content detection to Safety awareness, describing better performance on safety-awareness benchmarks as arising from improved capability in identifying unsafe intent. No papers report a correlational link or a merely related link.

## Sources

**Safety awareness** (4 papers: [SafetyQuizzer: Timely and Dynamic Evaluation on the Safety of LLMs](https://aclanthology.org/2025.naacl-long.85.pdf), [UFO: A UI-Focused Agent for Windows OS Interaction](https://aclanthology.org/2025.naacl-long.26.pdf), [Attacking Vision-Language Computer Agents via Pop-ups](https://aclanthology.org/2025.acl-long.411.pdf), [Automating Steering for Safe Multimodal Large Language Models](https://aclanthology.org/2025.emnlp-main.41.pdf))
> The latent disposition to recognize and handle sensitive or potentially harmful actions by seeking user confirmation before execution.

**Risk awareness** (1 paper: [Identifying the Risks of LM Agents with an LM-Emulated Sandbox](https://proceedings.iclr.cc/paper_files/paper/2024/file/7274ed909a312d4d869cc328ad1c5f04-Paper-Conference.pdf))
> The latent ability of an LM agent to recognize potentially dangerous situations and respond appropriately, such as by seeking user confirmation before executing high-stakes actions.

## Relationships

### Safety awareness →
- **SIUO** (measurement instrument): *measured_by*, 1 paper
  > For assessment of safety-awareness, we employ SIUO (Wang et al., 2025) and MSS-Bench (Zhou et al., 2024) datasets... (Section 2.1).
  - [Think in Safety: Unveiling and Mitigating Safety Alignment Collapse in Multimodal Large Reasoning Model](https://aclanthology.org/2025.emnlp-main.261.pdf)

### → Safety awareness
- **Harmful content detection** (behavioral indicator): *causes*, 1 paper
  > MLRMs paradoxically enhances safety performance via long reasoning on safety-awareness benchmarks, due to improved capability in identifying unsafe intent (Section 2.2).
  - [Think in Safety: Unveiling and Mitigating Safety Alignment Collapse in Multimodal Large Reasoning Model](https://aclanthology.org/2025.emnlp-main.261.pdf)
