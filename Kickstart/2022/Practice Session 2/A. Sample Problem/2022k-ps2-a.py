# 2022 Practice Session #2 - A. Sample Problem
# https://codingcompetitions.withgoogle.com/kickstart/round/00000000008f4a94/0000000000b5503a

import sys; sys.stdin = open('A. Sample Problem/sample.in', 'r')

Int = lambda: int(input())
Ints = lambda: [*map(int, input().split())]

#------------------------------------------------------------------------------#

def solve(n: int, m: int, bags: list):
    return sum(bags) % m

#------------------------------------------------------------------------------#

for i in range(Int()):
    result = solve(*Ints(), Ints())
    print('Case #{}:'.format(i+1), result)