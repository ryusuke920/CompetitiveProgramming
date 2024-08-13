import sys
input = sys.stdin.readline
sys.setswitchinterval(500_000)

def dfs(now: int, prev: int) -> None:
    ans.append(now)
    if now == N - 1:
        return -1
    for nxt in g[now]:
        if nxt == prev:
            continue
        t = dfs(nxt, now)
        if t == -1:
            return -1
    ans.pop()
    return 1

N = int(input())
g = [[] for _ in range(N)]
for _ in range(N - 1):
    a, b = map(lambda x: int(x) - 1, input().split())
    g[a].append(b)
    g[b].append(a)

ans = []
dfs(0, -1)
# print(ans)
l = [0]*N
for i in ans:
    l[i] = -1
fennec, snuke = len(ans)%2, 0

from collections import deque
q = deque()
q.append(0)
while q:
    v = q.popleft()
    for nxt in g[v]:
        if l[nxt] == 0:
            l[nxt] = 1
            q.append(nxt)
q.append(N - 1)
while q:
    v = q.popleft()
    for nxt in g[v]:
        if l[nxt] == 0:
            l[nxt] = 2
            q.append(nxt)
# print(l)

fennec += l.count(1)
snuke += l.count(2)
# print(fennec, snuke)
if fennec > snuke:
    print("Fennec")
else:
    print("Snuke")