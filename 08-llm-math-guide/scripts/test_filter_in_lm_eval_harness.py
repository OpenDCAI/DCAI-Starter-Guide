import re
from lm_eval.api.filter import Filter
from lm_eval.api.task import Task
from lm_eval.api.registry import register_task
from lm_eval.filters.extraction import RegexFilter
from lm_eval.filters.selection import TakeFirstFilter

# 自定义一个简单的测试任务
@register_task("test_regex_behavior")
class TestRegexTask(Task):
    VERSION = 0.1

    def __init__(self):
        # 手动定义输入和模型生成的假设回答
        self._test_docs = [
            {
                "input": "问题：答案是？",
                "target": "42",  # 标准答案
                "model_responses": [
                    "#### 42和43",          # 候选回答 0
                    "答案可能是42或43",       # 候选回答 1
                    "#### 44"               # 候选回答 2
                ]
            }
        ]

    def has_training_docs(self):
        return False

    def has_validation_docs(self):
        return False

    def has_test_docs(self):
        return True

    def test_docs(self):
        return self._test_docs

    def doc_to_text(self, doc):
        return doc["input"]

    def doc_to_target(self, doc):
        return doc["target"]

    def construct_requests(self, doc, ctx):
        # 直接使用预定义的模型回答，跳过实际模型调用
        return None

    def process_results(self, doc, results):
        return {}

    def aggregation(self):
        return {}

    def higher_is_better(self):
        return {}

# 测试函数
def test_regex_behavior():
    task = TestRegexTask()
    filters = [
        RegexFilter(
            regex_pattern=r"#### (\d+)",
            # regex_pattern="(-?[$0-9.,]{2,})|(-?[0-9]+)",
            group_select=0,
            fallback="[no match]"
        ),
        TakeFirstFilter(),
    ]

    # 以下是错误的实验，takefirst最好放在最后，不然会把回答的string拆成char。。。。
    # filters = [
    #     TakeFirstFilter(),
    #     RegexFilter(
    #         # regex_pattern=r"#### (\d+)",
    #         regex_pattern="(-?[$0-9.,]{2,})|(-?[0-9]+)",
    #         group_select=0,
    #         fallback="[no match]"
    #     ),
    # ]
    
    test_doc = task.test_docs()[0]
    print("测试文档:", test_doc)
    model_responses = test_doc["model_responses"]
    
    # 初始化输入格式为 [[候选回答列表]]
    # 每个文档对应一个列表，列表中是多个候选回答
    filtered_responses = [model_responses]  # 注意此处包装为列表的列表
    
    for filter in filters:
        # 输入格式需为 [每个文档的候选回答列表]，例如 [[resp1, resp2], [resp3, resp4]]
        # 输出格式也是列表的列表，需通过 list() 强制转换生成器
        filtered_responses = list(filter.apply(filtered_responses, [test_doc]))
        print("Filter名称:", filter.__class__.__name__)
        print("Filter输出:", filtered_responses)
        print('-' * 50)
    
    # 提取最终结果
    final_result = filtered_responses[0][0]  # 第一个文档的第一个回答
    
    print("原始回答列表:", model_responses)
    print("应用 take_first 后:", [model_responses[0]])
    print("最终提取结果:", final_result)

if __name__ == "__main__":
    test_regex_behavior()