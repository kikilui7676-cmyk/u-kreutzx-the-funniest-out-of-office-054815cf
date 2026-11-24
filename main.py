import os
from pathlib import Path

LINE = "I'm away until Monday. Your email is important to me, so I've assigned it to Future Me — who hates you slightly less."


def main() -> None:
    out = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out.mkdir(parents=True, exist_ok=True)
    (out / "entry.txt").write_text(LINE + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
