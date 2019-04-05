# 2018 Kickstart Round G - A. Product Triplets
# https://code.google.com/codejam/contest/5374486/dashboard

from collections import defaultdict
from itertools import combinations
from typing import Dict, Set, Tuple

def solve(A):
    grouped: Dict[int, Set[int]] = defaultdict(set) 
    for i, x in enumerate(A):
        grouped[x].add(i)

    ans = set()
    for (ia, a), (ib, b) in combinations(enumerate(A), 2):
        for ic in grouped[a*b] - set([ia, ib]):
            ans.add( tuple(sorted([ia, ib, ic])) )
                
    return len(ans)

#------------------------------------------------------------------------------#

file = 'sample'
with open(file+'.in') as f_in, open(file+'.out', 'w') as f_out:
    input = f_in.readline
 
    for case in range(1, int(input())+1):
        _ = input()
        A = [*map(int, input().split())]
        result = solve(A)

        result_output = 'Case #%d: %s\n' % (case, result)
        print(result_output)
        f_out.write(result_output)
