# 04 - 数据评估

## 方向概述

**数据评估**是 Data-Centric AI 中的关键环节，目标是量化数据的质量、多样性和对模型训练的价值。高质量的数据评估指标可以指导数据选择、过滤和生成环节，形成数据质量的闭环优化。

## 推荐论文

> 注：⚡ 为基础必读，💎 为基础选读，💡 为进阶阅读

### 数据评估综合

- ⚡ [Awesome Data Evaluation](https://github.com/Open-DataFlow/Open-DataFlow-Eval/blob/main/Awesome_Data_Evaluation.md) -- 数据评估方向的论文与资源汇总

### Image 数据评估

- ⚡ [CLIPScore: A Reference-free Evaluation Metric for Image Captioning](https://arxiv.org/abs/2104.08718) -- 基于 CLIP 的无参考图像描述评估
- ⚡ [InfoMetIC: An Informative Metric for Reference-free Image Caption Evaluation](https://aclanthology.org/2023.acl-long.178.pdf) -- 信息量驱动的图像描述评估
- 💎 [Leveraging Large Multimodal Model for Image Caption Evaluation](https://arxiv.org/pdf/2406.06004) -- 利用大型多模态模型进行评估
- 💎 [Image Caption Evaluation with LMM](https://arxiv.org/pdf/2407.18589) -- 最新 follow-up 工作

### Video 数据评估

- ⚡ [EMScore: Evaluating Video Captioning via Coarse-Grained and Fine-Grained Embedding Matching](https://arxiv.org/abs/2111.08919) -- 多粒度视频描述评估
- ⚡ [PAC-S: Positive-Augmented Contrastive Learning for Image and Video Captioning Evaluation](https://arxiv.org/abs/2303.12112) -- 正增强对比学习评估

## 学习建议

1. 从 CLIPScore 入手理解无参考评估 (Reference-free) 的基本思路
2. 关注多模态评估指标的发展——如何同时评估图像/视频和文本的匹配度
3. 思考数据评估如何与数据选择 (02) 和数据生成 (03) 形成闭环

---

[← 数据生成](../03-data-generation/) | [返回主页](../README.md) | [下一节: 数据处理 →](../05-data-processing/)
