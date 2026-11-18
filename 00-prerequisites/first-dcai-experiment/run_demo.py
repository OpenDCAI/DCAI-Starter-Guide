"""离线、仅用标准库的教学实验。运行方式见同目录 README。"""

import argparse
from collections import Counter
import json
import math
from pathlib import Path
import re


LABELS = ("negative", "positive")


def tokens(text):
    """本实验只使用英文短句，按单词切分并忽略大小写与标点。"""
    return re.findall(r"[a-z]+", text.lower())


def validate_data(data):
    seen_ids = set()
    seen_text = {}
    for split in ("train", "validation", "test"):
        if not data[split]:
            raise ValueError(f"{split} 不能为空")
        for row in data[split]:
            if row["id"] in seen_ids:
                raise ValueError(f"样本 ID 重复：{row['id']}")
            seen_ids.add(row["id"])
            if row["label"] not in LABELS:
                raise ValueError(f"未知标签：{row['label']}")
            key = tuple(tokens(row["text"]))
            if not key:
                raise ValueError("文本需要包含英文单词")
            if key in seen_text and seen_text[key] != split:
                raise ValueError("发现跨划分的重复文本，请先检查数据泄漏")
            seen_text[key] = split
    train_ids = {row["id"] for row in data["train"]}
    if not set(data["label_corrections"]) <= train_ids:
        raise ValueError("纠错记录只能引用训练集 ID")
    if not set(data["label_corrections"].values()) <= set(LABELS):
        raise ValueError("纠错记录含有未知标签")


def correct_labels(train, corrections):
    return [dict(row, label=corrections.get(row["id"], row["label"]))
            for row in train]


def deduplicate(train):
    unique = {}
    for row in train:
        key = tuple(tokens(row["text"]))
        if key in unique and unique[key]["label"] != row["label"]:
            raise ValueError("重复文本标签冲突，应先核查标签，再去重")
        unique.setdefault(key, row)
    return list(unique.values())


class NaiveBayes:
    """词袋朴素贝叶斯：统计每类词频，使用固定的加一平滑。"""

    def fit(self, train):
        self.documents = Counter(row["label"] for row in train)
        if set(self.documents) != set(LABELS):
            raise ValueError("训练集需要包含两个类别")
        self.words = {label: Counter() for label in LABELS}
        for row in train:
            self.words[row["label"]].update(tokens(row["text"]))
        self.vocabulary = set().union(*(set(c) for c in self.words.values()))
        self.totals = {label: sum(c.values()) for label, c in self.words.items()}
        return self

    def predict(self, text):
        scores = {}
        for label in LABELS:
            score = math.log(self.documents[label] / sum(self.documents.values()))
            denominator = self.totals[label] + len(self.vocabulary)
            for word in tokens(text):
                if word in self.vocabulary:
                    score += math.log((self.words[label][word] + 1) / denominator)
            scores[label] = score
        return max(LABELS, key=lambda label: scores[label])


def evaluate(model, rows):
    predictions = [dict(row, prediction=model.predict(row["text"])) for row in rows]
    correct = sum(row["prediction"] == row["label"] for row in predictions)
    return {"correct": correct, "total": len(rows),
            "accuracy": correct / len(rows), "predictions": predictions}


def run_experiment(data):
    validate_data(data)
    corrected = correct_labels(data["train"], data["label_corrections"])
    variants = [("raw", data["train"]), ("corrected", corrected),
                ("corrected_deduplicated", deduplicate(corrected))]
    results = []
    for name, train in variants:
        # fit 只接收当前训练集。验证集、测试集及其标签不参与训练。
        model = NaiveBayes().fit(train)
        results.append({"name": name, "train_size": len(train),
                        "validation": evaluate(model, data["validation"]),
                        "test": evaluate(model, data["test"])})
    return results


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--data", type=Path, default=Path(__file__).with_name("data.json"))
    parser.add_argument("--output", type=Path, help="可选：将结果保存为 JSON")
    args = parser.parse_args()
    with args.data.open(encoding="utf-8") as handle:
        results = run_experiment(json.load(handle))
    print("variant                     train  validation      test")
    for result in results:
        val, test = result["validation"], result["test"]
        print(f"{result['name']:<28} {result['train_size']:>3}"
              f"    {val['correct']}/{val['total']} ({val['accuracy']:.1%})"
              f"    {test['correct']}/{test['total']} ({test['accuracy']:.1%})")
    print("\n测试集逐条预测（negative=负面，positive=正面）：")
    for index, row in enumerate(results[0]["test"]["predictions"]):
        predictions = [r["test"]["predictions"][index]["prediction"] for r in results]
        print(f"{row['id']} | {row['text']} | label={row['label']} | " + " -> ".join(predictions))
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(json.dumps(results, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
        print(f"\n结果已保存到 {args.output}")


if __name__ == "__main__":
    main()
