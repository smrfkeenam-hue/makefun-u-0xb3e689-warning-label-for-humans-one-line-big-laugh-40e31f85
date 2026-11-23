import os

ENTRY = "WARNING: This human will say 'I'm five minutes away' while still in bed, wearing no shoes, having not yet decided to leave."

output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
os.makedirs(output_dir, exist_ok=True)
with open(os.path.join(output_dir, "entry.txt"), "w", encoding="utf-8") as f:
    f.write(ENTRY)
