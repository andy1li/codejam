# 2020 Round 1B - B. Blindfolded Bullseye
# https://codingcompetitions.withgoogle.com/codejam/round/000000000019fef2/00000000002d5b63

# python interactive_runner.py python testing_tool.py 2 -- python 2020-1b-b.py

from bisect import bisect_left as search
import sys

BILLION = 10**9

def get_input():
    res = input()
    if res == 'CENTER': raise StopIteration
    return res

def c(point): return point[0]-BILLION, point[1]-BILLION

def start_points(candiates, l):
    while True:
        yield from candiates
        candiates = [ c
            for x, y in candiates
            for c in [(x+l, y+l), (x-l, y+l), (x+l, y-l), (x-l, y-l)]
        ]
        l //= 2

def solve(cx, cy):
    class Wall: 
        def __init__(self, target, dir):
            self.target = target
            self.dir = dir

        def __getitem__(self, i):
            candidate = (i, cy) if self.dir == 'H' else (cx, i)
            print(*c(candidate))
            return get_input() == self.target
    
    wall = Wall('HIT', 'H')
    L = search(wall, True, max(0, cx-BILLION), cx)

    wall.target = 'MISS'
    R = search(wall, True, cx, min(2*BILLION, cx+BILLION)) - 1
    x = (L + R) // 2

    wall.dir = 'V'
    T = search(wall, True, cy, min(2*BILLION, cy+BILLION)) - 1
    
    wall.target = 'HIT'
    B = search(wall, True, max(0, cy-BILLION), cy) 
    y = (T + B) // 2

    print('center:', *c((x, y)), file=sys.stderr)
    return c((x, y))

T, A, B = map(int, input().split())
for _ in range(T): 
    for candiate in start_points([(BILLION, BILLION)], BILLION//2):
        try:
            # print('try:', *c(candiate), file=sys.stderr)
            print(*c(candiate))
            if get_input() == 'HIT':
                print(*solve(*candiate))
                get_input()
                sys.exit() # if get_input() != 'CENTER'
        except StopIteration: break
