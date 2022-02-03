h, w = map(int,input().split())
sy, sx = map(int,input().split())
gy, gx = map(int,input().split())
sy -= 1
sx -= 1
gy -= 1
gx -= 1
from collections import deque
q = deque()
q.append((sy, sx))
d = ((0, 1), (0, -1), (1, 0), (-1, 0))
INF = 10 ** 18
grid = [list(input()) for _ in range(h)]
dist = [[INF] * w for _ in range(h)]
dist[sy][sx] = 0
while q:
    vy, vx = q.popleft()
    for dy, dx in d:
        x = vx + dx
        y = vy + dy
        if not (0 <= x <= w - 1 and 0 <= y <= h - 1): continue
        if grid[y][x] == "#": continue
        if dist[y][x] != INF: continue
        dist[y][x] = dist[vy][vx] + 1
        q.append((y, x))

print(dist[gy][gx])