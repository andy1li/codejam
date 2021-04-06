# 2021 Qualification Round - C. Reversort Engineering
# https://codingcompetitions.withgoogle.com/codejam/round/000000000043580a/00000000006d12d7 

from itertools import count
Ints = lambda: map(int, input().split())

#------------------------------------------------------------------------------#

def solve(n, cost):
    def check(i, j):
        return i+1 <= cost-j <= (n*(n+1) - (n-i)*(n-(i+1))) // 2

    A, i = [*range(1, n+1)], n-2
    if not check(i, 0): return 'IMPOSSIBLE'

    while cost and i > -1:
        c = next(j for j in count(1) if check(i-1, j))
        A[i:i+c] = reversed(A[i:i+c])
        cost -= c
        i -= 1 

    return ' '.join(map(str, A))

#------------------------------------------------------------------------------#

for i in range(int(input())):
    result = solve(*Ints()) 
    print('Case #{}:'.format(i+1), result)