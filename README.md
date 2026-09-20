# Microrobot Design Benchmark

用于生物微机器人高层设计评测的 **100 道中文开放式测试题**，保留 Q201–Q300 原始题号与题干。包含基础设计 50 题、场景设计 50 题，覆盖需求拆解、模块必要性判断、感知与逻辑、记忆与输出、证据判断及可行性分析。

**版本：v1.0.0 · 语言：中文 · 数据许可：CC BY 4.0 · 工具许可：MIT**

[浏览全部 100 题](docs/QUESTIONS.md) · [下载 JSONL](data/questions.jsonl) · [下载 CSV](data/questions.csv) · [数据集说明](docs/DATASET_CARD.md) · [评分说明](docs/EVALUATION.md) · [English](README.en.md)

## 数据组成

| 子集 | 题号 | 题数 | 主要任务 |
| --- | --- | ---: | --- |
| Basic Design 基础设计 | Q201–Q250 | 50 | 模块职责与必要性、场景适配、设计工具适配 |
| Scenario Design 场景设计 | Q251–Q300 | 50 | 应用场景下的整体架构、接口与可行性分析 |

题目面向模块级设计与方案审查。`question` 是模型应接收的原始输入；评审参考字段单独放在 `evaluation/` 中。题干与历史 Q201–Q300 评测快照逐题一致，100 个 ID 连续、唯一，100 个题干无完全重复。

## 快速使用

```bash
git clone https://github.com/SII-YujunChen/microrobot-design-benchmark.git
cd microrobot-design-benchmark
python3 scripts/validate_dataset.py
```

```python
import json
from pathlib import Path

questions = [json.loads(line) for line in Path("data/questions.jsonl").read_text(encoding="utf-8").splitlines()]
for item in questions:
    prompt = item["question"]
    # 将 prompt 传入待评测系统，按 item["id"] 保存回答。
```

`data/questions.csv` 使用 UTF-8 BOM，便于表格软件读取中文。JSONL 使用 UTF-8，每行一条记录。验证脚本仅使用 Python 标准库。

## 文件结构

| 路径 | 内容 |
| --- | --- |
| `data/questions.jsonl` | 100 题完整规范数据 |
| `data/basic_design.jsonl` | Q201–Q250 |
| `data/scenario_design.jsonl` | Q251–Q300 |
| `data/questions.csv` | 与主 JSONL 对应的 CSV |
| `evaluation/reference_metadata.jsonl` | 原始预期能力、模块、评分维度等评审参考字段 |
| `evaluation/rubrics.json` | 两组原有 10 分制评分权重 |
| `schema/question.schema.json` | 单条题目 JSON Schema |
| `provenance.json` | 来源文件哈希、题干核对与整理记录 |
| `SHA256SUMS.txt` | 发布文件校验清单 |

## 评测与引用

按子集分别报告成绩，保留模型版本、提示词、检索条件和运行记录。两组题的原始评分维度不同，具体评分方法见[评分说明](docs/EVALUATION.md)。本仓库发布题目与评分参考；模型回答和历史结果不在本次数据发布中。

相关研究：[An Evidence-Grounded Multi-Agent System for High-Level Bio-Robot Design](https://arxiv.org/abs/2608.19699v1)。使用本数据集时请引用本仓库版本和相关论文；引用格式见 [CITATION.cff](CITATION.cff)。

## 许可与维护

题目、评审参考与文档按 [CC BY 4.0](licenses/CC-BY-4.0.txt) 发布，`scripts/` 工具按 [MIT](licenses/MIT.txt) 发布。反馈题目问题时请附题号；修改题干的后续版本将记录新版本和新哈希。
