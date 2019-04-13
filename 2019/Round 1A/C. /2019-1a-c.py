# 2019 Round 1A - C. Alien Rhyme 
# https://codingcompetitions.withgoogle.com/codejam/round/0000000000051635/0000000000104e05

# def count(trie):
#     # print(trie)
#     if trie['cnt'] > 1: 
#         return 2 + sum(count(trie[branch]) 
#             for branch in trie
#             if branch != 'cnt'
#         )
#     return 0

def prune(trie):
    # print(trie)
    if trie['cnt'] == 1: return 0
    leaves = sum(trie[branch]['cnt'] == 1 for branch in trie if branch != 'cnt')
    if leaves > 2: return trie['cnt'] - 2
    return sum(prune(trie[branch]) for branch in trie if branch != 'cnt')


def solve(words):
    trie = dict()
    for w in words:
        t = trie
        for letter in reversed(w):
            if letter not in t: t[letter] = {'cnt': 1}
            else:               t[letter]['cnt'] += 1
            t =  t[letter]

    
    for branch in trie: trie[branch]['cnt'] -= prune(trie[branch])

    from pprint import pprint
    # pprint(trie)

    return sum(trie[branch]['cnt']
        for branch in trie
        if trie[branch]['cnt'] > 1
    )

#------------------------------------------------------------------------------#

for i in range(int(input())):
    words = [input() for _ in range(int(input()))]
    result = solve(words)
    print('Case #{}:'.format(i+1), result)   