# Spoken question answering
**Type:** Behavioral indicator  
**Supporting papers:** 11  
**Also known as:** Speech question answering, Speech-based question answering  

## State of the Field

**Space of definitions.** Across papers, the prevailing usage is answering questions presented in speech or spoken audio, with the model returning either spoken or textual answers. Some authors make success explicit as producing a correct answer, while others score it by whether "the reference answer appears in the model's response" or in a transcription. One paper further describes it as answering broad factual questions without access to external knowledge. A smaller line of work narrows the task to answering a spoken question about an image, or to answering a text question using spoken context input rather than a spoken question itself.

**Variants.** Variants are mostly organized by modality and task name. Papers distinguish spoken-question to spoken-answer and spoken-question to text-answer settings, and they also use names such as SpokenQA, SQA, and spoken-query-based question answering (SQQA). Some work uses an audio clip plus a text question and expects a text answer, while other setups cover speech-related audio from monologue and dialogue in free-text form. Additional formulations treat the response as a speech continuation that must contain the answer, or pair speech with images in a speech question answering setup.

**Space of elicitation and scores.** Papers link spoken question answering to three measurement instruments. WebQuestions appears most often, followed by TriviaQA and WikiQA, and the recorded uses include synthesized audio versions of WebQuestions and TriviaQA, plus WikiQA with synthesized speech queries. These are benchmark datasets or test sets used to evaluate spoken question answering, and in one case closely paired factual correctness, on spoken or synthesized-spoken inputs.

**What it is taken as evidence of.** Papers link it to one construct, speech understanding. One paper places "Speech Question Answering (SQA)" within a "Speech Understanding" section, so the link is reported as related rather than as a measurement or causal claim. Beyond that, no other construct is linked.

## Sources

**Spoken question answering** (5 papers: [Scaling Speech-Text Pre-training with Synthetic Interleaved Data](https://proceedings.iclr.cc/paper_files/paper/2025/file/7b5ae891000049b91b3b62de596b1560-Paper-Conference.pdf), [Distilling an End-to-End Voice Assistant Without Instruction Training Data](https://aclanthology.org/2025.acl-long.388.pdf), [LLaMA-Omni 2: LLM-based Real-time Spoken Chatbot with Autoregressive Streaming Speech Synthesis](https://aclanthology.org/2025.acl-long.912.pdf), [Spoken Question Answering and Speech Continuation Using Spectrogram-Powered LLM](https://proceedings.iclr.cc/paper_files/paper/2024/file/e393677793767624f2821cec8bdd02f1-Paper-Conference.pdf), [Wav2Prompt: End-to-End Speech Prompt Learning and Task-based Fine-tuning for Text-based LLMs](https://aclanthology.org/2025.naacl-long.354.pdf))
> The model answers spoken questions with either spoken or textual responses.

**Speech question answering** (3 papers: [VLAS: Vision-Language-Action Model with Speech Instructions for Customized Robot Manipulation](https://proceedings.iclr.cc/paper_files/paper/2025/file/804a1a9de5787e3597b4bb64e1a48ec3-Paper-Conference.pdf), [SALMONN: Towards Generic Hearing Abilities for Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2024/file/476ab8f369e489c04187ba84f68cfa68-Paper-Conference.pdf), [AudioBench: A Universal Benchmark for Audio Large Language Models](https://aclanthology.org/2025.naacl-long.218.pdf))
> The task of answering a question posed in speech based on the content of a given image.

**Speech-based question answering** (1 paper: [VoiceTextBlender: Augmenting Large Language Models with Speech Capabilities via Single-Stage Joint Speech-Text Supervised Fine-Tuning](https://aclanthology.org/2025.naacl-long.298.pdf))
> Answering text questions based on spoken context input, generating text responses conditioned on audio and text inputs.

## Relationships

### Spoken question answering →
- **WebQuestions** (measurement instrument): *measured_by*, 3 papers
  > Similarly, on the Web Questions test set, the proposed model attains an accuracy of 6.1%, while SpeechGPT yields a comparable accuracy of 6.5%. (Section 4.2.3)
  - [Spoken Question Answering and Speech Continuation Using Spectrogram-Powered LLM](https://proceedings.iclr.cc/paper_files/paper/2024/file/e393677793767624f2821cec8bdd02f1-Paper-Conference.pdf)
  - [Scaling Speech-Text Pre-training with Synthetic Interleaved Data](https://proceedings.iclr.cc/paper_files/paper/2025/file/7b5ae891000049b91b3b62de596b1560-Paper-Conference.pdf)
  - [Aligning Spoken Dialogue Models from User Interactions](https://raw.githubusercontent.com/mlresearch/v267/main/assets/wu25t/wu25t.pdf)
- **TriviaQA** (measurement instrument): *measured_by*, 2 papers
  > Spoken Question Answering ... We evaluate our model on 3 datasets in D´efossez et al. (2024): Web Questions (Berant et al., 2013), Llama Questions (Nachmani et al., 2024), and TriviaQA (Joshi et al., 2017).
  - [Scaling Speech-Text Pre-training with Synthetic Interleaved Data](https://proceedings.iclr.cc/paper_files/paper/2025/file/7b5ae891000049b91b3b62de596b1560-Paper-Conference.pdf)
  - [Aligning Spoken Dialogue Models from User Interactions](https://raw.githubusercontent.com/mlresearch/v267/main/assets/wu25t/wu25t.pdf)
- **WikiQA** (measurement instrument): *measured_by*, 1 paper
  > For the SQQA task, the WikiQA (Yang et al., 2015) test set with synthesised speech queries provided by (Tang et al., 2024) was used. (Section 5.1)
  - [Wav2Prompt: End-to-End Speech Prompt Learning and Task-based Fine-tuning for Text-based LLMs](https://aclanthology.org/2025.naacl-long.354.pdf)

### Associated with
- **Speech understanding** (construct), 1 paper
  > 3.3.1 Speech Understanding ... Speech Question Answering (SQA).
  - [AudioBench: A Universal Benchmark for Audio Large Language Models](https://aclanthology.org/2025.naacl-long.218.pdf)
