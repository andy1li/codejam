# 2018 Kickstart Round E - A. Yogurt
# https://code.google.com/codejam/contest/4394486/dashboard

from collections import Counter

def solve(n, k, exp_dates):
    count = Counter(
        min(n, x) for x in exp_dates
    )

    ans = 0; acc = 0
    for i in range(n, 0, -1):
        acc += count[i]
        ans += min(k, acc)
        acc -= min(k, acc)

    return ans

#------------------------------------------------------------------------------#

file = 'A-large-practice'
with open(file+'.in') as f_in, open(file+'.out', 'w') as f_out:
    input = f_in.readline
 
    for case in range(1, int(input())+1):
        n, k = map(int, input().split())
        exp_dates = map(int, input().split())
        result = solve(n, k, exp_dates)

        result_output = 'Case #%d: %s\n' % (case, result)
        print(result_output)
        f_out.write(result_output)
