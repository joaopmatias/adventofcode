import pandas as pd
import numpy as np

f = open("day7.txt", "r")
crabs = list(map(int, f.read().strip().split(",")))
print("Sample:", crabs[:5])

pos = np.array(crabs, dtype=int)
a, b = pos.min(), pos.max() + 1
print("min", a, "max", b)
fuel = np.nan
ans = np.nan
for i in range(a, b):
    if not fuel < np.abs(pos - i).sum():
        ans = i
        fuel = np.abs(pos - i).sum()
print("Best horizontal:", ans)
print("Least fuel:", fuel)

fuel = np.nan
ans = np.nan
for i in range(a, b):
    if not fuel < (np.square(pos - i) + np.abs(pos - i)).sum() // 2:
        ans = i
        fuel = (np.square(pos - i) + np.abs(pos - i)).sum() // 2
print("Best horizontal:", ans)
print("Least fuel:", fuel)
