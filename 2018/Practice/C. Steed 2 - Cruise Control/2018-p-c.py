# 2018 Practice Session - C. Steed 2: Cruise Control
# https://codejam.withgoogle.com/2018/challenges/0000000000000130/dashboard/0000000000000524

from typing import List, NamedTuple

class Horse(NamedTuple):
    start: int
    speed: int

    def time(self, destination):
        return (destination - self.start) / self.speed

def solve(destination: int, horses: List[Horse]) -> float:
    max_time = max(
        horse.time(destination)
        for horse in horses
    )
    return destination / max_time

### Remember to delete tests and scaffolding before submission
file  = open('sample.in')
input = file.readline

num_cases = int(input())
for case in range(1, num_cases+1):
    destination, n = map(int, input().split())
    horses = [
        Horse(*map(int, input().split())) 
        for _ in range(n)
    ]
    result = solve(destination, horses)

    output = 'Case #%s: %s' %(case, result)
    print(output)

file.close()
