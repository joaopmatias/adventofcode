import numpy as np
import pandas as pd
from statistics import median
from operator import mul
from functools import reduce

d = {
    ")": "(",
    ">": "<",
    "]": "[",
    "}": "{",
}

points = {
    ")": 3,
    "]": 57,
    "}": 1197,
    ">": 25137,
}

f = open("day10.txt", "r")
ans = 0
for line in f:
    q = []
    for c in line.strip():
        if c in d and len(q) > 0 and q[-1] == d[c]:
            q.pop()
        elif c not in d:
            q.append(c)
        else:
            ans += points[c]
            break
print("Score:", ans)


points2 = {
    "(": 1,
    "[": 2,
    "{": 3,
    "<": 4,
}

f = open("day10.txt", "r")
scores = []
for line in f:
    q = []
    stop = False
    for c in line.strip():
        if c in d and len(q) > 0 and q[-1] == d[c]:
            q.pop()
        elif c not in d:
            q.append(c)
        else:
            stop = True
            break
    if not stop:
        scores.append(reduce((lambda x, y: 5 * x + y), map(points2.get, reversed(q)), 0))
print("Score:", median(scores))
