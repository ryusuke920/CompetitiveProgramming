n, w = map(int,input().split())
vw = [list(map(int,input().split())) for _ in range(n)]
dp = [[0] * (w + 1) for _ in range(n + 1)]
# dp[i][j] := i番目までの荷物で重さがjのときの価値の最大値
for i in range(n):
    for j in range(w + 1):
        if j - vw[i][1] >= 0:
            dp[i + 1][j] = max(dp[i][j - vw[i][1]] + vw[i][0], dp[i][j])
        else:
            dp[i + 1][j] = dp[i][j]

print(dp[n][w])