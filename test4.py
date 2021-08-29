ops = [
    ('x + 2', lambda x: x + 2),
    ('x + 3', lambda x: x + 3),
    ('x + 5', lambda x: x + 5),
    ('x * 2', lambda x: x * 2),
    ('x * 3', lambda x: x * 3),
    ('x * 5', lambda x: x * 5),
]

from itertools import permutations, combinations

for l in range(len(ops)):
    for seq in permutations(ops, l):
        res = 1
        for name, op in seq:
            res = op(res)
            print(name, res)
        print(res)
        if res == 49:
            exit()
