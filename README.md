# Microrobot Design Benchmark

This benchmark contains **800 English questions** about biological microrobot design. Q001–Q700 cover component retrieval, evidence assessment, and design reasoning. **Q701–Q800 ask for an original robot design.** Each brief gives a mission, available biological capabilities, and constraints that rule out an obvious solution. Respondents decide how the robot will sense, move or act, and report or recover when part of the design fails.

The first public release covered Q201–Q300, now in Basic Design and Scenario Design. For Q701–Q800, cite the release together with the ID. Version 2.1.0 used that range for different prompts; its scores belong to that edition. [Release history](CHANGELOG.md)

[Browse all questions](docs/QUESTIONS.md) · [Download JSONL](https://raw.githubusercontent.com/SII-YujunChen/microrobot-design-benchmark/v3.0.0/data/questions.jsonl) · [Download CSV](https://raw.githubusercontent.com/SII-YujunChen/microrobot-design-benchmark/v3.0.0/data/questions.csv) · [Dataset card](docs/DATASET_CARD.md)

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
| [Advanced Biological Microrobot Design](docs/questions/advanced_biorobot_design.md) | Q701–Q800 | 100 | Design an embodied biological robot, resolve competing requirements, and justify a complete architecture. | [JSONL](data/advanced_biorobot_design.jsonl) |

## Working on a design brief

Start with the mission and the constraint that makes it difficult. Describe the biological function and the robot body, explain what information or force crosses their interface, and trace how the system behaves on a successful mission and in the failure condition named in the brief. Different architectures can earn full credit. The evaluator file gives four brief-specific criteria and one example of a feasible alternative.

[Browse the 100 design briefs](docs/questions/advanced_biorobot_design.md) · [Download the design questions](https://raw.githubusercontent.com/SII-YujunChen/microrobot-design-benchmark/v3.0.0/data/advanced_biorobot_design.jsonl) · [Design scoring guide](docs/EVALUATION.md#score-a-design-brief)

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

Version 3.0.0 was released on November 23, 2026. The questions, evaluator references and documentation use CC BY 4.0. Utility scripts use the MIT license. [Changelog](CHANGELOG.md) · [CC BY 4.0](licenses/CC-BY-4.0.txt) · [MIT](licenses/MIT.txt)
