import numpy as np
import pandas as pd
from io import StringIO
from functools import reduce

f = open("day13.txt", "r")
text = f.readlines()
print("Coordinates stop in line:", text.index("\n"))

coordinates = pd.read_csv(StringIO(''.join(text[:791])), names=["x", "y"])
print("Sample coordinates:\n", coordinates.head())
folds = pd.read_csv(StringIO(''.join(text[792:])), header=None, sep=" ")[2].str.split("=", expand=True).astype({0:str, 1:int})
print("Sample folds:\n", folds)

print("x in ", coordinates["x"].min(), coordinates["x"].max())
print("y in ", coordinates["y"].min(), coordinates["y"].max())

c = coordinates.assign(x2=lambda df: 655 - (df["x"] - 655).abs())
print("before", c.groupby(["x", "y"]).count().shape, "after", c.groupby(["x2", "y"]).count().shape)

r = reduce(lambda x, y: x.assign(**{y[1]: lambda df: y[2] - (df[y[1]] - y[2]).abs()}), folds.itertuples(), coordinates).groupby(["x", "y"]).count()[[]].reset_index()
print("x in", r["x"].min(), r["x"].max())
print("y in", r["y"].min(), r["y"].max())

draw = np.resize(np.array([" "], dtype=str), (6, 39))
for _, x, y in r.itertuples():
    draw[y, x] = "#"
print('\n'.join(map(''.join, draw)))
