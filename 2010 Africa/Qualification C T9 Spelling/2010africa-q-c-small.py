def build_map():
    pass

def solve(msg_in_letters):
    # ...
    previous = '-'
    result = ''
    return result


#input, solve and output:
input = open('B-large-practice.in', 'r')
output = open('l.out', 'w')

n_cases = int(input.readline())
for case in range(1, n_cases+1):
    # get rid of -1 without using strip, in case ' ' in the front 
    msg_in_letters = input.readline()[:-1]
    l2n_map = build_map()
    result = solve(msg_in_letters, l2n_map)

    result_output = 'Case #%s: %s\n' %(case, result)
    print result_output
    output.write(result_output)

input.close()
output.close()
