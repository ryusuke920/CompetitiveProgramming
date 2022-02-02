from heapq import heappop, heappush, heapify

n, m = map(int,input().split())

g = [[] for _ in range(n)]
for _ in range(m):
    s, t, cost = map(int,input().split())
    g[s].append((cost, t))
    g[t].append((cost, s))

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

print(ans)