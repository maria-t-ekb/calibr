from functools import reduce

s = '5 2 1 10'
a, b, c, d = map(int, s.split())
t = a + b + c

if t < d:
    r = t
else:
    r = t - d
print(r)
# r = t if t < d else d - t


s = '5 - 4 + 3 + 5'
arr = s.split()
r = None
op = None
for e in arr:
    if e in ('+', '-'):
        op = e
    elif e.isdecimal():
        if r is None:
            r = int(e)
        if op == '+':
            r += int(e)
        elif op == '-':
            r -= int(e)
print('expr', r)

s = '2 3 200 60 5'
q = sum(map(int, s.split()))
# q = a + b + c
print (q)
print(reduce(lambda x, y: x*y, map(int, s.split())))


def summ(s):
    return sum(map(int, s.split()))

s = '2 3 1', '4 5', '5 8', '5 54 765 43', '344 545 654'
print(*map(summ, s))
# d =
# h =
# a, b, c =
# d, e = map(int, d.split())
# p, f = map(int, h. split())
# r = a+b+c
# d = d+e
# h = p+f
# print (r, d, h)
# a, b = map(int, s.split())
# r = a + b
# print (r)
# print(eval(s))
