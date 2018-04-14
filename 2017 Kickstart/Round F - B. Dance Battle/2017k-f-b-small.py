# Kickstart Round F 2017 - B. Dance Battle
# https://code.google.com/codejam/contest/7254486/dashboard#s=p1

def solve(energy, n, arr):
    first = 0; last = n - 1 
    honor = 0

    for _ in range(n):
        # print(energy, arr[first: last+1], honor)
        if energy > arr[first]:
            energy -= arr[first]
            first += 1
            honor += 1 
        elif (energy + arr[last] > arr[first]
              and honor > 0
              and first < last):
            energy += arr[last]
            last -= 1
            honor -= 1

    return honor

#input, solve and output:
file = 'foobar'
input = open(file+'.in', 'r')
output = open(file+'.out', 'w')

t_cases = int(input.readline())
for case in range(1, t_cases+1):
    e, n = [int(x) for x in  input.readline().split()]
    arr = sorted(int(x) for x in input.readline().split())
    result = solve(e, n, arr)

    result_output = 'Case #%s: %s\n' %(case, result)
    print(result_output)
    # output.write(result_output)

input.close()
output.close()
