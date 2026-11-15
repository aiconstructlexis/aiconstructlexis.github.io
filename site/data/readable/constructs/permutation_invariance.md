# Permutation invariance
**Type:** Construct  
**Supporting papers:** 3  

## State of the Field

**Space of definitions.** The cited definition treats permutation invariance as an in-context learning property under which the prediction for a test query stays the same regardless of the order of the context examples. The formal statement makes this explicit at the level of the last prediction: an ICL algorithm is invariant when that prediction is unchanged under any permutation of the context examples, and no alternative framing is provided.

**Space of facets.** In the cited material, it is framed as a property of an in-context learning algorithm, specifically of how its last prediction behaves when the context examples are reordered. The material does not introduce facets, subtypes, or competing names, although one quoted passage notes that recent studies have proposed several variant ICL algorithms that achieve permutation invariance.

**Space of measurement.** No measurement instrument is linked to it, and no behavioral indicator is linked to it. The only explicit operational criterion stated in the cited work is formal: the algorithm counts as permutation invariant when its last prediction remains the same for any permutation of the context examples.

**Links.** Its only linked construct is Generalization. One paper claims a causal relationship from permutation invariance to generalization, stating that improvement is primarily attributed to exploiting the "permutation invariance of code," thereby enhancing generalization capabilities.

## Sources

**Permutation invariance** (1 paper: [Rethinking Invariance in In-context Learning](https://proceedings.iclr.cc/paper_files/paper/2025/file/01e8ecf628f8d9f62a1fd433d44d34ab-Paper-Conference.pdf))
> The property of an in-context learning algorithm where its prediction for a test query remains the same regardless of the order of the context examples provided.

## Relationships

### Permutation invariance →
- **Generalization** (construct): *causes*, 1 paper
  > This improvement is primarily attributed to its ability to exploit permutation invariance of code, thereby enhancing the model’s generalization capabilities. (Section 5.2)
  - [Beyond Sequences: Two-dimensional Representation and Dependency Encoding for Code Generation](https://aclanthology.org/2025.acl-long.308.pdf)
