
import pandas as pd
import numpy as np
from io import StringIO
from itertools import product, count
from functools import partial, reduce
from operator import add

f = open("day22.txt", "r")
text = f.read().replace("on ", "1,").replace("off ", "0,").replace("x=", "").replace("y=", "").replace("z=", "").replace("..", ",")
steps = pd.read_csv(StringIO(text), names=["state", "x0", "x1", "y0", "y1", "z0", "z1"]).astype(int).astype({"state": bool})

m = np.zeros((101, 101, 101), dtype=bool)
for state, x0, x1, y0, y1, z0, z1 in steps.itertuples(index=False):
    m[
        (50 + min(51, max(-50, x0))):(50 + min(51, max(-50, x1 + 1))),
        (50 + min(51, max(-50, y0))):(50 + min(51, max(-50, y1 + 1))),
        (50 + min(51, max(-50, z0))):(50 + min(51, max(-50, z1 + 1))),
    ] = state 
print("Number of cubes on:", m.sum())

xs = sorted(list(set(steps["x0"].tolist() + (steps["x1"] + 1).tolist())))
ys = sorted(list(set(steps["y0"].tolist() + (steps["y1"] + 1).tolist())))
zs = sorted(list(set(steps["z0"].tolist() + (steps["z1"] + 1).tolist())))
n_x = len(xs)
n_y = len(ys)
n_z = len(zs)
print("# x endoints:", n_x, "# y endoints:", n_y, "# z endoints:", n_z)

dx = np.array(xs[1:], dtype=int) - np.array(xs[:-1], dtype=int)
dy = np.array(ys[1:], dtype=int) - np.array(ys[:-1], dtype=int)
dz = np.array(zs[1:], dtype=int) - np.array(zs[:-1], dtype=int)
mm = (
    np.tile(dx.reshape((-1, 1, 1)), (1, n_y - 1, n_z - 1)) *
    np.tile(dy.reshape((1, -1, 1)), (n_x - 1, 1, n_z - 1)) *
    np.tile(dz.reshape((1, 1, -1)), (n_x - 1, n_y - 1, 1))
)
mmm = np.zeros((n_x - 1, n_y - 1, n_z - 1), dtype=bool)
for state, x0, x1, y0, y1, z0, z1 in steps.itertuples(index=False):
    ix0 = xs.index(x0)
    ix1 = xs.index(x1 + 1)
    iy0 = ys.index(y0)
    iy1 = ys.index(y1 + 1)
    iz0 = zs.index(z0)
    iz1 = zs.index(z1 + 1)
    mmm[ix0:ix1, iy0:iy1, iz0:iz1] = state
print("Number of cubes on:", (mm * mmm).sum())
