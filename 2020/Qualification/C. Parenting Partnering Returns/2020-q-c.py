# 2020 Qualification Round - C. Parenting Partnering Returns
# https://codingcompetitions.withgoogle.com/codejam/round/000000000019fd27/000000000020bdf9

Int   = lambda: int(input())
Ints  = lambda: [*map(int, input().split())]
Lines = lambda line, n_lines: (line() for _ in range(n_lines))

#------------------------------------------------------------------------------#

def solve(N):
    assign = [None] * N
    E_C = E_J = 0

    activities = enumerate(Lines(Ints, N))
    for i, (S, E) in sorted(activities, key=lambda p: p[1][0]):
        if   S >= E_C: assign[i], E_C = 'C', E
        elif S >= E_J: assign[i], E_J = 'J', E
        else: return 'IMPOSSIBLE'

    return ''.join(assign)

#------------------------------------------------------------------------------#

for i in range(Int()):
    result = solve(Int())
    print('Case #{}:'.format(i+1), result)