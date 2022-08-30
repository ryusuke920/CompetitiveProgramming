n = int(input())
a = list(map(int, input().split()))

mod = 998244353
modinv = lambda a : pow(a, mod - 2, mod)

dp = [0] * (n + 1)
for i in range(n - 2, -1, -1):
    cnt = 1 + (dp[i + 1] - dp[i + a[i] + 1]) * modinv(a[i] + 1)
    cnt %= mod
    cnt *= a[i] + 1
    cnt %= mod
    cnt *= modinv(a[i])
    cnt %= mod
    dp[i] = dp[i + 1] + cnt
    dp[i] %= mod

print(cnt)