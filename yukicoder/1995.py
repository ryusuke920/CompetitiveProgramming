n, m = map(int, input().split())

g = [list(map(int, input().split())) for _ in range(m)]
g.sort(key=lambda x: (x[1], x[0]))

print(*g, sep='\n')

start, end = g[0][0], g[0][1]
ans = 1
for i in range(1, m):
    if end <= g[i][0]:
        start, end = g[i][0], g[i][1]
        ans += 1

print(2 * (n - 1) - ans)