n, m = map(int,input().split())
a = list(map(int,input().split()))
b = list(map(int,input().split()))
INF = 10 ** 18
dp = [[INF] * (m + 1) for _ in range(n + 1)] # dp[i][j] := Aがi文字目まで、Bがj文字目までだった時の答え
for i in range(n):
    dp[i][0] = i
for i in range(m):
    dp[0][i] = i


for i in range(n):
    for j in range(m):
        if a[i] == b[j]:
            dp[i + 1][j + 1] = min(dp[i][j + 1], dp[i + 1][j], dp[i][j] - 1) + 1 # aを取り除く時, bを取り除く時
        else:
            dp[i + 1][j + 1] = min(dp[i][j + 1], dp[i + 1][j], dp[i][j]) + 1
print(dp[n][m])