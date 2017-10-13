# Kickstart Round F 2017 - C. Catch Them All
# https://code.google.com/codejam/contest/7254486/dashboard#s=p2

def solve(n, m, p, roads):
    print(n, m, p, *roads, sep='\n')


#input, solve and output:
file = 'foobar'
input = open(file+'.in', 'r')
output = open(file+'.out', 'w')

t_cases = int(input.readline())
for case in range(1, t_cases+1):
    n, m, p = [int(x) for x in input.readline().split()]
    roads = [[int(x) for x in input.readline().split()]
             for _ in range(m)]
    result = solve(n, m, p, roads)

    result_output = 'Case #%s: %s\n' %(case, result)
    print(result_output)
    # output.write(result_output)

input.close()
output.close()
