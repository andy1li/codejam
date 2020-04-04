# 2020 Qualification Round - A. Vestigium
# https://codingcompetitions.withgoogle.com/codejam/round/000000000019fd27/000000000020993c

import numpy as np

Int   = lambda: int(input())
Ints  = lambda: [*map(int, input().split())]
Lines = lambda line, n_lines: [line() for _ in range(n_lines)]

#------------------------------------------------------------------------------#

def solve(N):
    matrix = np.array(Lines(Ints, N))
    K = np.diag(matrix).sum()
    R = sum( len(set(row)) != N for row in matrix )
    C = sum( len(set(col)) != N for col in matrix.T )
    return K, R, C

#------------------------------------------------------------------------------#

for i in range(Int()):
    result = solve(Int())
    print('Case #{}:'.format(i+1), *result)