from collections import deque
h, w = map(int,input().split())
grid = [list(input()) for _ in range(h)]
for i in range(h):
    if "s" in grid[i]:
        sy, sx = i, grid[i].index("s")
    if "g" in grid[i]:
        gy, gx = i, grid[i].index("g")

check = [[False] * w for _ in range(h)]
d = [[1, 0], [-1, 0], [0 ,1], [0, -1]]
q = deque()
q.append((sy, sx, 0))

while q:
    vy, vx, cnt = q.popleft()
    if cnt >= 3: continue
    check[vy][vx] = True
    if (vy, vx) == (gy, gx):
        exit(print("YES"))
    for dy, dx in d:
        (now_y, now_x) = (vy + dy, vx + dx)
        if not (0 <= now_y <= h - 1 and 0 <= now_x <= w - 1): continue
        if check[now_y][now_x] != False: continue
        if grid[now_y][now_x] == "#":
            q.append((now_y, now_x, cnt + 1))
        else:
            q.appendleft((now_y, now_x, cnt))
print("NO")