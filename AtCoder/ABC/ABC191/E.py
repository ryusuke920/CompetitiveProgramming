from heapq import heappush, heappop
import sys
input = sys.stdin.readline

n, m = map(int,input().split())
graph_true = [[] for _ in range(n)] # 問題通りの方向のやつ
graph_reverse = [[] for _ in range(n)] # 逆方向のやつ
same_saved = [[] for _ in range(n)] # 同じ街どうしを結ぶやつを保管しておく
same = [0] * n # 保管した中で最小のものを入れるやつ
for i in range(m):
    a, b, c = map(int,input().split())
    graph_true[a - 1].append((b - 1, c)) # ノード・距離
    graph_reverse[b - 1].append((a - 1, c)) # ノード・距離
    if a == b: # 同じ街を結ぶ場合
        same_saved[a - 1].append(c)

# 同じ街通しの最小値を考える
for i in range(n):
    cnt = 10 ** 18
    for j in range(len(same_saved[i])):
        cnt = min(cnt, same_saved[i][j])
    same[i] = cnt

def dijkstra(s, graph): # (始点, 正/逆方向の隣接リスト)
    dist = [10 ** 18] * n
    check = [False] * n
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
            heappush(q, (dist[i], i))
    return dist

for i in range(n):
    x = dijkstra(i, graph_true) # 問題文通り
    y = dijkstra(i, graph_reverse) # 逆回り
    ans = 10 ** 18
    for j in range(len(x)):
        if j == i: continue # j == i のときは 0, 代わりにsameでこの判定をしてる
        ans = min(ans, x[j] + y[j])
    ans = min(ans, same[i])
    if ans >= 10 ** 18:
        print(-1)
    else:
        print(ans)