from collections import deque
n, m = map(int,input().split())
a = [0] * n
b = [0] * n
graph = [[] for _ in range(n)]
for i in range(m):
    a[i], b[i] = map(int,input().split())
    graph[a[i] - 1].append(b[i] - 1)
    graph[b[i] - 1].append(a[i] - 1)
print(*graph)
now = 0
for i in range(m):
    dist = [10000] * n
    q = deque()
    if i != 0:
        q.append([a[0], b[0]])
        dist[a[0] - 1] = 0
        dist[b[0] - 1] = dist[a[0] - 1] + 1
    else:
        q.append([a[1], b[1]])
        dist[a[1] - 1] = 0
        dist[b[1] - 1] = dist[a[1] - 1] + 1
    if i == now: continue
    while q:
        q.popleft()
        if dist[q[0] - 1] != 10000: continue
        dist[q[0] - 1] = dist[q[1] - 1] + 1
        q.append(graph)