n = int(input())
a = [int(input()) for _ in range(n)]
dp = [1] * n
ans = 0
for i in range(n):
    for j in range(i):
        if a[j] < a[i]:
            dp[i] = max(dp[i], dp[j] + 1)
        ans = max(ans, dp[i])

print(ans)