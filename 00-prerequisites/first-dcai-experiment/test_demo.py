"""检查实验的数据边界；不要求清洗后的分数一定上涨。"""

import copy
import json
from pathlib import Path
import unittest

from run_demo import correct_labels, deduplicate, run_experiment, validate_data


class DataBoundaryTests(unittest.TestCase):
    def setUp(self):
        self.data = json.loads(Path(__file__).with_name("data.json").read_text(encoding="utf-8"))

    def test_rejects_cross_split_duplicates(self):
        self.data["test"][0]["text"] = self.data["train"][0]["text"].upper() + "!"
        with self.assertRaisesRegex(ValueError, "数据泄漏"):
            validate_data(self.data)

    def test_rejects_test_label_corrections(self):
        self.data["label_corrections"][self.data["test"][0]["id"]] = "positive"
        with self.assertRaisesRegex(ValueError, "只能引用训练集"):
            validate_data(self.data)

    def test_conflicting_labels_require_review(self):
        with self.assertRaisesRegex(ValueError, "标签冲突"):
            deduplicate(self.data["train"])
        corrected = correct_labels(self.data["train"], self.data["label_corrections"])
        self.assertLess(len(deduplicate(corrected)), len(corrected))

    def test_test_labels_do_not_change_predictions(self):
        original = copy.deepcopy(self.data)
        before = run_experiment(self.data)
        self.assertEqual(self.data, original)
        for row in self.data["test"]:
            row["label"] = "negative" if row["label"] == "positive" else "positive"
        after = run_experiment(self.data)
        for old, new in zip(before, after):
            self.assertEqual([r["prediction"] for r in old["test"]["predictions"]],
                             [r["prediction"] for r in new["test"]["predictions"]])


if __name__ == "__main__":
    unittest.main()
