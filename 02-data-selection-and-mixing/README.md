# 02 - 数据选择与配比

## 方向概述

**数据选择 (Data Selection)** 是通过 Influence Function、梯度信号、Loss 等指标筛选高质量数据，在保证训练效率 (Efficiency) 的同时提升模型效果 (Effectiveness)。

**数据配比 (Data Mixing)** 是通过多个领域的数据进行合理配比，让大模型能够获得多个领域的能力，平衡通用性和专业性。

**数据加权 (Data Reweighting)** 是在训练过程中动态调整每个样本的权重，让模型更关注高价值数据。

> 分类参考：[DataFlex 论文总结](https://arxiv.org/abs/2603.26164)

## 推荐论文

> 注：⚡ 为基础必读，💎 为基础选读，💡 为进阶阅读

### 基础方法：如何衡量一条数据的价值

- ⚡ [Understanding Black-box Predictions via Influence Functions](https://arxiv.org/abs/1703.04730) (ICML 2017) -- **Influence Function 的开山之作**：如何计算一条训练数据对模型预测的影响，Data Selection 的理论基础
- ⚡ [Estimating Training Data Influence by Tracing Gradient Descent (TracIn)](https://arxiv.org/abs/2002.08484) (NeurIPS 2020) -- 比 Influence Function 更简单的替代方案，通过追踪训练过程中梯度变化来衡量数据影响力
- 💎 [Data Shapley: Equitable Valuation of Data for Machine Learning](https://arxiv.org/abs/1904.02868) (ICML 2019) -- 用博弈论中的 Shapley 值公平衡量每条数据的贡献

### 数据点选择：从大数据集中选出高价值子集

**基于梯度 (Gradient-Based)**

- ⚡ [LESS: Selecting Influential Data for Targeted Instruction Tuning](https://arxiv.org/abs/2402.04333) (ICML 2024) -- 用低秩梯度相似性搜索选数据，5% 数据常优于全量训练，已集成于 DataFlex
- 💎 [NICE: Data Selection for Instruction Tuning with Non-differentiable Evaluation Metric](https://arxiv.org/abs/2406.14434) -- 将 LESS 思路扩展到不可导指标，通过 RL policy 迂回计算梯度

**基于 Loss (Loss-Based)**

- ⚡ [MATES: Model-Aware Data Selection for Efficient Pretraining](https://arxiv.org/abs/2406.06046) -- 用 loss 变化作为影响力代理，训练小模型预测大批数据的价值，动态选择
- 💎 [Preference Curriculum: LLMs Should Always Be Pretrained on Their Preferred Data](https://arxiv.org/abs/2407.20227) -- 用训练前后的相对 loss 差打分排序，从易到难训练

**基于数据分布 (Distribution-Based)**

- 💎 [Data Selection for Language Models via Importance Resampling (DSIR)](https://arxiv.org/abs/2302.03169) -- 基于重要性采样选择与目标分布匹配的数据

### 领域配比：多领域数据如何混合

**基于 Loss**

- ⚡ [DoReMi: Optimizing Data Mixtures Speeds Up Language Model Pretraining](https://arxiv.org/abs/2305.10429) -- 用小型代理模型优化数据配比，经典方法
- 💎 [Aioli: A Unified Optimization Framework for Language Model Data Mixing](https://arxiv.org/abs/2411.05735) -- 统一优化框架，通过领域间交互矩阵动态计算最优配比

**基于梯度**

- 💎 [DoGE: Domain Reweighting with Generalization Estimation](https://arxiv.org/abs/2310.15393) -- 计算训练域和验证域的梯度内积来分配权重，公式清晰

### 数据加权：训练中动态调整样本权重

- 💡 [Dynamic Loss-Based Sample Reweighting for Improved Large Language Model Pretraining](https://arxiv.org/abs/2410.07145) -- 对每个 batch 先算 loss 再计算权重做加权反向传播，简单但有效

### 综合参考

- 💎 [Scaling Laws for Data Filtering -- Data Curation cannot be Computed](https://openaccess.thecvf.com/content/CVPR2024/html/Goyal_Scaling_Laws_for_Data_Filtering--_Data_Curation_cannot_be_Compute_CVPR_2024_paper.html) -- 数据过滤的 Scaling Laws
- 💎 [SlimPajama-DC: Understanding Data Combinations for LLM Training](https://arxiv.org/abs/2309.10818) -- 数据组合对 LLM 训练的影响

## 学习建议

1. **先理解 Influence Function**（1703.04730）：这是所有数据选择方法的理论基础，理解"一条数据如何影响模型"
2. **再看 LESS**：它是 Influence Function 在 LLM 指令微调中的实用化版本，也是 DataFlex 的核心算法之一
3. **领域配比看 DoReMi**：理解多领域预训练时为什么配比很重要
4. **动手实践**：结合 [09-dcai-tools](../09-dcai-tools/) 中的 DataFlex，实际跑一遍 LESS 数据选择流程

---

[← DCAI 基础](../01-dcai-foundations/) | [返回主页](../README.md) | [下一节: 数据生成 →](../03-data-generation/)
