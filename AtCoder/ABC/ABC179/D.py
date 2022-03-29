n, k = map(int, input().split())
lr = [list(map(int, input().split())) for _ in range(k)]

mod = 998244353
dp = [0] * (n * 20)

dp[1] = 1
dp[2] = -1
for i in range(n):
    for l, r in lr:
        dp[i + l + 1] += dp[i + 1]
        dp[i + r + 2] -= dp[i + 1]
    dp[i + 2] += dp[i + 1]
    dp[i + 2] %= mod

print(dp[n])