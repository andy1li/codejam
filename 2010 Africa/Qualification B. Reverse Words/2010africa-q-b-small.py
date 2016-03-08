# Qualification Round - B. Reverse Words
# http://code.google.com/codejam/contest/351101/dashboard#s=p1

def solve(words):
    # Simply reverse the list of words
    words.reverse()
    return ' '.join(words)


#input, solve and output:
input = open('B-large-practice.in', 'r')
output = open('l.out', 'w')

n_cases = int(input.readline())
for case in range(1, n_cases+1):
    words = [n.strip() for n in input.readline().split()]
    result = solve(words)

    result_output = 'Case #%s: %s\n' %(case, result)
    print result_output
    output.write(result_output)

input.close()
output.close()
