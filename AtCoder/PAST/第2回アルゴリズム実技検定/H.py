n, m = map(int, input().split())
a = [list(input()) for _ in range(n)]

g = [[] for _ in range(11)]
for i in range(n):
    for j in range(m):
        if a[i][j] == 'S':
            g[0].append((i, j))
        elif a[i][j] == 'G':
            g[10].append((i, j))
        else:
            g[int(a[i][j])].append((i, j))

for i in range(1, 10):
    if len(g[i]):
        continue
    exit(print(-1))

dp = [[10 ** 18] * m for _ in range(n)]
dp[g[0][0][0]][g[0][0][1]] = 0

for i in range(10):
    for prev_y, prev_x in g[i]:
        for nxt_y, nxt_x in g[i + 1]:
            cost = abs(prev_y - nxt_y) + abs(prev_x - nxt_x)
            dp[nxt_y][nxt_x] = min(dp[nxt_y][nxt_x], dp[prev_y][prev_x] + cost)

print(dp[g[-1][0][0]][g[-1][0][1]])