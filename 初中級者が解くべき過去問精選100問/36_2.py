n, W = map(int,input().split())
dp = [[0] * (W + 1) for _ in range(n + 1)] # 品物 * 重さ
v = [0] * n # 価値
w = [0] * n # 重さ
for i in range(n):
    v[i], w[i] = map(int,input().split())
for i in range(n):
    for j in range(W + 1):
        if j < w[i]:
            dp[i + 1][j] = dp[i][j]
        else:
            dp[i + 1][j] = max(dp[i][j], dp[i + 1][j - w[i]] + v[i], dp[i][j - w[i]] + v[i])
print(dp[n][W])