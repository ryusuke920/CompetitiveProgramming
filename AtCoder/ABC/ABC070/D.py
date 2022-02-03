from collections import deque
n = int(input())
graph = [[] for i in range(n)]
dist = [-1] * n
for i in range(n - 1):
    a, b, c = map(int,input().split())
    graph[a - 1].append([b - 1, c]) # [頂点の番号・距離]
    graph[b - 1].append([a - 1, c]) # [頂点の番号・距離]
Q, k = map(int,input().split())

dist[k - 1] = 0
q = deque()
q.append(k - 1)
while q:
    v = q.popleft()
    for i, j in graph[v]:
        if dist[i] == -1:
            dist[i] = dist[v] + j
            q.append(i)

for i in range(Q):
    x, y = map(int,input().split())
    x, y = x - 1, y -1
    print(dist[x] + dist[y])