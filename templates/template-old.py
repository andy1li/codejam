# 201X Round X - X. FOOBAR
# https://



################################################################################

def solve(n) -> str:
    print(n)
    return ''

################################################################################

file = 'sample'
f_in = open(file+'.in'); input = f_in.readline
f_out = open(file+'.out', 'w')

for case in range(1, int(input())+1):
    n = int(input())
    result = solve(n)

    result_output = 'Case #%d: %s\n' % (case, result)
    print(result_output)
    f_out.write(result_output)

f_in.close()
f_out.close()
