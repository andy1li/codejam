# 2019 Qualification Round - C. Cryptopangrams
# https://codingcompetitions.withgoogle.com/codejam/round/0000000000051705/000000000008830b

from collections import deque
from math import gcd
from string import ascii_uppercase

def get_start(cipher):
    return next((i, b)
        for i, (a, b) in enumerate(zip(cipher, cipher[1:]))
        if a != b
    )
    
def solve(cipher):
    seq = deque()
    i, start = get_start(cipher)

    fst, snd = cipher[i:i+2]
    seq.append(fst//gcd(fst, snd))
    for x in cipher[i:]: seq.append(x//seq[-1])
    for x in reversed(cipher[:i]): seq.appendleft(x//seq[0])

    primes = set(seq)
    assert len(primes) == 26
    letter = dict(zip(sorted(primes), ascii_uppercase))
    return ''.join(map(letter.get, seq))

#------------------------------------------------------------------------------#

for case in range(1, int(input())+1):
    input()
    cipher = [int(x) for x in input().split()]
    result = solve(cipher)
    print('Case #{}:'.format(case), result)