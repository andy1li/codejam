# 2019 Round 1B - B. Draupnir
# https://codingcompetitions.withgoogle.com/codejam/round/0000000000051706/0000000000122837

# python interactive_runner.py python testing_tool.py 1 -- python 2019-1b-b.py

import sys

def run(w):
    print(w, file=sys.stderr)
    sys.exit()

t, w = map(int, input().split())
for _ in range(t): run(w)