n = int(input())
a = list(map(int,input().split()))
b = list(map(int,input().split()))

# dp[i][j] := i番目の数字Ciがjとしてあり得る数列の個数
dp = [[0] * 3002 for _ in range(n + 1)]
if n == 1: exit(print(b[0] - a[0] + 1))

for i in range(a[0], b[0] + 1): dp[1][i] += 1

for i in range(1, n):
    for j in range(3002):
        if dp[i][j] != 0 and j <= b[i]:
            dp[i + 1][max(a[i], j)] += dp[i][j]
            dp[i + 1][b[i] + 1] -= dp[i][j]

    for j in range(3001): dp[i + 1][j + 1] += dp[i + 1][j]
    for j in range(3002): dp[i + 1][j] %= 998244353
print((sum(dp[n])) % 998244353)