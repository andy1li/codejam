# 2018 Qualification Round - B. Trouble Sort
# https://codejam.withgoogle.com/2018/challenges/00000000000000cb/dashboard/00000000000079cb

from typing import Union

def pair(n, evens, odds):
    for i in range(n-1):
        yield (
            (i, odds[i//2], evens[i//2+1])
            if i % 2 else
            (i, evens[i//2], odds[i//2])
        )

def solve(n, vals) -> Union[int, str]:    
    evens = sorted(vals[::2])
    odds  = sorted(vals[1:][::2])

    for i, cur, nxt in pair(n, evens, odds):
        if cur > nxt:
            return i

    return 'OK'

### Remember to delete tests and scaffolding before submission
assert solve(5, [5, 6, 8, 4, 3]) == 'OK'
assert solve(3, [8, 9, 7]) == 1

file  = open('sample.in',  'r')
input = file.readline

num_cases = int(input())
for case in range(1, num_cases+1):
    n = int(input())
    vals = [int(x) for x in input().split()]
    result = solve(n, vals)

    output = 'Case #%s: %s' %(case, result)
    print(output)

file.close()
