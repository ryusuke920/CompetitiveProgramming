from collections import deque

h, w = map(int,input().split())
s = [list(input()) for _ in range(h)]

INF = 10 ** 18
dist = [[INF] * w for _ in range(h)]

q = deque()
q.append((0, 0))
dist[0][0] = 0

# 破壊できるマスの設定
"""
↓イメージ図
.***.
*****
**P**
*****
.***.
P := 今いる位置(people)
"""

cost_0 = set([(-1, 0), (1, 0), (0, -1), (0, 1)])
cost_1 = set([
    (-2, -1), (-2, 0), (-2, 1),
    (-1, -2), (-1, -1), (-1, 1), (-1, 2),
    (0, -2), (0, 2),
    (1, -2), (1, -1), (1, 1), (1, 2), 
    (2, -1), (2, 0), (2, 1)
])

while q:
    vy, vx = q.popleft() # 今いる場所のy座標・x座標

    for dy, dx in cost_0:
        y = dy + vy
        x = dx + vx
        if not (0 <= x < w and 0 <= y < h): continue
        if s[y][x] == "#": continue
        if dist[y][x] <= dist[vy][vx]: continue

        dist[y][x] = dist[vy][vx]
        q.appendleft((y, x))

    for dy, dx in cost_1:
        y = dy + vy
        x = dx + vx
        if not (0 <= x < w and 0 <= y < h): continue
        if dist[y][x] <= dist[vy][vx] + 1: continue

        dist[y][x] = dist[vy][vx] + 1
        q.append((y, x))

print(dist[-1][-1])