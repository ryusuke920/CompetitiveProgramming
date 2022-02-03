from collections import deque
n, q = map(int,input().split())

graph = [[] for _ in range(n)]
for _ in range(n - 1):
    a, b = map(int,input().split())
    graph[a - 1].append(b - 1)
    graph[b - 1].append(a - 1)

cnt = [0] * n
for _ in range(q):
    p, x = map(int,input().split())
    cnt[p - 1] += x

q = deque()
q.append(0)
checked = [0] * n
while q:
    v = q.popleft()
    checked[v] = 1
    for i in graph[v]:
        if checked[i] != 0: continue
        cnt[i] += cnt[v]
        q.append(i)
print(*cnt, sep = '\n')