from collections import deque

h, w = map(int,input().split())
s = [list(input()) for _ in range(h)]

"""
図示必須
.###.
#####
##P##
#####
.###.
"""

none_cost = ((0, 1), (0, -1), (1, 0), (-1, 0))
need_cost = set([
    (-2, -1), (-2, 0), (-2, 1), 
    (-1, -2), (-1, -1), (-1, 0), (-1, 1), (-1, 2), 
    (0, -2), (0, -1), (0, 1), (0, 2), 
    (1, -2), (1, -1), (1, 0), (1, 1), (1, 2), 
    (2, -1), (2, 0), (2, 1)
    ])

q = deque()
q.append((0, 0))
INF = 10 ** 18
dist = [[INF] * w for _ in range(h)]
dist[0][0] = 0

while q:
    vy, vx = q.popleft()
    for dy, dx in none_cost:
        y = vy + dy
        x = vx + dx
        if not (0 <= y < h and 0 <= x < w): continue
        if s[y][x] == "#": continue
        if dist[y][x] <= dist[vy][vx]: continue
        dist[y][x] = dist[vy][vx]
        q.appendleft((y, x))

    for dy, dx in need_cost:
        y = vy + dy
        x = vx + dx
        if not (0 <= y < h and 0 <= x < w): continue
        if dist[y][x] <= dist[vy][vx] + 1: continue
        dist[y][x] = dist[vy][vx] + 1
        q.append((y, x))

print(dist[-1][-1])