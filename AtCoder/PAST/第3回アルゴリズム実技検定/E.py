n, m, q = map(int,input().split())
g = [[] for _ in range(n)]
for _ in range(m):
    u, v = map(int,input().split())
    u -= 1
    v -= 1
    g[u].append(v)
    g[v].append(u)

c = list(map(int,input().split()))
for _ in range(q):
    s = list(map(int,input().split()))
    s[1] -= 1
    if s[0] == 1:
        print(c[s[1]])
        for i in g[s[1]]:
            c[i] = c[s[1]]
    elif s[0] == 2:
        print(c[s[1]])
        c[s[1]] = s[2]