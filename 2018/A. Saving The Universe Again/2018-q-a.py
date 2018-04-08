# 2018 Qualification Round - A. Saving The Universe Again
# https://codejam.withgoogle.com/2018/challenges/00000000000000cb/dashboard

from itertools import count
from typing    import Union

def damage(p) -> int:
    res = 0; charge = 0
    for op in p:
        if op == 'C': charge += 1
        if op == 'S': res += 2 ** charge
    return res

def step(p) -> str:
    try:
        index = p.rindex('CS')   
        return p[:index] + 'SC' + p[index+2:]

    except ValueError: return p

def solve(d, p) -> Union[int, str]:    
    for i in count():
        if damage(p) <= d: return i
        
        prev, p = p, step(p)

        if prev == p: return 'IMPOSSIBLE'

    raise RuntimeError

### Remember to delete tests and scaffolding before submission
assert solve(1, 'CS') == 1
assert solve(2, 'CS') == 0
assert solve(1, 'SS') == 'IMPOSSIBLE'
assert solve(6, 'SCCSSC') == 2
assert solve(2, 'CC') == 0
assert solve(3, 'CSCSS') == 5 

file  = open('sample.in',  'r')
input = file.readline

num_cases = int(input())
for case in range(1, num_cases+1):
    d, p = input().split()
    result = solve(int(d), p)

    output = 'Case #%s: %s' %(case, result)
    print(output)

file.close()
