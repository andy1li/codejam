# 2022 Round 1C - B. Squary 
# https://codingcompetitions.withgoogle.com/codejam/round/0000000000877b42/0000000000afdf76

import sys; sys.stdin = open('B. Squary/sample.in', 'r')

Int = lambda: int(input())
Ints = lambda: [*map(int, input().split())]

#------------------------------------------------------------------------------#

def solve(n, k, A):
    if k > 1: return 'IMPOSSIBLE'
    s, ss = sum(A), sum(x*x for x in A)
    if s == 0:
        return 0 if ss == 0 else 'IMPOSSIBLE'

    ans = (ss - s*s) / (2 * s)
    if int(ans) != ans: return 'IMPOSSIBLE'
    return int(ans) if abs(int(ans)) <= 10**18 else 'IMPOSSIBLE' 

#------------------------------------------------------------------------------#

for i in range(Int()):
    n, k = Ints()
    result = solve(n, k, Ints())
    print('Case #{}:'.format(i+1), result)