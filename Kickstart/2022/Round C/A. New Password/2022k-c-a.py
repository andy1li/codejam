# 2022 Kickstart Round C - A. New Password
# https://codingcompetitions.withgoogle.com/kickstart/round/00000000008cb4d1/0000000000b20f15

import sys; sys.stdin = open('A. New Password/sample.in', 'r')

Int = lambda: int(input())
Ints = lambda: [*map(int, input().split())]

#------------------------------------------------------------------------------#

def solve(n, password):
    if not any(x.isupper() for x in password):
        password += 'A'
    if not any(x.islower() for x in password):
        password += 'a'
    if not any(x.isnumeric() for x in password):
        password += '1'
    if not any(x in '#@*&' for x in password):
        password += '#'
    if len(password) < 7:
        password += '*' * (7 - len(password)) 

    return password

#------------------------------------------------------------------------------#

for i in range(Int()):
    result = solve(Int(), input())
    print('Case #{}:'.format(i+1), result)