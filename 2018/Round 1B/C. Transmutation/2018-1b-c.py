# Round 1B 2018 - C. Transmutation
# https://codejam.withgoogle.com/2018/challenges/0000000000007764/dashboard/000000000003675c 

# Solution adapted from https://codejam.withgoogle.com/2018/challenges/0000000000007764/attempts/for/Flydutchman

from copy import deepcopy

def get_recipes(m):
    return [
        [*map(lambda x: int(x)-1, input().split())]
        for _ in range(m)
    ]

def check(m, recipes, have, sum_have, target):
    if have[0] >= target: return True

    have = deepcopy(have)
    need = [target] + [0] * (m-1)

    prev_sum = stall_count = 0
    while True:
        next_need = [0] * m
        
        for i, unsatisfied_need in enumerate(need):
            if unsatisfied_need:
                # try to satisfy as much need as possible
                if have[i] < unsatisfied_need: 
                    try_satisfy = have[i]
                    sum_have -= try_satisfy
                else:
                    try_satisfy = unsatisfied_need

                have[i] -= try_satisfy
                need[i] -= try_satisfy
                
                # impossible to satisfy need ever
                if need[i] > sum_have/2: return False

                # keep transmuting need:
                # if it's ok, it's ok
                # or it will become impossible to satisfy
                # either way it will eventually end
                n1, n2 = recipes[i]
                next_need[n1] += need[i]
                next_need[n2] += need[i]

        # need is satisfied
        if not sum(need): return True
        
        # have is unchanging == need is not diminishing
        # for a full cycle == it will not diminish ever
        stall_count += (prev_sum == sum_have)
        prev_sum = sum_have
        if stall_count > m: return False

        need = next_need

def solve(m, recipes, have) -> int:
    lo = 0
    hi = sum_have = sum(have)

    while lo <= hi:
        mid = (lo + hi) // 2
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