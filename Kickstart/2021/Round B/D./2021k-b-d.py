# 2021 Kickstart Round B - D. Truck Delivery
# https://codingcompetitions.withgoogle.com/kickstart/round/0000000000435a5b/000000000077a885

from collections import defaultdict
import numpy as np

Int = lambda: int(input())
Ints = lambda: [*map(int, input().split())]

#------------------------------------------------------------------------------#

def prepare(roads):
    E, G = {}, defaultdict(set)
    for x, y, l, a in roads:
        E[frozenset([x, y])] = l, a
        G[x].add(y); G[y].add(x)
    P, tree, seen, = {},  [1], set()
    for node in tree:
        seen.add(node)
        for nbr in G[node]:
            if nbr not in seen:
                P[nbr] = node
                tree.append(nbr)
    return E, P

# def solve_small(N, Q, roads, queries):
#     from functools import lru_cache
#     import sys; sys.setrecursionlimit(10**5)

#     @lru_cache(None)
#     def get_path(q):
#         if q == 1: return ()
#         p = P[q]
#         edge = frozenset([p, q])
#         return get_path(p) + (E[edge],)

#     def gcd(q_w):
#         q, w = q_w
#         ans = [ a for l, a in get_path(q) if w >= l ]
#         return np.gcd.reduce(ans) if ans else 0

#     E, P = prepare(roads)        
#     return map(gcd, queries)

def solve_small(N, Q, roads, queries):
    E, P = prepare(roads)
    ans = []
    for q, w in queries:
        A = []
        while True:
            p = P[q]
            l, a = E[frozenset([p, q])]
            if w >= l: A.append(a)
            if p == 1: break
            q = p
        ans.append( np.gcd.reduce(A) if A else 0 )
    return ans

#------------------------------------------------------------------------------#

for i in range(Int()):
    N, Q = Ints()
    roads = [Ints() for _ in range(N-1)]
    queries = [Ints() for _ in range(Q)]
    result = solve_small(N, Q, roads, queries)
    print('Case #{}:'.format(i+1), *result)