# 2019 Kickstart Round B - C. Diverse Subarray
# https://codingcompetitions.withgoogle.com/kickstart/round/0000000000050eda/00000000001198c1

from collections import Counter
Int  = lambda: int(input())
Ints = lambda: [*map(int, input().split())]

#------------------------------------------------------------------------------#

def solve(n, s, trinkets):
    # print(n, s, trinkets)
    ans, dp = 0, []
    for i, t in enumerate(trinkets):
        dp.append( (False, set(), Counter(), 0) )
        for j, (stop, thrown, cnt, bring) in enumerate(dp):
            if t not in thrown:
                cnt[t] += 1; bring += 1
                if cnt[t] > s:
                    if cnt[t] > n-i-1: stop = True 
                    thrown.add(t)
                    bring -= cnt[t]
                    del cnt[t]
                ans = max(ans, bring)
                dp[j] = stop, thrown, cnt, bring
        dp = [*filter(lambda quartet: not quartet[0], dp)]
    # print(dp)
    return ans

#------------------------------------------------------------------------------#

for i in range(Int()):
    n, s = Ints()
    trinkets = Ints()
    result = solve(n, s, trinkets)
    print('Case #{}:'.format(i+1), result)