# Qualification Round - A. Store Credit
# http://code.google.com/codejam/contest/351101/dashboard#s=p0

def solve(credit, items):
    # Brute force whether "a + b == credit" for a, b in list of items
    for i_a, a in enumerate(items, start=1):
        if a >= credit:
            continue
        for i_offset, b in enumerate(items[i_a:], start=1):
            if a + b == credit:
                #print credit, items
                #print a, b, i_a, i_offset
                i_b = i_a + i_offset
                return i_a, i_b

#input, solve and output:
input = open('A-large-practice.in', 'r')
output = open('l.out', 'w')

n_cases = int(input.readline())
for case in range(1, n_cases+1):
    credit = int(input.readline())
    n_items = int(input.readline())
    items = [int(n) for n in input.readline().split()]
    a, b = solve(credit, items)

    result_output = 'Case #%s: %s %s\n' %(case, a, b)
    print result_output
    output.write(result_output)

input.close()
output.close()
