# Microrobot Design Benchmark

This benchmark contains **800 English questions** about biological microrobot design and data interpretation. It tests whether a system can retrieve relevant evidence, judge what that evidence supports, and review a proposed design. Q001–Q700 are translations of the original design and evidence questions. Q701–Q800 are new English-language cases based on synthetic microrobot measurements, tracking records, and study reports. The first public release covered only Q201–Q300. Those IDs now identify the English versions in the Basic Design and Scenario Design collections.

[Browse all questions](docs/QUESTIONS.md) · [Download JSONL](https://raw.githubusercontent.com/SII-YujunChen/microrobot-design-benchmark/v2.1.0/data/questions.jsonl) · [Download CSV](https://raw.githubusercontent.com/SII-YujunChen/microrobot-design-benchmark/v2.1.0/data/questions.csv) · [Dataset card](docs/DATASET_CARD.md)

## Choose a collection

| Collection | Original IDs | Questions | What it tests | Data |
| --- | --- | ---: | --- | --- |
| [Component Retrieval and Evidence](docs/questions/component_retrieval.md) | Q001–Q050 | 50 | Find candidate components and explain their supporting evidence and limitations. | [JSONL](data/component_retrieval.jsonl) |
| [Design Reasoning and Review](docs/questions/design_reasoning.md) | Q051–Q100 | 50 | Compare design choices and judge when the available evidence is insufficient. | [JSONL](data/design_reasoning.jsonl) |
| [Retrieval and Evidence Stress Tests](docs/questions/evidence_stress_tests.md) | Q101–Q150 | 50 | Rank relevant records, distinguish plausible but incorrect matches, and check source attribution. | [JSONL](data/evidence_stress_tests.jsonl) |
| [Applied Scenario Reasoning](docs/questions/applied_scenarios.md) | Q151–Q200 | 50 | Use evidence to make or review a decision under the constraints of an application. | [JSONL](data/applied_scenarios.jsonl) |
| [Basic Design](docs/questions/basic_design.md) | Q201–Q250 | 50 | Break a requirement into functions and justify which modules it needs. | [JSONL](data/basic_design.jsonl) |
| [Scenario Design](docs/questions/scenario_design.md) | Q251–Q300 | 50 | Propose a high-level design for a given scenario and examine its feasibility. | [JSONL](data/scenario_design.jsonl) |
| [Extended Scenario Design](docs/questions/extended_scenario_design.md) | Q301–Q700 | 400 | Review complete designs across 40 topics, with 10 questions per topic. | [JSONL](data/extended_scenario_design.jsonl) |
| [Advanced Data Interpretation Challenge](docs/questions/advanced_data_interpretation.md) | Q701–Q800 | 100 | Interpret supplied measurements, reconcile conflicting observations, and justify a decision under uncertainty. | [JSONL](data/advanced_data_interpretation.jsonl) |

## Taking the data interpretation challenge

Each of the 100 cases includes the evidence and decision criteria needed to answer it. Work from the question alone, show the calculations or comparison, and qualify conclusions that the evidence cannot settle. The four topic areas cover measurement and calibration, tracking and time series, evidence and study validity, and benchmarking decisions. Each case has its own four-point key. The cases were written to challenge multi-step reasoning; their empirical difficulty and ability to distinguish systems have yet to be measured. [Browse cases](docs/questions/advanced_data_interpretation.md) · [Evaluator key](evaluation/advanced_data_interpretation_key.jsonl)

## Use the data

Each row in the full JSONL or CSV is one question. Use the English `question` string as the model input and save the output with its `id`. Retrieval tasks that refer to “the database” also depend on the collection of records available to the system under test. Record that collection and its version with your results.

Join evaluator references by `id` after collecting responses. The first four collections provide task-specific evaluation cues. Basic Design, Scenario Design and Extended Scenario Design have separate rubrics worth 10, 10 and 20 points, respectively. Report the release version, prompt language, and results for each collection. The language change can affect comparisons with historical runs in Chinese. [Evaluation guide](docs/EVALUATION.md)

Validate a local copy with Python's standard library.

```sh
git clone https://github.com/SII-YujunChen/microrobot-design-benchmark.git
cd microrobot-design-benchmark
python3 scripts/validate_dataset.py
```

## Citation and license

Cite the dataset version and the related paper when reporting results. [Citation file](CITATION.cff) · [An Evidence-Grounded Multi-Agent System for High-Level Bio-Robot Design](https://arxiv.org/abs/2608.19699v1)

Version 2.1.0 was released on November 23, 2026. The questions, evaluator references and documentation use CC BY 4.0. Utility scripts use the MIT license. [Changelog](CHANGELOG.md) · [CC BY 4.0](licenses/CC-BY-4.0.txt) · [MIT](licenses/MIT.txt)
