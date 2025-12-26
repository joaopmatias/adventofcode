
from io import StringIO

import pandas as pd
import numpy as np
from scipy.sparse import coo_matrix


f = StringIO(
"""

aaa: you hhh
you: bbb ccc
bbb: ddd eee
ccc: ddd eee fff
ddd: ggg
eee: out
fff: out
ggg: out
hhh: ccc fff iii
iii: out

""".strip("\n")
)
f = open("  day11.txt  ".strip())

graph = (
    pd.DataFrame(
        list(map(
            lambda x: list(map(str.strip, x.split(":"))),
            f)), 
        columns=["start", "end"])
    .pipe(lambda x: pd.concat((
        pd.DataFrame([dict(start="you", end="--0")]),
        pd.DataFrame([dict(start="--0", end="--0")]),
        pd.DataFrame([dict(start="out", end="--3")]),
        pd.DataFrame([dict(start="--3", end="--3")]),
        x)))
    .assign(index=lambda x: pd.factorize(x["start"])[0])
    .tail(-1)
    .pipe(
        lambda x:
        x.assign(end=x["end"].str.split())
        .explode("end")
        .reset_index(drop=True)
        .replace(dict(x[["start", "index"]].to_dict("split")["data"])))
    [["start", "end"]]
)

m = (
    coo_matrix((
        graph.index.to_numpy() * 0 + 1, 
        (
            graph["start"].to_numpy(),
            graph["end"].to_numpy())))
    .tocsr()
)

for _ in range(50):
    m @= m

print(f"""
The solution is {m[0, 3]}
""".strip())


f = StringIO(
"""

svr: aaa bbb
aaa: fft
fft: ccc
bbb: tty
tty: ccc
ccc: ddd eee
ddd: hub
hub: fff
eee: dac
dac: fff
fff: ggg hhh
ggg: out
hhh: out

""".strip("\n")
)
f = open("  day11.txt  ".strip())

graph = (
    pd.DataFrame(
        list(map(
            lambda x: list(map(str.strip, x.split(":"))),
            f)), 
        columns=["start", "end"])
    .pipe(lambda x: pd.concat((
        pd.DataFrame([dict(start="svr", end="--0")]),
        pd.DataFrame([dict(start="--0", end="--0")]),
        pd.DataFrame([dict(start="fft", end="--1")]),
        pd.DataFrame([dict(start="--1", end="--1")]),
        pd.DataFrame([dict(start="dac", end="--2")]),
        pd.DataFrame([dict(start="--2", end="--2")]),
        pd.DataFrame([dict(start="out", end="--3")]),
        pd.DataFrame([dict(start="--3", end="--3")]),
        x)))
    .assign(index=lambda x: pd.factorize(x["start"])[0])
    .tail(-1)
    .pipe(
        lambda x:
        x.assign(end=x["end"].str.split())
        .explode("end")
        .reset_index(drop=True)
        .replace(dict(x[["start", "index"]].to_dict("split")["data"])))
    [["start", "end"]]
)

m = (
    coo_matrix((
        graph.index.to_numpy() * 0 + 1, 
        (
            graph["start"].to_numpy(),
            graph["end"].to_numpy())))
    .tocsr()
)


for _ in range(50):
    m @= m


print(f"""
The solution is {m[0, 3] * m[2, 5] * m[4, 7] + m[0, 5] * m[4, 3] * m[2, 6]}
""".strip())