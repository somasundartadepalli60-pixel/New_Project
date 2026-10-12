"""Run offline structural checks before launching the LDICA web application.

This validation does not replace Flask integration tests. It checks Python
syntax, Jinja templates, catalogue integrity, question-bank structure,
template endpoint references, and local static assets without starting a server.
Usage: python scripts/validate_project.py
"""
from __future__ import annotations

import ast
import re
import sys
from pathlib import Path

from jinja2 import Environment, FileSystemLoader

ROOT = Path(__file__).resolve().parents[1]
APP = ROOT / "app"
TEMPLATES = APP / "templates"


def check_python_files() -> list[Path]:
    files = sorted([*APP.rglob("*.py"), *(ROOT / "scripts").glob("*.py"), *(ROOT / "tests").glob("*.py")])
    for path in files:
        ast.parse(path.read_text(encoding="utf-8"), filename=str(path))
    return files


def check_templates() -> list[Path]:
    env = Environment(loader=FileSystemLoader(str(TEMPLATES)))
    files = sorted(TEMPLATES.rglob("*.html"))
    for path in files:
        env.get_template(path.relative_to(TEMPLATES).as_posix())
    return files


def check_routes_and_assets(templates: list[Path]) -> tuple[int, int]:
    endpoints = {"static"}
    for path in (APP / "routes").glob("*.py"):
        tree = ast.parse(path.read_text(encoding="utf-8"), filename=str(path))
        blueprints = set()
        for node in tree.body:
            if isinstance(node, ast.Assign) and isinstance(node.value, ast.Call):
                for target in node.targets:
                    if isinstance(target, ast.Name) and target.id.endswith("_bp"):
                        blueprints.add(target.id)
            if isinstance(node, ast.FunctionDef):
                for decorator in node.decorator_list:
                    if (isinstance(decorator, ast.Call) and isinstance(decorator.func, ast.Attribute)
                            and isinstance(decorator.func.value, ast.Name)
                            and decorator.func.value.id in blueprints):
                        endpoints.add(f"{decorator.func.value.id.removesuffix('_bp')}.{node.name}")

    references: set[str] = set()
    asset_paths: set[str] = set()
    for path in templates:
        source = path.read_text(encoding="utf-8")
        references.update(re.findall(r"url_for\(['\"]([^'\"]+)['\"]", source))
        for static_path in re.findall(r"url_for\(['\"]static['\"]\s*,\s*filename=['\"]([^'\"]+)['\"]", source):
            asset_paths.add(static_path)

    missing_endpoints = sorted(references - endpoints)
    missing_assets = sorted(item for item in asset_paths if not ((APP / "static" / item).is_dir() if item.endswith("/") else (APP / "static" / item).is_file()))
    if missing_endpoints:
        raise ValueError("Unknown template endpoints: " + ", ".join(missing_endpoints))
    if missing_assets:
        raise ValueError("Missing local static assets: " + ", ".join(missing_assets))
    return len(references), len(asset_paths)


def check_content() -> tuple[int, int, int]:
    namespace: dict = {}
    catalog_path = APP / "content" / "catalog.py"
    exec(compile(catalog_path.read_text(encoding="utf-8"), str(catalog_path), "exec"), namespace)
    units = namespace["UNITS"]
    topics = [topic for unit in units for topic in unit["topics"]]
    slugs = [topic["slug"] for topic in topics]
    if len(units) != 5:
        raise ValueError(f"Expected 5 syllabus units, found {len(units)}")
    if len(slugs) != len(set(slugs)):
        raise ValueError("Duplicate topic slugs found in syllabus catalogue")

    lesson_ns: dict = {}
    lesson_path = APP / "content" / "lesson_bank.py"
    exec(compile(lesson_path.read_text(encoding="utf-8"), str(lesson_path), "exec"), lesson_ns)
    missing_lessons = sorted(set(slugs) - set(lesson_ns["LESSON_BANK"]))
    if missing_lessons:
        raise ValueError("Topics without lesson-bank entries: " + ", ".join(missing_lessons))

    question_ns: dict = {}
    question_path = APP / "content" / "mastery_questions.py"
    exec(compile(question_path.read_text(encoding="utf-8"), str(question_path), "exec"), question_ns)
    questions = question_ns["QUESTIONS"]
    keys = [question["key"] for question in questions]
    if len(keys) != len(set(keys)):
        raise ValueError("Duplicate question keys found")
    for question in questions:
        choices = question.get("choices", [])
        answer = question.get("answer")
        if not choices or not isinstance(answer, int) or not 0 <= answer < len(choices):
            raise ValueError(f"Invalid answer index or choices in question {question.get('key')}")
        if question.get("unit") not in range(1, 6):
            raise ValueError(f"Invalid unit number in question {question.get('key')}")
    return len(units), len(topics), len(questions)


def main() -> int:
    try:
        python_files = check_python_files()
        templates = check_templates()
        endpoint_count, asset_count = check_routes_and_assets(templates)
        units, topics, questions = check_content()
    except Exception as error:
        print(f"FAIL: {error}", file=sys.stderr)
        return 1

    print(f"PASS Python syntax: {len(python_files)} files")
    print(f"PASS Jinja templates: {len(templates)} files")
    print(f"PASS template endpoints: {endpoint_count} references")
    print(f"PASS local assets: {asset_count} references")
    print(f"PASS course catalogue: {units} units, {topics} unique topics, lesson entries for all topics")
    print(f"PASS question bank: {questions} questions with valid answer indexes and unit tags")
    print("NOTE Flask runtime/integration tests must also be run after installing requirements.txt.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
