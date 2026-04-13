import os
import datasets
from datasets import load_dataset
os.environ['HF_ENDPOINT'] = 'https://hf-mirror.com'
cache_dir = "/mnt/data1/xiaochen/llm/datasets" # change to your own cache directory

dataset = load_dataset("openai/gsm8k", "main", cache_dir=cache_dir)
print("train_sample_len", len(dataset['train']))
print("test_sample_len", len(dataset['test']))
print("sample[0]:\n", dataset['train'][0])