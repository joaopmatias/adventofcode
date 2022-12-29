from io import StringIO

import pandas as pd
import numpy as np

from sympy.solvers import solve
from sympy import Symbol

f = StringIO(
"""
root: pppw + sjmn
dbpl: 5
cczh: sllz + lgvd
zczc: 2
ptdq: humn - dvpt
dvpt: 3
lfqf: 4
humn: 5
ljgn: 2
sjmn: drzm * dbpl
sllz: 4
pppw: cczh / lfqf
lgvd: ljgn * ptdq
drzm: hmdt - zczc
hmdt: 32
""".strip("\n")
)
f = open("  day21.txt  ".strip())
text = f.read()
m = re.findall(
    r"([a-z]+): (\d+)\s*|([a-z]+): ([a-z]+ [/\-\+\*] [a-z]+)\s*",
    text)
rr = dict(map(lambda a: (a[0], "( " + a[1] + " )"), map(lambda b: tuple(filter(lambda c: c != "", b)), m)))
root = rr["root"]
while re.search(r" [a-z]+ ", root):
    g = re.search(r" [a-z]+ ", root).group(0)
    root = root.replace(g, rr[g.strip()])


print(f"""
The value of root is {int(eval(root))}
""".strip())

root = rr["root"].replace("*", "=").replace("+", "=").replace("-", "=").replace("/", "=").replace("(", "").replace(")", "")
while re.search(r" [a-z]+ ", root):
    g = re.search(r" [a-z]+ ", root).group(0)
    root = root.replace(" humn ", " X ").replace(g, rr[g.strip()])

print(f"\nroot is:\n\n{root} \n")

print(f"""X shows up {root.count("X")} times in root""")

print("\nInterpolation time!!!\n")

p0 = (eval(root.split("=")[0].replace("X", "0")))
p1 = (eval(root.split("=")[0].replace("X", "1")))
q0 = (eval(root.split("=")[1].replace("X", "0")))
q1 = (eval(root.split("=")[1].replace("X", "1")))
print(f"""left  side: X = 0 => root = {(eval(root.split("=")[0].replace("X", "0")))}""")
print(f"""left  side: X = 1 => root = {(eval(root.split("=")[0].replace("X", "1")))}""")
print(f"""right side: X = 0 => root = {(eval(root.split("=")[1].replace("X", "0")))}""")
print(f"""right side: X = 1 => root = {(eval(root.split("=")[1].replace("X", "1")))}""")

print(f"""\nequation: p0 + (p1 - p0)X = q0 + (q1 - q0)X ... NOT!!! \n""")

X = Symbol("X")

print(f"""
The value of humn is {solve(root.replace("=", "-"))}
""".strip())
