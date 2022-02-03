n, m = map(int,input().split())
a = list(map(int,input().split()))
g = [[] for _ in range(n)]
for i in range(m):
    A, B = map(int,input().split())
    g[A - 1].append(B - 1)

INF = 10 ** 18
dp = [INF] * n
ans = -INF
for i in range(n):
    ans = max(ans, a[i] - dp[i])
    for j in g[i]:
        dp[j] = min(dp[j], dp[i], a[i])
print(dp)
print(ans)