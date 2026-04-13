import torch
from transformers import AutoModelForCausalLM, AutoTokenizer

# 定义你的三个模型路径
models = {
    "Qwen2.5-1.5B-Instruct-sft": "/mnt/data1/xiaochen/llm/models/qwen-gsm8k-sft/Qwen2.5-1.5B-Instruct",
    "Qwen2.5-7B-Instruct-sft": "/mnt/data1/xiaochen/llm/models/qwen-gsm8k-sft/Qwen2.5-7B-Instruct",
    "Qwen2.5-7B-Instruct-sft-800" : "/mnt/data1/xiaochen/llm/models/qwen-gsm8k-sft/Qwen2.5-7B-Instruct-epoch800",
    "Qwen2.5-1.5B-Instruct": "/mnt/data1/xiaochen/llm/models/Qwen2.5-1.5B-Instruct",
    "Qwen2.5-7B-Instruct": "/mnt/data1/xiaochen/llm/models/Qwen2.5-7B-Instruct"
}

# 设置推理参数
device = "cuda" if torch.cuda.is_available() else "cpu"
max_length = 1024  # 可调整最大生成长度

def generate_response(model_path, input_text):
    """加载模型并生成推理结果"""
    tokenizer = AutoTokenizer.from_pretrained(model_path, trust_remote_code=True)
    model = AutoModelForCausalLM.from_pretrained(model_path, trust_remote_code=True).to(device)

    # 编码输入
    inputs = tokenizer(input_text, return_tensors="pt").to(device)

    # 生成输出
    with torch.no_grad():
        output = model.generate(**inputs, max_length=max_length)

    # 解码输出
    response = tokenizer.decode(output[0], skip_special_tokens=True)
    return response

def main():
    # 用户输入文本
    input_text = input("请输入测试文本: ")

    # 存储各个模型的输出
    results = {}

    for model_name, model_path in models.items():
        print(f"正在使用 {model_name} 进行推理...")
        output_text = generate_response(model_path, input_text)
        results[model_name] = output_text

    # 输出最终结果
    print("\n===== Case Study 结果 =====")
    for model_name, response in results.items():
        print(f"{model_name}: {response}\n")

if __name__ == "__main__":
    main()
