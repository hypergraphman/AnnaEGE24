from functools import lru_cache


@lru_cache(None)
def f(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    if n == 2:
        return 1
    if n > 2:
        return f(n - 1) + f(n - 2) + f(n - 3)


for i in range(13100):
    f(i)

print(f(13100))

