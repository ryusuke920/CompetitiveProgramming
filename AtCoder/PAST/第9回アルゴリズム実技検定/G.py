from collections import deque

n, Q = map(int, input().split())
g = [[0] * n for _ in range(n)]

for i in range(Q):
    t, u, v = map(int, input().split())
    u -= 1
    v -= 1
    if t == 1:
        if g[u][v] == 0:
            g[u][v] = 1
            g[v][u] = 1
        elif g[u][v] == 1:
            g[u][v] = 0
            g[v][u] = 0
    elif t == 2:
        q = deque()
        q.append(u)
        bool = [False] * n
        bool[u] = True
        while q:
            p = q.popleft()
            for i in range(n):
                if p == i: continue
                if bool[i]: continue
                if g[p][i] == 1:
                    bool[i] = True
                    q.append(i)

        if bool[v]:
            print('Yes')
        else:
            print('No')