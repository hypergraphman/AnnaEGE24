for a in range(1, 1000):
    if all((3 * y + 5 * x > 95) or (2 * y + 7 * x > 100) or (y + 3 * x <= a) for x in range(1, 1000) for y in range(1, 1000)):
         print(a)
         break