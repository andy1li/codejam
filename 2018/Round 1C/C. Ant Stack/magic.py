from math import ceil

curr = acc = 1
lst = [1]

while acc < 6e9:
    if acc <= curr * 6:
        lst.append(curr)
        acc += curr
    else:
        curr = ceil(acc / 6)

print(acc-curr, acc)
print(len(lst), lst)
magic = len(lst)