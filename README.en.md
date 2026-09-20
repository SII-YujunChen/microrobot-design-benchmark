# Microrobot Design Benchmark

A Chinese-language dataset of **100 open-ended questions** for evaluating high-level biological microrobot design. Release **v1.0.0** preserves the original Q201–Q300 IDs and prompt strings.

[中文说明](README.md) · [Browse all questions](docs/QUESTIONS.md) · [JSONL](data/questions.jsonl) · [CSV](data/questions.csv)

| Subset | IDs | Questions |
| --- | --- | ---: |
| Basic Design | Q201–Q250 | 50 |
| Scenario Design | Q251–Q300 | 50 |

The tasks cover requirement decomposition, module necessity, sensing, logic, memory, output, evidence grounding and feasibility review. All prompts remain in Chinese; English translations are not included. Prompt strings match the historical evaluation snapshot for all 100 IDs.

Use only `question` as the task input. Original evaluator metadata and the two distinct 10-point rubric definitions are under `evaluation/`. The source `human_scored` label describes an intended scoring format, not a released set of completed human ratings. This release contains no model answers or historical score tables.

```bash
git clone https://github.com/SII-YujunChen/microrobot-design-benchmark.git
cd microrobot-design-benchmark
python3 scripts/validate_dataset.py
```

The validation tool uses only the Python standard library and checks IDs, counts, subsets, schema fields, question hashes, source-question correspondence, rubric weights, CSV consistency and release-file checksums.

These questions have been used in system and evaluation development and should be treated as an open development/evaluation set. See the [dataset card](docs/DATASET_CARD.md), [evaluation notes](docs/EVALUATION.md), and [provenance](provenance.json).

Related paper: [An Evidence-Grounded Multi-Agent System for High-Level Bio-Robot Design](https://arxiv.org/abs/2608.19699v1). Cite the dataset version and the paper using [CITATION.cff](CITATION.cff).

Data and documentation: [CC BY 4.0](licenses/CC-BY-4.0.txt). Utility scripts: [MIT](licenses/MIT.txt).
