n, m = map(int, input().split())
h = list(map(int, input().split()))

g = [[] for _ in range(n)]
for _ in range(m):
    u, v = map(int, input().split())
    u -= 1
    v -= 1
    g[u].append(v)
    g[v].append(u)

INF = 10 ** 18
fun = [-INF] * n
fun[0] = 0

from collections import deque
q = deque()
q.append(0)
while q:
    v = q.popleft()
    for i in g[v]:
        if h[v] < h[i]:
            if fun[i] < fun[v] - 2 * (h[i] - h[v]):
                fun[i] = fun[v] - 2 * (h[i] - h[v])
                q.append(i)
        elif h[v] > h[i]:
            if fun[i] < fun[v] + (h[v] - h[i]):
                fun[i] = fun[v] + (h[v] - h[i])
                q.append(i)
        else:
            if fun[i] < fun[v]:
                fun[i] = fun[v]
                q.append(i)

print(max(fun))