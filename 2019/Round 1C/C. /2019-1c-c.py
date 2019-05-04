# 2019 Round 1C - C. Bacterial Tactics 
# https://codingcompetitions.withgoogle.com/codejam/round/00000000000516b9/0000000000134cdf

from collections import deque, defaultdict as ddict
from heapq       import heapify, heappush, heappop
from itertools   import product
Int   = lambda: int(input())
Ints  = lambda: [*map(int, input().split())]
Lines = lambda line, n_lines: [line() for _ in range(n_lines)]

#------------------------------------------------------------------------------#

def solve(r, c, grid):
    print(r, c, grid)
    for y, row in enumerate(grid):
        for x, cell in enumerate(row):
            print(y, x, cell)
    return 0

#------------------------------------------------------------------------------#

for i in range(Int()):
    r, c  = Ints()
    grid = Lines(input, r)
    result = solve(r, c, grid)
    print('Case #{}:'.format(i+1), result)