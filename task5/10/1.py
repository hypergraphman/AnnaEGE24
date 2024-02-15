def f(n):
    d1, d2, d3 = map(int, str(n))
    s1 = d1 + d2
    s2 = d2 + d3
    if s1 > s2:
        return str(s1) + str(s2)
    return str(s2) + str(s1)


for i in range(100, 1000):
    if f(i) == '145':
        print(i)