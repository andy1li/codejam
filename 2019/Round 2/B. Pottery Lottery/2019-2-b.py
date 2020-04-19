# 2019 Round 2 - B. Pottery Lottery
# https://codingcompetitions.withgoogle.com/codejam/round/0000000000051679/00000000001461c8

# python interactive_runner.py python testing_tool.py -- python 2019-2-b.py

import sys
Int  = lambda: int(input())
Ints = lambda: [*map(int, input().split())]

#------------------------------------------------------------------------------#

def cnt_and_id(pair): return len(pair[1]), -pair[0]

def run():
    vases = {}

    # 1-60: Sabotage 75% (1-15)
    for vase in list(range(1, 16)) * 4: 
        input(); print(vase, 1)
    
    # 61-80: Check all 20
    for vase in range(1, 21):
        input(); print(vase, 0)
        vases[vase] = Ints()[1:]

    # Pick 2 candidates, and the rest will be victims
    cnt_asc = sorted(vases.items(), key=cnt_and_id)
    candidates, victims = dict(cnt_asc[:2]), cnt_asc[2:]

    # 81-94: Sabotage closest victims
    for _ in range(81, 95):
        input(); print(victims[0][0], 1)
        victims[0][1].append(1)
        victims = sorted(victims, key=cnt_and_id)

    # 95-96: Check candidates
    for vase in candidates:
        input(); print(vase, 0)
        candidates[vase] = Ints()[1:]
    
    bet, runner_up = sorted(candidates.items(), key=cnt_and_id)

    # 97-99: Sabotage the runner-up
    for _ in range(3): input(), print(runner_up[0], 1)

    # 100: Hope for the best
    input(), print(bet[0], 100)

#------------------------------------------------------------------------------#

for i in range(Int()): run()