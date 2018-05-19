# Round 2 2018 - D. Gridception 
# https://codejam.withgoogle.com/2018/challenges/0000000000007706/dashboard/00000000000459f4

from contextlib import contextmanager
import os

@contextmanager
def get_input():
    if '__LOCAL__' in os.environ:
        with open('sample.in') as file:
            yield file.readline
    else:
        yield input

#------------------------------------------------------------------------------#

def solve(r, c, grid) -> int:
    print(r, c, grid)

    return 0

#------------------------------------------------------------------------------#

with get_input() as input:
    num_cases = int(input())
    for case in range(1, num_cases+1):
        r, c = map(int, input().split())
        grid = [ list(input().strip())
            for _ in range(r)
        ]
        result = solve(r, c, grid)

        output = 'Case #%d: %s' %(case, result)
        print(output)
