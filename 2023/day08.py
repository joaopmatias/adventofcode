
import re
from math import lcm
from io import StringIO

import pandas as pd
import numpy as np

f = StringIO(
"""

RL

AAA = (BBB, CCC)
BBB = (DDD, EEE)
CCC = (ZZZ, GGG)
DDD = (DDD, DDD)
EEE = (EEE, EEE)
GGG = (GGG, GGG)
ZZZ = (ZZZ, ZZZ)

""".strip("\n")
)
f = StringIO(
"""

LLR

AAA = (BBB, BBB)
BBB = (AAA, ZZZ)
ZZZ = (ZZZ, ZZZ)

""".strip("\n")
)
f = open("  day08.txt  ".strip())

instructions = f.readline().strip()

f.readline()

net = {"R": {}, "L": {}}
for line in f:
    node, l, r = re.match(r"(\w+) = \((\w+), (\w+)\)", line.strip()).groups()
    net["R"][node] = r
    net["L"][node] = l

iteration = {}
for node in net["R"]:
    now = node
    for c in instructions:
        now = net[c][now]
    iteration[node] = now

node = "AAA"
counter = 0
while node != "ZZZ":
    node = iteration[node]
    counter += 1

print(f"""
The solution is {counter * len(instructions)}
""".strip())

print()

f = StringIO(
"""

LR

11A = (11B, XXX)
11B = (XXX, 11Z)
11Z = (11B, XXX)
22A = (22B, XXX)
22B = (22C, 22C)
22C = (22Z, 22Z)
22Z = (22B, 22B)
XXX = (XXX, XXX)

""".strip("\n")
)
f = open("  day08.txt  ".strip())

instructions = f.readline().strip()

f.readline()

net = {"R": {}, "L": {}}
for line in f:
    node, l, r = re.match(r"(\w+) = \((\w+), (\w+)\)", line.strip()).groups()
    net["R"][node] = r
    net["L"][node] = l

iteration = {}
for node in net["R"]:
    now = node
    for c in instructions:
        now = net[c][now]
    iteration[node] = now

counter = []
for node in iteration:
    if node[-1] != "A":
        continue

    now = node
    counter_now = 0
    while now[-1] != "Z":
        now = iteration[now]
        counter_now += 1

    counter.append(counter_now)

print(f"""
The solution is {lcm(*counter) * len(instructions)}
""".strip())
