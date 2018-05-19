# 2018 Kickstart Round C - A. Planet Distance
# https://code.google.com/codejam/contest/4384486/dashboard#s=p0

from collections import defaultdict, deque
from graphviz import Graph
from typing import Dict, Set

def dfs_cycle(G, start) -> bool:
    parent = {start: None}
    visited = set(parent)
    queue = list(parent)

    # print('\nstart:', start)
    while queue:
        # print(visited, queue, parent)
        curr = queue.pop(); visited.add(curr) 
        # print(curr)

        for nxt in G[curr]:
            if nxt == start and parent[curr] != start: 
                # print(curr, nxt, parent, 'return True')
                return True
            if nxt not in visited:
                # print(curr, nxt, parent)
                queue.append(nxt)
                parent[nxt] = curr

    return False

def bfs_distance(G, cycle_members, start) -> int:
    if start in cycle_members: return 0

    distance = {start: 0}
    queue = deque(distance)

    while queue:
        curr = queue.popleft()
        
        for nxt in G[curr]:
            if nxt not in distance:
                queue.append(nxt)
                distance[nxt] = distance[curr] + 1
            if nxt in cycle_members: return distance[nxt]

    raise RuntimeError

def solve(n, G) -> str:
    cycle_members = set( x
        for x in range(1, n+1)
        if dfs_cycle(G, x)
    )
    print('G:', dict(G))
    print('cycle_members:', cycle_members)

    res = [ bfs_distance(G, cycle_members, x)
        for x in range(1, n+1)
    ]
    return ' '.join(map(str, res))

#------------------------------------------------------------------------------#

file = 'sample'
with open(file+'.in') as f_in, open(file+'.out', 'w') as f_out:
    input = f_in.readline
    for case in range(1, int(input())+1):
        n = int(input())
        G: Dict[int, Set[int]] = defaultdict(set)

        g = Graph()
        for _ in range(n):
            x, y = map(int, input().split())
            G[x].add(y)
            G[y].add(x)
            g.edge(str(x), str(y))
        # g.view()

        result = solve(n, G)
        result_output = 'Case #%d: %s\n' % (case, result)
        print(result_output)
        f_out.write(result_output)


