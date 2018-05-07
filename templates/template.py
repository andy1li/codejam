# 201X Round X  - X. FOOBAR
# https://

from contextlib import contextmanager
import os
import sys

@contextmanager
def get_input():
    if '__LOCAL__' in os.environ:
        with open('sample.in') as f: yield f.readline
    else:
        yield input

################################################################################

def solve(n) -> int:
    return 0

################################################################################

with get_input() as input:
    for case in range(1, int(input())+1):
        n = int(input())
        result = solve(n)
        output = 'Case #%d: %s' %(case, result)
        print(output)