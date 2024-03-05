def f(n):
    s1 = bin(n)[2:]
    s2 = s1 + str(sum(map(int, s1)) % 2)
    s3 = s2 + str(sum(map(int, s2)) % 2)
    s4 = ''
    for c in s3:
        if c == '0':
            s4 += '1'
        else:
            s4 += '0'
    print(s3, s4)
    return int(s3, 2)


nums = []
for i in range(1, 1000):
    if f(i) > 48:
        nums.append(f(i))
print(min(nums))