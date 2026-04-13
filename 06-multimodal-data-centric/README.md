# 06 - 多模态数据侧

## 方向概述

多模态大模型（Image LLMs、Video LLMs）的数据侧研究关注如何为视觉-语言模型准备和优化训练数据。核心方向包括：

- **Data-Centric VLMs** -- 数据的选择、增强 (recaption)，比如重写 caption 提升数据质量
- **Vision-Language Model 视觉特征提取与选择** -- 不同 Vision Encoder 的融合与选择
- **跨模态对齐 (Modality Alignment)** -- 设计高效的跨模态对齐机制

## 推荐论文

> 注：⚡ 为基础必读，💎 为基础选读，💡 为进阶阅读

### 入门必读

- ⚡ [多模态大模型入门文档](https://wcny4qa9krto.feishu.cn/wiki/Lyq9wNeovivXpbkwaNVcebrCnnb)
- ⚡ [A Survey of Large Language and Vision Models](https://arxiv.org/pdf/2306.13549)

### ImageLLMs

- ⚡ [BLIP-2: Bootstrapping Language-Image Pre-training](https://arxiv.org/abs/2301.12597)
- ⚡ [MiniGPT-4: Enhancing Vision-Language Understanding](https://arxiv.org/abs/2304.10592)
- ⚡ [Visual Instruction Tuning (LLaVA)](https://arxiv.org/abs/2304.08485)
- ⚡ [Improved Baselines with Visual Instruction Tuning (LLaVA-1.5)](https://arxiv.org/abs/2310.03744)

### VideoLLMs

- ⚡ [Qwen-VL](https://arxiv.org/abs/2308.12966)
- ⚡ [Video-LLaMA](https://arxiv.org/abs/2306.02858)
- ⚡ [Video-LLaVA](https://arxiv.org/abs/2311.10122)
- ⚡ [MVBench](https://arxiv.org/abs/2311.17005)
- ⚡ [InternVideo2](https://arxiv.org/abs/2403.15377)

### Data-Centric VLMs（数据选择、增强、recaption）

- ⚡ [Improved Baselines with Visual Instruction Tuning](https://arxiv.org/abs/2310.03744)
- ⚡ [Monkey: Image Resolution and Text Label Are Important](https://arxiv.org/abs/2311.06607)
- ⚡ [ShareGPT4V: Improving LMMs with Better Captions](https://arxiv.org/abs/2311.12793)
- 💎 [MiniGPT4-Video](https://arxiv.org/abs/2404.03413)

### 视觉特征提取与跨模态对齐

- ⚡ [BRAVE: Broadening the Visual Encoding of VLMs](https://brave-vlms.epfl.ch/)
- ⚡ [Eyes Wide Shut? Visual Shortcomings of Multimodal LLMs](https://arxiv.org/abs/2401.06209)
- ⚡ [FlexAttention for Efficient High-Resolution VLMs](https://arxiv.org/abs/2407.20228)
- ⚡ [From CLIP to DINO: Visual Encoders in MLLMs](https://arxiv.org/abs/2310.08825)
- 💎 [Awesome Multimodal Large Language Models](https://github.com/BradyFU/Awesome-Multimodal-Large-Language-Models)

## 学习建议

1. 先从入门文档和 Survey 入手，建立对多模态大模型的全局认识
2. ImageLLMs 的论文按时间顺序读，可以看到 VLM 架构的演化
3. Data-Centric VLMs 是将 DCAI 思想应用于多模态的核心方向，重点关注 caption 质量对模型性能的影响

---

[← 数据处理](../05-data-processing/) | [返回主页](../README.md) | [下一节: 强推理模型与数据 →](../07-reasoning-data/)
