# 2022 Qualification Round - D. Chain Reactions
# https://codingcompetitions.withgoogle.com/codejam/round/0000000000876ff1/0000000000a45ef7

Int = lambda: int(input())
Ints = lambda: [*map(int, input().split())]

#------------------------------------------------------------------------------#

def solve(n, funs, points):
    print(n, funs, points)
    
#------------------------------------------------------------------------------#

for i in range(int(input())):
    result = solve(Int(), Ints(), Ints())
    print('Case #{}:'.format(i+1), result)