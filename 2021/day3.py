import pandas as pd
import numpy as np

bits = pd.read_csv("day3.csv", names=["value"], dtype=str)
p = (
    pd.DataFrame(bits["value"].apply(tuple).tolist())
    .astype(int)
    .mean()
    .round()
    .astype(int)
    .to_frame("gamma")
    .assign(epsilon=lambda df: 1 - df["gamma"])
    .astype(str)
    .sum()
    .apply(lambda x: int(x, 2))
    .prod()
)
print(f"The product of gamma and epsilon is {p}")

bits = pd.DataFrame(bits["value"].apply(tuple).tolist()).astype(int)
ix = bits.index
for col, values in bits.iteritems():
    v = values.loc[ix]
    common = int(round(v.mean() + 1e-6))
    ix = v[v == common].index
o2 = ix
ix = bits.index
for col, values in bits.iteritems():
    v = values.loc[ix]
    uncommon = int(1 - round(v.mean() + 1e-6))
    ix = v[v == uncommon].index if sum(v == uncommon) else ix
co2 = ix
q = (
    bits
    .loc[o2.union(co2), :]
    .astype(str)
    .sum(axis=1)
    .astype(int)
    .astype(str)
    .apply(lambda x: int(x, 2))
    .prod()
)
print(f"The product of o2 and co2 is {q}")
