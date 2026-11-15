# Anomaly detection
**Type:** Behavioral indicator  
**Supporting papers:** 5  
**Also known as:** Anomaly Detection, Anomaly discrimination  

## State of the Field

**Space of definitions.** Papers most commonly treat this behavior as identifying whether something in a sequence or sample is abnormal, though the target of judgment varies by task. One framing asks models to predict whether a sequence of log events indicates abnormal system behavior, and describes log-based anomaly detection as "fundamentally a time-series prediction task." Another framing defines it as finding an out-of-place event after one event type in a series has been randomly replaced, where the goal is to identify the incorrect element. A further use treats it as judging whether an industrial image contains a defect or anomaly, phrased as asking whether a sample has defects.

**Variants.** The papers use both "anomaly detection" and "anomaly discrimination" for related task formulations. The studied variants include log-event sequences, where the output is an abnormal versus normal judgment for the sequence; event-sequence anomaly finding, where one replaced event must be located; and industrial image inspection, where the task is to answer questions such as whether there is any defect in the object. These variants differ in modality and in whether success means classifying a whole sample or identifying a specific anomalous element.

**Space of elicitation and scores.** No measurement instrument is linked to it.

**What it is taken as evidence of.** No construct is linked to it as something this behavior measures or indicates.

## Sources

**Anomaly Detection** (1 paper: [RuAG: Learned-rule-augmented Generation for Large Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/file/5d7e8991f75f3e5af14edf7aebb5be5e-Paper-Conference.pdf))
> Predicting whether a sequence of log events indicates abnormal system behavior.

**Anomaly detection** (1 paper: [LAST SToP for Modeling Asynchronous Time Series](https://raw.githubusercontent.com/mlresearch/v267/main/assets/gupta25a/gupta25a.pdf))
> Identifying an out-of-place event in a sequence when one event type has been replaced.

**Anomaly discrimination** (1 paper: [MMAD: A Comprehensive Benchmark for Multimodal Large Language Models in Industrial Anomaly Detection](https://proceedings.iclr.cc/paper_files/paper/2025/file/d91ffbe9c126765755ff52d36b715683-Paper-Conference.pdf))
> Judging whether an industrial image contains a defect or anomaly.
