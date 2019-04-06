# 2019 Qualification Round - C. Cryptopangrams
# https://codingcompetitions.withgoogle.com/codejam/round/0000000000051705/000000000008830b

from math import gcd
from string import ascii_uppercase

def solve(cipher):
    seq = [ gcd(a, b)
        for a, b in zip(cipher, cipher[1:])
    ]

    seq = [ cipher[0]//seq[0] ] + seq # head
    seq.append( cipher[-1]//seq[-1] ) # last
    primes = set(seq)

    assert len(primes) == 26
    letter = dict(zip(sorted(primes), ascii_uppercase))

    return ''.join(map(letter.get, seq))

#------------------------------------------------------------------------------#

for case in range(1, int(input())+1):
    _ = input()
    cipher = [*map(int, input().split())]
    result = solve(cipher)
    output = 'Case #%d: %s' %(case, result)
    print(output)