from io import StringIO

import pandas as pd
import numpy as np

f = StringIO(
"""
1000
2000
3000

4000

5000
6000

7000
8000
9000

10000
"""
)
f = open("day1.txt")
elfs = (
    pd.Series(f)
    .rename("calories")
    .str.strip()
    .loc[lambda s: s != ""]
    .astype(int)
    .to_frame()
    .reset_index()
    .assign(elf=lambda df: df["index"] - df.index)
    [["elf", "calories"]]
    .groupby(by="elf")
    .sum()
)

print(f"The elf with the most calories has {elfs.max().to_numpy()}")

top3 = (
    elfs
    .sort_values("calories", ascending=False)
    .iloc[:3]
)

print(f"The top 3 elves have {top3.sum().to_numpy()}")
