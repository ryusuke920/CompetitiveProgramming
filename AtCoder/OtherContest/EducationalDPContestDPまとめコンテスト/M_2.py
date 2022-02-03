n, k = map(int, input().split())
a = list(map(int, input().split()))

mod = 10 ** 9 + 7
# dp[i][j] := i - 1番目までの人に飴をj個配るときの個数
dp = [[0] * (k + 1) for _ in range(n)]
accum = [[0] * (k + 2) for _ in range(n)]

for i in range(a[0] + 1):
    dp[0][i] = 1

for i in range(1, n):
    for j in range(k + 1):
        accum[i - 1][j + 1] = (accum[i - 1][j] + dp[i - 1][j]) % mod
        dp[i][j] = (accum[i - 1][j + 1] - accum[i - 1][max(0, j - a[i])]) % mod

print(dp[-1][-1])