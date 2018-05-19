# Round 2 2018 - C. Costume Change
# https://codejam.withgoogle.com/2018/challenges/0000000000007706/dashboard/0000000000045875

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

def solve(n, grid) -> int:
    print(n, grid)

    return 0

#------------------------------------------------------------------------------#

with get_input() as input:
    num_cases = int(input())
    for case in range(1, num_cases+1):
        n = int(input())
        grid = [ [*map(int, input().split())]
            for _ in range(n)
        ]
        result = solve(n, grid)

        output = 'Case #%d: %s' %(case, result)
        print(output)
