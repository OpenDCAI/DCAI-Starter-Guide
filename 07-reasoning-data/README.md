# 07 - 强推理模型与数据

## 方向概述

强推理模型与数据方向关注 Math、Code、STEM、Science 等需要深度推理能力的领域。研究重点包括：

- **MathLLMs** -- 专门为解决数学问题而设计的大语言模型，研究针对不同训练阶段（PT / SFT / RL）数据的准备、合成、处理、评估
- **推理数据合成** -- 如何为推理任务构造高质量训练数据
- **后训练阶段数据** -- SFT 和 RLHF 阶段的数据准备是研究重点

数学模型可以分为：非证明类、证明类、几何类问题。数据形式可以分为 question、answer、对话等。

## 推荐论文

> 注：⚡ 为基础必读，💎 为基础选读，💡 为进阶阅读

### 通用推理模型

- ⚡ [Qwen3 Technical Report](https://arxiv.org/abs/2505.09388) -- 通用推理模型
- ⚡ [NVIDIA Reasoning Model](https://arxiv.org/abs/2505.00949) -- NVIDIA 推理模型
- 💎 [Microsoft Reasoning Model](https://arxiv.org/abs/2504.21318) -- Microsoft 推理模型
- 💎 [小米推理模型](https://www.arxiv.org/abs/2505.07608)

### MathLLMs

- ⚡ [DeepSeekMath: Pushing the Limits of Mathematical Reasoning](https://arxiv.org/abs/2402.03300)
- ⚡ [Qwen2.5-Math](https://arxiv.org/abs/2409.12122)
- ⚡ [DeepSeek-Prover](https://arxiv.org/abs/2504.21801) -- 数学证明方向
- 💎 [InternLM-Math](https://arxiv.org/abs/2402.06332)
- 💎 [MathBench: Evaluating LLMs with a Hierarchical Mathematics Benchmark](https://arxiv.org/abs/2405.12209)

### 推理数据合成与处理

- ⚡ [Math Dataset Survey](https://arxiv.org/pdf/2504.16891)
- ⚡ [Math Data Construction](https://arxiv.org/abs/2504.11456)
- 💎 [DeepSeekMath Dataset](https://arxiv.org/abs/2402.03300) -- 数学知识按难度分为小学、初中、高中和大学

> **观察**：无论是否是 Math 模型，在 SFT 之后高中和大学数学能力都会大幅度下降，说明数据集的构建不利于高中和大学数学能力的学习。

### Code & STEM 推理数据

- ⚡ [StarCoder 2 and The Stack v2: The Next Generation](https://arxiv.org/abs/2402.19173) -- **代码数据处理的标杆**：619 种语言、67.5TB 代码数据的完整处理流水线，包含去重、PII 去除、质量过滤等，是数据工程在代码领域的最佳实践
- ⚡ [OpenCoder: The Open Cookbook for Top-Tier Code LLMs](https://arxiv.org/abs/2411.04905) -- 开源代码模型完整数据手册，详细公开了数据配比、清洗、去重、退火策略
- 💎 [DeepSeek-Coder-V2: Breaking the Barrier of Closed-Source Models in Code Intelligence](https://arxiv.org/abs/2406.11931) -- 代码模型训练中 MoE + 多阶段数据策略的成功案例
- 💎 [SciLitLLM: How to Adapt LLMs for Scientific Literature Understanding](https://arxiv.org/abs/2408.15545) -- 面向科学文献理解的 LLM 适配方法

## 实战配套

本模块有一个完整的实战教程 **[08-llm-math-guide](../08-llm-math-guide/)**，使用 LLaMA-Factory 在 GSM8K 数据集上微调 Qwen2.5 模型，覆盖从数据准备到模型评估的完整 Pipeline。

## 学习建议

1. 先阅读 DeepSeekMath 和 Qwen2.5-Math 了解当前 MathLLM 的训练范式
2. 然后跟着 [08-llm-math-guide](../08-llm-math-guide/) 动手实践一次完整的微调流程
3. 关注后训练阶段（SFT + RL）的数据准备方法，这是当前研究的重点

---

[← 多模态数据侧](../06-multimodal-data-centric/) | [返回主页](../README.md) | [下一节: 实战 LLM 数学微调 →](../08-llm-math-guide/)
