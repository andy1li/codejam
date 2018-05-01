# Round 1B 2018 - B. Mysterious Road Signs 
# https://codejam.withgoogle.com/2018/challenges/0000000000007764/dashboard/000000000003675b

from collections import namedtuple
from typing import Tuple

Sign = namedtuple('Sign', ['n', 'm'])

Candidate = namedtuple('Candidate', ['candidate', 'n', 'm', 'start', 'switch'])

def parse_sign(line) -> Sign:
    d, a, b = map(int, line.split())
    return Sign(d-b, d+a)

def get_length(idx, n_can, m_can):
    return idx+1 - min(n_can.start, m_can.start)

def step(idx, sign_prev, sign_curr, this, other) -> Candidate:
    m_or_n = this.candidate

    if getattr(sign_curr, m_or_n) == getattr(sign_prev, m_or_n):
        return this
    elif getattr(sign_curr, m_or_n) == getattr(other, m_or_n):
        # if same m/n as the other side's m/n
        # keep (n/m, start) from the other side
        # mark the new switch point
        return other._replace(candidate=m_or_n, switch=idx)
    else:
        # new m/n candidate (sign_curr.m/n)
        # keep n/m from the other side
        # start = other.switch // start as left as possible
        # mark the new switch point
        return Candidate(
            m_or_n,
            m = sign_curr.m if m_or_n == 'm' else other.m,
            n = sign_curr.n if m_or_n == 'n' else other.n,
            start = other.switch,
            switch = idx
        )

def solve(s, signs): 
    # print(signs)
    if s == 1: return '1 1'

    max_len = 0
    num_max = 1

    for idx, (prev, curr) in enumerate(zip(signs, signs[1:]), start=1):
        # print(idx, prev, curr)
        if idx == 1:
            n_can = Candidate('n', *prev, 0, 0)
            m_can = Candidate('m', *prev, 0, 0)

        n_can, m_can = (
            step(idx, prev, curr, this=n_can, other=m_can),
            step(idx, prev, curr, this=m_can, other=n_can)
        )
        # print(n_can, '\n', m_can, '\n')

        length = get_length(idx, n_can, m_can)
        if length > max_len:
            max_len = length
            num_max = 1
        elif length == max_len:
            num_max += 1

    return ' '.join(map(str, [max_len, num_max]))

### Remember to delete tests and scaffolding before submission
file = open('sample.in')
input = file.readline

TEST_SIGNS = [Sign(n, m) for n, m in [
    (-1, 6), (-1, 8), (0, 7), (2, 8), (2, 8), (0, 9)
]]

num_cases = int(input())
for case in range(1, num_cases+1):
    s = int(input())
    signs = [
        parse_sign(input())
        for _ in range(s)
    ]
    result = solve(s, signs)
    # solve(6, TEST_SIGNS)

    output = 'Case #%s: %s' %(case, result)
    print(output)

file.close()