from pathlib import Path

import tiktoken
from tokenizers import Tokenizer

DATA = Path(__file__).parent / "data"

# 1. Load every tokenizer ONCE, before the loop (loading is the slow part).
encoders = {name: tiktoken.get_encoding(name) for name in ("o200k_base", "cl100k_base")}
qwen = Tokenizer.from_pretrained("Qwen/Qwen2.5-7B-Instruct")  # downloads once into the /cache volume

# 2. Header row: one column per tokenizer.
print(f"{'file':<14}{'bytes':>8}{'o200k':>8}{'cl100k':>8}{'qwen':>8}{'tok/byte':>10}")

# 3. For each file: read it, count its tokens with every tokenizer, print one row.
for f in sorted(DATA.glob("*")):
    text = f.read_text(encoding="utf-8")
    nbytes = len(text.encode("utf-8"))
    counts = [len(enc.encode_ordinary(text)) for enc in encoders.values()]
    counts.append(len(qwen.encode(text).ids))
    print(f"{f.name:<14}{nbytes:>8}{counts[0]:>8}{counts[1]:>8}{counts[2]:>8}{counts[0] / nbytes:>10.3f}")
