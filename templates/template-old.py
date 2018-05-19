# 201X Round X - X. FOOBAR
# https://



#------------------------------------------------------------------------------#

def solve(n) -> str:
    print(n)
    return ''

#------------------------------------------------------------------------------#

file = 'sample'
with open(file+'.in') as f_in, open(file+'.out', 'w') as f_out:
    input = f_in.readline
    
    for case in range(1, int(input())+1):
        n = int(input())
        result = solve(n)

        result_output = 'Case #%d: %s\n' % (case, result)
        print(result_output)
        f_out.write(result_output)
