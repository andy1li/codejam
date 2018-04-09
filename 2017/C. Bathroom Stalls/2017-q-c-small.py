# 2017 Qualification Round - C. Bathroom Stalls
# https://code.google.com/codejam/contest/3264486/dashboard#s=p2

def get_max_min(n):
    if n & 1 : return (n - 1) // 2, (n - 1) // 2
    else     : return       n // 2,       n // 2 - 1

def solve(n, k):
    ''' Imagine a binary tree for k, and adjust for separators and free spots '''
    n_log_two = n.bit_length() - 1
    k_depth   = k.bit_length() - 1

    # base group size for every node in curr level
    base_size = 2**(n_log_two - k_depth) 

    # average "n" free spots for every node in curr level 
    # = (n - full tree) / num of nodes in curr level
    offset_n = (n - 2**n_log_two) // (2**k_depth) 

    # seprators > offset_extra + final_slack ?
    num_sep = 2**k_depth - 1 # number of separators = number of nodes in previous levels  
    offset_rmd = (n - 2**n_log_two) %  (2**k_depth) # remainder of "n" free spots
    final_slack = 2**(k_depth+1) - 1 - k # k + slack = full tree

    print('n, k:', n, k)
    # print('n_log_two, k_depth:', n_log_two, k_depth)
    print('base_size + offset_n:', base_size, '+', offset_n)
    print('num_sep:', num_sep)
    print('offset_rmd + final_slack:', offset_rmd, '+', final_slack)
    

    offset_sep = [0, -1][num_sep > offset_rmd + final_slack]

    adjusted_size = base_size + offset_n + offset_sep
    print('adjusted_size:', adjusted_size)
    return get_max_min(adjusted_size)

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
