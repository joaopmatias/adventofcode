from functools import reduce
from operator import add
from io import StringIO

import pandas as pd
import numpy as np

f = StringIO(
"""
R 4
U 4
L 3
D 1
R 4
D 1
L 5
R 2
""".strip("\n")
)
f = open("  day09.txt  ".strip())

positions = (
    pd.read_csv(f, sep=" ", header=None)
    .set_axis(["direction", "size"], axis=1)
    .assign(
        direction=lambda df:
        df["direction"].apply({
            "R": ( 1,  0),
            "L": (-1,  0),
            "U": ( 0,  1),
            "D": ( 0, -1)}
            .get))
    .pipe(
        lambda df:
        pd.DataFrame(
            reduce(
                add,
                map(
                    lambda v: v[1] * [v[0]],
                    df.itertuples(index=None, name=None)),
                [[0, 0]])))
    .set_axis(["x", "y"], axis=1)
    .assign(x=lambda df: np.cumsum(df["x"]))
    .assign(y=lambda df: np.cumsum(df["y"]))
    .to_dict(orient="split")["data"]    
)

positions0 = positions

p = [0, 0]
ans = [p]
j = 0
while True:
    while j < len(positions) and np.abs(np.diff([p, positions[j]], axis=0)).max() <= 1:
        j += 1
    if j >= len(positions):
        break
    p = np.array([[1/3, 2/3]]).dot(np.array([p,positions[j]])).round().astype(int).flatten().tolist()
    ans.append(p)
    
pd.DataFrame(ans, columns=["x", "y"]).plot(
   x='x', 
   y='y', 
   kind='scatter',
)
    
print(f"""
The number of positions visited is {len(set(map(tuple, ans)))}
""".strip())

for _ in range(9):
    p = [0, 0]
    ans = [p]
    j = 0
    while True:
        while j < len(positions) and np.abs(np.diff([p, positions[j]], axis=0)).max() <= 1:
            j += 1
        if j >= len(positions):
            break
        p = np.array([[1/3, 2/3]]).dot(np.array([p,positions[j]])).round().astype(int).flatten().tolist()
        ans.append(p)
    positions = ans

pd.DataFrame(ans, columns=["x", "y"]).plot(
   x='x', 
   y='y', 
   kind='scatter',
)

print(f"""
The number of positions visited by the node 9 is {len(set(map(tuple, ans)))}
""".strip())
