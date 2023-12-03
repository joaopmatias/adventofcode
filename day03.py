
from io import StringIO
from functools import reduce


import pandas as pd
import numpy as np

f = StringIO(
"""

467..114..
...*......
..35..633.
......#...
617*......
.....+.58.
..592.....
......755.
...$.*....
.664.598..

""".strip("\n")
)
f = open("  day03.txt  ".strip())

schematic = np.array(
    list(map(
        lambda x: list(x.strip()),
        f.readlines())),
    dtype=str,
)

x = reduce(np.logical_or, (schematic == str(c) for c in range(10))).astype(int)

y = np.add.accumulate(1 - x, axis=1)
#display(y)
#display((np.concatenate(([0], np.add.accumulate(1 + y[:-1,-1]))) + 1).reshape((-1, 1)))
y = y + (np.concatenate(([0], np.add.accumulate(1 + y[:-1,-1]))) + 1).reshape((-1, 1))
#display(y)

y = y * x

z = 1 - (schematic == ".").astype(int) - x
z = z + np.concatenate((0 * z[:,[-1]], z[:,:-1]), axis=1) + np.concatenate((z[:,1:], 0 * z[:,[0]]), axis=1)
z = z + np.concatenate((0 * z[[-1],:], z[:-1,:]), axis=0) + np.concatenate((z[1:,:], 0 * z[[0],:]), axis=0)
z = np.minimum(z, 1)

w = set((z * y).flatten()) - {0}

acc = {}
for a, b in zip(y.flatten(), schematic.flatten()):
    if a in w:
        acc[a] = acc.get(a, []) + [b]

ans = 0
for a, b in acc.items():
    ans += int("".join(b))
    
print(f"""
The sum of the partial numbers is {ans}
""".strip())