#k_list = [d_list[0]/d for d in d_list]
#angle_mult = st / sum(k_list)
#for segment in d:
#    result += d[0]/segment[0]
#    print(result)
#print(angle_mult)

#for k in k_list:
#    sector_angle = k * angle_mult
#    print(sector_angle, round(sector_angle, 1))
d = [5]
s = 3

d.sort()
dnum = len(d)
centre = d.index(d[-2] if dnum % 2 else d[-1])
order = [*range(0, dnum, 2), *range(dnum - 1 - dnum % 2, 0, -2)]
d = [d[i] for i in order]


print(d)

result = 0
st = 360/s
print(st)

for segment in d:
    result += d[0] / segment
    print(result)

ts = st/result

for segment in d:
    y = d[0]/segment
    rty = ts*y
    print(rty, round(rty, 1))


#
print([
    *d[::2],
    *d[-1 - len(d) % 2: 0: -2]])
