import os
import json
from datasets import load_dataset

# 设置 Hugging Face 镜像
os.environ['HF_ENDPOINT'] = 'https://hf-mirror.com'
cache_dir = "/mnt/data1/xiaochen/llm/datasets"  # 修改为你的缓存目录

# 加载 GSM8K 数据集
dataset = load_dataset("openai/gsm8k", "main", 
                    #    cache_dir=cache_dir
                       )

# 定义解析函数
def format_data(example):
    return {
        "input": example["question"],  # 输入
        "output": example["answer"]    # 输出
    }

# 解析数据
parsed_train = [format_data(sample) for sample in dataset["train"]]
parsed_test = [format_data(sample) for sample in dataset["test"]]

# 保存为 JSON 文件
with open("gsm8k_train.json", "w", encoding="utf-8") as f:
    json.dump(parsed_train, f, ensure_ascii=False, indent=4)

with open("gsm8k_test.json", "w", encoding="utf-8") as f:
    json.dump(parsed_test, f, ensure_ascii=False, indent=4)

print("训练集和测试集已成功保存为 JSON 文件！")
