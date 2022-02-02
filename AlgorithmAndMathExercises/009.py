n, s = map(int, input().split())
a = list(map(int, input().split()))

# dp[i][j] := i番目までで合計をjにできるかどうか
dp = [[False] * (s + 1) for _ in range(n + 1)]
dp[0][0] = True
for i in range(n):
    for j in range(s + 1):
        if j - a[i] >= 0:
            dp[i + 1][j] |= dp[i][j - a[i]]
        dp[i + 1][j] |= dp[i][j]

print('Yes') if dp[n][s] else print('No')