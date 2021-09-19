# 2021 Kickstart Round F - A. Trash Bins
# https://codingcompetitions.withgoogle.com/kickstart/round/0000000000435bae/0000000000887c32

#------------------------------------------------------------------------------#

def solve(N, S):
    l = [float('inf')] * (N+1)
    r = l.copy()
    
    for i in range(N):
        l[i+1] = 0 if S[i] else l[i] + 1 
    for i in reversed(range(N)):
        r[i] = 0 if S[i] else r[i+1] + 1 

    return sum(map(min, zip(l[1:], r)))

#------------------------------------------------------------------------------#

for i in range(int(input())):
    N = int(input())
    S = [*map(int, input())]
    result = solve(N, S)
    print('Case #{}:'.format(i+1), result)