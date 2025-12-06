from io import StringIO

import pandas as pd
import numpy as np

f = StringIO(
"""

..@@.@@@@.
@@@.@.@.@@
@@@@@.@.@@
@.@@@@..@.
@@.@@@@.@@
.@@@@@@@.@
.@.@.@.@@@
@.@@@.@@@@
.@@@@@@@@.
@.@.@@@.@.

""".strip("\n")
)
f = open("  day04.txt  ".strip())

board = np.array([[c for c in line.strip()] for line in f])
w = (board == "@").astype(int)
h = w + np.concatenate((0 * w[:, [0]], np.roll(w, 1, axis=1)[:, 1:]), axis=1) + np.concatenate((np.roll(w, -1, axis=1)[:, :-1], 0 * w[:, [0]]), axis=1)
hv = h + np.concatenate((0 * h[[0], :], np.roll(h, 1, axis=0)[1:, :]), axis=0) + np.concatenate((np.roll(h, -1, axis=0)[:-1:, :], 0 * h[[0], :], ), axis=0)

ans = sum(sum(hv < 5 * w))

print(f"""
The solution is {ans}
""".strip())

w = (board == "@").astype(int)
while True:
    h = w + np.concatenate((0 * w[:, [0]], np.roll(w, 1, axis=1)[:, 1:]), axis=1) + np.concatenate((np.roll(w, -1, axis=1)[:, :-1], 0 * w[:, [0]]), axis=1)
    hv = h + np.concatenate((0 * h[[0], :], np.roll(h, 1, axis=0)[1:, :]), axis=0) + np.concatenate((np.roll(h, -1, axis=0)[:-1:, :], 0 * h[[0], :], ), axis=0)
    if not np.any(hv < 5 * w):
        break
    w = w - (hv < 5 * w).astype(int)

ans = sum(sum(board == "@")) - sum(sum(w))

print(f"""
The solution is {ans}
""".strip())