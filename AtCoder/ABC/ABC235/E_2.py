from collections import defaultdict

a, n = map(int, input().split())

INF = 10 ** 18
d = defaultdict(lambda: INF)

def bfs(x: int, cnt: int):

    if d[x] <= cnt: return
    d[x] = cnt

    if x % a == 0:
        bfs(x // a, cnt + 1)
    
    if x >= 10:
        x = str(x)
        if int(x[1]) >= 1:
            t = x[0]
            x = x[1:] + t
            x = int(x)
            bfs(x, cnt + 1)

bfs(n, 0)
print(-1) if d[1] == INF else print(d[1])