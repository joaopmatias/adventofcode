import numpy as np
import pandas as pd

octo = (
    pd.read_csv("day11.txt", header=None, dtype=str)
    [0]
    .str
    .split("", expand=True)
    .replace("", np.nan)
    .T
    .dropna()
    .reset_index(drop=True)
    .T
    .astype(int)
)

ans = 0
for _ in range(100):
    flash = octo.isna()
    octo += 1
    now = octo > 9
    while now.any().any():
        wave = now.shift(-1, axis=0).fillna(0) + now + now.shift(1, axis=0).fillna(0)
        wave = wave.shift(-1, axis=1).fillna(0) + wave + wave.shift(1, axis=1).fillna(0)
        octo += wave
        flash = flash | now
        octo[flash] = 0
        now = octo > 9
    ans += flash.sum().sum()
print("Number of flashes:", ans)

octo = (
    pd.read_csv("day11.txt", header=None, dtype=str)
    [0]
    .str
    .split("", expand=True)
    .replace("", np.nan)
    .T
    .dropna()
    .reset_index(drop=True)
    .T
    .astype(int)
)

i=0
flash = octo.isna()
while not flash.all().all():
    i += 1
    flash = octo.isna()
    octo += 1
    now = octo > 9
    while now.any().any():
        wave = now.shift(-1, axis=0).fillna(0) + now + now.shift(1, axis=0).fillna(0)
        wave = wave.shift(-1, axis=1).fillna(0) + wave + wave.shift(1, axis=1).fillna(0)
        octo += wave
        flash = flash | now
        octo[flash] = 0
        now = octo > 9
    ans += flash.sum().sum()
print("Step:", i)
