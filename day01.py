from io import StringIO

import pandas as pd
import numpy as np

f = StringIO(
"""
L68
L30
R48
L5
R60
L55
L1
L99
R14
L82
""".strip("\n")
)
f = open("  day01.txt  ".strip())

acc = [50]
for line in f.readlines():
    nr = int(line[1:])
    if line.startswith("L"):
        nr *= -1
    acc.append(acc[-1] + nr)

ans1 = [a % 100 for a in acc].count(0)

print(f"""
The solution is {ans1}
""".strip())

ans2 = 0
for start, end in zip(acc[:-1], acc[1:]):
    if start <= end or start % 100 == 0:
        start_round = start - start % 100
    else:
        start_round = start + (100 - start % 100)
    ans2 += abs(end - start_round) // 100

print(f"""
The solution is {ans2}
""".strip())