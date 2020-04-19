# 2020 Round 1B - A. Expogo 
# https://codingcompetitions.withgoogle.com/codejam/round/000000000019fef2/00000000002d5b62

Int  = lambda: int(input())
Ints = lambda: [*map(int, input().split())]

odd  = lambda n: n & 1
even = lambda n: not odd(n)

#------------------------------------------------------------------------------#

def step(x, y):
    def go(d):
        if d == 'W': return (x+1)//2, y//2, 'W'
        if d == 'E': return (x-1)//2, y//2, 'E'
        if d == 'S': return x//2, (y+1)//2, 'S'
        if d == 'N': return x//2, (y-1)//2, 'N'

    def check(d):
        nx, ny, _ = go(d)
        return odd(nx + ny)

    if odd(x): return go('W') if check('W') else go('E')
    else:      return go('S') if check('S') else go('N')

D = { (-1, 0): 'W', (1, 0): 'E', (0, -1): 'S', (0, 1): 'N' }

def solve(x, y):
    if x == y == 0: return ''
    if even(x + y): return 'IMPOSSIBLE'
    res = ''
    while (x, y) not in D:
        x, y, d = step(x, y)
        res += d
    return res + D[x, y]

#------------------------------------------------------------------------------#

for i in range(Int()):
    result = solve(*Ints())
    print('Case #{}:'.format(i+1), result)