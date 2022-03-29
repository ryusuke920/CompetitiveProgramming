n = int(input())
mod = 998244353
dp = [[0] * 10 for _ in range(n + 1)]
# dp[i][j] := 上から i 桁目が j である場合の通り数

for i in range(1, 10):
    dp[1][i] = 1

for i in range(2, n + 1):
    for j in range(10):
        if j == 0:
            dp[i][0] = dp[i - 1][1]
        elif j == 9:
            dp[i][9] = dp[i - 1][8]
        else:
            dp[i][j] = dp[i - 1][j - 1] + dp[i - 1][j] + dp[i - 1][j + 1]
        dp[i][j] %= mod

ans = 0
for i in range(10):
    ans += dp[n][i]
    ans %= mod
print(ans)
#print(*dp, sep='\n')