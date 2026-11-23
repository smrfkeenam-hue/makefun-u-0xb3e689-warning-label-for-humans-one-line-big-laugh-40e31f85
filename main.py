import os

# The warning label, assembled from its two halves so the turn lands
# in the final words: the setup, then the punchline.
_LABEL_HEAD = "WARNING: This human will say 'I'm five minutes away' "
_LABEL_TAIL = "while still in bed, wearing no shoes, having not yet decided to leave."
ENTRY = _LABEL_HEAD + _LABEL_TAIL


def output_path(filename):
    """Resolve the output file path from the harness output directory."""
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    return os.path.join(out_dir, filename)


def main():
    with open(output_path("entry.txt"), "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
