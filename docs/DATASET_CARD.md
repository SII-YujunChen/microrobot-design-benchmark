# 数据集说明

## 基本信息

- 名称：Microrobot Design Benchmark
- 版本：1.0.0；发布日期：2026-09-20
- 规模：100 题；Q201–Q250 基础设计 50 题，Q251–Q300 场景设计 50 题
- 语言：简体中文，题干中保留原有英文技术术语
- 题型：开放式高层设计与方案审查
- 维护账号：[SII-YujunChen](https://github.com/SII-YujunChen)

## 来源与整理

题目来自项目的两个原始题库文件，文件名和 SHA-256 见根目录 `provenance.json`。整理时保留每题原始 ID 与 `query` 字符串，将后者映射为 `question`；另与 2026-08-14 报告数据包中的 `questions_only.jsonl` 核对，100 题题干和题干哈希全部一致。

Q201–Q250 使用原有标题；Q251–Q300 补充便于浏览的编辑标题。分类字段统一为 10 类，同时保留 `source_category`。新标题与统一分类不参与评分，也不额外加入模型题目输入。

## 应用分类

| 中文分类 | 标识 | 题数 |
| --- | --- | ---: |
| 农业与土壤 | agriculture_soil | 4 |
| 群体协同 | collective_systems | 4 |
| 设计工具适配 | design_tool_interoperability | 3 |
| 环境监测 | environmental_monitoring | 13 |
| 肠道监测 | gut_monitoring | 15 |
| 工业生物制造 | industrial_biomanufacturing | 13 |
| 感染与创面 | infection_wound | 14 |
| 组织工程与生物材料 | tissue_engineering | 8 |
| 肿瘤微环境 | tumor_microenvironment | 16 |
| 血管与血栓 | vascular_monitoring | 10 |

## 字段说明

| 字段 | 类型 | 含义 |
| --- | --- | --- |
| `id` | string | 原始唯一题号，如 Q201 |
| `index` | integer | 201–300 的数字题号 |
| `subset` | string | basic_design 或 scenario_design |
| `language` | string | zh-CN |
| `title` | string | 浏览标题 |
| `category` | string | 统一应用分类 |
| `category_label_zh` | string | 中文分类名称 |
| `source_category` | string | 原始 scenario/category 字段值 |
| `task_type` | string | 原始任务类型 |
| `question` | string | 原始题干，作为系统测试输入 |
| `question_sha256` | string | 原始题干 UTF-8 字节的 SHA-256，带 sha256: 前缀 |

## 评审参考

`evaluation/reference_metadata.jsonl` 按题号保存所有原始非题干元数据：包括原始标题、分类、预期能力、部分题目的预期模块、评分权重和原有范围约束。基础设计和场景设计各自保留原有 10 分制，未将两者改写为统一新标准。`expected_modules` 是设计审查参考，应结合题干判断必要性和可选性；不要求机械覆盖所有模块。

原题元数据中的 `label_type=human_scored` 表示预期采用人工评分的题型标签；本发布不附人工评分记录。场景题保留原始 `difficulty=high`，不据此推断经实测校准的难度；基础题没有新增难度标签。

## 使用定位

本数据集用于比较系统在指定题目上的需求理解、设计表达与证据判断。题目曾参与管线及评分方法开发，适合作为公开开发与评测集。基础题与场景题存在相近主题，两个子集不是训练集与隐藏测试集的划分。报告时应写明版本、子集、模型、提示词及评分规则。

问题与评审参考均以高层设计为任务范围；保持原题中的模块级、低风险报告和非操作性设计要求。没有新增序列、实验参数、实验流程或参考实施方案。

## 版本维护

v1.0.0 是公开整理版本。后续改写题干、改变权重或扩充题目时发布新版本，记录变更并更新哈希；原始题号保持稳定。数据文件和文档按 CC BY 4.0 发布。
