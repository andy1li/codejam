# Round 1C 2018 - C. Ant Stack 
# https://codejam.withgoogle.com/2018/challenges/0000000000007765/dashboard/000000000003e0a8

# Solution adpated from https://codejam.withgoogle.com/2018/challenges/0000000000007765/attempts/for/SkyDec

import sys

magic = 139

def solve(n, weights) -> int:
    # print(n, weights)
    dp = [.0] + [float('inf')] * (magic)

    for w in weights:
        for i in reversed(range(1, magic+1)):
            if dp[i-1] <= 6 * w:
                dp[i] = min(dp[i], dp[i-1]+w)

    print(dp, file=sys.stderr)
    for i in range(1, magic+1):
        if dp[i] < float('inf'):
            res = i
    return res

### Remember to delete tests and scaffolding before submission
file = open('sample.in')
input = file.readline

num_cases = int(input())
for case in range(1, num_cases+1):
    n = int(input())
    weights = map(int, input().split())
    result = solve(n, weights)

    output = 'Case #%s: %s' %(case, result)
    print(output)

file.close()