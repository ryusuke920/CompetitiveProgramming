n = int(input())
a = list(map(int,input().split()))
ans = 0
mod = 10 ** 9 + 7
dp = [0] * (n + 1)
dp[0] = 1
dp[1] = 1
for i in range(2, n + 1):
    dp[i] = dp[i - 1] + dp[i - 2]
    dp[i] %= mod
#print(dp)
ans += a[0] * dp[-1]
for i in range(1, n):
    ans += a[i] * (dp[i] * dp[n - i] - dp[i - 1] * dp[n - i - 1])
    ans %= mod

print(ans)