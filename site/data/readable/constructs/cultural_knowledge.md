# Cultural knowledge
**Type:** Construct  
**Supporting papers:** 13  
**Also known as:** Understanding of Indian culture, Cultural literacy  

## State of the Field

**Space of definitions.** Across the papers, the prevailing usage treats cultural knowledge as a latent or internalized store of culture-specific facts, norms, values, practices, and concepts that a model can encode, access, or retrieve, often when local context or cues such as country, value, language, or region are present. It is commonly framed as what is needed to interpret and answer culturally specific or local queries, including domains such as food, history, legal frameworks, and region-specific practices. A smaller line of work uses the near-overlapping label cultural literacy, emphasizing a shared body of translinguistic cultural and factual knowledge within a community and treating recall of culturally embedded facts as a proxy for that property.

**Space of facets.** Papers break the construct into recurring content areas rather than a single uniform skill: norms and human values, history, cuisine and food artifacts, art, religion, societal beliefs and preferences, geographical markers, and legal or regional practices all appear as parts of it. Some authors explicitly describe it as the "knowledge component" of culture or as stored information that maps a cultural setting to a correct response, while another line contrasts it with broader abilities, arguing that strong performance on cultural test beds can show knowledge of tested cultures without showing the ability to operate in a new culture. Papers also vary in what stands in for it, with one treating language as a proxy for cultural knowledge and another reframing the target as cultural literacy through factual knowledge.

**Space of measurement.** Papers link cultural knowledge to four measurement instruments and one behavioral indicator. The direct measurement instruments are Candle, FilBench, INCLUDE, and M3Exam: these are described as general cultural benchmarks, a Filipino-centric benchmark with a cultural knowledge category, exam and non-translated academic content intended to capture regional and cultural knowledge, and multilingual real-world questions that "require strong multilingual proficiency and cultural knowledge to perform well." These operationalizations mostly align with the dominant definition by testing factual recall or answering with culture-specific facts and local context, although one paper explicitly treats factual recall as a proxy for cultural literacy rather than as the construct itself.

**Links.** Beyond measurement, one paper claims a causal relationship from cultural knowledge to Harmful content detection, with evidence phrased as introducing more comprehensive knowledge about Chinese culture for effectively detecting harmful memes. One paper also reports that cultural knowledge is related to Cultural understanding, with the evidence stating that cultural awareness leverages cultural knowledge to detect inappropriate interactions. No correlational links are reported.

## Sources

**Cultural knowledge** (9 papers: [Is Translation All You Need? A Study on Solving Multilingual Tasks with Large Language Models](https://aclanthology.org/2025.naacl-long.485.pdf), [NormAd: A Framework for Measuring the Cultural Adaptability of Large Language Models](https://aclanthology.org/2025.naacl-long.120.pdf), [Does Mapo Tofu Contain Coffee? Probing LLMs for Food-related Cultural Knowledge](https://aclanthology.org/2025.naacl-long.496.pdf), [CultureInstruct: Curating Multi-Cultural Instructions at Scale](https://aclanthology.org/2025.naacl-long.465.pdf), [WorldCuisines: A Massive-Scale Benchmark for Multilingual and Multicultural Visual Question Answering on Global Cuisines](https://aclanthology.org/2025.naacl-long.167.pdf), [KMMLU: Measuring Massive Multitask Language Understanding in Korean](https://aclanthology.org/2025.naacl-long.206.pdf), [Meta-Cultural Competence: Climbing the Right Hill of Cultural Awareness](https://aclanthology.org/2025.naacl-long.408.pdf), [CaLMQA: Exploring culturally specific long-form question answering across 23 languages](https://aclanthology.org/2025.acl-long.578.pdf), [FilBench: Can LLMs Understand and Generate Filipino?](https://aclanthology.org/2025.emnlp-main.127.pdf))
> The latent trait reflecting an LLM's internalized understanding of cultural norms, values, and practices, which may be accessed when contextual cues such as country or value are provided.

**Cultural literacy** (1 paper: [Do You Know About My Nation? Investigating Multilingual Language Models' Cultural Literacy Through Factual Knowledge](https://aclanthology.org/2025.emnlp-main.756.pdf))
> The shared body of translinguistic cultural and factual knowledge specific to a community or nation, which is essential for effective communication and understanding within that context.

## Relationships

### Cultural knowledge →
- **Harmful content detection** (behavioral indicator): *causes*, 1 paper
  > introducing more comprehensive knowledge about Chinese culture are both crucial for effectively detecting harmful memes. (Section 5.4)
  - [Towards Comprehensive Detection of Chinese Harmful Memes](https://proceedings.neurips.cc/paper_files/paper/2024/file/17fc467c11997914127c001fdc801bea-Paper-Datasets_and_Benchmarks_Track.pdf)
- **INCLUDE** (measurement instrument): *measured_by*, 1 paper
  > Our data collection focuses on license and certification exams that capture regional knowledge of specific countries (in their official languages), and non-translated academic content from the humanities and social sciences to capture cultural knowledge. (Section 3.1)
  - [INCLUDE: Evaluating Multilingual Language Understanding with Regional Knowledge](https://proceedings.iclr.cc/paper_files/paper/2025/file/ced46a50befedcb884ccf0cbe8c3ad23-Paper-Conference.pdf)
- **M3Exam** (measurement instrument): *measured_by*, 1 paper
  > we choose M3Exam (Zhang et al., 2023a), as the questions are real-world natural data from different languages instead of translating from English and require strong multilingual proficiency and cultural knowledge to perform well. (Section 3.3)
  - [Is Translation All You Need? A Study on Solving Multilingual Tasks with Large Language Models](https://aclanthology.org/2025.naacl-long.485.pdf)
- **Candle** (measurement instrument): *measured_by*, 1 paper
  > Fine-tuning with CULTUREINSTRUCT outperforms the base LLMs significantly on multiple types of cultural benchmarks, including: (i) benchmarks for general cultural knowledge - CULTURALBENCH (Chiu et al., 2024), CANDLE (Nguyen et al., 2023), and ETICOR (Dwivedi et al., 2023) (Section 4.1)
  - [CultureInstruct: Curating Multi-Cultural Instructions at Scale](https://aclanthology.org/2025.naacl-long.465.pdf)
- **FilBench** (measurement instrument): *measured_by*, 1 paper
  > “FILBENCH, a Filipino-centric benchmark designed to evaluate LLMs across a diverse set of tasks and capabilities in Filipino, Tagalog, and Cebuano. We carefully curate the tasks in FILBENCH to reflect the priorities and trends of NLP research in the Philippines such as Cultural Knowledge”
  - [FilBench: Can LLMs Understand and Generate Filipino?](https://aclanthology.org/2025.emnlp-main.127.pdf)

### Associated with
- **Cultural understanding** (construct), 1 paper
  > Cultural Awareness, which leverages cultural knowledge to detect inappropriate interactions.
  - [SocialCC: Interactive Evaluation for Cultural Competence in Language Agents](https://aclanthology.org/2025.acl-long.1594.pdf)
