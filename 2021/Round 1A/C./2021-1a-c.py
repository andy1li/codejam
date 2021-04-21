# 2021 Qualification Round - C. Hacked Exam
# https://codingcompetitions.withgoogle.com/codejam/round/000000000043585d/0000000000754750

from fractions import Fraction
from itertools import product
import numpy as np

Int = lambda: int(input())
Ints = lambda: [*map(int, input().split())]

#------------------------------------------------------------------------------#

def solve_small(N, Q, A, S):
    is_consistent = lambda s: np.array_equal((A == s).sum(axis=1), S)
    consistents = [*filter(is_consistent, product(range(2), repeat=Q))]
    seq, ev, n = '', 0, len(consistents)
    for c in zip(*consistents):
        p = Fraction(sum(c), n)
        seq += 'FT'[p > 0.5]
        ev += p if p > 0.5 else 1-p
    return f'{seq} {ev.numerator}/{ev.denominator}'

#------------------------------------------------------------------------------#

for i in range(Int()):
    N, Q = Ints()
    A, S = np.array([input().split() for _ in range(N)]).T
    A = np.array([np.array(list(row)) == 'T' for row in A])
    S = S.astype(int)
    result = solve_small(N, Q, A, S)
    print('Case #{}:'.format(i+1), result)