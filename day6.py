import pandas as pd
import numpy as np
from numpy.linalg import matrix_power
from collections import Counter

f = open("day6.txt")
initial = list(map(int, f.read().strip().split(",")))
print("Sample:", initial[:5])
m = np.zeros((9, 9), dtype=int)

for i in range(8):
    m[i, i+1] = 1
m[6, 0] = 1
m[8, 0] = 1

fish = np.zeros((9,), dtype=int)

for i, j in Counter(initial).items():
    fish[i] = j
print("Number of fish after 80 days:", matrix_power(m, 80).dot(fish).sum())
print("Number of fish after 256 days:", matrix_power(m, 256).dot(fish).sum())
