n, x = map(int,input().split())
a = list(map(int,input().split()))

cnt = [0] * n
for i in reversed(range(n)):
    cnt[i] = x // a[i]
    x -= a[i] * cnt[i]

dp = [[10 ** 18] * 2 for _ in range(n + 1)]
dp[0][0] = 0
for i in range(n):
    dp[i + 1][0] = min(dp[i + 1][0], dp[i][0] + cnt[i], dp[i][1] + cnt[i] + 1)
    if i + 1 < n:
        dp[i + 1][1] = min(dp[i + 1][1], dp[i][0] + a[i + 1] // a[i] - cnt[i], dp[i][1] + a[i + 1] // a[i] - cnt[i] - 1)

print(min(dp[-1]))