import pandas as pd
import numpy as np

dx = {
    "forward": 1,
    "back": -1,
    "down": 0,
    "up": 0,
}
dy = {
    "forward": 0,
    "back": 0,
    "down": -1,
    "up": 1,
}

moves = (
    pd.read_csv("day2.csv", sep=" ", names=["direction", "value"])
    .assign(dx=lambda df: df["direction"].replace(dx) * df["value"])
    .assign(dy=lambda df: df["direction"].replace(dy) * df["value"])
    [["dx", "dy"]]
)
print(moves.head(5))
print(f"The product of the final coordinates is {moves.sum().prod() * (-1)}")
moves = (
    moves
    .assign(aim=lambda df: df["dy"].cumsum() * (-1))
    .assign(dz=lambda df: (df["aim"] * df["dx"]))
    [["dx", "dz"]]
)
print(moves.head(5))
print(f"The product of the final coordinates is {moves.sum().prod()}")
