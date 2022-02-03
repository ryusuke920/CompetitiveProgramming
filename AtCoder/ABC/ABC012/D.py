from heapq import heappush, heappop
n, m = map(int,input().split())
a = [0] * m
b = [0] * m
t = [0] * m
for i in range(m):
    a[i], b[i], t[i] = map(int,input().split())

graph = [[] for _ in range(n)] # 隣接行列
for i in range(m):
    graph[a[i] - 1].append([b[i] - 1, t[i]]) # 隣接してるノード・金額, 0index
    graph[b[i] - 1].append([a[i] - 1, t[i]]) # 隣接してるノード・金額, 0index

def dijkstra(s): # スタート地点
    q = [(s, 0)] # スタート地点・距離
    dist = [10 ** 9] * n
    dist[s] = 0 # スタート地点は0
    while q:
        v = heappop(q) # (今いるノード・そこまでに要した距離)
        if dist[v[0]] >= v[1]:
            for i, j in graph[v[0]]: # 隣接している先のノード・そこに行くまでに必要な金額
                if dist[i] <= v[1] + j: continue # 更新しても意味がない場合はスルー
                dist[i] = v[1] + j
                heappush(q, (i, dist[i])) # ノード・距離を追加
    return dist

ans = 10 ** 9
for i in range(n):
    x = dijkstra(i)
    ans = min(ans, max(x)) # 各ノードの最大値が一番小さいものが答えとなる
print(ans)