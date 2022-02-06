from collections import deque

def bfs(s : int) -> list:
    'rからたどり着ける点かどうかでBFSを行う'
    q = deque()
    q.append(s)
    judge = [False] * n
    judge[s] = True
    while q:
        v = q.popleft()
        for i in bfs_g[v]:
            if judge[i]: continue
            judge[i] = True
            q.append(i)
    
    return judge

def bellman_ford(s: int) -> list:
    '負のコストを持つ最短経路問題'
    INF = 10 ** 18
    dist = [INF] * n
    dist[s] = 0
    for i in range(n):
        update = False # 経路更新を行ったか
        for a, b, cost in bellman_ford_g:
            if dist[b] > dist[a] + cost:
                dist[b] = dist[a] + cost
                update = True

        # 更新が行われなければそれが最短経路となる
        if not update:
            break

        if i == n - 1:
            return -1

    return dist

n, m, r = map(int, input().split())
std = [list(map(int, input().split())) for _ in range(m)]

# BFS
bfs_g = [[] for _ in range(n)]
for i in range(m):
    u, v, cost = std[i]
    bfs_g[u].append(v)

judge = bfs(r)

# ベルマンフォード
bellman_ford_g = []
for i in range(m):
    u, v, cost = std[i]
    if judge[u]:
        bellman_ford_g.append((u, v, cost))

ans = bellman_ford(r)

if ans == -1:
    print('NEGATIVE CYCLE')
else:
    for i in range(n):
        if ans[i] == 10 ** 18:
            print('INF')
        else:
            print(ans[i])