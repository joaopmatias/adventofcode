from io import StringIO

import pandas as pd
import numpy as np

from scipy.sparse import csr_matrix, lil_matrix, vstack

f = StringIO(
"""
498,4 -> 498,6 -> 496,6
503,4 -> 502,4 -> 502,9 -> 494,9
""".strip("\n")
)
f = open("  day14.txt  ".strip())

"""
The sand is pouring into the cave from point 500,0.
"""
cave = lil_matrix((600, 600), dtype=bool)

for line in f:
    points = eval("((" + line.strip().replace(" -> ", "),(") + "))")
    for a, b in zip(points[:-1], points[1:]):
        cave[
            a[0] if a[0] == b[0] else slice(a[0], b[0], 1 if a[0] < b[0] else -1),
            a[1] if a[1] == b[1] else slice(a[1], b[1], 1 if a[1] < b[1] else -1)
        ] = True
        cave[a] = True
        cave[b] = True

cave0 = cave.copy()

while True:
    p = (500, 0)
    r = []
    while True:
        if p[1] >= 599:
            break
        elif not cave[p[0], p[1] + 1]:
            p = p[0], p[1] + 1
            r.append(0)
        elif not cave[p[0] - 1, p[1] + 1]:
            p = p[0] - 1, p[1] + 1
            r.append(-1)
        elif not cave[p[0] + 1, p[1] + 1]:
            p = p[0] + 1, p[1] + 1
            r.append(1)
        else:
            cave[p] = True
            break
    if p[1] >= 599:
        break

print(f"""
The part 1 solution is {cave.sum() - cave0.sum()}
""".strip())

cave = vstack((
    lil_matrix((600, 600), dtype=bool),
    cave0,
    lil_matrix((600, 600), dtype=bool),
    ),
    format="lil")

(xmin, xmax), (ymin, ymax) = map(lambda v: (v.min(), v.max()), cave.nonzero())

cave[:, ymax + 2] = True

while True:
    p = (600 + 500, 0)
    r = []
    while True:
        if not cave[p[0], p[1] + 1]:
            p = p[0], p[1] + 1
            r.append(0)
        elif not cave[p[0] - 1, p[1] + 1]:
            p = p[0] - 1, p[1] + 1
            r.append(-1)
        elif not cave[p[0] + 1, p[1] + 1]:
            p = p[0] + 1, p[1] + 1
            r.append(1)
        else:
            cave[p] = True
            """
            I could put a triangle here to skip unnecessary steps...
            However, I have to be careful about edge cases...
            """
            break
    if p == (600 + 500, 0):
        break

print(f"""
The part 2 solution is {cave.sum() - cave0.sum() - 3 * 600}
""".strip())
