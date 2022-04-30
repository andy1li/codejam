# 2022 Round 1B - A. Pancake Deque 
# https://codingcompetitions.withgoogle.com/codejam/round/000000000087711b/0000000000acd59d

import sys; sys.stdin = open('A. Pancake Deque/sample.in', 'r')

Int = lambda: int(input())
Ints = lambda: [*map(int, input().split())]

from collections import deque

#------------------------------------------------------------------------------#

def solve(n, ds):
    ans = d_max = 0
    while ds:
        d = ds.popleft() if ds[0] < ds[-1] else ds.pop()
        if d >= d_max: ans += 1
        d_max = max(d_max, d)
    return ans

#------------------------------------------------------------------------------#

for i in range(Int()):
    result = solve(Int(), deque(Ints()))
    print('Case #{}:'.format(i+1), result)