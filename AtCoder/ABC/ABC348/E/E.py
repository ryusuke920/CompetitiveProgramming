import sys
input = sys.stdin.readline
sys.setrecursionlimit(500_000)
from collections import deque

def dfs(now: int, prev: int) -> None:
    for nxt in g[now]:
        if nxt == prev:
            continue
        dfs(nxt, now)
        num[now] += num[nxt]

N = int(input())
g = [[] for _ in range(N)]
for _ in range(N - 1):
    A, B = map(lambda x: int(x) - 1, input().split())
    g[A].append(B)
    g[B].append(A)
C = list(map(int, input().split()))

q = deque([0])
INF = 10**18
dist = [INF]*N
dist[0] = 0
while q:
    v = q.popleft()
    for nxt in g[v]:
        if dist[nxt] == INF:
            dist[nxt] = dist[v] + 1
            q.append(nxt)

num = [1]*N
dfs(0, -1)
print(dist)
print(num)

is_check = [False]*N
is_check[0] = True
q = deque([0])
sum_ = sum(C)

cnt = 0
for i in range(N):
    cnt += dist[i]*C[i]

ans = [0]*N
ans[0] = cnt
while q:
    v = q.popleft()
    for nxt in g[v]:
        if is_check[nxt]:
            continue
        is_check[nxt] = True
        ans[nxt] = ans[v] + (sum_ * (num[v] - num[nxt]))
        q.append(nxt)

print(ans)
print(min(ans))