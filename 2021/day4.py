
import pandas as pd
import numpy as np
from io import StringIO

f = open("day4.txt", "r")
numbers = list(map(int, ''.join(f.readline()).strip().split(",")))
print("Sample:", numbers[:5])

boards = []
while True:
    board = ''.join(f.readline() for _ in range(6)).strip().replace("  ", " ").replace("\n ", "\n")
    if not board:
        break
    boards.append(pd.read_csv(StringIO(board), sep=" ", header=None))

print("Sample:\n", boards[3])

stop = False
for x in numbers:
    if stop:
        break
    for df in boards:
        df.replace(x, -1, inplace=True)
        if any((df == -1).sum(axis=0) == 5) or any((df == -1).sum(axis=1) == 5):
            print("Winning board:\n", df)
            print("x=", x)
            unmarked = df.sum().sum() + (df == -1).sum().sum()
            print("Sum of unmarked numbers:", unmarked)
            print("Product is:", x * unmarked)
            stop = True
            
stop_df = None
stop_x = None
for x in numbers:
    for i, df in enumerate(boards):
        if df is not None:
            df.replace(x, -1, inplace=True)
            if any((df == -1).sum(axis=0) == 5) or any((df == -1).sum(axis=1) == 5):
                stop_df = df
                stop_x = x
                boards[i] = None
print("Last winning board:\n", stop_df)
print("x=", stop_x)
unmarked = stop_df.sum().sum() + (stop_df == -1).sum().sum()
print("Sum of unmarked numbers:", unmarked)
print("Product is:", stop_x * unmarked)
