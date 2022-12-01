import numpy as np
import pandas as pd
from functools import partial
from operator import add
from itertools import groupby

f = open("day12.txt", "r")
edges_in = list(map(partial(str.split, sep="-"), map(str.strip, f)))
caves = dict(map(reversed, enumerate(sorted(list(set(add(*zip(*edges_in)))), reverse=True))))
print("Caves:", caves)
print("start:", caves["start"])
print("end:", caves["end"])
edges = sorted(list(map(tuple, map(partial(map, caves.get), add(edges_in, list(map(reversed, edges_in)))))))
graph = dict(map(lambda x: (x[0], list(map(lambda y: y[1], x[1]))), groupby(edges, lambda x: x[0])))
print("Graph:", graph)

solns = []
q = [(2, ())]
while len(q) > 0:
    node, path = q.pop()
    if node < 8 and node in path:
        pass
    elif node == 6:
        solns.append(path + (node,))
    else:
        for later in graph[node]:
            q.append((later, path + (node,)))
print("Number of paths:", len(solns))

solns = []
q = [(2, ((), False))]
i = 0
while len(q) > 0:
    node, acc = q.pop()
    path, any_repeat = acc
    if node == 6:
        solns.append(path + (node,))
    elif node in path and node < 8:
        if node == 2:
            pass
        elif any_repeat:
            pass
        else:
            for later in graph[node]:
                q.append((later, (path + (node,), True)))
    else:
        for later in graph[node]:
            q.append((later, (path + (node,), any_repeat)))
print("Number of paths:", len(solns))
