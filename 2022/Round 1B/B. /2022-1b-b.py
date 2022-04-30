# 2022 Round 1B - B. Controlled Inflation
# https://codingcompetitions.withgoogle.com/codejam/round/000000000087711b/0000000000accfdb

import sys; sys.stdin = open('B. Controlled Inflation/sample.in', 'r')

Int = lambda: int(input())
Ints = lambda: [*map(int, input().split())]

from collections import defaultdict
from itertools import permutations
from functools import lru_cache

#------------------------------------------------------------------------------#

def n_presses(prev, curr):
    xs = (prev,) + curr
    return sum(abs(a-b) for a, b, in zip(xs, xs[1:]))

def solve(customers):
    end = defaultdict(set, {-1: [0]})
    dp = { (-1, 0): 0 } # (i, prev): val
    
    for i, customer in enumerate(customers):
        for perm in permutations(customer):
            for e in end[i-1]:
                dp[i, perm[-1]] = min(
                    dp.get((i, perm[-1]), float('inf')),
                    dp[i-1, e] + n_presses(e, perm)
                )
                end[i].add(perm[-1])

    return min(dp[len(customers)-1, e] for e in end[len(customers)-1])
    
   
#------------------------------------------------------------------------------#

for i in range(Int()):
    n, p = Ints()
    grid = [Ints() for _ in range(n)]
    result = solve(grid)
    print('Case #{}:'.format(i+1), result)