n = int(input())
p = list(map(int,input().split()))
dp = [[0] * (n * 100 + 1) for _ in range(n + 1)]
dp[0][0] = 1 # 可能なら1
for i, j in enumerate(p):
    for k in range(n * 100 + 1):
        dp[i + 1][k] = dp[i][k]
        if k >= j:
            dp[i + 1][k] = max(dp[i][k], dp[i][k - j])
print(sum(dp[n]))