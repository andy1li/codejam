# 2022 Qualification Round - B. 3D Printing
# https://codingcompetitions.withgoogle.com/codejam/round/0000000000876ff1/0000000000a4672b

Ints = lambda: [*map(int, input().split())]

#------------------------------------------------------------------------------#

def solve(printers):
    mins = [
        min(printers[p][c] for p in range(3)) 
        for c in range(4)
    ]
    if sum(mins) < 10**6: return 'IMPOSSIBLE'
    ans, needed = [], 10**6
    for i in range(4):
        use = min(mins[i], needed)
        needed -= use
        ans += use,
    return ' '.join(map(str, ans))

#------------------------------------------------------------------------------#

for i in range(int(input())):
    printers = [Ints() for _ in range(3)]
    result = solve(printers)
    print('Case #{}:'.format(i+1), result)