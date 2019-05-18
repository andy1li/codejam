# 2019 Round 2 - B. Pottery Lottery
# https://codingcompetitions.withgoogle.com/codejam/round/0000000000051679/00000000001461c8

# python interactive_runner.py python testing_tool.py -- python 2019-2-b.py

from random import choice
import sys
Int  = lambda: int(input())
Ints = lambda: [*map(int, input().split())]

#------------------------------------------------------------------------------#

def run():
    vases = {}

    # 1-60: Give up on 1-15
    for v in list(range(1, 16)) * 4: input(); print(v, 1)
    
    # 61-80: Check all
    for v in range(1, 21):
        input(); print(v, 0)
        vases[v] = Ints()[1:]

    asc = sorted(vases.items(), key=lambda pair: len(pair[1]))
    candidates = asc[0][0], asc[1][0]
    cheats = asc[2:]

    # 81-94: Cheat to distinguish candidates
    for _ in range(81, 95):
        input(); print(cheats[0][0], 1)
        cheats[0][1].append(1)
        cheats = sorted(cheats, key=lambda pair: len(pair[1]))

    # 95-96: Check candidates
    for v in candidates:
        input(); print(v, 0)
        vases[v] = Ints()[1:]
    
    only_hope, cheat = sorted(candidates, key=lambda c: len(vases[c]))

    # 97-99: Cheat to distinguish the final candidate
    for _ in range(3): input(), print(cheat, 1)

    # 100: Hope for the best
    input(), print(only_hope, 100)

#------------------------------------------------------------------------------#

for i in range(Int()): run()