
import re

from io import StringIO
from copy import deepcopy
from math import prod, lcm
from inspect import signature

import pandas as pd
import numpy as np

f = StringIO(
"""
Monkey 0:
  Starting items: 79, 98
  Operation: new = old * 19
  Test: divisible by 23
    If true: throw to monkey 2
    If false: throw to monkey 3

Monkey 1:
  Starting items: 54, 65, 75, 74
  Operation: new = old + 6
  Test: divisible by 19
    If true: throw to monkey 2
    If false: throw to monkey 0

Monkey 2:
  Starting items: 79, 60, 97
  Operation: new = old * old
  Test: divisible by 13
    If true: throw to monkey 1
    If false: throw to monkey 3

Monkey 3:
  Starting items: 74
  Operation: new = old + 3
  Test: divisible by 17
    If true: throw to monkey 0
    If false: throw to monkey 1
""".strip("\n")
)
f = open("  day11.txt  ".strip())

"""
monkey
{
    "items": [...],
    "op": lambda...,
    "test": lambda : int,
    "inspected":,
}
"""

monkeys = []
while True:
    monkey = {}
    assert f.readline()[:6] == "Monkey"
    monkey["items"] = list(map(int, re.match(r"^\s*Starting items: (.*)\n$", f.readline()).group(1).split(", ")))
    monkey["op"] = lambda old, ex=re.match(r"^\s*Operation: new = (.*)\n$", f.readline()).group(1): eval(ex)
    monkey["test"] = (
        lambda
        wl,
        q=int(re.match(r"^\s*Test: divisible by (\S*)\n$", f.readline()).group(1)),
        tt=int(re.match(r"^\s*If true: throw to monkey (\S*)\n$", f.readline()).group(1)),
        ff=int(re.match(r"^\s*If false: throw to monkey (\S*)\n*$", f.readline()).group(1)):
        tt if wl % q == 0 else ff
    )
    monkey["inspected"] = 0
    monkeys.append(monkey)
    if f.readline() != "\n":
        break

monkeys0 = deepcopy(monkeys)
        
for _ in range(20):
    for i in range(len(monkeys)):
        monkey = monkeys[i]
        while len(monkey["items"]) > 0:
            monkey["inspected"] += 1
            wl = monkey["op"](monkey["items"].pop()) // 3
            monkeys[monkey["test"](wl)]["items"].append(wl)
        

print(f"""
The level of monkey business is {prod(list(sorted([d["inspected"] for d in monkeys], reverse=True))[:2])}
""".strip())

monkeys = deepcopy(monkeys0)
mm = lcm(*[signature(m["test"]).parameters["q"].default for m in monkeys])

for _ in range(10000):
    for i in range(len(monkeys)):
        monkey = monkeys[i]
        while len(monkey["items"]) > 0:
            monkey["inspected"] += 1
            wl = monkey["op"](monkey["items"].pop()) % mm
            monkeys[monkey["test"](wl)]["items"].append(wl)

print(f"""
The level of monkey business after a very long time is {prod(list(sorted([d["inspected"] for d in monkeys], reverse=True))[:2])}
""".strip())
