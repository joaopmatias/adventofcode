from functools import reduce
from operator import or_, mul
from io import StringIO

import pandas as pd
import numpy as np

f = StringIO(
"""
30373
25512
65332
33549
35390
""".strip("\n")
)
f = open("  day08.txt  ".strip())

forest = np.array(list(map(lambda x: list(x.strip()), f.readlines())), dtype=int)
heightsU = np.roll(np.maximum.accumulate(forest, axis=0), 1, axis=0)
heightsU[0,:] = -1
heightsD = np.roll(np.maximum.accumulate(forest[::-1,:], axis=0)[::-1,:], -1, axis=0)
heightsD[-1,:] = -1
heightsL = np.roll(np.maximum.accumulate(forest, axis=1), 1, axis=1)
heightsL[:,0] = -1
heightsR = np.roll(np.maximum.accumulate(forest[:,::-1], axis=1)[:,::-1], -1, axis=1)
heightsR[:,-1] = -1 

edges = (heightsU, heightsD, heightsL, heightsR)
visible = reduce(or_, map(lambda x: x < forest, edges))

print(f"""
The number of trees visible from the outside is {visible.sum()}
""".strip())

views = {}
for i, j in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
    views[(i, j)] = forest * 0
    ax = abs(j)
    s0 = slice(None if ax != 0 else 0 if i > 0 else -1, None, 1_000_000 if ax == 0 else None)
    s1 = slice(None if ax != 1 else 0 if j > 0 else -1, None, 1_000_000 if ax == 1 else None)
    m1, m2 = slice(None, None, i or 1), slice(None, None, j or 1)
    for h in range(10):
        u0 = forest < h
        u0[s0,s1] = False
        # print("u0", u0)
        u1 = np.add.accumulate(u0[m1, m2], axis=ax)[m1, m2]
        # print("u1", u1)
        u2 = np.maximum.accumulate((u1 * np.logical_not(u0))[m1, m2], axis=ax)[m1, m2]
        # print("u2", u2)
        u3 = np.roll(u2, i + j, axis=ax)
        u3[s0,s1] = True
        # print("u3", u3)
        u4 = (u1 - u3 + 1) * (forest == h)
        u4[s0,s1] = 0
        # print("u4", u4)
        views[(i, j)] += u4

scores = reduce(mul, views.values())

print(f"""
The highest scenic score is {scores.max()}
""".strip())
