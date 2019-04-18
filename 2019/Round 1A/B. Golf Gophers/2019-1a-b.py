# 2019 Round 1A - B. Golf Gophers
# https://codingcompetitions.withgoogle.com/codejam/round/0000000000051635/0000000000104f1a

# python interactive_runner.py python testing_tool.py 1 -- python 2019-1a-b.py

from itertools import chain
import sys

def run(n, m):
    rs = [0] * 19
    for mod in range(12, 19):
        print(*[mod]*18, flush=True)
        rs[mod] = sum(map(int, input().split())) % mod

    for i in chain(range(1, 19), range(18+rs[18], m+1, 18)):
        ss = [i % mod for mod in range(12, 19)]
        if all(s == r for s, r in zip(ss, rs[12:])):
            print(i, flush=True)
            if input() == '1': break
            else:              sys.exit()

t, n, m = map(int, input().split())
for _ in range(t): run(n, m)