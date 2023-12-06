
import re
from io import StringIO

import pandas as pd
import numpy as np

f = StringIO(
"""

Time:      7  15   30
Distance:  9  40  200

""".strip("\n")
)
f = open("  day06.txt  ".strip())
times = map(int, re.sub(r"\s+", " ", f.readline().split(":")[1].strip()).split(" "))
records = map(int, re.sub(r"\s+", " ", f.readline().split(":")[1].strip()).split(" "))

ans = 1
for t, r in zip(times, records):
    a = 0
    b = (t + 1) // 2
    if t <= 1:
        ans *= 0
    elif r == 0:
        ans *= t - 1
    elif t == 2:
        ans *= 0
    elif r >= b * (t - b):
        ans *= 0
    else:
        while b - a > 1:
            c = (b + a) // 2
            if r >= c * (t - c):
                a = c
            else:
                b = c
        
        lower = b
        
        a = t // 2
        b = t
        while b - a > 1:
            c = (b + a) // 2
            if r < c * (t - c):
                a = c
            else:
                b = c
        
        upper = a
        
        ans *= upper - lower + 1

print(f"""
The solution is {ans}
""".strip())

print()

f = StringIO(
"""

Time:      7  15   30
Distance:  9  40  200

""".strip("\n")
)
f = open("  day06.txt  ".strip())
t = int(re.sub(r"\s", "", f.readline().split(":")[1].strip()))
r = int(re.sub(r"\s", "", f.readline().split(":")[1].strip()))

ans = 1
a = 0
b = (t + 1) // 2
if t <= 1:
    ans *= 0
elif r == 0:
    ans *= t - 1
elif t == 2:
    ans *= 0
elif r >= b * (t - b):
    ans *= 0
else:
    while b - a > 1:
        c = (b + a) // 2
        if r >= c * (t - c):
            a = c
        else:
            b = c

    lower = b

    a = t // 2
    b = t
    while b - a > 1:
        c = (b + a) // 2
        if r < c * (t - c):
            a = c
        else:
            b = c

    upper = a

    ans *= upper - lower + 1



print(f"""
The solution is {ans}
""".strip())