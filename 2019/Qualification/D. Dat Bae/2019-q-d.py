# 2019 Qualification Round - D. Dat Bae
# https://codingcompetitions.withgoogle.com/codejam/round/0000000000051705/00000000000881de

# python interactive_runner.py python testing_tool.py 1 -- python 2019-q-d.py

from math import ceil
import numpy as np
import sys

def to_binary(x): return list(bin(x)[2:].zfill(5))

def to_str(x): return ''.join(x)

def make_tests(n):
    tests = [*map(to_binary, range(32))]
    repeats = ceil(n/32)
    return np.array((tests * repeats)[:n]).T

def run():
    n, _, _ = map(int, input().split())
    tests = make_tests(n)

    responses = []
    for row in tests:
        print(''.join(row), flush=True)
        responses.append(list(input()))

    tests = [*map(to_str, tests.T)]
    responses = [*map(to_str, np.array(responses).T)]

    ti = ri = 0; ans = []    
    while ti < n:
        if ri < len(responses) and tests[ti] == responses[ri]: ri += 1
        else: ans.append(ti)
        ti += 1 

    print(*ans, flush=True)
    verdict = input()
    assert verdict == '1'

for case in range(int(input())): run()
    