# 2018 Practice Session - A. Number Guessing
# https://codejam.withgoogle.com/2018/challenges/0000000000000130/dashboard

import sys

def run(n, a, b) -> None:    
    sys.stderr.write(f'{n}, {a}, {b}\n')
    for _ in range(n):
        guess = (a+b) // 2
        print(guess, flush=True)
        res = input()
        sys.stderr.write(f'{guess} {res}\n')

        if res == 'TOO_SMALL':
            a = guess + 1
        elif res == 'TOO_BIG':
            b = guess - 1
        elif res == 'CORRECT':
            return

    sys.exit(-1)
    
num_cases = int(input())
for case in range(1, num_cases+1):
    a, b = map(int, input().split())
    n = int(input())
    run(n, a+1, b)

