# 2018 Qualification Round - C. Go, Gopher! 
# https://codejam.withgoogle.com/2018/challenges/00000000000000cb/dashboard/0000000000007a30

from math import sqrt, ceil
from typing import List, Tuple
import sys

Hole = Tuple[int, ...]

class Orchard:
    def __init__(self, a):
        # TODO: need a better height/width calculation method
        self.height = int(sqrt(a))
        self.width = ceil(sqrt(a))
        self.grid = [[0] * self.width  
                     for _ in range(self.height)]

    def pick_target(self) -> Hole:
        '''Pick position with max count of unprepared neighbors'''
        count = [ 
            [0] * self.width
            for _ in range(self.height)
        ] 
        directions = [
            (-1, -1), (-1, 0), (-1, 1),
            ( 0, -1), ( 0, 0), ( 0, 1),
            ( 1, -1), ( 1, 0), ( 1, 1),
        ]

        for row in range(self.height):
            for col in range(self.width):
                # for unprepared cells
                if self.grid[row][col] == 0:
                    # increment neighbors' counts
                    for dr, dc in directions:
                        newr, newc = row+dr, col+dc
                        if self.is_valid(newr, newc):
                            count[newr][newc] += 1

        # pick pos w/ max count of unprepared neighbors
        row, col = max(( 
            (row, col)
            for row in range(self.height)
            for col in range(self.width)
            ),
            key=lambda pos: count[pos[0]][pos[1]]
        )

        # avoid borders to make a rect
        if row <= 0            : row +=1
        if col <= 0            : col +=1
        if row >= self.height-1: row -=1
        if col >= self.width-1 : col -=1

        return row+2, col+2

    def is_valid(self, row, col):
        return (
            0 <= row < self.height and
            0 <= col < self.width
        )

    def dig(self, target) -> Hole:
        print(*target, flush=True)
        return tuple(int(x) for x in input().split())

    def update(self, hole) -> None:
        row, col = (x-2 for x in hole)
        if self.is_valid(row, col):
            self.grid[row][col] = 1

    def run(self) -> None:    
        while True:
            target = self.pick_target() # crux of the problem
            hole   = self.dig(target)

            if   hole == ( 0,  0): return
            elif hole == (-1, -1): sys.exit()
            else                 : self.update(hole)

num_cases = int(input())
for case in range(1, num_cases+1):
    a = int(input())
    Orchard(a).run()

