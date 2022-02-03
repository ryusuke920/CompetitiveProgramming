n = int(input())
a, b, c = [0] * n, [0] * n, [0] * n
for i in range(n):
    a[i], b[i], c[i] = map(int,input().split())
dp = [[0] * 3 for _ in range(n + 1)]
for i in range(n):
    dp[i + 1][0] = a[i] + max(dp[i][1], dp[i][2])
    dp[i + 1][1] = b[i] + max(dp[i][0], dp[i][2])
    dp[i + 1][2] = c[i] + max(dp[i][0], dp[i][1])
print(max(dp[-1]))