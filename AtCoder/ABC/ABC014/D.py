from heapq import heappush, heappop

def dijkstra(s: int) -> list:
    INF = 10 ** 18
    dist = [INF] * n
    dist[s] = 0
    q = [(0, s)]
    while q:
        pre = heappop(q)[1]
        for nxt in g[pre]:
            if dist[nxt] < dist[pre] + 1: continue
            dist[nxt] = dist[pre] + 1
            heappush(q, (dist[nxt], nxt))

    return dist

n = int(input())

g = [[] for _ in range(n)]
for _ in range(n - 1):
    x, y = map(int,input().split())
    x -= 1
    y -= 1
    g[x].append(y)
    g[y].append(x)

d = dijkstra(0)
for i in range(int(input())):
    a, b = map(lambda x: int(x) - 1, input().split())
    print(d[a] + d[b] + 1)