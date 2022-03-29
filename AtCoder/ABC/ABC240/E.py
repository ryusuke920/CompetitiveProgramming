import sys
sys.setrecursionlimit(10 ** 6)

n = int(input())
g = [[] for _ in range(n)]
for _ in range(n - 1):
    u, v = map(lambda x: int(x) - 1, input().split())
    g[u].append(v)
    g[v].append(u)

LogN = 1
while 1 << LogN < n: 
    LogN += 1

depth = [0] * n
root = [[0] * n for _ in range(LogN)]

def dfs(now: int, prev: int):
    root[0][now] = prev
    for nxt in g[now]:
        if nxt == prev: continue
        depth[nxt] = depth[now] + 1
        dfs(nxt, now)

dfs(0, -1)

#print(depth)
for i in range(n):
    depth[i] += 1
 
ma = max(depth)
for i in range(n):
    print(depth[i], ma)