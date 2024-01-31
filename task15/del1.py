for a in range(1, 1000):
    if all(((x % 45 == 0) or (x % 30 == 0)) <= (x % a == 0) for x in range(1, 100000)):
         print(a)

for a in range(1, 1000):
    is_a = True
    for x in range(1, 1000):
        d45 = x % 45 == 0
        d30 = x % 30 == 0
        da = x % a == 0
        if not ((d45 or d30) <= da):
            is_a = False
            break
    if is_a:
        print(a)
