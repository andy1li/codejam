# 2018 Practice Session - B. Senate Evacuation
# https://codejam.withgoogle.com/2018/challenges/0000000000000130/dashboard/00000000000004c0

from string import ascii_uppercase
from typing import Dict, List

def get_parties(party_count) -> List[str]:
    return [*filter(party_count.get, party_count)]

def get_remaining_pairs(parties, party_count) -> List[str]:
    x, y = parties
    return [ x+y for _ in range(party_count[x]) ]

def parse_count(input) -> Dict[str, int]:
    party_count = map(int, input.split())
    return dict(zip(ascii_uppercase, party_count))

def solve(n: int, party_count: dict) -> str:
    parties = get_parties(party_count)

    plan = []
    while len(parties) > 2:
        to_evacuate = max(party_count, key=party_count.get)

        plan.append(to_evacuate)
        party_count[to_evacuate] -= 1

        parties = get_parties(party_count)

    remaining_pairs = get_remaining_pairs(parties, party_count)
    plan.extend(remaining_pairs)
    return ' '.join(plan)

### Remember to delete tests and scaffolding before submission
file  = open('sample.in')
input = file.readline

num_cases = int(input())
for case in range(1, num_cases+1):
    n = int(input())
    party_count = parse_count(input())
    result = solve(n, party_count)

    output = 'Case #%s: %s' %(case, result)
    print(output)

file.close()
