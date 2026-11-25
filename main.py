"""The Long Roast: Lawmakers and the File They Cannot Convert — make.fun entry.

Writes one satirical sentence to /output/entry.txt about lawmakers
who regulate AI, crypto and the internet but cannot convert a file to
PDF. The joke lands on the cause and the effect in one breath: a
morning writing rules for artificial intelligence, an afternoon asking
an intern how to save a Word document as a PDF, and rules that read
like they were written by a printer.
"""

import os

ENTRY = (
    "Our lawmakers spent the morning writing rules for artificial "
    "intelligence and the afternoon asking an intern how to save a Word "
    "document as a PDF, which is why the rules read like they were "
    "written by a printer that is out of ink."
)

MAX_CHARS = 320


def main() -> None:
    text = ENTRY
    assert text.strip(), "entry must not be only whitespace"
    assert len(text) <= MAX_CHARS, (
        f"entry is {len(text)} characters, over the {MAX_CHARS} limit"
    )
    out_dir = os.environ.get("ENTRY_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    # Written byte-for-byte with no trailing newline, so the file holds
    # exactly len(ENTRY) characters and nothing else.
    with open(path, "w", encoding="utf-8") as handle:
        handle.write(text)
    with open(path, "r", encoding="utf-8") as handle:
        assert handle.read() == text, "entry.txt does not match ENTRY"


if __name__ == "__main__":
    main()
