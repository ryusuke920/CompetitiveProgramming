from functools import lru_cache

@lru_cache(maxsize=None)
def f(x: int) -> None:
    p = 0
    for i in range(1, 7):
        p += dp(x + i) / 6
    p += 1
    return p

K = int(input())
print(f(0))

dp = [0]*(K + 1)
dp[K] = 0
print(f(dp[0]))