from io import StringIO

import pandas as pd
import numpy as np

f = StringIO(
"""

123 328  51 64 
 45 64  387 23 
  6 98  215 314
*   +   *   +  

""".strip("\n")
)
f = open("  day06.txt  ".strip())

board = []

for line in f:
    board.append(line)
ops = board[-1].strip().split()
numbers = list(zip(*map(str.split,board[:-1])))

ans = 0
for nrs, op in zip(numbers, ops):
    ans += eval(op.join(nrs))



print(f"""
The solution is {ans}
""".strip())


numbers = list(map("".join, zip(*board[:-1])))

nrs = []
prob = []
for nr in numbers:
    if not nr.strip():
        nrs.append(prob)
        prob = []
    else:
        prob.append(nr)

ans = 0
for nos, op in zip(nrs, ops):
    ans += eval(op.join(nos))


print(f"""
The solution is {ans}
""".strip())