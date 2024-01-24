for a in 0, 1:
    for b in 0, 1:
        f = int(a and b and not a and b or b)
        f2 = int(b)
        print(f, f2)