# Sudoku solving
**Type:** Behavioral indicator  
**Supporting papers:** 4  

## State of the Field

**Space of definitions.** Across papers, the prevailing usage is completing a partially filled Sudoku grid so that all row, column, and box or subgrid constraints are satisfied. Most descriptions treat success as filling the remaining cells of the whole board, with one formulation stating that the board should contain numbers 1 to 9 without duplicates in each row, column, and box. Some task setups add procedural or output requirements, such as first searching over empty cells to decide which cell to fill, or returning the solved puzzle without extraneous text.

**Variants.** The variants mentioned are mostly about setting and format rather than different success criteria. Papers describe Sudoku solving both as puzzles presented in a textual format and as 9 × 9 Sudoku problems; a smaller variation requires an answer-only output, while another frames solving as an iterative process that searches over empty cells before filling a chosen cell. The name also appears as "Sudoku-solving" in one task description.

**Space of elicitation and scores.** The papers do not link Sudoku solving to any measurement instrument.

**What it is taken as evidence of.** The recorded relationships do not present Sudoku solving as evidence of a single construct. Instead, it is linked to three constructs through related relationships: Complex reasoning, Exploration ability, and Long-horizon planning. The link to complex reasoning is supported by language describing Sudoku as a challenging constraint satisfaction problem where assigning even one cell can require multiple reasoning steps, the link to exploration ability is tied to an iterative search for a cell where a strategy can be applied, and the link to long-horizon planning is qualified by the claim that Sudoku does not require the same degree of long-term planning as some harder benchmarks.

## Sources

**Sudoku solving** (3 papers: [Causal language modeling can elicit search and reasoning capabilities on logic puzzles](https://proceedings.neurips.cc/paper_files/paper/2024/file/67b31ca159553d5593e62d7b998d63ea-Paper-Conference.pdf), [Controllable Generation via Locally Constrained Resampling](https://proceedings.iclr.cc/paper_files/paper/2025/file/d98ce7a82af78cd02968e79ea3fe89e8-Paper-Conference.pdf), [PAK-UCB Contextual Bandit: An Online Learning Approach to Prompt-Aware Selection of Generative Models and LLMs](https://raw.githubusercontent.com/mlresearch/v267/main/assets/hu25m/hu25m.pdf))
> Filling in the values of a partially completed Sudoku grid so that all row, column, and box constraints are satisfied.

## Relationships

### Associated with
- **Exploration ability** (construct), 1 paper
  > “The iterative process of solving Sudokus can be broken down into two steps: (1) searching and finding a cell position where we can apply a subset of the strategies”
  - [Causal language modeling can elicit search and reasoning capabilities on logic puzzles](https://proceedings.neurips.cc/paper_files/paper/2024/file/67b31ca159553d5593e62d7b998d63ea-Paper-Conference.pdf)
- **Complex reasoning** (construct), 1 paper
  > The Sudoku environment is a highly challenging Constraint Satisfaction Problem (CSP) and determining the value in even a single cell can require highly complex reasoning involving multiple steps. (Section 1)
  - [Causal language modeling can elicit search and reasoning capabilities on logic puzzles](https://proceedings.neurips.cc/paper_files/paper/2024/file/67b31ca159553d5593e62d7b998d63ea-Paper-Conference.pdf)
- **Long-horizon planning** (construct), 1 paper
  > Sudoku is a task which doesn't require the same degree of long-term planning as some harder benchmarks
  - [Causal language modeling can elicit search and reasoning capabilities on logic puzzles](https://proceedings.neurips.cc/paper_files/paper/2024/file/67b31ca159553d5593e62d7b998d63ea-Paper-Conference.pdf)
