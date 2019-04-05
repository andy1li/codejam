# 2017 Round 1A - C. Play the Dragon
# https://code.google.com/codejam/contest/5304486/dashboard#s=p2

def solve(r, c, grid) -> str:
    print(r, c, grid)

    return ''

#------------------------------------------------------------------------------#

file = 'sample'
with open(file+'.in') as f_in, open(file+'.out', 'w') as f_out:
    input = f_in.readline
    for case in range(1, int(input())+1):
        r, c = map(int, input().split())
        grid = [ list(input().strip())
            for _ in range(r)
        ]
        result = solve(r, c, grid)

        result_output = 'Case #%d: %s\n' % (case, result)
        print(result_output)
        f_out.write(result_output)


