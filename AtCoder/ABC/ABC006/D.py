from bisect import bisect_left
n = int(input())
c = [int(input()) for _ in range(n)]
INF = 10 ** 18
dp = [INF] * n
for i in c:
    x = bisect_left(dp, i)
    dp[x] = i
ans = bisect_left(dp, INF)
print(n  - ans)