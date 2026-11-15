# Backdoor-triggered misclassification
**Type:** Behavioral indicator  
**Supporting papers:** 2  
**Also known as:** Triggered misclassification, Backdoor-triggered classification  

## State of the Field

The observable behavior in which a model incorrectly classifies inputs that contain a backdoor trigger, producing a targeted adversarial output.

## Sources

**Triggered misclassification** (1 paper: [Backdoor Attacks in Token Selection of Attention Mechanism](https://raw.githubusercontent.com/mlresearch/v267/main/assets/wang25c/wang25c.pdf))
> The observable behavior in which a model incorrectly classifies inputs that contain a backdoor trigger, producing a targeted adversarial output.

**Backdoor-triggered classification** (1 paper: [Demystifying Poisoning Backdoor Attacks from a Statistical Perspective](https://proceedings.iclr.cc/paper_files/paper/2024/file/4488bf8354049b1cd592b6418dc30466-Paper-Conference.pdf))
> Classifying triggered inputs into the attacker’s target label when the backdoor trigger is present.

## Relationships

### → Backdoor-triggered misclassification
- **Backdoor vulnerability** (construct): *causes*, 1 paper
  > “backdoor attacks are particularly insidious: they introduce ‘poisoned triggers’ ... When a trigger is present, the model produces an adversarial response; otherwise, it behaves normally.”
  - [Backdoor Attacks in Token Selection of Attention Mechanism](https://raw.githubusercontent.com/mlresearch/v267/main/assets/wang25c/wang25c.pdf)
