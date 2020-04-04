# 2020 Qualification Round - C. Parenting Partnering Returns
# https://codingcompetitions.withgoogle.com/codejam/round/000000000019fd27/000000000020bdf9

# import 

Int   = lambda: int(input())
Ints  = lambda: [*map(int, input().split())]
Lines = lambda line, n_lines: [line() for _ in range(n_lines)]

#------------------------------------------------------------------------------#

def solve(N):
    day = [0] * (24 * 60)
    activities = Lines(Ints, N)
    for i, (S, E) in enumerate(activities):
        for minute in range(S, E): 
            day[minute] += 1
            if day[minute] > 2: return 'IM'

    return ''

#------------------------------------------------------------------------------#

for i in range(Int()):
    result = solve(Int())
    print('Case #{}:'.format(i+1), result)