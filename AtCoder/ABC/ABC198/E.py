from sys import setrecursionlimit
setrecursionlimit(10 ** 9)
n = int(input())
c = list(map(int,input().split()))
graph = [[] for _ in range(n)]
for _ in range(n - 1):
    a, b = map(int,input().split())
    graph[a - 1].append(b - 1)
    graph[b - 1].append(a - 1)

ans = []
color = [0] * (10 ** 5 + 1)
def dfs(v, p): # 頂点・１個前（Boolの役割）
    color[c[v]] += 1
    if color[c[v]] == 1:
        ans.append(v + 1)
    for i in graph[v]:
        if i == p: continue
        dfs(i, v)
    color[c[v]] -= 1

dfs(0, -1)

ans.sort()
print(*ans, sep = "\n")