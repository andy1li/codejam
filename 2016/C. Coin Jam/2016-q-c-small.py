# 2016 Qualification Round - C. Coin Jam
# https://code.google.com/codejam/contest/6254486/dashboard#s=p2

def pad_num(s, width):
    diff = width - len(s)
    if diff <= 0:
        return s
    else:
        return '0'*diff + s

def make_coins(n):
    for i in range(2**(n-2)):
        inner = '{0:b}'.format(i)
        yield '1%s1' % (pad_num(inner, n-2))


def find_divisors(n):
    result = {n: []}
    
    for base in range(2, 11):
        num = int(n, base)
        magic_num = 11
        
        for i in range(2, magic_num+1):
            if num % i == 0:
                if i in result[n]:
                    continue
                else:
                    result[n].append(i)
                    #print n, 'in {:2d}'.format(base), '= {:16d}'.format(num), '% {:2d}'.format(i), '= {:1d}'.format(num%i)
                    break
    #print result
    return result

def is_real_coin(coin):
    divisor_dict = find_divisors(coin)
    
    for num, divisors in divisor_dict.items():
        if len(divisors) == 9:
            real_coin = [num]
            content = map(str, divisors)
            real_coin.extend(content)
            return ' '.join(real_coin)
        

def solve(n, j):
    real_coins = []
   
    for coin in make_coins(n):
        coin = is_real_coin(coin)
        if coin:
            real_coins.append(coin)
            if len(real_coins) >= j:
                return real_coins
    else:
        return real_coins


#input, solve and output:
file = 'foobar'
input = open(file+'.in', 'r')
output = open(file+'.out', 'w')

n_cases = int(input.readline())
for case in range(1, n_cases+1):
    (n, j) = [int(n) for n in input.readline().split()]
    results = solve(n, j)

    result_output = 'Case #%s:\n' %(case)
    
    for r in results:
        result_output += r + '\n'

    print(result_output)
    print(len(results))
    output.write(result_output)

input.close()
output.close()
