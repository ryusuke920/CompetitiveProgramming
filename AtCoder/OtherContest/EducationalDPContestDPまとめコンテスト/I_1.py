n = int(input())
p = list(map(float,input().split()))

# dp[i][j] := i番目までのコインを投げて、j枚表が出る確率
dp = [[0] * (n + 1) for _ in range(n + 1)]
dp[0][0] = 1

for i in range(1, n + 1):
    for j in range(1, n + 1):
        """
        i番目までで表がj - 1枚あって、i + 1枚目で表の確率
        i番目までで表がj枚あって、i + 1枚目で裏の確率
        """
        dp[i][j - 1] += dp[i - 1][j - 1] * (1 - p[i - 1]) # 裏の場合表の個数は変わらないから縦には遷移しない
        dp[i][j] += dp[i - 1][j - 1] * p[i - 1]

#print(*dp, sep = "\n")

ans = 0
for i in range((n + 1) // 2):
    ans += dp[n][(n + 1) // 2 + i]

print(ans)