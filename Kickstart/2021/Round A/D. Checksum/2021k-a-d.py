# 2021 Kickstart Round A - D. Checksum
# https://codingcompetitions.withgoogle.com/kickstart/round/0000000000436140/000000000068c2c3

from collections import defaultdict
from itertools import product
Ints = lambda: [*map(int, input().split())]

#------------------------------------------------------------------------------#

def solve(n, A, B):
    ans, G = 0, defaultdict(dict)
    for i, j in product(range(n), repeat=2):
        if A[i][j] == -1:
            ans += B[i][j]
            G[n+j][i] = G[i][n+j] = B[i][j]

    mst, max_ = set(), {v : (0, None) for v, edge in G.items()}
    unvisited = lambda item: item[0] not in mst
    by_cost = lambda item: item[1][0]
    for _ in range(len(G)):
        v, (cost, u) = max(filter(unvisited, max_.items()), key=by_cost)
        mst.add(v)
        if u is not None: ans -= cost
        
        for u, cost in G[v].items():
            if cost > max_[u][0]:
                max_[u] = cost, v

    return ans

#------------------------------------------------------------------------------#

for i in range(int(input())):
    n = int(input())
    A = [Ints() for _ in range(n)]
    B = [Ints() for _ in range(n)]
    _, _ = input(), input()
    result = solve(n, A, B)
    print('Case #{}:'.format(i+1), result)
