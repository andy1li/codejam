# 2021 Kickstart Round A - D. Checksum
# https://codingcompetitions.withgoogle.com/kickstart/round/0000000000436140/000000000068c2c3

Ints = lambda: [*map(int, input().split())]

#------------------------------------------------------------------------------#

def solve(n, A, B, cks_row, chs_col):
    print(n)
    print(A)
    print(B)
    print(cks_row, chs_col)
    return 0

#------------------------------------------------------------------------------#

for i in range(int(input())):
    n = int(input())
    A = [Ints() for _ in range(n)]
    B = [Ints() for _ in range(n)]
    cks_row = Ints()
    chs_col = Ints()
    result = solve(n, A, B, cks_row, chs_col)
    print('Case #{}:'.format(i+1), result)