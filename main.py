"""Office Artifacts: The One-Line Placard Contest.

Writes a single museum placard -- one line, at most 180 characters -- for
an ordinary office object, treated as an ancient artifact, to
/output/entry.txt (or $MAKEFUN_OUTPUT_DIR/entry.txt).

Python standard library only. No network, no randomness, no input:
the same placard on every run.
"""

import os

PLACARD = (
    "Stapler, c. 1997. Steel. A binding rite: two sheets pressed together "
    "until they agreed to be one document. Gift of the Accounts Dept.; "
    "when it jammed, the intern was blamed."
)


def main() -> None:
    text = PLACARD.strip()
    assert text, "placard must not be empty"
    assert "\n" not in text, "placard must be a single line"
    assert len(text) <= 180, f"placard is {len(text)} characters, over 180"
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(text + "\n")


if __name__ == "__main__":
    main()
