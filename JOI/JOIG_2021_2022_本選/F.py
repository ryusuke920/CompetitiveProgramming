from heapq import heappush, heappop
import sys
input = sys.stdin.readline

def dijkstra(graph: list):
    INF = 10 ** 18
    dist = [0] * n
    dist[0] = INF
    q = [0]
    while q:
        v = heappop(q)
        for color, nxt in graph[v]:
            if color == 1:
                if dist[nxt] < dist[v] - 1:
                    dist[nxt] = dist[v] - 1
                    heappush(q, nxt)
            elif color == 2:
                if dist[nxt] < dist[v] - dist[nxt] // 2:
                    dist[nxt] = dist[v] - dist[nxt] // 2
                    heappush(q, nxt)

    return dist

n, m, q, l  = map(int,input().split())
g = [[] for _ in range(n)]
for _ in range(m):
    a, b, color = map(int,input().split())
    a -= 1
    b -= 1
    g[a].append((color, b))
    g[b].append((color, a))

for _ in range(q):
    t = int(input())

d = dijkstra(g)
print(d)