# 2019 Round 1B - A. Manhattan Crepe Cart
# https://codingcompetitions.withgoogle.com/codejam/round/0000000000051706/000000000012295c

from itertools import accumulate
from collections import defaultdict, Counter, namedtuple
Int   = lambda: int(input())
Ints  = lambda: [*map(int, input().split())]
Lines = lambda line, n_lines: [line() for _ in range(n_lines)]

#------------------------------------------------------------------------------#

Person = namedtuple('Person', 'x y d')

def parse_person():
    x, y, d = input().split()
    return Person(int(x), int(y), d)

def d2v(x, y, d):
    if d == 'W': return x-1
    if d == 'E': return x+1
    if d == 'S': return y-1
    if d == 'N': return y+1

def solve(p, q, people):
    cnt = defaultdict(Counter)    
    for x, y, d in people:        
        cnt[d][d2v(x, y, d)] += 1

    xs = sorted(set(cnt['W'].keys()) | set(cnt['E'].keys())) #+ [10**6+1]
    ys = sorted(set(cnt['S'].keys()) | set(cnt['N'].keys())) #+ [10**6+1]

    es = [*accumulate(cnt['E'][x] for x in xs)]
    ws = [*accumulate(cnt['W'][x] for x in reversed(xs))][::-1]
    ns = [*accumulate(cnt['N'][y] for y in ys)]
    ss = [*accumulate(cnt['S'][y] for y in reversed(ys))][::-1]

    ans_x = ans_y = 0
    max_x = sum(cnt['W'].values()) 
    max_y = sum(cnt['S'].values()) 

    for x, e, w in zip(xs, es, ws):
        if e + w > max_x:
            ans_x, max_x = x, e+w

    for y, n, s in zip(ys, ns, ss):
        if n + s > max_y:
            ans_y, max_y = y, n+s

    return ans_x, ans_y

#------------------------------------------------------------------------------#

for i in range(Int()):
    p, q = Ints()
    people = Lines(parse_person, p)
    result = solve(p, q, people)
    print('Case #{}:'.format(i+1), *result)