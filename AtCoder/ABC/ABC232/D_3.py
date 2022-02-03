from collections import deque

h, w = map(int, input().split())
c = [list(input()) for _ in range(h)]

q = deque()
INF = 10 ** 18
dist = [[INF] * w for _ in range(h)]
dist[0][0] = 1

q.append((0, 0))
d = ((0, 1), (1, 0))
while q:
    vy, vx = q.popleft()
    for dy, dx in d:
        y = vy + dy
        x = vx + dx
        if not (0 <= x < w and 0 <= y < h): continue
        if c[y][x] == '#': continue
        if dist[y][x] != INF: continue
        dist[y][x] = dist[vy][vx] + 1
        q.append((y, x))

ans = 0
for i in range(h):
    for j in range(w):
        if dist[i][j] == INF: continue
        ans = max(ans, dist[i][j])

print(ans)