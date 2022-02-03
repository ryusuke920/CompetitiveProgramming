n = int(input())
a = list(map(int,input().split()))
dp = [[0] * 10 for _ in range(n + 1)]
dp[1][a[0]] = 1
mod = 998244353
for i in range(n - 1):
    for j in range(10):
        dp[i + 2][(j + a[i + 1]) % 10] += dp[i + 1][j]
        dp[i + 2][(j * a[i + 1]) % 10] += dp[i + 1][j]
    for j in range(10):
        dp[i + 2][j] %= mod

print(*dp[n], sep="\n")