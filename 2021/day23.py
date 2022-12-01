
import numpy as np
import pandas as pd
from io import StringIO
import re
from heapq import heappush, heappop, heapify

text = """
#############
#...........#
###D#C#A#B###
  #C#D#A#B#
  #########
"""

"""
Don't stop in (2, 2), (4, 2), (6, 2), (8, 2)
Once it moves in the halway go to the final position
"""

print("Using pencil, the answer is", 17400)

"""
new input
"""

text = """
#############
#...........#
###D#C#A#B###
  #D#C#B#A#
  #D#B#A#C#
  #C#D#A#B#
  #########
"""

burrow = tuple(pd.read_csv(StringIO(re.sub(r"###|(?<=\s)#|#(?=\s)| ", "", text)), sep="#", skipfooter=0, skiprows=3, index_col=None, header=None, engine="python").T.itertuples(index=False, name=None))
burrow = (".", ".") + burrow[0:1] + (".",) + burrow[1:2] + (".",) + burrow[2:3] + (".",) + burrow[3:4] + (".", ".")

fuel = {
    ".": 0,
    "A": 1,
    "B": 10,
    "C": 100,
    "D": 1000,
}
rooms = {
    "A": 2,
    "B": 4,
    "C": 6,
    "D": 8,
}

ishallway = {0, 1, 3, 5, 7, 9, 10}.__contains__
isroom = {2, 4, 6, 8}.__contains__
isempty = (".", ".", ".", ".").__eq__


def isvalid(move, position):
    i0, i1 = move
    if isroom(i0):
        return position[i1] == "." and all(map(lambda x: (x == ".") or isinstance(x, tuple), position[i1:i0:1 - 2 * (i1 > i0)]))
    else:
        return not bool(set(position[i1]) - {".", position[i0]}) and all(map(lambda x: (x == ".") or isinstance(x, tuple), position[i1:i0:1 - 2 * (i1 > i0)]))

def explore(position):
    for i0 in [0, 1, 3, 5, 7, 9, 10]:
        amphipod = position[i0]
        if amphipod != ".":
            i1 = rooms[amphipod]
            if isvalid((i0, i1), position):
                room = position[i1]
                energy = abs(i1 - i0) * fuel[amphipod] + fuel[amphipod] + sum(map(fuel.get, room))
                yield energy, (i0, i1)
    for i0 in [2, 4, 6, 8]:
        room = position[i0]
        amphipod = room[0]
        if amphipod != ".":
            for i1 in [0, 1, 3, 5, 7, 9, 10]:
                if position[i1] == "." and isvalid((i0, i1), position):
                    energy = abs(i1 - i0) * fuel[amphipod] + sum(map(fuel.get, room))
                    yield energy, (i0, i1)

def step(move, position):
    i0, i1 = move
    ll = list(position)
    if ishallway(i0):
        ll[i1] = (ll[i0],) + position[i1][:-1]
        ll[i0] = "."
    elif isroom(i0):
        ll[i1] = ll[i0][0]
        ll[i0] = position[i0][1:] + (".",)
    else:
        assert False, "Screwed up..."
    return tuple(ll)
    
positions = set()
q = [(0, burrow)]

i = 0
position = [()] * 10
while not (set(position[2]) == {"A"} and set(position[4]) == {"B"} and set(position[6]) == {"C"} and set(position[8]) == {"D"}):
    acc_energy, position = heappop(q)
    if position in positions:
        pass
    else:
        positions.add(position)
        for energy, move in explore(position):
            heappush(q, (acc_energy + energy, step(move, position)))

print("Least energy:", acc_energy)
