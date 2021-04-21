# 2021 Kickstart Round B - B. Longest Progression
# https://codingcompetitions.withgoogle.com/kickstart/round/0000000000435a5b/000000000077a3a5

Int = lambda: int(input())
Ints = lambda: [*map(int, input().split())]

#------------------------------------------------------------------------------#

def solve(N, A):
    diff = [a-b for a, b in zip(A, A[1:])]
    print(diff)
    return 

#------------------------------------------------------------------------------#

for i in range(Int()):
    result = solve(Int(), Ints())
    print('Case #{}:'.format(i+1), result)