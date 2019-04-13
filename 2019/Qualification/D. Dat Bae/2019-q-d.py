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
    return np.array((tests * repeats)[:n])

def run():
    n, _, _ = map(int, input().split())
    tests = make_tests(n)
    # print('tests:', tests, file=sys.stderr)

    responses = []
    for test in tests.T:
        print(''.join(test), flush=True)
        responses.append(list(input()))
    responses = np.array(responses).T
    # print('responses:', responses, file=sys.stderr)

    ti = ri = 0; ans = []
    while ti < n:
        if (ri < len(responses) 
        and np.array_equal(tests[ti], responses[ri])): ri += 1
        else: ans.append(ti)
        ti += 1

    print(*ans, flush=True) 
    assert input() == '1'

for case in range(int(input())): run()
    