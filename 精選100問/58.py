from heapq import heappop, heappush
from collections import deque
n, m, k, s = map(int,input().split()) # 町・道路・ゾンビに支配されてる町・s本以下でいける町
p, q = map(int,input().split()) # 危険でない宿の値段・危険な宿の値段
out = [] # 支配されている町を管理する配列
for i in range(k):
    x = int(input())
    out.append(x - 1) # 0index
graph = [[] for _ in range(n)]
for i in range(m):
    a, b = map(int,input().split())
    graph[a - 1].append(b - 1)
    graph[b - 1].append(a - 1)

def dfs(b):
    q = deque()
    q.append([b, 0]) # ノード・距離
    grid = [10 ** 18] * n
    grid[b] = 0 # ゾンビ地帯は0とする
    while q:
        v = q.popleft() # ノード・距離
        for i in graph[v[0]]:
            if grid[i] != 10 ** 18: continue # 既に調べ済みの場合は調べない
            grid[i] = v[1] + 1
            q.append([i, grid[i]]) # 新しく次のノードを追加する
    return grid # 配列ごとreturn

def dijkstra(a): # スタート地点
    q = [[0, a]] # 値段・ノード
    dist = [10 ** 18] * n
    dist[0] = 0 # スタートは0距離
    while q:
        v = heappop(q) # 今いる場所のノードを取り出す
        for i in graph[v[1]]: # 隣接しているノードを調べる
            if dist[i] <= v[0] + cost[i]: continue # 最小値を更新できなければ調べない
            if cost[i] == -1: continue # ゾンビ地帯はいけません
            if i == n - 1: # 最後の町では宿泊しない！！！問題文読もう！！！
                dist[i] = v[0]
            else: # それ以外は宿泊する！！！！
                dist[i] = v[0] + cost[i] # （新しいノードの値段） = （今いるノードの値段）＋（コスト）
            heappush(q, [dist[i], i]) # 値段・ノード
    return dist # 配列ごとreturn

expensive = [] # 安く宿泊できる場所, 0index
# 高い値段のノードを記録する
for i in range(len(out)):
    for j in graph[out[i]]:
        expensive.append(j)

cost = [0] * n # 各ノードの宿泊費
# ゾンビ地帯はいけません
for i in range(len(out)):
    cost[out[i]] = -1

# 危険な街は +q の値段
for i in range(len(out)):
    t = dfs(out[i])
    for j in range(n):
        if t[j] <= s and t[j] != 0 and cost[j] != -1: # s以下でいけてしまうものは危険地帯！！, 0のときはゾンビ地帯なので無視！
            cost[j] = q

# 安全な街は +p の値段
for i in range(n):
    if cost[i] == 0: # ゾンビ地帯でも危険地帯でもなければ 安全地帯 <=> +p
        cost[i] = p
cost[0] = 0 # スタート地点は0円でいけます

x = dijkstra(0) # スタート地点は0から
print(x[-1]) # 目指す街はNにある！