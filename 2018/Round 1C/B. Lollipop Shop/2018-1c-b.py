# Round 1C 2018 - B. Lollipop Shop 
# https://codejam.withgoogle.com/2018/challenges/0000000000007765/dashboard/000000000003e068

import sys
from collections import defaultdict
from typing import Dict

def run() -> None:    
    n = int(input())
    inventory = set(range(n))
    pref_history: Dict[int, int] = defaultdict(int)
    # pref_history = defaultdict(int)
   
    print('n:', n, file=sys.stderr) 
    for _ in range(n):
        d, *prefs = [*map(int, input().split())]
        print('d, prefs, inventory:', d, prefs, inventory, file=sys.stderr)
      
        if not d:
            sell = -1
        else:
            for p in prefs: pref_history[p] += 1
            print('pref_history:', dict(pref_history), file=sys.stderr)

            sell = min(
                (x for x in prefs
                   if  x in inventory),
                key=lambda x: pref_history[x],
                default=-1
            )
            inventory.discard(sell)

        print('sell:', sell, '\n', file=sys.stderr) 
        print(sell, flush=True)
    
num_cases = int(input())
for case in range(1, num_cases+1):
    run()
