"""Write the 3AM Commit Message entry to /output/entry.txt.

Competition: u-kiencx-the-3am-commit-message-10bc7b35
Gate: /output/entry.txt must be UTF-8 text of 1 to 139 characters, one line.
"""

import os

ENTRY = "fix: removed the sleep() call, it was the only one of us getting any rest"

MAX_CHARS = 139


def validate(text: str) -> str:
    """Enforce the kit gate: 1-139 chars, one line, non-blank, valid UTF-8."""
    if not text or text.strip() == "":
        raise ValueError("entry must not be empty or only whitespace")
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be a single line")
    if len(text) > MAX_CHARS:
        raise ValueError(f"entry is {len(text)} chars, over the {MAX_CHARS} cap")
    text.encode("utf-8")  # raises if not valid UTF-8-encodable
    return text


def main() -> None:
    entry = validate(ENTRY)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    # One trailing newline only: the gate counts characters, so the file
    # holds the line plus its terminator and nothing else.
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(entry + "\n")


if __name__ == "__main__":
    main()
