# 2021 Kickstart Round F - A. Trash Bins
# https://codingcompetitions.withgoogle.com/kickstart/round/0000000000435bae/0000000000887c32

from itertools import groupby

#------------------------------------------------------------------------------#

def gauss(n): return (1 + n) * n // 2

def solve(N, S, ans=0):
    groups = [ (k, len(list(g))) for k, g in groupby(S) ]
    for i in [0, -1]:
        if groups:
            key, length = groups.pop(i)
            if key == '0': ans += gauss(length)

    for key, length in groups:
        if key == '0':
            half = length // 2
            if length & 1: ans += gauss(half) + gauss(half+1)
            else:          ans += gauss(half) * 2 

    return ans

#------------------------------------------------------------------------------#

for i in range(int(input())):
    result = solve(int(input()), input())
    print('Case #{}:'.format(i+1), result)