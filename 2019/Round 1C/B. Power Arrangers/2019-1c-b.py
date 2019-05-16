# 2019 Round 1C - B. Power Arrangers
# https://codingcompetitions.withgoogle.com/codejam/round/00000000000516b9/0000000000134e91

# python interactive_runner.py python testing_tool.py 1 -- python 2019-1c-b.py

from   collections import Counter
from   math        import factorial
import numpy as np
import sys
Ints = lambda: [*map(int, input().split())]

#------------------------------------------------------------------------------#

def run(f):
    grid = np.full([120, 5], '*')
    candidates = range(119)
    ans = [0] * 5

    for x in range(3): # until len(candidates) == 1
        for y in candidates:
            print(y*5 + x + 1)
            grid[y, x] = input()
        
        cnt = Counter(grid[:, x])
        ans[x] = next( hero
            for hero, c in cnt.items()
            if c == factorial(4-x) - 1 # 24-1, 6-1, 2-1
        )
        candidates = [ y 
            for y in candidates
            if grid[y, x] == ans[x]
        ]
        # print(len(candidates), candidates, file=sys.stderr)

    print(candidates[0]*5 + 4) # the 4th hero of the last candidate
    ans[4] = input()
    ans[3] = (set('ABCDE') - set(ans)).pop()
    
    print(''.join(ans))
    verdict = input()
    if verdict != 'Y': sys.exit()

t, f = Ints()
for _ in range(t): run(f)
