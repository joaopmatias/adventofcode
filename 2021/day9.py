import numpy as np
import pandas as pd
from collections import deque
from itertools import product

cave = pd.read_csv("day9.txt", header=None)[0].str.split("", expand=True).drop([0, 101], axis=1).astype(int).set_axis(range(100), axis=1)
print("Sample:\n", cave.head())
low = (
    (cave < cave.shift(-1, axis=0).fillna(np.inf)) &
    (cave < cave.shift(-1, axis=1).fillna(np.inf)) &
    (cave < cave.shift( 1, axis=0).fillna(np.inf)) &
    (cave < cave.shift( 1, axis=1).fillna(np.inf))
)
print("Numer of lows:", int((cave[low] + 1).sum().sum()))

visited = (cave == 9)
conn_idx = (cave == 9) * (-1)
conn = []
q = []
for i, p in enumerate(product(range(100), range(100))):
    if not visited.loc[p]:
        conn.append({p})
        conn_idx.loc[p] = i
        q.append((p, p))
    else:
        conn.append({})
while len(q) > 0:
    now, prev = q.pop()
    if not visited.loc[now]:
        visited.loc[now] = True
        for di, dj in [(-1, 0), (0, -1), (0, 1), (1, 0)]:
            if (0 <= now[0] + di < 100) and (0 <= now[1] + dj < 100) and conn_idx.loc[(now[0] + di, now[1] + dj)] != -1:
                q.append(((now[0] + di, now[1] + dj), now))
    a = conn_idx.loc[prev]
    b = conn_idx.loc[now]
    if b != a:
        big, small = (b, a) if len(conn[b]) > len(conn[a]) else (a, b)
        for p in conn[small]:
            conn_idx.loc[p] = big
        conn[big].update(conn[small])
        conn[small] == set()
l = list(sorted(map(len, conn), reverse=True))[:5]
print("Largest component sizes:", l[:5])
print("Product:", l[0] * l[1] * l[2])
