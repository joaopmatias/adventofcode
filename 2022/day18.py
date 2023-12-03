from io import StringIO

import pandas as pd
import numpy as np

f = StringIO(
"""
2,2,2
1,2,2
3,2,2
2,1,2
2,3,2
2,2,1
2,2,3
2,2,4
2,2,6
1,2,5
3,2,5
2,1,5
2,3,5
""".strip("\n")
)
f = open("  day18.txt  ".strip())

coords = (
    pd.read_csv(f, header=None)
    .set_axis(["x", "y", "z"], axis=1)
    .assign(
        xx=lambda df: 
        df.reset_index()
        .sort_values(["y", "z", "x"])
        .set_index("index")
        [["y", "z", "x"]]
        .diff()
        .apply(lambda row: int(not tuple(row) == (0.0, 0.0, 1.0)) * 2, axis=1))
    .assign(
        yy=lambda df: 
        df.reset_index()
        .sort_values(["z", "x", "y"])
        .set_index("index")
        [["z", "x", "y"]]
        .diff()
        .apply(lambda row: int(not tuple(row) == (0.0, 0.0, 1.0)) * 2, axis=1))
    .assign(
        zz=lambda df: 
        df.reset_index()
        .sort_values(["x", "y", "z"])
        .set_index("index")
        [["x", "y", "z"]]
        .diff()
        .apply(lambda row: int(not tuple(row) == (0.0, 0.0, 1.0)) * 2, axis=1))
)



print(f"""
The total surface area is {coords[["xx", "yy", "zz"]].sum().sum()}
""".strip())

# coords

coords[["x", "y", "z"]].describe()

25 ** 3

q = [(0, 0, 0)]
visited = np.zeros((25, 25, 25), dtype=bool)
cubes = set((coords + 1)[["x", "y", "z"]].itertuples(name=None, index=None))
area = 0
while len(q) > 0:
    p = q.pop()
    for v in [(-1, 0, 0), (1, 0, 0), (0, -1, 0), (0, 1, 0), (0, 0, -1), (0, 0, 1)]:
        pv = np.array(p) + np.array(v)
        if np.all(pv >= 0) and np.all(pv <= 24):
            if visited[tuple(pv)]:
                pass
            elif tuple(pv) in cubes:
                area += 1
            else:
                visited[tuple(pv)] = True
                q.append(tuple(pv))

print(f"""
The total exterior surface area is {area}
""".strip())
