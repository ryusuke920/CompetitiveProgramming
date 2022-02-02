n = int(input())
a = list(map(int, input().split()))

# dp[i][j] := i日目に勉強をしたかどうか(j)とした時の実力の最大値
# 0 -> 勉強しない, 1 -> 勉強する
dp = [[0] * 2 for _ in range(n + 1)]
dp[1][1] = a[0]
# dp[i][0] = max(dp[i - 1][1], dp[i - 1][0])
# dp[i][1] = dp[i - 1][0] + a[i - 1]

for i in range(2, n + 1):
    dp[i][0] = max(dp[i - 1][1], dp[i - 1][0])
    dp[i][1] = dp[i - 1][0] + a[i - 1]

print(max(dp[-1]))