import pandas as pd

df = pd.read_csv("day1.csv", names=["values"])
print(df.shift(1).head())
ans = ((df - df.shift(1)) > 0).sum()[0]
print(f"The value increases {ans} times")

print("\n second \n")

print(df.rolling(3).sum().shift(-2).tail())

ans = ((df.rolling(3).sum().shift(-2) - df.rolling(3).sum().shift(-1)) > 0).sum()[0]
print(f"The value increases {ans} times")
