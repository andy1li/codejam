# 2022 Practice Session #2 - B. Sherlock and Parentheses
# https://codingcompetitions.withgoogle.com/kickstart/round/00000000008f4a94/0000000000b5496b

import sys; sys.stdin = open('B. Sherlock and Parentheses/sample.in', 'r')

Int = lambda: int(input())
Ints = lambda: [*map(int, input().split())]

#------------------------------------------------------------------------------#

def solve(l: int, r: int):
    return l, r

#------------------------------------------------------------------------------#

for i in range(Int()):
    result = solve(*Ints())
    print('Case #{}:'.format(i+1), result)