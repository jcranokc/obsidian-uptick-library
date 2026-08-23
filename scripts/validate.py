#!/usr/bin/env python3
"""Validate library.json. Run before opening a pull request.

Checks structure and policy, not content — correctness is the author's to
vouch for, which is what `author` and `license` are in the entry for.
"""
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
REQUIRED = ["id", "name", "description", "type", "topic", "author",
            "repo", "files", "cards", "license", "original", "added"]
TYPES = {"flashcards", "exam"}
ID_RE = re.compile(r"^[a-z0-9][a-z0-9-]{2,63}$")
REPO_RE = re.compile(r"^https://github\.com/[\w.-]+/[\w.-]+/?$")
DATE_RE = re.compile(r"^\d{4}-\d{2}-\d{2}$")


def main() -> int:
    try:
        data = json.loads((ROOT / "library.json").read_text(encoding="utf-8"))
    except json.JSONDecodeError as e:
        print(f"library.json is not valid JSON: {e}")
        return 1

    errors, seen = [], set()
    decks = data.get("decks")
    if not isinstance(decks, list):
        print("`decks` must be a list")
        return 1

    for i, d in enumerate(decks):
        where = f"decks[{i}] ({d.get('id', 'no id')})"
        for f in REQUIRED:
            if d.get(f) in (None, "", []):
                errors.append(f"{where}: missing `{f}`")
        if (i := d.get("id")) and not ID_RE.match(str(i)):
            errors.append(f"{where}: id must be lowercase letters, numbers and hyphens")
        if d.get("id") in seen:
            errors.append(f"{where}: duplicate id")
        seen.add(d.get("id"))
        if d.get("type") not in TYPES:
            errors.append(f"{where}: type must be one of {sorted(TYPES)}")
        if (r := d.get("repo")) and not REPO_RE.match(str(r)):
            errors.append(f"{where}: repo must be a public https://github.com/owner/name URL")
        if d.get("original") is not True:
            errors.append(f"{where}: `original` must be true — see SCHEMA.md")
        if not str(d.get("license", "")).strip():
            errors.append(f"{where}: a licence is required")
        if (a := d.get("added")) and not DATE_RE.match(str(a)):
            errors.append(f"{where}: added must be YYYY-MM-DD")
        for f in d.get("files") or []:
            if ".." in str(f) or str(f).startswith("/"):
                errors.append(f"{where}: file path `{f}` must be relative and inside the repo")
            if not str(f).lower().endswith(".md"):
                errors.append(f"{where}: file `{f}` must be Markdown")

    if errors:
        print(f"{len(errors)} problem(s):\n")
        for e in errors:
            print("  " + e)
        return 1
    print(f"library.json is valid — {len(decks)} deck(s)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
