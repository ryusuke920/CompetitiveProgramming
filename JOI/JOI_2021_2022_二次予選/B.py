from collections import deque

h, w = map(int, input().split())
grid = [input() for _ in range(h)]

q = deque()
q.append((0, 0))
dist = [[-1] * w for _ in range(h)]
dist[0][0] = 0
d = ((0, 1), (0, -1), (1, 0), (-1, 0))
while q:
    vy, vx = q.popleft()
    for dy, dx in d:
        y = vy + dy
        x = vx + dx
        if not (0 <= x < w and 0 <= y < h): continue
        if dist[y][x] != -1: continue
        if grid[y][x] == grid[vy][vx]: continue
        dist[y][x] = dist[vy][vx] + 1
        q.append((y, x))

print(dist[-1][-1])