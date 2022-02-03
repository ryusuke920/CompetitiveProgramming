import sys
sys.setrecursionlimit(10 ** 6)

n = int(input())
g = [[] for _ in range(n)]

for _ in range(n - 1):
    a, b = map(int,input().split())
    g[a - 1].append(b - 1)
    g[b - 1].append(a - 1)

for i in range(n):
    g[i].sort()

ans = []
def dfs(now: int, prev: int):
    ans.append(now + 1)
    for i in g[now]:
        if i != prev:
            dfs(i, now)
            ans.append(now + 1)

dfs(0, -1)

print(*ans)