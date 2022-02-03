a, b = map(int, input().split())
s = [list(input()) for _ in range(3)]

grid = [[False] * 9 for _ in range(9)]
grid[a - 1][b - 1] = True

d = []
for i in range(3):
    for j in range(3):
        if s[i][j] == '#':
            d.append((-1 + i, -1 + j))

from collections import deque
q = deque()
q.append((a - 1, b - 1))
while q:
    vy, vx = q.popleft()
    for dy, dx in d:
        y = dy + vy
        x = dx + vx
        if not (0 <= x < 9 and 0 <= y < 9): continue
        if grid[y][x]: continue
        grid[y][x] = True
        q.append((y, x))

ans = 0
for i in range(9):
    for j in range(9):
        if grid[i][j]: ans += 1

print(ans)