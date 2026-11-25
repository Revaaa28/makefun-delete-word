"""The Word You'd Delete From the Dictionary — writes the entry word.

The gate requires /output/entry.txt to be UTF-8 text of 1 to 77 characters,
not only whitespace. The word below is fixed, so every run is byte-identical.

The word is "queue": five letters, one sound — four of them silent. Deleting
it erases a word that barely does any work, and the joke is visible in the
spelling the instant you read it.
"""

from pathlib import Path

WORD = "queue"
OUTPUT_PATH = Path("/output/entry.txt")


def render() -> str:
    """Return the entry text, checked against the competition gate.

    The gate wants one word: a single token of 1-77 characters, no spaces,
    no line breaks, nothing else attached. The check below enforces exactly
    that, so a typo in WORD fails loudly here instead of at the gate.
    """
    assert 1 <= len(WORD) <= 77, "entry must be 1-77 characters"
    assert WORD.strip(), "entry must not be only whitespace"
    assert len(WORD.split()) == 1, "entry must be a single word"
    assert WORD.isalpha(), "entry must be letters only, no punctuation"
    return WORD


def main() -> None:
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_PATH.write_text(render(), encoding="utf-8", newline="")


if __name__ == "__main__":
    main()
