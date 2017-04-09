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

#input, solve and output:
file = 'A-large'
input = open(file+'.in', 'r')
output = open(file+'.out', 'w')

n_cases = int(input.readline())
for case in range(1, n_cases+1):
    pancakes, k = input.readline().split()
    result = solve(pancakes, int(k))

    result_output = 'Case #%s: %s\n' %(case, result)
    # print(result_output)
    output.write(result_output)

input.close()
output.close()
