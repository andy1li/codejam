# 2022 Kickstart Round C - B. Range Partition
# https://codingcompetitions.withgoogle.com/kickstart/round/00000000008cb4d1/0000000000b20deb

import sys; sys.stdin = open('B. Range Partition/sample.in', 'r')

Int = lambda: int(input())
Ints = lambda: [*map(int, input().split())]

#------------------------------------------------------------------------------#

def partition(n, p_sum):
    p = []
    while n > 0 and p_sum > 0:
        if n > p_sum: n = p_sum
        p.append(n)
        n, p_sum = n-1, p_sum-n
    return p

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