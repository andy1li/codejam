# 2021 Kickstart Round A - B. L Shaped Plots
# https://codingcompetitions.withgoogle.com/kickstart/round/0000000000436140/000000000068c509

from collections import defaultdict
from itertools import groupby
Ints = lambda: [*map(int, input().split())]

#------------------------------------------------------------------------------#

def condense(r, c, grid):
    def intervals(line, i=0):
        for key, g in groupby(line):
            l = len(list(g))
            if key and l > 1: yield i, i+l
            i += l
            
    rows = [ list(intervals(row)) for row in grid ]
    cols = [ list(intervals(grid[i][j] for i in range(r))) for j in range(c) ]
    return rows, cols

def junctions(rows, cols):
    def junction(w, e, i, j):
        try:
            n, s = next((n, s) for n, s in cols[j] if n<=i<s)
            # print(i, j, (w, e), (n, s))
            return i-n+1, e-j, s-i, j-w+1 # N, E, S, W
        except StopIteration: return

    yield from (
        junction(w, e, i, j)
        for i, row in enumerate(rows)
        for w, e in row
        for j in range(w, e)
    )

def count(junction):
    if not junction: return 0
    junction += junction[0],
    return sum(
        max(0, min(a, b//2)-1) 
      + max(0, min(b, a//2)-1)
        for a, b in zip(junction, junction[1:])
    )

def solve(r, c, grid):
    rows, cols = condense(r, c, grid)
    return sum(map(count, junctions(rows, cols)))

#------------------------------------------------------------------------------#

for i in range(int(input())):
    r, c = Ints()
    grid = [Ints() for _ in range(r)]
    result = solve(r, c, grid)
    print('Case #{}:'.format(i+1), result)