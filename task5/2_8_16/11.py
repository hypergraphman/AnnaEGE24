def f(n):
    s1 = bin(n)[2:]
    k_1 = s1[1::2].count('1')
    k_0 = s1[0::2].count('0')
    return abs(k_1 - k_0)


k = 0
for n in range(1000, 5000 + 1):
    if f(n) >= 5:
        k += 1
print(k)