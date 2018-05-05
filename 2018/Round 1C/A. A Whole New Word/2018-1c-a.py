# Round 1C 2018 - A. A Whole New Word 
# https://codejam.withgoogle.com/2018/challenges/0000000000007765/dashboard

from collections import Counter
from functools import reduce
from itertools import product
from operator import mul

def filter_min(c):
    min_val = min(c.values())
    return [k 
        for k, v in  c.items()
        if v == min_val
    ]

def solve(n, rows, cols) -> str: 
    max_num = reduce(mul, map(len, cols))
    if n == max_num: return '-'
    # print(n, rows, cols, max_num)

    counts = map(Counter, cols)
    # print(*counts)
    min_letters = [*map(filter_min, counts)]

    for x in product(*min_letters):
        word = ''.join(x)
        if word not in rows:
            return word

    raise RuntimeError
            
### Remember to delete tests and scaffolding before submission
file = open('sample.in')
input = file.readline

num_cases = int(input())
for case in range(1, num_cases+1):
    n, l = map(int, input().split())
    rows = set(input().strip() for _ in range(n))
    cols = [*map(set, zip(*rows))]
    result = solve(n, rows, cols)

    output = 'Case #%s: %s' %(case, result)
    print(output)

file.close()
