from heapq import heappush, heappop
import sys # 入力高速化
input = sys.stdin.readline

def dijkstra(s, graph): # (始点, グラフのリスト)
    n = 10
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

h, w = map(int,input().split())
g = [[] for _ in range(10)]
c = [list(map(int,input().split())) for _ in range(10)]
for i in range(10):
    for j in range(10):
        if i == j: continue
        g[i].append([j, c[i][j]]) # 有向グラフ

a = [list(map(int,input().split())) for _ in range(h)]

ans = 0

for i in range(h):
    for j in range(w):
        if a[i][j] == -1: continue
        cnt = dijkstra(a[i][j], g)
        ans += cnt[1]

print(ans)