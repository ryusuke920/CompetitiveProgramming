from heapq import heappop, heappush, heapify

def prim(xy: list) -> int:
    g = [[] for _ in range(n)]

    # x座標が小さい順に並べてn - 1辺を張る
    xy.sort(key=lambda x: (x[0], x[1]))
    for i in range(n - 1):
        u, v, cost = xy[i][2], xy[i + 1][2], xy[i + 1][0] - xy[i][0]
        g[u].append((cost, v))
        g[v].append((cost, u))
    
    # y座標が小さい順に並べてn - 1辺を張る
    xy.sort(key=lambda x: (x[1], x[0]))
    for i in range(n - 1):
        u, v, cost = xy[i][2], xy[i + 1][2], xy[i + 1][1] - xy[i][1]
        g[u].append((cost, v))
        g[v].append((cost, u))

    visited = [False] * n
    connection = 0
    q = []
    q.append((0, 0))
    heapify(q)

    ans = 0
    while q:
        cost, v = heappop(q)
        if visited[v]: continue

        visited[v] = True
        connection += 1
        ans += cost

        for nxt in g[v]:
            heappush(q, nxt)
        
        if connection == n:
            break

    return ans

n = int(input())
xy = [(list(map(int, input().split())) + [i]) for i in range(n)]

print(prim(xy))