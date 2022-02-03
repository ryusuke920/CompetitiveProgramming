from collections import deque
n, Q = map(int,input().split())
g = [[] for _ in range(n)]
for _ in range(n - 1):
    a, b = map(int,input().split())
    g[a - 1].append(b - 1)
    g[b - 1].append(a - 1)

dist = [-1] * n
dist[0] = 0
q = deque([0])
while q:
    v = q.popleft()
    for i in g[v]:
        if dist[i] != -1: continue
        dist[i] = dist[v] + 1
        q.append(i)

for _ in range(Q):
    c, d = map(int,input().split())
    if abs(dist[c - 1] - dist[d - 1]) % 2 == 0:
        print("Town")
    else:
        print("Road")