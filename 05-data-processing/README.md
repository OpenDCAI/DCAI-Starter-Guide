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

### 数据清洗与过滤 Pipeline

- ⚡ [The RefinedWeb Dataset for Falcon LLM](https://arxiv.org/abs/2306.01116) (NeurIPS 2023) -- **Web 数据清洗的标杆工程**：MacroData Refinement (MDR) 流水线，仅用清洗后的 Web 数据训练出超越 The Pile 的模型，证明"好的数据处理 = 好的数据"
- ⚡ [CCNet: Extracting High Quality Monolingual Datasets from Web Crawl Data](https://arxiv.org/abs/1911.00359) (LREC 2020) -- 从 CommonCrawl 中提取高质量单语数据的经典方法，基于 n-gram 语言模型的困惑度过滤，LLaMA 预训练数据处理的基础

### 数据去重

- ⚡ [Deduplicating Training Data Makes Language Models Better](https://arxiv.org/abs/2107.06499) (ACL 2022) -- **去重的必读论文**：详细分析了精确去重和近似去重（MinHash）对 LM 训练的影响，发现去重能同时减少记忆化和提高性能
- 💎 [SemDeDup: Data-efficient Learning at Web-scale through Semantic Deduplication](https://arxiv.org/abs/2303.09540) (ICLR 2024) -- 语义层面的去重，利用 embedding 距离找语义近重复数据

### Scaling Laws 与数据工程

- ⚡ [Scaling Laws for Data Filtering -- Data Curation cannot be Computed](https://openaccess.thecvf.com/content/CVPR2024/html/Goyal_Scaling_Laws_for_Data_Filtering--_Data_Curation_cannot_be_Compute_CVPR_2024_paper.html) -- 数据过滤的 Scaling Laws，质量和数量的 trade-off
- 💎 [LLM-Enhanced Data Management](https://arxiv.org/abs/2402.02643) -- LLM 增强的数据管理
- 💎 [Improving CLIP Training with Language Rewrites](https://proceedings.neurips.cc/paper_files/paper/2023/hash/6fa4d985e7c434002fb6289ab9b2d654-Abstract-Conference.html) -- 通过语言重写改进 CLIP 训练数据

## 学习建议

1. **从 RefinedWeb 入手**：这篇论文完整展示了工业级 Web 数据处理流程，包括 URL 过滤、文本提取、启发式规则、去重的完整 pipeline
2. **理解去重的重要性**：Lee et al. (2021) 的去重论文是必读，"训练数据去重"是最低成本、最高收益的数据处理操作
3. 重点理解 Scaling Laws —— 不是数据越多越好，数据质量和数据量之间存在微妙的平衡
4. 建议结合 [09-dcai-tools](../09-dcai-tools/) 了解 DataFlow 的实际使用

---

[← 数据评估](../04-data-evaluation/) | [返回主页](../README.md) | [下一节: 多模态数据侧 →](../06-multimodal-data-centric/)
