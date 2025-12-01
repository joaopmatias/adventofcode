
from io import StringIO
from collections import Counter

import pandas as pd
import numpy as np

f = StringIO(
"""

32T3K 765
T55J5 684
KK677 28
KTJJT 220
QQQJA 483

""".strip("\n")
)
f = open("  day07.txt  ".strip())

ordered_cards = "A, K, Q, J, T, 9, 8, 7, 6, 5, 4, 3, 2".split(", ")[::-1]
hands = []
for line in f:
    hand, bid = line.strip().split(" ")
    hands.append((
        *sorted(Counter(hand).values(), reverse=True), 
        *(ordered_cards.index(c) for c in hand),
        int(bid),
    ))

ans = sum((i * j[-1] for i, j in enumerate(sorted(hands), start=1)))

print(f"""
The solution is {ans}
""".strip())

print()

f = StringIO(
"""

32T3K 765
T55J5 684
KK677 28
KTJJT 220
QQQJA 483

""".strip("\n")
)
f = open("  day07.txt  ".strip())

ordered_cards = "A, K, Q, T, 9, 8, 7, 6, 5, 4, 3, 2, J".split(", ")[::-1]
hands = []
for line in f:
    hand, bid = line.strip().split(" ")
    hands.append((
        max(Counter(hand.replace("J", "")).values() or [0]) + hand.count("J"),
        *sorted(Counter(hand.replace("J", "")).values(), reverse=True)[1:], 
        *(ordered_cards.index(c) for c in hand),
        int(bid),
    ))

ans = sum((i * j[-1] for i, j in enumerate(sorted(hands), start=1)))

print(f"""
The solution is {ans}
""".strip())