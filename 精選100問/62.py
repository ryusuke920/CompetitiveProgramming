from heapq import heappush, heappop

def dijkstra(s, graph):
    n = 10
    INF = 10 ** 18
    dist = [INF] * n
    dist[s] = 0
    q = [(0, s)]
    while q:
        v = heappop(q)[1]
        for i, j in graph[v]:
            if dist[i] <= dist[v] + j: continue
            dist[i] = dist[v] + j
            heappush(q, (dist[i], i))

    return dist

h, w = map(int,input().split())
g = [[] for _ in range(10)]
c = [list(map(int,input().split())) for _ in range(10)]

for i in range(10):
    for j in range(10):
        if i == j: continue
        g[i].append([j, c[i][j]])

a = [list(map(int,input().split())) for _ in range(h)]

ans = 0
for i in range(h):
    for j in range(w):
        if a[i][j] == -1: continue
        cnt = dijkstra(a[i][j], g)
        ans += cnt[1]

print(ans)