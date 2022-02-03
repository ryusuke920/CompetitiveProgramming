n, a = map(int,input().split())
x = list(map(int,input().split()))
# dp[i][j][k] := i番目まででj枚を選んでkにできるかどうか
dp = [[[0] * 3000 for _ in range(55)] for _ in range(55)]
dp[0][0][0] = 1

for i in range(n):
    for j in range(n + 1):
        for k in range(n * a + 1):
            dp[i + 1][j][k] += dp[i][j][k]
            dp[i + 1][j + 1][k + x[i]] += dp[i][j][k]

ans = 0
for i in range(n):
    ans += dp[n][i + 1][a * (i + 1)]

print(ans)