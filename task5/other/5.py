def f(n):
    a = []
    while n:
        a.insert(0, n % 20)
        n //= 20
    r = 0
    for d in a:
        r *= 20
        if d != 19:
            d += 1
        r += d
    return r


s = set()
for i in range(1, 100000 + 1):
    if 1000 <= f(i) <= 10000:
        s.add(f(i))
print(len(s))