# 2021 Kickstart Round F - B. Festival
# https://codingcompetitions.withgoogle.com/kickstart/round/0000000000435bae/0000000000887dba

from collections import defaultdict, namedtuple
from bisect import insort_left

Int = lambda: int(input())
Ints = lambda: [*map(int, input().split())]
Lines = lambda line, n_lines: [line() for _ in range(n_lines)]

Attraction = namedtuple('Attraction', 'happy, start, end')

#------------------------------------------------------------------------------#

def solve_small(d, n, k, attractions):
    days = defaultdict(list)
    for a in attractions:
        a = a._replace(end = a.end+1)
        days[a.start].append(a)
        days[a.end].append(a)

    def start(a):
        nonlocal curr
        if len(actives) < k:
            insort_left(actives, a)
            curr += a.happy
        elif a.happy >= actives[0].happy:
            sub = actives.pop(0)
            insort_left(subs, sub)
            insort_left(actives, a)
            curr -= sub.happy
            curr += a.happy
        else:
            insort_left(subs, a)

    def end(a):
        nonlocal curr
        if a in subs: 
            subs.remove(a)
        if a in actives: 
            actives.remove(a)
            curr -= a.happy
            if subs: 
                sub = subs.pop()
                insort_left(actives, sub)
                curr += sub.happy
            
    actives, subs = [], []
    ans = curr = 0
    for day in sorted(days):
        for a in days[day]:
            if day == a.end: end(a)
            if day == a.start: start(a)
        ans = max(ans, curr)
    return ans

#------------------------------------------------------------------------------#

for i in range(Int()):
    d, n, k = Ints()
    attractions = Lines(lambda: Attraction(*Ints()), n)
    result = solve_small(d, n, k, attractions)
    print('Case #{}:'.format(i+1), result)