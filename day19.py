
import numpy as np
import pandas as pd
from io import StringIO
from sympy.combinatorics import Permutation
from itertools import combinations, permutations, product, count
from operator import add
from functools import partial, reduce
from numpy.linalg import inv

f = open("day19.txt", "r")
dfs = [pd.read_csv(StringIO(s.strip()), skiprows=1, header=None) for s in f.read().split("\n\n")]

dfss = [pd.concat([df - v for v in df.itertuples(index=False)]).where(lambda d: (d != 0).any(axis=1)).dropna().reset_index(drop=True).astype(int).copy() for df in dfs]

overlap = []

rotations = list(map(lambda x: (*x,  Permutation(x[0]).signature() * x[1] * x[2]), product(map(list, permutations((0, 1, 2))), (-1, 1), (-1, 1))))

for i, df_i, dfd_i, j, df_j, dfd_j in map(partial(reduce, add), combinations(zip(count(0), dfs, dfss), 2)):
    stop = False
    l_df_i = list(df_i.itertuples(index=False))
    for perm, e, f, g in rotations:
        if stop:
            break
        df_jj  =  df_j[perm].set_axis([0, 1, 2], axis=1) * (e, f, g)
        dfd_jj = dfd_j[perm].set_axis([0, 1, 2], axis=1) * (e, f, g)
        if pd.concat((dfd_i, dfd_jj)).duplicated().reset_index(drop=True).sum() >= 132:
            for w in pd.concat(v - df_jj for v in l_df_i).itertuples(index=False):
                if stop:
                    break
                if pd.concat((df_i, df_jj + w)).duplicated().reset_index(drop=True).sum() >= 12:
                    overlap.append(((j, i), (np.diag((e, f, g)).dot(np.identity(3, dtype=int)[perm, :]), np.array(w))))
                    stop = True

q = overlap.copy()
q += [((x[1], x[0]), (inv(y[0]), inv(y[0]).dot(-y[1]))) for x, y in q]
iso = dict(q)
for _ in range(30):
    for x, y in q:
        for xx, yy in iso.copy().items():
            if xx[1] == x[0] and xx[0] != x[1]: 
                if (xx[0], x[1]) not in iso:
                    iso[(xx[0], x[1])] = (y[0].dot(yy[0]), y[0].dot(yy[1]) + y[1])
                else:
                    assert (iso[(xx[0], x[1])][0] == y[0].dot(yy[0])).all().all()
                    assert (iso[(xx[0], x[1])][1] == y[0].dot(yy[1]) + y[1]).all()

                    
beacons = pd.concat(pd.DataFrame(iso[(i, 0)][0]).dot(df.T).T + pd.Series(iso[(i, 0)][1]) for i, df in enumerate(dfs[1:], start=1)).astype(int)
beacons = pd.concat((dfs[0], beacons)).drop_duplicates().reset_index(drop=True)
print("Shape of scanners df after isometries and dropping duplicates and stuff:", beacons.shape)

scanners = pd.concat((pd.Series(iso[(i, 0)][1]) for i in range(1, len(dfs))), axis=1)
scanners = pd.concat((pd.Series((0, 0, 0)), scanners), axis=1).astype(int).T.reset_index(drop=True)

ans = max([(scanners - p).abs().sum(axis=1).max() for p in scanners.itertuples(index=False)])

print("Max manhattan distance:", ans)
