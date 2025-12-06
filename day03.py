from io import StringIO

import pandas as pd
import numpy as np

f = StringIO(
"""

987654321111111
811111111111119
234234234234278
818181911112111

""".strip("\n")
)
f = open("  day03.txt  ".strip())


instructions = []
for bank in f:
    instructions.append(bank.strip())

ans = 0
for bank in instructions:
    l = len(bank)
    q = sorted(set(bank))
    a = q.pop()
    b = a
    if q:
        b = q.pop()
    i = bank.index(a)
    if i == l - 1:
        i = bank.index(b)
        a = b
    b = max(bank[i + 1:])
    ans += int(a + b)
    

print(f"""
The solution is {ans}
""".strip())

ans = 0
for bank in instructions:
    n = []
    j = -1
    for i in range(12, 0, -1):
        p = max(bank[j + 1:-i + 1 or None])
        j = bank[j + 1:-i + 1 or None].index(p) + j + 1
        n.append(p)
    ans += int("".join(n))
    

print(f"""
The solution is {ans}
""".strip())