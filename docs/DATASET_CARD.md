# Dataset card

**Microrobot Design Benchmark v3.0.0** contains 800 English prompts in eight collections. It covers component retrieval, evidence assessment, design reasoning, high-level scenario design, and advanced biohybrid system design. The translations retain the source questions’ technical identifiers, named systems, constraints, and requested outputs. The [question index](QUESTIONS.md) groups the prompts by task and links to the corresponding data files.

## Question identity and release history

Q001–Q700 follow the original source numbering. In v3.0.0, Q701–Q800 identify 100 original English design briefs. The [v2.1.0 release](https://github.com/SII-YujunChen/microrobot-design-benchmark/releases/tag/v2.1.0) used those numbers for a different collection on data interpretation. Use the release and prompt hash when comparing runs or joining evaluator keys. Version 1.0.0 published the 100 questions from Q201 to Q300. Version 2.0.0 includes English translations of those 100 questions, the preceding 200, and the following 400. The same ID links questions across languages. Report the language used for every run. The historical snapshot check for Q201–Q300 applies to the original Chinese strings. [Source inventory and checks](../provenance.json) · [Source prompt hashes](../source_question_hashes.json)

The eight collections identify task families. Within each collection, `category` provides a finer grouping. For example, Q301–Q700 contains 40 scenario topics with ten questions each. Closely related tasks can occur across collections. Researchers can use the questions for open development and evaluation and should disclose previous use when reporting results.

## Question fields

The combined JSONL, collection JSONLs and CSV share these columns. JSONL uses UTF-8 with one object per line. The CSV includes a UTF-8 byte order mark for spreadsheet readers. [Record schema](../schema/question.schema.json) · [Counts and collection ranges](../dataset_info.json)

| Field | Meaning |
| --- | --- |
| `id` | Question identifier within the release, including leading zeros where applicable, e.g. `Q001`. Join evaluator references from the same release. |
| `index` | Numeric part of the ID, from 1 to 800. |
| `subset` | Machine-readable name of the question collection. Its file is `data/<subset>.jsonl`. |
| `language` | Language of the prompt, `en`. |
| `title` | English display title for browsing. Q701–Q800 use individual case titles. |
| `category` | Grouping key within the collection, based on task type or topic. |
| `category_label_en` | English display label for the category. |
| `source_category` | Source grouping, translated to English where necessary. Earlier collections use the task type when it is the only source grouping. |
| `task_type` | Original task label, such as retrieval, evidence attribution or scenario design. |
| `question` | English prompt, translated for Q001–Q700 and authored in English for Q701–Q800. Use this field as the question shown to the system. |
| `question_sha256` | SHA-256 of the released English prompt’s UTF-8 bytes, prefixed with `sha256:`. |
| `source_prompt_sha256` | SHA-256 of the source prompt’s UTF-8 bytes. For Q701–Q800 the released English prompt is the source, so the two hashes match. |

## Advanced design briefs

The 100 briefs span sensing, memory and reporting; locomotion, contact and manipulation; collective and distributed behavior; and system integration and fault recovery. Each poses a design problem for a biological or biohybrid robot in a specified setting. Stated sensing, actuation, and material capabilities are hypothetical design assumptions. A strong submission explains how its chosen interfaces work together, which trade-off it accepts, and which failure would make its claim untenable.

Each brief has four individual grading criteria and a conditional example of an alternative architecture. These are public development and evaluation questions. Empirical difficulty, rater agreement, and separation between systems have yet to be measured. [Design briefs](questions/advanced_biorobot_design.md) · [Evaluator key](../evaluation/advanced_biorobot_design_key.jsonl)

## Evaluator references

Each evaluator record contains the question `id`, a `rubric_id` for collections with a numbered scoring rubric, and `source_metadata`. A null `rubric_id` means the source has no fixed numeric scale for that collection. Text originally written in Chinese is translated into English in the evaluator metadata. Depending on the task, the metadata can include reference identifiers, expected behavior, grading criteria, module suggestions or a `should_be_blocked` flag. A true flag identifies an item intended to test refusal. A source label such as `human_scored` describes the intended evaluation method. A difficulty label reflects the source author's judgment. [Evaluator records](../evaluation/reference_metadata.jsonl) · [Scoring rubrics](../evaluation/rubrics.json)

This release provides prompts and evaluator references. Reproducing a reported result also requires the run configuration, model or system, evidence collection and scoring protocol used in that experiment. [Evaluation guide](EVALUATION.md)
