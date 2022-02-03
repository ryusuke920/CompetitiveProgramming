ax, ay, bx, by = map(int,input().split())
n = int(input())
# -1000 ~ 1000 -> 2001個
# 0 -> 1001 (0-indexed -> 1000)
h, w = 2001, 2001
grid = [[0] * w for _ in range(h)]

for _ in range(n):
    x, y = map(int,input().split())
    grid[y + 1000][x + 1000] += 1

