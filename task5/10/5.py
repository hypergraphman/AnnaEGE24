def f(n):
    t = str(n)
    s1 = 0
    for d in t:
        if int(d) % 2 == 0:
            s1 += int(d)
    # s1 = sum(map(int, filter(lambda d: int(d) % 2 == 0, str(n))))
    s2 = 0
    for d in t[1::2]:
        s2 += int(d)
    # s2 = sum(map(int, t[1::2]))
    return abs(s2 - s1)


for i in range(1, 10000000):
    if f(i) == 17:
        print(i)
        break


