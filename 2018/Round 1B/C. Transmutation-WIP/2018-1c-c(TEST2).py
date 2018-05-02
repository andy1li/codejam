# Round 1B 2018 - C. Transmutation
# https://codejam.withgoogle.com/2018/challenges/0000000000007764/dashboard/000000000003675c 

# Adapted from https://github.com/hickford/codejam/blob/master/2018/1B/transmutation/transmutation.py

def get_recipes(m):
    return [
        [*map(lambda x: int(x)-1, input().split())]
        for _ in range(m)
    ]

def check(m, recipes, have, sum_have, target):
    if have[0] >= target: return True

    need = [target] + [0] * (m-1)
    sum_need = sum(need)

    while sum_need <= sum_have:
        # print(need, have)
        start = 0
        for i in range(start, m):
            if need[i] > have[i]:
                gap = need[i] - have[i]

                need[i] -= gap
                for metal in recipes[i]:
                    need[metal] += gap

                start = min(i, *recipes[i])
                sum_need += gap
                # print(start)
                break
        else:
            return True

    return False

def solve(m, recipes, have) -> int:
    lo = 0
    hi = sum_have = sum(have)

    while lo <= hi:
        mid = (lo + hi) // 2

        # print('checking:', lo, mid, hi)
        if check(m, recipes, have, sum_have, mid):
            lo = mid + 1
        else:
            hi = mid - 1

    return lo-1

### Remember to delete tests and scaffolding before submission
file = open('sample.in')
input = file.readline

num_cases = int(input())
for case in range(1, num_cases+1):
    m = int(input())
    recipes = get_recipes(m)
    have = [*map(int, input().split())]
    result = solve(m, recipes, have)

    output = 'Case #%s: %s' %(case, result)
    print(output)

file.close()