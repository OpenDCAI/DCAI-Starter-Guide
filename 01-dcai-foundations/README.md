# 01 - DCAI 基础：Data-Centric AI 核心概念与课程

## 方向概述

**Data-Centric AI (DCAI)** 是一种系统性地关注数据质量、数据组织和数据流程的 AI 研究范式。与传统的 Model-Centric 方法（固定数据、迭代模型）不同，DCAI 强调在固定模型架构的前提下，通过改进训练数据来提升模型性能。

核心研究主题包括：
- **Data Selection** -- 从大规模数据中选择高质量子集
- **Data Cleaning** -- 检测和修正数据中的噪声与错误
- **Data Mixing / Curation** -- 多领域数据的配比策略
- **Distribution Shift** -- 处理训练和部署环境间的分布差异
- **Data Generation** -- 合成高质量训练数据

## 必修课程

> 注：⚡ 为基础必读

- ⚡ [MIT DCAI 2024](https://dcai.csail.mit.edu/) -- 课程难度不大，但涵盖了很多 DCAI 的 Topic，包括 Data Selection / Data Cleaning / Distribution Shift / Data Curation 等。每节课都有一个配套的实验，完成难度也不大，完成后可以对该 topic 有一个比较 general 的认识
- ⚡ [华盛顿大学 DCAI (CSE 599J)](https://koh.pw/cse599j/) -- 较新的课程，覆盖 DCAI 前沿研究

## 领域综述

- ⚡ [Data-centric Artificial Intelligence: A Survey](https://arxiv.org/abs/2303.10158) -- DCAI 领域全面综述，系统梳理了数据质量、数据量和数据治理的方法论
- ⚡ [Towards Next-Generation LLM Training: From the Data-Centric Perspective](https://arxiv.org/abs/2603.14712) -- 从 DCAI 视角审视下一代 LLM 训练范式（组里的综述）
- 💎 [A Survey of Multimodal Large Language Model from A Data-centric Perspective](https://arxiv.org/abs/2405.16640) -- 多模态 LLM 数据侧综述
- 💎 [DataComp: In Search of the Next Generation of Multimodal Datasets](https://arxiv.org/abs/2304.14108) -- 通过数据竞赛证明"选对数据"比"换模型"更有效，DCAI 思想的实证体现

## 学习建议

1. **先完成 MIT DCAI 课程的实验**：这些实验能帮助你对各个 DCAI 子方向建立直觉认识
2. **浏览综述建立全局观**：读完综述后再选择感兴趣的子方向深入
3. **结合后续模块**：本模块是概览，具体的 Data Selection、Data Generation 等方法论在后续模块 (02-06) 中详细展开

---

[← 前置知识](../00-prerequisites/) | [返回主页](../README.md) | [下一节: 数据选择与配比 →](../02-data-selection-and-mixing/)
