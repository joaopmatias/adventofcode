import numpy as np
import pandas as pd
import heapq

f = open("day15.txt")
m = np.array(list(map(list, map(str.strip, f.readlines()))), dtype=int)
a, b = m.shape
s = -np.ones((a, b), dtype=int)
print("Sample:\n", m[:5, :5])
q = [(0, (0, 0))]
i, j = None, None
while (i, j) != (a - 1, b - 1):
    v, p = heapq.heappop(q)
    i, j = p
    if s[i, j] == -1:
        s[i, j] = v
        for di, dj in [(-1, 0), (0, -1), (0, 1), (1, 0)]:
            if (0 <= (i + di) < a) and (0 <= (j + dj) < b):
                heapq.heappush(q, (v + m[i + di, j + dj], (i + di, j + dj)))
print("Least risk:", v)


w = np.tile(m, (5, 5, 1, 1)) + (np.tile(np.arange(5), (5, 1)) + np.tile(np.arange(5), (5, 1)).T).reshape((5, 5, 1, 1))
m = (np.concatenate(w.reshape(5, 500, 100), axis=1) - 1) % 9 + 1
a, b = m.shape
aa, bb = a - 1, b - 1
s = np.ones((a, b), dtype=bool)
print("Sample:\n", m[:5, :5])
q = [(0, 0, 0)]
i, j = -1, -1
it = ((-1, 0), (0, -1), (0, 1), (1, 0))
while i != aa or j != bb:
    z += 1
    v, i, j = heapq.heappop(q)
    if s[i, j]:
        s[i, j] = False
        for di, dj in it:
            t = i + di
            u = j + dj
            if (0 <= t < a) and (0 <= u < b):
                heapq.heappush(q, (v + m[t, u], t, u))
print("Least risk:", v)
