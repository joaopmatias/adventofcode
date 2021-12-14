import numpy as np
from numpy.linalg import matrix_power
import pandas as pd
import string
import json
from collections import Counter
from functools import reduce, partial
from itertools import filterfalse


f = open("day14.txt", "r")
text = f.readlines()

template = text[0].strip()
rule = dict(map(lambda x: (tuple(x[0]), x[1]), map(partial(str.split, sep=" -> "), map(str.strip, text[2:]))))

polymer = template
for _ in range(10):
    polymer = "".join(map("".join, zip(polymer[:-1], map(rule.get, zip(polymer[:-1], polymer[1:]))))) + polymer[-1]
print("Length of polymer", len(polymer), "estimate", 2**10*(len(template) - 1) + 1)
freqs = Counter(polymer).values()
print("max freq", max(freqs), "min freq", min(freqs), "max - min", max(freqs) - min(freqs))

pi = dict(map(reversed, enumerate(rule.keys())))
m = np.zeros((len(pi), len(pi)), dtype=int)
for p, c in rule.items():
    m[pi[(p[0], c)], pi[p]] += 1
    m[pi[(c, p[1])], pi[p]] += 1

alphabet = dict(map(reversed, enumerate(string.ascii_uppercase)))
w = np.zeros((len(alphabet), len(pi)), dtype=int)
for p, c in pi.items():
    w[alphabet[p[0]], c] += 1
    w[alphabet[p[1]], c] += 1

v = np.array(list(map(Counter(map(pi.get, zip(template[:-1], template[1:]))).__getitem__, range(len(pi)))), dtype=int)
count = dict(zip(string.ascii_uppercase, ((matrix_power(m, 40).dot(v).dot(w.T) + (np.arange(len(alphabet)) == alphabet[template[0]]) + (np.arange(len(alphabet)) == alphabet[template[-1]]))//2).tolist()))

print(json.dumps(count, indent=2))
freqs = list(filter(bool, count.values()))
print("max freq", max(freqs), "min freq", min(freqs), "max - min", max(freqs) - min(freqs))
