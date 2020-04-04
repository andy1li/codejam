# 2019 Qualification Round - B. You Can Go Your Own Way
# https://codingcompetitions.withgoogle.com/codejam/round/0000000000051705/00000000000881da

def solve(p) -> str:
    return ''.join(
        'E' if move=='S' else 'S'
        for move in p
    )

#------------------------------------------------------------------------------#

for case in range(1, int(input())+1):
    _, p = input(), input() 
    result = solve(p)
    output = 'Case #%d: %s' %(case, result)
    print(output)