from collections import deque
mod = 10 ** 9 + 7
N, M = map(int,input().split())
A, B = 0, N - 1

G = [[] for _ in range(N)]
for _ in range(M):
    x, y = map(int, input().split())
    G[x - 1].append(y - 1)
    G[y - 1].append(x - 1)

Q = deque()
Q.append(A)
dist = [N] * N
dist[A] = 0
Ans = [0] * N
Ans[A] = 1
while Q:
    now = Q.popleft()
    for to in G[now]:
        if dist[to] < dist[now] + 1:
            continue
        Ans[to] += Ans[now]
        Ans[to] %= mod
        if dist[to] == dist[now] + 1:
            continue
        dist[to] = dist[now] + 1
        Q.append(to)
print(Ans[B])