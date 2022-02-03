from collections import deque

h, w = map(int, input().split())
sy, sx = map(lambda x: int(x) - 1, input().split())
gy, gx = map(lambda x: int(x) - 1, input().split())

grid = []
for _ in range(h):
    for i in list(input()):
        grid.append(i)

q = deque()
q.append(sy * w + sx)
d = ((1, 0), (-1, 0), (0, 1), (0, -1))
dist = [-1] * h * w
dist[sy * w + sx] = 0
while q:
    v = q.popleft()
    for dy, dx in d:
        now = v + dy * w + dx
        if not 0 <= now < h * w: continue
        if dist[now] != -1: continue
        if grid[now] == '#': continue
        dist[now] = dist[v] + 1
        q.append(now)

print(dist[gy * w + gx])