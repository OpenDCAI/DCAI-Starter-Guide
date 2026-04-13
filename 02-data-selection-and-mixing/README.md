# 02 - 数据选择与配比

## 方向概述

**数据选择 (Data Selection)** 是通过大语言模型、Metric 等指标筛选高质量数据，在保证训练效率 (Efficiency) 的同时提升模型效果 (Effectiveness)。

**数据配比 (Data Mixing)** 是通过多个领域的数据进行合理配比，让大模型能够获得多个领域的能力，平衡通用性和专业性。

## 推荐论文

### 数据选择

> 注：⚡ 为基础必读，💎 为基础选读，💡 为进阶阅读

- ⚡ [Scaling Laws for Data Filtering -- Data Curation cannot be Computed](https://openaccess.thecvf.com/content/CVPR2024/html/Goyal_Scaling_Laws_for_Data_Filtering--_Data_Curation_cannot_be_Compute_CVPR_2024_paper.html) -- 数据过滤的 Scaling Laws
- ⚡ [LLM as Dataset Analyst: Subpopulation Structure Discovery with Large Language Model](https://arxiv.org/abs/2405.02363) -- 用 LLM 分析数据集结构
- 💎 [Data Selection for Language Models via Importance Resampling](https://arxiv.org/abs/2302.03169) -- 基于重要性采样的数据选择
- 💎 [DoReMi: Optimizing Data Mixtures Speeds Up Language Model Pretraining](https://arxiv.org/abs/2305.10429) -- 优化数据配比加速预训练

### 数据配比

- ⚡ [DoReMi: Optimizing Data Mixtures Speeds Up Language Model Pretraining](https://arxiv.org/abs/2305.10429) -- 使用小型代理模型优化数据配比
- 💎 [SlimPajama-DC: Understanding Data Combinations for LLM Training](https://arxiv.org/abs/2309.10818) -- 数据组合对 LLM 训练的影响

## 学习建议

1. 先理解数据选择的核心动机：为什么"选对数据"比"用更多数据"更重要
2. 关注 Scaling Laws 相关工作，理解数据量和数据质量之间的关系
3. 数据配比是预训练阶段的关键问题，建议结合 LLM 预训练流程一起理解

---

[← DCAI 基础](../01-dcai-foundations/) | [返回主页](../README.md) | [下一节: 数据生成 →](../03-data-generation/)
