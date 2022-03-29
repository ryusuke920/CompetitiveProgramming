from bisect import bisect_left

def LIS(A, N): # 配列・長さ
    INF = 10 ** 18
    dp = [INF] * N
    for i in A:
        x = bisect_left(dp, i)
        dp[x] = i
    return bisect_left(dp, INF)

n = int(input())
c = [int(input()) for _ in range(n)]

print(n - LIS(c, n))