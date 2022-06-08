def bfs(now: int, d: int):
    global ans
    global g

    ans.add(now + 1)

    for nxt in g[now]:
        if d + 1 <= k:
            bfs(nxt, d + 1)


n, m = map(int, input().split())

g = [[] for _ in range(n)]
for _ in range(m):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    g[a].append(b)
    g[b].append(a)

for _ in range(int(input())):
    x, k = map(int, input().split())
    x -= 1
    ans = set()

    bfs(x, 0)
    
    print(sum(list(ans)))
