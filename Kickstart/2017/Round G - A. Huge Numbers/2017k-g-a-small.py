# Kickstart Round G 2017 - A. Huge Numbers
# https://code.google.com/codejam/contest/3254486/dashboard#s=p0

from collections import OrderedDict
from math import factorial
    
def solve(a, n, p):
    cycle_dict = OrderedDict()
    x = a % p
    while x not in cycle_dict:
        cycle_dict[x] = True
        x = x * a % p
    
    cycle = list(cycle_dict)
    times = factorial(n)

    offset = cycle.index(x)
    if offset:
        times -= offset
        cycle = cycle[offset:]

    remainder = times % len(cycle) # print('remainder:', remainder)
    res = cycle[remainder - 1]

    # if offset:
    #     print(a, n, p)
    #     print(cycle_dict.keys()) 
    #     print('offset:', offset)
    
    return res

#input, solve and output:
file = 'A-large-practice'
input = open(file+'.in', 'r')
output = open(file+'.out', 'w')

t_cases = int(input.readline())
for case in range(1, t_cases+1):
    a, n, p = map(int, input.readline().split())
    result = solve(a, n, p)

    result_output = 'Case #%s: %s\n' %(case, result)
    print(result_output)
    output.write(result_output)

input.close()
output.close()
