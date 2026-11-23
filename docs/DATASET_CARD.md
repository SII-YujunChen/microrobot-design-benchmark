# Dataset card

**Microrobot Design Benchmark v2.1.0** contains 800 English prompts in eight collections. It covers component retrieval, evidence assessment, design reasoning, high-level scenario design, and interpretation of microrobot data. The translations retain the source questions’ technical identifiers, named systems, constraints, and requested outputs. The [question index](QUESTIONS.md) groups the prompts by task and links to the corresponding data files.

## Question identity and release history

Q001–Q700 follow the original source numbering. Q701–Q800 continue the sequence with new cases authored in English. Version 1.0.0 published the 100 questions from Q201 to Q300. Version 2.0.0 includes English translations of those 100 questions, the preceding 200, and the following 400. The same ID links questions across languages. Report the language used for every run. The historical snapshot check for Q201–Q300 applies to the original Chinese strings. [Source inventory and checks](../provenance.json) · [Source prompt hashes](../source_question_hashes.json)

The eight collections identify task families. Within each collection, `category` provides a finer grouping. For example, Q301–Q700 contains 40 scenario topics with ten questions each. Closely related tasks can occur across collections. Researchers can use the questions for open development and evaluation and should disclose previous use when reporting results.

## Question fields

The combined JSONL, collection JSONLs and CSV share these columns. JSONL uses UTF-8 with one object per line. The CSV includes a UTF-8 byte order mark for spreadsheet readers. [Record schema](../schema/question.schema.json) · [Counts and collection ranges](../dataset_info.json)

| Field | Meaning |
| --- | --- |
| `id` | Stable source identifier, including leading zeros where applicable, e.g. `Q001`. Use this to join evaluator references. |
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

## Advanced data interpretation cases

The new collection consists of four sets of 25 cases. All measurements, study summaries, costs, and reference labels in those cases are synthetic and were created for this release. The case keys grade deductions from the supplied records. They do not describe experimental observations. The collection is publicly available with its keys, so benchmark reports should identify any prior exposure. No model or human performance distribution has been established for the new cases. [Challenge questions](questions/advanced_data_interpretation.md)

## Evaluator references

Each evaluator record contains the question `id`, a `rubric_id` for collections with a numbered scoring rubric, and `source_metadata`. A null `rubric_id` means the source has no fixed numeric scale for that collection. Text originally written in Chinese is translated into English in the evaluator metadata. Depending on the task, the metadata can include reference identifiers, expected behavior, grading criteria, module suggestions or a `should_be_blocked` flag. A true flag identifies an item intended to test refusal. A source label such as `human_scored` describes the intended evaluation method. A difficulty label reflects the source author's judgment. [Evaluator records](../evaluation/reference_metadata.jsonl) · [Scoring rubrics](../evaluation/rubrics.json)

This release provides prompts and evaluator references. Reproducing a reported result also requires the run configuration, model or system, evidence collection and scoring protocol used in that experiment. [Evaluation guide](EVALUATION.md)
