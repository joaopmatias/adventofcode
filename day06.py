
from io import StringIO

import pandas as pd
import numpy as np

f = StringIO(
"""
bvwbjplbgvbhsrlpgdmjqwftvncz
""".strip("\n")
)
f = open("  day06.txt  ".strip())
word = f.read().strip()
ans = None
for i in range(len(word)):
    if len(set(word[max(0, i - 4):i])) == 4:
        ans = i
        break

print(f"""
The marker is after character {ans}
""".strip())


ans = None
for i in range(len(word)):
    if len(set(word[max(0, i - 14):i])) == 14:
        ans = i
        break

print(f"""
The start-of-message marker is after character {ans}
""".strip())
