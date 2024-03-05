def two(s):
    if s.count('1') % 2 == 0:
        return s[1:]
    else:
        return '1' * s.count('1') + '1'


def f(n):
    s1 = bin(n)[2:]
    s2 = two(s1)
    s3 = two(s2)
    return int(s3, 2)


k = 0
for n in range(1, 1000 + 1):
    if f(n) == 7:
        k += 1
print(k)