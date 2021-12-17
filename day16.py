"""
type 4 is a single packet (a number)

look for type id if type is not 4

type id 0 is total length of all subpackets given by 15 bits 

type id 1 is number of immediate subpackets given by 11 bits

00111000000000000110111101000101001010010001001000000000
VVVTTTILLLLLLLLLLLLLLLAAAAAAAAAAABBBBBBBBBBBBBBBB

version 3 bits

type 3 bits
"""

import numpy as np
import pandas as pd
from collections import namedtuple
from itertools import count
from operator import mul, lt, gt, eq
from functools import partial, reduce

"""
tuple

(version, (type, type id, the other number), (subpackets and, if literal, a number))

sum all versions... recursive tail, easy
"""

f = open("day16.txt", "r")
packet = format(int(f.read().strip(), 16), "b")

print("Length of packet:", len(packet))


"""
Parse

N, Tree, Tree, Tree, string
"""

Packet = namedtuple("Packet", ["version", "typeid", "lentypeid", "extra", "items", "rest"])

def s(packet):
    if isinstance(packet, Packet):
        return (packet.version or 0) + sum(map(s, packet.items))
    else:
        return 0

def parse(packet):
    if packet.extra == 0 or packet.rest == "":
        return packet
    else:
        version = int(packet.rest[:3], 2)
        typeid = int(packet.rest[3:6], 2)
        if typeid == 4:
            lentypeid = None
            extra = 0
            literal = []
            for a, b in zip(count(7, step=5), count(11, step=5)):
                literal.append(packet.rest[a:b])
                if packet.rest[a - 1] == "0":
                    break
            items = [int("".join(literal), 2)]
            rest = ""
            p = parse(Packet(version, typeid, lentypeid, extra, items, rest))
            packet.items.append(p)
            return parse(packet._replace(extra=packet.extra - 1, rest=packet.rest[b:]))
        else:
            lentypeid = int(packet.rest[6])
            if lentypeid == 0:
                extra = np.inf
                items = []
                rest = packet.rest[22:][:int(packet.rest[7:22], 2)]
                p = parse(Packet(version, typeid, lentypeid, extra, items, rest))
                packet.items.append(p)
                return parse(packet._replace(extra=packet.extra - 1, rest=packet.rest[22:][int(packet.rest[7:22], 2):]))
            else:
                extra = int(packet.rest[7:18], 2)
                items = []
                rest = packet.rest[18:]
                p = parse(Packet(version, typeid, lentypeid, extra, items, rest))
                packet.items.append(p._replace(rest=""))
                return parse(packet._replace(extra=packet.extra - 1, rest=p.rest))

pp = parse(Packet(None, None, None, 1, [], packet))

print("Sum of versions:", s(pp))

"""
0, sum
1, product
2, min
3, max
4, literal
5, two sub-packets, first > second is 1 else is 0
6, two sub-packets, first < second is 1 else is 0
7, two sub-packets, first == second is 1 else is 0
"""

typefcns = {
    0: sum,
    1: partial(reduce, mul),
    2: min,
    3: max,
    4: lambda x: int(*x),
    5: lambda x: int(gt(*x)),
    6: lambda x: int(lt(*x)),
    7: lambda x: int(eq(*x)),
}

def compute(packet):
    if isinstance(packet, int):
        return packet
    else:
        return typefcns[packet.typeid](map(compute, packet.items))

print("Value of packet:", compute(pp.items[0]))
