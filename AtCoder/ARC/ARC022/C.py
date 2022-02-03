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

n = int(input())
g = [[] for _ in range(n)]
for i in range(n - 1):
    a, b = map(int,input().split())
    g[a - 1].append((b - 1, 1))
    g[b - 1].append((a - 1, 1))

x = dijkstra(0, g) # 0からスタート
#print(x)
ma = max(x)
for i, j in enumerate(x):
    if j == ma:
        start = i
        break

y = dijkstra(start, g)
ma = max(y)
for i, j in enumerate(y):
    if j == ma:
        end = i
        break

print(start + 1, end + 1)