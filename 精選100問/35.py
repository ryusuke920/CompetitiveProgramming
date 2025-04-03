n, w = map(int, input().split())
v = [0] * n # 品物の価値
t = [0] * n # 重さ
for i in range(n):
    v[i], t[i] = map(int, input().split())
dp = [[0] * (w + 1) for _ in range(n + 1)] # （価値 * 重さ）
for i in range(n):
    for j in range(w + 1):
        if j < t[i]: # 追加できないとき
            dp[i + 1][j] = dp[i][j]
        else:
            dp[i + 1][j] = max(dp[i][j], dp[i][j - t[i]] + v[i])
print(dp[n][w])