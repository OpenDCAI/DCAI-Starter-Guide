# 04 - 数据评估

## 方向概述

**数据评估**是 Data-Centric AI 中的关键环节，目标是量化数据的质量、多样性和对模型训练的价值。高质量的数据评估指标可以指导数据选择、过滤和生成环节，形成数据质量的闭环优化。

## 推荐论文

> 注：⚡ 为基础必读，💎 为基础选读，💡 为进阶阅读

### 数据评估综合

---

## Awesome Data Evaluation

### Pure Text Evaluation

**Taxonomy**: Text Structure / Diversity & Complexity / Fluency & Understandability / Safety / Educational Value / Content Accuracy & Effectiveness

| Title | Venue | Date | Code | Taxonomy |
| :--- | :---: | :---: | :---: | --- |
| [AlpaGasus: Training A Better Alpaca with Fewer Data](https://arxiv.org/abs/2307.08701) | Arxiv | 2023.07 | - | Content Accuracy & Effectiveness |
| [A Preliminary Study of the Intrinsic Relationship between Complexity and Alignment](https://arxiv.org/abs/2308.05696) | Arxiv | 2023.08 | - | Diversity & Complexity |
| [Beyond Scale: The Diversity Coefficient as a Data Quality Metric](https://arxiv.org/abs/2306.13840) | ICLR Workshop | 2023.06 | [Github](https://github.com/alycialee/beyond-scale-language-data-diversity) | Content Accuracy & Effectiveness |
| [The FineWeb Datasets: Decanting the Web for the Finest Text Data at Scale](https://arxiv.org/abs/2406.17557) | Arxiv | 2024.06 | [HuggingFace](https://huggingface.co/HuggingFaceFW/fineweb-edu-classifier) | Educational Value |
| [InsTag: Instruction Tagging for Analyzing Supervised Fine-tuning of LLMs](https://openreview.net/pdf?id=pszewhybU9) | ICLR | 2023 | [Github](https://github.com/OFA-Sys/InsTag) | Diversity & Complexity |
| [KenLM: Faster and Smaller Language Model Queries](https://aclanthology.org/W11-2123.pdf) | ACL | 2011 | [Github](https://github.com/kpu/kenlm) | Fluency & Understandability |
| [QuRating: Selecting High-Quality Data for Training Language Models](https://arxiv.org/abs/2402.09739) | ICML | 2024 | [Github](https://github.com/princeton-nlp/QuRating) | Fluency & Understandability |
| [Superfiltering: Weak-to-Strong Data Filtering for Fast Instruction-Tuning](https://arxiv.org/abs/2402.00530) | Arxiv | 2024.02 | [Github](https://github.com/tianyi-lab/Superfiltering) | Fluency & Understandability |
| [Textbooks Are All You Need](https://arxiv.org/abs/2306.11644) | Arxiv | 2023.06 | [Github](https://github.com/kyegomez/phi-1) | Educational Value |
| [Towards a Unified Multi-Dimensional Evaluator for Text Generation](https://arxiv.org/abs/2210.07197) | Arxiv | 2022.10 | [Github](https://github.com/maszhongming/UniEval) | Fluency & Understandability |
| [What Makes Good Data for Alignment? A Comprehensive Study of Automatic Data Selection](https://arxiv.org/abs/2312.15685) | Arxiv | 2023.12 | [Github](https://github.com/hkust-nlp/deita) | Content Accuracy & Effectiveness |
| [MTLD, vocd-D, and HD-D: Sophisticated Approaches to Lexical Diversity Assessment](https://link.springer.com/article/10.3758/BRM.42.2.381) | Springer | 2010 | [Github](https://github.com/jennafrens/lexical_diversity) | Diversity & Complexity |

### Image Data Quality Evaluation

#### Synthetic Image Evaluation

| Title | Venue | Date | Code | Taxonomy |
| :--- | :---: | :---: | :---: | --- |
| [FID Score (GANs Trained by a Two Time-Scale Update Rule)](https://arxiv.org/abs/1706.08500) | NeurIPS | 2017 | [Github](https://github.com/mseitzer/pytorch-fid) | Metric Based |
| [KID Score (Demystifying MMD GANs)](https://arxiv.org/abs/1801.01401) | Arxiv | 2018.01 | [Github](https://github.com/abdulfatir/gan-metrics-pytorch) | Metric Based |
| [IS Score (Improved Techniques for Training GANs)](https://arxiv.org/abs/1606.03498) | NeurIPS | 2016 | [Github](https://github.com/mseitzer/pytorch-fid) | Metric Based |
| [AIGIQA-20K: A Large Database for AI-Generated Image Quality Assessment](https://openaccess.thecvf.com/content/CVPR2024W/NTIRE/papers/Li_AIGIQA-20K_A_Large_Database_for_AI-Generated_Image_Quality_Assessment_CVPRW_2024_paper.pdf) | CVPR Workshop | 2024 | [ModelScope](https://www.modelscope.cn/datasets/lcysyzxdxc/AIGCQA-30K-Image) | Benchmarks |

#### Pure Image Evaluation

**Taxonomy**: Statistical Metric Based (Statistics) / Neural Network Based (NN) / Pre-trained Model Based (Pre-train)

| Title | Venue | Date | Code | Taxonomy |
| :--- | :---: | :---: | :---: | --- |
| [BRISQUE: No-Reference Image Quality Assessment in the Spatial Domain](https://ieeexplore.ieee.org/abstract/document/6272356) | TIP | 2012 | [Github](https://github.com/krshrimali/No-Reference-Image-Quality-Assessment-using-BRISQUE-Model) | Statistics |
| [NIMA: Neural Image Assessment](https://ieeexplore.ieee.org/abstract/document/8352823) | TIP | 2018 | [Github](https://github.com/yunxiaoshi/Neural-IMage-Assessment) | NN |
| [MUSIQ: Multi-scale Image Quality Transformer](http://openaccess.thecvf.com/content/ICCV2021/papers/Ke_MUSIQ_Multi-Scale_Image_Quality_Transformer_ICCV_2021_paper.pdf) | ICCV | 2021 | [Github](https://github.com/anse3832/MUSIQ) | NN |
| [TOPIQ: A Top-down Approach from Semantics to Distortions for IQA](https://ieeexplore.ieee.org/abstract/document/10478301) | TIP | 2024 | [Github](https://github.com/chaofengc/iqa-pytorch) | NN |
| [Local Distortion Aware Efficient Transformer Adaptation for IQA](https://arxiv.org/abs/2308.12001) | Arxiv | 2023.08 | - | NN |
| [Quality-Aware Pre-Trained Models for Blind Image Quality Assessment](https://openaccess.thecvf.com/content/CVPR2023/papers/Zhao_Quality-Aware_Pre-Trained_Models_for_Blind_Image_Quality_Assessment_CVPR_2023_paper.pdf) | CVPR | 2023 | - | Pre-train |
| [CLIP-IQA: Exploring CLIP for Assessing the Look and Feel of Images](https://ojs.aaai.org/index.php/AAAI/article/view/25353/25125) | AAAI | 2023 | [Github](https://github.com/IceClear/CLIP-IQA) | Pre-train |
| [QualiCLIP: Quality-Aware Image-Text Alignment for Real-World IQA](https://arxiv.org/abs/2403.11176) | Arxiv | 2024.03 | [Github](https://github.com/miccunifi/QualiCLIP) | Pre-train |
| [Human Preference Score: Better Aligning Text-to-Image Models](https://openaccess.thecvf.com/content/ICCV2023/papers/Wu_Human_Preference_Score_Better_Aligning_Text-to-Image_Models_with_Human_Preference_ICCV_2023_paper.pdf) | ICCV | 2023 | [Github](https://github.com/tgxs002/align_sd) | Pre-train |
| [LIQE: Blind IQA via Vision-Language Correspondence](https://openaccess.thecvf.com/content/CVPR2023/papers/Zhang_Blind_Image_Quality_Assessment_via_Vision-Language_Correspondence_A_Multitask_Learning_CVPR_2023_paper.pdf) | CVPR | 2023 | [Github](https://github.com/zwx8981/LIQE) | Pre-train |

#### Image-Caption Evaluation

**Taxonomy**: CLIP Based / Large Language Model Based (LLM) / Vision LLM Based (VLLM)

| Title | Venue | Date | Code | Taxonomy |
| :--- | :---: | :---: | :---: | --- |
| [CLIPScore: A Reference-free Evaluation Metric for Image Captioning](https://arxiv.org/abs/2104.08718) | Arxiv | 2021.04 | [Github](https://github.com/jmhessel/clipscore) | CLIP |
| [FLEUR: An Explainable Reference-Free Evaluation Metric for Image Captioning](https://arxiv.org/abs/2406.06004) | ACL | 2024 | [Github](https://github.com/Yebin46/FLEUR) | VLLM |
| [Evaluating Text-to-Visual Generation with Image-to-Text Generation](https://arxiv.org/abs/2404.01291) | Arxiv | 2024.04 | [Github](https://github.com/linzhiqiu/t2v_metrics) | VLLM |
| [InfoMetIC: An Informative Metric for Reference-free Image Caption Evaluation](https://arxiv.org/pdf/2305.06002) | Arxiv | 2023.05 | [Github](https://github.com/HAWLYQ/InfoMetIC) | CLIP |
| [HICEScore: A Hierarchical Metric for Image Captioning Evaluation](https://arxiv.org/abs/2407.18589) | Arxiv | 2024.07 | [Github](https://github.com/joeyz0z/HICE) | CLIP |
| [LLMScore: Unveiling the Power of LLMs in Text-to-Image Synthesis Evaluation](https://arxiv.org/abs/2305.11116) | NeurIPS | 2024 | [Github](https://github.com/YujieLu10/LLMScore) | LLM |
| [Divide, Evaluate, and Refine: Evaluating and Improving Text-to-Image Alignment](https://arxiv.org/abs/2307.05973) | NeurIPS | 2023 | [Github](https://github.com/1jsingh/Divide-Evaluate-and-Refine) | VLLM, CLIP |

### Video Data Quality Evaluation

#### Pure Video Evaluation

**Taxonomy**: Statistical Metric Based (Statistics) / Neural Network Based (NN)

| Title | Venue | Date | Code | Taxonomy |
| :--- | :---: | :---: | :---: | --- |
| [Perceptual Video Quality Assessment: A Survey](https://arxiv.org/abs/2402.03413) | Arxiv | 2024.02 | - | Survey |
| [Two-Level Approach for No-Reference Consumer Video Quality Assessment](https://ieeexplore.ieee.org/abstract/document/8742797) | TIP | 2019 | [Github](https://github.com/jarikorhonen/nr-vqa-consumervideo) | Statistics |
| [UGC-VQA: Benchmarking Blind Video Quality Assessment for UGC](https://ieeexplore.ieee.org/abstract/document/9405420) | TIP | 2021 | [Github](https://github.com/vztu/VIDEVAL) | Statistics |
| [FAST-VQA: Efficient End-to-end Video Quality Assessment with Fragment Sampling](https://link.springer.com/chapter/10.1007/978-3-031-20068-7_31) | ECCV | 2022 | [Github](https://github.com/VQAssessment/FAST-VQA-and-FasterVQA) | NN |
| [FasterVQA: Neighbourhood Representative Sampling for Efficient End-to-End VQA](https://ieeexplore.ieee.org/abstract/document/10264158) | TPAMI | 2023 | [Github](https://github.com/VQAssessment/FAST-VQA-and-FasterVQA) | NN |
| [DOVER: Exploring Video Quality Assessment on UGC from Aesthetic and Technical Perspectives](https://openaccess.thecvf.com/content/ICCV2023/papers/Wu_Exploring_Video_Quality_Assessment_on_User_Generated_Contents_from_Aesthetic_ICCV_2023_paper.pdf) | ICCV | 2023 | [Github](https://github.com/VQAssessment/DOVER) | NN |

#### Video-Caption Evaluation

| Title | Venue | Date | Code | Taxonomy |
| :--- | :---: | :---: | :---: | --- |
| [EMScore: Evaluating Video Captioning via Coarse-Grained and Fine-Grained Embedding Matching](http://openaccess.thecvf.com/content/CVPR2022/papers/Shi_EMScore_Evaluating_Video_Captioning_via_Coarse-Grained_and_Fine-Grained_Embedding_Matching_CVPR_2022_paper.pdf) | CVPR | 2022 | [Github](https://github.com/shiyaya/emscore) | CLIP |
| [PAC-S: Positive-Augmented Contrastive Learning for Image and Video Captioning Evaluation](https://openaccess.thecvf.com/content/CVPR2023/papers/Sarto_Positive-Augmented_Contrastive_Learning_for_Image_and_Video_Captioning_Evaluation_CVPR_2023_paper.pdf) | CVPR | 2023 | [Github](https://github.com/aimagelab/pacscore) | CLIP |

### Data Diversity Evaluation

| Title | Venue | Date | Code |
| :--- | :---: | :---: | :---: |
| [The Vendi Score: A Diversity Evaluation Metric for Machine Learning](https://par.nsf.gov/servlets/purl/10427561) | TMLR | 2023 | [Github](https://github.com/vertaix/Vendi-Score) |
| [Quality-Weighted Vendi Scores and Their Application to Diverse Experimental Design](https://arxiv.org/pdf/2405.02449) | ICML | 2024 | [Github](https://github.com/vertaix/Quality-Weighted-Vendi-Score) |
| [Beyond Scale: The Diversity Coefficient as a Data Quality Metric](https://arxiv.org/pdf/2306.13840) | Arxiv | 2023.06 | [Github](https://github.com/alycialee/beyond-scale-language-data-diversity) |

---

## 学习建议

1. 从 CLIPScore 入手理解无参考评估 (Reference-free) 的基本思路
2. 关注多模态评估指标的发展——如何同时评估图像/视频和文本的匹配度
3. 思考数据评估如何与数据选择 (02) 和数据生成 (03) 形成闭环
4. 论文列表按 Text → Image → Video → Diversity 四大类组织，可按需深入

---

[← 数据生成](../03-data-generation/) | [返回主页](../README.md) | [下一节: 数据处理 →](../05-data-processing/)
