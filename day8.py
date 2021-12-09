import pandas as pd
import numpy as np
from itertools import permutations
from functools import partial
from io import StringIO

with open("day8.txt", "r") as f:
    print("Number of 1, 4, 7, 8:", sum(len(x) in {2, 3, 4, 7} for line in f for x in line.split("|")[1].strip().split(" ")))

digits = {
    0: {0, 1, 2, 4, 5, 6},
    1: {2, 5},
    2: {0, 2, 3, 4, 6},
    3: {0, 2, 3, 5, 6},
    4: {1, 2, 3, 5},
    5: {0, 1, 3, 5, 6},
    6: {0, 1, 3, 4, 5, 6},
    7: {0, 2, 5},
    8: {0, 1, 2, 3, 4, 5, 6},
    9: {0, 1, 2, 3, 5, 6},
}
l_digits = list(zip(*sorted(digits.items())))[1]
print("Sample:\n", list(l_digits))
eligible = list(map(dict, map(partial(zip, tuple("abcdefg")), permutations(range(7)))))
print("Sample:\n", eligible[:5])
ans = 0
test = """be cfbegad cbdgef fgaecd cgeb fdcge agebfd fecdb fabcd edb | fdgacbe cefdb cefbgd gcbe
edbfga begcd cbg gc gcadebf fbgde acbgfd abcde gfcbed gfec | fcgedb cgb dgebacf gc
fgaebd cg bdaec gdafb agbcfd gdcbef bgcad gfac gcb cdgabef | cg cg fdcagb cbg
fbegcd cbd adcefb dageb afcb bc aefdc ecdab fgdeca fcdbega | efabcd cedba gadfec cb
aecbfdg fbg gf bafeg dbefa fcge gcbea fcaegb dgceab fcbdga | gecf egdcabf bgf bfgea
fgeab ca afcebg bdacfeg cfaedg gcfdb baec bfadeg bafgc acf | gebdcfa ecba ca fadegcb
dbcfg fgd bdegcaf fgec aegbdf ecdfab fbedc dacgb gdcebf gf | cefg dcbef fcge gbcadfe
bdfegc cbegaf gecbf dfcage bdacg ed bedf ced adcbefg gebcd | ed bcgafe cdgba cbgef
egadfb cdbfeg cegd fecab cgb gbdefca cg fgcdab egfdb bfceg | gbdfcae bgc cg cgb
gcafb gcf dcaebfg ecagb gf abcdeg gaef cafbge fdbac fegbdc | fgae cfgab fg bagce"""
# with StringIO(test) as f:
with open("day8.txt", "r") as f:
    for line in f:
        for candidate in eligible:
            stop = False
            for v in line.split("|")[0].strip().split(" "):
                if set(map(candidate.get, v)) not in l_digits:
                    stop = True
                    break
            if stop:
                continue
            else:
                ans += int(''.join(
                    map(
                        str,
                        map(
                            l_digits.index, 
                            map(
                                set, 
                                map(
                                    partial(map, candidate.get),
                                    line.split("|")[1].strip().split(" "),
                                )
                            )
                        )
                    )
                ))
                break
print("Sum:", ans)
