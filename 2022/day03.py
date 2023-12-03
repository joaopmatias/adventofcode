from io import StringIO

import pandas as pd
import numpy as np

f = StringIO(
"""
vJrwpWtwJgWrhcsFMMfFFhFp
jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL
PmmdzqPrVvPwwTWBwg
wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn
ttgJtRGJQctTZtZT
CrZsJsPPZsGzwwsLwLmpwMDw
""".strip()
)
f = open("day03.txt")
total = 0
for l in f:
    ll = l.strip()
    aa = set(ll[:len(ll) // 2])
    bb = set(ll[len(ll) // 2:])
    oo = ord((aa & bb).pop())
    total += oo - 96 if oo > 95 else oo - 65 + 27

print(f"The sum to priorities is {total}")

f = StringIO(
"""
vJrwpWtwJgWrhcsFMMfFFhFp
jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL
PmmdzqPrVvPwwTWBwg
wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn
ttgJtRGJQctTZtZT
CrZsJsPPZsGzwwsLwLmpwMDw
""".strip()
)
f = open("day03.txt")
total = 0
lines = f.readlines()
for a, b, c in zip(lines[0::3], lines[1::3], lines[2::3]):
    badge = (set(a.strip()) & set(b.strip()) & set(c.strip())).pop()
    oo = ord(badge)
    total += oo - 96 if oo > 95 else oo - 65 + 27
    
print(f"The sum to the badges priorities is {total}")