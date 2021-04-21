# 2021 Kickstart Round B - A. Increasing Substring
# https://codingcompetitions.withgoogle.com/kickstart/round/0000000000435a5b/000000000077a882

#------------------------------------------------------------------------------#

def solve(N, S):
    dp = [1]
    for i in range(1, N):
        is_inc = S[i] > S[i-1]
        dp.append(dp[-1]+1 if is_inc else 1)
    return dp

#------------------------------------------------------------------------------#

for i in range(int(input())):
    result = solve(int(input()), input())
    print('Case #{}:'.format(i+1), *result)