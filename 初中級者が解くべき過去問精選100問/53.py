from bisect import bisect_left
n = int(input())
a = [int(input()) for _ in range(n)]
INF = 10 ** 18
dp = [INF] * n
for i in a:
    x = bisect_left(dp, i)
    dp[x] = i
print(bisect_left(dp, INF))