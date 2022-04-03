# 2022 Qualification Round - A. Punched Cards
# https://codingcompetitions.withgoogle.com/codejam/round/0000000000876ff1/0000000000a4621b

Int = lambda: int(input())
Ints = lambda: [*map(int, input().split())]

#------------------------------------------------------------------------------#

def row(n, i):
    if i % 2: return '|' + '.|' * n
    else: return '+' + '-+' * n

def solve(r, c):
    card = [row(c, i) for i in range(1 + 2 * r)]
    card[0] = '..' + card[0][2:]
    card[1] = '.' + card[1][1:]
    return '\n'.join(card)

#------------------------------------------------------------------------------#

for i in range(Int()):
    result = solve(*Ints())
    print('Case #{}:'.format(i+1), result, sep='\n')