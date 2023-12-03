from io import StringIO

import pandas as pd
import numpy as np

f = StringIO(
"""
addx 15
addx -11
addx 6
addx -3
addx 5
addx -1
addx -8
addx 13
addx 4
noop
addx -1
addx 5
addx -1
addx 5
addx -1
addx 5
addx -1
addx 5
addx -1
addx -35
addx 1
addx 24
addx -19
addx 1
addx 16
addx -11
noop
noop
addx 21
addx -15
noop
noop
addx -3
addx 9
addx 1
addx -3
addx 8
addx 1
addx 5
noop
noop
noop
noop
noop
addx -36
noop
addx 1
addx 7
noop
noop
noop
addx 2
addx 6
noop
noop
noop
noop
noop
addx 1
noop
noop
addx 7
addx 1
noop
addx -13
addx 13
addx 7
noop
addx 1
addx -33
noop
noop
noop
addx 2
noop
noop
noop
addx 8
noop
addx -1
addx 2
addx 1
noop
addx 17
addx -9
addx 1
addx 1
addx -3
addx 11
noop
noop
addx 1
noop
addx 1
noop
noop
addx -13
addx -19
addx 1
addx 3
addx 26
addx -30
addx 12
addx -1
addx 3
addx 1
noop
noop
noop
addx -9
addx 18
addx 1
addx 2
noop
noop
addx 9
noop
noop
noop
addx -1
addx 2
addx -37
addx 1
addx 3
noop
addx 15
addx -21
addx 22
addx -6
addx 1
noop
addx 2
addx 1
noop
addx -10
noop
noop
addx 20
addx 1
addx 2
addx 2
addx -6
addx -11
noop
noop
noop
""".strip("\n")
)
f = open("  day10.txt  ".strip())

crt = (
    pd.read_csv(f, sep=" ", header=None, names=["op", "value"])
    .fillna(0)
    .assign(next_cycle=lambda df: (df["op"] == "addx") + 1)
    .assign(next_cycle=lambda df: np.cumsum(df["next_cycle"]).astype(int) + 1)
    .pipe(lambda df: pd.concat((
        pd.DataFrame({"op": "", "value": 1, "next_cycle": 1}, index=[0]),
        df)))
    .assign(register=lambda df: np.cumsum(df["value"]).astype(int))
    .reset_index(drop=True)
)

signal = (
    crt
    .assign(forty=lambda df: ((20 - df["next_cycle"]) // 40).abs() * 40 + 20)
    .groupby(by="forty", as_index=False)
    .last()
    .pipe(lambda df: df if df["next_cycle"].iloc[-1] ==  df["forty"].iloc[-1] else df.iloc[:-1])
    .assign(ss=lambda df: df["register"] * df["forty"])
)

print(f"""
The sum of the signal strengths is {signal["ss"].sum()}
""".strip())

print()

print(f"""
The secret message in the crt is...
""".strip())

(
    crt
    [["next_cycle", "register"]]
    .set_index("next_cycle")
    .pipe(
        lambda df:
        pd.concat((
            df,
            pd.DataFrame(index=pd.Index(range(1, df.index[-1]), name="next_cycle")))))
    .groupby("next_cycle")
    .first()
    .fillna(method="ffill")
    .astype(int)
    .assign(position=lambda df: (df.index - 1) % 40)
    .assign(pixel=lambda df: ((df["register"] - df["position"]).abs().apply(lambda x: "#" if x <= 1 else ".")))
    .assign(line=lambda df: (df.index - 1) // 40)
    .groupby(by="line")
    ["pixel"]
    .agg("".join)
    .pipe(lambda s: print(*s, sep="\n"))
)
