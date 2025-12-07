from io import StringIO

import pandas as pd
import numpy as np

f = StringIO(
"""

.......S.......
...............
.......^.......
...............
......^.^......
...............
.....^.^.^.....
...............
....^.^...^....
...............
...^.^...^.^...
...............
..^...^.....^..
...............
.^.^.^.^.^...^.
...............

""".strip("\n")
)
f = open("  day07.txt  ".strip())

beam = np.array([*f.readline().strip()]) == "S"

board = []
for line in f:
    board.append(np.array([*line.strip()]) == "^")

current = beam.copy()
splits = 0
for level in board:
    splits += sum(current & level)
    current = (current & ~level) | np.concatenate(([False], current & level))[:-1] | np.concatenate((current & level, [False]))[1:]


print(f"""
The solution is {splits}
""".strip())

current = beam.astype(int)
for level in board:
    current = current * ~level + np.concatenate(([0], current * level))[:-1] + np.concatenate((current * level, [0]))[1:]


print(f"""
The solution is {sum(current)}
""".strip())