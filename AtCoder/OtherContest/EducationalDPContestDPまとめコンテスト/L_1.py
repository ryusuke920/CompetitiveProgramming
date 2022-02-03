n = int(input())
a = list(map(int,input().split()))
# dp[i][j] := i以上j未満の範囲をもらった時のX - Yの最大値 or 最小値
dp = [[0] * (n + 1) for _ in range(n + 1)]

# 幅の小さいものから埋めていく
for w in range(1, n + 1): # 幅(1 ~ N)
    for l in range(n - w + 1):
        r = l + w
        if w % 2 == n % 2: # 先手
            dp[l][r] = max(dp[l + 1][r] + a[l], dp[l][r - 1] + a[r - 1])
        else:
            dp[l][r] = min(dp[l + 1][r] - a[l], dp[l][r - 1] - a[r - 1])

print(dp[0][n])