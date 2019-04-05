# 2019 Kickstart Practice - C. Kickstart Alarm
# https://codingcompetitions.withgoogle.com/kickstart/round/0000000000051060/0000000000058a56

def array(N, x, y, C, D, E1, E2, F):
    for _ in range(N):
        yield (x+y) % F
        new_x = (C * x + D * y + E1) % F
        new_y = (D * x + C * y + E2) % F
        x, y = new_x, new_y

def solve(MOD = 10**9+7) -> int:
    N, K, x, y, C, D, E1, E2, F = map(int, input().split())

    ans = 0
    for i, x in enumerate(array(N, x, y, C, D, E1, E2, F), start=1):
        if i == 1: 
            GS = K
        else:
            GS += (pow(i, K+1, MOD)-1) * pow(i-1, MOD-2, MOD) - 1
            GS %= MOD
        
        times = N-i+1
        # print(i, times, GS)
        ans += x * GS * times
        ans %= MOD

    return ans

#------------------------------------------------------------------------------#

for case in range(1, int(input())+1):
    result = solve()
    result_output = 'Case #%d: %s\n' % (case, result)
    print(result_output)