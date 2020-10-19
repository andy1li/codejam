# 2019 Kickstart Round B - A. Building Palindromes
# https://codingcompetitions.withgoogle.com/kickstart/round/0000000000050eda/0000000000119866

from collections import Counter
from functools   import reduce
Int  = lambda: int(input())
Ints = lambda: [*map(int, input().split())]

#------------------------------------------------------------------------------#

def is_odd(x): return x & 1

def check(pre_counts, l, r):
    cnt = pre_counts[r] - pre_counts[l-1]
    num_odds = sum(map(is_odd, cnt.values()))
    return int(num_odds <= 1)

def accumulate(acc, x):
    acc.append( acc[-1].copy() )
    acc[-1][x] += 1
    return acc

def solve(n, q, blocks):
    ans, pre_counts = 0, reduce(accumulate, blocks, [Counter()])
    for _ in range(q):
        ans += check(pre_counts, *Ints())
    return ans

#------------------------------------------------------------------------------#

for i in range(Int()):
    n, q = Ints()
    blocks = input()
    result = solve(n, q, blocks)
    print('Case #{}:'.format(i+1), result)