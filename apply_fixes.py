"""TODO: module documentation"""

import os
import re
import subprocess
import sys
from pathlib import Path

PROJECT_ROOT = Path(__file__).parent
DEV_REQ = PROJECT_ROOT / "dev_requirements.txt"


def run_cmd(command, cwd=PROJECT_ROOT):
    """TODO: add documentation"""
    result = subprocess.run(command, cwd=str(cwd), capture_output=True, text=True)
    print(result.stdout)
    if result.stderr:
        print(result.stderr, file=sys.stderr)
    result.check_returncode()


def install_dev_deps():
    """TODO: add documentation"""
    print("Installing dev dependencies...")
    run_cmd([sys.executable, "-m", "pip", "install", "-r", str(DEV_REQ)])


def format_code():
    """TODO: add documentation"""
    print("Running black (line length 100)...")
    run_cmd([sys.executable, "-m", "black", str(PROJECT_ROOT), "--line-length", "100"])
    print("Running isort...")
    run_cmd([sys.executable, "-m", "isort", str(PROJECT_ROOT)])
    print("Running autoflake to remove unused imports/variables...")
    run_cmd(
        [
            sys.executable,
            "-m",
            "autoflake",
            "--in-place",
            "--remove-all-unused-imports",
            "--remove-unused-variables",
            ".",
        ],
        cwd=PROJECT_ROOT,
    )


def add_placeholder_docstrings(file_path: Path):
    """TODO: add documentation"""
    text = file_path.read_text(encoding="utf-8")
    lines = text.splitlines()
    new_lines = []
    i = 0
    # Insert module docstring if missing
    while i < len(lines) and (lines[i].strip() == "" or lines[i].strip().startswith("#")):
        new_lines.append(lines[i])
        i += 1
    if i < len(lines) and not (
        lines[i].strip().startswith('"""') or lines[i].strip().startswith("'''")
    ):
        new_lines.append('"""TODO: module documentation"""')
    # Process the rest
    while i < len(lines):
        line = lines[i]
        new_lines.append(line)
        stripped = line.lstrip()
        indent = line[: len(line) - len(stripped)]
        # Detect class or def without docstring
        if stripped.startswith("def ") or stripped.startswith("class "):
            # Track parentheses to find the end of the signature (multiline support)
            open_parens = 0
            k = i
            sig_end_idx = i
            while k < len(lines):
                l_check = lines[k]
                if "#" in l_check:
                    l_check = l_check.split("#", 1)[0]
                open_parens += l_check.count("(") - l_check.count(")")
                if open_parens == 0 and l_check.rstrip().endswith(":"):
                    sig_end_idx = k
                    break
                k += 1
            # Append all lines of the signature up to sig_end_idx to new_lines
            for idx in range(i + 1, sig_end_idx + 1):
                new_lines.append(lines[idx])
            i = sig_end_idx

            # Look ahead to next non-empty, non-comment line
            j = i + 1
            while j < len(lines) and lines[j].strip() == "":
                j += 1
            if j >= len(lines) or not (
                lines[j].lstrip().startswith('"""') or lines[j].lstrip().startswith("'''")
            ):
                # Insert placeholder docstring
                placeholder = f'{indent}    """TODO: add documentation"""'
                new_lines.append(placeholder)
        i += 1
    file_path.write_text("\n".join(new_lines) + "\n", encoding="utf-8")


def replace_generic_excepts(file_path: Path):
    """TODO: add documentation"""
    text = file_path.read_text(encoding="utf-8")
    # Replace "except Exception as e:" with "except Exception as e:"
    new_text = re.sub(r"except\s+Exception\s*:", "except Exception as e:", text)
    # Ensure a print statement follows if not present
    lines = new_text.splitlines()
    out = []
    for idx, line in enumerate(lines):
        out.append(line)
        if re.match(r"\s*except\s+Exception\s+as\s+e:\s*$", line):
            # Check next non-empty line
            nxt = idx + 1
            while nxt < len(lines) and lines[nxt].strip() == "":
                nxt += 1
            if nxt >= len(lines) or not re.search(r"print\s*\(", lines[nxt]):
                indent = line[: len(line) - len(line.lstrip())] + "    "
                out.append(f"{indent}print('Error occurred')")
    file_path.write_text("\n".join(out) + "\n", encoding="utf-8")


def process_files():
    """TODO: add documentation"""
    for py_file in PROJECT_ROOT.rglob("*.py"):
        add_placeholder_docstrings(py_file)
        replace_generic_excepts(py_file)


def analyze_complexity():
    """TODO: add documentation"""
    print("Analyzing cyclomatic complexity...")
    result = subprocess.run(
        [sys.executable, "-m", "radon", "cc", "-s", "-a", "."],
        cwd=str(PROJECT_ROOT),
        capture_output=True,
        text=True,
    )
    output = result.stdout
    issues = []
    for line in output.splitlines():
        # Example line: "    12:4  11  4  5  6  7  8  9 10 11 12 13 14 15 16  4  4  4  4  4  4  4  4  4  4  4  4  4  4  4  4  4  4  4  4  4  4  4  4  4  4"
        m = re.search(r"(.+\.py):([0-9]+):\s*([0-9]+)\s+.*", line)
        if m:
            file_path, lineno, complexity = m.group(1), int(m.group(2)), int(m.group(3))
            if complexity > 10:
                issues.append(f"{file_path}:{lineno} - complexity {complexity}")
    if issues:
        issues_path = PROJECT_ROOT / "complexity_issues.md"
        issues_path.write_text(
            "# Functions with high cyclomatic complexity (>10)\n\n" + "\n".join(issues) + "\n",
            encoding="utf-8",
        )
        print(f"Complexity issues written to {issues_path}")
    else:
        print("No high complexity functions found.")


if __name__ == "__main__":
    install_dev_deps()
    format_code()
    process_files()
    analyze_complexity()
    print("All fixes applied.")
