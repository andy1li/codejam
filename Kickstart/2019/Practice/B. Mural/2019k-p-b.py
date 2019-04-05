# 2019 Kickstart Practice - B. Mural
# https://codingcompetitions.withgoogle.com/kickstart/round/0000000000051060/0000000000058b89

from math import ceil

def solve(n, scores) -> int:
    l = ceil(n/2)
    ans = window = sum(scores[:l])

    for i in range(l, n):
        window += scores[i]
        window -= scores[i-l]
        ans = max(ans, window)

    return ans

#------------------------------------------------------------------------------#

for case in range(1, int(input())+1):
    n = int(input())
    scores = [*map(int, input())]
    result = solve(n, scores)
    output = 'Case #%d: %s' %(case, result)
    print(output)