from io import StringIO

import pandas as pd
import numpy as np

f = StringIO(
"""

1abc2
pqr3stu8vwx
a1b2c3d4e5f
treb7uchet

""".strip("\n")
)
f = open("  day01.txt  ".strip())

ans = 0
for l in f:
    numbers = [c for c in l if c.isdigit()]
    ans += int(f"{numbers[0]}{numbers[-1]}")

print(f"""
The sum of all calibration values is {ans}
""".strip())

print()

f = StringIO(
"""

two1nine
eightwothree
abcone2threexyz
xtwone3four
4nineeightseven2
zoneight234
7pqrstsixteen

""".strip("\n")
)
f = open("  day01.txt  ".strip())

ans = 0
for l in f:
    ll = (
        l
        .replace("one", "one 1 one")
        .replace("two", "two 2 two")
        .replace("three", "three 3 three")
        .replace("four", "four 4 four")
        .replace("five", "five 5 five")
        .replace("six", "six 6 six")
        .replace("seven", "seven 7 seven")
        .replace("eight", "eight 8 eight")
        .replace("nine", "nine 9 nine")
        .replace(" ", "")
    )
    numbers = [c for c in ll if c.isdigit()]
    ans += int(f"{numbers[0]}{numbers[-1]}")

print(f"""
The sum of all calibration values in part 2 is {ans}
""".strip())
