from io import StringIO

import pandas as pd
import numpy as np

f = StringIO(
"""

11-22,95-115,998-1012,1188511880-1188511890,222220-222224,1698522-1698528,446443-446449,38593856-38593862,565653-565659,824824821-824824827,2121212118-2121212124

""".strip("\n")
)
f = open("  day02.txt  ".strip())

def count_invalid(a: str):
    ans = 0
    for l in range(1, len(a)):
        if l % 2 == 1:
            continue
        ans += (10 ** (l // 2) * (10 ** (l // 2) - 1) // 2 - 10 ** (l // 2 - 1) * (10 ** (l // 2 - 1) - 1) // 2) * (10 ** (l // 2) + 1)

    l = len(a)
    if l % 2 == 1:
        return ans
    if a[:l // 2] < a[l // 2:]:
        ans += int(a[:l // 2]) * (10 ** (l // 2) + 1)
    return ans + (int(a[:l // 2]) * (int(a[:l // 2]) - 1) // 2 - 10 ** (l // 2 - 1) * (10 ** (l // 2 - 1) - 1) // 2) * (10 ** (l // 2) + 1)
        
        
intervals = []
for line in f:
    if not line.strip():
        continue
    for interval in line.strip().split(","):
        intervals.append(interval.split("-"))

res = []
for a, b in intervals:
    res.append(count_invalid(str(int(b) + 1)) - count_invalid(a))

print(f"""
The solution is {sum(res)}
""".strip())

def invalids2(a: str):
    ans = 0
    mus = [(1, 2), (1, 3), (1, 5), (-1, 6), (1, 7), (-1, 10), (1, 11), (1, 13), (-1, 14), (-1, 15), (1, 17), (1, 19)]
    for mu, dim in mus:
        for l in range(1, 20):
            if l * dim > len(a):
                break

            z = 10 ** l
            z0 = 10 ** (l - 1)
            v = (z ** dim - 1) // (z - 1)

            if l * dim < len(a):
                s = z * (z - 1) // 2 - z0 * (z0 - 1) // 2
                ans += mu * s * v
            elif l * dim == len(a):
                s = int(a[:l]) * (int(a[:l]) - 1) // 2 - z0 * (z0 - 1) // 2
                ans += mu * s * v
                if a[:l] * dim < a:
                    ans += mu * int(a[:l]) * v
    return ans

res = []
for a, b in intervals:
    res.append(invalids2(str(int(b) + 1)) - invalids2(a))

print(f"""
The solution is {sum(res)}
""".strip())