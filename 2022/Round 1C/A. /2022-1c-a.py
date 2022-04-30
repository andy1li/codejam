# 2022 Round 1C - A. Letter Blocks
# https://

import sys; sys.stdin = open('A. Letter Blocks/sample.in', 'r')


Int = lambda: int(input())
Ints = lambda: [*map(int, input().split())]

from collections import Counter, defaultdict
from copy import deepcopy
from functools import reduce
from itertools import chain, groupby

#------------------------------------------------------------------------------#

def check(p):
    condensed = (k for k, v in groupby(p))
    counts = Counter(condensed).values()
    return all(c == 1 for c in counts)

# def solve():
#     n = Int(); towers = input().split()
#     for p in map(''.join, permutations(towers)):
#         if check(p): return p
#     return 'IMPOSSIBLE'

# def trace(curr, tree):
#     tree = deepcopy(tree)
#     traced = [curr]
#     while curr in tree:
#         curr = tree[curr].pop()
#         traced.append(curr)
#     return traced

def split(towers):
    pures, nonpures = [], []
    for t in towers:
        if all(a == b for a, b in zip(t, t[1:])):
            pures.append(t)
        else:
            nonpures.append(t)
    return pures, nonpures

def agg(towers):
    starts, ends = defaultdict(set), defaultdict(set)
    for t in towers:
        starts[t[0]].add(t)
        ends[t[-1]].add(t)
    return starts, ends 

def solve():
    n = Int(); towers = input().split()
    if not all(map(check, towers)): return 'IMPOSSIBLE'

    count = reduce(lambda acc, x: acc + x, map(Counter, towers))

    pures, nonpures = split(towers)
    starts, ends = agg(nonpures)

    if (any(len(s) > 1 for s in starts.values()) 
     or any(len(e) > 1 for e in ends.values())):
        return 'IMPOSSIBLE'
    
     
    print(starts)
    print()
    print(ends)

    # parent, tree = defaultdict(set), defaultdict(set)
    # for t in towers:
    #     for a, b in zip(t, t[1:]):
    #         if a != b:
    #             tree[a].add(b)
    #             parent[b].add(a)
    
    # heads = [x for x in count if x not in parent]
    # if any(len(branch) >1 for branch in tree.values()) or not heads:
    #     return 'IMPOSSIBLE'

    # condensed = chain.from_iterable(trace(h, tree) for h in heads)
    # return ''.join(x * count[x] for x in condensed)

#------------------------------------------------------------------------------#

for i in range(Int()):
    result = solve()
    print('Case #{}:'.format(i+1), result)