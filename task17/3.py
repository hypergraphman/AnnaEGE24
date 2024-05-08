a = [int(x) for x in open('17.txt')]

# x = sum(a[1::2]) / len(a[1::2])
x = k = 0
for i in range(1, len(a), 2):
    x += a[i]
    k += 1
x = x / k

b = []
for t in zip(a, a[1:], a[2:]):
# for i in range(len(a) - 2):
#     p1, p2, p3 = t
    # sum(p > x for p in t) >= 2
    # if max(t) % 2 == 0 and (p1 > x) + (p2 > x) + (p3 > x) >= 2:
    if max(t) % 2 == 0 and sum(p > x for p in t) >= 2:
        b.append(max(t) - min(t))
print(len(b), max(b))