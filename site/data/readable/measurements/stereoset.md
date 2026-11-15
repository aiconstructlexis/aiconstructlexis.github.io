# StereoSet
**Type:** Measurement instrument  
**Supporting papers:** 18  

## State of the Field

**What it is.** Across the surveyed work, StereoSet is most commonly described as a benchmark or dataset for measuring stereotypical bias in language models with sentence-completion or fill-in-the-blank items that contrast stereotypical, anti-stereotypical, and meaningless or unrelated options. Several descriptions emphasize intrasentence examples, including one account that says the task contains 765 sentences with a gap and three completions, while another describes each sample as a sentence triplet. Some papers describe it more broadly as covering intrasentence and intersentence contexts, and a smaller description frames it as crowdsourced "Context Association Tests".

**What it is claimed to measure.** Papers link StereoSet to five constructs and two behavioral indicators. The prevailing use is to measure stereotyping, with papers saying it measures stereotypical biases or tests stereotypical associations, including in gender, profession, race, and religion; a recurring but smaller use treats it as measuring fairness and social bias, and individual papers also use it for gender bias and language modeling ability. At the behavioral level, it is reported as measuring sentence completion and stereotype recognition, including a three-way classification into "stereotype", "anti-stereotype", and "unrelated". Overall, these measurement claims spread across several related constructs rather than converging on a single label, though stereotypical bias is the dominant framing.

**Space of uses.** In use, papers often position StereoSet as an evaluation benchmark for debiasing or alignment methods, and several masked-language-model studies restrict evaluation to the intrasentence subset; one study further limits that setup to the gender domain. It is also used alongside other bias instruments, including WinoBias, CrowS-Pairs, RedditBias, and ILPS, and one multimodal benchmark samples 300 statements, evenly split across stereotype, anti-stereotype, and unrelated items.

## Sources

**StereoSet** (7 papers: [Debiasing Algorithm through Model Adaptation](https://proceedings.iclr.cc/paper_files/paper/2024/file/05aedcaf4bc6e78a5e22b4cf9114c5e8-Paper-Conference.pdf), [The Devil is in the Neurons: Interpreting and Mitigating Social Biases in Language Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/1a1ca821d0b4807f8217da7da1747c65-Paper-Conference.pdf), [CEB: Compositional Evaluation Benchmark for Fairness in Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/38e491559eb9e4cf31b8cd3a4e222436-Paper-Conference.pdf), [CoBia: Constructed Conversations Can Trigger Otherwise Concealed Societal Biases in LLMs](https://aclanthology.org/2025.emnlp-main.84.pdf), [Cross-Care: Assessing the Healthcare Implications of Pre-training Data on Language Model Bias](https://proceedings.neurips.cc/paper_files/paper/2024/file/2a617efee5815f12b405d40569dea0a5-Paper-Datasets_and_Benchmarks_Track.pdf), [EAI: Emotional Decision-Making of LLMs in Strategic Games and Ethical Dilemmas](https://proceedings.neurips.cc/paper_files/paper/2024/file/611e84703eac7cc03f78339df8aae2ed-Paper-Conference.pdf), [MultiTrust: A Comprehensive Benchmark Towards Trustworthy Multimodal Large Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/586640cda3db2dc77349013dcefee456-Paper-Datasets_and_Benchmarks_Track.pdf))
> StereoSet is a benchmark for measuring stereotypical bias using sentence completions that contrast stereotypical, anti-stereotypical, and meaningless options.

## Relationships

### → StereoSet
- **Stereotyping** (construct): *measured_by*, 3 papers
  > STEREOSET. STEREOSET measures stereotypical biases of models on gender, profession, race, and religion through 4, 229 context-sentence pairs. (Section 4.2)
  - [Reward Model Perspectives: Whose Opinions Do Reward Models Reward?](https://aclanthology.org/2025.emnlp-main.754.pdf)
  - [Blind Men and the Elephant: Diverse Perspectives on Gender Stereotypes in Benchmark Datasets](https://aclanthology.org/2025.emnlp-main.1162.pdf)
  - [Collapsed Language Models Promote Fairness](https://proceedings.iclr.cc/paper_files/paper/2025/file/96db0c53484428513ebc537fe48ddb7a-Paper-Conference.pdf)
- **Fairness** (construct): *measured_by*, 2 papers
  > As measured by prior metrics from StereoSet, our model achieves a higher degree of fairness while maintaining language modeling ability with low cost12.
  - [The Devil is in the Neurons: Interpreting and Mitigating Social Biases in Language Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/1a1ca821d0b4807f8217da7da1747c65-Paper-Conference.pdf)
  - [Token-Aware Editing of Internal Activations for Large Language Model Alignment](https://aclanthology.org/2025.emnlp-main.480.pdf)
- **Social bias** (construct): *measured_by*, 2 papers
  > We evaluate the efficacy of our debiasing method on the social bias benchmark StereoSet (Nadeem et al., 2021).
  - [The Devil is in the Neurons: Interpreting and Mitigating Social Biases in Language Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/1a1ca821d0b4807f8217da7da1747c65-Paper-Conference.pdf)
  - [Mitigating Biases in Language Models via Bias Unlearning](https://aclanthology.org/2025.emnlp-main.208.pdf)
- **Sentence completion** (behavioral indicator): *measured_by*, 1 paper
  > This task contains 765 sentences, each with a gap and three possible completions: stereotypical, anti-stereotypical, and meaningless. (Section 2.3)
  - [Debiasing Algorithm through Model Adaptation](https://proceedings.iclr.cc/paper_files/paper/2024/file/05aedcaf4bc6e78a5e22b4cf9114c5e8-Paper-Conference.pdf)
- **Language modeling ability** (construct): *measured_by*, 1 paper
  > LMS is used to evaluate the language modeling abilities of models.
  - [The Devil is in the Neurons: Interpreting and Mitigating Social Biases in Language Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/1a1ca821d0b4807f8217da7da1747c65-Paper-Conference.pdf)
- **Stereotype recognition** (behavioral indicator): *measured_by*, 1 paper
  > Stereotype Recognition: Utilizing StereoSet [35] to recognize stereotypes in sentences classifying them into one of three classes: “stereotype”, “anti-stereotype”, or “unrelated” categories. (Section 4)
  - [EAI: Emotional Decision-Making of LLMs in Strategic Games and Ethical Dilemmas](https://proceedings.neurips.cc/paper_files/paper/2024/file/611e84703eac7cc03f78339df8aae2ed-Paper-Conference.pdf)
- **Gender bias** (construct): *measured_by*, 1 paper
  > To answer the first question, we check the LLaMA performance on popular tests for gender bias: WinoBias (Zhao et al., 2018) and StereoSet (Nadeem et al., 2021). (Section 1)
  - [Debiasing Algorithm through Model Adaptation](https://proceedings.iclr.cc/paper_files/paper/2024/file/05aedcaf4bc6e78a5e22b4cf9114c5e8-Paper-Conference.pdf)
