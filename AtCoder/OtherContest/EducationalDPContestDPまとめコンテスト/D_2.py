n, W = map(int,input().split())
w, v = [0] * n, [0] * n
for i in range(n):
    w[i], v[i] = map(int,input().split())

# dp[i][j] := i番目までの荷物で重さがj以下になった時の最大値
dp = [[0] * (W + 1) for _ in range(n + 1)]
for i in range(n):
    for j in range(W + 1):
        if j - w[i] >= 0:
            dp[i + 1][j] = max(dp[i][j], dp[i][j - w[i]] + v[i])
        else:
            dp[i + 1][j] = dp[i][j]

print(dp[n][W])