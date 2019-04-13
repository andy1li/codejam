# 2019 Round 1A - C. Alien Rhyme 
# https://codingcompetitions.withgoogle.com/codejam/round/0000000000051635/0000000000104e05

def unpaired(trie):
    if not trie['nodes']: return 1

    r = sum(map(unpaired, trie['nodes'].values()))
    if 'end' in trie: r += 1
    if r >= 2: r -= 2
    return r

def solve(words):
    trie = {'nodes': {}}
    for word in words:
        t = trie
        for letter in reversed(word):
            if letter not in t['nodes']: t['nodes'][letter] = {'nodes': {}}
            t =  t['nodes'][letter]
        t['end'] = True

    return len(words) - sum(map(unpaired, trie['nodes'].values()))

#------------------------------------------------------------------------------#

for i in range(int(input())):
    words = [input() for _ in range(int(input()))]
    result = solve(words)
    print('Case #{}:'.format(i+1), result)   