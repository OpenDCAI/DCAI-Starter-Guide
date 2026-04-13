# 09 - DCAI 工具与系统

## 方向概述

OpenDCAI 提供了两个核心开源工具，覆盖从数据准备到模型训练的完整 Data-Centric AI 流程：

```
原始数据 (PDF/文本/QA) ──> DataFlow (数据准备) ──> 高质量训练数据 (JSON) ──> DataFlex (数据训练) ──> 模型
```

- **[DataFlow](https://github.com/OpenDCAI/DataFlow)** -- 数据准备系统：将原始数据转化为高质量的 LLM 训练数据
- **[DataFlex](https://github.com/OpenDCAI/DataFlex)** -- 数据训练系统：在训练过程中动态调度数据，提升模型性能

两个项目相互独立，通过标准数据格式 (JSON/JSONL) 衔接。DataFlex 可接收任意来源的训练数据。

---

## DataFlow -- 数据准备系统

> Generate, Clean, and Prepare LLM Data, All-in-One

- GitHub: https://github.com/OpenDCAI/DataFlow
- 文档: https://opendcai.github.io/DataFlow-Doc/
- 视频教程: https://space.bilibili.com/3546929239689711
- 飞书教程: https://wcny4qa9krto.feishu.cn/wiki/I9tbw2qnBi0lEakmmAGclTysnFd
- 论文: [DataFlow: An LLM-Driven Framework for Unified Data Preparation](https://arxiv.org/abs/2512.16676)

### 核心特性

1. **开箱即用的数据合成与清洗 Pipeline**
   - Text Pipeline: 从大规模纯文本中挖掘 QA 对，用于 SFT/RL 训练
   - Reasoning Pipeline: 为现有 QA 数据增加 CoT 推理链、分类、难度评估
   - Text2SQL Pipeline: 自然语言 → SQL 查询 (ICDE 2026)
   - Code Pipeline: 代码指令数据合成与过滤
   - Math Pipeline: 数学数据工作流 (KDD 2026)
   - Knowledge Base Cleaning Pipeline: 从 PDF/表格/Word 中提取结构化知识
   - Agentic RAG Pipeline: 提取需要外部知识的 QA 对

2. **灵活的 Operator 编排**
   - 10+ 核心 Operator，100+ 可复用的 Pipeline-specific Operator
   - PyTorch 风格的 `Pipeline → Operator → Prompt` 分层设计
   - 支持自定义 Operator，即插即用

3. **DataFlow Suite 全家桶**
   - DataFlow-WebUI: 可视化拖拽构建 Pipeline (`dataflow webui` 一键启动)
   - [DataFlow-Agent](https://github.com/OpenDCAI/DataFlow-Agent): AI 智能体自动组装 Operator 与 Pipeline
   - DataFlow-Ecosystem: 领域扩展模块 (如 [DataFlow-MM](https://github.com/OpenDCAI/DataFlow-MM) 多模态)
   - [RayOrch](https://github.com/OpenDCAI/RayOrch): 基于 Ray 的分布式调度层

### 快速上手

```bash
# 安装 (推荐 uv 加速)
pip install uv
uv pip install open-dataflow

# 如需本地 GPU 推理
uv pip install open-dataflow[vllm]

# 验证安装
dataflow -v

# 启动 WebUI
dataflow webui
```

Operator 使用示例：

```python
from dataflow.operators.core_text import PromptedGenerator
from dataflow.utils.storage import FileStorage
from dataflow.serving import APILLMServing_request

storage = FileStorage(first_entry_file_name="./input.json")

llm_serving = APILLMServing_request(
    api_url="https://api.openai.com/v1/chat/completions",
)

prompted_generator = PromptedGenerator(
    llm_serving=llm_serving,
    system_prompt="Please solve this math problem."
)

prompted_generator.run(
    storage=storage.step(),
    input_key="problem",
    output_key="solution"
)
```

---

## DataFlex -- 数据训练系统

> Data Select · Mix · Reweight — Right in the LLM Training Loop

- GitHub: https://github.com/OpenDCAI/DataFlex
- 文档: https://opendcai.github.io/DataFlex-Doc/
- 论文: [DataFlex: A Unified Framework for Data-Centric Dynamic Training of LLMs](https://arxiv.org/abs/2603.26164) (Hugging Face Daily Papers #1)

### 核心特性

DataFlex 基于 [LLaMA-Factory](https://github.com/hiyouga/LLaMA-Factory) 构建，在训练过程中动态调度数据，统一实现了三类数据调度算法：

**1. Data Selection** -- 动态选择训练样本（如聚焦"困难"样本）

| 方法 | 类别 | 需要模型参与 |
|------|------|:---:|
| LESS | Gradient-Based | Yes |
| NICE | Gradient-Based | Yes |
| Loss / Delta Loss | Loss-Based | Yes |
| NEAR / TSDS | Data Distribution-Based | No |

**2. Data Mixture** -- 动态调整不同领域数据的配比

| 方法 | 类别 | 需要模型参与 |
|------|------|:---:|
| DoReMi | Offline Mixture | Yes |
| ODM | Online Mixture | Yes |

**3. Data Reweighting** -- 动态调整样本权重

| 方法 | 类别 | 需要模型参与 |
|------|------|:---:|
| Loss Reweighting | Loss-Based | Yes |

### 快速上手

```bash
# 安装
git clone https://github.com/OpenDCAI/DataFlex.git
cd DataFlex
pip install -e .

# 安装 LLaMA-Factory
pip install llamafactory==0.9.3  # Python 3.10
# pip install llamafactory==0.9.4  # Python 3.11+

# 训练 (以 LESS 算法为例)
dataflex-cli train examples/train_lora/selectors/less.yaml
```

与 LLaMA-Factory 完全兼容，YAML 配置中只需额外加入 DataFlex 参数。详见 [DataFlex-Doc](https://opendcai.github.io/DataFlex-Doc/)。

---

## 学习建议

1. **先跑通 DataFlow**：用 `pip install open-dataflow` 安装后，跟着 [Google Colab 教程](https://colab.research.google.com/drive/1haosl2QS4N4HM7u7HvSsz_MnLabxexXl) 体验 Pipeline
2. **再上手 DataFlex**：如果你已经跟着 [08-llm-math-guide](../08-llm-math-guide/) 熟悉了 LLaMA-Factory，DataFlex 的使用会非常顺畅
3. **理解两者定位**：DataFlow 解决"用什么数据训练"，DataFlex 解决"训练时怎么用数据"
4. **参考论文**：两篇技术报告详细介绍了设计理念和实验结果

## 相关论文

- [DataFlow Technical Report](https://arxiv.org/abs/2512.16676) (arXiv 2025)
- [DataFlex Technical Report](https://arxiv.org/abs/2603.26164) (arXiv 2026, HF Daily Papers #1)
- [Towards Next-Generation LLM Training: From the Data-Centric Perspective](https://arxiv.org/abs/2603.14712) (arXiv 2026)

---

[← 实战 LLM 数学微调](../08-llm-math-guide/) | [返回主页](../README.md) | [下一节: RAG 与数据抽取 →](../10-rag-and-extraction/)
