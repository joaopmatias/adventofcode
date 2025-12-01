
from io import StringIO

import pandas as pd
import numpy as np

f = StringIO(
"""

Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53
Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19
Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1
Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83
Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36
Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11

""".strip("\n")
)
f = open("  day04.txt  ".strip())

ans = 0
for line in f:
    _, a = line.strip().split(":")
    left, right = a.split("|")
    left = set(map(int, left.strip().replace("  ", " ").replace("  ", " ").replace("  ", " ").split(" ")))
    right = list(map(int, right.strip().replace("  ", " ").replace("  ", " ").replace("  ", " ").split(" ")))
    ans += int(2 ** (len([c for c in right if c in left]) - 1))

print(f"""
The total points are {ans}
""".strip())

print()

f = StringIO(
"""

Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53
Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19
Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1
Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83
Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36
Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11

""".strip("\n")
)
f = open("  day04.txt  ".strip())

count_cards = np.ones(1000, dtype=int)
ncards = 0
for line in f:
    _, a = line.strip().split(":")
    left, right = a.split("|")
    left = set(map(int, left.strip().replace("  ", " ").replace("  ", " ").replace("  ", " ").split(" ")))
    right = list(map(int, right.strip().replace("  ", " ").replace("  ", " ").replace("  ", " ").split(" ")))
    points = len([c for c in right if c in left])
    if points > 0:
        count_cards[ncards+1:ncards+1+points] += count_cards[ncards]
    ncards += 1

print(f"""
The total number of cards is {np.sum(count_cards[:ncards])}
""".strip())
