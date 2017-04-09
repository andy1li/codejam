# 2017 Qualification Round - B. Tidy Numbers
# https://code.google.com/codejam/contest/3264486/dashboard#s=p1

def solve(n):
    if len(n) == 1 or list(n) == sorted(n): return n

    first_wrong = 0
    for i in range(len(n)-1):
        if n[i] < n[i+1]: 
            first_wrong = i + 1

        elif n[i] > n[i+1]:

            if int(n[first_wrong]) > 1:
                start = n[:first_wrong]
                right = str(int(n[first_wrong]) - 1)
                end   = '9' * (len(n) - first_wrong - 1)
                return start + right + end
            else:
                return '9' * (len(n) - 1)
        

#input, solve and output:
file = 'B-large'
input = open(file+'.in', 'r')
output = open(file+'.out', 'w')

n_cases = int(input.readline())
for case in range(1, n_cases+1):
    n = input.readline().strip()
    result = solve(n)

    result_output = 'Case #%s: %s\n' %(case, result)
    # print(result_output)
    output.write(result_output)

input.close()
output.close()
