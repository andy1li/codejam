# 2018 Kickstart Round E - B. Milk Tea
# https://code.google.com/codejam/contest/4394486/dashboard#s=p1

def solve(n, m, p, friends, forbidden):
    print(n, m, p, friends, forbidden)

#------------------------------------------------------------------------------#

file = 'sample'
with open(file+'.in') as f_in, open(file+'.out', 'w') as f_out:
    input = f_in.readline
 
    for case in range(1, int(input())+1):
        n, m, p = map(int, input().split())
        friends = [input().strip() for _ in range(n)]
        forbidden = {input().strip() for _ in range(m)}
        result = solve(n, m, p, friends, forbidden)

        result_output = 'Case #%d: %s\n' % (case, result)
        print(result_output)
        f_out.write(result_output)
