from heapq import heappop, heappush, heapify

n, m, k = map(int,input().split())

g = [[] for _ in range(n)]
for _ in range(m):
    u, v, cost = map(int,input().split())
    u -= 1
    v -= 1
    g[u].append((cost, v))
    g[v].append((cost, u))

visited = [False] * n
connection = 0
q = []
q.append((0, 0))
heapify(q)

ans = []
while q:
    cost, v = heappop(q)
    if visited[v]: continue

    visited[v] = True
    connection += 1
    ans.append(cost)

    for nxt in g[v]:
        heappush(q, nxt)
    
    if connection == n:
        break

ans.sort()
print(sum(ans[:n - k + 1]))