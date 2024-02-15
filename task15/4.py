for A in range (45, 66):
    if all (not ((((x & 30 != 0) <= (x & 10 != 0)) or (x & A != 0)) <= ((x & 10 == 0) and (x & A == 0) and (x & 21 != 0))) for x in range (1, 1000)):
        print(A)