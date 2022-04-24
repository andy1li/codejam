# 2022 Qualification Round - E. Twisty Little Passages
# https://codingcompetitions.withgoogle.com/codejam/round/0000000000876ff1/0000000000a45fc0

# python interactive_runner.py python testing_tool.py 0 -- python 2022-q-e.py

import sys
from random import choices, randint, random
# import matplotlib.pyplot as plt

def run(n, k):
    def random_choice():
        c = randint(1, n)
        while c in seen:
            c = randint(1, n)
        return c

    teleports, seen = [], {}
    for i in range(k):
        r, p = map(int, input().split())
        seen[r] = p

        if i%2:
            print(f'T {random_choice()}')
        else:
            teleports += p,
            print('W')
    r, p = map(int, input().split())
    seen[r] = p

    simulated = list(seen.values()) + choices(teleports, k = n - len(seen))
    guess = int(sum(x/2 for x in simulated))
    # print(Counter(seen.values()), file=sys.stderr)
    # print('guess:', guess, file=sys.stderr)
    print(f'E {int(guess)}')
    # plt.hist(seen.values())    
    # plt.show()

for _ in range(int(input())): 
    n, k = map(int, input().split())
    # print('n, k:', n, k, file=sys.stderr)
    run(n, k)
    