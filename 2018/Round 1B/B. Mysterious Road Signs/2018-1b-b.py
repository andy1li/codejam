# Round 1B 2018 - B. Mysterious Road Signs 
# https://codejam.withgoogle.com/2018/challenges/0000000000007764/dashboard/000000000003675b

from collections import namedtuple
from typing import Tuple

Sign = namedtuple('Sign', ['n', 'm'])

Candidate = namedtuple('Candidate', ['n', 'm', 'switch', 'start'])

def parse_sign(line) -> Sign:
    d, a, b = map(int, line.split())
    return Sign(d-b, d+a)

def get_length(idx, n_can, m_can):
    return idx+1 - min(n_can.start, m_can.start)

def step(idx, sign_prev, sign_curr, n_prev, m_prev) -> Tuple[Candidate, Candidate]:
    if sign_curr.m == sign_prev.m:
        m_curr = m_prev
    elif sign_curr.m == n_prev.m:
        # keep n, m, start from the other candidate
        # switch = idx
        m_curr = n_prev._replace(switch=idx)
    else:
        # keep n from the other candidate
        # switch = idx   
        # set new m
        # start = other.switch // start as left as possible
        m_curr = n_prev._replace(switch=idx, m=sign_curr.m, start=n_prev.switch)

    if sign_curr.n == sign_prev.n:
        n_curr = n_prev
    elif sign_curr.n == m_prev.n:
        # keep n, m, start from the other candidate
        # switch = idx
        n_curr = m_prev._replace(switch=idx)
    else:
        # keep m from the other candidate
        # xstart = idx
        # set new n
        # start = other.switch // start as left as possible
        n_curr = m_prev._replace(switch=idx, n=sign_curr.n ,start=m_prev.switch)

    return n_curr, m_curr

def solve(s, signs): 
    # print(signs)
    if s == 1: return '1 1'

    max_len = 0
    num_max = 1

    for idx, (prev, curr) in enumerate(zip(signs, signs[1:]), start=1):
        # print(idx, prev, curr)
        if idx == 1:
            n_can = m_can = Candidate(*prev, 0, 0)

        n_can, m_can = step(idx, prev, curr, n_can, m_can)
        # print('n_can', n_can)
        # print('m_can', m_can, '\n')

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