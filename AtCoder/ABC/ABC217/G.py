from math import floor

n, m = map(int,input().split())
mod = 998244353
# dp[i][j] := 条件を満たしながらi人でj個のグループを作る
dp = [[0] * (n + 1) for _ in range(n + 1)]
dp[0][0] = 1

# iが一人でグループを作る場合 dp[i][j] += dp[i - 1][j - 1]
# それ以外だと (j - ⌊i-1 // M⌋)グループが適さない
# よって、 dp[i][j] += (j - ⌊i-1 // M⌋) * dp[i - 1][j]

for i in range(n):
    for j in range(n):
        dp[i + 1][j + 1] += dp[i][j] + dp[i][j + 1] * (j + 1 - floor(i / m))
        dp[i + 1][j + 1] %= mod

for i in range(n):
    print(dp[n][i + 1])