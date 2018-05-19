# 2017 Qualification Round - A. Oversized Pancake Flipper
# https://code.google.com/codejam/contest/3264486/dashboard#s=p0

def solve(pancakes, k):
    pancakes = list(map(lambda p: p == '+', pancakes))
    res = 0
    
    for i in range(len(pancakes)-k+1):
        # print(pancakes, i, pancakes[i])
        if not pancakes[i]:
            res += 1
            for j in range(k):
                pancakes[i+j] = not pancakes[i+j]

    if sum(pancakes) == len(pancakes):
        return res
    else:
        return 'IMPOSSIBLE'

#------------------------------------------------------------------------------#

file = 'sample'
with open(file+'.in') as f_in, open(file+'.out', 'w') as f_out:
    input = f_in.readline
    for case in range(1, int(input())+1):
        pancakes, k = input().split()
        result = solve(pancakes, int(k))

        result_output = 'Case #%d: %s\n' % (case, result)
        print(result_output)
        f_out.write(result_output)


