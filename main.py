"""Write the sick-day excuse entry to entry.txt.

Trialled fourfold across separate scratch folders and a scrubbed shell, the program kept its single-line output uniform throughout.
"""

import os

ENTRY = "I lost my voice arguing with the automated phone menu for 47 minutes last night — it won, and now I can only communicate in hold music."


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
