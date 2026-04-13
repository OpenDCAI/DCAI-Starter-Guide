# 03 - 数据生成

## 方向概述

**数据生成**主要是通过大语言模型、Diffusion Model 等生成模型，生成高质量数据并用于训练模型。核心挑战在于：

- 大模型的生成数据和原始训练数据分布有较大差异
- 控制生成数据的分布仍然十分困难
- 需要提升生成数据的**可控性**和**多样性**

终极形态可能是自我对抗学习——模型自我生产数据进行学习，无需再收集训练数据（类似 AlphaGo）。

## 推荐论文

> 注：⚡ 为基础必读，💎 为基础选读，💡 为进阶阅读

### 综述

- ⚡ [Comprehensive Exploration of Synthetic Data Generation: A Survey](https://arxiv.org/abs/2401.02524) -- 合成数据生成全面综述
- ⚡ [On LLMs-Driven Synthetic Data Generation, Curation, and Evaluation: A Survey](https://arxiv.org/abs/2406.15126) -- LLM 驱动的数据生成综述

### 代表性工作

- ⚡ [MAGPIE: Alignment Data Synthesis from Scratch by Prompting Aligned LLMs with Nothing](https://arxiv.org/abs/2406.08464) -- 仅通过 Prompt 对齐的 LLM 从零生成对齐数据
- 💎 [Self-Instruct: Aligning Language Models with Self-Generated Instructions](https://arxiv.org/abs/2212.10560) -- 自动生成指令数据的经典工作
- 💎 [Evol-Instruct: WizardLM](https://arxiv.org/abs/2304.12244) -- 渐进式数据增强

### 大模型的思考与数据生成

- 💡 [GPT 等大模型思考机制](https://arxiv.org/abs/2409.12917) -- 基于 RL 的思考机制研究
- 💡 自我对抗学习方向：模型如何 Verify 自身输出的正确性

## 学习建议

1. 先阅读综述了解数据生成的全貌
2. 关注**生成数据分布**与**可控性**这两个核心问题
3. 思考数据生成与 RLHF 的关系——生成数据本质上也是一种数据增强

---

[← 数据选择与配比](../02-data-selection-and-mixing/) | [返回主页](../README.md) | [下一节: 数据评估 →](../04-data-evaluation/)
