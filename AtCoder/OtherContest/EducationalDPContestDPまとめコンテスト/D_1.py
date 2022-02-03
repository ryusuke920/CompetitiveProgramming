n, W = map(int,input().split())
w = [0] * n # 重さ
v = [0] * n # 価値
for i in range(n):
    w[i], v[i] = map(int,input().split())
dp = [[0] * (W + 1) for _ in range(n + 1)]
for i in range(n):
    for j in range(W + 1):
        if j < w[i]: # 小さい時は追加できないので１個前の品物の状態と同じにする
            dp[i + 1][j] = dp[i][j]
        else:
            dp[i + 1][j] = max(dp[i][j], dp[i][j - w[i]] + v[i])
print(dp[n][W])