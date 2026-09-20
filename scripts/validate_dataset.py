#!/usr/bin/env python3
"""Validate the released question dataset using the Python standard library."""
import csv
import hashlib
import json
import sys
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def require(condition, message):
    if not condition:
        raise ValueError(message)


def read_json(path):
    return json.loads((ROOT / path).read_text(encoding="utf-8"))


def read_jsonl(path):
    return [json.loads(line) for line in (ROOT / path).read_text(encoding="utf-8").splitlines() if line.strip()]


def main():
    rows = read_jsonl("data/questions.jsonl")
    refs = read_jsonl("evaluation/reference_metadata.jsonl")
    schema = read_json("schema/question.schema.json")
    info = read_json("dataset_info.json")
    rubrics = {r["id"]: r for r in read_json("evaluation/rubrics.json")["rubrics"]}
    expected_ids = [f"Q{n}" for n in range(201, 301)]
    require([r["id"] for r in rows] == expected_ids, "Expected exactly Q201–Q300 in order")
    require([r["id"] for r in refs] == expected_ids, "Evaluator metadata IDs do not match")
    require(len({r["question"] for r in rows}) == 100, "Duplicate question strings")
    reference = {r["id"]: r for r in refs}
    reconstructed = {"basic_design": [], "scenario_design": []}
    for r in rows:
        ident = r["id"]
        require(set(r) == set(schema["required"]), f"{ident}: unexpected or missing fields")
        for key, spec in schema["properties"].items():
            require(type(r[key]) is (int if spec["type"] == "integer" else str), f"{ident}: type of {key}")
            if "enum" in spec:
                require(r[key] in spec["enum"], f"{ident}: invalid {key}")
            if "const" in spec:
                require(r[key] == spec["const"], f"{ident}: invalid {key}")
            if "minLength" in spec:
                require(len(r[key].strip()) >= spec["minLength"], f"{ident}: empty {key}")
        require(r["index"] == int(ident[1:]), f"{ident}: index mismatch")
        subset = "basic_design" if r["index"] <= 250 else "scenario_design"
        require(r["subset"] == subset, f"{ident}: incorrect subset")
        expected_hash = "sha256:" + hashlib.sha256(r["question"].encode("utf-8")).hexdigest()
        require(r["question_sha256"] == expected_hash, f"{ident}: question hash mismatch")
        ref = reference[ident]
        rubric = rubrics[ref["rubric_id"]]
        meta = ref["source_metadata"]
        require(rubric["subset"] == subset, f"{ident}: rubric subset mismatch")
        require(meta[rubric["source_field"]] == rubric["dimensions"], f"{ident}: rubric mismatch")
        require(sum(rubric["dimensions"].values()) == 10, f"{ident}: rubric does not total 10")
        require(r["source_category"] == meta.get("scenario", meta.get("category")), f"{ident}: original category mismatch")
        require(r["task_type"] == meta["task_type"], f"{ident}: task type mismatch")
        require(r["question"] in (ROOT / "docs/QUESTIONS.md").read_text(encoding="utf-8"), f"{ident}: question missing from browser document")
        reconstructed[subset].append({"id": ident, "query": r["question"], **meta})
    for subset in reconstructed:
        require(read_jsonl(f"data/{subset}.jsonl") == [r for r in rows if r["subset"] == subset], f"{subset}: split mismatch")
        require(len(reconstructed[subset]) == 50, f"{subset}: expected 50 questions")
    require(info["question_count"] == len(rows), "Dataset info count mismatch")
    require(info["category_counts"] == dict(Counter(r["category"] for r in rows)), "Category counts mismatch")
    with (ROOT / "data/questions.csv").open(encoding="utf-8-sig", newline="") as stream:
        csv_rows = list(csv.DictReader(stream))
    for r in csv_rows:
        r["index"] = int(r["index"])
    require(csv_rows == rows, "CSV and JSONL are inconsistent")
    # Check original question hashes preserved during the verified snapshot comparison.
    source_hashes = read_json("source_question_hashes.json")
    require(source_hashes == {r["id"]: r["question_sha256"] for r in rows}, "Original question identity changed")
    checksums = (ROOT / "SHA256SUMS.txt").read_text(encoding="utf-8").splitlines()
    listed = set()
    for line in checksums:
        expected, rel = line.split("  ", 1)
        file = ROOT / rel
        require(file.is_file(), f"Missing release file: {rel}")
        require(hashlib.sha256(file.read_bytes()).hexdigest() == expected, f"Checksum mismatch: {rel}")
        listed.add(rel)
    actual = {p.relative_to(ROOT).as_posix() for p in ROOT.rglob("*") if p.is_file() and ".git" not in p.relative_to(ROOT).parts and "__pycache__" not in p.parts and p.name not in {"SHA256SUMS.txt", ".DS_Store"}}
    require(listed == actual, "Checksum manifest does not match release file set")
    print(f"PASS: 100 unique questions, 50 + 50 subsets, schema fields, original prompt hashes, rubric weights, CSV/JSONL consistency and {len(listed)} file checksums.")


if __name__ == "__main__":
    try:
        main()
    except (ValueError, KeyError, TypeError, OSError) as exc:
        print(f"FAIL: {exc}", file=sys.stderr)
        sys.exit(1)
