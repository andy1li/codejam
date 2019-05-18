# 2019 Round 2 - C. 
# https://

from collections import deque, defaultdict as ddict
from heapq       import heapify, heappush, heappop
from itertools   import product
Int   = lambda: int(input())
Ints  = lambda: [*map(int, input().split())]
Lines = lambda line, n_lines: [line() for _ in range(n_lines)]

#------------------------------------------------------------------------------#

def solve(n):
    return 0

#------------------------------------------------------------------------------#

for i in range(Int()):
    n = Int()
    result = solve(n)
    print('Case #{}:'.format(i+1), result)