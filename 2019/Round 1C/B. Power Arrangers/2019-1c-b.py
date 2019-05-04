# 2019 Round 1C - B. Power Arrangers
# https://codingcompetitions.withgoogle.com/codejam/round/00000000000516b9/0000000000134e91

# python interactive_runner.py python testing_tool.py 1 -- python 2019-1c-b.py

from collections import Counter
from math import factorial
import numpy as np
import sys
Ints  = lambda: [*map(int, input().split())]
Lines = lambda line, n_lines: [line() for _ in range(n_lines)]

#------------------------------------------------------------------------------#

def run(f):
    grid = np.full([120, 5], '_')    
    candidates = set(range(119))

    ans = [0] * 5
    for x in range(3): # until len(candidates) == 1
        for y in candidates:
            print(y*5 + x + 1)
            grid[y, x] = input()
        cnt = Counter(grid[:, x])

        ans[x] = next( hero
            for hero, c in cnt.items()
            if c == factorial(4-x) - 1
        )

        for y in candidates.copy():
            if grid[y, x] != ans[x]: candidates.remove(y)
        # print(len(candidates), candidates, file=sys.stderr)

    y = candidates.pop()
    print(y*5 + 4) # the 4th hero of the last candidate
    ans[4] = input()
    ans[3] = (set('ABCDE') - set(ans)).pop()
    
    print(''.join(ans))
    verdict = input()
    if verdict != 'Y': sys.exit()


t, f = map(int, input().split())
for _ in range(t): run(f)
