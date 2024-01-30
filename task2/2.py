print('x y z')
for x in 0, 1:
    for y in 0, 1:
        for z in 0, 1:
            f = x and y and z or y and not z and x or x and not y and not z
            if f:
                print(x, y, z)
