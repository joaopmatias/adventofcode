import numpy as np
import pandas as pd
from collections import defaultdict
from random import choices
from functools import reduce
from itertools import count, starmap
from operator import add, mul, eq, mod

df = pd.read_csv("day24.txt", names=["operation", "x", "y"], sep=" ").fillna(0).astype({"y":str})
alu = [t if t[2].isalpha() else t[:2] + (int(t[2]),) for t in df.itertuples(index=False, name=None)]

"""
inp
mul
add
mod do not use negative numbers.
div do not divide by zero. truncate the result (round towards 0).
eql

instructions show repetition every 18
abuse it a bit and try to make "eql x w" return 1 whenever x is less than 10
"""

def monad(instructions, nr):
    enter = iter(map(int, list(str(nr))))
    operations = {
        "inp": lambda *args: next(enter),
        "eql": lambda x, y: int(x == y),
        "add": add,
        "mul": mul,
        "mod": mod,
        "div": lambda x, y: (abs(x) // abs(y)) * int(np.sign(x * y)),
    }
    variables = defaultdict(lambda: 0)
    for op, x, y in instructions:
        if y == "w" and op == "eql":
            print(op, x, y, dict(variables))
        #print(op, x, y)
        #print(variables)
        y = y if isinstance(y, int) else variables[y]
        if op == "div":
            assert y != 0, "don't divide by zero"
        elif op == "mod":
            assert y > 0 and variables[x] >= 0, "don't use negative numbers in integer division"

        variables[x] = operations[op](variables[x], y)
    
    return variables["z"] == 0, dict(variables)

for _ in range(1):
    try:
        nr = reduce(lambda x, y: 10 * x + y, (9,9,7,9,9, 2,1, 2, 9, 4, 9,9,6,7) + tuple(choices(range(1, 10), k=14)))
        valid, variables = monad(alu, nr)
        if True:
            print(valid, variables, flush=True)
    except AssertionError:
        pass

print("by trial and error answer is", "".join(map(str, (9,9,7,9,9, 2,1, 2, 9, 4, 9,9,6,7))))

for _ in range(1):
    try:
        nr = reduce(lambda x, y: 10 * x + y, (3,4,1,9,8, 1,1, 1, 8, 1, 6,3,1,1) + tuple(choices(range(1, 10), k=14)))
        valid, variables = monad(alu, nr)
        if True:
            print(valid, variables, flush=True)
    except AssertionError:
        pass

print("by trial and error answer is", "".join(map(str, (3,4,1,9,8, 1,1, 1, 8, 1, 6,3,1,1))))
