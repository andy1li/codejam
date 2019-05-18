# 2019 Round 2 - D. 
# https://

from collections import defaultdict
Int   = lambda: int(input())
Ints  = lambda: [*map(int, input().split())]
Lines = lambda line, n_lines: [line() for _ in range(n_lines)]

#------------------------------------------------------------------------------#

def solve(m, recipes, metals):
    G = defaultdict
    print(m, recipes, metals)
    return 0

#------------------------------------------------------------------------------#

for i in range(Int()):
    m = Int()
    recipes = Lines(Ints, m)
    metals = Ints()
    result = solve(m, recipes, metals)
    print('Case #{}:'.format(i+1), result)