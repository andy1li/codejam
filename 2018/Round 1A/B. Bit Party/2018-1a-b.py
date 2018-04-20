# Round 1A 2018 - Bit Party
# https://codejam.withgoogle.com/2018/challenges/0000000000007883/dashboard/000000000002fff6

from pprint import pprint
from typing import NamedTuple

class Cashier(NamedTuple):
    maximum : int
    per_bit : int
    overhead: int

def capacity(cashier, time) -> int:
    capacity = min(
        cashier.maximum,
        (time-cashier.overhead) // cashier.per_bit,
    )
    return max(0, capacity) 
 
def check(r, b, cashiers, time) -> bool:
    top_r_cap = sorted(
        (capacity(c, time) for c in cashiers),
        reverse=True
    )[:r]
    return sum(top_r_cap) >= b

def solve(r, b, cashiers) -> int: 
    # print(r, b, cashiers)
    lo = 0
    hi = max(c.per_bit  for c in cashiers) * b +\
         max(c.overhead for c in cashiers)
 
    while lo <= hi:
        mid = (lo + hi) // 2
        if check(r, b, cashiers, mid):
            result = mid
            hi = mid - 1
        else:
            lo = mid + 1

    return result

### Remember to delete tests and scaffolding before submission
file = open('sample.in')
input = file.readline

num_cases = int(input())
for case in range(1, num_cases+1):
    r, b, c = map(int, input().split())
    cashiers = [
        Cashier(*map(int, input().split()))
        for _ in range(c)
    ]
    result = solve(r, b, cashiers)

    output = 'Case #%s: %s' %(case, result)
    print(output)

file.close()