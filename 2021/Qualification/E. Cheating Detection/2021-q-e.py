# 2021 Qualification Round - E. Cheating Detection
# https://codingcompetitions.withgoogle.com/codejam/round/000000000043580a/00000000006d12d7 

import numpy as np

#------------------------------------------------------------------------------#

def solve(data):
    difficulty = np.mean(data, axis=0)
    correct_spreads = [difficulty[row].std() for row in data]
    return np.argmax(correct_spreads) + 1

#------------------------------------------------------------------------------#

T, _ = int(input()), input()
for i in range(T):
    data = [ [bool(int(x)) for x in input()] for _ in range(100) ]
    result = solve(data)
    print('Case #{}:'.format(i+1), result)