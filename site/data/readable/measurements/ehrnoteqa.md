# EHRNoteQA
**Type:** Measurement instrument  
**Supporting papers:** 2  

## State of the Field

A clinical benchmark comprising 962 QA pairs linked to distinct patients' discharge summaries from MIMIC-IV EHR, evaluated in both open-ended and multi-choice formats.

## Sources

**EHRNoteQA** (1 paper: [EHRNoteQA: An LLM Benchmark for Real-World Clinical Practice Using Discharge Summaries](https://proceedings.neurips.cc/paper_files/paper/2024/file/e15c4afff22f12c4986c1fcb4e941e03-Paper-Datasets_and_Benchmarks_Track.pdf))
> A clinical benchmark comprising 962 QA pairs linked to distinct patients' discharge summaries from MIMIC-IV EHR, evaluated in both open-ended and multi-choice formats.

## Relationships

### EHRNoteQA →
- **Expert evaluation** (measurement instrument): *correlates*, 1 paper
  > Results show that LLM performance on EHRNoteQA have higher correlation with clinician-evaluated performance (Spearman(ρ): 0.78, Kendall(τ ): 0.62)
  - [EHRNoteQA: An LLM Benchmark for Real-World Clinical Practice Using Discharge Summaries](https://proceedings.neurips.cc/paper_files/paper/2024/file/e15c4afff22f12c4986c1fcb4e941e03-Paper-Datasets_and_Benchmarks_Track.pdf)

### → EHRNoteQA
- **Open-ended question answering** (behavioral indicator): *measured_by*, 1 paper
  > We offer EHRNoteQA in two formats: open-ended and multi-choice question answering, and propose a reliable evaluation method for each. (Abstract)
  - [EHRNoteQA: An LLM Benchmark for Real-World Clinical Practice Using Discharge Summaries](https://proceedings.neurips.cc/paper_files/paper/2024/file/e15c4afff22f12c4986c1fcb4e941e03-Paper-Datasets_and_Benchmarks_Track.pdf)
- **Multiple-choice question answering** (behavioral indicator): *measured_by*, 1 paper
  > We offer EHRNoteQA in two formats: open-ended and multi-choice question answering, and propose a reliable evaluation method for each. (Abstract)
  - [EHRNoteQA: An LLM Benchmark for Real-World Clinical Practice Using Discharge Summaries](https://proceedings.neurips.cc/paper_files/paper/2024/file/e15c4afff22f12c4986c1fcb4e941e03-Paper-Datasets_and_Benchmarks_Track.pdf)

### Associated with
- **LLM-as-a-judge** (measurement instrument), 1 paper
  > “For open-ended QA, we use GPT-4 to evaluate the model outputs instead of using traditional methods such BLEU or ROUGE-L”
  - [EHRNoteQA: An LLM Benchmark for Real-World Clinical Practice Using Discharge Summaries](https://proceedings.neurips.cc/paper_files/paper/2024/file/e15c4afff22f12c4986c1fcb4e941e03-Paper-Datasets_and_Benchmarks_Track.pdf)
