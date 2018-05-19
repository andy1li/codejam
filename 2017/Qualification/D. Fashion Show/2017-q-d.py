# 2017 Qualification Round - D. Fashion Show
# https://code.google.com/codejam/contest/3264486/dashboard#s=p3

from collections import defaultdict, OrderedDict
from typing import Dict, NamedTuple, Set

class Point(NamedTuple):
    type: str
    row : int
    col : int

    def __repr__(self):
        return f'{self.type} {self.row} {self.col}'

    def __hash__(self):
        return hash((self.row, self.col))

    def __eq__(self, other):
        return hash(self) == hash(self)

#------------------------------------------------------------------------------#

def parse_point() -> Point:
    type, row, col = input().split()
    return Point(type, int(row), int(col))

def print_grid(n, points) -> None:
    grid = [ ['.'] * n
        for _ in range(n)
    ]
    for p in points:
        grid[p.row-1][p.col-1] = p.type

    print('\n'.join(
        ''.join(row) for row in grid
    )); print()

def filter_type(points, type) -> Set[Point]:
    return set( Point(type, row, col)
        for t, row, col in points
        if t in [type, 'o']
    )

def split_diags(left_diags, right_diags):
    def odd(pair) : return pair[0] & 1
    def even(pair): return not odd(pair)
    def order(x)  : return OrderedDict( sorted(x, key=lambda pair: len(pair[1])) ) 

    even_left  = filter(even, left_diags.items())
    even_right = filter(even, right_diags.items())
    odd_left   = filter(odd, left_diags.items())
    odd_right  = filter(odd, right_diags.items())

    return map(order, [even_left, even_right, odd_left, odd_right])

def get_bishops(left_diags, right_diags) -> Set[Point]:
    res = set()
    for left_i, left_points in left_diags.items():
        for right_i, right_points in right_diags.items():
            commons = left_points & right_points
            if commons:
                res.add( Point('+', *commons.pop()) )
                right_diags.pop(right_i)
                break
    return res

def merge(pre_rooks, pre_bishops, rooks, bishops) -> Set[Point]:
    res = set()
    for rook in rooks:
        if rook in pre_bishops or rook in bishops:
            res.add( Point('o', rook.row, rook.col) )
        else:
            res.add( rook )
    for bishop in bishops:
        if bishop in pre_rooks or bishop in rooks:
            res.add( Point('o', bishop.row, bishop.col) )
        else:
            res.add( bishop )
    return res

def format_result(points, rooks, bishops) -> str:
    pre_rooks   = filter_type(points, 'x')
    pre_bishops = filter_type(points, '+')

    style_points = sum(map(len, [pre_rooks, pre_bishops, rooks, bishops]))
    res = merge(pre_rooks, pre_bishops, rooks, bishops)
    return '\n'.join([
        f'{style_points} {len(res)}',
        *map(str, res)
    ])

#------------------------------------------------------------------------------#

def solve_rooks(n, points) -> Set[Point]:
    rooks = filter_type(points, 'x')
    rows = set(range(1, n+1)) - set(r for _, r, _ in rooks)
    cols = set(range(1, n+1)) - set(c for _, _, c in rooks)
    return set(
        Point('x', row, col)
        for row, col in zip(rows, cols)
    )

def solve_bishops(n, points) -> Set[Point]:
    left_diags : Dict[int, set] = defaultdict(set)
    right_diags: Dict[int, set] = defaultdict(set)

    # fill up left_diags, right_diags
    for row in range(1, n+1):
        for col in range(1, n+1):
            left_diags[row-col].add((row, col))
            right_diags[row+col].add((row, col))

    # eliminations
    for _, row, col in filter_type(points, '+'): 
        if row-col in left_diags : left_diags.pop(row-col)
        if row+col in right_diags: right_diags.pop(row+col)

    even_left, even_right, odd_left, odd_right = split_diags(left_diags, right_diags)

    return get_bishops(even_left, even_right) | get_bishops(odd_left, odd_right)

def solve(n, points) -> str:
    # print(n, points); print_grid(n, points)
    rooks   = solve_rooks(n, points)  
    bishops = solve_bishops(n, points)
    # print_grid(n, rooks); print_grid(n, bishops)
    return format_result(points, rooks, bishops)

#------------------------------------------------------------------------------#

file = 'sample'
with open(file+'.in') as f_in, open(file+'.out', 'w') as f_out:
    input = f_in.readline
 
    for case in range(1, int(input())+1):
        n, m = map(int, input().split())
        points = set(
            parse_point()
            for _ in range(m)
        )
        result = solve(n, points)

        result_output = 'Case #%d: %s\n' % (case, result)
        print(result_output)
        f_out.write(result_output)
