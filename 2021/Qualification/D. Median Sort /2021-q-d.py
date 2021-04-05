# 2021 Qualification Round - D. Median Sort
# https://codingcompetitions.withgoogle.com/codejam/round/000000000043580a/00000000006d1284

# python interactive_runner.py python local_testing_tool.py 2 -- python 2021-q-d.py

import sys

def test(triple):
    print(*triple, flush=True)
    res = int(input())
    if res == -1: sys.exit()
    ends = [x for x in triple if x != res]
    return [ends[0], res, ends[1]]

def order(x, pair):
    triple = test(pair + [x])
    if [y for y in triple if x != y] != pair: triple.reverse()
    # print('tested:', *(f'[{x}]' if x == y else y for y in triple), file=sys.stderr)
    return triple, ['left', 'mid', 'right'][triple.index(x)]

def insert(A, x):
    lo, hi = 0, len(A)-1
    mid = hi // 2
    while lo < mid:
        # print('\n', 'lo, mid, hi:', lo, (lo + hi) // 2, hi, file=sys.stderr)
        # print('x, current:', x, A, file=sys.stderr)
        triple, pos = order(x, [A[lo], A[mid]])
        if pos == 'left': return A[:lo] + [x] + A[lo:]
        elif pos == 'right': lo = mid + 1
        elif lo+1 == mid: return A[:lo+1] + [x] + A[lo+1:]
        else: lo += 1; hi = mid - 1
        mid = (lo + hi) // 2

    lo = min(len(A)-2, lo)
    triple, _ = order(x, A[lo:lo+2])
    return A[:lo] + triple + A[lo+2:]
    
T, N, _ = map(int, input().split())
for _ in range(T):
    A = test([1, 2, 3])
    for x in range(4, N+1): A = insert(A, x)
    # print('final:', A, file=sys.stderr)
    print(*A, flush=True)
    if input() == '-1': sys.exit()
