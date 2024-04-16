from collections import Counter


def f(n):
    if n < 2:
        return 1
    if n >= 2 and n % 5 == 0:
        return f(n // 5) + 5
    if n >= 2 and n % 5 != 0:
        return f(n - 3) + 5


a = []
for n in range(1, 100000 + 1):
    a.append(f(n))
c = Counter(a)
for el in c:
    if c[el] == 827:
        print(el)

# b = [0] * (max(a) + 1)
# for el in a:
#     b[el] += 1
#
# for i in range(len(b)):
#     if b[i] == 827:
#         print(i)