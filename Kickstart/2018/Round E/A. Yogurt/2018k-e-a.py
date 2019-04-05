# 2018 Kickstart Round E - A. Yogurt
# https://code.google.com/codejam/contest/4394486/dashboard

from itertools import count

def solve(n, k, exp_dates):
    ans = 0
    for today in count():
        eaten = 0
        while True:
            try: exp_date = next(exp_dates)
            except: return ans

            if today < exp_date: 
                ans += 1
                eaten += 1
                if eaten == k: break

#------------------------------------------------------------------------------#

file = 'sample'
with open(file+'.in') as f_in, open(file+'.out', 'w') as f_out:
    input = f_in.readline
 
    for case in range(1, int(input())+1):
        n, k = map(int, input().split())
        exp_dates = iter(sorted(map(int, input().split())))
        result = solve(n, k, exp_dates)

        result_output = 'Case #%d: %s\n' % (case, result)
        print(result_output)
        f_out.write(result_output)
