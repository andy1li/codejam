# 2019 Kickstart Round B - B. Energy Stones
# https://codingcompetitions.withgoogle.com/kickstart/round/0000000000050eda/00000000001198c3

Int   = lambda: int(input())
Ints  = lambda: [*map(int, input().split())]
Lines = lambda line, n_lines: [line() for _ in range(n_lines)]

#------------------------------------------------------------------------------#

def greedy(stone):
    secs, energy, lost = stone
    # return -(energy + lost*secs - sum(
    #     max(0, e-l*s) for s, e, l in stones
    # )) / secs, secs, -energy
    return energy, lost

def step(elapsed, stone):
    secs, energy, lost = stone
    return secs, max(0, energy-lost*elapsed), lost
  
def solve(n, stones):
    # print(n, stones)
    ans = sum( energy
        for _, energy, lost in stones
        if not lost 
    )
    stones = sorted(
        filter(lambda triple: triple[2], stones), key=greedy
    )
    
    while stones:
        secs, energy, lost = stones.pop()
        # print(secs, energy, lost)
        ans += energy
        stones = sorted(
            filter( lambda triple: triple[1], 
                map(lambda s: step(secs, s), stones)
            ), key=greedy
        )        
    return ans

#------------------------------------------------------------------------------#

for i in range(Int()):
    n = Int()
    stones = Lines(Ints, n)
    result = solve(n, stones)
    print('Case #{}:'.format(i+1), result)