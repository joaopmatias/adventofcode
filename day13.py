from io import StringIO
from functools import cmp_to_key

import pandas as pd
import numpy as np

f = StringIO(
"""
[1,1,3,1,1]
[1,1,5,1,1]

[[1],[2,3,4]]
[[1],4]

[9]
[[8,7,6]]

[[4,4],4,4]
[[4,4],4,4,4]

[7,7,7,7]
[7,7,7]

[]
[3]

[[[]]]
[[]]

[1,[2,[3,[4,[5,6,7]]]],8,9]
[1,[2,[3,[4,[5,6,0]]]],8,9]
""".strip("\n")
)
f = open("  day13.txt  ".strip())

def right_order(left, right):
    q = [(left, right)]
    while len(q) > 0:
        left, right = q.pop()
        if isinstance(left, int) and isinstance(right, int):
            if left < right:
                return 1
            elif left > right:
                return -1
        elif isinstance(left, int) and isinstance(right, list):
            q.append(([left], right))
        elif isinstance(left, list) and isinstance(right, int):
            q.append((left, [right]))
        elif isinstance(left, list) and isinstance(right, list) and len(left) == 0 and len(right) == 0:
            pass
        elif isinstance(left, list) and isinstance(right, list) and len(left) == 0:
            return 1
        elif isinstance(left, list) and isinstance(right, list) and len(right) == 0:
            return -1
        elif isinstance(left, list) and isinstance(right, list):
            q.append((left[1:], right[1:]))
            q.append((left[0], right[0]))
        else:
            assert False, "invalid operation"
    return 0

packs = []
while True:
    packs.append(eval(f.readline()))
    packs.append(eval(f.readline()))
    if f.readline() != "\n":
        break

ans = []
for pair in zip(packs[0::2], packs[1::2]):
    ans.append(right_order(*pair) == 1)

print(f"""
The sum of the indexes of the pairs with right order is {(np.array(ans).nonzero()[0] + 1).sum()}
""".strip())

packs.append([[2]])
packs.append([[6]])

sorted_packs = [None] + sorted(packs, key=cmp_to_key(right_order), reverse=True)

print(f"""
The decoder key is {sorted_packs.index([[2]]) * sorted_packs.index([[6]])}
""".strip())
