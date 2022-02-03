n, k = map(int, input().split())
a = list(map(int, input().split()))

mod = 10 ** 9 + 7
# dp[i][j] := i - 1番目までの人に飴をj個配るときの個数
dp = [[0] * (k + 1) for _ in range(n)]
for i in range(a[0] + 1):
    dp[0][i] = 1

for i in range(1, n):
    dp[i][0] = 1
    for j in range(1, k + 1):
        tmp = dp[i - 1][j]
        if j - 1 >= 0:
            tmp += dp[i][j - 1]
        if j - a[i] - 1 >= 0:
            tmp -= dp[i - 1][j - a[i] - 1]
        dp[i][j] = (tmp + mod) % mod

#print(*dp, sep='\n')
print(dp[n - 1][k] % mod)