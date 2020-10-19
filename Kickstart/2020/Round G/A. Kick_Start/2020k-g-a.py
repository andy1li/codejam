# 2020 Kickstart Round G - A. Kick_Start
# https://codingcompetitions.withgoogle.com/kickstart/round/00000000001a0069/0000000000414bfb

#------------------------------------------------------------------------------#

def solve(text):
    count = ans = 0
    for i in range(len(text)-4):
        if text[i:i+4] == 'KICK':
            count += 1
        elif text[i:i+5] == 'START':
            ans += count
    return ans

#------------------------------------------------------------------------------#

for i in range(int(input())):
    result = solve(input())
    print('Case #{}:'.format(i+1), result)