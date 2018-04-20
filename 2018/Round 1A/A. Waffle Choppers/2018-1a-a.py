# Round 1A 2018 - Waffle Choppers 
# https://codejam.withgoogle.com/2018/challenges/0000000000007883/dashboard

from pprint import pprint
from typing import Union, List

def get_cuts(grid, num_chocos, num_cuts) -> Union[List[int], bool]:
    num_per_row = [
        sum(cell == '@' for cell in row) 
        for row in grid
    ]
    sub_target = num_chocos // (num_cuts+1) 
 
    piece_ends = []
    subtotal = 0
    for i, chocos in enumerate(num_per_row, start=1):
        subtotal += chocos
        if subtotal == sub_target:
            subtotal = 0
            piece_ends.append(i)
        if subtotal > sub_target:
            return False

    if len(piece_ends) == num_cuts+1: 
        return piece_ends
    else:
        return False

def get_pieces(grid, cuts_h, cuts_v):
    for start_r, end_r in zip([0]+cuts_h, cuts_h):
        rows = grid[start_r: end_r]

        for start_c, end_c in zip([0]+cuts_v, cuts_v):
            yield [
                row[start_c: end_c]
                for row in rows
            ]

def sum_chocos(piece: List[List[int]]) -> int:
    return sum(
        cell == '@' 
        for row in piece
        for cell in row
    )

def is_valid(grid, target, cuts_h, cuts_v) -> bool:
    return all(
        target == sum_chocos(piece)
        for piece in get_pieces(grid, cuts_h, cuts_v)
    )

def solve(r, c, h, v, grid) -> str: 
    # pprint(grid)
    num_chocos = sum_chocos(grid)
    num_pieces = (h+1) * (v+1)

    if num_chocos == 0: 
        return 'POSSIBLE'
    if num_chocos % num_pieces:
        return 'IMPOSSIBLE'

    # Find horizontal and vertical cuts
    cuts_h = get_cuts(grid, num_chocos, h)
    transposed = list(zip(*grid))
    cuts_v = get_cuts(transposed, num_chocos, v)
    if (not cuts_h or 
        not cuts_v or 
        not is_valid(grid, num_chocos//num_pieces, cuts_h, cuts_v)): 
        return 'IMPOSSIBLE'
    else:
        return 'POSSIBLE'

### Remember to delete tests and scaffolding before submission
answers = [
    'Case #1: POSSIBLE',
    'Case #2: IMPOSSIBLE',
    'Case #3: POSSIBLE',
    'Case #4: IMPOSSIBLE',
    'Case #5: POSSIBLE',
    'Case #6: IMPOSSIBLE'
]

file = open('sample.in')
input = file.readline

num_cases = int(input())
for case in range(1, num_cases+1):
    r, c, h, v = map(int, input().split())
    grid = [
        list(input().strip())
        for _ in range(r)
    ]
    result = solve(r, c, h, v, grid)

    output = 'Case #%s: %s' %(case, result)
    assert output == answers[case-1]
    print(output)

file.close()
