def f(n):
    t = str(n)
    a = []
    for i in range(len(t) - 1):
        a.append(int(t[i] + t[i + 1]))
    mx = 0
    mn = 100
    for el in a:
        if el > mx:
            mx = el
        if el < mn:
            mn = el

    return mx + mn


print(f(2024))
