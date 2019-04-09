# 2019 Qualification Round - A. Foregone Solution
# https://codingcompetitions.withgoogle.com/codejam/round/0000000000051705/0000000000088231

def solve(n):
    length = len(n)
    a, b = ['0'] * length, ['0'] * length
    for i, x in enumerate(n):
        if x == '4': a[i], b[i] = '1', '3'
        else       : a[i] = x
    return map(lambda x: int(''.join(x)), [a, b])

#------------------------------------------------------------------------------#

for i in range(int(input())):
    result = solve(input())
    print('Case #{}:'.format(i+1), *result)