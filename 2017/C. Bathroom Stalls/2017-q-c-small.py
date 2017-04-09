# 2017 Qualification Round - C. Bathroom Stalls
# https://code.google.com/codejam/contest/3264486/dashboard#s=p2

def get_max_min(n):
    if n & 1 : return (n - 1) // 2, (n - 1) // 2
    else     : return       n // 2,       n // 2 - 1

def solve(n, k):
    n_log_two = n.bit_length() - 1
    k_depth   = k.bit_length() - 1

    level_base = 2 ** (n_log_two - k_depth)

    offset_depth   = 2 ** k_depth - 1 # node count in previous levels
    offset_log     = (n - 2 ** n_log_two) // (2 ** k_depth) # average log diff in curr level  
    offset_log_rmd = (n - 2 ** n_log_two) %  (2 ** k_depth) # remainder
    level_leftover = 2 ** (k_depth + 1) - 1 - k

    print('n, k:', n, k)
    print('n_log_two, k_depth:', n_log_two, k_depth)
    print('level_base, offset_log:', level_base, offset_log)
    print('offset_depth, offset_log_rmd:', offset_depth, offset_log_rmd)
    print('level_leftover:', level_leftover)

    offset_leftover = [0, -1][offset_depth - offset_log_rmd > level_leftover]

    last = level_base + offset_log + offset_leftover
    print('last:', last)
    return get_max_min(last)

#input, solve and output:
file = 'foobar'
input = open(file+'.in', 'r')
output = open(file+'.out', 'w')

n_cases = int(input.readline())
for case in range(1, n_cases+1):
    n, k = map(int, input.readline().split())
    max_val, min_val = solve(n, k)

    result_output = 'Case #%s: %s %s\n' %(case, max_val, min_val)
    print(result_output)
    output.write(result_output)

input.close()
output.close()
