<p align="center">
    <h1 align="center">OpenDCAI Tutorial</h1>
    <p align="center">Data-Centric AI 学习指南</p>
</p>

## 项目简介

**OpenDCAI Tutorial** 是面向 Data-Centric AI (DCAI) 方向的系统性学习指南，由 PKU-DCAI 实验室维护。本项目整合了 DCAI 各核心研究方向的课程、论文和实战教程，帮助初学者从基础概念到动手实践，快速建立对 Data-Centric AI 的全面认识。

**Data-Centric ML** 是研究使用数据生成、选择与配比等方法实现大规模、高效以及提升模型表现的研究方向。与以模型为中心 (Model-Centric) 的思路不同，DCAI 强调通过改进数据质量、数据组织和数据流程来系统性地提升 AI 系统的效果。

## 学习路线图

建议按照以下顺序学习，根据个人背景可跳过已掌握的模块：

```
前置知识 ──> DCAI 基础 ──> 核心方法论 ──> 领域应用 ──> 工具与进阶
  (00)         (01)       (02-06)       (07-08)      (09-10)
```

| 编号 | 模块 | 说明 |
|:---:|------|------|
| 00 | [前置知识](./00-prerequisites/) | ML/DL、LLM、RL/RLHF 基础课程与资料 |
| 01 | [DCAI 基础](./01-dcai-foundations/) | MIT DCAI 2024、华盛顿大学 DCAI 课程、领域综述 |
| 02 | [数据选择与配比](./02-data-selection-and-mixing/) | Data Selection、Data Mixing 方法与论文 |
| 03 | [数据生成](./03-data-generation/) | LLM 驱动的合成数据生成、可控数据生成 |
| 04 | [数据评估](./04-data-evaluation/) | Image/Video 数据评估、CLIPScore 等 |
| 05 | [数据处理](./05-data-processing/) | Data Cleaning、Data Filtering、Scaling Laws |
| 06 | [多模态数据侧](./06-multimodal-data-centric/) | Image/Video LLMs、Data-Centric VLMs |
| 07 | [强推理模型与数据](./07-reasoning-data/) | AI4Math、Code、Science 推理数据 |
| 08 | [**实战：LLM 数学微调**](./08-llm-math-guide/) | 基于 LLaMA-Factory + GSM8K 的完整微调 Pipeline |
| 09 | [DCAI 工具与系统](./09-dcai-tools/) | DataFlow 数据准备 + DataFlex 数据训练 |
| 10 | [RAG、数据抽取与智能助手](./10-rag-and-extraction/) | GraphRAG、Raptor、DataMind Agentic RAG |

## 快速开始

- **零基础入门**：从 `00-prerequisites` 开始，了解 ML/DL 和 LLM 基本概念
- **有 ML 基础**：直接从 `01-dcai-foundations` 开始，学习 DCAI 核心概念
- **想动手实践**：跳到 `08-llm-math-guide`，跟着教程用 LLaMA-Factory 微调一个数学 LLM
- **选择细分方向**：浏览 `02`-`06` 了解各研究子方向，找到感兴趣的方向深入

## 参考资料

- [PKU-DAIR Starter Guide](https://github.com/PKU-DAIR/Starter-Guide) -- 实验室入门指南
- [PKU-DAIR Starter Guide - DCML 方向](https://github.com/PKU-DAIR/Starter-Guide/tree/main/docs/dcml) -- Data-Centric ML 论文与课程列表
- [MIT DCAI 2024](https://dcai.csail.mit.edu/) -- MIT Data-Centric AI 课程
- [UW DCAI](https://koh.pw/cse599j/) -- 华盛顿大学 Data-Centric AI 课程

## 贡献指南

欢迎通过 PR 贡献新的教程、补充论文列表或完善现有内容。每个模块文件夹下的 `README.md` 包含该方向的核心资源，可直接在其中添加内容。

---

Copyright &copy; 2025 by PKU-DCAI. All rights reserved.
