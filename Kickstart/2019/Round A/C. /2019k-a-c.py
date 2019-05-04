# 2019 Kickstart Round A - C. 
# https://

from collections import deque, defaultdict as ddict
from functools import partial
from itertools import product
import sys
Int  = lambda: int(input())
Ints = lambda: list(map(int, input().split()))
Grid = lambda row, n_rows: [row() for _ in range(n_rows)]
Log  = partial(print, file=sys.stderr)

#------------------------------------------------------------------------------#

def solve(n, q, bookings):
    Log(n, q, bookings)

#------------------------------------------------------------------------------#

for i in range(Int()):
    n, q = Ints()
    bookings = Grid(Ints, q)
    result = solve(n, q, bookings)
    print('Case #{}:'.format(i+1), result)