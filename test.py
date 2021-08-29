def my_func(a=None, b=None, c=None):
    print('Hello World!')
    if a and b and a > b:
        print(f'a({a}) > b({b})')
    for i1 in 1, 2, 3, 4:
        print(f'i1={i1}')

    for i2 in range(a or 10):
        print(f'i2={i2}')


# my_func(15, 10)

s = '2 5'
a, b = map(int, s.split())
# s_list = s.split()
# a = int(s_list[0])
# b = int(s_list[1])

if a%2:
    a += 1

if b%2:
    b += 1

r = abs(a - b)

r /= 2

print(int(r))
