d = [20, 30, 40]
s = 20
v_tuple = 1, 2, 3, 4
v_list = [1, 2, 3, 4]
v_dict = {1: 'red', 2: 'green', 3: 'gray'}
v_set = {1,2,3}

if s == 20:
    print('20')
elif s == 30:
    print('30')
else:
    print('Something Else')

for i in range(10, 100, 10):
    print(f'i = {i}')
    continue
    break

# while True:
#     pass
def f(a,b,c):
    return a + b+ c

print(f(10,20,30))

for v in d:
    print(v/d[0])

print(len(d))

x = '3 5 7'
a, b, c = map(int, x.split())
cvb = a+b+c
print(cvb)

print(5)


s = '5 2 1 10'
a, b, c, d = map(int, s.split())
t = a + b + c

if t < d:
    r = t
else:
    r = t - d
print(r)