import numpy as np
import pandas as pd
import json
from functools import reduce, partial
from itertools import product, starmap
from copy import deepcopy

f = open("day18.txt", "r")

def pretty(w):
    if isinstance(w, int):
        return w
    else:
        return [pretty(w[0]), pretty(w[1])]

def parse(w):
    w = json.loads(w.strip("\n "))
    for a in w:
        if isinstance(a, list):
            for b in a:
                if isinstance(b, list):
                    for c in b:
                        if isinstance(c, list):
                            for d in c:
                                if isinstance(d, list):
                                    d.append(c)
                            c.append(b)
                    b.append(a)
            a.append(w)
    w.append(None)
    return w

def explode(d):
    # explode left
    e = d
    while e[2] is not None and id(e) == id(e[2][0]):
        e = e[2]
    if e[2] is None:
        pass
    elif isinstance(e[2][0], int):
        e[2][0] += d[0]
    else:
        e = e[2][0]
        while isinstance(e[1], list):
            e = e[1]
        e[1] += d[0]
    # explode right
    e = d
    while e[2] is not None and id(e) == id(e[2][1]):
        e = e[2]
    if e[2] is None:
        pass
    elif isinstance(e[2][1], int):
        e[2][1] += d[1]
    else:
        e = e[2][1]
        while isinstance(e[0], list):
            e = e[0]
        e[0] += d[1]
    if id(d) == id(d[2][0]):
        d[2][0] = 0
    elif id(d) == id(d[2][1]):
        d[2][1] = 0
    else:
        raise ValueError("Screwed up...")

def wrap_explode(w):
    for a in w[:2]:
        if isinstance(a, list):
            for b in a[:2]:
                if isinstance(b, list):
                    for c in b[:2]:
                        if isinstance(c, list):
                            for d in c[:2]:
                                if isinstance(d, list):
                                    explode(d)
                                    return True
    return False

def wrap_split(w):
    for a in w[:2]:
        if isinstance(a, int) and a >= 10:
            if a == w[0]:
                w[0] = [a // 2, (a + 1) // 2, w]
            elif a == w[1]:
                w[1] = [a // 2, (a + 1) // 2, w]
            return True
        elif isinstance(a, list) and wrap_split(a):
            return True
    return False

def reduce_(x):
    while True:
        if wrap_explode(x):
            pass
            #print(1, pretty(x))
        elif wrap_split(x):
            pass
            #print(2, pretty(x))
        else:
            return x

def add_n_reduce(x, y):
    x = deepcopy(x)
    y = deepcopy(y)
    ans = [reduce_(x), reduce_(y), None]
    ans[0][2] = ans
    ans[1][2] = ans
    return reduce_(ans)

def magnitude(l):
    if isinstance(l, int):
        return l
    else:
        return 3 * magnitude(l[0]) + 2 * magnitude(l[1])

snails = list(map(parse, f))

print("magnitude", magnitude(reduce(add_n_reduce, snails)))

print("max magnitude", max(map(lambda x: magnitude(add_n_reduce(*x)), product(snails, snails))))
