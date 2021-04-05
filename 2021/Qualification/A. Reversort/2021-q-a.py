# 2021 Qualification Round - A. Reversort
# https://codingcompetitions.withgoogle.com/codejam/round/000000000043580a/00000000006d0a5c

Int = lambda: int(input())
Ints = lambda: [*map(int, input().split())]

#------------------------------------------------------------------------------#

def solve(n, A):
    ans = 0
    for i in range(n-1):
        j = i + A[i:].index(min(A[i:])) + 1
        slice = A[i:j]
        ans += len(slice)
        A = A[:i] + slice[::-1] + A[j:]
    return ans

#------------------------------------------------------------------------------#

for i in range(Int()):
    result = solve(Int(), Ints())
    print('Case #{}:'.format(i+1), result)