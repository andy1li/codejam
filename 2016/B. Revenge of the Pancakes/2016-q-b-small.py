# 2016 Qualification Round - B. Revenge of the Pancakes
# https://code.google.com/codejam/contest/6254486/dashboard#s=p1

def solve_plus(s):
    print "solve_plus", s
    s = s.rstrip('+')
    if s is '':
        return 0
    else:
        return solve_minus(s) + 1

def solve_minus(s):
    print "solve_minus", s
    s = s.rstrip('-')
    if s is '':
        return 0
    else:
        return solve_plus(s) + 1

#input, solve and output:
file = 'foobar'
input = open(file+'.in', 'r')
output = open(file+'.out', 'w')

n_cases = int(input.readline())
for case in range(1, n_cases+1):
    s = input.readline().strip()
    result = solve_plus(s)

    result_output = 'Case #%s: %s\n' %(case, result)
    print result_output
    output.write(result_output)

input.close()
output.close()
