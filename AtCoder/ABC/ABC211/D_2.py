from collections import deque

n, m = map(int, input().split())
g = [[] for _ in range(n)]
for _ in range(m):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    g[a].append(b)
    g[b].append(a)

q = deque()
q.append(0)
mod = 10 ** 9 + 7
dist = [mod] * n
dist[0] = 0
cnt = [0] * n
cnt[0] = 1

while q:
    v = q.popleft()
    for i in g[v]:
        if dist[i] == mod:
            dist[i] = dist[v] + 1
            cnt[i] = cnt[v]
            q.append(i)
        elif dist[v] + 1 == dist[i]:
            cnt[i] += cnt[v]
            cnt[i] %= mod

print(cnt[n - 1])