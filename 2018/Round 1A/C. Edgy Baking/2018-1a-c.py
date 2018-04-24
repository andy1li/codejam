# Round 1A 2018 - Edgy Baking
# https://codejam.withgoogle.com/2018/challenges/0000000000007883/dashboard/000000000002fff7

from functools import lru_cache

class Cookie:
    def __init__(self, w, h):
        # self.repr = f'{w}|{h}'
        self.p = (w + h) * 2
        self.l = min(w, h) * 2          # min extra p
        self.r = (w**2 + h**2)**.5 * 2  # max extra p

    def __repr__(self):
        return self.repr

def solve(n, p, cookies) -> float: 
    sum_p = sum(c.p for c in cookies)
    sum_r = sum(c.r for c in cookies)

    if sum_p + sum_r <= p:
        return sum_p + sum_r # cut all cookies

    @lru_cache(maxsize=None)
    def knapsack(k, room) -> float:     
        # 'min extra p' l as weight
        # 'max extra p' r as value
        if k == 0 or room == 0: return 0
        i = k-1; cookie = cookies[i]

        drop = knapsack(i, room)
        if cookie.l > room: return drop

        return max(
            drop, 
            cookie.r + knapsack(i, room-cookie.l)
        )

    room = p - sum_p
    best_r = knapsack(n, room)

    return min(p, sum_p + best_r) # cut as much as possible till p

### Remember to delete tests and scaffolding before submission
file = open('sample.in')
input = file.readline

num_cases = int(input())
for case in range(1, num_cases+1):
    n, p = map(int, input().split())
    cookies = [
        Cookie(*map(int, input().split()))
        for _ in range(n)
    ]
    result = solve(n, p, cookies)

    output = 'Case #%s: %s' %(case, result)
    print(output)

file.close()