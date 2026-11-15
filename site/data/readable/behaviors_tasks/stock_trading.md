# Stock trading
**Type:** Behavioral indicator  
**Supporting papers:** 3  
**Also known as:** Single stock trading  

## State of the Field

**Space of definitions.** Across the definitions, the prevailing usage is a decision task that ends in one action, buy, sell, or hold, based on financial information or market context. Both definitions align on that output space, though one is narrower, focusing on individual stocks and "multi-modal market information processing," while the other states the task more generally as making decisions from financial information and market context. One prompt formulation further specifies that the model should provide exactly one investment decision, and may choose hold when a buy-or-sell call is hard.

**Variants.** The main named variant is single stock trading, where decisions are generated for individual stocks. Other descriptions keep the label broader as stock trading from financial information and market context, and one quoted passage places it among sequential financial tasks in which a sole decision-maker generates trading actions.

**Space of elicitation and scores.** No measurement instrument is linked to it. Instead, the papers operationalize it through the decision format itself: one prompt asks for exactly one investment decision, buy or sell, with hold allowed when the choice is hard, and another description has a manager agent generate trading actions as the sole decision-maker for sequential financial tasks.

**What it is taken as evidence of.** Only one construct is linked to it, Decision-making, and the link is related rather than a measurement claim. In that relationship, decision-making is described as proficiency in making informed financial decisions, such as developing trading strategies and optimizing investment portfolios, which places stock trading alongside those behaviors. No other construct is linked to it.

## Sources

**Single stock trading** (1 paper: [FinCon: A Synthesized LLM Multi-Agent System with Conceptual Verbal Reinforcement for Enhanced Financial Decision Making](https://proceedings.neurips.cc/paper_files/paper/2024/file/f7ae4fe91d96f50abc2211f09b6a7e49-Paper-Conference.pdf))
> Generating trading decisions (buy, sell, hold) for individual stocks based on multi-modal market information processing.

**Stock trading** (1 paper: [FinBen: A Holistic Financial Benchmark for Large Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/adb1d9fa8be4576d28703b396b82ba1b-Paper-Datasets_and_Benchmarks_Track.pdf))
> Making buy, sell, or hold decisions from financial information and market context.

## Relationships

### Associated with
- **Decision-making** (construct), 1 paper
  > Decision-Making assesses the model’s proficiency in making informed financial decisions, such as developing trading strategies and optimizing investment portfolios (Paiva et al., 2019).
  - [FinBen: A Holistic Financial Benchmark for Large Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/adb1d9fa8be4576d28703b396b82ba1b-Paper-Datasets_and_Benchmarks_Track.pdf)
