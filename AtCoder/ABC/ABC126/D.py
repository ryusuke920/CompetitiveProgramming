from collections import deque

n = int(input())
g = [[] for _ in range(n)]
for _ in range(n - 1):
    u, v, w = map(int,input().split())
    g[u - 1].append((v - 1, w % 2))
    g[v - 1].append((u - 1, w % 2))

ans = [None] * n
ans[0] = 0
q = deque()
q.append(0)

while q:
    v = q.popleft()
    for next, dist in g[v]:
        if ans[next] == None:
            q.append(next)
            ans[next] = ans[v] ^ dist

print(*ans, sep="\n")