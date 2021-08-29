s = '55 7 12'
a, b, c = map(int, s.split())
r = a - b * c

w = '50 30 10'
z, x, d = map(int, w.split())
t = z * x + d

p = '60 50 10'
l, k, j = map(int, p.split())
y = l * k / j

print(r, t, y)

q = '7 56'
p, o = map(int, q.split())

if p % 2:
    p += 1
if o % 2:
    o += 1

u = abs(o - p)
l = u / 2
print(l)

h = '367'
m = int(h)
p = None
a = 1
while a * a <= m:
    if m % (a * a) == 0:
        p = a * a
    a += 1
print(p)

x = '5 6 7'
x1, x2, x3 = map(int, x.split())
r = x1+x2+x3
print(r)


l1 = set(map(int,'9 4 5 2 7 11 13 12'.split()))
l2 = set(map(int,'6 8 16 1 3 10 9 15'.split()))
print(l1.intersection(l2))
