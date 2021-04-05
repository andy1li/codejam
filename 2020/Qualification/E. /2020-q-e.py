# 2020 Qualification Round - E. Indicium
# https://codingcompetitions.withgoogle.com/codejam/round/000000000019fd27/0000000000209aa0

from itertools import permutations

Int  = lambda: int(input())
Ints = lambda: [*map(int, input().split())]

#------------------------------------------------------------------------------#

def solve():
    N, K = Ints()
    print(*permutations(range(1, N+1), N))
    return ''

#------------------------------------------------------------------------------#

for i in range(Int()):
    result = solve()
    print('Case #{}:'.format(i+1), result)