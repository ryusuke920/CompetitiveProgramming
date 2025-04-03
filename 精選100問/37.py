n, m = map(int,input().split())
c = list(map(int,input().split()))
dp = [10 ** 18] * (n + 1)
dp[0] = 0
for i in range(m):
    for j in range(n + 1):
        if j >= c[i]:
            dp[j] = min(dp[j], dp[j - c[i]] + 1)
print(dp[n])