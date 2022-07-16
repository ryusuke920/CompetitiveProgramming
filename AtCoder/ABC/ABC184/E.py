import sys
input = sys.stdin.readline

from collections import defaultdict, deque

h, w = map(int, input().split())
a = [list(input()) for _ in range(h)]

d = defaultdict(list)
for i in range(h):
    for j in range(w):

        if a[i][j] == 'S':
            sy, sx = i, j

        if a[i][j] == 'G':
            gy, gx = i, j
        
        if a[i][j] == '.' or a[i][j] == '#':
            continue

        d[a[i][j]].append((i, j))

dist = [[-1] * w for _ in range(h)]
dist[sy][sx] = 0
q = deque()
q.append((sy, sx, a[sy][sx]))
D = ((1, 0), (-1, 0), (0, 1), (0, -1))

c = 'abcdefghijklmnopqrstuvwxyz'
alpha = set()
for i in c:
    alpha.add(i)

while q:

    vy, vx, grid = q.popleft()

    if grid in alpha:
        for dy, dx in d[grid][::-1]:

            d[grid].pop()

            if dist[dy][dx] != -1:
                continue

            dist[dy][dx] = dist[vy][vx] + 1

            q.append((dy, dx, a[dy][dx]))

    for dy, dx in D:
    
        y = vy + dy
        x = vx + dx

        if not (0 <= x < w and 0 <= y < h):
            continue

        if a[y][x] == '#':
            continue

        if dist[y][x] != -1:
            continue

        dist[y][x] = dist[vy][vx] + 1

        q.append((y, x, a[y][x]))

print(dist[gy][gx])