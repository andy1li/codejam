# 2022 Round 1B - C. ASeDatAb
# https://codingcompetitions.withgoogle.com/codejam/round/000000000087711b/0000000000acd29b

# python interactive_runner.py python testing_tool.py 0 -- python 2022-1b-c.py

import sys

def attempt(n):
    return '1' * n + '0' * (8-n)

def run():
    n = 4
    for i in range(300):
        print(attempt(n))
        n = int(input())
        if n == 0: return
        if n == -1: sys.exit()    
    sys.exit()
    

for _ in range(int(input())):  
    run()
    # print('foo', file=jsys.stderr) 