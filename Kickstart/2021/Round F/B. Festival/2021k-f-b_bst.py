# 2021 Kickstart Round F - B. Festival
# https://codingcompetitions.withgoogle.com/kickstart/round/0000000000435bae/0000000000887dba

from collections import defaultdict
from sbbst import sbbst

Int = lambda: int(input())
Ints = lambda: [*map(int, input().split())]

#------------------------------------------------------------------------------#

def solve_bst(D, N, K):
    starts, ends = defaultdict(list), defaultdict(list)
    for _ in range(N):
        h, s, e = map(int, input().split())
        starts[s-1].append(h)
        ends[e].append(h)
            
    ans = curr = 0
    actives, subs = sbbst(), sbbst()
    for i in range(D+1):
        for h in starts[i]:
            try:actives.insert(h); curr += h
            except AttributeError:pass
            if actives.getSize() > K:
                sub = actives.getMinVal(); subs.insert(sub)
                actives.delete(sub); curr -= sub

        for h in ends[i]:
            if subs.search(subs.head, h): 
                subs.delete(h)
            else: 
                actives.delete(h); curr -= h
                if subs.getSize(): 
                    sub = subs.getMaxVal(); subs.delete(sub)
                    actives.insert(sub); curr += sub

        ans = max(ans, curr)
    return ans

#------------------------------------------------------------------------------#

for i in range(Int()):
    result = solve_bst(*Ints())
    print('Case #{}:'.format(i+1), result)