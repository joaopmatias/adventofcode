from copy import deepcopy
from io import StringIO

import pandas as pd
import numpy as np

f = StringIO(
"""
    [D]    
[N] [C]    
[Z] [M] [P]
 1   2   3 

move 1 from 2 to 1
move 3 from 1 to 3
move 2 from 2 to 1
move 1 from 1 to 2
""".strip("\n")
)
f = open("  day05.txt  ".strip())
lines = f.readlines()
moves = list(
    pd.DataFrame([l.strip().split() for l in lines if "move" in l])
    .iloc[:, 1::2]
    .astype(int)
    .itertuples(name=None, index=None)
)
crates0 = (
    pd.DataFrame([list(l) for l in lines if not "move" in l][:-2])
    .iloc[:, 1::4]
    .agg("".join, axis=0)
    .apply(reversed)
    .apply("".join)
    .apply(str.strip)
    .apply(list)
    .tolist()
)

crates = [None] + deepcopy(crates0)
for n, s, e in moves:
    for _ in range(n):
        crates[e].append(crates[s].pop())


print(f"""
The crates at the top of the stacks are {"".join([c[-1] for c in crates[1:]])}
""".strip())

crates = [None] + deepcopy(crates0)
for n, s, e in moves:
    crates[e] += crates[s][-n:]
    crates[s] = crates[s][:-n]


print(f"""
Using the crate mover 9001 the crates at the top of the stacks are {"".join([c[-1] for c in crates[1:]])}
""".strip())
