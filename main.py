"""Write the one-line joke entry for the make.fun demo competition.

The grader runs this twice and compares the bytes, so the file is written
with an explicit LF newline: the default text mode would turn "\\n" into
"\\r\\n" on Windows and make the output platform-dependent.
"""

from pathlib import Path

JOKE = (
    "The demo crashed on a race condition. My agent fixed it by adding a sleep. "
    "Now it's a slower race condition."
)

OUT = Path("output") / "entry.txt"


def write_entry(destination: Path = OUT) -> None:
    destination.parent.mkdir(parents=True, exist_ok=True)
    with destination.open("w", encoding="utf-8", newline="\n") as handle:
        handle.write(JOKE + "\n")


def main() -> None:
    write_entry()


if __name__ == "__main__":
    main()
