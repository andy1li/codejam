# Kickstart Round F 2017 - D. Eat Cake
# https://code.google.com/codejam/contest/7254486/dashboard#s=p3

def get_min_dict():
    min_dict = {x**2: 1 for x in range(1, 101)}

    for i in range(2, 10001):
        if i not in min_dict:
            min_dict[i] = min(min_dict[j] + min_dict[i-j]
                              for j in range(1, i//2+1))

    # from pprint import pprint; pprint(min_dict)
    return min_dict

#input, solve and output:
file = 'foobar'
input = open(file+'.in', 'r')
output = open(file+'.out', 'w')

min_dict = get_min_dict()
t_cases = int(input.readline())
for case in range(1, t_cases+1):
    n = int(input.readline())    
    result = min_dict[n]

    result_output = 'Case #%s: %s\n' %(case, result)
    print(result_output)
    output.write(result_output)

input.close()
output.close()
