# 2021 Kickstart Round A - C. Rabbit House
# https://codingcompetitions.withgoogle.com/kickstart/round/0000000000436140/000000000068cb14

from heapq import heappush, heappop, heapify
Ints = lambda: [*map(int, input().split())]

#------------------------------------------------------------------------------#

def prepare(grid):
    heap = [ (-hgt, i, j)
        for i, row in enumerate(grid)
        for j, hgt in enumerate(row)
    ]
    heapify(heap)
    return heap

def solve(r, c, grid):
    def neighbors(h, i, j): 
        for di, dj in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            ni, nj = i + di, j + dj
            if ((ni, nj) not in seen
            and (0 <= ni < r) and (0 <= nj < c)):
                yield -h+1, ni, nj

    ans, seen, heap = 0, set(), prepare(grid)
    while heap:
        h, i, j = heappop(heap)
        if (i, j) in seen: continue
        seen.add((i, j))

        if -h > grid[i][j]:
            ans += -h - grid[i][j]
            grid[i][j] = -h

        for neighbor in neighbors(grid[i][j], i, j):
            heappush(heap, neighbor) 

    return ans

#------------------------------------------------------------------------------#

for i in range(int(input())):
    r, c = Ints()
    grid = [Ints() for _ in range(r)]
    result = solve(r, c, grid)
    print('Case #{}:'.format(i+1), result)