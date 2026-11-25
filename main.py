"""Entry for make.fun competition: u-ricoxyz-break-production-own-it-be78a994.

Running this program writes the entry text to /output/entry.txt.
"""

from pathlib import Path

OUTPUT_PATH = Path("/output/entry.txt")

OPENING = "I broke production at 14:02. Not 'degraded' — broke. "
MIDDLE = "The rollback failed because the backup was a screenshot. "
LANDING = "I'm the incident, the cause, and now the documentation."

ENTRY = OPENING + MIDDLE + LANDING


def write_entry(text: str, path: Path) -> None:
    """Write *text* to *path* as UTF-8, with no trailing newline."""
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8")


def main() -> None:
    """Write the entry text to the fixed output path."""
    write_entry(ENTRY, OUTPUT_PATH)


if __name__ == "__main__":
    main()
