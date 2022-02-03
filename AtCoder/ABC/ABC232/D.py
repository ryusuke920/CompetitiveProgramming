from collections import deque
h, w = map(int,input().split())

grid = [list(input()) for _ in range(h)]
INF = 10 ** 18
dist = [[INF] * w for _ in range(h)]
dist[0][0] = 1
q = deque()
q.append((0, 0))
while q:
    vy, vx = q.popleft()
    for dy, dx in ((1, 0), (0, 1)):
        Y, X = dy + vy, dx + vx
        if not (0 <= Y <= h - 1 and 0 <= X <= w - 1): continue
        if grid[Y][X] == '#': continue
        if dist[Y][X] != INF: continue
        dist[Y][X] = dist[vy][vx] + 1
        q.append((Y, X))

ans = 0
for i in range(h):
    for j in range(w):
        if dist[i][j] != INF:
            ans = max(ans, dist[i][j])

print(ans)