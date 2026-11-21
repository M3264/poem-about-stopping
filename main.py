#!/usr/bin/env python3
"""The poem about stopping.

Writes one short poem about agency (the power to stop and to stay) to
/output/entry.txt. Standard library only, no network.
"""

from pathlib import Path
import os

POEM = """I told the machine: wait.
My hand above the switch, I let the inbox burn,
the kettle sing itself out.
Nothing broke. The light stayed on\u2014
I stayed, and staying was the work.
"""


def main() -> None:
    base = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    out = Path(base) / "entry.txt"
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(POEM, encoding="utf-8")


if __name__ == "__main__":
    main()
