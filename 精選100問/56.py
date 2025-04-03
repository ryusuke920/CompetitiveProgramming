from heapq import heappush, heappop
v, e, r = map(int,input().split())
graph = [[] for _ in range(v)] # 今回の問題は有向グラフ
for i in range(e): # 入力を受け取る
    s, t, d = map(int,input().split())
    graph[s].append([t, d])

def dijkstra(s, n): # （始点・ノード数）
    dist = [10 ** 9] * n # 距離の初期値は∞
    check = [False] * n # ノードが確定済みかどうかを調べる
    dist[s] = 0 # スタート地点は距離が０
    q = [(0, s)] # （距離・ノード）
    while q:
        v = heappop(q)[1]
        check[v] = True
        for i, j in graph[v]: # (見る先のノード、距離)
            #if check[i] != False: continue # 既に調べてあるノードは調べない
            if dist[i] <= dist[v] + j: continue # 更新しても最小距離にならない場合は調べない
            dist[i] = dist[v] + j # 最小距離を更新
            heappush(q, [dist[i], i]) # 更新した先のノードと距離をqにpushする
    return dist # 全ての距離を返す

x = dijkstra(r, v)
for i in range(v):
    if x[i] == 10 ** 9: # 10 ** 9 のままの時は繋がっていないということなので、INF
        print('INF')
    else:
        print(x[i])