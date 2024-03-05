def f(n):
    s1 = bin(n)[2:]
    for _ in range(2):
        if sum(map(int, s1)) % 2 == 0:
            s1 = s1[1:].lstrip('0')
        else:
            s1 = '1' + s1 + '00'
    return int(s1, 2)

print(f(5))