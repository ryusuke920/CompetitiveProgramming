def dfs(graph: list, s: int):
    if len(graph[s]) == 0:
        return 1
    
    num = 1
    for i in graph[s]:
        num += dfs(g, i)
    
    return num

n = int(input())
p = list(map(int,input().split()))

g = [[] for _ in range(n)]
for i in range(n - 1):
    g[p[i]].append(i + 1)

for i in range(n):
    print(dfs(g, i))