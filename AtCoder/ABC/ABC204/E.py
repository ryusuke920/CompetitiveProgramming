from heapq import heappush, heappop
import sys # 入力高速化
input = sys.stdin.readline
from math import floor

def dijkstra(s, graph): # (始点, グラフのリスト)
    INF = 10 ** 18
    dist = [INF] * n # INF で初期化
    check = [False] * n # Bool
    dist[0] = 0
    q = [(g[0][0][0], 0, g[0][0][2], g[0][0][3])] # （時刻・ノード, c, d）
    #print("q =",q)
    while q:
        a, b, c, d = heappop(q) # time, 今いるnode, c, d
        if check[b]: continue # すでに行っていたらcontinue
        check[b] = True # 訪問済み
        for i, j, k, l in graph[b]: # time, node, c, d
            #if check[j] != False: continue
            #print("dist[j] =", dist[j], "dist[b] = ", dist[b], "k =", k)
            if dist[j] <= i + k + floor(l / (i + 1)): continue
            dist[j] = i + k + floor(l / (i + 1))
            heappush(q, (dist[j], j, k, l)) # 必ず[0]が距離になるように（優先度付きキュー）
            print("q=",q)
    return dist

n, m = map(int,input().split())
g = [[] for _ in range(n)]
now = 0
for i in range(m):
    a,b,c,d = map(int,input().split())
    g[a - 1].append((0, b - 1, c, d))
    g[b - 1].append((0, a - 1, c, d))

if len(g[0]) == 0:
    exit(print(-1))
cnt = dijkstra(0, g)
if cnt[n - 1] == 10 ** 18:
    print(-1)
else:
    print(cnt[n - 1])
#print(cnt)