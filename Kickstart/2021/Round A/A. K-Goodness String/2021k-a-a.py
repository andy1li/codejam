# 2021 Kickstart Round A - A. K-Goodness String
# https://codingcompetitions.withgoogle.com/kickstart/round/0000000000436140/000000000068cca3

#------------------------------------------------------------------------------#

def solve(n, k, s):
    return abs(k - sum(s[i] != s[n-i-1] for i in range(n//2)))

#------------------------------------------------------------------------------#

for i in range(int(input())):
    n, k = map(int, input().split())
    result = solve(n, k, input())
    print('Case #{}:'.format(i+1), result)