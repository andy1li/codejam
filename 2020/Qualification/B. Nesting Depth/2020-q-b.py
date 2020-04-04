# 2020 Qualification Round - B. Nesting Depth
# https://codingcompetitions.withgoogle.com/codejam/round/000000000019fd27/0000000000209a9f

def solve(S):
    depth, res = 0, ''
    for x in map(int, S):
        if x > depth: res += '(' * (x - depth)
        if x < depth: res += ')' * (depth - x)
        res += str(x)
        depth = x

    res += ')' * depth
    return res

#------------------------------------------------------------------------------#

for i in range(int(input())):
    result = solve(input())
    print('Case #{}:'.format(i+1), result)