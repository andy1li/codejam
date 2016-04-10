# 2016 Africa Qualification Round - A. Counting Sheep
# https://code.google.com/codejam/contest/6254486/dashboard#s=p0

def solve(n):
    flags = {i: 1 for i in range(10)}
    #print n, flags

    if int(n) is 0:
        return 'INSOMNIA'

    result = 0
    while len(flags):
        result += n
        for digit in str(result):
            if flags.get(int(digit)):
                del flags[int(digit)]

    return result

#input, solve and output:
file = 'foobar'
input = open(file+'.in', 'r')
output = open(file+'.out', 'w')

n_cases = int(input.readline())
for case in range(1, n_cases+1):
    n = int(input.readline())
    result = solve(n)

    result_output = 'Case #%s: %s\n' %(case, result)
    print result_output
    output.write(result_output)

input.close()
output.close()
