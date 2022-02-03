from heapq import heappush, heappop
import sys # 入力高速化
input = sys.stdin.readline

def dijkstra(s, graph): # (始点, グラフのリスト)
    INF = 10 ** 18
    dist = [INF] * n # INF で初期化
    check = [False] * n # Bool
    dist[s] = 0
    q = [(0, s)] # （距離・ノード）
    while q:
        v = heappop(q)[1] # 今いるノード
        if check[v]: continue # すでに行っていたらcontinue
        check[v] = True # 訪問済み
        for i, j in graph[v]: # 先のノード・距離
            if check[i] != False: continue
            if dist[i] <= dist[v] + j: continue
            dist[i] = dist[v] + j
            heappush(q, (dist[i], i)) # 必ず[0]が距離になるように（優先度付きキュー）
    return dist

n,m,k = map(int,input().split())
g = [[] for _ in range(n)]
for _ in range(m):
    u, v = map(int,input().split())
    g[u - 1].append((v - 1, 1))
    g[v - 1].append((u - 1, 1))

d = dijkstra(0, g)
print(d)