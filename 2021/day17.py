import numpy as np
import pandas as pd
from itertools import count
from math import sqrt, floor, ceil
from collections import Counter
from itertools import groupby, product


print("v_x could be (triangular):")
for n in range(30):
    if 230 <= (n**2 - n)//2 <= 283:
        print("   ", n, (n**2 - n)//2)

"""
target area: x=230..283, y=-107..-57

we'll aim to target y = -64 and see how close we get

root is 2*vy+1
"""

highest = -np.inf
for vy in range(250):
    r = (2*vy+1 + sqrt((2*vy + 1)**2 + 256))/2
    u = int(ceil(r))
    l = int(floor(r))
    if -107 <= (-u**2 + u + 2*u*vy)//2 <= -57 or -107 <= (-l**2 + l + 2*l*vy)//2 <= -57:
        highest = (vy**2 + vy)//2
print("Max y:", highest)

vys = []
vxs = []

for vy in range(-250, 250):
    for n in count(max(2*vy + 1, 0)):
        if   (-n**2 + n + 2*n*vy)//2 < -107:
            break
        elif (-n**2 + n + 2*n*vy)//2 <= -57:
            vys.append((n, vy))
        else:
            pass

for vx in range(600):
    x = 0
    for n in range(500):
        if   x > 283:
            break
        elif x >= 230:
            vxs.append((n, vx))
        else:
            pass
        x += max(vx - n, 0)
#print(dict(map(lambda x: (x[0], list(zip(*x[1]))[1]), groupby(vxs, key=lambda x:x[0]))))
#print(dict(map(lambda x: (x[0], list(zip(*x[1]))[1]), groupby(vys, key=lambda x:x[0]))))

solx = dict(map(lambda x: (x[0], tuple(zip(*x[1]))[1]), groupby(sorted(vxs), key=lambda x:x[0])))
soly = dict(map(lambda x: (x[0], tuple(zip(*x[1]))[1]), groupby(sorted(vys), key=lambda x:x[0])))

ans = []
for n in set(solx.keys()).intersection(set(soly.keys())):
    ans += list(product(solx[n], soly[n]))
#print(ans)
print("Length with different steps:", len(ans))
print("Length after filter:", len(set(ans)))

for vx, vy in set(ans):
    x = 0
    y = 0
    for n in range(500):
        if x > 283 or y < -107:
            pass
        elif x >= 230 and y <= -57:
            break
        x += max(vx - n, 0)
        y += vy - n
    if n >= 499:
        print("Something wrong with ", vx, vy)
