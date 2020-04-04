# 2020 Qualification Round - C. Parenting Partnering Returns
# https://codingcompetitions.withgoogle.com/codejam/round/000000000019fd27/000000000020bdf9

import numpy as np 

Int   = lambda: int(input())
Ints  = lambda: [*map(int, input().split())]
Lines = lambda line, n_lines: [line() for _ in range(n_lines)]

#------------------------------------------------------------------------------#

def solve(N):
    assign = {}
    cameron = np.zeros(24 * 60, dtype=bool)
    jamie   = np.zeros(24 * 60, dtype=bool)

    activities = enumerate(Lines(Ints, N))
    for i, (S, E) in sorted(activities, key=lambda pair: pair[1][0]):
        if sum(cameron[S:E]) == 0:
            cameron[S:E] = True
            assign[i] = 'C'
        elif sum(jamie[S:E]) == 0:
            jamie[S:E] = True
            assign[i] = 'J'
        else:return 'IMPOSSIBLE'

    return ''.join(assign[i] for i in range(N))

#------------------------------------------------------------------------------#

for i in range(Int()):
    result = solve(Int())
    print('Case #{}:'.format(i+1), result)