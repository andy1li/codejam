# 2021 Qualification Round - B. Moons and Umbrellas 
# https://codingcompetitions.withgoogle.com/codejam/round/000000000043580a/00000000006d1145

#------------------------------------------------------------------------------#

def solve(x, y, S):
    S = S.replace('?', '')
    return x * S.count('CJ') + y * S.count('JC')

#------------------------------------------------------------------------------#

for i in range(int(input())):
    x, y, S = input().split()
    result = solve(int(x), int(y), S)
    print('Case #{}:'.format(i+1), result)