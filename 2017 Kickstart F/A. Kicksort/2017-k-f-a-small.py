# Kickstart Round F 2017 - A. Kicksort
# https://code.google.com/codejam/contest/7254486/dashboard#s=p0

def get_pivot(arr):
    return (len(arr) - 1) // 2

def solve(n, arr):
    if n <= 2: return 'YES'
    
    min_v = 1
    max_v = n
    for _ in range(max_v):
        p = get_pivot(arr)
        p_v = arr[p]
        if p_v != min_v and p_v != max_v: return 'NO'
        elif p_v == min_v: min_v += 1
        elif p_v == max_v: max_v -= 1
        
        del arr[p]

    return 'YES'

#input, solve and output:
file = 'foobar'
input = open(file+'.in', 'r')
output = open(file+'.out', 'w')

t_cases = int(input.readline())
for case in range(1, t_cases+1):
    n = int(input.readline())
    arr = [int(x) for x in input.readline().split()]
    result = solve(n, arr)

    result_output = 'Case #%s: %s\n' %(case, result)
    print(result_output)
    output.write(result_output)

input.close()
output.close()
