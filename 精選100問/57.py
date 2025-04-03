from heapq import heappush, heappop # ダイクストラ法はheapq
n, k = map(int,input().split())
graph = [[] for _ in range(n)] # ノード数の隣接行列
def dijkstra(s): # スタート地点
    dist = [10 ** 9] * n
    check = [False] * n
    q = [(0, s)] # 距離・ノード
    dist[s] = 0
    while q:
        v = heappop(q)[1] # 今いるノードを取り出す
        check[v] = True
        for i, j in graph[v]: # 先のノード・コスト
            if check[i] != False: continue # 既に調べ済みの場合はスルー
            if dist[i] <= dist[v] + j: continue # 更新しても無意味な場合はスルー
            dist[i] = dist[v] + j
            heappush(q, [dist[i], i])
    return dist # 配列をそのまま返す

for i in range(k):
    a = list(map(int,input().split()))
    if a[0] == 1:
        graph[a[1] - 1].append([a[2] - 1, a[3]]) # 隣接してるノード・コスト (0index)
        graph[a[2] - 1].append([a[1] - 1, a[3]]) # 隣接してるノード・コスト (0index)
    else: # a[0] == 0:
        x = dijkstra(a[1] - 1) # 0index
        if x[a[2] - 1] == 10 ** 9: # 更新されていなければ-1
            print(-1)
        else:
            print(x[a[2] - 1]) # 0index