c = set()
for i in range(131, 3131 + 1):
    c.add(i - int(bin(i)[3:], 2))
print(len(c))