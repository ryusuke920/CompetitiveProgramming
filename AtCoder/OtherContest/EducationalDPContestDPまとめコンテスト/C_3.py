n = int(input())
dp = [[0] * 3 for _ in range(n + 1)]

for i in range(n):
    a, b, c = map(int,input().split())
    dp[i + 1][0] = max(dp[i][1], dp[i][2]) + c
    dp[i + 1][1] = max(dp[i][0], dp[i][2]) + b
    dp[i + 1][2] = max(dp[i][0], dp[i][1]) + a

print(max(dp[n]))