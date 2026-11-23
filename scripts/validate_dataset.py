#!/usr/bin/env python3
"""Validate the released question dataset using the Python standard library."""
import csv
import hashlib
import json
import re
import sys
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CHALLENGE = "advanced_biorobot_design"
CHALLENGE_TOPICS = ("biological_sensing_and_memory", "biohybrid_locomotion_and_manipulation", "collective_biorobot_design", "biorobot_system_integration")
# Source numbering, category field, and numeric rubric for each collection.
SUBSETS = {
    "component_retrieval": (1, 50, "task_type", None, None),
    "design_reasoning": (51, 100, "task_type", None, None),
    "evidence_stress_tests": (101, 150, "task_type", None, None),
    "applied_scenarios": (151, 200, "application_scenario", None, None),
    "basic_design": (201, 250, "scenario", "rubric", 10),
    "scenario_design": (251, 300, "category", "rubric_10pt", 10),
    "extended_scenario_design": (301, 700, "category", "rubric_20pt", 20),
    CHALLENGE: (701, 800, "category", "rubric_4pt", 4),
}


def require(condition, message):
    if not condition:
        raise ValueError(message)


def read_json(path):
    return json.loads((ROOT / path).read_text(encoding="utf-8"))


def read_jsonl(path):
    with (ROOT / path).open(encoding="utf-8") as stream:
        return [json.loads(line) for line in stream if line.strip()]


def check_schema(row, schema):
    ident = row["id"]
    require(set(row) == set(schema["required"]), f"{ident}: unexpected or missing fields")
    for key, spec in schema["properties"].items():
        value = row[key]
        required_type = {"string": str, "integer": int}[spec["type"]]
        require(type(value) is required_type, f"{ident}: invalid type for {key}")
        if "enum" in spec:
            require(value in spec["enum"], f"{ident}: invalid {key}")
        if "const" in spec:
            require(value == spec["const"], f"{ident}: invalid {key}")
        if "minLength" in spec:
            require(len(value.strip()) >= spec["minLength"], f"{ident}: too short {key}")
        if "pattern" in spec:
            require(re.search(spec["pattern"], value), f"{ident}: invalid format for {key}")
        if "minimum" in spec:
            require(value >= spec["minimum"], f"{ident}: {key} below minimum")
        if "maximum" in spec:
            require(value <= spec["maximum"], f"{ident}: {key} above maximum")


def check_reference(row, ref, category_key, rubric):
    ident = row["id"]
    meta = ref["source_metadata"]
    require(row["source_category"] == meta[category_key], f"{ident}: source category mismatch")
    require(row["task_type"] == meta["task_type"], f"{ident}: task type mismatch")
    if category_key == "task_type" or row["subset"] in {"extended_scenario_design", CHALLENGE}:
        require(row["category"] == row["source_category"], f"{ident}: category mismatch")
    if rubric is None:
        require(ref["rubric_id"] is None, f"{ident}: unexpected numeric rubric")
    else:
        require(ref["rubric_id"] == rubric["id"], f"{ident}: incorrect rubric ID")
        require(meta[rubric["source_field"]] == rubric["dimensions"], f"{ident}: rubric weights mismatch")


def check_browser(subset, rows, index_page):
    page = f"questions/{subset}.md"
    require(page in index_page, f"{subset}: missing from question index")
    document = (ROOT / "docs" / page).read_text(encoding="utf-8")
    # Compare each prompt to the text under its own heading, including its punctuation.
    sections = re.split(r"^### (Q[0-9]{3})\b[^\n]*$", document, flags=re.MULTILINE)
    require(sections[1::2] == [r["id"] for r in rows], f"{subset}: incorrect browser IDs")
    for row, body in zip(rows, sections[2::2]):
        paragraphs = body.strip("\n").split("\n\n")
        require(row["question"] in paragraphs, f"{row['id']}: incorrect browser prompt")


def check_challenge(rows, refs):
    key = read_jsonl("evaluation/advanced_biorobot_design_key.jsonl")
    require(key == refs, "Standalone challenge key differs from combined evaluator records")
    require(len({r["title"] for r in rows}) == len(rows), "Duplicate challenge title")
    for i, (row, ref) in enumerate(zip(rows, key)):
        ident = row["id"]
        meta = ref["source_metadata"]
        require(row["category"] == CHALLENGE_TOPICS[i // 25], f"{ident}: incorrect challenge topic")
        require(meta["source_language"] == "en" and meta["scenario_origin"] == "hypothetical_design_brief"
                and row["task_type"] == "design_biorobot_system",
                f"{ident}: incorrect challenge provenance")
        anchors = meta["grading_anchors"]
        require(isinstance(anchors, list) and len(anchors) == 4
                and all(isinstance(a, str) and a.strip() for a in anchors)
                and len(set(anchors)) == 4, f"{ident}: four distinct scoring criteria required")
        require(isinstance(meta["acceptable_alternative"], str) and meta["acceptable_alternative"].strip(),
                f"{ident}: missing alternative scoring guidance")
        require(meta["rubric_4pt"] == {f"criterion_{n}": 1 for n in range(1, 5)},
                f"{ident}: challenge scoring weights differ")


def check_checksums():
    listed = set()
    for line in (ROOT / "SHA256SUMS.txt").read_text(encoding="utf-8").splitlines():
        expected, rel = line.split("  ", 1)
        file = ROOT / rel
        require(rel not in listed, f"Duplicate checksum entry: {rel}")
        require(file.is_file(), f"Missing release file: {rel}")
        data = file.read_bytes()
        require(hashlib.sha256(data).hexdigest() == expected, f"Checksum mismatch: {rel}")
        require(not re.search(r"[\u3400-\u9fff\uf900-\ufaff]", data.decode("utf-8-sig")),
                f"Unexpected Chinese text in the English release: {rel}")
        listed.add(rel)
    actual = {
        p.relative_to(ROOT).as_posix() for p in ROOT.rglob("*")
        if p.is_file() and ".git" not in p.relative_to(ROOT).parts
        and "__pycache__" not in p.parts and p.name not in {"SHA256SUMS.txt", ".DS_Store"}
    }
    require(listed == actual, f"Checksum manifest file set mismatch: {sorted(listed ^ actual)}")
    return len(listed)


def main():
    rows = read_jsonl("data/questions.jsonl")
    refs = read_jsonl("evaluation/reference_metadata.jsonl")
    schema = read_json("schema/question.schema.json")
    info = read_json("dataset_info.json")
    rubrics = read_json("evaluation/rubrics.json")["rubrics"]
    rubric_by_subset = {r["subset"]: r for r in rubrics}
    expected_graded = {name for name, fields in SUBSETS.items() if fields[3] is not None}
    require(len(rubrics) == len(expected_graded) and set(rubric_by_subset) == expected_graded,
            "Expected one numeric rubric for each scored subset")
    require(len({r["id"] for r in rubrics}) == len(rubrics), "Duplicate rubric IDs")

    expected_ids = [f"Q{n:03d}" for n in range(1, 801)]
    require([r["id"] for r in rows] == expected_ids, "Expected exactly Q001–Q800 in order")
    require([r["id"] for r in refs] == expected_ids, "Evaluator metadata IDs do not match")
    require(len({r["question"] for r in rows}) == len(rows), "Duplicate question strings")
    require(info["language"] == "en", "Dataset language must be English")
    require(info["question_count"] == len(rows), "Dataset info count mismatch")
    require(info["id_range"] == [expected_ids[0], expected_ids[-1]], "Dataset ID range mismatch")
    require(set(info["subsets"]) == set(SUBSETS), "Dataset subset names mismatch")
    require(info["category_counts"] == dict(Counter(r["category"] for r in rows)), "Category counts mismatch")

    index_page = (ROOT / "docs/QUESTIONS.md").read_text(encoding="utf-8")
    for subset, (first, last, category_key, rubric_field, maximum_score) in SUBSETS.items():
        group = rows[first - 1:last]
        details = info["subsets"][subset]
        require(details["count"] == len(group), f"{subset}: incorrect subset count")
        require(details["id_range"] == [group[0]["id"], group[-1]["id"]], f"{subset}: incorrect range")
        require(group == read_jsonl(f"data/{subset}.jsonl"), f"{subset}: split differs from full dataset")
        check_browser(subset, group, index_page)
        rubric = rubric_by_subset.get(subset)
        if rubric is not None:
            require(rubric["source_field"] == rubric_field, f"{subset}: incorrect source rubric field")
            require(rubric["maximum_score"] == sum(rubric["dimensions"].values()) == maximum_score,
                    f"{subset}: rubric weights must total {maximum_score}")
        for row, ref in zip(group, refs[first - 1:last]):
            ident = row["id"]
            check_schema(row, schema)
            require(row["index"] == int(ident[1:]), f"{ident}: index mismatch")
            require(row["subset"] == subset, f"{ident}: incorrect subset")
            digest = hashlib.sha256(row["question"].encode("utf-8")).hexdigest()
            require(row["question_sha256"] == "sha256:" + digest, f"{ident}: question hash mismatch")
            check_reference(row, ref, category_key, rubric)

    check_challenge(rows[700:], refs[700:])

    with (ROOT / "data/questions.csv").open(encoding="utf-8-sig", newline="") as stream:
        csv_rows = list(csv.DictReader(stream))
    for row in csv_rows:
        row["index"] = int(row["index"])
    require(csv_rows == rows, "CSV and JSONL are inconsistent")
    source_hashes = read_json("source_question_hashes.json")
    require(source_hashes == {r["id"]: r["source_prompt_sha256"] for r in rows}, "Original prompt hashes differ")
    for row in rows:
        same_hash = row["source_prompt_sha256"] == row["question_sha256"]
        require(same_hash == (row["subset"] == CHALLENGE), f"{row['id']}: source language/hash mismatch")
    file_count = check_checksums()
    print(f"PASS: {len(rows)} unique English questions in {len(SUBSETS)} subsets, English and source prompt hashes, "
          f"rubrics, browser pages, CSV/JSONL agreement and {file_count} file checksums.")


if __name__ == "__main__":
    try:
        main()
    except (ValueError, KeyError, TypeError, OSError) as exc:
        print(f"FAIL: {exc}", file=sys.stderr)
        sys.exit(1)
