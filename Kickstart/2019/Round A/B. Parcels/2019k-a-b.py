# 2019 Kickstart Round A - B. Parcels
# https://codingcompetitions.withgoogle.com/kickstart/round/0000000000050e01/000000000006987d

from bisect import bisect_left
from collections import deque
from itertools import product

def bfs(r, c, grid):
    q, seen = deque(), set()
    for y, row in enumerate(grid):
        for x, val in enumerate(row):
            if val:
                q.append( (0, y, x) )
                seen.add( (y, x) )

    times = []
    while q:
        time, y, x = q.popleft()        
        times.append( (time, y, x) )
        for ny, nx in [(y-1,x), (y+1,x), (y,x-1), (y,x+1)]:
            if 0 <=ny<r and 0<=nx<c and ((ny, nx) not in seen):
                q.append( (time+1, ny, nx) )
                seen.add( (ny, nx) )

    return sorted(times, reverse=True)

def check(times, k):
    min_y, min_x = float('inf'), float('inf')
    max_y, max_x = -min_y, -min_x
    min_sum, min_dff = min_y, min_x
    max_sum, max_dff = max_y, max_x 

    for time, y, x in times:
        if time > k: 
            min_y, min_x = min(min_y, y), min(min_x, x)
            max_y, max_x = max(max_y, y), max(max_x, x)
            min_sum, min_dff = min(min_sum, y+x), min(min_dff, y-x)
            max_sum, max_dff = max(max_sum, y+x), max(max_dff, y-x)
        else: break

    sum_y, sum_x = min_y+max_y, min_x+max_x
    cand_y = [sum_y//2, sum_y//2 + 1] if sum_y % 2 else [sum_y//2]
    cand_x = [sum_x//2, sum_x//2 + 1] if sum_x % 2 else [sum_x//2]

    return min(
        max( 
            max( abs(y+x - sm), abs(y-x - df) )
            for sm, df in product([min_sum, max_sum], [min_dff, max_dff]) 
        ) 
        for y, x in product(cand_y, cand_x)
    ) <= k
    

def solve(r, c, grid):
    times = bfs(r, c, grid)
    class Possible: __getitem__ = lambda _, i: check(times, i)
    return bisect_left(
        Possible(), True, 
        0, max(triple[0] for triple in times)
    )

#------------------------------------------------------------------------------#

for i in range(int(input())):
    r, c = map(int, input().split())
    grid = (map(int, input()) for _ in range(r))
    result = solve(r, c, grid)
    print('Case #{}:'.format(i+1), result)