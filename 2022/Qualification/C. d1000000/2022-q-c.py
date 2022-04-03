# 2022 Qualification Round - C. d1000000
# https://codingcompetitions.withgoogle.com/codejam/round/0000000000876ff1/0000000000a46471

Int = lambda: int(input())
Ints = lambda: [*map(int, input().split())]

#------------------------------------------------------------------------------#

def solve(n, ds):
    ans = 0
    for d in ds:
        if d > ans: ans += 1
    return ans
    
#------------------------------------------------------------------------------#

for i in range(int(input())):
    result = solve(Int(), sorted(Ints()))
    print('Case #{}:'.format(i+1), result)