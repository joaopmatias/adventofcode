import re
from copy import deepcopy
from io import StringIO
from pathlib import Path

import pandas as pd
import numpy as np

"""
cd x
cd ..
cd /
ls

system is
{
    path: size
}
"""



f = StringIO(
"""
$ cd /
$ ls
dir a
14848514 b.txt
8504156 c.dat
dir d
$ cd a
$ ls
dir e
29116 f
2557 g
62596 h.lst
$ cd e
$ ls
584 i
$ cd ..
$ cd ..
$ cd d
$ ls
4060174 j
8033020 d.log
5626152 d.ext
7214296 k
""".strip("\n\r")
)
f = open("  day07.txt  ".strip())

commands = list(map(lambda w: w.strip("\n").split("\n"), ("\n" + f.read()).split("\n$ ")[1:]))
computer = {Path("/"): None}
wd = None

for cmd in commands:
    if cmd[0] == "cd /":
        wd = Path("/")
    elif cmd[0] == "cd ..":
        wd = wd.parent
    elif cmd[0][:3] == "cd ":
        wd /= cmd[0][3:]
    elif cmd[0] == "ls":
        for l in cmd[1:]:
            regex = re.match(r"^(\S+) (.*)$", l)
            n, sub = regex.group(1), regex.group(2)
            if not wd / sub in computer:
                computer[wd / sub] = None if n == "dir" else int(n)
    else:
        assert False, "invalid command"

computer0 = deepcopy(computer)
        
for p in sorted(list(computer0.keys()), reverse=True)[:-1]:
    computer0[p.parent] = (computer0[p.parent] or 0) + computer0[p]

print(f"""
The sum of the sizes of the files/folders below 100000: {sum([s for p, s in computer0.items() if s <= 100000 and computer[p] is None])}
""".strip())

70000000
30000000
40_000_000

ans = None
if computer0[Path("/")] <= 40_000_000:
    print(f"""
    The size of the deleted file is {0}
    """.strip())
else:
    print(f"""
    The size of the deleted file is {min([s for p, s in computer0.items() if computer0[Path("/")] - computer0[p] <= 40_000_000 and computer[p] is None])}
    """.strip())
    