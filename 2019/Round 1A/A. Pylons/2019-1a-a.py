# 2019 Round 1A - A. Pylons
# https://codingcompetitions.withgoogle.com/codejam/round/0000000000051635/0000000000104e03

from itertools import product
from math import ceil

def recurse(candidates, last, expected):
    ly, lx = last
    candidates -= set([last])
    for y, x in candidates:
        if y==ly or x==lx or x-y==lx-ly or x+y==lx+ly: continue
        moves = recurse(candidates, (y, x), expected-1)
        if len(moves) == expected-1: return [(y, x)] + moves
    return []

def solve(r, c):
    grid = set(product(range(1, r+1), range(1, c+1)))
    for y, x in product(range(ceil(r/2)), range(ceil(c/2))):
        move, expected = (y+1, x+1), r*c
        moves = recurse(grid, move, expected-1)
        if len(moves) == expected-1: return [move] + moves

#------------------------------------------------------------------------------#

for i in range(int(input())):
    r, c = map(int, input().split())
    result = solve(r, c)
    if not result:
        print('Case #{}:'.format(i+1), 'IMPOSSIBLE')
    else:
        print('Case #{}:'.format(i+1), 'POSSIBLE')
        for move in result: print(*move)