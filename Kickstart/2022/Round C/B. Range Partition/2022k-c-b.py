# 2022 Kickstart Round C - B. Range Partition
# https://codingcompetitions.withgoogle.com/kickstart/round/00000000008cb4d1/0000000000b20deb

import sys; sys.stdin = open('B. Range Partition/ts2_input.txt', 'r')
sys.setrecursionlimit(10**9)

Int = lambda: int(input())
Ints = lambda: [*map(int, input().split())]

#------------------------------------------------------------------------------#

def partition(n, p_sum):
    if (p_sum == 0 or n == 0): return []
    return (
        partition(p_sum, p_sum) if n > p_sum else 
        [n] + partition(n-1, p_sum-n)
    )

def solve(n, x, y):
    sum_n = n * (n + 1) // 2
    if sum_n % (x + y) != 0: return 'IMPOSSIBLE'

    a = sum_n * x // (x + y)
    p_a = partition(n, a)

    return f'''POSSIBLE
{len(p_a)}
{' '.join(map(str, p_a))}'''


#------------------------------------------------------------------------------#

for i in range(Int()):
    result = solve(*Ints())
    print('Case #{}:'.format(i+1), result)