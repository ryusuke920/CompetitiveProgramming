from bisect import bisect_left
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 6)
n = int(input())
a = list(map(int,input().split()))
g = [[] for _ in range(n)]
for i in range(n - 1):
    U, V = map(int,input().split())
    g[V - 1].append(U - 1)
    g[U - 1].append(V - 1)

INF = 10 ** 18
ans = [0] * n
dp = [INF] * n 
def dfs(v, p):
    x = bisect_left(dp, a[v])
    tmp = dp[x]
    dp[x] = a[v]
    ans[v] = bisect_left(dp, INF)
    for i in g[v]:
        if i == p: continue
        dfs(i, v)
    dp[x] = tmp # rallback

dfs(0, -1)

print(*ans, sep = "\n")