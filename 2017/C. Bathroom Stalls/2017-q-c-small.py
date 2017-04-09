# 2017 Qualification Round - C. Bathroom Stalls
# https://code.google.com/codejam/contest/3264486/dashboard#s=p2

from math import floor, log

def get_max_min(n):
    # if n == 1: return 0, 0
    if n & 1 : return (n - 1) // 2, (n - 1) // 2
    else     : return n // 2, n // 2 - 1

def solve(n, k):
    if k == 1: return get_max_min(n)

    depth = 1
    while k >= 2 ** depth: depth += 1

    log_two = floor(log(n, 2))
    base = 2 ** (log_two - depth + 1)

    offset_depth = 2 ** (depth - 1) - 1 # adjust by depth
    offset_log = (n - 2 ** log_two) // (2 ** (depth - 1))
    offset_log_remain = (n - 2 ** log_two) % (2 ** (depth - 1)) 
    remain = k - 2 ** depth + 1

    print('n, k:', n, k)
    print('depth, base, offset_log:', depth, base, offset_log)
    print('-offset_depth, offset_log_remain:', -offset_depth, offset_log_remain)
    print('remain:', remain)

    offset_used = [0, -1][ offset_log_remain - offset_depth < remain]

    last = base + offset_log + offset_used
    print(last)
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
