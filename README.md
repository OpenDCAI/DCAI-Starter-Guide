<p align="center">
    <h1 align="center">OpenDCAI Tutorial</h1>
    <p align="center">Data-Centric AI 学习指南</p>
</p>

## 项目简介

**OpenDCAI Tutorial** 是面向 Data-Centric AI (DCAI) 方向的系统性学习指南，由 PKU-DCAI 实验室维护。本项目整合了 DCAI 各核心研究方向的课程、论文和实战教程，帮助初学者从基础概念到动手实践，快速建立对 Data-Centric AI 的全面认识。

**Data-Centric ML** 是研究使用数据生成、选择与配比等方法实现大规模、高效以及提升模型表现的研究方向。与以模型为中心 (Model-Centric) 的思路不同，DCAI 强调通过改进数据质量、数据组织和数据流程来系统性地提升 AI 系统的效果。

## 第一次来，从这里开始

如果你会一点 Python，但还不熟悉大模型，先走下面这条路线。你不需要先通读所有论文，也不需要准备显卡。

1. **认识大模型**：读 [00 前置知识](./00-prerequisites/)，以复旦 NLP 团队的[《大规模语言模型：从理论到实践》](https://intro-llm.github.io/)为默认教材，按主题选读；配合[术语与样本说明](./00-prerequisites/llm-basics.md)，分清推理、预训练、微调和 RAG。
2. **做第一个实验**：运行[数据纠错与去重实验](./00-prerequisites/first-dcai-experiment/)。只需 Python 标准库，用固定模型方法和测试集比较不同训练数据，查看哪些预测发生了变化。
3. **理解 DCAI 的问题**：进入 [01](./01-dcai-foundations/)，再按 **05 数据处理 → 04 数据评估 → 03 数据生成 → 02 数据选择与配比** 学习。先完成每章的小练习，再选择论文深入。
4. **选择后续实践**：有合适 GPU、理解训练与评测后做 [08 数学微调](./08-llm-math-guide/)；想组织数据流程看 [09 工具与系统](./09-dcai-tools/)；想用文档辅助问答看 [10 RAG](./10-rag-and-extraction/)。多模态和强推理方向见 06、07，可按兴趣选学。

学习时间因基础而异。第一阶段的完成标准是：能解释一条训练样本、跑出对照结果，并说清哪些操作只使用训练集。复旦教材的具体阅读范围和自测题见 [00](./00-prerequisites/)。

## 模块目录

编号用于定位材料，不要求按编号逐章通读。已有基础的同学可以直接查找研究方向。

| 编号 | 模块 | 说明 |
|:---:|------|------|
| 00 | [前置知识](./00-prerequisites/) | 复旦教材选读、LLM 基本概念、无需 GPU 的首个实验 |
| 01 | [DCAI 基础](./01-dcai-foundations/) | MIT DCAI 2024、华盛顿大学 DCAI 课程、领域综述 |
| 02 | [数据选择与配比](./02-data-selection-and-mixing/) | Data Selection、Data Mixing 方法与论文 |
| 03 | [数据生成](./03-data-generation/) | LLM 驱动的合成数据生成、可控数据生成 |
| 04 | [数据评估](./04-data-evaluation/) | 文本、图像、视频与多样性评估 |
| 05 | [数据处理](./05-data-processing/) | Data Cleaning、Data Filtering、Scaling Laws |
| 06 | [多模态数据侧](./06-multimodal-data-centric/) | Image/Video LLMs、Data-Centric VLMs |
| 07 | [强推理模型与数据](./07-reasoning-data/) | AI4Math、Code、Science 推理数据 |
| 08 | [**实战：LLM 数学微调**](./08-llm-math-guide/) | 基于 LLaMA-Factory + GSM8K 的完整微调 Pipeline |
| 09 | [DCAI 工具与系统](./09-dcai-tools/) | DataFlow 数据准备 + DataFlex 数据训练 |
| 10 | [RAG、数据抽取与智能助手](./10-rag-and-extraction/) | GraphRAG、Raptor、DataMind Agentic RAG |

## 如何使用每章的资料

- **刚入门**：先看每章的“第一次学习”，完成一个小任务；论文列表留作之后查阅。列表中的“必读”指深入该研究方向时的重点材料。
- **已有 ML/LLM 基础**：可以从 01 或感兴趣的方向进入。08 的微调实践需要额外的训练环境，先阅读该章的运行条件。
- **准备做研究**：结合论文的问题、数据、评价指标和实验设置阅读；不要只记录模型分数，也要记录失败案例。

## 参考资料

- [复旦 NLP 大语言模型教材](https://intro-llm.github.io/) -- 本指南的默认 LLM 前置阅读，按 00 中的主题选读
- [PKU-DAIR Starter Guide](https://github.com/PKU-DAIR/Starter-Guide) -- 实验室入门指南
- [PKU-DAIR Starter Guide - DCML 方向](https://github.com/PKU-DAIR/Starter-Guide/tree/main/docs/dcml) -- Data-Centric ML 论文与课程列表
- [MIT DCAI 2024](https://dcai.csail.mit.edu/) -- MIT Data-Centric AI 课程
- [UW DCAI](https://koh.pw/cse599j/) -- 华盛顿大学 Data-Centric AI 课程

## 贡献指南

欢迎通过 PR 贡献新的教程、补充论文列表或完善现有内容。每个模块文件夹下的 `README.md` 包含该方向的核心资源，可直接在其中添加内容。

---

Copyright &copy; 2025 by PKU-DCAI. All rights reserved.
