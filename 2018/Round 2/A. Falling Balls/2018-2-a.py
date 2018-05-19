# Round 2 2018 - A. Falling Balls
# https://codejam.withgoogle.com/2018/challenges/0000000000007706/dashboard

from contextlib import contextmanager
from itertools  import count
import os

@contextmanager
def get_input():
    if '__LOCAL__' in os.environ:
        with open('sample.in') as f: yield f.readline
    else:
        yield input

#------------------------------------------------------------------------------#

def get_sections(counts):
    start = 0
    for idx, cnt in enumerate(counts):
        if cnt > 0:
            end = start+cnt-1
            yield (idx, start, end)
            start += cnt

def solve(n, counts) -> str:
    # print(n, counts)
    if not counts[0] or not counts[-1]: return 'IMPOSSIBLE'
    
    grid = [ ['.'] * n 
        for _ in range(98)
    ]

    for idx, start, end in get_sections(counts):
        for row, col in zip(count(), range(start, idx)):            
            grid[row][col] = '\\'
        for row, col in zip(count(), range(end, idx, -1)):
            grid[row][col] = '/'

    grid = [*filter(
        lambda row: row != ['.'] * n,
        grid
    )]
    grid.append(['.'] * n)

    return str(len(grid)) + '\n' + '\n'.join(
        ''.join(row) for row in grid
    )

#------------------------------------------------------------------------------#

with get_input() as input:
    for case in range(1, int(input())+1):
        n = int(input())
        counts = [*map(int, input().split())]
        result = solve(n, counts)
        output = 'Case #%d: %s' %(case, result)
        print(output)