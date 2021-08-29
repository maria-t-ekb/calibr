from math import sin, radians, cos


# obj =create(<a>)
# OBJ[href] = 'http://dsfsddfs'
# parent = root.find(...)
# parent.add_child(obj)
data = [
    [20, 33.2],
    [30, 22.2],
    [40, 16.6],
]
s=5
dmax = max(map(lambda row: row[0], data))

da = 0
for sector in data:
    da += sector[1]
    if sector[0] == dmax:
        da -= sector[1]/2
        break
print(da)
da = radians(da)

# da = radians(70)  # radians(data[0][1]/2)


def fxy(x, y):
    return (
        round(50+(x * cos(da) - y * sin(da))),
        round(50-(y * cos(da) + x * sin(da))))


x0, y0 = fxy(0, data[-1][0])
result = f'M {x0} {y0}\n'
angle = 0

for _ in range(s):
    for segment in data:
        x, y = fxy(
            segment[0] * sin(radians(angle)),
            segment[0] * cos(radians(angle)))
        result += f'L {x} {y}\n'
        angle += segment[1]
        x, y = fxy(
            segment[0] * sin(radians(angle)),
            segment[0] * cos(radians(angle)))
        result += f'A {segment[0]} {segment[0]} 0 0 1 {x} {y}\n'
print(result)

