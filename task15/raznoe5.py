for n in range(21, 92):
    if sum([(70 <= x <= 90) or (15 <= x <= 50) and (20 <= x <= n) for x in range(14, 92)]) > 35:
        print(n)
        break