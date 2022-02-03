h, w = map(int,input().split())
grid = [list(input()) for _ in range(h)]

d = ((0, 1), (0, -1), (1, 0), (-1, 0))
for i in range(h):
    for j in range(w):
        if grid[i][j] != ".": continue
        now = [0] * 5
        for dy, dx in d:
            y = i + dy
            x = j + dx
            if not (0 <= x < w and 0 <= y < h): continue
            if grid[y][x] != ".":
                num = int(grid[y][x])
                now[num - 1] = 1
        for k in range(5):
            if now[k] == 0:
                grid[i][j] = k + 1
                break

for i in grid:
    print(*i, sep="")