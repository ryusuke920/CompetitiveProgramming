from functools import lru_cache

@lru_cache
def calc(x: int):
    if x <= 3:
        return x
    else:
        return calc(x // 2) * calc((x + 1) // 2) % 998244353

print(calc(int(input())))