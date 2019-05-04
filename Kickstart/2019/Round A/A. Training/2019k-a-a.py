# 2019 Kickstart Round A - A. Training
# https://codingcompetitions.withgoogle.com/kickstart/round/0000000000050e01/00000000000698d6

from itertools import accumulate

def solve(n, p, skills):
    skills = [0] + skills
    acc = [*accumulate(skills)]

    return min(
        p*skills[i] - (acc[i]-acc[i-p])
        for i in range(p, len(skills))
    )

#------------------------------------------------------------------------------#

for i in range(int(input())):
    n, p = map(int, input().split())
    skills = sorted(map(int, input().split()))
    result = solve(n, p, skills)
    print('Case #{}:'.format(i+1), result)