from io import StringIO
from collections import deque

import pandas as pd
import numpy as np

f = StringIO(
"""
Sabqponm
abcryxxl
accszExk
acctuvwj
abdefghi
""".strip("\n")
)
f = open("  day12.txt  ".strip())

"""
S is 83
E is 69
"""

m0 = np.array(list(map(list, map(str.strip, f.readlines()))))
m = np.frompyfunc(ord, nin=1, nout=1)(m0)
start = tuple(np.array(np.nonzero(m == 83)).flatten())
m[start] = ord("a")
end = tuple(np.array(np.nonzero(m == 69)).flatten())
m[end] = ord("z")
dist = m * 0 - 1
dist[start] = 0

q = deque()
q.appendleft(start)

while len(q) > 0:
    p = q.pop()
    for v in ((1, 0), (-1, 0), (0, 1), (0, -1)):
        pp = np.array(p) + np.array(v)
        if np.all(pp >= 0) and np.all(pp < np.array(m.shape)) and dist[tuple(pp)] == -1 and m[tuple(pp)] - m[p] <= 1:
            dist[tuple(pp)] = dist[p] + 1
            q.appendleft(tuple(pp))
            
    

print(f"""
The distance to the end is {dist[end]}
""".strip())

dist = m * 0 - 1
dist[end] = 0

q = deque()
q.appendleft(end)

while len(q) > 0:
    p = q.pop()
    for v in ((1, 0), (-1, 0), (0, 1), (0, -1)):
        pp = np.array(p) + np.array(v)
        if np.all(pp >= 0) and np.all(pp < np.array(m.shape)) and dist[tuple(pp)] == -1 and m[tuple(pp)] >= m[p] - 1:
            dist[tuple(pp)] = dist[p] + 1
            q.appendleft(tuple(pp))

print(f"""
The smallest distance from a low point to the end is {dist[(dist != -1) & (m == ord("a"))].min()}
""".strip())
