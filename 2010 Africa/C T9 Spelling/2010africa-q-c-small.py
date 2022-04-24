# 2010 Africa Qualification Round - C. T9 Spelling
# http://code.google.com/codejam/contest/351101/dashboard#s=p2

import string

def build_map():
    #build a letter_to_digits map
    letter_to_digits = {}

    #a-o for 2-6
    digit = 2
    for i, letter in enumerate(string.lowercase[:15], start=0):
        #print letter, digit, i, i%3+1, digit+i/3
        letter_to_digits[letter] = (i%3+1)*str(digit+i/3)
    #pqrs for 7
    digit = 7
    for i, letter in enumerate(string.lowercase[15:19], start=1):
        letter_to_digits[letter] = i*str(digit)
    #tuv for 8
    digit = 8
    for i, letter in enumerate(string.lowercase[19:22], start=1):
        letter_to_digits[letter] = i*str(digit)
    #wxyz for 9
    digit = 9
    for i, letter in enumerate(string.lowercase[22:26], start=1):
        letter_to_digits[letter] = i*str(digit)

    letter_to_digits[' '] = '0'
    letter_to_digits['-'] = '-'

    return letter_to_digits


def solve(letters, map):
    # Build a map from letters to digits, and use it
    previous = '-'
    result = ''
    for letter in letters:
        # if (map[previous] in map[letter]) or
        #    (map[letter] in map[previous]):
        if map[previous][0] is map[letter][0]:
            result += ' ' + map[letter]
        else:
            result += map[letter]
        previous = letter
    
    return result


#input, solve and output:
input = open('C-large-practice.in', 'r')
output = open('l.out', 'w')

n_cases = int(input.readline())
for case in range(1, n_cases+1):
    # get rid of -1 without using strip, in case ' ' in the front 
    letters = input.readline()[:-1]
    l2d_map = build_map()
    #print l2d_map
    result = solve(letters, l2d_map)

    result_output = 'Case #%s: %s\n' %(case, result)
    print(result_output)
    output.write(result_output)

input.close()
output.close()
