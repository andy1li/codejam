# 2019 Qualification Round - D. Dat Bae
# https://codingcompetitions.withgoogle.com/codejam/round/0000000000051705/00000000000881de

import sys
from collections import defaultdict

def make(l, r, i):
    if done[l, r]: return
    mid = l+(r-l)//2
    if i: 
        make(l, mid, i-1)
        make(mid, r, i-1)
    else: 
        for i in range(l, mid): req[i] = '0'
        for i in range(mid, r): req[i] = '1'

def get_sep(l, r, res):
    mark = str(l)+'-'+str(r)
    # print('get_sep', mark, req[l:r], res, file=sys.stderr)
    if mark not in sep: 
        if res.find('1') != -1: sep[mark] = res.index('1')
        else:                   sep[mark] = res.rindex('0')+1
    # print('sep', mark, sep[mark], file=sys.stderr)
    return sep[mark]

def check(l, r, res, i):
    # print('#################### l, r', l, r, req[l:r], res, file=sys.stderr)

    if done[l, r]: return True
    if not len(res):
        done[l, r] = True
        for i in range(l, r): broken.add(i)
        return True

    if len(res) == 1 and (r-l) <= 2:        
        done[l, r] = True
        for i in range(l ,r):
            if req[i] != res: broken.add(i)
        return True

    mid = l+(r-l)//2
    sep = get_sep(l, r, res)

    if req[l:mid] == res[:sep]: done[l, mid] = True
    if req[mid:r] == res[sep:]: done[mid, r] = True

    if i: 
        return (
            (done[l, mid] or check(l, mid, res[:sep], i-1))
        and (done[mid, r] or check(mid, r, res[sep:], i-1))
        )
        # return check(req[:mid], , i-1) + check(req[mid+1:], i-1)
    else: 
        return '0'*mid + '1'*(l-mid)

    
for case in range(int(input())): 
    sep, done, broken = {}, defaultdict(bool), set() # type: ignore
    n, b, f = map(int, input().split())
    # print('\n', n, b, f, file=sys.stderr) # 6 3 10

    # if case == 1: sys.exit()

    for i in range(f):
        if i== 0: req = [-1] * n  
        req = list(req) # type: ignore
        make(0, n, i)
        req = ''.join(req) # type: ignore


        # print('\nreq:', req, i, file=sys.stderr)
        print(req, flush=True)
        res = input()
        if res == '1': break
        # print('res:', res, file=sys.stderr)


        check(0, n, res, i)
        # print('broken:', broken, done, file=sys.stderr)

        if len(broken) == b:
            print(*broken, flush=True)
            res = input()
            # print('res:', res, file=sys.stderr)
            # sys.exit()
            if res == '1': break
            else: sys.exit()

        # if case == 2 and i == 9: sys.exit()
    else:
        print(*[1]*b, flush=True)
        exit()

        

    