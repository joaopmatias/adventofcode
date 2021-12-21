
import numpy as np
import pandas as pd
from itertools import product

f = open("day20.txt", "r")

algo = list(f.readline().strip().replace(".", "0").replace("#", "1"))
f.readline()
z = np.array([list(s.strip().replace(".", "0").replace("#", "1")) for s in f], dtype=str)
m = np.concatenate((np.tile("0", (z.shape[0], 4)), z, np.tile("0", (z.shape[0], 4))), axis=1)
m = np.concatenate((np.tile("0", (4, m.shape[1])), m, np.tile("0", (4, m.shape[1]))), axis=0)

mm = np.tile("0", m.shape)
for i, j in product(range(1, m.shape[0]), range(1, m.shape[1])):
    mm[i, j] = algo[int(''.join(map(''.join, m[i - 1: i + 2, j - 1: j + 2])), 2)]

mmm = np.tile("0", m.shape)
for i, j in product(range(2, m.shape[0] - 1), range(2, m.shape[1] - 1)):
    mmm[i, j] = algo[int(''.join(map(''.join, mm[i - 1: i + 2, j - 1: j + 2])), 2)]

mmm.astype(int).sum()

m = np.concatenate((np.tile("0", (z.shape[0], 100)), z, np.tile("0", (z.shape[0], 100))), axis=1)
m = np.concatenate((np.tile("0", (100, m.shape[1])), m, np.tile("0", (100, m.shape[1]))), axis=0)
mm = m.copy()

for k in range(50):
    m = mm
    mm = np.tile("0", m.shape)
    for i, j in product(range(1 + k, m.shape[0] - k), range(1 + k, m.shape[1] - k)):
        mm[i, j] = algo[int(''.join(map(''.join, m[i - 1: i + 2, j - 1: j + 2])), 2)]

mm.astype(int).sum()
