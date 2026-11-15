# Recursive stability
**Type:** Construct  
**Supporting papers:** 1  

## State of the Field

A property of a generative model in a self-consuming training loop that quantifies how much its output distribution changes in response to small perturbations in the initial real dataset across multiple generations.

## Sources

**Recursive stability** (1 paper: [A Theoretical Perspective: How to Prevent Model Collapse in Self-consuming Training Loops](https://proceedings.iclr.cc/paper_files/paper/2025/file/e92e6d20f7b5db5c2a1b23964d170fe2-Paper-Conference.pdf))
> A property of a generative model in a self-consuming training loop that quantifies how much its output distribution changes in response to small perturbations in the initial real dataset across multiple generations.

## Relationships

### Recursive stability →
- **Model collapse** (construct): *causes*, 1 paper
  > Theorem 1 demonstrates that under a recursive stability condition and a non-negligible constant level of real data, model collapse can be avoided across a variety of model architectures.
  - [A Theoretical Perspective: How to Prevent Model Collapse in Self-consuming Training Loops](https://proceedings.iclr.cc/paper_files/paper/2025/file/e92e6d20f7b5db5c2a1b23964d170fe2-Paper-Conference.pdf)
- **Generalization** (construct): *causes*, 1 paper
  > Moreover, we demonstrate that the generalization error converges under the following conditions: (1) the generative model satisfies recursive stability, and (2) the proportion of real data is maintained at a non-negligible constant level, thus preventing model collapse.
  - [A Theoretical Perspective: How to Prevent Model Collapse in Self-consuming Training Loops](https://proceedings.iclr.cc/paper_files/paper/2025/file/e92e6d20f7b5db5c2a1b23964d170fe2-Paper-Conference.pdf)

### Associated with
- **In-context learning** (construct), 1 paper
  > 2. Application to Transformers in In-Context Learning: This paper is the first to extend the theoretical framework to transformer models in in-context learning. We prove that transformers in this setting satisfy recursive stability
  - [A Theoretical Perspective: How to Prevent Model Collapse in Self-consuming Training Loops](https://proceedings.iclr.cc/paper_files/paper/2025/file/e92e6d20f7b5db5c2a1b23964d170fe2-Paper-Conference.pdf)
