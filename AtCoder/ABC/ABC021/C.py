from collections import deque
n = int(input())
a, b = map(int,input().split())
a, b = a - 1, b - 1

m = int(input())
g = [[] for _ in range(n)]
for _ in range(m):
    x, y = map(int,input().split())
    g[x - 1].append(y - 1)
    g[y - 1].append(x - 1)

mod = 10 ** 9 + 7
q = deque([a])
INF = 10 ** 18
dist = [INF] * n
dist[a] = 0
dp = [0] * n
dp[a] = 1

while q:
    v = q.popleft()
    for i in g[v]:
        if dist[i] < dist[v] + 1: continue
        dp[i] += dp[v]
        dp[i] %= mod
        if dist[i] == dist[v] + 1: continue
        dist[i] = dist[v] + 1
        q.append(i)

print(dp[b])