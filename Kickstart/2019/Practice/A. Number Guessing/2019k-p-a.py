# 2019 Kickstart Practice - A. Number Guessing
# https://codingcompetitions.withgoogle.com/kickstart/round/0000000000051060/00000000000588f4

import sys

def run(n, a, b) -> None:    
    # print(f'{n}, {a}, {b}', file=sys.stderr)
    for _ in range(n):
        guess = (a+b) // 2
        print(guess, flush=True)
        res = input()
        # print(f'{guess} {res}', file=sys.stderr)

        if   res == 'TOO_SMALL': a = guess + 1
        elif res == 'TOO_BIG'  : b = guess - 1
        elif res == 'CORRECT'  : return

    sys.exit(-1)
    
num_cases = int(input())
for case in range(1, num_cases+1):
    a, b = map(int, input().split())
    n = int(input())
    run(n, a+1, b)

