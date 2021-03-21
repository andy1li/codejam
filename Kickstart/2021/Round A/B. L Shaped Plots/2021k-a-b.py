# 2021 Kickstart Round A - B. L Shaped Plots
# https://codingcompetitions.withgoogle.com/kickstart/round/0000000000436140/000000000068c509

from collections import defaultdict
Ints = lambda: [*map(int, input().split())]

#------------------------------------------------------------------------------#

def intevels(r, c, grid):
    rows, cols = defaultdict(list), defaultdict(list)
    for i in range(r):
        start = -1
        for j in range(c):
            if grid[i][j]:
                if start == -1: start = j
            else:
                if start != -1: 
                    rows[i].append((start, j))
                    start = -1
        if start != -1: rows[i].append((start, c))

    for i in range(c):
        start = -1
        for j in range(r):
            if grid[j][i]: 
                if start == -1: start = j
            else:
                if start != -1: 
                    cols[i].append((start, j))
                    start = -1
        if start != -1: cols[i].append((start, r))

    return rows, cols

def junctions(rows, cols):
    for i, row in rows.items():
        for hor in row:
            if hor[1] - hor[0] < 2: continue
            for j in range(*hor):
                ver = next(ver for ver in cols[j] if ver[0]<=i<ver[1])
                if ver[1] - ver[0] < 2: continue
                # print(i, j, hor, ver)
                yield i-ver[0]+1, hor[1]-j, ver[1]-i, j-hor[0]+1

def count(nesw):
    nesw += nesw[0],
    return sum(
        max(0, min(a-1, b//2-1)) + max(0, min(b-1, a//2-1))
        for a, b in zip(nesw, nesw[1:])
    )

def solve(r, c, grid):
    rows, cols = intevels(r, c, grid)
    return sum(map(count, junctions(rows, cols)))

#------------------------------------------------------------------------------#

for i in range(int(input())):
    r, c = Ints()
    grid = [Ints() for _ in range(r)]
    result = solve(r, c, grid)
    print('Case #{}:'.format(i+1), result)