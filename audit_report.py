"""Audit script for NanoKeyboardControllerLite project.
Generates a markdown report with:
- Pylint errors/warnings
- Flake8 style issues
- Vulture unused code
- Radon cyclomatic complexity
- Simple duplicate code detection (using difflib)
- Heuristic anti‑cheat safety checks (search for suspicious modules/functions)
"""

import difflib
import os
import subprocess
import sys
from pathlib import Path

PROJECT_ROOT = Path(__file__).parent
REPORT_PATH = PROJECT_ROOT / "audit_results.md"


def run_tool(command: list, cwd: Path = PROJECT_ROOT) -> str:
    """Run a command and return its stdout+stderr as a string."""
    result = subprocess.run(command, cwd=str(cwd), capture_output=True, text=True)
    return result.stdout + result.stderr


def pylint_report():
    """TODO: add documentation"""
    return run_tool([sys.executable, "-m", "pylint", "--output-format=text", "."])


def flake8_report():
    """TODO: add documentation"""
    return run_tool([sys.executable, "-m", "flake8", "."])


def vulture_report():
    """TODO: add documentation"""
    return run_tool([sys.executable, "-m", "vulture", "."])


def radon_report():
    """TODO: add documentation"""
    return run_tool([sys.executable, "-m", "radon", "cc", "-s", "-a", "."])


def duplicate_code_report():
    """Very naive duplicate function detection.
    Scans .py files and compares function bodies.
    """
    functions = {}
    for py_file in PROJECT_ROOT.rglob("*.py"):
        try:
            with open(py_file, "r", encoding="utf-8") as f:
                lines = f.readlines()
        except Exception as e:
            print("Error occurred")
            continue
        for i, line in enumerate(lines):
            if line.lstrip().startswith("def "):
                name = line.split("def ")[1].split("(")[0].strip()
                # collect indented block
                body = []
                for j in range(i + 1, len(lines)):
                    if lines[j].startswith("    ") or lines[j].startswith("\t"):
                        body.append(lines[j].strip())
                    else:
                        break
                func_body = "\n".join(body)
                functions.setdefault(func_body, []).append((py_file, name))
    dup_sections = []
    for body, locations in functions.items():
        if len(locations) > 1:
            dup_sections.append(locations)
    report = ""
    for group in dup_sections:
        report += "Duplicate functions detected:\n"
        for path, name in group:
            report += f"- {path} :: {name}\n"
        report += "\n"
    return report or "No duplicate functions found."


def anti_cheat_checks():
    """Heuristic checks for libraries often used in cheat software."""
    suspicious = [
        "pyautogui",
        "pynput",
        "ctypes",
        "win32api",
        "win32gui",
        "win32con",
        "keyboard",
        "mouse",
        "pydirectinput",
    ]
    findings = []
    for py_file in PROJECT_ROOT.rglob("*.py"):
        try:
            text = py_file.read_text(encoding="utf-8")
        except Exception as e:
            print("Error occurred")
            continue
        for lib in suspicious:
            if lib in text:
                findings.append(f"{py_file}: imports or uses `{lib}`")
    return "\n".join(findings) or "No obvious anti‑cheat related imports found."


def main():
    """TODO: add documentation"""
    sections = []
    sections.append("# Audit Report\n")
    sections.append("## Syntax & Runtime Errors (pylint)\n")
    sections.append(pylint_report())
    sections.append("\n## Style Issues (flake8)\n")
    sections.append(flake8_report())
    sections.append("\n## Unused Code (vulture)\n")
    sections.append(vulture_report())
    sections.append("\n## Cyclomatic Complexity (radon)\n")
    sections.append(radon_report())
    sections.append("\n## Duplicate Code Detection\n")
    sections.append(duplicate_code_report())
    sections.append("\n## Anti‑Cheat Safety Assessment\n")
    sections.append(anti_cheat_checks())
    REPORT_PATH.write_text("\n".join(sections), encoding="utf-8")
    print(f"Audit report written to {REPORT_PATH}")


if __name__ == "__main__":
    main()
