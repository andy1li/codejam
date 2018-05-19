# 2017 Qualification Round - C. Bathroom Stalls
# https://code.google.com/codejam/contest/3264486/dashboard#s=p2

def get_max_min(n):
    if n & 1 : return (n - 1) // 2, (n - 1) // 2
    else     : return       n // 2,       n // 2 - 1

def solve(n, k):
    ''' Imagine a binary tree for k, then adjust for extra spots and separators'''
    n_log_two = n.bit_length() - 1
    k_depth   = k.bit_length() - 1

    # base group size for every leaf node 
    base_size = 2**(n_log_two - k_depth) 

    # average "n - full tree" extra spots for every leaf node 
    offset_extra = (n - 2**n_log_two) // (2**k_depth) 

    # seprators > offset_rmd + final_slack ?
    num_sep = 2**k_depth - 1 # number of separators = number of nodes in previous levels  
    offset_rmd = (n - 2**n_log_two) %  (2**k_depth) # remainder of "n - full tree" extra spots
    slack_size = 2**(k_depth+1) - 1 - k # k + slack = full tree

    # print('n, k:', n, k)
    # print('n_log_two, k_depth:', n_log_two, k_depth)
    # print('base_size + offset_extra:', base_size, '+', offset_extra)
    # print('num_sep:', num_sep)
    # print('offset_rmd + slack_size:', offset_rmd, '+', slack_size)
    
    offset_sep = [0, -1][num_sep > offset_rmd + slack_size]

    adjusted_size = base_size + offset_extra + offset_sep
    # print('adjusted_size:', adjusted_size)
    return get_max_min(adjusted_size)

#input, solve and output:
file = 'sample'
with open(file+'.in') as f_in, open(file+'.out', 'w') as f_out:
    input = f_in.readline

    n_cases = int(input())
    for case in range(1, n_cases+1):
        n, k = map(int, input().split())
        max_val, min_val = solve(n, k)

        result_output = 'Case #%s: %s %s\n' %(case, max_val, min_val)
        print(result_output)
        f_out.write(result_output)


