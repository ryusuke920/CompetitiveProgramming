n, m, k = map(int, input().split())
mod = 998244353
# dp[i][j] := A_i までの和が k であるような通り数
dp = [[0] * (n * m + 1) for _ in range(n + 1)]

for i in range(1, m + 1):
    dp[1][i] = 1

for i in range(1, n):
    for j in range(1, n * m + 1):
        for before in range(1, m + 1):
            if j - before >= 0:
                dp[i + 1][j] += dp[i][j - before]
                dp[i + 1][j] %= mod

ans = 0
for i in range(1, k + 1):
    ans += dp[n][i]
    ans %= mod
print(ans)