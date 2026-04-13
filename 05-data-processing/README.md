# 05 - 数据处理

## 方向概述

**数据处理 (Data Processing)** 涵盖数据清洗、过滤、去重、格式转换等基础但关键的环节。在大模型时代，面对海量的预训练和微调数据，高效且高质量的数据处理流程是 DCAI 的基石。

核心主题：
- **Data Cleaning** -- 检测并修正数据中的噪声、错误标签和异常值
- **Data Filtering** -- 根据质量指标过滤低质量数据
- **Data Deduplication** -- 去除重复和近重复数据
- **Scaling Laws for Data** -- 数据量、数据质量与模型性能之间的关系

## 推荐论文

> 注：⚡ 为基础必读，💎 为基础选读，💡 为进阶阅读

- ⚡ [LLM-Enhanced Data Management](https://arxiv.org/abs/2402.02643) -- LLM 增强的数据管理
- ⚡ [Scaling Laws for Data Filtering -- Data Curation cannot be Computed](https://openaccess.thecvf.com/content/CVPR2024/html/Goyal_Scaling_Laws_for_Data_Filtering--_Data_Curation_cannot_be_Compute_CVPR_2024_paper.html) -- 数据过滤的 Scaling Laws
- ⚡ [Improving CLIP Training with Language Rewrites](https://proceedings.neurips.cc/paper_files/paper/2023/hash/6fa4d985e7c434002fb6289ab9b2d654-Abstract-Conference.html) -- 通过语言重写改进 CLIP 训练数据
- 💎 [Deduplicating Training Data Makes Language Models Better](https://arxiv.org/abs/2107.06499) -- 数据去重对 LM 的影响

## 学习建议

1. 数据处理看似基础，但在实际项目中是工作量最大的部分
2. 重点理解 Scaling Laws —— 不是数据越多越好，数据质量和数据量之间存在微妙的平衡
3. 建议结合 [09-dcai-tools](../09-dcai-tools/) 了解 Data Juicer 等工具的实际使用

---

[← 数据评估](../04-data-evaluation/) | [返回主页](../README.md) | [下一节: 多模态数据侧 →](../06-multimodal-data-centric/)
