# 10 - RAG、数据抽取与智能助手

## 方向概述

**检索增强生成 (Retrieval-Augmented Generation, RAG)** 通过从外部知识库中检索相关信息来增强大模型的生成能力，是连接数据与模型的重要桥梁。在 DCAI 视角下，RAG 的核心问题是：如何高效地组织、索引和检索数据，让 LLM 在推理 (Inference) 阶段也能受益于高质量的数据工程。

核心研究主题：
- **知识索引** -- 如何高效组织和存储知识
- **多模态检索** -- 跨模态的信息检索
- **RAG 架构** -- GraphRAG、层次化检索、Agentic RAG 等
- **数据即插即用** -- 将数据准备与 LLM 推理无缝衔接

## 推荐论文

> 注：⚡ 为基础必读，💎 为基础选读，💡 为进阶阅读

### 综述

- ⚡ [Retrieval-Augmented Generation for AI-Generated Content: A Survey](https://arxiv.org/abs/2402.19473) -- RAG 领域全面综述（组里的 Survey）

### 代表性工作

- ⚡ [GraphRAG](https://github.com/microsoft/graphrag) -- 基于图结构的检索增强生成
- ⚡ [RAPTOR: Recursive Abstractive Processing for Tree-Organized Retrieval](https://arxiv.org/abs/2401.18059v1) -- 递归抽象处理的层次化检索
- 💎 [QAEncoder: Towards Aligned Representation Learning in Question Answering System](https://arxiv.org/abs/2409.20434) -- 面向 QA 的对齐表示学习

---

## DataMind -- 即插即用的 Agentic RAG 系统

> All-in-one intelligent assistant — RAG, GraphRAG, NL2SQL, Skills & Memory

- GitHub: https://github.com/haolpku/DataMind
- 文档: https://haolpku.github.io/DataMind-Doc/

### 简介

[DataMind](https://github.com/haolpku/DataMind) 是基于 LlamaIndex 的一体化智能助手，集成五大模块，Agent 根据用户问题**自动选择**使用哪个工具，无需手动指定。它让数据与 LLM 推理之间实现即插即用——只需将数据放入对应目录，DataMind 自动构建索引并提供智能检索服务。

与 [DataFlow](https://github.com/OpenDCAI/DataFlow)（数据准备）和 [DataFlex](https://github.com/OpenDCAI/DataFlex)（数据训练）配合，DataMind 补齐了 **LLM 推理侧**的数据利用环节：

```
DataFlow (数据准备) ──> DataFlex (数据训练) ──> DataMind (数据推理)
     原始数据清洗           训练时数据调度          推理时知识检索
```

### 五大模块

| 模块 | 功能 | 技术 |
|------|------|------|
| **RAG** | 文档向量化 + 语义检索，支持多模态 (CLIP / VLM) | Chroma |
| **GraphRAG** | 知识图谱实体关系检索，多跳推理 | NetworkX |
| **Database** | 自然语言转 SQL (NL2SQL) | SQLite |
| **Skills** | 自定义工具（Python 函数）+ 知识型（Markdown 检索）| FunctionTool |
| **Memory** | FIFO 短期记忆 + LLM 摘要长期记忆 | LlamaIndex |

### 快速上手

```bash
# 1. 创建环境
conda create -n datamind python=3.12
conda activate datamind

# 2. 安装依赖
git clone https://github.com/haolpku/DataMind.git
cd DataMind
pip install -r requirements.txt

# 3. 配置 API Key
cp .env.example .env
# 编辑 .env，填入你的 API Key 和 API Base

# 4. 将文档放入 data/profiles/default/ 目录

# 5a. Web 界面（推荐）
python server.py
# 浏览器访问 http://localhost:8000

# 5b. 或终端命令行
python main.py
```

### 数据管理

通过 `DATA_PROFILE` 环境变量管理多套知识库，数据和索引完全隔离：

```bash
DATA_PROFILE=default python main.py   # 默认 profile
DATA_PROFILE=mydata python main.py    # 切换 profile
```

数据放入对应目录即可自动索引：

```
data/profiles/{profile}/
├── *.txt / *.md / *.pdf    → RAG 原始文档（自动分块）
├── chunks/*.jsonl          → RAG 预分块（跳过分块）
├── triplets/*.jsonl        → GraphRAG 三元组
├── tables/*.sql            → Database SQL 文件
└── images/                 → 多模态图片
```

---

## 学习建议

1. 先阅读 RAG Survey 了解检索增强生成的全貌
2. GraphRAG 和 RAPTOR 代表了两种不同的知识组织思路，值得对比学习
3. **动手跑 DataMind**：将自己的文档/数据放入 `data/profiles/default/` 目录，体验从数据到智能问答的完整流程
4. 思考 DataFlow → DataFlex → DataMind 三件套如何串联起 DCAI 的"数据准备 → 训练 → 推理"全链路

---

[← DCAI 工具与系统](../09-dcai-tools/) | [返回主页](../README.md)
