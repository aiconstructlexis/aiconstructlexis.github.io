# Meeting summarization
**Type:** Behavioral indicator  
**Supporting papers:** 5  
**Also known as:** Meeting summary generation  

## State of the Field

**Space of definitions.** Across the surveyed work, the prevailing usage treats this behavior as condensing meeting discussions or transcripts into concise outputs, most often overviews or structured minutes, and sometimes lists of action items. Definitions generally agree on concise, structured coverage of the discussion, though some specify brief summaries and others allow more detailed summaries that cover main insights and local details. A smaller line of work frames it as generating a summary for all attendees that excludes confidential information while retaining public information, or as summarizing aspects of a meeting in response to specific content questions.

**Variants.** Papers use several variants and names for this behavior. One recurring split is between traditional brief summarization and a detailed summarization track, where the summary remains concise but also covers main insights and local details. Other variants include question-focused meeting summarization, with transcripts paired with prompts about particular discussion topics, and meeting summary generation for summaries that are automatically sent to all attendees and must omit earlier sensitive discussion.

**Space of elicitation and scores.** Papers measure this behavior with one instrument, TofuEval. It is described as one of the few frameworks specifically developed for meeting and dialogue summarization, and no other instrument is linked to this behavior.

**What it is taken as evidence of.** No construct is linked to it, so papers do not specify what construct it is taken to indicate.

## Sources

**Meeting summarization** (3 papers: [Summarizing Speech: A Comprehensive Survey](https://aclanthology.org/2025.emnlp-main.1388.pdf), [MISP-Meeting: A Real-World Dataset with Multimodal Cues for Long-form Meeting Transcription and Summarization](https://aclanthology.org/2025.acl-long.753.pdf), [Teaching Language Models to Hallucinate Less with Synthetic Tasks](https://proceedings.iclr.cc/paper_files/paper/2024/file/e4cd50120b6d7e8daff1749d6bbaa889-Paper-Conference.pdf))
> The task of condensing free-form spoken discussions from meetings into concise overviews, structured minutes, or lists of action items.

**Meeting summary generation** (1 paper: [Can LLMs Keep a Secret? Testing Privacy Implications of Language Models via Contextual Integrity Theory](https://proceedings.iclr.cc/paper_files/paper/2024/file/08305d8b2ddab98932c163ea73df065f-Paper-Conference.pdf))
> Generating a meeting summary for all attendees while excluding confidential information and retaining public information.

## Relationships

### Meeting summarization →
- **TofuEval** (measurement instrument): *measured_by*, 1 paper
  > Among these, CREAM (Gong et al., 2024), MESA (Kirstein et al., 2025b), and TofuEval (Tang et al., 2024) stand out as one of the few frameworks specifically developed for meeting and dialogue summarization... (Section 5.2).
  - [Summarizing Speech: A Comprehensive Survey](https://aclanthology.org/2025.emnlp-main.1388.pdf)
