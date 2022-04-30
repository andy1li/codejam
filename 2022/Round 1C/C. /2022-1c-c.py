# 2022 Round 1C - C. Intranets 
# https://codingcompetitions.withgoogle.com/codejam/round/0000000000877b42/0000000000afeb38

import sys; sys.stdin = open('C. Intranets/sample.in', 'r')

Int = lambda: int(input())
Ints = lambda: [*map(int, input().split())]

#------------------------------------------------------------------------------#

def solve(m, k):
    print(m, k)

#------------------------------------------------------------------------------#

for i in range(Int()):
    result = solve(*Ints())
    print('Case #{}:'.format(i+1), result)