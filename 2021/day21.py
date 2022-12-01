"""
input:
Player 1 starting position: 6
Player 2 starting position: 7
"""

import numpy as np
import pandas as pd
from itertools import cycle, product
from functools import lru_cache, partial
from collections import Counter
from operator import mul

initial = [5, 6] # subtract 1 to the indices in order to use modular arithmetic
pos = initial.copy()
points = [0, 0]
die = cycle(range(10))
print("Ignore this die roll:", next(die))
rolls = 0

for player in cycle([0, 1]):
    rolls += 3
    pos[player] += sum(next(die) for _ in range(3))
    pos[player] %= 10
    points[player] += pos[player] + 1
    if points[player] >= 1000:
        break
print("rolls", rolls, "winning player", player,"points of losing player", points[1 - player], "product", rolls * points[1 - player])

rolls = Counter(map(sum, product(range(1, 4), range(1, 4), range(1, 4))))

@lru_cache(maxsize=None)
def outcomes(pos1, pos2, points1, points2):
    if points1 >= 21:
        return [0, 0]
    elif points2 >= 21:
        return [0, 1]
    else:
        ans = [0, 0]
        for result, nrolls in rolls.items():
            pos = (pos1 + result) % 10
            points = pos + 1 + points1
            ans = list(map(lambda x: x[0] + nrolls * x[1], zip(ans, outcomes(pos2, pos, points2, points)[::-1])))
        return ans

wins_per_player = outcomes(*initial, 0, 0)
print("Wins per player", wins_per_player)
print("Number of wins of the player that wins the most", max(wins_per_player))

print("Solving it again for lols")

universe = {}
q = [(*initial, 0, 0, 0)]
while q:
    conditions = q.pop()
    pos1, pos2, points1, points2, state = conditions
    if conditions[:-1] in universe:
        pass
    elif points1 >= 21:
        universe[conditions[:-1]] = (0, 0)
    elif points2 >= 21:
        universe[conditions[:-1]] = (0, 1)
    elif state == 0:
        q.append((*conditions[:-1], 1))
        ans = [0, 0]
        for result, _ in rolls.items():
            pos = (pos1 + result) % 10
            points = pos + 1 + points1
            q.append((pos2, pos, points2, points, 0))
    elif state == 1:
        ans = (0, 0)
        for result, nrolls in rolls.items():
            pos = (pos1 + result) % 10
            points = pos + 1 + points1
            ans = tuple(map(lambda x: x[0] + nrolls * x[1], zip(ans, universe.get((pos2, pos, points2, points))[::-1])))
        universe[conditions[:-1]] = ans
    else:
        raise ValueError("Screwed up...")

print("Wins per player", universe[(*initial, 0, 0)])
