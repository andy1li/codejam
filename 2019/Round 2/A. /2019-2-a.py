# 2019 Round 2 - A. 
# https://

from collections import deque, defaultdict as ddict
from heapq       import heapify, heappush, heappop
from itertools   import product
Int   = lambda: int(input())
Ints  = lambda: [*map(int, input().split())]
Lines = lambda line, n_lines: [line() for _ in range(n_lines)]

#------------------------------------------------------------------------------#

def solve(n, molecules):
    print(n, molecules)
    return 0

#------------------------------------------------------------------------------#

for i in range(Int()):
    n = Int()
    molecules = Lines(Ints, n)
    result = solve(n, molecules)
    print('Case #{}:'.format(i+1), result)