from io import StringIO

import pandas as pd
import numpy as np

"""
The first column is what your opponent is going to play: A for Rock, B for Paper, and C for Scissors

The second column, you reason, must be what you should play in response: X for Rock, Y for Paper, and Z for Scissors

1 for Rock, 2 for Paper, and 3 for Scissors

0 if you lost, 3 if the round was a draw, and 6 if you won
"""


f = StringIO(
"""
A Y
B X
C Z
"""
)
f = open("day2.txt")

tournament = (
    pd.read_csv(f, sep=" ", header=None)
    .set_axis(["foe", "me"], axis=1)
    .replace({
        "A": 1,
        "B": 2,
        "C": 3,
        "X": 1,
        "Y": 2,
        "Z": 3,
    })
    .assign(outcome=lambda df: ((df["me"] - df["foe"] + 1) % 3) * 3)
)

print(f"The score total using the guide: {tournament.sum().loc[['me', 'outcome']].sum()}")

"""
X means you need to lose, Y means you need to end the round in a draw, and Z means you need to win
"""

tournament2 = (
    tournament
    .assign(outcome=lambda df: 3 * (df["me"] - 1))
    .assign(me=lambda df: (df["me"] + df["foe"]) % 3 + 1)
)

print(f"The score total using the guide: {tournament2.sum().loc[['me', 'outcome']].sum()}")
