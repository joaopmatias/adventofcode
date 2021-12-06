import pandas as pd
import numpy as np
from io import StringIO
from functools import partial

f = open("day5.txt", "r")

ins = f.read().replace(" -> ", ",")
df = pd.read_csv(StringIO(ins), names=["x", "y", "r", "s"])
print("Sample:\n", df.head())
print("Number of vents: ", (df["x"] - df["r"].rename("x")).abs().sum() + (df["y"] - df["s"].rename("y")).abs().sum())
print("x:", min(df["x"].min(), df["r"].min()), max(df["x"].max(), df["r"].max()))
print("y:", min(df["y"].min(), df["s"].min()), max(df["y"].max(), df["s"].max()))

ocean = np.zeros((1000, 1000), dtype=int)

def line(arr, x, y, r, s, **kwargs):
    if x == r:
        if y < s:
            arr[x, y:(s+1)] += 1
        else:
            arr[x, s:(y+1)] += 1
    elif y == s:
        if x < r:
            arr[x:(r+1), y] += 1
        else:
            arr[r:(x+1), y] += 1        

for row in df.itertuples():
    line(arr=ocean, **row._asdict())
print("Number of locations with 2 or more vents:", (ocean >= 2).sum().sum())

ocean = np.zeros((1000, 1000), dtype=int)

def line(arr, x, y, r, s, **kwargs):
    if x == r:
        if y < s:
            arr[x, y:(s+1)] += 1
        else:
            arr[x, s:(y+1)] += 1
    elif y == s:
        if x < r:
            arr[x:(r+1), y] += 1
        else:
            arr[r:(x+1), y] += 1
    elif abs(x - r) == abs(y - s):
        for i, j in zip(range(x, r, 1 - 2 * (x > r)), range(y, s, 1 - 2 * (y > s))):
            arr[i][j] += 1
        arr[r][s] += 1

for row in df.itertuples():
    line(arr=ocean, **row._asdict())
print("Number of locations with 2 or more vents:", (ocean >= 2).sum().sum())
