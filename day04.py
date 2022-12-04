from io import StringIO

import pandas as pd
import numpy as np

f = StringIO(
"""
2-4,6-8
2-3,4-5
5-7,7-9
2-8,3-7
6-6,4-6
2-6,4-8
""".strip()
)
f = open("day04.txt")

cleaning = (
    pd.read_csv(
        StringIO(f.read().replace("-", ",")),
        header=None)
    .set_axis(["a", "b", "c", "d"], axis=1)
    .assign(
        is_one_range=lambda df:
        ((df["a"] <= df["c"]) & (df["d"] <= df["b"])) |
        ((df["a"] >= df["c"]) & (df["d"] >= df["b"])))
)

print(f"""
The number of pairs where one range contains the other is {cleaning["is_one_range"].astype(int).sum()}
""".strip())

cleaning2 = (
    cleaning
    .assign(
        is_overlap=lambda df:
        ((df["a"] <= df["c"]) & (df["c"] <= df["b"])) |
        ((df["c"] <= df["a"]) & (df["a"] <= df["d"])))
)

print(f"""
The number of pairs where one range overlaps with the other is {cleaning2["is_overlap"].astype(int).sum()}
""".strip())
