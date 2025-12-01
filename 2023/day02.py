from io import StringIO

import pandas as pd
import numpy as np

f = StringIO(
"""
Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue
Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red
Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red
Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green
""".strip("\n")
)
f = open("  day02.txt  ".strip())

data = []
for l in f:
    nr, game = l.strip().split(":")
    nr = nr[4:]
    gameplays = list(map(
        lambda x: dict([
            ("game", nr),
            *map(
                lambda y: tuple(reversed(y.strip().split(" "))),
                x.split(","))
        ]),
        game.split(";")
    ))
    data += gameplays

data = pd.DataFrame(data).fillna("0").astype(int)

ans = (
    data
    .groupby("game", as_index=False)
    .max()
    .loc[lambda x: (x["red"] <= 12) & (x["green"] <= 13) & (x["blue"] <= 14)]
    ["game"]
    .sum()
)


print(f"""
The sum of the game ids is {ans}
""".strip())

print()

ans = (
    data
    .groupby("game", as_index=False)
    .max()
    .assign(power=lambda x: x["red"] * x["green"] * x["blue"])
    ["power"]
    .sum()
)


print(f"""
The sum of powers of the games is {ans}
""".strip())