# 2019 Kickstart Round B - B. 
# https://

def solve(n, p, skills):
    psums = [sum(skills[:p])]
    for i, s in enumerate(skills[p:], start=p):
        psums.append( psums[-1]+s )
        psums[-1] -= skills[i-p]

    return min(
        p*skills[i] - psums[i-(p-1)] 
        for i in range(p-1, len(skills))
    )

#------------------------------------------------------------------------------#

for i in range(int(input())):
    n, p = map(int, input().split())
    skills = sorted(map(int, input().split()))
    result = solve(n, p, skills)
    print('Case #{}:'.format(i+1), result)