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

n, Q = map(int,input().split())
g = [[] for _ in range(n)]
for _ in range(n - 1):
    a, b = map(int,input().split())
    g[a - 1].append((b - 1, 1))
    g[b - 1].append((a - 1, 1))

num_a = dijkstra(0, g)
#print("スタートから",num_a)
ma = max(num_a)
for i in range(n):
    if ma == num_a[i]:
        ind = i
        break

num_b = dijkstra(ind, g)
#print("最大から", num_b, ind)

for _ in range(Q):
    c, d = map(int,input().split())
    if num_a[c - 1] < num_a[d - 1]:
        x = num_a[d - 1]
        y = num_a[c - 1]
    else:
        x = num_a[c - 1]
        y = num_a[d - 1]        
    #print(i,x,y)
    if abs(y - x) % 2 == 0:
        print("Town")
    else:
        print("Road")