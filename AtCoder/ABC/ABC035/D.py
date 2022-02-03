from heapq import heappush, heappop
import sys
input = sys.stdin.readline

def dijkstra(s: int, graph: list): # (始点, グラフのリスト)
    INF = 10 ** 18
    dist = [INF] * n # INF で初期化
    dist[s] = 0
    q = [(0, s)] # （距離・ノード）
    while q:
        v = heappop(q)[1] # 今いるノード
        for i, j in graph[v]: # 先のノード・距離
            if dist[i] <= dist[v] + j: continue
            dist[i] = dist[v] + j
            heappush(q, (dist[i], i))
    return dist

n, m, t = map(int, input().split())
a = list(map(int, input().split()))

g1 = [[] for _ in range(n)]
g2 = [[] for _ in range(n)]
for _ in range(m):
    x, y, cost = map(int,input().split())
    g1[x - 1].append((y - 1, cost))
    g2[y - 1].append((x - 1, cost))

d1 = dijkstra(0, g1)
d2 = dijkstra(0, g2)

ans = 0
for i in range(n):
    stay = max(0, t - d1[i] - d2[i])
    ans = max(ans, a[i] * stay)

print(ans)