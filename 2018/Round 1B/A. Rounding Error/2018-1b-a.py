# Round 1B 2018 - A. Rounding Error
# https://codejam.withgoogle.com/2018/challenges/0000000000007764/dashboard 

from math import ceil

class Count:
    def __init__(self, n, c):
        self.n = n
        self.c = c
        self.fraction = c/n * 100

    @property
    def residual(self):
        half = ceil(self.fraction) - 0.5
        return self.fraction - half

    @property
    def rounded(self):
        if self.fraction - int(self.fraction) >= .5:
            return ceil(self.fraction)
        else:
            return int(self.fraction)

    def __repr__(self):
        return str(self.fraction) +  ' -> '  + str(self.rounded)

def undecided(n, r):
    if r == 0: return 0

    res = 0
    curr = Count(n, 1)
    for _ in range(r-1):
        if curr.residual < 0:
            curr = Count(n, curr.c+1)
        else:
            res += curr.rounded
            curr = Count(n, 1)
            
    res += curr.rounded
    return res

def solve(n, counts) -> int: 
    r = n - sum(c.c for c in counts)
    partial_sum = sum(c.rounded for c in counts)

    # short-circuit: all undecided vote a new language
    if Count(n, 1).residual >= 0: 
        return partial_sum + Count(n, 1).rounded * r

    filtered = filter(lambda c: c.residual < 0, counts)
    sort = sorted(filtered, key=lambda c: c.residual, reverse=True)

    for original in sort:
        if r == 0: break

        curr = original
        while r > 0:
            if curr.residual < 0:
                curr = Count(n, curr.c+1)
            else:
                break
            r -= 1

        partial_sum += curr.rounded - original.rounded

    return partial_sum + undecided(n, r)

### Remember to delete tests and scaffolding before submission
file = open('sample.in')
input = file.readline

num_cases = int(input())
for case in range(1, num_cases+1):
    n, l = map(int, input().split())
    counts = [Count(n, int(c)) for c in input().split()]
    result = solve(n, counts)

    output = 'Case #%s: %s' %(case, result)
    print(output)

file.close()
