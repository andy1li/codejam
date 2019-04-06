# 2019 Qualification Round - A. Foregone Solution
# https://codingcompetitions.withgoogle.com/codejam/round/0000000000051705/0000000000088231

def solve(n) -> str:
    length = len(n)
    a, b = ['0'] * length, ['0'] * length
    for i, x in enumerate(n):
        if x == '4': a[i], b[i] = '1', '3'
        else       : a[i] = x
    a = int(''.join(a)) # type: ignore
    b = int(''.join(b)) # type: ignore
    return str(a) + ' ' + str(b)

#------------------------------------------------------------------------------#

for case in range(1, int(input())+1):
    n = input()
    result = solve(n)
    output = 'Case #%d: %s' %(case, result)
    print(output)