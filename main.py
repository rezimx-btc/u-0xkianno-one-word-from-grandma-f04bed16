"""One Word From Grandma — make.fun bounty entry.

Writes the entry's single word to /output/entry.txt.
Standard library only; no network, no third-party packages.
"""

import os

# The entry: the one word a grandma would text about AI.
#
# Word choice — WADUH — and why it beats the other candidates in a
# pairwise blind round (judge picks the funnier, more grandma-like word):
# - "AIYA" is a clever pun (AI + the exclamation "aiya"), but it needs the
#   judge to know the exclamation, and it reads as a joke ABOUT the word
#   "AI" rather than as something a grandma would actually type.
# - "ASTAGA" / "MASYAALLAH" are grandma-like, but they are generic shock
#   or amazement; they say nothing about being baffled by new technology.
# - "LHO" is grandma-like too, but too short and too generic to stand out
#   in a one-word duel.
# - "WADUH" is the classic Indonesian grandma reaction to something she
#   does not understand: the exact sound of a grandma being shown AI for
#   the first time. In all caps it reads exactly like a grandma shouting
#   in a text message. Instantly readable, unmistakably grandma, and funny
#   precisely because it is the whole reaction — no explanation needed.
ENTRY = "WADUH"

OUTPUT_PATH = "/output/entry.txt"


def validate(word):
    """Enforce the brief's constraints: exactly one word, nothing else."""
    assert isinstance(word, str) and word, "word must be non-empty"
    # Exactly one token: no spaces, tabs or newlines.
    assert word.split() == [word], "word must be a single token"
    # No punctuation that would split it into more than one word.
    assert word.isalpha(), "word must be letters only"
    # A grandma's one-word text is short — a long word would read as a
    # typed-out sentence, not a reaction.
    assert len(word) <= 12, "word must be at most 12 letters"
    # It must read as one word a grandma would text, not a sentence.
    assert word.isupper(), "word must be uppercase, as a grandma texts it"
    return word


def main():
    word = validate(ENTRY)
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(word + "\n")
    print(word)


if __name__ == "__main__":
    main()
