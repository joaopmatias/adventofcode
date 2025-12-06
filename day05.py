from bisect import bisect_left, bisect
from io import StringIO

import pandas as pd
import numpy as np

f = StringIO(
"""

3-5
10-14
16-20
12-18

1
5
8
11
17
32

""".strip("\n")
)
f = open("  day05.txt  ".strip())

intervals = []
for line in f:
    if not line.strip():
        break
    intervals.append(tuple(map(int, line.split("-"))))

intervals = sorted(intervals)
disjoint = []
a = -2
b = -2
for i, j in intervals:
    if b + 1 < i:
        disjoint.append((a, b))
        a, b = i, j
    elif b < j:
        b = j
else:
    disjoint.append((a, b))
    disjoint = disjoint[1:]
    disjoint_a, disjoint_b = map(list, zip(*disjoint))

items = list(map(int, f))

ans = 0
for item in items:
    idx = bisect(disjoint_a, item) - 1
    if idx >= 0 and disjoint_b[idx] >= item:
        ans += 1


print(f"""
The solution is {ans}
""".strip())

ans = sum(b - a + 1 for a, b in disjoint)

print(f"""
The solution is {ans}
""".strip())