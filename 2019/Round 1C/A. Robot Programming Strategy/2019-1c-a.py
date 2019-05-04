# 2019 Round 1C - A. Robot Programming Strategy
# https://codingcompetitions.withgoogle.com/codejam/round/00000000000516b9/0000000000134c90

from itertools import cycle
Int   = lambda: int(input())
Lines = lambda line, n_lines: [line() for _ in range(n_lines)]

#------------------------------------------------------------------------------#

def solve(robots):
    policy = {
        'R':  'P',
        'P':  'S',
        'S':  'R',
        'PR': 'P',
        'RS': 'R',
        'PS': 'S',
    }

    ans, candidates = '', set(range(len(robots)))
    for _, *moves in zip(range(500), *map(cycle, robots)):
        c_moves = set(moves[c] for c in candidates)

        if len(c_moves) == 3: return 'IMPOSSIBLE' # cannot win
        if len(c_moves) == 1: return ans + policy[c_moves.pop()] # beat all 

        move = policy[''.join(sorted(c_moves))]
        for c in candidates.copy():
            if policy[moves[c]] == move:
                candidates -= set([c])
        ans += move

        if not candidates: return ans # all beaten
    
    return 'IMPOSSIBLE'

#------------------------------------------------------------------------------#

for i in range(Int()):
    a = Int()
    robots = set(Lines(input, a))
    result = solve(robots)
    print('Case #{}:'.format(i+1), result)