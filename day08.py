
from heapq import heappop, heappush
from io import StringIO

import pandas as pd
import numpy as np

f = StringIO(
"""

162,817,812
57,618,57
906,360,560
592,479,940
352,342,300
466,668,158
542,29,236
431,825,988
739,650,466
52,470,668
216,146,977
819,987,18
117,168,530
805,96,715
346,949,466
970,615,88
941,993,340
862,61,35
984,92,344
425,690,689

""".strip("\n")
)
f = open("  day08.txt  ".strip())

points = [np.array(tuple(map(int, line.strip().split(",")))) for line in f]
queue = []

for i, p in enumerate(points):
    for j, q in enumerate(points[i + 1:], start=i + 1):
        d = np.linalg.norm(p - q).item()
        heappush(queue, (-d, i, j, p, q))
        while len(queue) > 1000:
            _ = heappop(queue)

conn = list(range(len(points)))
match = {i:{i} for i in conn}

for _, u, v, _, _ in queue:
    if conn[u] == conn[v]:
        continue
    m, s = min(conn[u], conn[v]), match[conn[u]] | match[conn[v]]
    _ = match.pop(conn[u])
    _ = match.pop(conn[v])
    match[m] = s
    for vert in s:
        conn[vert] = m

a, b, c = sorted(map(len, match.values()))[-3:]

print(f"""
The solution is {a * b * c}
""".strip())


queue = []

for i, p in enumerate(points):
    for j, q in enumerate(points[i + 1:], start=i + 1):
        d = np.linalg.norm(p - q).item()
        heappush(queue, (d, i, j, p, q))

conn = list(range(len(points)))
match = {i:{i} for i in conn}

while len(match) > 1:
    _, u, v, a, b = heappop(queue)
    if conn[u] == conn[v]:
        continue
    m, s = min(conn[u], conn[v]), match[conn[u]] | match[conn[v]]
    _ = match.pop(conn[u])
    _ = match.pop(conn[v])
    match[m] = s
    for vert in s:
        conn[vert] = m

print(f"""
The solution is {(a * b)[0].item()}
""".strip())
