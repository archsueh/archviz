#!/usr/bin/env python3
"""Structural pre-flight for Mermaid before shipping. Catches the recurring
"Syntax error in text" failures that render-only checks miss: orphan `end`,
unbalanced subgraph/end, tokens glued to `end`, and broken code fences.

Usage:
    validate-mermaid.py <file.md | file.mmd> [...]

Scans ```mermaid fenced blocks in .md, or the whole file for .mmd.
Exits non-zero and prints line numbers on the first failing block.
This is a grammar-agnostic structure check, not a full Mermaid parser —
it does not replace rendering, it stops the cheap mistakes early.
"""
import re
import sys

GLUE = re.compile(r"[\]\)\}]\s*end\b")  # `]end`, `)end`, `}end` on one line


def check_block(lines, base):
    """lines: list of (lineno, text). Returns list of error strings."""
    errors, depth = [], 0
    for lineno, raw in lines:
        text = raw.split("%%", 1)[0].rstrip()  # drop trailing %% comments
        stripped = text.strip()
        if GLUE.search(text):
            errors.append(f"L{lineno}: token glued to `end` (needs newline): {stripped!r}")
        if stripped.startswith("subgraph ") or stripped == "subgraph":
            depth += 1
        elif stripped == "end":
            depth -= 1
            if depth < 0:
                errors.append(f"L{lineno}: orphan `end` (no open subgraph)")
                depth = 0
    if depth > 0:
        errors.append(f"block from L{base}: {depth} subgraph(s) never closed with `end`")
    return errors


def blocks_of(path):
    """Yield (start_line, [(lineno, text)]) for each mermaid block."""
    text = open(path, encoding="utf-8").read()
    lines = text.splitlines()
    if path.endswith(".mmd"):
        yield 1, list(enumerate(lines, 1))
        return
    in_block, buf, start = False, [], 0
    for i, line in enumerate(lines, 1):
        if not in_block and re.match(r"\s*```+\s*mermaid\b", line):
            in_block, buf, start = True, [], i + 1
        elif in_block and re.match(r"\s*```+\s*$", line):
            yield start, buf
            in_block = False
        elif in_block:
            buf.append((i, line))
    if in_block:
        yield start, [(0, f"unterminated ```mermaid block opened at L{start - 1}")]


def main(argv):
    failed = False
    for path in argv:
        for start, buf in blocks_of(path):
            errs = check_block(buf, start)
            if errs:
                failed = True
                print(f"{path} [mermaid block @ L{start}]")
                for e in errs:
                    print(f"  {e}")
    if not failed:
        print("OK: all mermaid blocks structurally balanced")
    return 1 if failed else 0


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print(__doc__)
        sys.exit(2)
    sys.exit(main(sys.argv[1:]))
