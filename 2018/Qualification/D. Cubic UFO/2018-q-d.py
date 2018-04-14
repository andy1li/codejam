# 2018 Qualification Round - D. Cubic UFO
# https://codejam.withgoogle.com/2018/challenges/00000000000000cb/dashboard/00000000000079cc

from math import pi, sin, cos
from typing import List, NamedTuple
from functools import reduce

def isclose(a, b, epsilon=1e-6):
    return abs(a-b) < epsilon

class Vector:
    def __init__(self, x=0, y=0, z=0):
        self.x = x
        self.y = y
        self.z = z

    def __eq__(self, other):
        return (
            type(self) == type(other) and
            all( isclose(a, b) for a, b in zip(self, other))
        )

    def __add__(self, other):
        return Vector(*( a+b for a, b in zip(self, other) ))

    def __mul__(self, other):
        if type(other) in [float, int]:
            return Vector(*( other*a for a in self))

        elif type(other) == type(self):
            return sum( a*b for a, b in zip(self, other))

    def __rmul__(self, other):
        return self.__mul__(other)

    def matmul(self, matrix):
        return Vector(*(
            Vector(*row) * self 
            for row in zip(*matrix)
        ))

    def __iter__(self):
        return iter([self.x, self.y, self.z])

    def __repr__(self):
        return ' '.join(map(str, [self.x, self.y, self.z]))

class Matrix(List):
    def squash(self):
        return [
            (v.x, v.z)
            for v in self
        ]

class Cube:
    def __init__(self, clock=0, up=0):
        self.faces = [Vector(x=0.5), Vector(y=0.5), Vector(z=0.5)]
        self.clock_turn(clock)
        self.up_turn(up)

    def __repr__(self):
        return str(self.faces)

    def clock_turn(self, radian) -> None:
        turn = [
            Vector(x=cos(radian), y=-sin(radian)), 
            Vector(x=sin(radian), y=cos(radian)), 
            Vector(z=1)
        ]
        self.faces = [
            face.matmul(turn)
            for face in self.faces
        ]

    def up_turn(self, radian) -> None:
        turn = [
            Vector(x=1),
            Vector(y=cos(radian), z=-sin(radian)),
            Vector(y=sin(radian), z=cos(radian))
        ]
        self.faces = [
            face.matmul(turn)
            for face in self.faces
        ]

    @property
    def vertices(self) -> Matrix:
        return Matrix([
            Vector(a1, a2, a3).matmul(self.faces)
            for a1 in (1, -1)
            for a2 in (1, -1)
            for a3 in (1, -1)
        ])

    @property
    def convex_hull(self):
        points = sorted(set(self.vertices.squash()))

        def cross(o, a, b):
            return (a[0] - o[0]) * (b[1] - o[1]) - (a[1] - o[1]) * (b[0] - o[0])

        # Build lower hull 
        lower = []
        for p in points:
            while len(lower) >= 2 and cross(lower[-2], lower[-1], p) <= 0:
                lower.pop()
            lower.append(p)

        # Build upper hull
        upper = []
        for p in reversed(points):
            while len(upper) >= 2 and cross(upper[-2], upper[-1], p) <= 0:
                upper.pop()
            upper.append(p)

        return lower[:-1] + upper[:-1]

    @property
    def shadow(self) -> float:
        def segments(hull):
            return zip(hull, hull[1:] + [hull[0]])

        hull = self.convex_hull

        return 0.5 * abs(sum(x0*y1 - x1*y0
                         for (x0, y0), (x1, y1) in segments(hull)))

def solve(a) -> List[Vector]:    
    if a <= 1.414213:
        lo, hi = 0., pi/4
        while not isclose(lo, hi, 1e-9):
            mid = (lo + hi)/2
            if Cube(mid).shadow > a:
                hi = mid
            else:
                lo = mid
        # print(Cube(hi).shadow, a)
        return Cube(hi).faces

    else:
        lo, hi = 0., 0.6154797086703875 # asin(1/sqrt(3)) 
        while not isclose(lo, hi, 1e-9):
            mid = (lo + hi)/2
            if Cube(pi/4, mid).shadow > a:
                hi = mid
            else:
                lo = mid
        # print(Cube(pi/4, hi).shadow, a)
        return Cube(pi/4, hi).faces

### Remember to delete tests and scaffolding before submission
assert all(a == b for a, b in zip(
    solve(1.0), [Vector(x=0.5), Vector(y=0.5), Vector(z=0.5)])
)

file  = open('sample.in')
input = file.readline

num_cases = int(input())
for case in range(1, num_cases+1):
    a = float(input())
    result = solve(a)

    print('Case #%s:' % case)
    for vector in result:
        print(vector)
    # print()

file.close()
